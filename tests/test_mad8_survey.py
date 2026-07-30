"""Check our survey against MAD-8's own output.

The component list is a derived artefact: `makelist_release.m` reads MAD-8's
SURVEY and TWISS tapes and, on the way out, drops drifts and coordinate
rotations, synthesises element names from `floor(Z)` and rounds bend lengths to
1e-4.  Validating against it therefore validates against a lossy render.

The tapes archived in `src/euxfel/mad8/` are the undistorted upstream, so this
is the sharper test: build each dump path in Ocelot, seed the survey from the
tape's own INITIAL row, and require the two geometries to coincide.

Comparison is by arc length rather than by name.  MAD-8's element names are not
the component list's -- `BZ.2030.T1` is MAD-8's `BZ.2.T1` -- but `SUML` and
Ocelot's `s` are the same coordinate, and the two models agree on total length
exactly.  Every point where an element boundary falls at the same arc length in
both is compared.

Only geometry is covered here.  Comparing the TWISS tapes is worth doing too,
but needs the per-path energy profile and re-matching handled first.
"""

import polars as pl
import pytest
from ocelot.cpbd.magnetic_lattice import MagneticLattice

from euxfel import pand8, sequences
from euxfel.mad8 import TAPE_TARGETS, survey_tape
from euxfel.rotations import SRot, YRot

# Targets that have both an archived tape and a generated sequence.  G1D has a
# tape but is not yet a conversion target.
COMPARED_TARGETS = [
    target
    for target in TAPE_TARGETS
    if hasattr(sequences, f"cathode_to_{target.lower()}")
]

# Both models place elements to well under a micron; anything above this is a
# real geometric disagreement rather than accumulated floating-point error.
POSITION_TOLERANCE_M = 1e-6
ANGLE_TOLERANCE_RAD = 1e-9

# Arc lengths are matched at nanometre resolution before comparing.
ARC_LENGTH_MATCH_M = 1e-9

# T5D used to be the one target that failed here, by 2.3 mm and 9.769 urad,
# because MAD-8 applies four zero-length frame rotations on the SASE2 branch
# that the component list has no record of -- `makelist_release.m:56` discards
# every row whose name begins ROT.  They are now modelled explicitly; see
# `euxfel.rotations` for the full account.  Nothing here special-cases T5D any
# more, which is the point: if the rotations are ever dropped from the
# conversion config, this test is what notices.
#
# RotSystemTD1 sits at the head of T1M, immediately before the first untilted
# septum, and leaves a deliberate residual roll of az1 + az2.
NET_ROLL_RAD = -0.00440392786446921 + 0.00441369699554469


def _ocelot_survey(target: str, seed: dict) -> pl.DataFrame:
    """Survey our sequence for a target, seeded from the tape's INITIAL row."""
    mlat = MagneticLattice(getattr(sequences, f"cathode_to_{target.lower()}"))
    _, end_points = mlat.survey(
        X0=seed["X"],
        Y0=seed["Y"],
        Z0=seed["Z"],
        theta0=seed["THETA"],
        phi0=seed["PHI"],
        psi0=seed["PSI"],
    )
    return pl.DataFrame(
        {
            name: [float(point[name]) for point in end_points]
            for name in ("S", "X", "Y", "Z", "THETA", "PHI", "PSI")
        }
    )


def _at_common_arc_lengths(ours: pl.DataFrame, tape: pl.DataFrame) -> pl.DataFrame:
    """Join the two surveys at arc lengths present in both.

    Several zero-length markers share an arc length; the last row at each is
    the state after all of them, on both sides.
    """

    def keyed(df: pl.DataFrame, s_column: str) -> pl.DataFrame:
        key = (pl.col(s_column) / ARC_LENGTH_MATCH_M).round().cast(pl.Int64)
        return df.with_columns(key.alias("_s")).unique("_s", keep="last")

    return keyed(ours, "S").join(keyed(tape, "SUML"), on="_s", suffix="_mad8")


@pytest.fixture(scope="module")
def surveys() -> dict[str, tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]]:
    """Per target: (joined at common arc lengths, ours, MAD-8's)."""
    result = {}
    for target in COMPARED_TARGETS:
        tape = pand8.read_survey(survey_tape(target))
        ours = _ocelot_survey(target, tape.row(0, named=True))
        result[target] = (_at_common_arc_lengths(ours, tape), ours, tape)
    return result


def _worst(joined: pl.DataFrame, columns: tuple[str, ...]) -> float:
    return max(
        float((joined[name] - joined[f"{name}_mad8"]).abs().max()) for name in columns
    )


