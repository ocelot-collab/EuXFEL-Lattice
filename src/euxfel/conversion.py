import logging
import re
from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum, auto
from importlib.resources import files
from pathlib import Path
from typing import Any, TypeVar, Union

import ocelot.cpbd.elements as elements
import polars as pl
import yaml
from ocelot import MagneticLattice
from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements.optic_element import OpticElement
from ocelot.cpbd.match import match

from euxfel.complist import ComponentList
from euxfel.slicing import SlicedElement
from euxfel.writer import PythonSubsequenceWriter

DEFAULT_CONVERSION_CONFIG_PATH = str(files("euxfel.longlists") / "conversion-config.yaml")

logging.basicConfig()
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

@dataclass
class RowSkips:
    """
    Specify row-level exclusions for converting from the Component List Excel spreadsheet.

    This dataclass collects sets of identifiers used to skip rows from the
    spreadsheet during model conversion. Each field corresponds to a column
    in the Excel source and defines values that should be ignored.

    Attributes
    ----------
    group : set[str]
        Spreadsheet GROUP values identifying rows to skip.
    cls : set[str]
        Spreadsheet CLASS values identifying rows to skip.
    type : set[str]
        Spreadsheet TYPE values identifying rows to skip.
    name1 : set[str]
        Spreadsheet NAME1 values identifying rows to skip.
    """
    group: set[str] = field(default_factory=set)
    cls: set[str] = field(default_factory=set)
    type: set[str] = field(default_factory=set)
    name1: set[str] = field(default_factory=set)

@dataclass
class RowEdits:
    """
    Define row-level edits applied to rows of the Component List Excel spreadsheet before
    converting to an Ocelot element.

    This dataclass stores mappings from spreadsheet identifiers to dictionaries
    of field updates. When applied to a row, edits are conditionally merged
    based on the row's GROUP, CLASS, and TYPE values.

    Attributes
    ----------
    group : dict[str, Any]
        Mapping from GROUP values to dictionaries of updates to apply.
    cls : dict[str, Any]
        Mapping from CLASS values to dictionaries of updates to apply.
    type : dict[str, Any]
        Mapping from TYPE values to dictionaries of updates to apply.
    """

    group: dict[str, Any] = field(default_factory=dict)
    cls: dict[str, Any] = field(default_factory=dict)
    type: dict[str,  Any] = field(default_factory=dict)

    def apply_changes(self, row: dict[str, Any]) -> None:
        """
        Apply in-place edits to a single row dictionary from the Component List.

        Updates are applied in the following order:
        1. GROUP-based edits
        2. CLASS-based edits
        3. TYPE-based edits

        Later updates override earlier ones if keys overlap.

        Parameters
        ----------
        row : dict[str, Any]
            A row dictionary parsed from the Excel spreadsheet. The dictionary
            is modified in place.
        """
        # if row["TYPE"] in ["CAX", "CAY", "CBX", "CBY"]:
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
    delta_s: float
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


