import logging
import re
from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum, auto
from importlib.resources import files
from pathlib import Path
from typing import Any, TypeVar, Union

import numpy as np
from ocelot import MagneticLattice
import ocelot.cpbd.elements as elements
import pandas as pd
import polars as pl
import yaml
from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements.optic_element import OpticElement
from ocelot.cpbd.match import match

from euxfel.complist import ComponentList
from euxfel.slicing import SlicedElement
from euxfel.writer import PythonSubsequenceWriter


# from .xfelt import EuXFELSimConfig, EuXFEL
# from .optics import START_SIM, MATCH_37, MATCH_52, INJECTOR_MATCHING_QUAD_NAMES

# from .astra import load_reference_0320_100k_distribution


# DEFAULT_CONVERSION_CONFIG_PATH = str(files("euxfel.longlists") / "conversion-config.toml")
DEFAULT_CONVERSION_CONFIG_PATH = str(files("euxfel.longlists") / "conversion-config.yaml")

logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

AnyTupT = tuple[Any, ...]
ElementT = TypeVar("ElementT", bound=OpticElement)

# SKIP_TYPE = ["BENDMARK", "RF", "CTBI", "CUX"]
# SKIP_CLASS = ["CRYO", "UNDPLACEH"]
SKIP_GROUP = [
    "CRYO",
    "VACUUM",
    "MOVER",  # "FASTKICK"
    "HKIC", # NAUGHTy
    "VKIC", # NAUGHTY
    "PHOTON",
    "DUMP",
    "CRYO"
]


TRACKING_CONF_NAME = "tracking-matched-conf.toml"
REAL_CONF_NAME = "real-matched-conf.toml"

@dataclass
class RowSkips:
    group: set[str] = field(default_factory=set)
    cls: set[str] = field(default_factory=set)
    type: set[str] = field(default_factory=set)
    name1: set[str] = field(default_factory=set)

@dataclass
class RowEdits:
    group: dict[str, Any] = field(default_factory=dict)
    cls: dict[str, Any] = field(default_factory=dict)
    type: dict[str,  Any] = field(default_factory=dict)

    def apply_changes(self, row: dict[str, Any]) -> None:
        row.update(self.group.get(row["GROUP"], {}))
        row.update(self.cls.get(row["CLASS"], {}))
        row.update(self.type.get(row["TYPE"], {}))


class AdjacentPositionType(Enum):
    BEFORE = auto()
    AFTER = auto()

@dataclass
class Placement:
    element: OpticElement

@dataclass
class AdjacentPlacement(Placement):
    before_after: AdjacentPositionType
    reference_name1: str

@dataclass
class OffsetPlacement(Placement):
    s: float
    reference_name1: str = ""

@dataclass
class MatchingRequest:
    marker_name: str
    quadrupoles: list[str]

@dataclass
class SubsequenceModule:
    start_marker_name1: str
    stop_marker_name1: str
    name: str
    sheet_name: str = "LONGLIST"
    extras: dict[str, dict[str, float | str]] = field(default_factory=dict)
    new_elements: dict[str, Placement] = field(default_factory=dict)
    matching: MatchingRequest | None = None


class ComponentListToOcelotConversionError(Exception):
    pass


class UnknownLongListElement(ComponentListToOcelotConversionError):
    pass


# class NewLatticeIO(LatticeIO):

class ExternalElementPlacer:
    def __init__(self, placements: dict[str, Placement]):
        self.adjacent_placements = defaultdict(list)
        self.offset_placements = defaultdict(list)
        self.global_placements = defaultdict(list)

        for name, placement in placements.items():
            ref_name1 = placement.reference_name1
            if isinstance(placement, OffsetPlacement):
                if not ref_name1:
                    self.global_placements[placement.s].append(placement)
                else:
                    self.offset_placements[ref_name1].append(placement)
            if isinstance(placement, AdjacentPlacement):
                self.adjacent_placements[ref_name1].append(placement)

    def get_elements_to_insert_in_range(self, s0: float, s1: float, element0: OpticElement, element1: OpticElement):
        # First we check adjacent_placements:
        append_element0: list[OpticElement] = []
        prepend_element1: list[OpticElement] = []
        for p in self.adjacent_placements[element0.id]:
            if p.before_after is AdjacentPositionType.AFTER:
                append_element0.append(p.element)
        for p in self.adjacent_placements[element1.id]:
            if p.before_after is AdjacentPositionType.BEFORE:
                prepend_element1.append(p.element)

        # Now we check global placements:
        between_elements: list[tuple[float, Placement]] = []
        for s, placements in self.global_placements.items():
            if s0 <= s <= s1:
                between_elements.append((s, placements))

        # now we check offset placements:
        for placement in self.offset_placements[element0.id]:
            s = placement.s
            if s >= 0:
                between_elements.append((s0 + element0.l + s, [placement]))

        for placement in self.offset_placements[element1.id]:
            s = placement.s
            if s <= 0:
                between_elements.append((s0 + s - element1.l * 0.5, [placement]))

        return append_element0, between_elements, prepend_element1

    # def s_elements_in_interval(
    #     self, s_start: float, s_stop: float
    # ) -> list[tuple[elements.Element, float]]:
    #     result = []
    #     for s_element in self.s_elements:
    #         s = s_element.s
    #         if s >= s_start and s < s_stop:
    #             result.append((elements.Element(eid=s_element.name), s))
    #     return result



