"""Build an Ocelot sequence directly from a MAD-8 SURVEY tape.

The component list is a lossy re-render of these tapes: `makelist_release.m`
deletes the drifts and the coordinate rotations, rounds bend lengths to 1e-4,
collapses the `CAX`/`CAY` corrector pairs onto one position, and synthesises
element names from `floor(Z)`.  Building from the tape instead means none of
that damage is inherited, and the workarounds it forces -- zeroed corrector
lengths, reconstructed drifts, hand-added rotations -- become unnecessary.

The tape is already the parsed lattice: one record per element in order, with
`L`, `ANGLE`, `K1`, `K2`, `K3`, `TILT`, `E1`, `E2`, `VOLT`, `FREQ`, `LAG` and the
survey block at full precision.  No MAD-8 parser is needed; `euxfel.pand8` reads
it.

**Names come from the component list, not from here.**  MAD-8 names are reused
heavily -- `D0100` appears 256 times in T5D, and only 13% of records have a
unique name -- and the control-system names (`BZ.2030.T1`) are a `makelist`
invention that `sections.py` and the s2e scripts depend on.  Rather than
reimplement `makelist`'s `TYPE.floor(Z).SECTION` rule and its ~50 one-off
renames, the tape records are aligned positionally with the sheet rows and take
their identity from there.  See `align_to_sheet`.
"""

from typing import Any, Iterator

import polars as pl
from ocelot.cpbd.elements import (
    Cavity,
    Drift,
    Hcor,
    Marker,
    Monitor,
    Octupole,
    Quadrupole,
    RBend,
    SBend,
    Sextupole,
    Solenoid,
    TDCavity,
    Undulator,
    Vcor,
)
from ocelot.cpbd.elements.optic_element import OpticElement

from euxfel import kickers, metadata, pand8
from euxfel.conversion import load_conversion_config
from euxfel.mad8 import survey_tape
from euxfel.rotations import SRot, YRot

#: Keywords `makelist_release.m` drops on the way into the spreadsheet, so the
#: sheet has no row for them.  `DRIF` at :333-339, the rotations at :56.
DROPPED_KEYWORDS = frozenset({"DRIF", "SROT", "YROT"})

#: Zero-strength RBends MAD-8 uses as survey fitting handles
#: (`XFEL_TL.txm:307-327`).  The MAD-8 author has confirmed they carry no
#: information and can be dropped; the data agrees, with no HELP row in any
#: sheet against 4-14 records per tape.
DROPPED_NAME_PREFIXES = ("HELP",)

#: Transverse-deflecting structures, which share the `LCAV` keyword with the
#: accelerating cavities and are told apart by frequency.
TDS_FREQUENCY_MHZ = 2800.0

#: A `DRIF` whose name begins with one of these is an undulator, not a gap
#: (`XFEL_North_2025.txm:1219`: `U68.SA3: Drift, L = 5.0;`).  The period is the
#: digits in the stem, in mm -- the same rule `conversion.py` already uses.
UNDULATOR_PREFIXES = ("U40", "U68", "U74", "UE90", "SCU")


def _stem(name: str) -> str:
    """The MAD-8 name up to its first dot, which is the component type code."""
    return name.split(".")[0]


def _is_undulator(record: dict[str, Any]) -> bool:
    return record["KEYWORD"] == "DRIF" and _stem(record["NAME"]).startswith(
        UNDULATOR_PREFIXES
    )


def _undulator(record: dict[str, Any], eid: str) -> Undulator:
    """An undulator from a drift, with the period read out of its name."""
    stem = _stem(record["NAME"])
    period_mm = int("".join(character for character in stem if character.isdigit()))
    lperiod = period_mm * 1e-3
    return Undulator(lperiod=lperiod, nperiods=record["L"] / lperiod, eid=eid)


def _cavity(record: dict[str, Any], eid: str) -> Cavity | TDCavity:
    """An `LCAV`.  VOLT is in MV, FREQ in MHz and LAG in turns."""
    kind = TDCavity if record["FREQ"] == TDS_FREQUENCY_MHZ else Cavity
    return kind(
        l=record["L"],
        v=(record["VOLT"] or 0.0) * 1e-3,
        freq=(record["FREQ"] or 0.0) * 1e6,
        phi=(record["LAG"] or 0.0) * 360.0,
        eid=eid,
    )


