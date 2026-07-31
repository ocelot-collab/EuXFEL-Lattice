"""High-level controls: the quantities physicists actually think in.

A knob owns a group of elements and maps a small number of physically
meaningful parameters onto them -- an R56 rather than four dipole angles, a
chirp rather than a voltage and a phase -- updating whatever else has to follow,
such as the drift lengths inside a chicane.

Each knob provides three operations:

``apply``
    Write the high-level parameters onto the elements.
``read``
    Recover the high-level parameters from the elements.  This is what makes
    snapshotting and diffing possible, and it is the half the earlier attempt at
    this never had.
``owns``
    Report the ``(element id, attribute)`` pairs it controls, so that a config
    setting the same thing twice can be rejected rather than silently resolved
    by ordering.

Most of the physics already exists in OCELOT and is reused rather than
reimplemented: ``beam2rf``/``rf2beam`` and their linac wrappers are exact
inverses of one another, and ``chicane_RTU`` gives an exact chicane R56.  What
is added here is solving for a *requested* R56 against the real transfer matrix,
and rescaling only the drifts.
"""

from __future__ import annotations

import math
import warnings
from typing import ClassVar

import numpy as np
from ocelot.cpbd.elements import Drift, SBend
from ocelot.cpbd.magnetic_lattice import MagneticLattice
from ocelot.utils.acc_utils import (
    beam2rf,
    beam2rf_xfel_linac,
    rf2beam,
    rf2beam_xfel_linac,
)
from pydantic import BaseModel, ConfigDict, model_validator
from scipy.optimize import brentq

from .library import ChicaneSpec, InjectorSpec, LinacSpec

__all__ = [
    "ChicaneError",
    "ChicaneKnob",
    "InjectorRFKnob",
    "Knob",
    "LinacKnob",
]

#: Largest dipole angle the chicane solver will consider, in radians.  Well
#: above anything the EuXFEL compressors do (BC0 runs at ~0.14 rad).
MAX_CHICANE_ANGLE = 0.5


class ChicaneError(Exception):
    """Raised when a chicane cannot be configured as requested."""


class Knob(BaseModel):
    """Base class for high-level controls."""

    model_config = ConfigDict(extra="forbid", validate_assignment=True)

    def __repr__(self) -> str:
        # Only the parameters actually set: these get printed in run logs, and
        # a chicane carries one of three, so the default repr is mostly None.
        given = {
            name: value
            for name, value in self.model_dump().items()
            if value is not None
        }
        body = ", ".join(f"{name}={value!r}" for name, value in given.items())
        return f"{type(self).__name__}({body})"

    __str__ = __repr__

    def is_set(self) -> bool:
        """Whether this knob carries a complete setting to apply."""
        raise NotImplementedError

    def missing(self) -> tuple[str, ...]:
        """Parameters still needed before this knob can be applied.

        Empty when the knob is either fully set or entirely unset.  Knobs allow
        partial states so that they can be filled in field by field
        (``optics.injector.chirp = -8.92``); completeness is checked when the
        optics is applied, where a half-specified knob would otherwise be
        silently ignored.
        """
        return ()

    def apply(self, index, spec) -> None:
        raise NotImplementedError

    def read(self, index, spec) -> Knob:
        raise NotImplementedError

    def owns(self, index, spec) -> set[tuple[str, str]]:
        raise NotImplementedError


# --------------------------------------------------------------------------- #
# Chicanes
# --------------------------------------------------------------------------- #


def _ordered(index, group) -> tuple[list, list[float]]:
    """A supply's elements in beamline order, with their design factors."""
    pairs = sorted(
        zip(group.elements, group.factors), key=lambda pair: index.position(pair[0])
    )
    return [element for element, _ in pairs], [factor for _, factor in pairs]


def chicane_dipoles(index, spec: ChicaneSpec) -> tuple[list, list[float]]:
    """The four dipoles of a chicane, in beamline order, and their polarities."""
    group = index.resolve(spec.supply, namespace="ps")
    dipoles, factors = _ordered(index, group)

    if len(dipoles) != 4:
        raise ChicaneError(
            f"Chicane {spec.name!r} expects 4 dipoles on supply {spec.supply!r}, "
            f"found {len(dipoles)}: {', '.join(d.id for d in dipoles)}."
        )
    if not all(isinstance(dipole, SBend) for dipole in dipoles):
        raise ChicaneError(
            f"Chicane {spec.name!r} has non-SBend dipoles; the pole face "
            f"convention used here is only defined for SBend."
        )
    return dipoles, factors


