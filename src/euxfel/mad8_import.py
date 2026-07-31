"""Build an Ocelot sequence directly from a MAD-8 SURVEY tape.

The component list is a lossy re-render of these tapes: `makelist_release.m`
deletes the drifts and the coordinate rotations, rounds bend lengths to 1e-4,
collapses the `CAX`/`CAY` corrector pairs onto one position, and merges the two
halves of a split magnet.  Building from the tape instead means none of that
damage is inherited, and the workarounds it forces -- zeroed corrector lengths,
reconstructed drifts, hand-added rotations -- become unnecessary.

The tape is already the parsed lattice: one record per element in order, with
`L`, `ANGLE`, `K1`, `K2`, `K3`, `TILT`, `E1`, `E2`, `VOLT`, `FREQ`, `LAG` and the
survey block at full precision.  No MAD-8 parser is needed; `euxfel.pand8` reads
it.

**Nothing is dropped.**  Every tape record becomes an element, including the
drifts, the `SROT`/`YROT` frame rotations and the zero-strength `HELP.*` survey
handles.  What the component list leaves out is a fact about the component list,
not about the machine, and a model that starts by discarding rows cannot claim to
supersede the thing it was derived from.

**Names are generated, not copied.**  A MAD-8 name is not an identity: `D0100`
occurs 256 times in the T5D tape and carries no position.  The control-system
names -- `BZ.2030.T1`, `C.A1.1.I1` -- are synthesised by `makelist_release.m`,
and `euxfel.mad8_names` reproduces that synthesis rule for rule, so the
spreadsheet becomes an output of this repository rather than an input to it.
Elements the spreadsheet has no row for keep their MAD-8 name.

**Repeated drifts share one object.**  A MAD-8 drift name fixes its length
uniquely -- 5800 drift placements in T4D are only 522 distinct lengths -- so one
`Drift` instance is created per name and referenced wherever it occurs, exactly
as a hand-written Ocelot lattice would.
"""

from __future__ import annotations

import math
from typing import Any

import numpy as np
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

from euxfel import kickers, mad8_names, pand8
from euxfel.mad8 import load_config, survey_tape
from euxfel.rotations import SRot, YRot

#: Keywords the component list has no row for, so `makelist_release.m` never
#: gives them a NAME1 (`:56` for the rotations, `:333-339` for the drifts).  They
#: stay in the model and keep their MAD-8 name.
UNNAMED_KEYWORDS = frozenset({"DRIF", "SROT", "YROT"})

#: Name stems `makelist_release.m:1306-1310` removes before writing.  They are
#: alignment scaffolding for the south branch geometry -- `MQF`/`MYQ`/`MXQ` are
#: markers and `YQK`/`XQK` the slice stack of the combined-function `QK.2.T1.TL`.
#: Kept in the model, but unnamed, since the spreadsheet cannot name them.
UNNAMED_NAME_STEMS = ("MQF", "MYQ", "MXQ", "YQK", "XQK", "ROT", "BZ.0.")

#: Transverse-deflecting structures, which share the `LCAV` keyword with the
#: accelerating cavities and are told apart by frequency.
TDS_FREQUENCY_MHZ = 2800.0

#: `MATR` records model a short in-line undulator, because MAD-8 has no undulator
#: element.  We use Ocelot's, whose focusing is the one we want; only the period
#: has to be supplied, since the tape prints none.
MATRIX_UNDULATOR_PERIOD_M = 0.04


def _stem(name: str) -> str:
    """The MAD-8 name up to its first dot, which is the component type code."""
    return name.split(".")[0]


def _undulator_period(name: str) -> float:
    """Period in metres from an undulator's name stem, where the digits are mm.

    `U68.SA3` is a 68 mm undulator (`XFEL_North_2025.txm:1219`).  This is the
    rule `conversion.py` already applies coming the other way.
    """
    digits = "".join(character for character in _stem(name) if character.isdigit())
    return int(digits) * 1e-3


def read_tape(target: str) -> pl.DataFrame:
    """The SURVEY tape for a target, ready to be turned into elements.

    SURVEY rather than TWISS: MAD-8 omits `SROT`/`YROT` from the TWISS tape (T5D
    has 9008 rows there against 9012 here), and those rotations are the whole
    reason the SASE2 geometry comes out right.

    Three repairs, all of them things `makelist_release.m` also does:

    * the `INITIAL` seed row is dropped -- it is the survey origin, not an
      element;
    * `MATR` records print `L = 0` although `SUML` advances across them, so the
      length is recovered from the arc-length step (`:117-118`);
    * magnets MAD-8 splits in two so a marker can sit at the centre are merged
      back into one of twice the length and twice the angle (`:172-190`).
    """
    tape = pand8.read_survey(survey_tape(target)).slice(1)
    tape = tape.with_columns(
        pl.when(pl.col("KEYWORD") == "MATR")
        .then(pl.col("SUML") - pl.col("SUML").shift(1))
        .otherwise(pl.col("L"))
        .alias("L")
    )
    tape = _merge_half_magnets(tape, load_config().get("half_magnets") or {})
    return _lengths_from_survey(tape)


