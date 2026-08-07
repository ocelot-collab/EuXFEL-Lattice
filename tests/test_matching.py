"""Tests for :mod:`euxfel.matching`.

Nothing here needs a beam file.  The distributions are generated from the
design optics, and the sections tracked over are short and carry no physics
processes, so the whole module runs in a few seconds.
"""

import numpy as np
import pytest
from ocelot.cpbd.beam import Twiss, generate_parray, get_envelope
from ocelot.cpbd.elements import Cavity, Quadrupole, TDCavity
from ocelot.cpbd.magnetic_lattice import MagneticLattice
from ocelot.cpbd.optics import twiss as linear_twiss

from euxfel.matching import (
    INJECTOR_MATCHING_QUAD_NAMES,
    MATCH_37,
    MATCH_52,
    BacktrackingLinearMatcher,
    backtrack_twiss,
    design_twiss_at,
    get_unary_twiss_function,
    match_with_backtracking,
    navigator_between,
    reverse_element,
    reversed_lattice,
    slice_twiss,
)
from euxfel.subsequences import i1

#: A stretch of the injector with three quadrupoles and nothing else that
#: matters -- no RF, no dipoles.  Reversing this line really is running it
#: backwards, so it is where the backtracking trick is exactly true.
DRIFT_QUAD_START = "OTRC.58.I1"
DRIFT_QUAD_STOP = "ENSUB.62.I1"
DRIFT_QUAD_QUADS = ["QI.59.I1", "QI.60.I1", "QI.61.I1"]


@pytest.fixture(scope="module")
def design_twiss():
    """Ocelot's own design optics at every element of i1, keyed by name."""
    at = {}
    for tws in linear_twiss(MagneticLattice(i1.cell), tws0=i1.twiss0):
        at.setdefault(tws.id, tws)
    return at


def _parray_at(design_twiss, marker, nparticles=2000):
    tws = design_twiss[marker]
    return generate_parray(tws=tws, energy=tws.E, nparticles=nparticles, charge=250e-12)


# --------------------------------------------------------------------------- #
# The pieces
# --------------------------------------------------------------------------- #


def test_design_twiss_at_reads_the_component_list():
    tws = design_twiss_at(MATCH_52)
    assert tws.id == MATCH_52
    assert tws.beta_x == pytest.approx(3.1317, abs=1e-3)
    assert tws.alpha_x == pytest.approx(-0.9249, abs=1e-3)
    assert tws.beta_y == pytest.approx(5.4175, abs=1e-3)
    assert tws.alpha_y == pytest.approx(1.7301, abs=1e-3)


def test_design_twiss_at_agrees_with_ocelot(design_twiss):
    """The spreadsheet's optics columns and Ocelot's tracking of the generated
    lattice are two independent routes to the same number."""
    for marker in (MATCH_37, MATCH_52):
        longlist, ocelot = design_twiss_at(marker), design_twiss[marker]
        assert longlist.beta_x == pytest.approx(ocelot.beta_x, rel=1e-3)
        assert longlist.beta_y == pytest.approx(ocelot.beta_y, rel=1e-3)
        assert longlist.alpha_x == pytest.approx(ocelot.alpha_x, abs=1e-3)
        assert longlist.alpha_y == pytest.approx(ocelot.alpha_y, abs=1e-3)


def test_design_twiss_at_unknown_marker():
    with pytest.raises(KeyError, match="no optics in the component list"):
        design_twiss_at("NOT.A.MARKER")


@pytest.mark.parametrize("name", ["projected", "PROJECTED", "imax", "emax"])
def test_get_unary_twiss_function_by_name(name, design_twiss):
    parray = _parray_at(design_twiss, MATCH_37, nparticles=20000)
    tws = get_unary_twiss_function(name)(parray)
    assert isinstance(tws, Twiss)
    assert tws.beta_x > 0
    assert tws.beta_y > 0


def test_get_unary_twiss_function_accepts_a_callable(design_twiss):
    parray = _parray_at(design_twiss, MATCH_37)
    function = get_unary_twiss_function(get_envelope)
    assert function(parray).beta_x == pytest.approx(
        get_envelope(parray).beta_x, rel=1e-12
    )


def test_get_unary_twiss_function_rejects_nonsense():
    with pytest.raises(ValueError, match="Unknown twiss type"):
        get_unary_twiss_function("sideways")