class LongListConverter:
    ROUND_NDIGITS = 6  # For rounding to make drifts and other lenghts look nice.
    MINIMUM_DRIFT_LENGTH = 1e-6


    def __init__(self, clist: ComponentList, extra_properties=None,
                 rowskips: RowSkips | None = None,
                 rowedits: RowEdits | None = None
                 ):
        self.clist = clist
        self.extra_properties = extra_properties if extra_properties else {}
        # # to have unique drift names...
        self.rowskips: RowSkips = rowskips or RowSkips()
        self.rowedits: RowEdits = rowedits or RowEdits()

        self.drift_counter = 0

    @property
    def twiss0(self) -> Twiss:
        start = self.clist.longlist.iloc[0]
        t = Twiss()
        t.beta_x = start.BETX
        t.beta_y = start.BETY
        t.alpha_x = start.ALFX
        t.alpha_y = start.ALFY
        t.E = start.ENERGY
        return t

    def _round(self, value: float) -> float:
        return round(value, self.ROUND_NDIGITS)

    def convert_sections(self, sections: list[SubsequenceModule]) -> dict[str, tuple[Twiss, list[OpticElement]]]:
        self.drift_counter = 0
        result = {}
        for section in sections:
            self.drift_counter = 0
            try:
                result[section.name] = self.convert_section(section)
            # except ComponentListToOcelotConversionError as e:
            #     raise ComponentListToOcelotConversionError(
            #         f"Conversion failed in {section.name} in sheet {section.sheet_name}"
            #         ) from e
            except Exception as e:
                raise ComponentListToOcelotConversionError(
                    f"Conversion failed in {section.name} in sheet {section.sheet_name}"
                    ) from e

        return result

    def _filter_on_bad_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        bad_element_types = (
            pl.col("TYPE").is_in(self.rowskips.type)
            | pl.col("CLASS").is_in(self.rowskips.cls)
            | pl.col("GROUP").is_in(self.rowskips.group)
            | pl.col("NAME1").is_in(self.rowskips.name1)
        )

        # zero_length = pl.col("LENGTH") == 0
        # full_bad = bad_element_types & zero_length
        full_bad = bad_element_types

        skipped = df.filter(full_bad)

        # # equivalent to: if skipped_elements.LENGTH.abs().sum() > 0
        # if skipped.select(pl.col("LENGTH").abs().sum()).item() > 0:
        #     raise ValueError("Non-zero length elements are to be skipped")

        for n1, s, t, cls, grp in skipped.select("NAME1", "S", "TYPE", "CLASS", "GROUP").iter_rows():
            print(f"Skipping: NAME1 = {n1}, @ S = {s}, TYPE = {t}, CLASS = {cls}, GROUP = {grp}")

        return df.filter(~full_bad)

    def _shift_overlapping_correctors(self, df: pl.DataFrame) -> pl.DataFrame:
        return df
        # add a stable row id to define "first" vs "second"
        df = df.with_row_count("Index")

        thick = df.filter(pl.col("LENGTH") != 0)

        dup_counts = (
            thick.group_by("S")
            .agg(pl.len().alias("cnt"))
            .filter(pl.col("cnt") > 1)
        )

        if not dup_counts.is_empty():
            from IPython import embed; embed()


        # keep the same assertion semantics (expects exactly 2)
        bad = dup_counts.filter(pl.col("cnt") != 2)
        if bad.height > 0:
            raise ValueError("Expected exactly 2 thick elements per duplicated S")

        dup_s = dup_counts.select("S")

        # position within each S-group (in original row order)
        pos_in_s = pl.int_range(0, pl.len()).over("S")

        df2 = df.with_columns(
            pos_in_s.alias("_pos_in_s"),
            pl.col("S").is_in(dup_s["S"]).alias("_is_dup_s"),
        ).with_columns(
            pl.when((pl.col("_is_dup_s")) & (pl.col("LENGTH") != 0) & (pl.col("_pos_in_s") == 1))
            .then(pl.col("S") + pl.col("LENGTH") * 0.5)
            .otherwise(pl.col("S"))
            .alias("S")
        )

        return df2.drop(["Index", "_pos_in_s", "_is_dup_s"])

    def _filter_bad_entries(self, df: pd.DataFrame) -> pd.DataFrame:
        """Filter bad/nonsensical columns from the DataFrame,
        e.g.:
         * elements with negative S
         * elements with irrelevant types (that also have no length)
         * Markers that are inside other elements

        """
        neg_s = df.filter(pl.col("S") < 0)

        for name1, s in neg_s.select("NAME1", "S").iter_rows():
            LOG.warning(f"Dropping element with negative S: {name1 = }, {s = }")

        df = df.filter(pl.col("S") >= 0)
        df = self._filter_on_bad_columns(df)

        # "markers" (zero length) that are inside other elements
        thin = df.filter(pl.col("LENGTH") == 0).select(["NAME1", "S", "LENGTH"])

        starts = (df["S"] - df["LENGTH"] * 0.5).to_numpy()
        stops  = (df["S"] + df["LENGTH"] * 0.5).to_numpy()

        bad_name1s: list[str] = []
        for row in thin.iter_rows(named=True):
            s = row["S"]
            is_inside = ((s > starts) & (s < stops)).any()
            if is_inside:
                LOG.warning(
                    f"Dropping bad row inside other element: {row['NAME1']}"
                )
                bad_name1s.append(row["NAME1"])
                assert row["LENGTH"] == 0.0

        df_no_bad = df.filter(~pl.col("NAME1").is_in(bad_name1s))

        return self._shift_overlapping_correctors(df_no_bad)

    def convert_section(self, pysec: SubsequenceModule) -> tuple[Twiss, list[ElementT]]:
        # Do the slicing of the longlist and extract the subsections we want based on the names
        print(f"Converting section \"{pysec.name}\" from sheet \"{pysec.sheet_name}\"")
        df = self.clist.get_sheet(pysec.sheet_name)
        # from IPython import embed; embed()
        # section_df = df.set_index("NAME1").loc[pysec.start_marker_name1:pysec.stop_marker_name1]
        # section_df = section_df.reset_index()  # put NAME1 back as a column again.

        idx = df.with_row_index("row_nr")
        start_row = idx.filter(pl.col("NAME1") == pysec.start_marker_name1)
        stop_row = idx.filter(pl.col("NAME1") == pysec.stop_marker_name1)

        if start_row.is_empty():
            raise MalformedConversionConfig(f"Start marker not found: {pysec.start_marker_name1}")
        if stop_row.is_empty():
            raise MalformedConversionConfig(f"Stop marker not found: {pysec.stop_marker_name1}")

        idx_start = start_row.select("row_nr")[0, 0]
        idx_stop  = stop_row.select("row_nr")[0, 0]

        try:
            section_df = df.slice(idx_start, idx_stop - idx_start + 1)
        except:
            from IPython import embed; embed()

        _raise_if_row_is_not_marker(df[idx_start])
        _raise_if_row_is_not_marker(df[idx_stop])

        start = section_df[0]
        twiss0 = Twiss(beta_x=start["BETX"].item(),
                  beta_y=start["BETY"].item(),
                  alpha_x=start["ALFX"].item(),
                  alpha_y=start["ALFY"].item(),
                  E=start["ENERGY"].item())


        # Get rid of bad elements
        section_df = self._filter_bad_entries(section_df)

        # to be returned:
        sequence = []
        externals_placer = ExternalElementPlacer(pysec.new_elements)

        # the end position of the last element in S
        # running_s_end = section_df.iloc[0].S - 0.5 * section_df.iloc[0].LENGTH

        rows_here = section_df.iter_rows(named=True)
        rows_there = section_df.iter_rows(named=True)
        next(rows_there) # type: ignore
        for row_here, row_there in zip(rows_here, rows_there):
            # row_here corresponds to the next row we will be building UP TO, but we do not
            # convert that element (if indeed we do) until the next.

            self.rowedits.apply_changes(row_here)

            # Convert to OCELOT element
            oelement_here = self.dispatch(row_here)
            oelement_there = self.dispatch(row_there) # We convert next element to get e.g. correct lengths

            if oelement_here.id in pysec.extras:
                for property_name, value in pysec.extras[oelement_here.id].items():
                    print(f"Setting new value for element: {oelement_here.id}, {property_name} -> {value}")
                    setattr(oelement_here, property_name, value)
                    # Special handling for undulators...
                    if property_name == "nperiods" or property_name == "lperiod":
                        oelement_here.l = oelement_here.nperiods * oelement_here.lperiod

            # Can't use row["LENGTH"] because it's wrong for example in
            # UNDU.  S Is the same/correct though.  Indeed it has to
            # be because the longlist includes no drifts, so figuring
            # out the structure of the lattice only using lengths is
            # not possible.
            oelement_here_start_s = row_here["S"] - oelement_here.l * 0.5
            oelement_there_start_s = row_there["S"] - oelement_there.l * 0.5

            oelement_here_until_next_element = self._expand_from_this_element_to_next(
                oelement_here,
                oelement_there,
                oelement_here_start_s,
                oelement_there_start_s,
                externals_placer,
            )

            sequence.extend(oelement_here_until_next_element)

        # # Now we attach the final element, which we have checked
        # # above is indeed a marker.
        sequence.append(self.convert_mark(row_there))

        if pysec.matching:
            marker_name = pysec.matching.marker_name
            quadrupole_names = set(pysec.matching.quadrupoles)
            df = self.clist.get_sheet(pysec.sheet_name)
            first_row = self.clist.get_sheet(pysec.sheet_name)[0]
            marker_row = self.clist.get_sheet(pysec.sheet_name).filter(pl.col("NAME1") == marker_name)

            twiss0 = Twiss(beta_x=first_row["BETX"].item(),
                           beta_y=first_row["BETY"].item(),
                           alpha_x=first_row["ALFX"].item(),
                           alpha_y=first_row["ALFY"].item(),
                           E=first_row["ENERGY"].item())


            marker = next(ele for ele in sequence if ele.id == marker_name)
            quadrupoles = []
            for element in sequence:
                if element.id in quadrupole_names:
                    quadrupoles.append(element)

            initial_strengths = {q.id: q.k1 for q in quadrupoles}

            print(f"Start matching @ {marker_name} with quads: {quadrupoles}")
            print(f"Initial quadrupole strengths: {initial_strengths}")
            new_k1 = match(
                MagneticLattice(sequence),
                {
                    marker: {
                        "beta_x": marker_row["BETX"].item(),
                        "beta_y": marker_row["BETY"].item(),
                        "alpha_x": marker_row["ALFX"].item(),
                        "alpha_y": marker_row["ALFY"].item(),
                        "E": marker_row["ENERGY"].item()
                    }
                },
                quadrupoles,
                twiss0,
            )
            print(f"End matching @ {marker_name} with quads: {quadrupoles}")
            print(f"New quadrupole strengths: { {q.id: q.k1 for q in quadrupoles} }")



        return twiss0, sequence

    def _expand_from_this_element_to_next(
            self,
            oelement0: OpticElement,
            oelement1: OpticElement,
            oelement_s_start: float,
            next_element_s_start: float,
            external_element_placer: ExternalElementPlacer,
            ):
        if oelement_s_start == next_element_s_start:
            return [oelement0]

        # The length of the expanded sequence we are going for here...
        final_length = next_element_s_start - oelement_s_start

        ep = external_element_placer



        # We go through the elements 1 by 1 now that we may wish to attach...

        append0, between, prepend1 = ep.get_elements_to_insert_in_range(
            oelement_s_start, next_element_s_start, oelement0, oelement1
        )

        # XX THJIS SI WRONG< WHAT IF MARKER INSSIDE FIRST ELEMENT??? ASSUMED NOIT TO BE< BUT COULD BE!!
        expanded_sequence = [oelement0]

        # if not (append0 or between or prepend1):
        #     return [oelement0, self._next_drift(l=next_element_s_start - oelement_s_start + oelement0.l)]

        for p in append0:
            print(f"Appending element @ {p}")
            expanded_sequence.append(p)

        # Something impressive goes here for placing global and relative S elements...

        for s, placements_at_this_s in between:
            if  oelement_s_start < s < oelement_s_start + oelement0.l:
                # THIS NEEDS TO BE HANDLED PROPERLY!!!  split them??
                # XXX!!!
                continue
                # from IPython import embed; embed()
            # We are currently at in global s-space:
            # s_oelement_s_start + sum(x.l for x in expanded_sequence)
            # from IPython import embed; embed()
            expanded_sequence.extend(self._next_drift_sequence(s - oelement_s_start - sum(x.l for x in expanded_sequence)))
            for placement in placements_at_this_s:
                print(placement.element)
                print(f"Placing element @ {s}")
                expanded_sequence.append(placement.element)

        length_so_far = sum(x.l for x in expanded_sequence)
        expanded_sequence.extend(self._next_drift_sequence(l=final_length - length_so_far))

        for p in prepend1:
            print(f"Prepending element vor {p}")
            expanded_sequence.append(p)

        return expanded_sequence

        # from IPython import embed; embed()


    # def _attach_markers_to_element(
    #     self, s_start: float, s_stop: float, oelement, element_placer: ExternalElementPlacer
    # ) -> list:
    #     """s_start, s_stop define region where were look to try to insert markers"""
    #     #XXX: This function is also responsible for adding drifts to the sequence!
    #     try:
    #         assert np.isclose(s_stop, s_start) or (s_stop > s_start)
    #     except:
    #         import ipdb; ipdb.set_trace()

    #     # Attach any markers either side of the element (based on name)
    #     oelement_with_markers = marker_placer.build_element_sequence_with_markers(
    #         oelement
    #     )

    #     # See if there are any markers placed at S
    #     markers_with_s = marker_placer.s_markers_in_interval(s_start, s_stop)
    #     if not markers_with_s:
    #         drift_length = s_stop - s_start
    #         if drift_length > 0:
    #             drift = self._next_drift(l=drift_length)
    #             oelement_with_markers = [drift] + oelement_with_markers
    #         return oelement_with_markers

    #     # Place markers
    #     for marker, s in markers_with_s:
    #         # Drift, Marker
    #         drift_length = self._round(s - s_start)
    #         if drift_length > 0:
    #             oelement_with_markers.append(self._next_drift(l=drift_length))
    #         oelement_with_markers.append(marker)
    #         s_start = s

    #     oelement_with_markers.append(self._next_drift(s_stop - s))

    #     return oelement_with_markers

    def _next_drift_sequence(self, l: float) -> list[elements.Drift]:
        # We reject very small
        if abs(l) < self.MINIMUM_DRIFT_LENGTH:
            return []
        if l < 0:
            from ipdb import set_trace; set_trace()

        if l < 0:
            return []

        drift = elements.Drift(l=l, eid=f"D_{self.drift_counter}")
        self.drift_counter += 1
        return [drift]

    def _apply_manual_changes(self, element: ElementT) -> None:
        try:
            properties = self.extra_properties[element.id]
        except KeyError:
            return
        else:
            for property_name, value in properties.items():
                setattr(element, property_name, value)
                if property_name == "nperiods" or property_name == "lperiod":
                    element.l = element.nperiods * element.lperiod

    def dispatch(self, row: dict[str, Any]) -> ElementT:
        ocelot_class_name = row["GROUP"].lower()
        try:
            oelement = getattr(self, f"convert_{ocelot_class_name}")(row)
            self._apply_manual_changes(oelement)
            return oelement
        except AttributeError:
            raise UnknownLongListElement(
                "Unknown element to be converted:"
                f"{row["NAME1"]=}, {row["GROUP"]=}, {row["CLASS"]=}, {row["TYPE"]=}, {row["LENGTH"]=}"
            )
        except Exception as e:
            raise ComponentListToOcelotConversionError(
                "Unexpected error converting element:"
                f"{row["NAME1"]=}, {row["GROUP"]=}, {row["CLASS"]=}, {row["TYPE"]=}, {row["LENGTH"]=}"
            ) from e


    def convert_magnet(
        self, row: dict[str, Any]
    ) -> Union[
        elements.Quadrupole,
        elements.Hcor,
        elements.Vcor,
        elements.SBend,
        elements.Solenoid,
        elements.Sextupole,
        elements.Octupole,
        elements.RBend
    ]:
        common_kw = {
            "eid": row["NAME1"],
            "l": row["LENGTH"],
        }

        if row["TILT"] != 0.0:
            common_kw["tilt"] = row["TILT"]
        if row["LENGTH"] != 0.0:
            common_kw["l"] = row["LENGTH"]

        assert row["GROUP"] in {"RAMPKICK", "MAGNET", "FASTKICK", "FBKICK"}, row["GROUP"]

        if row["TYPE"] in ["CAX", "CAY", "CBX", "CBY"]:
            # vertical and horizontal aircoils have the same position and non zero length
            common_kw["l"] = 0


        if row["CLASS"] == "QUAD":
            if row["LENGTH"] == 0 and row["STRENGTH"] == 0:
                return elements.Quadrupole(**common_kw)                
            return elements.Quadrupole(k1=row["STRENGTH"] / row["LENGTH"], **common_kw)
        elif row["CLASS"] == "HKIC":
            return elements.Hcor(angle=row["STRENGTH"], **common_kw)
        elif row["CLASS"] == "VKIC":
            return elements.Vcor(angle=row["STRENGTH"], **common_kw)
        elif row["CLASS"] == "SBEN":
            return elements.SBend(
                angle=row["STRENGTH"], e1=row["E1/LAG"], e2=row["E2/FREQ"], **common_kw
            )
        elif row["CLASS"] == "SOLE":
            return elements.Solenoid(**common_kw)
        elif row["CLASS"] == "SEXT":
            if row["LENGTH"] == 0 and row["STRENGTH"] == 0:
                return elements.Sextupole(**common_kw)
            return elements.Sextupole(k2=row["STRENGTH"] / row["LENGTH"], **common_kw)
        elif row["CLASS"] == "RBEN":
            return elements.RBend(
                angle=row["STRENGTH"], e1=row["E1/LAG"], e2=row["E2/FREQ"], **common_kw
            )
        elif row["CLASS"] == "OCTU":
            if row["LENGTH"] == 0 and row["STRENGTH"] == 0:
                return elements.Octupole(**common_kw)
            return elements.Octupole(k3=row["STRENGTH"] / row["LENGTH"], **common_kw)

        raise UnknownLongListElement(row)

    def convert_pmagnet(self, row: dict[str, Any]) -> elements.RBend | elements.Quadrupole:
        common_kw = dict(eid=row["NAME1"], l=row["LENGTH"])
        if row["CLASS"] == "RBEN":
            return elements.RBend(
                angle=row["STRENGTH"], e1=row["E1/LAG"], e2=row["E2/FREQ"], **common_kw
            )
        if row["CLASS"] == "QUAD":
            return elements.Quadrupole(k1=row["STRENGTH"] / row["LENGTH"], **common_kw)
        raise UnknownLongListElement(row)


    def convert_undu(self, row: dict[str, Any]) -> elements.Undulator | elements.Drift:
        assert row["GROUP"] == "UNDU"

        if row["CLASS"] == "PHASESHIFTER":
            return self.convert_phaseshifter(row)
        assert row["CLASS"] == "UNDULATOR"
        # Extract sequences of numbers from the TYPE
        type_numbers = re.findall(r"\d+", row["TYPE"])
        lperiod = float(type_numbers[0]) * 1e-3

        length = row["LENGTH"]
        nperiods = length / lperiod
        undulator = elements.Undulator(lperiod=lperiod, nperiods=nperiods, eid=row["NAME1"])
        # # have to explicitly set the length here, otherwise it is 0.0
        # # cos the class invariant is not properly preserved by the
        # # class itself.
        # undulator.l = undulator.lperiod * undulator.nperiods
        return undulator

    def convert_phaseshifter(self, row: dict[str, Any]) -> elements.Drift:
        """Phase shifters are converted to drifts (at least for now)"""
        assert row["GROUP"] == "UNDU"
        assert row["CLASS"] == "PHASESHIFTER"
        return elements.Drift(l=row["LENGTH"], eid=row["NAME1"])

    def convert_cryo(self, row: dict[str, Any]) -> elements.Drift:
        assert row["GROUP"] == "CRYO"
        assert row["CLASS"] == "CRYO"
        return elements.Drift(l=row["LENGTH"], eid=row["NAME1"])

    def convert_vacuum(self, row: dict[str, Any]) -> elements.Drift:
        assert row["GROUP"] == "VACUUM"
        assert row["CLASS"] in {"VAC", "ECOL", "PLACEH", "ABSORBER"}, (row["CLASS"], row["LENGTH"])
        return elements.Drift(l=row["LENGTH"], eid=row["NAME1"])

    def convert_cavity(self, row: dict[str, Any]) -> Union[elements.Cavity, elements.TDCavity]:
        assert row["GROUP"] == "CAVITY"
        common_kw = {
            "eid": row["NAME1"],
            "l": row["LENGTH"],
            "v": row["STRENGTH"] * 1e-3,
            "phi": row["E1/LAG"] * 360,
            "freq": row["E2/FREQ"] * 1000000,
        }
        if row["TILT"]:
            common_kw["tilt"] = row["TILT"]

        if row["TYPE"] == "C" or row["TYPE"] == "C3":
            return elements.Cavity(**common_kw)
        elif row["TYPE"] == "TDSA" or row["TYPE"] == "TDSB":
            return elements.TDCavity(**common_kw)

        raise UnknownLongListElement(row)

    def convert_diag(self, row: dict[str, Any]) -> Union[elements.Marker, elements.Monitor]:
        assert row["GROUP"] == "DIAG"
        if row["CLASS"] == "INSTR":
            return elements.Marker(eid=row["NAME1"])
        elif row["CLASS"] == "MONI":
            return elements.Monitor(eid=row["NAME1"], l=row["LENGTH"])
        elif row["CLASS"] == "CM":
            return elements.Marker(eid=row["NAME1"])
        raise UnknownLongListElement(row)

    def convert_mark(self, row: dict[str, Any]) -> elements.Marker:
        assert row["GROUP"] == "MARK"
        return elements.Marker(eid=row["NAME1"])

    convert_rampkick = convert_magnet
    convert_fastkick = convert_magnet
    convert_fbkick = convert_magnet