def kicker_families(config: dict[str, Any] | None = None) -> dict[str, str]:
    """MAD-8 name stem -> kicker family, from the conversion config.

    A tape record `HKICKER, L=0.1` named `KIX.I1` is indistinguishable from one
    named `CIX.I1`, an ordinary steerer -- only the stem separates them, exactly
    as `makelist_release.m:447-478` does it.  The longlist route needs none of
    this because it has a `GROUP` column, which is what makes the two a
    cross-check on each other.
    """
    if config is None:
        config = load_conversion_config()
    declared = config.get("kicker_classes") or {}
    return {
        stem: family
        for family, stems in declared.items()
        if family != "overrides"
        for stem in stems
    }


def kicker_overrides(config: dict[str, Any] | None = None) -> dict[str, str]:
    """NAME1 -> family, for the by-name overrides at `makelist:803-812`."""
    if config is None:
        config = load_conversion_config()
    return (config.get("kicker_classes") or {}).get("overrides") or {}


def _kicker_plane(record: dict[str, Any]) -> str:
    """Which plane a kicker record deflects in.

    MAD-8 says it two ways: with the keyword for the ones modelled as kickers,
    and with the tilt for the ones modelled as bends (`KNY`, and the six `KL`s
    in the TL that really do carry `pi/2`).
    """
    if record["KEYWORD"] == "HKIC":
        return "H"
    if record["KEYWORD"] == "VKIC":
        return "V"
    return "V" if abs(record["TILT"] or 0.0) > 1e-9 else "H"


def _element_from(
    record: dict[str, Any],
    eid: str,
    kicker_family: str | None = None,
) -> OpticElement:
    """One Ocelot element from one tape record."""
    keyword, length = record["KEYWORD"], record["L"] or 0.0
    common = {"l": length, "eid": eid}
    tilt = record["TILT"] or 0.0

    if _is_undulator(record):
        return _undulator(record, eid)

    if kicker_family is not None:
        # The plane is in the class name, so the tilt is passed through as it
        # stands rather than being synthesised or stripped.
        kind = kickers.BY_FAMILY_AND_PLANE[kicker_family, _kicker_plane(record)]
        return kind(
            angle=record["ANGLE"] or 0.0,
            e1=record["E1"] or 0.0,
            e2=record["E2"] or 0.0,
            tilt=tilt,
            **common,
        )

    match keyword:
        case "DRIF":
            return Drift(**common)
        case "MARK":
            return Marker(eid=eid)
        case "MONI":
            return Monitor(**common)
        case "QUAD":
            return Quadrupole(k1=record["K1"] or 0.0, tilt=tilt, **common)
        case "SEXT":
            return Sextupole(k2=record["K2"] or 0.0, tilt=tilt, **common)
        case "OCTU":
            return Octupole(k3=record["K3"] or 0.0, tilt=tilt, **common)
        case "SBEN" | "RBEN":
            # MAD-8 SBEN with E1 = E2 = ANGLE/2 is geometrically an Ocelot RBend
            # with e1 = e2 = 0, but keeping the keyword's own class means the
            # tape and the model agree element for element.
            kind = SBend if keyword == "SBEN" else RBend
            return kind(
                angle=record["ANGLE"] or 0.0,
                k1=record["K1"] or 0.0,
                e1=record["E1"] or 0.0,
                e2=record["E2"] or 0.0,
                tilt=tilt,
                **common,
            )
        case "HKIC":
            return Hcor(angle=record["HKICK"] or 0.0, **common)
        case "VKIC":
            return Vcor(angle=record["VKICK"] or 0.0, **common)
        case "KICK":
            # Correctors with both planes; the design lattice has no strength on
            # any of them, and they are movers rather than magnets.
            return Marker(eid=eid) if length == 0.0 else Drift(**common)
        case "SOLE":
            return Solenoid(k=record["KS"] or 0.0, **common)
        case "LCAV":
            return _cavity(record, eid)
        case "ECOL":
            # Collimators; the aperture is on the record but the static lattice
            # has never modelled it, so keep the geometry only.
            return Marker(eid=eid) if length == 0.0 else Drift(**common)
        case "SROT":
            return SRot(angle=record["ANGLE"] or 0.0, eid=eid)
        case "YROT":
            return YRot(angle=record["ANGLE"] or 0.0, eid=eid)
        case "MATR":
            # MAD-8 uses a matrix for the short in-line undulators because it
            # has no undulator element; we do.  The tape prints no length for
            # MATR, so the caller supplies it from the arc-length step.
            return Undulator(lperiod=0.04, nperiods=length / 0.04, eid=eid)

    raise ValueError(f"no Ocelot element for MAD-8 keyword {keyword!r} ({eid})")