def test_navigator_between_includes_both_endpoints():
    navi = navigator_between(i1.cell, MATCH_37, MATCH_52)
    assert navi.lat.sequence[0].id == MATCH_37
    assert navi.lat.sequence[-1].id == MATCH_52
    assert navi.lat.totalLen == pytest.approx(14.6798, abs=1e-3)
    # No physics processes: this is linear optics done the slow way.
    assert not navi.get_phys_procs()


def test_navigator_between_rejects_an_unknown_marker():
    with pytest.raises(KeyError, match="No element called"):
        navigator_between(i1.cell, "NOT.A.MARKER", MATCH_52)


# --------------------------------------------------------------------------- #
# Backtracking, on its own
# --------------------------------------------------------------------------- #


def test_backtracking_inverts_a_drift_quad_line(design_twiss):
    """Where the reversal trick is valid, it is exact.

    A line of drifts and quadrupoles read backwards *is* the same line, so the
    round trip has to return the launch Twiss to numerical precision.
    """
    navi = navigator_between(i1.cell, DRIFT_QUAD_START, DRIFT_QUAD_STOP)
    launch = design_twiss[DRIFT_QUAD_START]

    end = linear_twiss(navi.lat, tws0=launch)[-1]
    recovered = backtrack_twiss(navi.lat, end)

    for key in ("beta_x", "alpha_x", "beta_y", "alpha_y"):
        assert getattr(recovered, key) == pytest.approx(
            getattr(launch, key), rel=1e-9, abs=1e-9
        )


def test_backtracking_inverts_the_injector_match_section(design_twiss):
    """The hard case: eight AH1 cavities and the four chicane dipoles.

    The energy is the sharpest check.  0.15 GeV goes in and 0.13 comes out, so
    backtracking has to climb back to 0.15.  Reversing the element list alone
    reaches 0.11 -- decelerating a second time instead of undoing it.
    """
    navi = navigator_between(i1.cell, MATCH_37, MATCH_52)
    launch = design_twiss[MATCH_37]

    end = linear_twiss(navi.lat, tws0=launch)[-1]
    assert end.E < launch.E, "AH1 decelerates, or this test proves nothing"

    recovered = backtrack_twiss(navi.lat, end)
    assert recovered.E == pytest.approx(launch.E, rel=1e-9)
    for key in ("beta_x", "alpha_x", "beta_y", "alpha_y"):
        assert getattr(recovered, key) == pytest.approx(
            getattr(launch, key), rel=1e-9, abs=1e-9
        )


def test_the_injector_match_section_is_the_hard_case():
    """Pin down what makes a naive reversal wrong, so the test above is not
    mysteriously specific."""
    navi = navigator_between(i1.cell, MATCH_37, MATCH_52)
    cavities = [e for e in navi.lat.sequence if isinstance(e, Cavity)]
    asymmetric = [
        e.id
        for e in navi.lat.sequence
        if abs(getattr(e, "e1", 0.0) - getattr(e, "e2", 0.0)) > 1e-12
    ]
    assert len(cavities) == 8, "the eight AH1 cavities"
    assert asymmetric == [
        "BL.48I.I1",
        "BL.48II.I1",
        "BL.50I.I1",
        "BL.50II.I1",
    ], "the laser-heater chicane dipoles"


def test_reverse_element_swaps_dipole_edges():
    bend = [e for e in i1.cell if e.id == "BL.48I.I1"][0]
    assert bend.e1 != bend.e2, "this bend has to be asymmetric to test anything"

    backwards = reverse_element(bend)
    assert backwards.e1 == bend.e2
    assert backwards.e2 == bend.e1
    assert backwards.angle == bend.angle
    assert backwards.l == bend.l
    # A copy: the forward lattice must not have had its edges swapped.
    assert bend.e1 == 0.0


def test_reverse_element_decelerates_a_cavity():
    cavity = [e for e in i1.cell if e.id == "C3.AH1.1.1.I1"][0]
    assert cavity.v != 0

    backwards = reverse_element(cavity)
    assert backwards.v == -cavity.v
    assert backwards.phi == cavity.phi
    assert cavity.v > 0 or cavity.v < 0, "unchanged in place"


def test_reverse_element_leaves_symmetric_elements_alone():
    quad = [e for e in i1.cell if e.id == "Q.37.I1"][0]
    backwards = reverse_element(quad)
    assert backwards.k1 == quad.k1
    assert backwards.l == quad.l