def longlist_to_ocelot(
    fname: str,
    ftoml: str,
    outdir: str,
) -> None:

    with open(ftoml, "rb") as f:
        config = yaml.safe_load(f)

    # Parse the config dictionary
    sections = _parse_config_dict(config)
    rowskips, rowedits = _parse_row_changes(config)

    llcv = LongListConverter(ComponentList(fname),
                             rowskips=rowskips,
                             rowedits=rowedits)

    sequences = llcv.convert_sections(sections)

    module_names = []
    for (name, (twiss0, sequence)) in sequences.items():

        module_name = name.lower()
        module_names.append(module_name)
        outf = outdir / Path(f"{module_name}.py")

        writer = PythonSubsequenceWriter(sequence, twiss0)

        with open(outf, "w") as f:
            f.write(writer.to_module())

    init_path = outdir / "__init__.py"
    with open(init_path, "w") as f:
        for module_name in module_names:
            f.write(f"from . import {module_name}\n")

    print("Written", init_path)

# def generate_real_i1_matched_config(i1_sequence, twiss0, realconfig):
#     # i1_dummy_section = FELSection(i1_sequence)
#     just_injector = EuXFEL(i1_sequence, twiss0, felconfig=realconfig)
#     match_52_twiss_constraint = get_default_component_list().get_optics_constraint(MATCH_52)
#     real_matched_conf = just_injector.match_twiss(
#         just_injector.twiss0,
#         elements=INJECTOR_MATCHING_QUAD_NAMES,
#         constraints=match_52_twiss_constraint,
#     )
#     return real_matched_conf


