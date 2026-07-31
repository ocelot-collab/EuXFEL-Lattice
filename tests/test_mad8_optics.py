"""Compare the tape-built model's optics against MAD-8's own, two ways.

`test_mad8_names.py` shows the geometry closes to 3e-6 m.  This is the other
half: does Ocelot's physics agree with MAD-8's on the same lattice?

Two tests, deliberately different in kind:

**Whole path** tracks cathode to dump in one go, seeded only from the tape's
`INITIAL` row, and compares every element.  Nothing is re-seeded along the way,
so a disagreement anywhere is carried to the end -- which is what makes it a real
test rather than a chain of independent short ones.  `test_mad8_convert.py`'s
boundary check is the weak version of this: each module there starts from MAD-8's
own numbers, so errors cannot accumulate.

**Per element** propagates each element *alone* from the tape's own upstream
values.  That localises a disagreement to the element responsible instead of
reporting one number for 3 km of machine, and it is what identified the cavities
below.  If a future Ocelot bump changes an element's transfer map, this is what
names it.
"""

import numpy as np
import polars as pl
import pytest
from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import Cavity
from ocelot.cpbd.magnetic_lattice import MagneticLattice
from ocelot.cpbd.track import twiss as ocelot_twiss

from euxfel import pand8
from euxfel.mad8 import TAPE_TARGETS, twiss_tape
from euxfel.mad8_import import build_sequence

#: TWISS tape column -> Ocelot `Twiss` attribute.
SEED_COLUMNS = (
    ("BETX", "beta_x"), ("ALFX", "alpha_x"),
    ("BETY", "beta_y"), ("ALFY", "alpha_y"),
    ("DX", "Dx"), ("DPX", "Dxp"),
    ("DY", "Dy"), ("DPY", "Dyp"),
)  # fmt: skip

#: Tracking the full path from the cathode, beta agrees with MAD-8 to this
#: relative tolerance.  The residue is not distributed; it has two known sources,
#: both localised:
#:
#: * the off-crest L1 cavities, worth ~1e-4 on every path -- see
#:   `test_off_crest_cavity_disagreement_is_bounded`;
#: * on T4D only, beta_y reaching 7.8e-4 by the dump.  This is the *same*
#:   mismatch amplified, not a second cause.  A per-element audit of T4D finds no
#:   local disagreement in SASE1 at all -- 61 of its 63 undulators are plain
#:   `DRIF` records in MAD-8, where `Kx = 0` is the matching model and they agree
#:   to 9.5e-10, and the 2 `MATR` ones reach only 2.6e-6.  Re-seeding from MAD-8
#:   at MATCH.2813.SA3 brings the dump to 9.6e-8, so the last 300 m are exact and
#:   the mismatch merely arrives there.  It looks large because beta at a dump is
#:   ~200 km, where a small error in alpha shifts the waist and a long drift
#:   magnifies it; x and y differ because the same mismatch lands at different
#:   betatron phases.  See docs-site/docs/mad8-comparison.md.
WHOLE_PATH_BETA_TOLERANCE = 1e-3

#: Where the SASE1 undulators begin, in metres of arc.  Upstream of this every
#: path shares a lattice, so they must all agree to the same level.
SASE1_START_M = 2002.0

#: What every path agrees to before any undulator is involved.
PRE_UNDULATOR_BETA_TOLERANCE = 2e-4

#: Dispersion is absolute, in metres, and holds far tighter than beta.
WHOLE_PATH_DISPERSION_TOLERANCE_M = 1e-5

#: Every element type except the cavities reproduces MAD-8's transfer map to
#: better than this.  Measured worst case is a drift at 4.8e-7.
ELEMENT_TOLERANCE = 2e-6

#: On-crest cavities agree to 5e-9 -- as tight as the quadrupoles.
ON_CREST_CAVITY_TOLERANCE = 1e-7

#: Off-crest cavities do not, and this is the one place Ocelot and MAD-8 disagree
#: on physics rather than on rounding.  The L1 chirping cavities run at phi = 25
#: degrees, and there the two transfer maps part company by 3.0e-5 at 130 MeV,
#: falling steadily as the beam is accelerated (2.0e-5 at 149 MeV, 1.4e-5 at
#: 169 MeV, under 2e-6 by 340 MeV).  On-crest cavities at the *same* energies
#: agree to 5e-9, so it is the phase and not the energy that separates them.
#:
#: MAD-8's `tmlcav` builds a TRANSPORT matrix with thin edge lenses in which the
#: RF phase appears *only* through the energy gain; Ocelot uses the
#: Rosenzweig-Serafini matrix, where `cos(phi)` appears explicitly in alpha and in
#: all four transverse terms.  That is the mechanism the numbers point to -- but
#: the `tmlcav` we can read is 8.51/15s and the tapes were made by 8.51.18, two
#: revisions later, so it is inferred rather than confirmed.
#:
#: Which model is preferable is a physics question this test does not settle.  It
#: pins the size and location of the difference so it stays known.  The full
#: account, including what source is still needed, is in
#: docs-site/docs/mad8-comparison.md.
OFF_CREST_CAVITY_TOLERANCE = 1e-4