def read_tape(target: str) -> pl.DataFrame:
    """The SURVEY tape for a target, without its INITIAL seed row.

    SURVEY rather than TWISS: MAD-8 omits `SROT`/`YROT` from the TWISS tape
    (T5D has 9008 rows there against 9012 here), and those rotations are the
    whole reason the SASE2 geometry comes out right.
    """
    tape = pand8.read_survey(survey_tape(target))
    # HELP.* are survey fitting handles that carry no information and appear in
    # no sheet, so dropping them is right -- but note it *widens* the alignment
    # gap rather than closing it (B1D from -4 to -8), because the tape already
    # had fewer rows than the sheet there.  Whatever the sheet has that the tape
    # does not is still unaccounted for.
    tape = tape.filter(~pl.col("NAME").str.starts_with(DROPPED_NAME_PREFIXES[0]))
    # MATR records print no length, but SUML still advances across them.
    return tape.slice(1).with_columns(
        pl.when(pl.col("KEYWORD") == "MATR")
        .then(pl.col("SUML") - pl.col("SUML").shift(1))
        .otherwise(pl.col("L"))
        .alias("L")
    )


def align_to_sheet(tape: pl.DataFrame, sheet: pl.DataFrame) -> list[str | None]:
    """Give every tape record the component list's NAME1, or None.

    The two are the same elements in the same order once the rows neither side
    has are removed: the tape has no bend markers (those are synthesised by
    `makelist_release.m:235`) and the sheet has no drifts or rotations.  So
    walking both and skipping those yields a one-to-one correspondence.

    Returns one entry per tape record, `None` for the drifts and rotations that
    the component list has no row for.
    """
    bend_markers = ("BENDIN", "BENDSTR", "BENDARC", "BENDOUT")
    names = list(sheet.filter(~pl.col("CLASS").is_in(bend_markers))["NAME1"])
    keyword = list(tape["KEYWORD"])

    wanted = sum(1 for word in keyword if word not in DROPPED_KEYWORDS)
    if wanted != len(names):
        raise ValueError(
            f"cannot align: {wanted} tape records against {len(names)} sheet rows. "
            f"makelist_release.m drops more rows than DROPPED_KEYWORDS accounts "
            f"for -- see its HELP/MQF/MYQ/MXQ/YQK/XQK removals at :1239-1310."
        )

    aligned, index = [], 0
    for word in keyword:
        if word in DROPPED_KEYWORDS:
            aligned.append(None)
        else:
            aligned.append(names[index])
            index += 1
    return aligned


def build_sequence(target: str, sheet: pl.DataFrame) -> list[OpticElement]:
    """The Ocelot sequence for a dump target, built from its MAD-8 tape.

    `sheet` is the corresponding `I1toXXX` frame, used only for element identity
    and the bookkeeping columns -- every number comes from the tape.
    """
    tape = read_tape(target)
    names = align_to_sheet(tape, sheet)
    by_name = {row["NAME1"]: row for row in sheet.iter_rows(named=True)}
    families, overrides = kicker_families(), kicker_overrides()

    sequence, drift_index = [], 0
    for record, name in zip(tape.iter_rows(named=True), names):
        # Drifts have no row in the component list and so no name of their own.
        if name is None and record["KEYWORD"] == "DRIF" and not _is_undulator(record):
            sequence.append(Drift(l=record["L"], eid=f"D_{drift_index}"))
            drift_index += 1
            continue

        eid = name if name is not None else record["NAME"]
        # A kicker is identified by its MAD-8 name stem; the by-name overrides
        # mirror makelist_release.m:803-812 and win where they apply.
        family = None
        if name is not None:
            family = overrides.get(name) or families.get(_stem(record["NAME"]))
        element = _element_from(record, eid, kicker_family=family)
        if name is not None:
            element.ps_id = by_name[name]["NAME2"]
            metadata.attach(element, by_name[name])
        sequence.append(element)

    return _merge_drifts(sequence)


def _merge_drifts(sequence: list[OpticElement]) -> list[OpticElement]:
    """Collapse consecutive drifts, as the component-list model does.

    MAD-8 splits the space between components into many named drifts; nothing
    downstream distinguishes them, and merging keeps the element count in step
    with the existing model.
    """
    merged: list[OpticElement] = []
    for element in sequence:
        previous = merged[-1] if merged else None
        if isinstance(element, Drift) and isinstance(previous, Drift):
            previous.l += element.l
        else:
            merged.append(element)

    for index, element in enumerate(_only_drifts(merged)):
        element.id = f"D_{index}"
    return merged


def _only_drifts(sequence: list[OpticElement]) -> Iterator[Drift]:
    return (element for element in sequence if isinstance(element, Drift))