# def make_felconfig_design_to_real(dconf: dict) -> EuXFELSimConfig:
#     result = EuXFELSimConfig()

#     try:
#         lh_angle = dconf["hlc"]["LH"]["angle"]
#     except KeyError:
#         lh_angle = None

#     result.controls["lh"].angle = lh_angle

#     try:
#         bc0_angle = dconf["hlc"]["BC0"]["angle"]
#     except KeyError:
#         bc0_angle = None
#     result.controls["bc0"].angle = bc0_angle

#     try:
#         bc1_angle = dconf["hlc"]["BC1"]["angle"]
#     except KeyError:
#         bc1_angle = None
#     result.controls["bc1"].angle = bc1_angle

#     try:
#         bc2_angle = dconf["hlc"]["BC2"]["angle"]
#     except KeyError:
#         bc2_angle = None
#     result.controls["bc2"].angle = bc2_angle

#     result.components = dconf["components"]
#     return result


def _parse_new_markers_dict(dconf: dict) -> dict[str, Placement]:
    markers = {}
    for new_marker_name, position_info in dconf.items():
        marker = elements.Marker(eid=new_marker_name)
        markers[new_marker_name] = _parse_element_placement(marker, position_info)
    return markers


def _parse_new_elements_dict(dconf: dict[str, dict[str, Any]]) -> dict[str, Placement]:
    new_elements = {}
    for name, properties in dconf.items():
        etype = properties["type"]
        if etype == "SlicedElement":
            print(1)
            elements = {}
            for slice_name, element_slice_def in properties["elements"].items():
                element_slice = _dict_to_element(slice_name, element_slice_def)
                elements[slice_name] = element_slice

            assert name not in new_elements
            element = SlicedElement(
                elements=elements, expression=properties["expression"], eid=name
            )
            placement = _parse_element_placement(element, properties["position"])
            new_elements[name] = placement
        else:
            # I could add the rest relatively easily, but not necessary atm.
            raise ValueError("Unsupported element type, %s", etype)
    return new_elements