#: A cavity is off-crest if its phase is further than this from the zero
#: crossing, in degrees.
ON_CREST_DEGREES = 1.0

#: Targets used for the per-element audit.  B1D and B2D between them cover every
#: element type in the machine bar the SASE undulators, and they carry all the
#: cavity families; running it on all seven would multiply the cost without
#: adding a class of element.
AUDITED_TARGETS = ("B1D", "B2D")


def _seed(tape: pl.DataFrame) -> Twiss:
    """Ocelot initial conditions from the tape's `INITIAL` row.

    The energy is taken from the first real element rather than that row: MAD-8
    prints `E = 0` on `INITIAL`, which would divide by zero in the first cavity.
    """
    row = tape.row(0, named=True)
    twiss = Twiss()
    for column, attribute in SEED_COLUMNS:
        setattr(twiss, attribute, float(row[column]))
    twiss.E = float(tape.filter(pl.col("E") > 0)["E"][0])
    return twiss


def _tracked_against_tape(target: str) -> pl.DataFrame:
    """Our optics and MAD-8's, joined on arc length."""
    tape = pand8.read_twiss(twiss_tape(target))
    tracked = ocelot_twiss(MagneticLattice(build_sequence(target)), tws0=_seed(tape))
    ours = pl.DataFrame(
        {
            "s": [point.s for point in tracked],
            "beta_x": [point.beta_x for point in tracked],
            "beta_y": [point.beta_y for point in tracked],
            "Dx": [point.Dx for point in tracked],
            "Dy": [point.Dy for point in tracked],
        }
    ).sort("s")

    reference = tape.select(
        pl.col("SUML").alias("s"), "BETX", "BETY", "DX", "DY", "NAME"
    )
    # SUML and Ocelot's s are the same coordinate and the models agree on total
    # length, so element boundaries land on each other to well under a micron.
    return reference.join_asof(
        ours, on="s", strategy="nearest", tolerance=1e-6
    ).drop_nulls("beta_x")


@pytest.mark.parametrize("target", TAPE_TARGETS)
def test_whole_path_optics_track_mad8(target):
    """Cathode to dump in one pass, compared element by element."""
    joined = _tracked_against_tape(target)
    assert joined.height > 0, f"{target}: nothing matched on arc length"

    for ours, theirs in (("beta_x", "BETX"), ("beta_y", "BETY")):
        relative = (
            (joined[ours] - joined[theirs]).abs() / joined[theirs].abs().clip(1e-9)
        ).max()
        assert relative < WHOLE_PATH_BETA_TOLERANCE, (
            f"{target}: {ours} drifts {relative:.2e} from MAD-8 over the full path"
        )

    for ours, theirs in (("Dx", "DX"), ("Dy", "DY")):
        absolute = (joined[ours] - joined[theirs]).abs().max()
        assert absolute < WHOLE_PATH_DISPERSION_TOLERANCE_M, (
            f"{target}: {ours} differs from MAD-8 by {absolute:.2e} m"
        )


def _local_errors(target: str) -> list[tuple[float, object, dict]]:
    """Relative beta error of each element propagated on its own."""
    sequence = build_sequence(target)
    tape = pand8.read_twiss(twiss_tape(target)).to_dicts()
    assert len(tape) == len(sequence) + 1, (
        f"{target}: tape has {len(tape)} rows against {len(sequence)} elements; "
        "the two are only comparable row for row when neither has rotations"
    )

    errors = []
    for index, element in enumerate(sequence):
        before, after = tape[index], tape[index + 1]
        if before["E"] <= 0 or after["BETX"] <= 0:
            continue
        twiss = Twiss()
        for column, attribute in SEED_COLUMNS:
            setattr(twiss, attribute, float(before[column]))
        twiss.E = float(before["E"])

        arrived = ocelot_twiss(MagneticLattice([element]), tws0=twiss)[-1]
        error = max(
            abs(arrived.beta_x - after["BETX"]) / after["BETX"],
            abs(arrived.beta_y - after["BETY"]) / after["BETY"],
        )
        errors.append((error, element, before))
    return errors


@pytest.mark.parametrize("target", AUDITED_TARGETS)
def test_per_element_transfer_maps_match_mad8(target):
    """Each element alone, against MAD-8's own step across it.

    Splitting the assertion three ways is the point: it records that the cavities
    are the only disagreement, and how big it is, rather than hiding all three
    behind one loose tolerance.
    """
    for error, element, _ in _local_errors(target):
        if isinstance(element, Cavity):
            continue
        assert error < ELEMENT_TOLERANCE, (
            f"{target}: {element.id} ({type(element).__name__}) differs from "
            f"MAD-8 by {error:.2e}"
        )


