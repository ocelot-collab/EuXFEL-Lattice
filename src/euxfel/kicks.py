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
    "DESIGN_KICK",
    "KickError",
    "design_factors",
    "design_kick",
    "is_kickable",
    "kick_attribute",
    "read_kick",
    "reference_kick",
    "stamp_design_kicks",
    "write_group",
    "write_kick",
]

#: Attribute each element carries its design kick on.
#:
#: Stamped once, when the generated modules import, so it records what is
#: written in ``subsequences/*.py`` rather than whatever the element has been
#: set to since.  An ordinary attribute, so ``copy.deepcopy`` carries it into
#: every :class:`~euxfel.beamline.Beamline` and writing ``k1`` cannot lose it.
DESIGN_KICK = "design_kick"


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


def stamp_design_kicks(elements) -> int:
    """Record each element's current kick on it as its design kick.

    Called once, on the elements of the generated modules as they import, which
    is the only moment they are guaranteed to hold what the files say.  Doing it
    then rather than remembering it later is what lets everything downstream
    stop worrying about whether it is looking at a pristine lattice.

    Returns how many were stamped.  Elements with no generalised kick, and the
    two zero-length XY-quadrupole slices whose kick is undefined, are skipped --
    neither is addressable by power supply, so nothing asks them for a design.
    """
    stamped = 0
    for element in elements:
        if hasattr(element, DESIGN_KICK) or not is_kickable(element):
            continue
        try:
            setattr(element, DESIGN_KICK, read_kick(element))
        except KickError:
            continue
        stamped += 1
    return stamped


def design_kick(element) -> float:
    """The kick ``element`` has in the generated lattice.

    Falls back to its current value for elements that were never stamped -- a
    hand-built cell, or one loaded from somewhere other than
    :mod:`euxfel.subsequences`.  For those there is no better answer, and it is
    the behaviour that held everywhere before stamping existed.
    """
    try:
        return getattr(element, DESIGN_KICK)
    except AttributeError:
        return read_kick(element)


def reference_kick(elements) -> float:
    """The design kick of largest magnitude among ``elements``, keeping its sign.

    This is the value a power supply is taken to be set to, so that read-back
    of a group returns a number which -- fed back through :func:`write_group` --
    reproduces the group exactly.
    """
    kicks = [design_kick(element) for element in elements]
    return max(kicks, key=abs)


def partially_zero(elements) -> bool:
    """Whether some but not all of ``elements`` have a zero design kick.

    Such elements get a factor of zero and stay at zero whatever setpoint is
    applied.  That is a faithful reading of the design, but surprising enough
    that callers report it -- aggregated, since a machine has a few dozen
    correctors sitting at zero and one warning each would be noise.
    """
    kicks = [design_kick(element) for element in elements]
    if len(kicks) < 2 or max(kicks, key=abs) == 0.0:
        return False
    return any(kick == 0.0 for kick in kicks)


def design_factors(elements) -> tuple[float, ...]:
    """Per-element scale factors relative to the supply setpoint.

    ``factor[i] = design_kick[i] / reference``, so applying a setpoint ``S``
    gives element ``i`` a kick of ``S * factor[i]``.  Opposite wiring is simply
    a factor of ``-1``, and genuinely unequal magnets keep their design ratio.

    This is the machine's *wiring*, not its optics: it says how the magnets on a
    supply are cabled, so it never moves.  Reading it from the stamped design
    kicks rather than from the elements' current values is what makes that true
    -- it can be computed at any time, on an already-modified lattice, and comes
    out the same.

    Zero design kicks
        If every element is at zero the ratios are undefined and all factors
        are 1, so a setpoint distributes uniformly.  If only some are zero those
        get a factor of 0 and stay at zero; see :func:`partially_zero`.
    """
    kicks = [design_kick(element) for element in elements]
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
