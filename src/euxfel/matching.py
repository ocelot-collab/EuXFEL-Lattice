"""Matching that accounts for what tracking does to the beam.

Linear matching answers "what quadrupole strengths take *this* Twiss to *that*
Twiss?", and it answers it exactly -- for a beam that is a linear-optics
abstraction.  A tracked particle distribution is not.  Space charge, CSR and
wakefields all act on it between the two markers, so the Twiss you measure at
the match point after tracking is not the Twiss linear optics promised, and the
strengths that linear matching handed you are the answer to a question nobody
asked.

The way out here is a fixed-point iteration.  Track the real distribution
through the section and measure its Twiss at the end.  Then run linear optics
*backwards* over the same section from that measured Twiss, which gives the
launch condition a purely linear line would have needed in order to arrive
where the tracked beam actually did.  Match forwards from that effective launch
condition instead of the real one, and the linear matcher is now solving a
problem whose answer is right for the tracked beam.  Iterate until it settles.

Backwards is negating ``alpha`` and propagating through the line reversed, which
is the standard trick: a Twiss ellipse run through a line backwards is the same
ellipse with its correlation flipped.  Reversing the *line*, though, is not
reversing the *list* -- a dipole must be entered through its other face and a
cavity must decelerate -- and getting that wrong quietly poisons the fixed
point, because the iteration is then converging on the solution to a line that
does not exist.  See :func:`reverse_element`.

The Twiss you measure is a choice, and it is the point of
``twiss_function``/``twiss_type``.  ``"projected"`` uses the whole distribution;
``"imax"`` and ``"emax"`` use a single slice, at peak current or peak energy.
Matching the slice at peak current is usually what an FEL wants, since that is
the part of the bunch that lases -- and it is not at all the same answer as
matching the projection.

Ported from ``oxfel.matching`` (the ocelot-euxfel package).
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from copy import deepcopy
from dataclasses import dataclass
from functools import partial
from typing import TYPE_CHECKING

import numpy as np
import polars as pl
from ocelot.cpbd.beam import Twiss, get_envelope
from ocelot.cpbd.beam.analysis import global_slice_analysis
from ocelot.cpbd.elements import Bend, Cavity, RBend, SBend, TDCavity
from ocelot.cpbd.magnetic_lattice import MagneticLattice
from ocelot.cpbd.match import match as ocelot_match
from ocelot.cpbd.navi import Navigator
from ocelot.cpbd.optics import twiss as linear_twiss
from ocelot.cpbd.track import track
from ocelot.cpbd.transformations.second_order import SecondTM

from .optics import bmag, optics_at_points_from_longlist

if TYPE_CHECKING:
    from ocelot.cpbd.beam import ParticleArray

__all__ = [
    "B2_MATCHING_QUAD_NAMES",
    "INJECTOR_MATCHING_QUAD_NAMES",
    "MATCH_37",
    "MATCH_52",
    "BacktrackingLinearMatcher",
    "MismatchSummary",
    "backtrack_twiss",
    "design_twiss_at",
    "get_unary_twiss_function",
    "match_with_backtracking",
    "navigator_between",
    "navigator_for_section",
    "reverse_element",
    "reversed_lattice",
    "slice_twiss",
]

LOG = logging.getLogger(__name__)

#: The injector match point the s2e simulation is launched from.
MATCH_37: str = "MATCH.37.I1"
#: The injector match point in front of the TDS, which must be hit.
MATCH_52: str = "MATCH.52.I1"

#: The five quadrupoles between :data:`MATCH_37` and :data:`MATCH_52`, in
#: beamline order.  Order matters: strengths come back from the matcher in the
#: order the elements appear in the lattice, not the order they are named here.
INJECTOR_MATCHING_QUAD_NAMES: list[str] = [
    "Q.37.I1",
    "Q.38.I1",
    "QI.46.I1",
    "QI.47.I1",
    "QI.50.I1",
]

#: The equivalent set in L2, ahead of the BC2 match point.
B2_MATCHING_QUAD_NAMES: list[str] = [
    "Q.333.L2",
    "Q.345.L2",
    "Q.357.L2",
    "Q.369.L2",
    "Q.381.L2",
]


@dataclass
class MismatchSummary:
    """How far the tracked beam ended up from the goal."""

    bmag_x: float
    bmag_y: float
    l2loss: float


def design_twiss_at(marker: str) -> Twiss:
    """The component list's own optics at ``marker``, as a :class:`Twiss`.

    This is the design answer -- what the spreadsheet's optics columns say
    should be there -- and so it is the natural goal for a match.  Only the
    transverse Twiss is filled in; nothing here knows the beam's energy or
    emittance.
    """
    frame = optics_at_points_from_longlist([marker]).filter(pl.col("id") == marker)
    if frame.is_empty():
        raise KeyError(
            f"{marker!r} has no optics in the component list. "
            f"Only markers the longlist carries optics columns for can be used."
        )
    row = frame.row(0, named=True)
    return Twiss(
        id=marker,
        s=row["s"],
        beta_x=row["beta_x"],
        alpha_x=row["alpha_x"],
        beta_y=row["beta_y"],
        alpha_y=row["alpha_y"],
    )


def _element_named(cell, name: str):
    """The one element in ``cell`` called ``name``."""
    found = [element for element in cell if element.id == name]
    if not found:
        raise KeyError(f"No element called {name!r} in this cell.")
    if len(found) > 1:
        raise KeyError(f"{name!r} names {len(found)} elements in this cell.")
    return found[0]


def _elements_named(mlat: MagneticLattice, names: list[str]) -> list:
    """Every element of ``mlat`` whose id is in ``names``, in *lattice* order.

    Deliberately the lattice's order and not ``names``' order: these are the
    objects handed to OCELOT's matcher as its free variables, and the strengths
    it returns come back in the order it was given them.
    """
    indices = mlat.find_indices_by_predicate(lambda element: element.id in names)
    return [mlat.sequence[i] for i in indices]


def navigator_between(
    cell,
    start: str,
    stop: str,
    *,
    unit_step: float = 0.02,
    method: dict | None = None,
) -> Navigator:
    """A navigator over ``cell`` from marker ``start`` to marker ``stop``.

    Both endpoints are included.  No physics processes are attached, so
    tracking through this navigator is linear optics done the slow way -- which
    makes it the right thing for checking that the backtracking itself is
    sound, since with nothing acting on the beam the iteration must not move.

    For a real match, use :func:`navigator_for_section` instead, or attach
    processes to the returned navigator yourself.
    """
    lattice = MagneticLattice(
        cell,
        start=_element_named(cell, start),
        stop=_element_named(cell, stop),
        method=method or {"global": SecondTM},
    )
    navi = Navigator(lattice)
    navi.unit_step = unit_step
    return navi


def reverse_element(element):
    """A copy of ``element`` as a beam travelling the other way would meet it.

    Reversing a *list* of elements is not reversing a *line*.  Two kinds of
    element are not symmetric end to end, and both are in the injector match
    section:

    Dipoles
        A chicane dipole has one flat face and one angled one.  Traversed
        backwards it is entered through what was the exit face, so ``e1`` and
        ``e2`` swap -- along with the fringe-field integrals and pole-face
        curvatures that go with them.  Leave them and the edge focusing lands on
        the wrong end of the magnet.

    Cavities
        A cavity that accelerates forwards must decelerate backwards, which is
        ``v -> -v``.  Leave it and the energy runs the same way whichever
        direction you go, so backtracking through AH1 arrives at 0.11 GeV
        instead of the 0.15 GeV it started from, and every beta comes out
        adiabatically damped in the wrong direction.  The coupler kicks swap
        ends with the cavity.

    Everything else in this machine -- drifts, quadrupoles, sextupoles,
    solenoids, undulators, markers -- is its own mirror image as far as linear
    optics is concerned, and is returned unchanged.

    A transverse deflecting structure is *not* handled: reversing one is not
    ``v -> -v``, and there is no TDS in any section this is used on (the
    injector TDS sits downstream of ``MATCH.52.I1``, which is the whole reason
    that match point has to be hit).  One in the line raises rather than
    quietly giving a slightly wrong answer.
    """
    if isinstance(element, TDCavity):
        raise NotImplementedError(
            f"{element.id!r} is a TDCavity, and reversing one is not implemented. "
            f"Backtracking through a transverse deflecting structure needs its "
            f"map inverted properly, not its voltage negated."
        )

    reversed_element = deepcopy(element)

    if isinstance(element, (Bend, RBend, SBend)):
        reversed_element.e1, reversed_element.e2 = element.e2, element.e1
        # `fintx=None` means "the same as fint", so resolve it before swapping
        # or the reversed magnet ends up with fint=None.
        fintx = element.fint if element.fintx is None else element.fintx
        reversed_element.fint, reversed_element.fintx = fintx, element.fint
        reversed_element.h_pole1, reversed_element.h_pole2 = (
            element.h_pole2,
            element.h_pole1,
        )
    elif isinstance(element, Cavity):
        reversed_element.v = -element.v
        for plane in ("vx", "vy", "vxx", "vxy"):
            setattr(reversed_element, f"{plane}_up", getattr(element, f"{plane}_down"))
            setattr(reversed_element, f"{plane}_down", getattr(element, f"{plane}_up"))

    return reversed_element


def reversed_lattice(lattice: MagneticLattice) -> MagneticLattice:
    """``lattice`` as a beam travelling through it backwards would see it.

    Every element is copied, so the forward lattice is untouched -- which
    matters, because the two would otherwise share the dipoles whose edge
    angles this swaps.
    """
    return MagneticLattice(
        [reverse_element(element) for element in reversed(lattice.sequence)]
    )


def backtrack_twiss(lattice: MagneticLattice, twiss1: Twiss) -> Twiss:
    """Run ``twiss1`` backwards through ``lattice`` and return the launch Twiss.

    Negate ``alpha`` on the way in and again on the way out: an ellipse
    traversed backwards is the same ellipse with the sign of its
    position-momentum correlation flipped.  Between the two, propagate through
    :func:`reversed_lattice`, which is a genuine reversal rather than a
    reversed list -- see there for why the difference is not cosmetic.

    Exact to rounding, so ``backtrack_twiss(lat, twiss(lat, tws0)[-1])`` returns
    ``tws0``.
    """
    # A copy, because the caller's Twiss is not ours to flip the sign of.
    reversed_in = deepcopy(twiss1)
    reversed_in.alpha_x *= -1
    reversed_in.alpha_y *= -1

    twiss0 = linear_twiss(reversed_lattice(lattice), tws0=reversed_in)[-1]

    # ...and point it forwards again.
    twiss0.alpha_x *= -1
    twiss0.alpha_y *= -1
    return twiss0


def navigator_for_section(section) -> Navigator:
    """The navigator of a :class:`~euxfel.section_track.SectionTrack`.

    A section already knows its lattice, its step size and which physics
    processes act where, so this is the route to a match that sees space
    charge, CSR and wakes.  It matches over the whole section, however -- a
    section boundary can only exist where a marker exists, so if the stretch you
    want to match over is not a section, it needs a marker and a section split.
    """
    section.init_navigator()
    return section.navigator


class BacktrackingLinearMatcher:
    """Match a tracked beam by feeding linear optics an effective launch Twiss.

    One iteration is: track, measure the Twiss at the end, run that Twiss
    backwards through the reversed line, and linear-match forwards from the
    result.  See the module docstring for why.

    The navigator is deep-copied, so the caller's lattice is untouched and the
    strengths this returns have to be applied by the caller.
    """

    MAX_ITER = 10_000

    def __init__(
        self,
        navi: Navigator,
        parray0: ParticleArray,
        goal_twiss: Twiss,
        quad_names: list[str],
        twiss_function: Callable[[ParticleArray], Twiss] = get_envelope,
        verbose: bool = False,
    ):
        self.navi = deepcopy(navi)
        self.parray0 = parray0
        self.quad_names = quad_names
        self.goal_twiss = goal_twiss
        self.twiss_function = twiss_function
        self.verbose = verbose
        self.parray1: ParticleArray | None = None

    def _get_constraint(self) -> dict:
        return {
            self.navi.lat.sequence[-1]: {
                "beta_x": self.goal_twiss.beta_x,
                "beta_y": self.goal_twiss.beta_y,
                "alpha_x": self.goal_twiss.alpha_x,
                "alpha_y": self.goal_twiss.alpha_y,
            }
        }

    def l2loss(self) -> float:
        """Root sum of squares of the four Twiss errors at the match point.

        Not a physical quantity -- it adds a beta in metres to a dimensionless
        alpha -- but it is monotone in the right direction and cheap, so it is
        useful for watching an iteration converge.  :meth:`bmags` is the number
        to quote.
        """
        assert self.parray1 is not None
        tws = self.twiss_function(self.parray1)
        goal = self.goal_twiss
        return np.sqrt(
            (tws.beta_x - goal.beta_x) ** 2
            + (tws.alpha_x - goal.alpha_x) ** 2
            + (tws.beta_y - goal.beta_y) ** 2
            + (tws.alpha_y - goal.alpha_y) ** 2
        )

    def bmags(self) -> tuple[float, float]:
        """The mismatch parameter in each plane.  1.0 is a perfect match."""
        assert self.parray1 is not None
        tws = self.twiss_function(self.parray1)
        return (
            bmag(
                tws.beta_x, tws.alpha_x, self.goal_twiss.beta_x, self.goal_twiss.alpha_x
            ),
            bmag(
                tws.beta_y, tws.alpha_y, self.goal_twiss.beta_y, self.goal_twiss.alpha_y
            ),
        )

    def mismatch_summary(self) -> MismatchSummary:
        bmag_x, bmag_y = self.bmags()
        return MismatchSummary(bmag_x, bmag_y, self.l2loss())

    def track_forwards(self, quad_strengths: list[float] | None = None) -> None:
        if quad_strengths is None:
            quad_strengths = self.quad_strengths()
        self.navi.go_to_start()
        _, parray1 = track(
            self.navi.lat,
            self.parray0.copy(),
            navi=self.navi,
            overwrite_progress=True,
            print_progress=False,
        )
        self.parray1 = parray1

    def _quad_instances_from_navi(self) -> list:
        return _elements_named(self.navi.lat, self.quad_names)

    def quad_strengths(self) -> list[float]:
        return [quad.k1 for quad in self._quad_instances_from_navi()]

    def _set_quads(self, strengths: list[float]) -> None:
        """Set the quadrupole strengths in this matcher's copy of the lattice."""
        for quad, strength in zip(self._quad_instances_from_navi(), strengths):
            quad.k1 = strength
        self.navi.lat.update_transfer_maps()

    def initial_match(self) -> list[float]:
        """The linear match, done before any particle has been tracked."""
        LOG.debug("Running initial matching")
        return ocelot_match(
            self.navi.lat,
            self._get_constraint(),
            self._quad_instances_from_navi(),
            self.twiss_function(self.parray0),
            verbose=self.verbose,
            max_iter=self.MAX_ITER,
        )

    def match(
        self, n: int = 1, quad_strengths: list[float] | None = None
    ) -> list[float]:
        if quad_strengths is None:
            quad_strengths = self.initial_match()
        self._set_quads(quad_strengths)
        self.track_forwards(quad_strengths)
        for _ in range(n):
            quad_strengths = self._backtrack_twiss_and_retrack()
            self._set_quads(quad_strengths)
        return quad_strengths

    def rematch(self) -> list[float]:
        """One more iteration on top of whatever state the matcher is in."""
        if self.parray1 is None:
            self.track_forwards()
        quad_strengths = self._backtrack_twiss_and_retrack()
        self._set_quads(quad_strengths)
        return quad_strengths

    def _backtrack_twiss_and_retrack(self) -> list[float]:
        assert self.parray1 is not None
        twiss1 = self.twiss_function(self.parray1)
        LOG.debug("Using twiss function: %s", self.twiss_function)
        LOG.debug(
            "Twiss at end of line before backtracking: beta_x=%s beta_y=%s "
            "alpha_x=%s alpha_y=%s",
            twiss1.beta_x,
            twiss1.beta_y,
            twiss1.alpha_x,
            twiss1.alpha_y,
        )

        backtracked_twiss0 = backtrack_twiss(self.navi.lat, twiss1)
        LOG.debug(
            "Twiss at start of line after backtracking: beta_x=%s beta_y=%s "
            "alpha_x=%s alpha_y=%s",
            backtracked_twiss0.beta_x,
            backtracked_twiss0.beta_y,
            backtracked_twiss0.alpha_x,
            backtracked_twiss0.alpha_y,
        )

        LOG.debug("Matching using backtracked Twiss parameters")
        matched_strengths = ocelot_match(
            self.navi.lat,
            self._get_constraint(),
            self._quad_instances_from_navi(),
            backtracked_twiss0,
            verbose=self.verbose,
            max_iter=self.MAX_ITER,
        )
        self.track_forwards(matched_strengths)
        return matched_strengths


