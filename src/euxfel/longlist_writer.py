"""Write a component-list sheet back out from an Ocelot sequence.

The inverse of `conversion.LongListConverter`.  `makelist_release.m` is the
reference for every rule here; where its behaviour is surprising the comment
says so, because the goal is to reproduce the spreadsheet exactly rather than to
produce a tidier one.

Three of its quirks are load-bearing:

- **`S` is the element centre, but the optics and angles are at the exit.**
  Both `S` and the Twiss block come from the TWISS tape, which reports at the
  exit; `makelist_release.m:399-426` then shifts `S` (and `X`/`Y`/`Z`) back by
  `L/2` without re-interpolating anything else.
- **A bend becomes five rows**, and all but `BENDIN` carry the bend's *exit*
  optics -- they are duplicates of the magnet's own row
  (`makelist_release.m:235`).  `BENDIN` is a duplicate of the row before it, so
  it carries the entry values.
- **`ST` is a running offset reset at every bend** (`makelist_release.m:499-517`),
  measuring distance from the previous bend's tangent vertex.

Drifts do not appear in the component list at all: `S` supplies the spacing.
"""

import math
from typing import Any, Iterator

import numpy as np
import polars as pl
from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import Drift, Marker, RBend, SBend, Vcor
from ocelot.cpbd.elements.optic_element import OpticElement
from ocelot.cpbd.magnetic_lattice import MagneticLattice
from ocelot.cpbd.optics import twiss as calc_twiss

from euxfel import metadata
from euxfel.conversion import written_s_offsets

#: Column order of an `I1toXXX` sheet, which is the header of the
#: `LONGLIST_<PATH>.dat` file it is an external-data query over.
COLUMNS: list[str] = [
    "SECTION", "SUBSECTION", "CADRoom", "NAME1", "NAME2", "GROUP", "CLASS", "TYPE",
    "LENGTH", "STRENGTH", "E1/LAG", "E2/FREQ", "TILT",
    "S", "ST", "X", "Y", "Z", "THETA", "PHI", "CHI",
    "XPD", "YPD", "ZPD", "THETAPD", "PHIPD", "CHIPD",
    "ENERGY", "BETX", "ALFX", "MUX", "BETY", "ALFY", "MUY", "DX", "DPX", "DY", "DPY",
    "XAPER", "YAPER",
]  # fmt: skip

#: The direction-cosine block is only filled in beyond the point where the
#: machine leaves the main tunnel (`makelist_release.m:641-651`); everywhere
#: upstream of this it is written as zero.
PD_COLUMNS_START_Z = 1994.4920

#: `makelist_release.m:254-262` rounds the written LENGTH to four decimals.
LENGTH_DECIMALS = 4

BEND_MARKER_CLASSES = ("BENDIN", "BENDSTR", "BENDARC", "BENDOUT")

#: Rows that no Ocelot sequence can hold, spliced back in from the previous
#: release.  Empty for `I1toG1D`: the gun solenoid looked like a candidate, but
#: it is a real MAD-8 element at the cathode and only its *written* position is
#: displaced -- see `conversion.WRITTEN_S_OFFSETS`.
#:
#: This belongs in the conversion YAML alongside the rest of the steering, and
#: moves there once the remaining sheets bring enough entries to be worth the
#: plumbing.
ROWS_ABSENT_FROM_OCELOT: dict[str, list[dict[str, str]]] = {
    "I1toG1D": [],
}


def _is_bend(element: OpticElement) -> bool:
    """True for a bend that actually bends.

    A zero-angle RBend is a septum in its straight-through state or a kicker;
    `makelist_release.m:227-228` gives those no marker block.
    """
    return isinstance(element, (SBend, RBend)) and element.angle != 0.0