#: How far a length recovered from the survey block may sit from the printed `L`
#: before the printed value is kept instead.  `F12.6` rounds to 5e-7, so twice
#: that admits the rounding and nothing else.
LENGTH_RECOVERY_TOLERANCE_M = 1e-6


def _lengths_from_survey(tape: pl.DataFrame) -> pl.DataFrame:
    """Recover each bend's arc length from the survey block, not the `L` column.

    The tape prints `L` with `F12.6` but the survey coordinates with `E16.9`, so
    positions are four orders of magnitude more precise than lengths.  That only
    matters where the printed length is not already exact -- and for a bend it is
    not, because MAD-8 computes it.  `XFEL_I1.txm:488-491` declares

        ang_lh = -0.099484
        arc_lh = LEN_BL*ang_lh/sin(ang_lh)
        BL.1.1.I1: Sbend, L = arc_lh, ANGLE = ang_lh

    so the arc length is derived from a round *projected* length and comes out at
    0.2003302835 m, which the tape truncates to `0.200330`.  That 1.4e-6 relative
    error puts the magnet's exit 283 nm short, and every element downstream
    inherits it.  Recovery reproduces `arc_lh` to 1e-9.

    The chord between the entry and exit points fixes the geometry exactly:

        |chord| = 2 * rho * sin(angle / 2)   =>   arc = rho * angle

    and because chord length is invariant under rotation this holds whatever the
    bend's tilt or plane.

    Straight elements are deliberately left alone.  Their lengths are literals in
    the MAD-8 source -- `D0050: DRIFT, L = 0.050` -- so the printed value is the
    definition and the surveyed chord merely adds round-off to it.  Recovering
    those made the geometry *worse*, and would also break the sharing of one
    `Drift` object per name, since each placement would recover a slightly
    different value and the last would win for all of them.
    """
    position = tape.select("X", "Y", "Z").to_numpy()
    angle = tape["ANGLE"].fill_null(0.0).to_numpy()
    printed = tape["L"].fill_null(0.0).to_numpy()
    lengths = printed.copy()

    # Index 0 has no preceding survey point to measure a chord to -- the INITIAL
    # row has already been dropped -- and no path begins on a bend.
    bends = np.flatnonzero((angle != 0.0) & (printed != 0.0))
    bends = bends[bends > 0]
    chord = np.linalg.norm(position[bends] - position[bends - 1], axis=1)
    half = angle[bends] / 2.0
    recovered = chord * half / np.sin(half)

    # A recovered value far from the printed one is not print rounding but a
    # disagreement about what the element is; there the `L` column is the
    # authority.
    trusted = np.abs(recovered - printed[bends]) <= LENGTH_RECOVERY_TOLERANCE_M
    lengths[bends[trusted]] = recovered[trusted]
    return tape.with_columns(pl.Series("L", lengths))


def _merge_half_magnets(tape: pl.DataFrame, rule: dict[str, Any]) -> pl.DataFrame:
    """Rejoin magnets MAD-8 splits at their midpoint (makelist:172-190).

    A `BL.48H.I1`/`BL.48H.I1` pair is one physical magnet cut in half so a marker
    can sit between the halves.  The second row is widened to the full magnet and
    the first discarded, which is what puts the merged element's survey record at
    the true exit face.
    """
    marker = rule.get("marker")
    if not marker:
        return tape

    exclude = tuple(rule.get("exclude") or ())
    rows, keep, pending = tape.to_dicts(), [], False
    for row in rows:
        name = row["NAME"]
        if marker in name and not any(token in name for token in exclude):
            row = dict(row)
            row["NAME"] = name.replace(marker, ".")
            row["L"] = 2 * (row["L"] or 0.0)
            row["ANGLE"] = 2 * (row["ANGLE"] or 0.0)
            if not pending:
                pending = True
                continue  # the upstream half; its twin carries the whole magnet
            pending = False
        keep.append(row)
    return pl.DataFrame(keep, schema=tape.schema)


def _is_named(record: dict[str, Any], keyword: str) -> bool:
    """Whether the component list has a row for this record, and so a name for it.

    `keyword` is the reclassified one: a `DRIF` named `U74.I1` is an undulator by
    the time `makelist_release.m` deletes the drifts, so it survives and is named
    while `D0100` is not.
    """
    name = record["NAME"]
    if keyword in UNNAMED_KEYWORDS or name.startswith(UNNAMED_NAME_STEMS):
        return False
    # HELP.* are zero-strength RBends used as survey fitting handles
    # (XFEL_TL.txm:307-327); makelist:1239-1245 drops the ones with no angle.
    return not (name.startswith("HELP") and not record["ANGLE"])