def yoke_length(dipole) -> float:
    """The straight iron length of a bent dipole.

    OCELOT's ``l`` is the arc length, but the physical magnet is a fixed chord:
    ``yoke = l * sin(angle) / angle``.  Holding the yoke fixed and deriving the
    arc is the correct convention -- the alternative, holding ``l`` fixed, would
    mean the iron shortened as the magnet bent harder.
    """
    angle = abs(dipole.angle)
    if not angle:
        return float(dipole.l)
    return float(dipole.l) * math.sin(angle) / angle


def projected_gaps(index, dipoles) -> tuple[float, float]:
    """Distance along the axis spanned by each shoulder of the chicane.

    The magnets are bolted to the floor, so these are invariant: bending harder
    lengthens the *path* between them as ``1/cos(angle)`` while leaving their
    separation alone.  This is the quantity a chicane update must preserve.

    The two shoulders are measured separately rather than assumed equal, so that
    the sub-micron differences the component list carries survive a round trip.
    """
    angle = abs(dipoles[0].angle)
    return tuple(  # type: ignore[return-value]
        sum(element.l for element in index.between(dipoles[first], dipoles[second]))
        * math.cos(angle)
        for first, second in ((0, 1), (2, 3))
    )


def projected_gap(index, dipoles) -> float:
    """Axial distance spanned by the first shoulder of the chicane."""
    return projected_gaps(index, dipoles)[0]


def _rescale_shoulder(shoulder, new_path: float, name: str) -> None:
    """Stretch a shoulder to ``new_path``, moving only the drifts.

    A BPM or screen between the dipoles has a fixed physical length; only true
    drift space can absorb the change.  (In the current lattice every
    length-bearing shoulder element is already a ``Drift``, so this is a guard
    against future insertions rather than a live correction.)
    """
    drifts = [element for element in shoulder if isinstance(element, Drift)]
    fixed = sum(element.l for element in shoulder if not isinstance(element, Drift))
    slack = new_path - fixed

    if slack <= 0:
        raise ChicaneError(
            f"Chicane {name!r} needs a shoulder path of {new_path:.6g} m but "
            f"{fixed:.6g} m of it is non-drift hardware, leaving no drift space."
        )

    current = sum(drift.l for drift in drifts)
    if current <= 0:
        raise ChicaneError(
            f"Chicane {name!r} has no drift length between its dipoles to "
            f"absorb a change of angle."
        )

    scale = slack / current
    for drift in drifts:
        drift.l *= scale


def set_chicane_angle(index, spec, dipoles, factors, angle: float) -> None:
    """Set the dipole angle, updating arc lengths and shoulder drifts with it.

    Each dipole keeps its own yoke length and each shoulder its own projected
    gap.  Both are exactly invariant under this transform, so it can be applied
    repeatedly without drift, and applying the design angle is a true no-op --
    which would not hold if the four dipoles were flattened to a common length.
    """
    angle = abs(float(angle))

    if angle >= math.pi / 2:
        raise ChicaneError(f"Chicane angle {angle} rad is not physical.")

    yokes = [yoke_length(dipole) for dipole in dipoles]
    gaps = projected_gaps(index, dipoles)

    for gap, (first, second) in zip(gaps, ((0, 1), (2, 3))):
        _rescale_shoulder(
            index.between(dipoles[first], dipoles[second]),
            gap / math.cos(angle),
            spec.name,
        )

    for position, (dipole, factor, yoke) in enumerate(zip(dipoles, factors, yokes)):
        signed = angle * np.sign(factor or 1.0)
        dipole.angle = signed
        dipole.l = (angle * yoke / math.sin(angle)) if angle else yoke
        # Entry face on the outer dipoles, exit face on the inner ones, matching
        # both the design lattice and OCELOT's update_bunch_compressor.
        if position in (0, 2):
            dipole.e1 = 0.0
            dipole.e2 = signed
        else:
            dipole.e1 = signed
            dipole.e2 = 0.0