@pytest.mark.parametrize("target", COMPARED_TARGETS)
def test_total_length_matches_mad8(target: str) -> None:
    """Our lattice and MAD-8's must be the same length.

    This is the cheapest way to catch an element dropped or duplicated by a
    conversion, and it holds even for T5D -- the missing rotations are
    zero-length, so they change orientation without changing arc length.
    """
    mlat = MagneticLattice(getattr(sequences, f"cathode_to_{target.lower()}"))
    ours = sum(getattr(element, "l", 0.0) for element in mlat.sequence)
    theirs = pand8.read_survey(survey_tape(target))["SUML"][-1]

    assert ours == pytest.approx(theirs, abs=1e-6), (
        f"{target}: our lattice is {ours} m, MAD-8's is {theirs} m"
    )


@pytest.mark.parametrize("target", COMPARED_TARGETS)
def test_survey_matches_mad8(target: str, surveys) -> None:
    """Position and orientation must match MAD-8 wherever the arcs coincide.

    Only points whose arc length is identical to the nanometre are compared.
    Our drift lengths come from differencing the spreadsheet's rounded `S`, so
    cumulative arc length wanders from MAD-8's by up to ~0.5 um over a full
    path and the two stop landing on the same value partway down the longer
    lines.  `test_end_of_line_matches_mad8` is what covers the far end.
    """
    joined, _, _ = surveys[target]

    assert joined.height >= 10, (
        f"{target}: only {joined.height} common arc lengths -- has the element "
        f"ordering changed?"
    )

    worst_position = _worst(joined, ("X", "Y", "Z"))
    worst_angle = _worst(joined, ("THETA", "PHI", "PSI"))

    assert worst_position < POSITION_TOLERANCE_M, (
        f"{target}: worst position disagreement with MAD-8 is {worst_position:.3e} m"
    )
    assert worst_angle < ANGLE_TOLERANCE_RAD, (
        f"{target}: worst angle disagreement with MAD-8 is {worst_angle:.3e} rad"
    )


@pytest.mark.parametrize("target", COMPARED_TARGETS)
def test_end_of_line_matches_mad8(target: str, surveys) -> None:
    """Each dump must sit where MAD-8 puts it.

    The arc-length join thins out towards the end of the longer paths, so state
    this separately: whatever happens in between, the final position and
    orientation have to agree.  This is the number that matters operationally
    and the one that was 2.3 mm out for T5D.
    """
    _, ours, tape = surveys[target]
    last_ours, last_tape = ours.row(-1, named=True), tape.row(-1, named=True)

    for name in ("X", "Y", "Z"):
        assert last_ours[name] == pytest.approx(last_tape[name], abs=1e-6), (
            f"{target}: dump {name} is {last_ours[name]}, MAD-8 says {last_tape[name]}"
        )
    for name in ("THETA", "PHI", "PSI"):
        assert last_ours[name] == pytest.approx(last_tape[name], abs=1e-9), (
            f"{target}: dump {name} is {last_ours[name]}, MAD-8 says {last_tape[name]}"
        )


def test_sase2_branch_carries_the_mad8_rotations() -> None:
    """The four survey-only rotations must be in the T5D lattice, in order.

    `test_survey_matches_mad8` already catches their removal, but only as one
    number among thousands and with no hint as to the cause.  This names the
    thing that was wrong: nothing in the component list can put these elements
    into the model, so only the conversion config holds them, and a config edit
    is exactly how they would go missing again.
    """
    mlat = MagneticLattice(sequences.cathode_to_t5d)
    found = [
        (element.id, element.angle)
        for element in mlat.sequence
        if isinstance(element, (SRot, YRot))
    ]

    assert found == [
        ("ROT.Z1.T1", -0.00440392786446921),
        ("ROT.Y.T1", 9.27121409529346e-08),
        ("ROT.Z2.T1", 0.00441369699554469),
        ("ROT.Y.SA2", -2.365095999996847e-06),
    ], (
        "the SASE2 survey rotations are missing or altered; they come only from "
        "the conversion config, since makelist_release.m:56 strips them out of "
        "the component list"
    )

    # Deliberately not cancelling: this residual is the whole reason T5D used
    # to be 2.3 mm out.
    net_roll = found[0][1] + found[2][1]
    assert net_roll == pytest.approx(NET_ROLL_RAD, rel=1e-12)

    # And the rotations must be zero-length, or they would displace the branch
    # rather than merely reorient it.
    assert all(
        element.l == 0.0
        for element in mlat.sequence
        if isinstance(element, (SRot, YRot))
    )
