"""Generalised kicks: the energy-independent quantity a power supply sets.

The DESY control room stores a machine's settings as one number per supply.  That
number is a *generalised kick*: a purely geometric quantity in rad/m^n.  This is
what makes it storable as a file at all -- it does not depend on the beam
energy, so the same numbers describe the same optics at 8 GeV and at 17.5 GeV.

======================  ==============  ===========================
Element                 Kick            OCELOT attribute
======================  ==============  ===========================
``Quadrupole``          ``k1 * l``      ``k1 = kick / l``   [rad/m]
``Sextupole``           ``k2 * l``      ``k2 = kick / l``   [rad/m^2]
``Octupole``            ``k3 * l``      ``k3 = kick / l``   [rad/m^3]
``SBend`` / ``RBend``   ``angle``       ``angle``           [rad]
``Cavity``              ``v``           ``v``               [GV]
======================  ==============  ===========================

``Cavity`` is included so cavities can be addressed by power supply like
anything else, but a voltage is not a kick and is excluded from Sascha files.

Two conventions are handled here because getting either wrong is silent:

``RBend`` pole faces
    ``writer.rbend_to_string`` emits ``e1 = <component list e1> - angle/2``, so
    the rectangular part is baked into the generated value.  Changing the angle
    therefore has to shift ``e1``/``e2`` by ``-delta/2`` to leave the true pole
    face deviation alone.

Design ratios
    Elements sharing a power supply are not identical -- they can be oppositely
    wired (``QE.1.L3`` is [+, -, +]) or genuinely unequal (``C.A2.L1`` drives 32
    cavities at four distinct design gradients).  A setpoint is therefore
    distributed in proportion to the *design* kicks rather than uniformly; see
    :func:`design_factors`.
"""

from __future__ import annotations


from ocelot.cpbd.elements import (
    Cavity,
    Octupole,
    Quadrupole,
    RBend,
    SBend,
    Sextupole,
)

__all__ = [
    "KickError",
    "design_factors",
    "is_kickable",
    "kick_attribute",
    "read_kick",
    "reference_kick",
    "write_group",
    "write_kick",
]


class KickError(Exception):
    """Raised when an element has no generalised-kick representation."""


#: Element class -> (OCELOT attribute, whether the kick is the attribute times
#: the element length).  Ordered most-derived-first so the MRO walk in
#: :func:`kick_attribute` picks the right entry for subclasses.
_KICK_ATTRIBUTES: dict[type, tuple[str, bool]] = {
    Quadrupole: ("k1", True),
    Sextupole: ("k2", True),
    Octupole: ("k3", True),
    RBend: ("angle", False),
    SBend: ("angle", False),
    Cavity: ("v", False),
}

#: Kicks that are not really kicks and so never appear in a Sascha file.
_NOT_A_KICK: tuple[type, ...] = (Cavity,)


def kick_attribute(element) -> tuple[str, bool]:
    """Return ``(attribute, per_metre)`` for ``element``.

    ``per_metre`` is True when the generalised kick is the attribute multiplied
    by the element length (quadrupoles, sextupoles, octupoles) and False when
    the attribute *is* the kick (bend angles, cavity voltages).

    Raises
    ------
    KickError
        If the element type has no generalised-kick representation.
    """
    for klass in type(element).__mro__:
        try:
            return _KICK_ATTRIBUTES[klass]
        except KeyError:
            continue
    raise KickError(
        f"{element.id!r} is a {type(element).__name__}, which has no "
        f"generalised kick. Set its attributes explicitly instead, e.g. "
        f"{{{element.id!r}: {{<attribute>: <value>}}}}."
    )


def is_kickable(element) -> bool:
    """Whether ``element`` has a generalised-kick representation."""
    try:
        kick_attribute(element)
    except KickError:
        return False
    return True


def is_sascha_representable(element) -> bool:
    """Whether ``element`` can appear in a Sascha file.

    Cavities are addressable by power supply but their voltage is not a kick,
    so they are excluded.
    """
    return is_kickable(element) and not isinstance(element, _NOT_A_KICK)


def read_kick(element) -> float:
    """Return the generalised kick currently set on ``element``."""
    attribute, per_metre = kick_attribute(element)
    value = getattr(element, attribute)
    if not per_metre:
        return float(value)
    if not element.l:
        raise KickError(
            f"{element.id!r} has zero length, so its generalised kick "
            f"({attribute} * l) is not defined."
        )
    return float(value) * float(element.l)


def write_kick(element, kick: float) -> None:
    """Set ``element`` so that its generalised kick becomes ``kick``.

    For an ``RBend`` this also shifts ``e1``/``e2`` by minus half the angle
    change, preserving the pole face deviation recorded in the component list
    (see the module docstring).
    """
    attribute, per_metre = kick_attribute(element)

    if per_metre:
        if not element.l:
            raise KickError(
                f"{element.id!r} has zero length, so a generalised kick "
                f"cannot be converted to {attribute}."
            )
        setattr(element, attribute, float(kick) / float(element.l))
        return

    if attribute == "angle" and isinstance(element, RBend):
        delta = float(kick) - float(element.angle)
        element.e1 -= delta / 2.0
        element.e2 -= delta / 2.0

    setattr(element, attribute, float(kick))


def reference_kick(elements) -> float:
    """The kick of largest magnitude among ``elements``, keeping its sign.

    This is the value a power supply is taken to be set to, so that read-back
    of a group returns a number which -- fed back through :func:`write_group` --
    reproduces the group exactly.
    """
    kicks = [read_kick(element) for element in elements]
    return max(kicks, key=abs)


def partially_zero(elements) -> bool:
    """Whether some but not all of ``elements`` have a zero design kick.

    Such elements get a factor of zero and stay at zero whatever setpoint is
    applied.  That is a faithful reading of the design, but surprising enough
    that callers report it -- aggregated, since a machine has a few dozen
    correctors sitting at zero and one warning each would be noise.
    """
    kicks = [read_kick(element) for element in elements]
    if len(kicks) < 2 or max(kicks, key=abs) == 0.0:
        return False
    return any(kick == 0.0 for kick in kicks)


def design_factors(elements) -> tuple[float, ...]:
    """Per-element scale factors relative to the supply setpoint.

    ``factor[i] = design_kick[i] / reference``, so applying a setpoint ``S``
    gives element ``i`` a kick of ``S * factor[i]``.  Opposite wiring is simply
    a factor of ``-1``, and genuinely unequal magnets keep their design ratio.

    Must be called on the *pristine* design lattice.  Recomputing factors from
    an already-modified lattice would let repeated application compound them.

    Zero design kicks
        If every element is at zero the ratios are undefined and all factors
        are 1, so a setpoint distributes uniformly.  If only some are zero those
        get a factor of 0 and stay at zero; see :func:`partially_zero`.
    """
    kicks = [read_kick(element) for element in elements]
    reference = max(kicks, key=abs)

    if reference == 0.0:
        return tuple(1.0 for _ in kicks)

    return tuple(kick / reference for kick in kicks)


def write_group(elements, factors, setpoint: float) -> None:
    """Apply ``setpoint`` across a power supply, preserving design ratios."""
    if len(elements) != len(factors):
        raise ValueError(f"Got {len(elements)} elements but {len(factors)} factors.")
    for element, factor in zip(elements, factors):
        write_kick(element, setpoint * factor)