def test_reversed_lattice_does_not_touch_the_forward_one():
    navi = navigator_between(i1.cell, MATCH_37, MATCH_52)
    before = [
        (e.id, getattr(e, "e1", None), getattr(e, "v", None)) for e in navi.lat.sequence
    ]
    backwards = reversed_lattice(navi.lat)

    assert backwards.sequence[0].id == MATCH_52
    assert backwards.sequence[-1].id == MATCH_37
    assert backwards.totalLen == pytest.approx(navi.lat.totalLen)
    after = [
        (e.id, getattr(e, "e1", None), getattr(e, "v", None)) for e in navi.lat.sequence
    ]
    assert after == before


def test_reversing_a_tds_is_refused():
    """A TDS is not reversed by negating its voltage, so it raises."""
    tds = next((e for e in i1.cell if isinstance(e, TDCavity)), None)
    assert tds is not None, "i1 should contain the injector TDS"
    with pytest.raises(NotImplementedError, match="TDCavity"):
        reverse_element(tds)


# --------------------------------------------------------------------------- #
# Slice Twiss
# --------------------------------------------------------------------------- #


def test_slice_twiss_works_where_ocelots_does_not(design_twiss):
    """OCELOT's own ``twiss_parray_slice`` raises for every input at the pinned
    revision; ours is the same calculation without the offending line."""
    from ocelot.cpbd.beam import twiss_parray_slice

    parray = _parray_at(design_twiss, MATCH_37, nparticles=20000)
    with pytest.raises(AttributeError, match="gamma_x"):
        twiss_parray_slice(parray, slice="Imax")

    tws = slice_twiss(parray, slice="Imax")
    assert tws.beta_x > 0
    assert tws.beta_y > 0
    assert tws.emit_x > 0


def test_get_envelope_slice_is_not_a_substitute(design_twiss):
    """Guards the reason :func:`slice_twiss` exists at all.

    ``get_envelope`` accepts a ``slice`` argument and ignores it unless
    ``bounds`` is given too, so it returns the projected Twiss while looking
    like it returned a slice.  If OCELOT ever fixes that, this test fails and
    the workaround can be reconsidered.
    """
    parray = _parray_at(design_twiss, MATCH_37, nparticles=20000)
    assert get_envelope(parray, slice="Imax").beta_x == get_envelope(parray).beta_x


# --------------------------------------------------------------------------- #
# The matcher, end to end
# --------------------------------------------------------------------------- #


def test_the_design_lattice_is_already_matched(design_twiss):
    """A tracked beam launched on design optics arrives on design optics.

    This is the wiring check: goal, navigator, tracking and Bmag all have to
    agree before any statement about matching means anything.
    """
    navi = navigator_between(i1.cell, MATCH_37, MATCH_52)
    matcher = BacktrackingLinearMatcher(
        navi,
        _parray_at(design_twiss, MATCH_37),
        design_twiss[MATCH_52],
        INJECTOR_MATCHING_QUAD_NAMES,
    )
    matcher.track_forwards()

    bmag_x, bmag_y = matcher.bmags()
    assert bmag_x == pytest.approx(1.0, abs=1e-3)
    assert bmag_y == pytest.approx(1.0, abs=1e-3)
    # Loose, because l2loss is dominated by the beta terms and 2000 particles
    # only pin beta down to a percent or so.
    assert matcher.l2loss() < 0.1


def test_quad_strengths_come_back_in_lattice_order(design_twiss):
    navi = navigator_between(i1.cell, MATCH_37, MATCH_52)
    matcher = BacktrackingLinearMatcher(
        navi,
        _parray_at(design_twiss, MATCH_37),
        design_twiss[MATCH_52],
        INJECTOR_MATCHING_QUAD_NAMES,
    )
    found = [quad.id for quad in matcher._quad_instances_from_navi()]
    assert found == INJECTOR_MATCHING_QUAD_NAMES
    assert matcher.quad_strengths() == [
        quad.k1
        for quad in navi.lat.sequence
        if isinstance(quad, Quadrupole) and quad.id in INJECTOR_MATCHING_QUAD_NAMES
    ]