@pytest.mark.parametrize("target", AUDITED_TARGETS)
def test_on_crest_cavities_match_mad8(target):
    """On-crest, the two cavity models are indistinguishable."""
    checked = 0
    for error, element, _ in _local_errors(target):
        if not isinstance(element, Cavity):
            continue
        if abs(element.phi) > ON_CREST_DEGREES:
            continue
        checked += 1
        assert error < ON_CREST_CAVITY_TOLERANCE, (
            f"{target}: on-crest cavity {element.id} differs by {error:.2e}"
        )
    assert checked, f"{target}: no on-crest cavities found to check"


@pytest.mark.parametrize("target", AUDITED_TARGETS)
def test_off_crest_cavity_disagreement_is_bounded(target):
    """Off-crest, they disagree -- by a known amount, in a known place.

    This asserts the disagreement is no *worse* than measured.  It is documenting
    a difference between two models, not asserting either is correct.
    """
    worst, culprit, energy = 0.0, None, 0.0
    for error, element, before in _local_errors(target):
        if not isinstance(element, Cavity) or abs(element.phi) <= ON_CREST_DEGREES:
            continue
        if error > worst:
            worst, culprit, energy = error, element, before["E"]

    assert culprit is not None, f"{target}: no off-crest cavities found"
    assert worst < OFF_CREST_CAVITY_TOLERANCE, (
        f"{target}: off-crest cavity {culprit.id} at {energy:.4f} GeV, "
        f"phi = {culprit.phi:.2f} deg, differs from MAD-8 by {worst:.2e} -- "
        f"worse than the {OFF_CREST_CAVITY_TOLERANCE:.0e} recorded when this was "
        "characterised"
    )


@pytest.mark.parametrize("target", AUDITED_TARGETS)
def test_off_crest_cavity_disagreement_falls_with_energy(target):
    """The disagreement is a low-energy effect, and shrinks as the beam gains it.

    Recorded because it is the strongest clue to the cause: an error that decays
    with energy at fixed phase points at the low-energy end of the cavity map,
    which is exactly what the DESY Rosenzweig-Serafini patch addresses.
    """
    points = [
        (before["E"], error)
        for error, element, before in _local_errors(target)
        if isinstance(element, Cavity) and abs(element.phi) > ON_CREST_DEGREES
    ]
    assert len(points) > 8, f"{target}: too few off-crest cavities to see a trend"

    energies = np.array([energy for energy, _ in points])
    errors = np.array([error for _, error in points])
    low, high = (
        errors[energies < np.median(energies)],
        errors[energies >= np.median(energies)],
    )
    assert low.max() > 5 * high.max(), (
        f"{target}: the off-crest cavity disagreement no longer falls with energy "
        f"(low-energy worst {low.max():.2e}, high-energy worst {high.max():.2e}); "
        "if a cavity model changed, re-characterise before adjusting this"
    )


@pytest.mark.parametrize("target", TAPE_TARGETS)
def test_optics_agree_everywhere_upstream_of_the_undulators(target):
    """Before any undulator, every path agrees with MAD-8 to the same level.

    This is what confines the T4D beta_y excursion to the SASE undulators rather
    than leaving it as an unexplained looser tolerance on one target.  If a
    disagreement ever appears upstream of SASE1 -- shared lattice, every path --
    this fails while the whole-path test might still pass.
    """
    joined = _tracked_against_tape(target).filter(pl.col("s") < SASE1_START_M)
    if joined.height == 0:
        pytest.skip(f"{target} ends before {SASE1_START_M} m")

    for ours, theirs in (("beta_x", "BETX"), ("beta_y", "BETY")):
        relative = (
            (joined[ours] - joined[theirs]).abs() / joined[theirs].abs().clip(1e-9)
        ).max()
        assert relative < PRE_UNDULATOR_BETA_TOLERANCE, (
            f"{target}: {ours} differs by {relative:.2e} upstream of the "
            f"undulators, where every path shares a lattice"
        )


def test_sase_undulators_have_no_focusing_yet():
    """Record that the SASE undulators are unfocused, as an executable fact.

    `Kx = 0` makes an Ocelot undulator a drift.  For matching MAD-8 that is
    *correct* rather than a gap: 61 of T4D's 63 undulators are plain `DRIF`
    records there, which is also a drift, and they agree to 9.5e-10.  `Kx` cannot
    come from the tape in any case -- MAD-8 has no undulator element and K is a
    gap setting, not lattice geometry.

    It is pinned here because adding the real gap settings would make the model
    deliberately *diverge* from MAD-8 in the undulators, which is a decision
    worth taking knowingly.  When that happens this test fails and
    `WHOLE_PATH_BETA_TOLERANCE` has to be re-measured against a model that no
    longer claims to reproduce MAD-8 there.
    """
    from ocelot.cpbd.elements import Undulator

    undulators = [e for e in build_sequence("T4D") if isinstance(e, Undulator)]
    assert undulators, "T4D should contain the SASE1 and SASE3 undulators"
    assert {u.Kx for u in undulators} == {0.0}, (
        "SASE undulators now carry a non-zero Kx -- re-measure the whole-path "
        "beta tolerance, which was set with them unfocused"
    )