class ExternalElementPlacer:
    """
    Manage insertion of externally-defined elements into a converted OCELOT sequence.

    This helper class organises placement instructions (typically provided by a
    section/module configuration) and, for a given interval between two lattice
    elements, determines which external elements should be:
    - appended immediately after the first element,
    - placed at specific global s positions between the two elements, and/or
    - prepended immediately before the second element.

    Placements are grouped into three categories:
    - Adjacent placements: inserted directly BEFORE/AFTER a named reference element.
    - Offset placements: inserted at an s offset relative to a named reference element.
    - Global placements: inserted at an absolute global s position (no reference).

    Parameters
    ----------
    placements : dict[str, Placement]
        Mapping of placement names/keys to placement instructions.

    Attributes
    ----------
    adjacent_placements : dict[str, list[AdjacentPlacement]]
        Placements keyed by reference element NAME1/id for BEFORE/AFTER insertion.
    offset_placements : dict[str, list[OffsetPlacement]]
        Placements keyed by reference element NAME1/id for relative-s insertion.
    global_placements : dict[float, list[OffsetPlacement]]
        Placements keyed by absolute global s coordinate (no reference element).
    """

    def __init__(self, placements: dict[str, Placement]):
        self.adjacent_placements = defaultdict(list)
        self.offset_placements = defaultdict(list)
        self.global_placements = defaultdict(list)

        for name, placement in placements.items():
            ref_name1 = placement.reference_name1
            if isinstance(placement, OffsetPlacement):
                if not ref_name1:
                    self.global_placements[placement.delta_s].append(placement)
                else:
                    self.offset_placements[ref_name1].append(placement)
            if isinstance(placement, AdjacentPlacement):
                self.adjacent_placements[ref_name1].append(placement)

    def get_elements_to_insert_in_range(
        self, s0: float, s1: float, element0: OpticElement, element1: OpticElement
    ) -> tuple[list[OpticElement], list[tuple[float, Placement]], list[OpticElement]]:
        """
        Determine which external elements to insert between two consecutive elements.

        The method returns three groups:
        1) Elements to append immediately after `element0` (AFTER adjacent placements).
        2) Elements to place at specific global s positions between `s0` and `s1`
           (global placements plus relative/offset placements that land in the range).
        3) Elements to prepend immediately before `element1` (BEFORE adjacent placements).

        Placement rules
        --------------
        - Adjacent placements:
            * AFTER(element0) are appended.
            * BEFORE(element1) are prepended.
        - Global placements:
            * Any placement with absolute s satisfying s0 <= s <= s1 is returned as a
              "between" placement.
        - Offset placements:
            * For element0: only non-negative offsets are applied (downstream),
              at s = s0 + element0.l + offset.
            * For element1: only non-positive offsets are applied (upstream),
              at s = s0 + offset - 0.5*element1.l.

        Parameters
        ----------
        s0 : float
            Global s coordinate of the start of the interval (typically the start of
            `element0`).
        s1 : float
            Global s coordinate of the end of the interval (typically the start of
            `element1`).
        element0 : OpticElement
            First element bounding the interval.
        element1 : OpticElement
            Second element bounding the interval.

        Returns
        -------
        tuple[list[OpticElement], list[tuple[float, list[Placement]]], list[OpticElement]]
            (append_element0, between_elements, prepend_element1), where:
            - append_element0 is a list of elements to append after element0,
            - between_elements is a list of (global_s, [placements]) to be placed at s,
            - prepend_element1 is a list of elements to prepend before element1.
        """

        # First we check adjacent_placements, which are placed either
        # immediately after element0 or immediately prior to element1
        # (i.e with no Drift elements in between).
        append_element0: list[OpticElement] = []
        prepend_element1: list[OpticElement] = []
        for p in self.adjacent_placements[element0.id]:
            if p.before_after is AdjacentPositionType.AFTER:
                append_element0.append(p.element)
        for p in self.adjacent_placements[element1.id]:
            if p.before_after is AdjacentPositionType.BEFORE:
                prepend_element1.append(p.element)

        # Now we check global placements, which are immediately
        # before/after each element.
        between_elements: list[tuple[float, Placement]] = []
        for s, placements in self.global_placements.items():
            if s0 <= s <= s1:
                between_elements.append((s, placements))

        # now we check offset placements: Let's look for elements to
        # be offset with respect to after the element0.  we interpret
        # delta_s as delta_s past the END of the element (not with
        # respect to S as it is in the longlist, i.e, the centre of
        # the element.
        for placement in self.offset_placements[element0.id]:
            delta_s = placement.delta_s
            if delta_s >= 0:
                between_elements.append((s0 + element0.l + delta_s, [placement]))

        # Now let's look for elements to be offset with respect to
        # before the element01.  we interpret delta_s as delta_s from
        # before the start of element1 (not with respect to S as it
        # is in the longlist, i.e, the centre of the element).
        for placement in self.offset_placements[element1.id]:
            delta_s = placement.delta_s
            if delta_s <= 0:
                between_elements.append((s0 + delta_s - element1.l * 0.5, [placement]))

        return append_element0, between_elements, prepend_element1