def _written_length(element: OpticElement) -> float:
    """The LENGTH column, which for a bend is neither arc nor magnet length.

    `makelist_release.m:254-262`: the projection onto the straight axis when the
    edge angles differ, the chord when they are equal.  Rounded to 1e-4, which
    is why the component list can never round-trip better than that.
    """
    length = element.l
    if not _is_bend(element):
        return length

    angle = element.angle
    if element.e1 != element.e2:
        written = length * math.sin(angle) / angle
    else:
        written = 2 * length * math.sin(angle / 2) / angle
    return round(written, LENGTH_DECIMALS)


def _strength(element: OpticElement) -> float:
    """The STRENGTH column: whichever single number characterises the element."""
    for attribute in ("angle", "k1", "k2", "k3", "k"):
        value = getattr(element, attribute, 0.0)
        if value:
            return value
    return 0.0


def _tangent_length(element: OpticElement) -> float:
    """`rho * tan(alpha/2)`, the distance from a bend face to its tangent vertex.

    This is what BENDSTR sits at and what ST is measured from.
    """
    rho = element.l / element.angle
    return rho * math.tan(element.angle / 2)


def _synthetic_marker(name: str, like: OpticElement) -> OpticElement:
    """A stand-in for a bend marker the forward conversion dropped.

    BENDSTR and BENDARC lie inside the magnet, so the converter discards them.
    Rebuild them from their surviving sibling: everything but the name is shared
    across the four markers of a block.
    """
    marker = Marker(eid=name)
    marker.ps_id = getattr(like, "ps_id", "")
    marker.metadata = dict(metadata.of(like))
    return marker