def _naming_records(tape: pl.DataFrame, keywords: list[str]) -> list:
    """One `mad8_names.Record` per tape record the component list would name.

    The naming position is the element's *centre*: `makelist_release.m:399-426`
    shifts every element with a length back by half of it, and `:243-259` takes
    the midpoint of a bend's entry and exit faces.  Both are the mean of the two
    survey points either side of the record, so consecutive tape rows give it
    directly -- no need to survey the built lattice, and no dependence on how
    faithfully we rebuilt it.
    """
    rows = tape.to_dicts()
    records = []
    for index, (row, keyword) in enumerate(zip(rows, keywords)):
        if not _is_named(row, keyword):
            continue
        entry = rows[index - 1] if index else row
        records.append(
            mad8_names.Record(
                mad_name=row["NAME"],
                z=0.5 * (entry["Z"] + row["Z"]),
                x=0.5 * (entry["X"] + row["X"]),
                dz_dlocal_z=math.cos(row["THETA"]) * math.cos(row["PHI"]),
            )
        )
    return records


def kicker_families(config: dict[str, Any] | None = None) -> dict[str, str]:
    """MAD-8 name stem -> kicker family, from the conversion config.

    A tape record `HKICKER, L=0.1` named `KIX.I1` is indistinguishable from one
    named `CIX.I1`, an ordinary steerer -- only the stem separates them, exactly
    as `makelist_release.m:447-478` does it.  The longlist route needs none of
    this because it has a `GROUP` column, which is what makes the two a
    cross-check on each other.
    """
    if config is None:
        config = load_config()
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
        config = load_config()
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


def _element_from(
    record: dict[str, Any],
    eid: str,
    keyword: str,
    kicker_family: str | None = None,
) -> OpticElement:
    """One Ocelot element from one tape record.

    `keyword` is the reclassified keyword.  Only `UNDULATOR` changes what gets
    built -- the rest of `drift_reclassification` decides whether a record has a
    spreadsheet row, which is bookkeeping, not physics: a vacuum-chamber drift is
    still a drift to the beam.
    """
    length = record["L"] or 0.0
    common = {"l": length, "eid": eid}
    tilt = record["TILT"] or 0.0

    if keyword == "UNDULATOR" and record["KEYWORD"] in ("DRIF", "MARK"):
        lperiod = _undulator_period(record["NAME"])
        return Undulator(lperiod=lperiod, nperiods=length / lperiod, eid=eid)

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

    match record["KEYWORD"]:
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
            kind = SBend if record["KEYWORD"] == "SBEN" else RBend
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
            # Both planes at once; in the design lattice these are the quadrupole
            # movers, which carry no strength.
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
            lperiod = MATRIX_UNDULATOR_PERIOD_M
            return Undulator(lperiod=lperiod, nperiods=length / lperiod, eid=eid)

    raise ValueError(
        f"no Ocelot element for MAD-8 keyword {record['KEYWORD']!r} ({eid})"
    )


def build_sequence(target: str) -> list[OpticElement]:
    """The Ocelot sequence for a dump target, built entirely from its MAD-8 tape.

    Every number is the tape's.  The component list is not consulted: the names
    it would have assigned are regenerated from the survey by `mad8_names`, which
    is what makes this the forward direction rather than a lookup.
    """
    config = load_config()
    reclassification = config.get("drift_reclassification") or []
    families, overrides = kicker_families(config), kicker_overrides(config)

    tape = read_tape(target)
    rows = tape.to_dicts()
    keywords = [
        mad8_names.reclassify(row["KEYWORD"], row["NAME"], reclassification)
        for row in rows
    ]

    named = _naming_records(tape, keywords)
    mad8_names.name_records(named, config["naming"])
    names = iter(named)

    sequence: list[OpticElement] = []
    drifts: dict[str, Drift] = {}
    for row, keyword in zip(rows, keywords):
        if not _is_named(row, keyword):
            # No spreadsheet row, so no generated name: keep MAD-8's own.  A
            # plain drift is shared between all its placements, since its name
            # fixes its length.
            if row["KEYWORD"] == "DRIF":
                drift = drifts.get(row["NAME"])
                if drift is None:
                    drift = drifts[row["NAME"]] = Drift(l=row["L"], eid=row["NAME"])
                sequence.append(drift)
                continue
            sequence.append(_element_from(row, row["NAME"], keyword))
            continue

        name = next(names).name
        # A kicker is identified by its MAD-8 name stem; the by-name overrides
        # mirror makelist_release.m:803-812 and win where they apply.
        family = overrides.get(name) or families.get(_stem(row["NAME"]))
        element = _element_from(row, name, keyword, kicker_family=family)
        # MAD-8's own name is the power-supply circuit the magnet sits on, which
        # is what the component list's NAME2 column records.
        element.ps_id = row["NAME"]
        sequence.append(element)

    return sequence


def generated_names(target: str) -> list[str]:
    """Just the NAME1s this target's tape produces, in order.

    Separate from `build_sequence` so the naming rules can be checked against the
    component list without building a lattice.
    """
    tape = read_tape(target)
    reclassification = load_config().get("drift_reclassification") or []
    keywords = [
        mad8_names.reclassify(row["KEYWORD"], row["NAME"], reclassification)
        for row in tape.to_dicts()
    ]
    records = _naming_records(tape, keywords)
    naming = load_config()["naming"]
    return [record.name for record in mad8_names.name_records(records, naming)]