class LongListConverter:
    """
    Convert an Excel/component-list lattice description into OCELOT elements.

    This class orchestrates the full conversion pipeline from a component list
    (presumably read from an Excel spreadsheet) into OCELOT optic elements and
    lattice subsequences. It handles row filtering, row editing, element
    dispatching, drift generation, external element insertion, and optional
    optics matching.

    Configuration is provided via:
    - `RowSkips`: declarative rules for skipping rows during conversion.
    - `RowEdits`: declarative rules for modifying rows after reading and before
      conversion.
    - `extra_properties`: per-element property overrides applied after element
      construction.

    Attributes
    ----------
    MINIMUM_DRIFT_LENGTH : float
        Minimum drift length below which drifts are discarded.
    clist : ComponentList
        Source component list containing one or more sheets describing the
        lattice.
    extra_properties : dict
        Mapping from element ID to dictionaries of attribute overrides applied
        after conversion.
    rowskips : RowSkips
        Rules defining which rows should be skipped during conversion.
    rowedits : RowEdits
        Rules defining in-place edits applied to rows before conversion.
    drift_counter : int
        Counter used to generate unique drift element IDs.
    """

    MINIMUM_DRIFT_LENGTH = 1e-9

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

    def convert_sections(self, sections: list[SubsequenceModule]) -> dict[str, tuple[Twiss, list[OpticElement]]]:
        """
        Convert multiple subsections of the component list into OCELOT sequences.

        Each subsection is converted independently using `convert_section`. The
        internal drift counter is reset before converting each section to ensure drift
        name integer suffixes stay reltively small.

        Parameters
        ----------
        sections : list[SubsequenceModule]
            List of subsection configurations defining which parts of the
            component-list sheets to convert.

        Returns
        -------
        dict[str, tuple[Twiss, list[OpticElement]]]
            Mapping from subsection name to a tuple containing:
            - the initial Twiss parameters for the subsection
            - the converted OCELOT element sequence

        Raises
        ------
        ComponentListToOcelotConversionError
            If conversion of any subsection fails. The raised error includes the
            subsection name and sheet for easier diagnosis.
        """
        self.drift_counter = 0
        result = {}
        for section in sections:
            self.drift_counter = 0
            try:
                result[section.name] = self.convert_section(section)
            except Exception as e:
                raise ComponentListToOcelotConversionError(
                    f"Conversion failed in {section.name} in sheet {section.sheet_name}"
                    ) from e

        return result

    def _filter_skippables(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Remove rows matching configured skip rules based on component list metadata.

        Rows are excluded if any of their identifying fields match values listed in
        the configured `RowSkips` instance:
        - TYPE
        - CLASS
        - GROUP
        - NAME1

        All matching rows are dropped unconditionally. Skipped rows are reported
        for traceability before removal.

        Parameters
        ----------
        df : pl.DataFrame
            Polars DataFrame containing component-list rows. Must include at least
            NAME1, S, TYPE, CLASS, and GROUP columns.

        Returns
        -------
        pl.DataFrame
            A filtered DataFrame with all rows matching the skip criteria removed.
        """

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

    # def _check_external_placements(self, df: pl.DataFrame, new_elements: dict[str, Placement]) -> None:
    #     return
    #     from IPython import embed; embed()
    #     # We basically need to check the new elements.  We consider
    #     # two types, "thin" new elements, and thick ones
    #     for new_element_name, placement in new_elements.items():
    #         element = placement.element
    #         length = placement.element.l
    #         refname = placement.reference_name1

    #         if refname == "":
    #             ref_element_start = 0.
    #             ref_element_stop = 0.
    #         else:
    #             ref_element_row = df.filter(pl.col("NAME1") == refname)
    #             ref_element_start = (ref_element_row["S"] - ref_element_row["LENGTH"] / 2.0).item()
    #             ref_element_stop = (ref_element_row["S"] + ref_element_row["LENGTH"] / 2.0).item()

                
    #         if isinstance(placement, AdjacentPlacement):
    #             # By definition we do not expect overlaps with
    #             # existing elements for an AdjacentPlacement of an
    #             # element with zero length.  So this is immediately
    #             # OK.
    #             if not length:
    #                 continue

    #             if placement.before_after is AdjacentPositionType.BEFORE:
    #                 element_stop = ref_element_start
    #                 element_start = element_stop - length
    #             elif placement.before_after is AdjacentPositionType.AFTER:
    #                 element_start = ref_element_stop

    #             if element.l:
    #                 element_Start = ref_element_stop
    #                 raise ValueError()


    #         if isinstance(placement, OffsetPlacement):
    #             if not length:
    #                 continue

    #             delta_s = placement.delta_s

    #             if delta_s > 0:
    #                 element_start = ref_element_stop + delta_s
    #                 element_stop = element_start + placement.element.l
                    
    #             elif delta_s < 0:
    #                 element_stop = ref_element_start - delta_s
    #                 element_start = element_stop - placement.element.l

    #             else:
    #                 pass

    #             # 
    #             existing_elements_start = df["S"] - df["LENGTH"] * 0.5
    #             existing_elements_stop = df["S"] + df["LENGTH"] * 0.5

                

    #     pass

    def _filter_bad_rows(self, df: pl.DataFrame) -> pl.DataFrame:
        """
        Remove invalid or nonsensical rows from a component-list DataFrame prior to conversion.

        This cleaning step is used after reading a section from the component list
        and before converting rows into OCELOT elements.

        The filtering includes:
        - Dropping elements with negative longitudinal position (S < 0), with a warning.
        - Applying additional column-based rejection rules via `_filter_on_bad_columns`.
        - Dropping zero-length entries (typically markers) that lie strictly inside the
          longitudinal extent of another element (based on each element's [S - L/2, S + L/2]
          interval), with a warning.

        Parameters
        ----------
        df : pl.DataFrame
            Polars DataFrame containing component-list rows. Must include at least
            NAME1, S, and LENGTH.

        Returns
        -------
        pl.DataFrame
            A filtered DataFrame with problematic rows removed and overlapping
            correctors shifted as required.
        """
        neg_s = df.filter(pl.col("S") < 0)

        for name1, s in neg_s.select("NAME1", "S").iter_rows():
            LOG.warning(f"Dropping element with negative S: {name1 = }, {s = }")

        df = df.filter(pl.col("S") >= 0)
        df = self._filter_skippables(df)

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

        # from IPython import embed; embed()

        return df_no_bad

    def convert_section(self, pysec: SubsequenceModule) -> tuple[Twiss, list[ElementT]]:
        """
        Convert a named subsection of a component-list sheet into an OCELOT sequence.

        This method slices an component list sheet between two marker rows,
        converts each row to an OCELOT element, inserts required drift segments to
        span gaps in global s, and optionally places additional external elements
        defined by the subsection configuration.

        Workflow
        --------
        1. Load the sheet specified by `pysec.sheet_name` and locate the rows whose
           NAME1 matches `pysec.start_marker_name1` and `pysec.stop_marker_name1`.
        2. Slice the DataFrame to include all rows from the start marker through
           the stop marker (inclusive), and validate that both endpoints are markers.
        3. Initialise the starting Twiss (`twiss0`) from the optics values stored on
           the start marker row.
        4. Filter out invalid/unwanted rows via `_filter_bad_entries`.
        5. Iterate over pairs of consecutive rows:
           - Apply row edits (`self.rowedits.apply_changes`) to both rows.
           - Convert both rows using `dispatch` (the next row is converted to obtain
             correct downstream geometry/length context).
           - Apply per-section overrides in `pysec.extras` (with special handling for
             undulator length updates when `nperiods` or `lperiod` changes).
           - Compute each element's start position in global s as `S - 0.5*l`.
           - Build an expanded sequence from the current element up to the next
             element via `_expand_from_this_element_to_next`, inserting drifts and any
             configured external elements.
        6. Append the final stop marker to close the section.
        7. If `pysec.matching` is enabled, perform Twiss matching at a configured marker
           by varying a configured set of quadrupoles to meet target optics extracted
           from the component list.

        Parameters
        ----------
        pysec : SubsequenceModule
            Configuration describing which sheet to convert, the start/stop marker
            NAME1 values, any external elements to insert, optional per-element
            overrides, and optional matching configuration.

        Returns
        -------
        tuple[Twiss, list[ElementT]]
            The initial Twiss conditions to be used for tracking through the section,
            and the converted OCELOT element sequence for the section.

        Raises
        ------
        MalformedConversionConfig
            If the configured start or stop marker cannot be found in the sheet.
        ValueError
            If marker validation fails (e.g. endpoints are not marker rows), as raised
            by `_raise_if_row_is_not_marker` or downstream conversion utilities.
        """

        # Do the slicing of the longlist and extract the subsections we want based on the names
        print(f"Converting section \"{pysec.name}\" from sheet \"{pysec.sheet_name}\"")
        df = self.clist.get_sheet(pysec.sheet_name)
        idx = df.with_row_index("row_nr")
        start_row = idx.filter(pl.col("NAME1") == pysec.start_marker_name1)
        stop_row = idx.filter(pl.col("NAME1") == pysec.stop_marker_name1)

        if start_row.is_empty():
            raise MalformedConversionConfig(f"Start marker not found: {pysec.start_marker_name1}")
        if stop_row.is_empty():
            raise MalformedConversionConfig(f"Stop marker not found: {pysec.stop_marker_name1}")

        idx_start = start_row.select("row_nr")[0, 0]
        idx_stop  = stop_row.select("row_nr")[0, 0]
        section_df = df.slice(idx_start, idx_stop - idx_start + 1)

        _raise_if_row_is_not_marker(df[idx_start])
        _raise_if_row_is_not_marker(df[idx_stop])

        start = section_df[0]
        twiss0 = Twiss(beta_x=start["BETX"].item(),
                  beta_y=start["BETY"].item(),
                  alpha_x=start["ALFX"].item(),
                  alpha_y=start["ALFY"].item(),
                  E=start["ENERGY"].item())


        # Get rid of bad elements
        section_df = self._filter_bad_rows(section_df)

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
            self.rowedits.apply_changes(row_there)

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
            match(
                MagneticLattice(sequence), # type: ignore
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
        """
        Expand the lattice sequence between two consecutive elements by inserting
        external elements and required drift segments.

        Given two neighbouring OCELOT elements (oelement0 followed by oelement1) and
        their start positions in global s, this method builds an expanded sequence
        that covers the full interval from `oelement_s_start` to `next_element_s_start`.

        The expansion logic:
        - If both start positions are identical, no expansion is needed and the
          original element is returned.
        - Queries `external_element_placer` for elements to be inserted:
            * elements to append immediately after `oelement0` (append0)
            * elements to place at specific s positions between the two elements (between)
            * elements to prepend immediately before `oelement1` (prepend1)
        - Inserts drift elements as needed so that placements in `between` occur at
          the requested global s positions.
        - Pads the end of the interval with a final drift so the total added length
          matches `next_element_s_start - oelement_s_start`.
        - Appends any `prepend1` elements at the end of the expanded sequence.

        Notes
        -----
        Placements whose global s lies strictly within the body of `oelement0`
        (i.e. `oelement_s_start < s < oelement_s_start + oelement0.l`) are currently
        skipped. Proper handling would require splitting `oelement0` (and/or more
        advanced insertion semantics).

        Parameters
        ----------
        oelement0 : OpticElement
            The current lattice element (start of the interval).
        oelement1 : OpticElement
            The next lattice element (end of the interval), used for context when
            requesting insertions.
        oelement_s_start : float
            Global s position (start) of `oelement0`.
        next_element_s_start : float
            Global s position (start) of `oelement1`.
        external_element_placer : ExternalElementPlacer
            Provider of external elements to be inserted in the interval.

        Returns
        -------
        list[OpticElement]
            Expanded sequence beginning with `oelement0`, followed by any inserted
            elements and drifts required to span the interval up to
            `next_element_s_start`.
        """

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
            # We are currently at in global s-space:
            # s_oelement_s_start + sum(x.l for x in expanded_sequence)
            try:
                expanded_sequence.extend(self._next_drift_sequence(s - oelement_s_start - sum(x.l for x in expanded_sequence)))
            except:
                from IPython import embed; embed()

            for placement in placements_at_this_s:
                print(placement.element)
                print(f"Placing element @ {s}")
                expanded_sequence.append(placement.element)

        length_so_far = sum(x.l for x in expanded_sequence)
        try:
            expanded_sequence.extend(self._next_drift_sequence(length=final_length - length_so_far))
        except:
            from IPython import embed; embed()

        for p in prepend1:
            print(f"Prepending element vor {p}")
            expanded_sequence.append(p)

        return expanded_sequence

    def _next_drift_sequence(self, length: float) -> list[elements.Drift]:
        """
        Generate the next drift element given longitudinal length.

        Drifts shorter than the configured minimum length are ignored. Negative
        drift lengths are treated as an error and abort the conversion.

        Parameters
        ----------
        length : float
            Longitudinal length of the drift section.

        Returns
        -------
        list[elements.Drift]
            A list containing a single Drift element if the length is valid,
            otherwise an empty list.

        Raises
        ------
        ComponentListToOcelotConversionError
            If a negative drift length is encountered.
        """
        # We reject very small drifts
        if abs(length) < self.MINIMUM_DRIFT_LENGTH:
            return []
        if length < 0:
            raise ComponentListToOcelotConversionError("Negative drift length detected")

        drift = elements.Drift(l=length, eid=f"D_{self.drift_counter}")
        self.drift_counter += 1
        return [drift]

    def _apply_manual_changes(self, element: OpticElement) -> None:
        """
        Apply user-defined property overrides to an optic element during conversion.

        If manual changes are defined for the element ID, the corresponding
        attributes are set on the element instance. For undulators,
        updates to `nperiods` or `lperiod` trigger a recomputation of the total
        element length.

        Parameters
        ----------
        element : OpticElement
            The optic element to which manual property overrides may be applied.

        Returns
        -------
        None
            The element is modified in place.
        """
        try:
            properties = self.extra_properties[element.id]
        except KeyError:
            return
        else:
            for property_name, value in properties.items():
                setattr(element, property_name, value)
                if property_name == "nperiods" or property_name == "lperiod":
                    element.l = element.nperiods * element.lperiod

    def dispatch(self, row: dict[str, Any]) -> OpticElement:
        """
        Dispatch a component-list row to the appropriate conversion method.

        The conversion function is selected dynamically from the row GROUP:
        `convert_{GROUP.lower()}`. After conversion, any configured manual property
        overrides are applied via `_apply_manual_changes`.

        Parameters
        ----------
        row : dict[str, Any]
            Dictionary representing a single component-list row read from the Excel
            model. Must contain at least NAME1, GROUP, CLASS, TYPE, and LENGTH.

        Returns
        -------
        OpticElement
            The converted OCELOT optic element.

        Raises
        ------
        UnknownLongListElement
            If there is no corresponding `convert_{group}` method for the row GROUP.
        ComponentListToOcelotConversionError
            If an unexpected error occurs during conversion or manual-edit
            application.
        """
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
        """
        Convert a magnet-related row from the component list into an OCELOT element.

        This method expects a row originating from the component list model with
        GROUP in {"RAMPKICK", "MAGNET", "FASTKICK", "FBKICK"}. The specific OCELOT
        element type is selected via the CLASS field:

        - "QUAD" → Quadrupole
        - "HKIC" → Horizontal corrector (Hcor)
        - "VKIC" → Vertical corrector (Vcor)
        - "SBEN" → Sector bend (SBend)
        - "RBEN" → Rectangular bend (RBend)
        - "SOLE" → Solenoid
        - "SEXT" → Sextupole
        - "OCTU" → Octupole

        Common parameters are taken from the row:
        - NAME1 → `eid`
        - LENGTH → `l`
        - TILT (if non-zero) → `tilt`

        Strength handling:
        - QUAD/SEXT/OCTU use k1/k2/k3 = STRENGTH / LENGTH (when LENGTH is non-zero).
          If both LENGTH and STRENGTH are zero, a zero-strength element is created.
        - HKIC/VKIC use STRENGTH as a kick `angle`.
        - SBEN/RBEN use STRENGTH as `angle` and E1/LAG, E2/FREQ as edge angles.

        The element power-supply identifier is stored as `ps_id` from NAME2.

        Parameters
        ----------
        row : dict[str, Any]
            Dictionary representing a single component list row with magnet
            semantics.

        Returns
        -------
        elements.Quadrupole | elements.Hcor | elements.Vcor | elements.SBend |
        elements.Solenoid | elements.Sextupole | elements.Octupole | elements.RBend
            The corresponding OCELOT magnet element.

        Raises
        ------
        UnknownLongListElement
            If the CLASS is not recognised.
        AssertionError
            If GROUP is not one of the supported magnet-related groups.
        """
        common_kw = {
            "eid": row["NAME1"],
            "l": row["LENGTH"],
        }

        if row["TILT"] != 0.0:
            common_kw["tilt"] = row["TILT"]
        common_kw["l"] = row["LENGTH"]

        assert row["GROUP"] in {"RAMPKICK", "MAGNET", "FASTKICK", "FBKICK"}, row["GROUP"]

        if row["CLASS"] == "QUAD":
            if row["LENGTH"] == 0 and row["STRENGTH"] == 0:
                return elements.Quadrupole(**common_kw)
            ele = elements.Quadrupole(k1=row["STRENGTH"] / row["LENGTH"], **common_kw)
        elif row["CLASS"] == "HKIC":
            ele = elements.Hcor(angle=row["STRENGTH"], **common_kw)
        elif row["CLASS"] == "VKIC":
            ele = elements.Vcor(angle=row["STRENGTH"], **common_kw)
        elif row["CLASS"] == "SBEN":
            ele = elements.SBend(
                angle=row["STRENGTH"], e1=row["E1/LAG"], e2=row["E2/FREQ"], **common_kw
            )
        elif row["CLASS"] == "SOLE":
            ele = elements.Solenoid(**common_kw)
        elif row["CLASS"] == "SEXT":
            if row["LENGTH"] == 0 and row["STRENGTH"] == 0:
                ele = elements.Sextupole(**common_kw)
            ele = elements.Sextupole(k2=row["STRENGTH"] / row["LENGTH"], **common_kw)
        elif row["CLASS"] == "RBEN":
            ele = elements.RBend(
                angle=row["STRENGTH"], e1=row["E1/LAG"], e2=row["E2/FREQ"], **common_kw
            )
        elif row["CLASS"] == "OCTU":
            if row["LENGTH"] == 0 and row["STRENGTH"] == 0:
                ele = elements.Octupole(**common_kw)
            ele = elements.Octupole(k3=row["STRENGTH"] / row["LENGTH"], **common_kw)
        else:
            raise UnknownLongListElement(row)
        ele.ps_id = row["NAME2"]
        return ele

    def convert_pmagnet(self, row: dict[str, Any]) -> elements.RBend | elements.Quadrupole:
        """
        Convert a PMAGNET row from the component list into an OCELOT magnet element.

        This method converts powered magnetic elements based on the CLASS field:
        - "RBEN" → Sector bending magnet (RBend)
        - "QUAD" → Quadrupole magnet

        Common geometric parameters are taken directly from the component list.
        Magnet strengths are interpreted according to OCELOT conventions.

        Parameters
        ----------
        row : dict[str, Any]
            Dictionary representing a single component list row with PMAGNET
            group semantics.

        Returns
        -------
        elements.RBend or elements.Quadrupole
            The corresponding OCELOT magnet element.

        Raises
        ------
        UnknownLongListElement
            If the PMAGNET CLASS is not recognised.
        """
        common_kw = dict(eid=row["NAME1"], l=row["LENGTH"])
        if row["CLASS"] == "RBEN":
            ele = elements.RBend(
                angle=row["STRENGTH"], e1=row["E1/LAG"], e2=row["E2/FREQ"], **common_kw
            )
        elif row["CLASS"] == "QUAD":
            ele = elements.Quadrupole(k1=row["STRENGTH"] / row["LENGTH"], **common_kw)
        else:
            raise UnknownLongListElement(row)
        ele.ps_id = row["NAME2"]
        return ele

    def convert_undu(self, row: dict[str, Any]) -> elements.Undulator | elements.Drift:
        """
        Convert a UNDU row from the component list into an OCELOT undulator element.

        This method expects a row originating from the component list model
        with GROUP equal to "UNDU". The conversion depends on the CLASS field:
        - "PHASESHIFTER" → delegated to `convert_phaseshifter`, producing a Drift
        - "UNDULATOR"    → converted to an OCELOT Undulator

        For undulators, the period length is extracted from the TYPE field,
        converted from millimetres to metres, and used together with the total
        length to determine the number of periods.

        Parameters
        ----------
        row : dict[str, Any]
            Dictionary representing a single component list row with UNDU group
            semantics.

        Returns
        -------
        elements.Undulator or elements.Drift
            The corresponding OCELOT undulator-related element.

        """
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
        undulator.ps_id = row["NAME2"]
        return undulator

    def convert_phaseshifter(self, row: dict[str, Any]) -> elements.Drift:
        """
        Convert a PHASESHIFTER row entry into an OCELOT Drift element.

        Phase shifters from the component list are currently modeled as simple
        drifts in OCELOT. This method expects a row with GROUP "UNDU" and
        CLASS "PHASESHIFTER".

        Parameters
        ----------
        row : dict[str, Any]
            Dictionary representing a single component-list row with phase shifter
            semantics.

        Returns
        -------
        elements.Drift
            Drift element representing the phase shifter.
        """
        assert row["GROUP"] == "UNDU"
        assert row["CLASS"] == "PHASESHIFTER"
        ele = elements.Drift(l=row["LENGTH"], eid=row["NAME1"])
        ele.ps_id = row["NAME2"]
        return ele

    def convert_cryo(self, row: dict[str, Any]) -> elements.Drift:
        """
        Convert a CRYO entry into an OCELOT Drift element.

        Cryomodules are represented as drifts during conversion. This method
        expects a row with GROUP "CRYO" and CLASS "CRYO".

        Parameters
        ----------
        row : dict[str, Any]
            Dictionary representing a single component-list row with cryomodule
            semantics.

        Returns
        -------
        elements.Drift
            Drift element representing the cryomodule.
        """
        assert row["GROUP"] == "CRYO"
        assert row["CLASS"] == "CRYO"
        ele = elements.Drift(l=row["LENGTH"], eid=row["NAME1"])
        ele.ps_id = row["NAME2"]
        return ele

    def convert_vacuum(self, row: dict[str, Any]) -> elements.Drift:
        """
        Convert a VACUUM entry into an OCELOT Drift element.

        Vacuum-related components are represented as drifts during conversion.
        This method expects a row with GROUP "VACUUM" and one of the supported
        CLASS values ("VAC", "ECOL", "PLACEH", "ABSORBER").

        Parameters
        ----------
        row : dict[str, Any]
            Dictionary representing a single component-list row with vacuum
            component semantics.

        Returns
        -------
        elements.Drift
            Drift element representing the vacuum component.
        """
        assert row["GROUP"] == "VACUUM"
        # assert row["CLASS"] in {"VAC", "ECOL", "PLACEH", "ABSORBER", "VA}, (row["CLASS"], row["LENGTH"])
        ele = elements.Drift(l=row["LENGTH"], eid=row["NAME1"])
        ele.ps_id = row["NAME2"]
        return ele

    def convert_cavity(self, row: dict[str, Any]) -> Union[elements.Cavity, elements.TDCavity]:
        """
        Convert a CAVITY row from the component list into an OCELOT cavity element.

        This method expects a row originating from the component list model
        with GROUP equal to "CAVITY". A common set of physical parameters is
        constructed from the row data and used to instantiate the appropriate
        OCELOT cavity type, depending on the TYPE field:
        - "C", "C3"   → RF Cavity
        - "TDSA", "TDSB" → Transverse deflecting cavity

        Unit conversions are applied to match OCELOT conventions:
        - Voltage is converted from kV to MV.
        - Phase lag is converted to degrees.
        - Frequency is converted from MHz to Hz.

        Parameters
        ----------
        row : dict[str, Any]
            Dictionary representing a single component-list row with CAVITY group
            semantics.

        Returns
        -------
        elements.Cavity or elements.TDCavity
            The corresponding OCELOT cavity element.

        Raises
        ------
        UnknownLongListElement
            If the cavity TYPE is not recognised.
        """
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
            ele = elements.Cavity(**common_kw)
        elif row["TYPE"] == "TDSA" or row["TYPE"] == "TDSB":
            ele = elements.TDCavity(**common_kw)
        else:
            raise UnknownLongListElement(row)

        ele.ps_id = row["NAME2"]
        return ele

    def convert_diag(self, row: dict[str, Any]) -> Union[elements.Marker, elements.Monitor]:
        """
        Convert a DIAG row from the component list into an OCELOT diagnostic element.

        This method expects a row dict from the component list
        with GROUP equal to "DIAG". The specific OCELOT element type is determined
        by the CLASS field:
        - "INSTR" → Marker
        - "MONI"  → Monitor (with finite length)
        - "CM"    → Marker

        Parameters
        ----------
        row : dict[str, Any]
            Dictionary representing a single component-list row with DIAG group
            semantics.

        Returns
        -------
        elements.Marker or elements.Monitor
            The corresponding OCELOT diagnostic element.

        Raises
        ------
        UnknownLongListElement
            If the DIAG CLASS is not recognised.
        """
        assert row["GROUP"] == "DIAG"
        if row["CLASS"] == "INSTR":
            ele = elements.Marker(eid=row["NAME1"])
        elif row["CLASS"] == "MONI":
            ele = elements.Monitor(eid=row["NAME1"], l=row["LENGTH"])
        elif row["CLASS"] == "CM":
            ele = elements.Marker(eid=row["NAME1"])
        else:
            raise UnknownLongListElement(row)
        ele.ps_id = row["NAME2"]
        return ele

    def convert_mark(self, row: dict[str, Any]) -> elements.Marker:
        """
        Convert a MARK row from the component list into an OCELOT Marker element.

        This method expects a row originating from the component list model
        with GROUP equal to "MARK".

        Parameters
        ----------
        row : dict[str, Any]
            Dictionary representing a single component-list row with MARK group
            semantics.

        Returns
        -------
        elements.Marker
            The corresponding OCELOT Marker element.
        """
        assert row["GROUP"] == "MARK"
        ele = elements.Marker(eid=row["NAME1"])
        ele.ps_id = row["NAME2"]
        return ele

    convert_rampkick = convert_magnet
    convert_fastkick = convert_magnet
    convert_fbkick = convert_magnet


def longlist_to_ocelot(
    yaml_config_path: str,
    outdir: str,
) -> None:

    with open(yaml_config_path, "rb") as f:
        config = yaml.safe_load(f)

    try:
        dwriter = config["writer"]
    except KeyError:
        write_types_power_supplies = set()
    else:
        write_types_power_supplies = dwriter.get("write_types_power_supplies", set())

    try:
        fname = config["component_list"]
    except KeyError:
        raise MalformedConversionConfig("Missing longlist input file name in conversion config.")

    fpath = files("euxfel.longlists") / fname

    # Parse the config dictionary
    sections = _parse_config_dict(config)
    rowskips, rowedits = _parse_row_changes(config)

    llcv = LongListConverter(ComponentList(fpath),
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
            f.write(writer.to_module(write_types_power_supplies=write_types_power_supplies,
                                     comment=f"Converted from {fname}"))

    fname = Path(fpath).name
    init_path = Path(outdir) / "__init__.py"
    with open(init_path, "w") as f:

        f.write(f"# Automatically generated __init__.py from {fname}\n")
        f.write("from importlib.resources import files\n\n")

        f.write("try:\n")
        for module_name in module_names:
            f.write(f"    from . import {module_name}\n")

        # Write the __all__ list for this __init__.py.
        f.write(f'\n\n    __all__ = ["{module_names[0]}",\n')
        for module_name in module_names[1:-1]:
            f.write(f'               "{module_name}",\n')
        f.write(f'               "{module_names[-1]}"]\n')
        f.write("except Exception:\n")
        f.write("    import warnings\n")
        f.write("    warnings.warn(\"Failed importing subsequence modules, so one or more modules will be missing.  Consider regenerating one or more of these files to correct this.\")\n")
        f.write("    del warnings\n\n")


        f.write("# The longlist file we used to generate the subsequences in this directory:\n")
        f.write(f'USED_COMPONENT_LIST = files("euxfel.longlists") / "{fname}"\n')

    print("Written", init_path)

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
    is_delta_s_pos = "delta_s" in dd

    if is_adjacent and is_delta_s_pos:
        raise ValueError()

    if is_adjacent:
        assert reference is not None
        placement = AdjacentPlacement(element, AdjacentPositionType[dd["adjacent"].upper()], reference)
    elif is_delta_s_pos:
        placement = OffsetPlacement(element, dd["delta_s"], reference_name1=reference)
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