def _parse_matching_dict(mconf: dict[str, str | list[str]]) -> MatchingRequest:
    try:
        return MatchingRequest(marker_name=mconf["marker"], quadrupoles=mconf["quadrupoles"])
    except KeyError as e:
        raise MalformedConversionConfig("Missing key(s) in matching section") from e

def _parse_element_placement(element, dd: dict[str, str]) -> Placement:
    reference = dd.get("reference", "")

    is_adjacent = "adjacent" in dd
    is_s_pos = "s" in dd

    if is_adjacent and is_s_pos:
        raise ValueError()

    if is_adjacent:
        assert reference is not None
        placement = AdjacentPlacement(element, AdjacentPositionType[dd["adjacent"].upper()], reference)
    elif is_s_pos:
        # from IPython import embed; embed()
        placement = OffsetPlacement(element, dd["s"], reference_name1=reference)
    else:
        raise KeyError()

    return placement


class MalformedConversionConfig(Exception):
    pass

def _dict_to_element(name: str, dconf: dict[str, Any]):
    try:
        etype = dconf.pop("type") # type: ignore
    except KeyError as e:
        raise MalformedConversionConfig("Missing type tag for new element") from e

    eid = dconf.pop("eid", name)
    return getattr(elements, etype)(**dconf, eid=eid)