def test_initial_match_recovers_the_design_optics(design_twiss):
    """Linear matching alone, with the quads knocked 10% off design.

    The assertion is on the *optics*, not the strengths.  Five quadrupoles
    against four constraints is an underdetermined problem, so the design
    strengths are one member of a one-parameter family of solutions and the
    simplex has no reason to return that particular one -- see
    :func:`test_the_injector_match_is_underdetermined`.
    """
    navi = navigator_between(i1.cell, MATCH_37, MATCH_52)
    goal = design_twiss[MATCH_52]
    matcher = BacktrackingLinearMatcher(
        navi,
        _parray_at(design_twiss, MATCH_37, nparticles=20000),
        goal,
        INJECTOR_MATCHING_QUAD_NAMES,
    )
    for quad in matcher._quad_instances_from_navi():
        quad.k1 *= 1.10

    matcher._set_quads(matcher.initial_match())
    matcher.track_forwards()

    assert matcher.bmags()[0] == pytest.approx(1.0, abs=1e-2)
    assert matcher.bmags()[1] == pytest.approx(1.0, abs=1e-2)


def test_the_injector_match_is_underdetermined(design_twiss):
    """Two different starting points, two different answers, same optics.

    Worth pinning down: it means "did the strengths come back to design?" is
    not a valid check on this matcher, and that the iteration can wander a long
    way along the degenerate direction while looking perfectly converged.
    """
    goal = design_twiss[MATCH_52]
    parray = _parray_at(design_twiss, MATCH_37, nparticles=20000)

    solutions = []
    for perturbation in (1.02, 1.10):
        navi = navigator_between(i1.cell, MATCH_37, MATCH_52)
        matcher = BacktrackingLinearMatcher(
            navi, parray, goal, INJECTOR_MATCHING_QUAD_NAMES
        )
        for quad in matcher._quad_instances_from_navi():
            quad.k1 *= perturbation
        solutions.append(matcher.initial_match())

    assert len(INJECTOR_MATCHING_QUAD_NAMES) == 5, "five free quadrupoles"
    assert not np.allclose(solutions[0], solutions[1], atol=1e-3), (
        "the two matches found the same strengths; if OCELOT's matcher has "
        "become deterministic in this sense, the caveat above can be dropped"
    )


def test_matcher_does_not_touch_the_callers_lattice(design_twiss):
    """The navigator is deep-copied, so the caller applies the result itself."""
    navi = navigator_between(i1.cell, MATCH_37, MATCH_52)
    before = [e.k1 for e in navi.lat.sequence if e.id in INJECTOR_MATCHING_QUAD_NAMES]

    matcher = BacktrackingLinearMatcher(
        navi,
        _parray_at(design_twiss, MATCH_37),
        design_twiss[MATCH_52],
        INJECTOR_MATCHING_QUAD_NAMES,
    )
    matcher._set_quads([k * 2 for k in before])

    after = [e.k1 for e in navi.lat.sequence if e.id in INJECTOR_MATCHING_QUAD_NAMES]
    assert after == before
    assert matcher.quad_strengths() == [k * 2 for k in before]


def test_match_with_backtracking_runs_end_to_end(design_twiss):
    navi = navigator_between(i1.cell, DRIFT_QUAD_START, DRIFT_QUAD_STOP)
    strengths, summary = match_with_backtracking(
        navi,
        _parray_at(design_twiss, DRIFT_QUAD_START),
        design_twiss[DRIFT_QUAD_STOP],
        DRIFT_QUAD_QUADS,
        maxiter=1,
    )
    assert len(strengths) == len(DRIFT_QUAD_QUADS)
    assert all(np.isfinite(k) for k in strengths)
    assert np.isfinite(summary.bmag_x)
    assert np.isfinite(summary.bmag_y)
    assert np.isfinite(summary.l2loss)


def test_backtracking_is_a_no_op_with_nothing_acting_on_the_beam(design_twiss):
    """The load-bearing end-to-end check.

    With no physics processes attached, the tracked beam follows linear optics,
    so the Twiss measured at the match point is the Twiss linear optics
    predicted, and backtracking it must hand back the launch condition the beam
    really had.  The iteration therefore has nothing to correct and has to leave
    the optics on the goal.

    It is stated in Bmag rather than in strengths deliberately: the strengths
    are free to slide along the degenerate direction (see
    :func:`test_the_injector_match_is_underdetermined`), and before the reversal
    was made exact they slid far enough to leave Bmag_y at 2.08.
    """
    navi = navigator_between(i1.cell, MATCH_37, MATCH_52)
    _, summary = match_with_backtracking(
        navi,
        _parray_at(design_twiss, MATCH_37, nparticles=20000),
        design_twiss[MATCH_52],
        INJECTOR_MATCHING_QUAD_NAMES,
        maxiter=1,
    )
    assert summary.bmag_x == pytest.approx(1.0, abs=1e-4)
    assert summary.bmag_y == pytest.approx(1.0, abs=1e-4)
    assert summary.l2loss < 1e-2