class ComponentListWriter:
    """Build an `I1toXXX` sheet from an Ocelot sequence.

    Parameters
    ----------
    sequence:
        The flattened cell, as `sequences.cathode_to_<target>`.
    twiss0:
        Initial Twiss, as `sequences.CATHODE_TWISS0`.
    survey_seed:
        MAD-8 survey initial conditions.  Uniform across the machine:
        `x0 = 0, y0 = -2.75, z0 = 23.2`, all angles zero.
    """

    DEFAULT_SURVEY_SEED = {
        "X0": 0.0,
        "Y0": -2.75,
        "Z0": 23.2,
        "theta0": 0.0,
        "phi0": 0.0,
        "chi0": 0.0,
    }

    def __init__(
        self,
        sequence: list[OpticElement],
        twiss0: Twiss,
        survey_seed: dict[str, float] | None = None,
        reinsert: list[dict[str, str]] | None = None,
        previous: pl.DataFrame | None = None,
        s_offsets: dict[str, float] | None = None,
    ):
        self.sequence = list(sequence)
        self.twiss0 = twiss0
        self.survey_seed = survey_seed or dict(self.DEFAULT_SURVEY_SEED)
        self.reinsert = reinsert or []
        self.previous = previous
        # Declared once in the conversion config and read by both directions, so
        # the shift taken out on the way in is the one put back on the way out.
        self.s_offsets = written_s_offsets() if s_offsets is None else s_offsets

        lattice = MagneticLattice(self.sequence)
        self._mid, self._end = lattice.survey_longlist(**self.survey_seed)
        # Ocelot emits more Twiss points than there are elements, so index them
        # by arc length rather than by position.  The last point at a given s is
        # the state after every zero-length element there, which is what the
        # component list records.
        self._twiss = {
            round(point.s, 9): point for point in calc_twiss(lattice, tws0=twiss0)
        }
        self._bend_markers = self._find_bend_markers()

    def _optics_at(self, arc: float) -> Twiss:
        try:
            return self._twiss[round(arc, 9)]
        except KeyError:
            raise KeyError(f"no Twiss point at s = {arc}") from None

    def _find_bend_markers(self) -> dict[int, tuple[OpticElement, OpticElement]]:
        """Pair each bend with its surviving BENDIN and BENDOUT marker elements.

        Of the four markers, only BENDIN and BENDOUT survive conversion -- they
        sit on the bend faces.  BENDSTR and BENDARC are dropped as lying inside
        another element, so those two rows have to be synthesised.
        """

        def marker_class(element: OpticElement) -> str | None:
            return metadata.get(element, "class")

        pairs = {}
        for index, element in enumerate(self.sequence):
            if not _is_bend(element):
                continue
            before = next(
                (
                    self.sequence[j]
                    for j in range(index - 1, -1, -1)
                    if marker_class(self.sequence[j]) == "BENDIN"
                ),
                None,
            )
            after = next(
                (
                    self.sequence[j]
                    for j in range(index + 1, len(self.sequence))
                    if marker_class(self.sequence[j]) == "BENDOUT"
                ),
                None,
            )
            if before is None or after is None:
                raise ValueError(f"{element.id} has no BENDIN/BENDOUT markers")
            pairs[index] = (before, after)
        return pairs

    def rows(self) -> pl.DataFrame:
        """The sheet, one row per component list entry."""
        frame = pl.DataFrame(list(self._iter_rows()), schema=self._schema())
        return self._reinsert_rows(frame)

    def _reinsert_rows(self, frame: pl.DataFrame) -> pl.DataFrame:
        """Splice back rows that cannot exist in an Ocelot model.

        `SOLA.23.I1` is the gun solenoid, which `makelist_release.m:392-397`
        shifts to s = -0.102 -- 102 mm *before* the cathode the lattice starts
        at.  There is nowhere in a sequence to put it, so the converter drops it
        and it is carried over from the previous release verbatim.

        Position is by named neighbour rather than by `S`: the sheet is in MAD-8
        lattice order, and a negative `S` would otherwise sort to the top.
        """
        if not self.reinsert:
            return frame
        if self.previous is None:
            raise ValueError("reinsert needs the previous release to carry rows from")

        for instruction in self.reinsert:
            name1, after = instruction["name1"], instruction["after"]
            carried = self.previous.filter(pl.col("NAME1") == name1)
            if carried.height != 1:
                raise ValueError(
                    f"{name1}: expected one row in the previous release, "
                    f"found {carried.height}"
                )
            position = frame.with_row_index().filter(pl.col("NAME1") == after)
            if position.height != 1:
                raise ValueError(f"{after}: not a unique anchor for {name1}")
            at = int(position["index"][0]) + 1
            frame = pl.concat(
                [
                    frame[:at],
                    carried.select(frame.columns).cast(frame.schema),
                    frame[at:],
                ]
            )
        return frame

    def _schema(self) -> dict[str, Any]:
        text = {"SECTION", "SUBSECTION", "CADRoom", "NAME1", "NAME2", "GROUP",
                "CLASS", "TYPE"}  # fmt: skip
        return {name: (pl.String if name in text else pl.Float64) for name in COLUMNS}

    def _iter_rows(self) -> Iterator[dict[str, Any]]:
        """Walk the sequence, expanding bends into their five-row block.

        `self._mid[i + 1]` and `self._end[i + 1]` are the survey at the centre
        and exit of `self.sequence[i]`; `self._end[i]` is the state entering it.
        Likewise `self._twiss[i + 1]` is the optics leaving element `i`.
        """
        arc = 0.0
        # Running ST offset, reset at every bend.  See _bend_rows.
        self._st_offset = 0.0

        for index, element in enumerate(self.sequence):
            length = getattr(element, "l", 0.0)

            # Drifts carry no row: the component list has none, and S supplies
            # the spacing between the elements either side.
            if isinstance(element, Drift):
                arc += length
                continue

            # The bend markers are emitted as part of their bend's block, not
            # in their own right.
            if metadata.get(element, "class") in BEND_MARKER_CLASSES:
                continue

            if _is_bend(element):
                yield from self._bend_rows(index, element, arc)
            else:
                yield self._plain_row(index, element, arc)

            arc += length

    def _plain_row(self, index: int, element: OpticElement, arc: float) -> dict:
        """A single non-bend row.

        `S` and the position are the element's centre; the optics and angles are
        those at its exit, which is the inconsistency the component list has
        carried since `makelist_release.m:399-426` shifted one and not the other.
        """
        centre = arc + getattr(element, "l", 0.0) / 2
        return self._row(
            element,
            s=centre,
            st=centre + self._st_offset,
            survey=self._mid[index + 1],
            optics=self._optics_at(arc + getattr(element, "l", 0.0)),
        )

    def _bend_rows(self, index: int, element: OpticElement, arc: float) -> Iterator:
        """The BENDIN / magnet / BENDSTR / BENDARC / BENDOUT block.

        Positions follow `makelist_release.m:233-331`.  The magnet row is
        geometrically identical to BENDARC, and every row but BENDIN carries the
        bend's exit optics, both because they are duplicates of the magnet's own
        row.
        """
        bendin, bendout = self._bend_markers[index]
        entry, exit_ = self._end[index], self._end[index + 1]
        middle = self._mid[index + 1]
        s_in, s_mid, s_out = arc, arc + element.l / 2, arc + element.l
        optics_in, optics_out = self._optics_at(s_in), self._optics_at(s_out)
        tangent = _tangent_length(element)

        # ST measures from the previous bend's tangent vertex, so entering the
        # bend the arc half-length is swapped for the tangent half-length, and
        # leaving it the count restarts at the vertex.
        st_body = s_mid + self._st_offset - element.l / 2 + tangent

        # BENDSTR and BENDARC are dropped by the forward conversion, so their
        # names are rebuilt from the magnet's (makelist_release.m:721-729):
        # 'M' + everything before the final dot + a letter + the section.
        stem, _, section = element.id.rpartition(".")
        bendstr = _synthetic_marker(f"M{stem}b.{section}", bendin)
        bendarc = _synthetic_marker(f"M{stem}c.{section}", bendin)

        # BENDSTR is not a blank marker: makelist_release.m:293-296 gives it the
        # bend's angle and tilt, and splits the angle into the E1/E2 columns as
        # its horizontal and vertical projections.
        tilt = getattr(element, "tilt", 0.0)
        bendstr_physics = {
            "LENGTH": 0.0,
            "STRENGTH": element.angle,
            "E1/LAG": element.angle * math.cos(tilt),
            "E2/FREQ": element.angle * math.sin(tilt),
            "TILT": tilt,
        }

        yield self._row(bendin, s_in, s_in + self._st_offset, entry, optics_in,
                        klass="BENDIN")  # fmt: skip
        yield self._row(element, s_mid, st_body, middle, optics_out)
        yield self._row(bendstr, s_mid, st_body, self._vertex(entry, exit_, tangent),
                        optics_out, klass="BENDSTR", physics=bendstr_physics)  # fmt: skip
        # BENDARC's ST is forced to zero -- it is the origin the next straight
        # section is measured from.
        yield self._row(bendarc, s_mid, 0.0, middle, optics_out, klass="BENDARC")
        yield self._row(bendout, s_out, tangent, exit_, optics_out, klass="BENDOUT")

        self._st_offset = tangent - s_out

    @staticmethod
    def _vertex(entry: dict, exit_: dict, tangent: float) -> dict:
        """BENDSTR's survey point: the tangent vertex, off the trajectory.

        Position is where the entry and exit tangents meet -- travel
        `rho * tan(alpha/2)` from the entry face along the incoming direction.
        Orientation is the bend's *exit* orientation, not the entry's, which is
        what the spreadsheet records.
        """
        vertex = dict(exit_)
        direction = np.array([entry["XPD"], entry["YPD"], entry["ZPD"]], dtype=float)
        position = np.array([entry["X"], entry["Y"], entry["Z"]], dtype=float)
        vertex["X"], vertex["Y"], vertex["Z"] = position + tangent * direction
        return vertex

    def _row(
        self,
        element: OpticElement,
        s: float,
        st: float,
        survey: dict,
        optics: Twiss,
        klass: str | None = None,
        physics: dict[str, float] | None = None,
    ) -> dict[str, Any]:
        """Assemble one row from the element, its survey point and its optics.

        `physics` overrides the five columns describing the component itself,
        for BENDSTR, which carries its bend's angle rather than blanks.
        """
        meta = metadata.of(element)
        marker = klass in BEND_MARKER_CLASSES
        if physics is None:
            physics = (
                dict.fromkeys(("LENGTH", "STRENGTH", "E1/LAG", "E2/FREQ", "TILT"), 0.0)
                if marker
                else self._physics_columns(element)
            )

        row: dict[str, Any] = {
            "SECTION": meta.get("section", ""),
            "SUBSECTION": meta.get("subsection", ""),
            "CADRoom": meta.get("cad_room", ""),
            "NAME1": element.id,
            "NAME2": getattr(element, "ps_id", ""),
            "GROUP": "MARK" if marker else meta.get("group", ""),
            "CLASS": klass or meta.get("class", ""),
            "TYPE": "BENDMARK" if marker else meta.get("type", ""),
            **physics,
            "S": s,
            "ST": st,
            "XAPER": meta.get("xaper", 0.0),
            "YAPER": meta.get("yaper", 0.0),
        }
        row.update(self._survey_columns(survey))
        row.update(self._optics_columns(optics))

        # Reapply the displacement the component list records this element with,
        # which the forward conversion took out so it could be modelled where it
        # acts.  See the `written_s_offsets` block in the conversion config.
        offset = self.s_offsets.get(element.id)
        if offset is not None:
            row["S"] += offset
            row["ST"] += offset
            row["Z"] += offset

        return row

    @staticmethod
    def _physics_columns(element: OpticElement) -> dict[str, float]:
        """The five columns describing the component itself."""
        tilt = getattr(element, "tilt", 0.0)
        # Ocelot represents a vertical corrector as a horizontal one rolled by
        # pi/2; MAD-8 uses a distinct VKICKER type and leaves TILT at zero.  Take
        # the roll back out so that a corrector which is *genuinely* tilted still
        # round-trips.
        if isinstance(element, Vcor):
            tilt -= math.pi / 2
        return {
            "LENGTH": _written_length(element),
            "STRENGTH": _strength(element),
            "E1/LAG": getattr(element, "e1", 0.0),
            "E2/FREQ": getattr(element, "e2", 0.0),
            "TILT": tilt,
        }

    @staticmethod
    def _survey_columns(survey: dict) -> dict[str, float]:
        columns = {
            name: float(survey[name])
            for name in ("X", "Y", "Z", "THETA", "PHI", "CHI")
        }  # fmt: skip
        # The direction cosines are written only past the tunnel branch point.
        beyond = columns["Z"] >= PD_COLUMNS_START_Z
        for name in ("XPD", "YPD", "ZPD"):
            columns[name] = float(survey[name]) if beyond else 0.0
        for name, source in (("THETAPD", "THETA"), ("PHIPD", "PHI"), ("CHIPD", "CHI")):
            columns[name] = columns[source] if beyond else 0.0
        return columns

    @staticmethod
    def _optics_columns(optics: Twiss) -> dict[str, float]:
        # MAD-8 writes the phase advance in units of 2*pi; Ocelot accumulates
        # it in radians.
        return {
            "ENERGY": optics.E,
            "BETX": optics.beta_x,
            "ALFX": optics.alpha_x,
            "MUX": optics.mux / (2 * math.pi),
            "BETY": optics.beta_y,
            "ALFY": optics.alpha_y,
            "MUY": optics.muy / (2 * math.pi),
            "DX": optics.Dx,
            "DPX": optics.Dxp,
            "DY": optics.Dy,
            "DPY": optics.Dyp,
        }