def _parse_config_dict(dconf: dict) -> list[SubsequenceModule]:
    sections = []
    for section_name, info in dconf["sections"].items():
        try:
            new_markers = _parse_new_markers_dict(info["new_markers"])
        except KeyError:
            new_markers = {}

        try:
            new_elements = _parse_new_elements_dict(info["new_elements"])
        except KeyError:
            new_elements = {}

        try:
            matching_request = _parse_matching_dict(info["matching"])
        except KeyError:
            matching_request = None


        section = SubsequenceModule(
            start_marker_name1=info["start_marker_name1"],
            stop_marker_name1=info["stop_marker_name1"],
            name=section_name,
            sheet_name=info.get("sheet", "LONGLIST"),
            extras=info.get("extras", {}),
            new_elements=new_elements | new_markers,
            matching=matching_request
        )
        sections.append(section)

    return sections

def _parse_row_changes(dconf: dict) -> tuple[RowSkips, RowEdits]:
    try:
        rconf = dconf["rows"]
    except KeyError:
        return RowSkips(), RowEdits()

    try:
        skipconf = rconf["skip"]
    except KeyError:
        skips = RowSkips()
    else:
        skips = RowSkips(group=set(skipconf.get("GROUP", [])),
                        cls=skipconf.get("CLASS", set()),
                        type=skipconf.get("TYPE", set()),
                        name1=skipconf.get("NAME1", set())                        
                         )


    try:
        editconf = rconf["edit"]
    except KeyError:
        edits = RowEdits()
    else:
        edits = RowEdits(group=editconf.get("GROUP", {}),
                        cls=editconf.get("CLASS", {}),
                        type=editconf.get("TYPE", {}))
    return skips, edits


