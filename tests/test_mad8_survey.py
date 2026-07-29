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

# T5D alone disagrees, and by a known and fully explained amount.
#
# `Run_South_2025.txm:299-322` puts three zero-length frame rotations at the
# head of T1M -- SROT(-4.40392786446921e-3), YROT(+9.27121409529346e-8),
# SROT(+4.41369699554469e-3) -- and another, YROT(-2.365096e-6), at the SA2
# entrance.  They sit in the *survey* line (`I1TT5D_sur`) and not the Twiss line,
# so they patch the as-built XTD1 tunnel geometry without touching the optics.
#
# `makelist_release.m:56` strips every row whose name starts with ROT, so they
# never reach the component list and our converter cannot know about them.  The
# net roll, az1 + az2 = +9.769e-06, is what leaves the SASE2 branch rolled and
# the T5D dump displaced by ~2.3 mm.  It is also the origin of `BZ.2030.T1` in
# `KNOWN_INCONSISTENT_BENDS` in test_survey.py -- that bend is the one that
# straddles the rotation.
KNOWN_MISSING_ROTATIONS = {"T5D"}
EXPECTED_ROLL_DEFICIT_RAD = 9.769e-6
EXPECTED_DISPLACEMENT_M = 2.29e-3


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
def surveys() -> dict[str, pl.DataFrame]:
    """One joined survey per target, ours against MAD-8's."""
    joined = {}
    for target in COMPARED_TARGETS:
        tape = pand8.read_survey(survey_tape(target))
        ours = _ocelot_survey(target, tape.row(0, named=True))
        joined[target] = _at_common_arc_lengths(ours, tape)
    return joined


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


@pytest.mark.parametrize(
    "target", [t for t in COMPARED_TARGETS if t not in KNOWN_MISSING_ROTATIONS]
)
def test_survey_matches_mad8(target: str, surveys) -> None:
    """Position and orientation must match MAD-8 wherever the arcs coincide."""
    joined = surveys[target]

    assert joined.height > 50, (
        f"{target}: only {joined.height} common arc lengths, too few to be a "
        f"meaningful comparison -- has the element ordering changed?"
    )

    worst_position = _worst(joined, ("X", "Y", "Z"))
    worst_angle = _worst(joined, ("THETA", "PHI", "PSI"))

    assert worst_position < POSITION_TOLERANCE_M, (
        f"{target}: worst position disagreement with MAD-8 is {worst_position:.3e} m"
    )
    assert worst_angle < ANGLE_TOLERANCE_RAD, (
        f"{target}: worst angle disagreement with MAD-8 is {worst_angle:.3e} rad"
    )


def test_t5d_differs_only_by_the_missing_survey_rotations(surveys) -> None:
    """Pin the one known disagreement to its explained magnitude.

    Asserted as an equality rather than a bound so that *fixing* it fails too:
    once the rotations are modelled this test must be deleted and T5D returned
    to `test_survey_matches_mad8`.
    """
    joined = surveys["T5D"]

    worst_position = _worst(joined, ("X", "Y", "Z"))
    worst_angle = _worst(joined, ("THETA", "PHI", "PSI"))

    assert worst_angle == pytest.approx(EXPECTED_ROLL_DEFICIT_RAD, rel=0.05), (
        f"T5D's angular disagreement with MAD-8 is {worst_angle:.4e} rad, not the "
        f"{EXPECTED_ROLL_DEFICIT_RAD:.4e} rad of the missing survey rotations. If the "
        f"rotations are now modelled, delete this test and add T5D back to "
        f"test_survey_matches_mad8."
    )
    assert worst_position == pytest.approx(EXPECTED_DISPLACEMENT_M, rel=0.05), (
        f"T5D's positional disagreement with MAD-8 is {worst_position:.4e} m, not the "
        f"expected {EXPECTED_DISPLACEMENT_M:.4e} m"
    )


def test_t5d_agrees_upstream_of_the_rotations(surveys) -> None:
    """Everything before the T1 septa must still match to the same tolerance.

    Confines the disagreement to the rotations rather than letting it stand as
    a blanket exemption for the whole SASE2 branch.
    """
    # RotSystemTD1 sits at the head of T1M, at s = 2006.68585 m.
    upstream = surveys["T5D"].filter(pl.col("S") < 2006.0)

    assert upstream.height > 1000
    assert _worst(upstream, ("X", "Y", "Z")) < POSITION_TOLERANCE_M
    assert _worst(upstream, ("THETA", "PHI", "PSI")) < ANGLE_TOLERANCE_RAD