#: Twiss attributes OCELOT's slice analysis tries to write but cannot.
#:
#: ``Twiss.gamma_x`` and ``gamma_y`` are read-only properties derived from beta
#: and alpha, but ``SliceParameters.extract_slice`` sets them along with
#: everything else, so ``ocelot.cpbd.beam.twiss_parray_slice`` raises
#: ``AttributeError`` for *every* input at the pinned revision.  Skipping them
#: loses nothing -- they are computed from what is set anyway.
_DERIVED_TWISS_NAMES = frozenset({"gamma_x", "gamma_y"})


def slice_twiss(parray: ParticleArray, slice: str = "Imax", **kwargs) -> Twiss:
    """The Twiss of one longitudinal slice of ``parray``.

    ``"Imax"`` picks the slice at peak current, ``"Emax"`` the one at peak
    energy, anything else the slice at the centre of the bunch.

    This does what ``ocelot.cpbd.beam.twiss_parray_slice`` is meant to do.  That
    function is unusable at the pinned OCELOT revision -- see
    :data:`_DERIVED_TWISS_NAMES` -- and ``get_envelope(parray, slice=...)`` is
    not a substitute: it ignores ``slice`` entirely unless ``bounds`` is also
    given, so it fails silently rather than loudly.
    """
    params = global_slice_analysis(parray, **kwargs)
    if slice == "Imax":
        index = int(np.argmax(params.I))
    elif slice == "Emax":
        index = int(np.argmax(params.me))
    else:
        index = int(np.argsort(np.abs(params.s))[0])

    tws = Twiss()
    for source, name in params.SP_TO_TWISS_NAMES.items():
        if name in _DERIVED_TWISS_NAMES:
            continue
        setattr(tws, name, getattr(params, source)[index])
    for source, name in params.VARIANCE_SP_NAMES.items():
        setattr(tws, name, getattr(params, source)[index] ** 2)
    for name, factor in params.TWISS_UNITS_CONVERSION.items():
        setattr(tws, name, getattr(tws, name) * factor)
    return tws