def _raise_if_row_is_not_marker(rowdict: dict[str, str | float]) -> None:
    if rowdict["GROUP"].item() != "MARK":
        raise MalformedConversionConfig(f"Start/Stop element: {rowdict["NAME1"]} is not a marker")
    if rowdict["CLASS"].item() != "MARK":
        raise MalformedConversionConfig(f"Start/Stop element: {rowdict["NAME1"]} is not a marker")


# def match_real_injector():
#     from oxfel import cat_to_i1d

#     fel = cat_to_i1d(model_type="real")

#     parray032 = load_reference_0320_100k_distribution()

#     parray37 = fel.track(parray032, start="start_ocelot", stop=MATCH_37)
#     twiss37 = get_envelope(parray37)

#     cl = get_default_longlist()
#     match_52_twiss_constraint = cl.get_optics_constraint("MATCH.52.I1")

#     linear_matched_conf = fel.match(
#         twiss37,
#         start=MATCH_37,
#         stop=MATCH_52,
#         constraints=match_52_twiss_constraint,
#         elements=INJECTOR_MATCHING_QUAD_NAMES,
#         verbose=True,
#     )

#     tracking_matched_conf = fel.match_beam(
#         parray37,
#         start=MATCH_37,
#         stop=MATCH_52,
#         elements=INJECTOR_MATCHING_QUAD_NAMES,
#         constraints=match_52_twiss_constraint,
#         felconfig=linear_matched_conf,
#     )

#     toml.load(files("oxfel.accelerator.lattice") / TRACKING_CONF_NAME)
#     outdir = files("oxfel.accelerator.lattice")

#     with (outdir / TRACKING_CONF_NAME).open("w") as f:
#         toml.dump(
#             {"components": tracking_matched_conf.components},
#             f,
#             encoder=toml.TomlNumpyEncoder(),
#         )
#         print(f"Wrote {f.name}")