def measure_r56(index, dipoles, energy: float, lattice=None) -> float:
    """R56 of the chicane, from the real transfer matrix."""
    if lattice is None:
        lattice = MagneticLattice(index.cell, start=dipoles[0], stop=dipoles[3])
    else:
        lattice.update_transfer_maps()
    _, r_matrix, _ = lattice.transfer_maps(energy)
    return float(r_matrix[4, 5])


class ChicaneReading(BaseModel):
    """A chicane's state expressed every way at once.

    Distinct from :class:`ChicaneKnob`, which carries exactly one parameter
    because setting two would be ambiguous.  Reading has no such problem: the
    three are simply three views of one geometry.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    r56: float
    angle: float
    rho: float


class ChicaneKnob(Knob):
    """A four-dipole bunch compressor.

    Set exactly one of:

    ``r56``
        The momentum compaction [m], which is what compression is actually
        specified in.  Solved numerically against the real transfer matrix,
        seeded from the analytic small-angle value, so it stays exact even
        though the closed form is not.
    ``angle``
        The dipole bend angle [rad].
    ``rho``
        The dipole bending radius [m], OCELOT's native parameter.

    Assigning to one clears the others, so the last thing you set is what is
    used.  The drift lengths between the dipoles follow automatically, holding
    the projected geometry fixed.
    """

    _EXCLUSIVE: ClassVar[tuple[str, ...]] = ("r56", "angle", "rho")

    r56: float | None = None
    angle: float | None = None
    rho: float | None = None

    @model_validator(mode="after")
    def _only_one(self) -> ChicaneKnob:
        given = [name for name in self._EXCLUSIVE if getattr(self, name) is not None]
        if len(given) > 1:
            raise ValueError(
                f"A chicane takes exactly one of r56, angle or rho; got "
                f"{', '.join(given)}. They are three ways of saying the same "
                f"thing, so setting more than one is ambiguous."
            )
        return self

    def __setattr__(self, name, value):
        # Assigning one parameter means "use this one", so drop the others
        # rather than raising about mutual exclusivity.
        if name in self._EXCLUSIVE and value is not None:
            for other in self._EXCLUSIVE:
                if other != name:
                    self.__dict__[other] = None
                    self.__pydantic_fields_set__.discard(other)
        super().__setattr__(name, value)

    def is_set(self) -> bool:
        return any(getattr(self, name) is not None for name in self._EXCLUSIVE)

    def target_angle(self, index, spec: ChicaneSpec) -> float:
        """The dipole angle this knob asks for, solving for R56 if needed."""
        dipoles, factors = chicane_dipoles(index, spec)
        yoke = yoke_length(dipoles[0])
        gap = projected_gap(index, dipoles)

        if self.angle is not None:
            return abs(float(self.angle))

        if self.rho is not None:
            rho = abs(float(self.rho))
            if rho < yoke:
                raise ChicaneError(
                    f"Chicane {spec.name!r}: a bending radius of {rho} m is "
                    f"smaller than the {yoke:.4g} m yoke length."
                )
            return math.asin(yoke / rho)

        return self._solve_for_r56(index, spec, dipoles, factors, yoke, gap)

    def _solve_for_r56(self, index, spec, dipoles, factors, yoke, gap) -> float:
        target = float(self.r56)
        if target == 0.0:
            return 0.0
        if target > 0.0:
            raise ChicaneError(
                f"Chicane {spec.name!r}: R56 of a C-chicane is negative, got {target}."
            )

        lattice = MagneticLattice(index.cell, start=dipoles[0], stop=dipoles[3])

        def residual(angle: float) -> float:
            set_chicane_angle(index, spec, dipoles, factors, angle)
            return measure_r56(index, dipoles, spec.energy, lattice) - target

        # Small-angle seed: r56 ~= -2 * theta^2 * (gap + 2*yoke/3).
        seed = math.sqrt(-target / (2.0 * (gap + 2.0 * yoke / 3.0)))

        low = min(seed * 0.5, 1e-9)
        high = max(seed * 1.5, 1e-6)
        while residual(high) > 0:
            high *= 2.0
            if high > MAX_CHICANE_ANGLE:
                raise ChicaneError(
                    f"Chicane {spec.name!r} cannot reach an R56 of {target} m; "
                    f"it would need a dipole angle above "
                    f"{MAX_CHICANE_ANGLE} rad."
                )

        angle = brentq(residual, low, high, xtol=1e-14, rtol=1e-15)
        set_chicane_angle(index, spec, dipoles, factors, angle)
        return angle

    def apply(self, index, spec: ChicaneSpec) -> None:
        if not self.is_set():
            return
        dipoles, factors = chicane_dipoles(index, spec)
        angle = self.target_angle(index, spec)
        set_chicane_angle(index, spec, dipoles, factors, angle)

    def report(self, index, spec: ChicaneSpec) -> ChicaneReading:
        """All three equivalent parameters, for display and diagnostics."""
        dipoles, _ = chicane_dipoles(index, spec)
        angle = abs(float(dipoles[0].angle))
        return ChicaneReading(
            r56=measure_r56(index, dipoles, spec.energy),
            angle=angle,
            rho=yoke_length(dipoles[0]) / math.sin(angle) if angle else math.inf,
        )

    def read(self, index, spec: ChicaneSpec) -> ChicaneKnob:
        """The setting this chicane currently corresponds to.

        Reported as an R56, the one of the three parameters that says what the
        chicane does to the beam rather than how it is bent, and the one a
        setting is normally written in.  A knob carries exactly one of the
        three, so use :meth:`report` when all three are wanted.
        """
        return ChicaneKnob(r56=self.report(index, spec).r56)

    def owns(self, index, spec: ChicaneSpec) -> set[tuple[str, str]]:
        dipoles, _ = chicane_dipoles(index, spec)
        owned = set()
        for dipole in dipoles:
            owned.update(
                (dipole.id, attribute) for attribute in ("angle", "l", "e1", "e2")
            )
        for first, second in ((0, 1), (2, 3)):
            for element in index.between(dipoles[first], dipoles[second]):
                if isinstance(element, Drift):
                    owned.add((element.id, "l"))
        return owned


# --------------------------------------------------------------------------- #
# RF
# --------------------------------------------------------------------------- #


def _cavities(index, supplies) -> list:
    cavities = []
    for supply in supplies:
        group = index.resolve(supply, namespace="ps")
        ordered, _ = _ordered(index, group)
        cavities.extend(ordered)
    if not cavities:
        raise ValueError(f"No cavities found on {', '.join(supplies)}.")
    return cavities


def _read_rf(cavities, what: str) -> tuple[float, float]:
    """Total voltage and common phase of a cavity group."""
    total = float(sum(cavity.v for cavity in cavities))
    phases = {round(float(cavity.phi), 9) for cavity in cavities}
    if len(phases) > 1:
        warnings.warn(
            f"{what} cavities are not all at the same phase ({sorted(phases)}); "
            f"reading back the first. A single knob cannot represent this.",
            stacklevel=3,
        )
    return total, float(cavities[0].phi)


def _write_rf(cavities, total_voltage: float, phase: float) -> None:
    per_cavity = total_voltage / len(cavities)
    for cavity in cavities:
        cavity.v = per_cavity
        cavity.phi = phase


class LinacKnob(Knob):
    """An accelerating section, set by sum voltage and chirp.

    ``sum_voltage`` [GV] and ``chirp`` are the control-system quantities, mapped
    onto cavity voltage and phase by OCELOT's ``beam2rf_xfel_linac``.  Both must
    be given together: two parameters in, two out.

    The voltage is spread uniformly over the cavities, matching what OCELOT's
    ``SectionTrack.update_cavity`` does during tracking.  Note that the design
    lattice gives L1's 32 cavities four distinct gradients, which a single
    section-level voltage cannot express either way.
    """

    _REQUIRED: ClassVar[tuple[str, ...]] = ("sum_voltage", "chirp")

    sum_voltage: float | None = None
    chirp: float | None = None

    def is_set(self) -> bool:
        return all(getattr(self, name) is not None for name in self._REQUIRED)

    def missing(self) -> tuple[str, ...]:
        given = [name for name in self._REQUIRED if getattr(self, name) is not None]
        if not given or len(given) == len(self._REQUIRED):
            return ()
        return tuple(name for name in self._REQUIRED if getattr(self, name) is None)

    def apply(self, index, spec: LinacSpec) -> None:
        if not self.is_set():
            return
        voltage, phase = beam2rf_xfel_linac(
            sum_voltage=self.sum_voltage,
            chirp=self.chirp,
            init_energy=spec.init_energy,
        )
        _write_rf(_cavities(index, spec.supplies), voltage, phase)

    def rf(self, spec: LinacSpec) -> tuple[float, float]:
        """The total voltage [GV] and phase [deg] this knob asks for."""
        if not self.is_set():
            raise ValueError(f"Linac knob {spec.name!r} has no setting.")
        return beam2rf_xfel_linac(
            sum_voltage=self.sum_voltage,
            chirp=self.chirp,
            init_energy=spec.init_energy,
        )

    def read(self, index, spec: LinacSpec) -> LinacKnob:
        cavities = _cavities(index, spec.supplies)
        total, phase = _read_rf(cavities, spec.name)
        sum_voltage, chirp = rf2beam_xfel_linac(
            total, phase, init_energy=spec.init_energy
        )
        return LinacKnob(sum_voltage=float(sum_voltage), chirp=float(chirp))

    def owns(self, index, spec: LinacSpec) -> set[tuple[str, str]]:
        return {
            (cavity.id, attribute)
            for cavity in _cavities(index, spec.supplies)
            for attribute in ("v", "phi")
        }


class InjectorRFKnob(Knob):
    """A1 and AH1 together, set by the beam parameters they produce.

    The 3.9 GHz module exists to linearise the 1.3 GHz section, so the two are
    solved jointly by OCELOT's ``beam2rf``: four beam parameters in, four RF
    parameters out.  ``gun_energy`` overrides the library default when the
    incoming beam is not at the nominal energy.
    """

    E1: float | None = None
    chirp: float | None = None
    curvature: float | None = None
    skewness: float | None = None
    gun_energy: float | None = None

    _BEAM: ClassVar[tuple[str, ...]] = ("E1", "chirp", "curvature", "skewness")

    def is_set(self) -> bool:
        return all(getattr(self, name) is not None for name in self._BEAM)

    def missing(self) -> tuple[str, ...]:
        given = [name for name in self._BEAM if getattr(self, name) is not None]
        if not given or len(given) == len(self._BEAM):
            return ()
        return tuple(name for name in self._BEAM if getattr(self, name) is None)

    def _gun_energy(self, spec: InjectorSpec) -> float:
        return spec.gun_energy if self.gun_energy is None else self.gun_energy

    def rf(self, spec: InjectorSpec) -> tuple[float, float, float, float]:
        """Fundamental and harmonic voltage [GV] and phase [deg]."""
        if not self.is_set():
            raise ValueError("Injector RF knob has no setting.")
        return beam2rf(
            E1=self.E1,
            chirp=self.chirp,
            curvature=self.curvature,
            skewness=self.skewness,
            n=spec.harmonic_number,
            freq=spec.frequency,
            E0=self._gun_energy(spec),
        )

    def apply(self, index, spec: InjectorSpec) -> None:
        if not self.is_set():
            return
        v1, phi1, vh, phih = self.rf(spec)
        _write_rf(_cavities(index, [spec.fundamental]), v1, phi1)
        _write_rf(_cavities(index, [spec.harmonic]), vh, phih)

    def read(self, index, spec: InjectorSpec) -> InjectorRFKnob:
        v1, phi1 = _read_rf(_cavities(index, [spec.fundamental]), spec.fundamental)
        vh, phih = _read_rf(_cavities(index, [spec.harmonic]), spec.harmonic)
        E1, chirp, curvature, skewness = rf2beam(
            v1,
            phi1,
            vh,
            phih,
            n=spec.harmonic_number,
            freq=spec.frequency,
            E0=self._gun_energy(spec),
        )
        return InjectorRFKnob(
            E1=float(E1),
            chirp=float(chirp),
            curvature=float(curvature),
            skewness=float(skewness),
            gun_energy=self.gun_energy,
        )

    def owns(self, index, spec: InjectorSpec) -> set[tuple[str, str]]:
        cavities = _cavities(index, [spec.fundamental, spec.harmonic])
        return {
            (cavity.id, attribute) for cavity in cavities for attribute in ("v", "phi")
        }