def get_unary_twiss_function(twiss_type, **twissfnkwargs) -> Callable:
    """A one-argument ``parray -> Twiss``, chosen by name.

    ``"projected"`` is the whole distribution; ``"imax"`` and ``"emax"`` are the
    slice at peak current and at peak energy respectively.  A callable is
    returned with any keyword arguments bound.

    Which one you pick is a physics choice, not a detail.  The slice at peak
    current is the part of the bunch that lases, and matching it is not the same
    as matching the projection -- for a bunch with any correlation along it, the
    two ask for different quadrupole strengths.
    """
    if callable(twiss_type):
        return partial(twiss_type, **twissfnkwargs)
    if twiss_type.lower() == "projected":
        return partial(get_envelope, **twissfnkwargs)
    if twiss_type.lower() == "imax":
        return partial(slice_twiss, slice="Imax", **twissfnkwargs)
    if twiss_type.lower() == "emax":
        return partial(slice_twiss, slice="Emax", **twissfnkwargs)
    raise ValueError(f"Unknown twiss type selected: {twiss_type}")


def match_with_backtracking(
    navi: Navigator,
    parray0: ParticleArray,
    twiss_goal: Twiss,
    quad_names: list[str],
    maxiter: int = 1,
    twiss_type: str = "projected",
    verbose: bool = False,
    **twissfnkwargs,
) -> tuple[list[float], MismatchSummary]:
    """Match ``parray0`` onto ``twiss_goal`` at the end of ``navi``'s lattice.

    Only the transverse Twiss of ``twiss_goal`` is used: ``alpha_x``,
    ``beta_x``, ``alpha_y``, ``beta_y``.

    :param navi: the section to match over, endpoints included.
    :param parray0: the distribution at the start of it.
    :param twiss_goal: what to hit at the end of it.
    :param quad_names: the quadrupoles to vary.
    :param maxiter: backtracking iterations after the initial linear match.
    :param twiss_type: ``"projected"``, ``"imax"``, ``"emax"``, or a callable.
    :param twissfnkwargs: passed on to the Twiss function.
    :return: the matched strengths, in lattice order, and how well they did.
    """
    matcher = BacktrackingLinearMatcher(
        navi,
        parray0,
        twiss_goal,
        quad_names,
        get_unary_twiss_function(twiss_type, **twissfnkwargs),
        verbose=verbose,
    )
    quad_strengths = matcher.match(maxiter)
    return quad_strengths, matcher.mismatch_summary()
