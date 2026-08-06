"""A sequence of elements you can address by name.

:class:`Beamline` is an ordinary Python sequence -- ``len``, iteration,
``beamline[0]``, slicing -- so it goes straight into ``MagneticLattice`` where a
list would.  What it adds is the two things OCELOT and the rest of this package
lack.

Names resolve to elements
    Elements are reached everywhere else in this repository by attribute access
    on the generated modules (``l1.bb_96_i1``).  There is no way to go from a
    name to an element, and no way at all to go from a *power supply* name to
    the magnets it feeds -- even though ``writer.py`` stamps a ``ps_id`` onto
    every powered element.  A ``Beamline`` builds both maps, and
    ``beamline["QI.1.I1"]`` searches them.

    Keys are resolved against element ids *and* power supply ids.  Measured over
    the current lattice, 59 strings appear in both namespaces and **none** is
    genuinely ambiguous: in every case the supply feeds exactly one magnet, and
    that magnet has the same name.  So no prefix syntax is needed in the common
    case, and a key that ever does resolve two ways raises rather than silently
    picking one.

The elements are its own
    ``MagneticLattice`` does not copy its sequence, so ``i1.cell`` is the *same*
    objects seen by every section, by ``sequences.cathode_to_*`` and by ``euxfel
    plot``.  Mutating them would leak into every other consumer in the process
    and make applying one setpoints file after another cumulative.
    :meth:`from_cell` therefore deep-copies by default, which is what makes a
    ``Beamline`` safe to write to.
"""

from __future__ import annotations

import copy
import difflib
import warnings
from collections.abc import Sequence
from dataclasses import dataclass, field

from ocelot.cpbd.magnetic_lattice import flatten

from . import machine
from .kicks import (
    design_factors,
    is_kickable,
    partially_zero,
    read_kick,
    reference_kick,
    write_group,
)

__all__ = [
    "AmbiguousKeyError",
    "Beamline",
    "GangedMagnetError",
    "Group",
    "KnobOwnedError",
    "UnknownKeyError",
    "all_machine_elements",
    "clear_design_factors",
]

#: Power supply -> the knob whose *geometry* it is part of.
#:
#: Only chicanes appear here.  A chicane's dipole angle cannot be changed on its
#: own: the drifts between the dipoles have to lengthen as ``1/cos(angle)`` to
#: keep the projected gap fixed, and only the knob knows to do that.  Cavity
#: supplies have no such coupling, so writing to one directly is fine and the
#: linac knobs do not claim them.
GEOMETRY_OWNERS: dict[str, str] = {
    supply: spec.name for spec in machine.CHICANES.values() for supply in spec.supplies
}


def all_machine_elements() -> list:
    """Every element in the machine, exactly once. **Not a beam path.**

    A setpoints file is machine-wide, but a lattice sequence is not: the EuXFEL
    branches, so no single ``cathode_to_*`` contains everything.  Even
    ``cathode_to_t5d``, the longest, is missing 2260 elements that live in the
    other dump lines and the SASE2 branch.  There is nothing to hand a
    whole-machine file that covers the whole machine, so this makes one.

    It walks the six targets longest-first and keeps only what it has not seen,
    which gives a list where every element appears once and adjacency survives
    *within* each branch -- enough for the chicane knobs, whose dipoles and
    shoulder drifts all sit in the shared prefix.  The joins *between* branches
    are fictional: one branch's dump is followed by the next branch's tail.

    So this is a catalogue to address and write to, not a line to track down.
    ``MagneticLattice`` will happily accept it and ``twiss`` will happily return
    a beta of 1e17.  When you mean to track, pass the ``cathode_to_*`` you mean.
    """
    from euxfel import sequences

    cell: list = []
    seen: set[int] = set()
    for name in ("t5d", "t4d", "tld", "b2d", "b1d", "i1d"):
        target = getattr(sequences, f"cathode_to_{name}", None)
        if target is None:
            continue
        for element in target:
            if id(element) in seen:
                continue
            seen.add(id(element))
            cell.append(element)
    return cell


#: Per-supply design ratios, remembered for the life of the process.
#:
#: They have to be remembered rather than re-read, because they describe the
#: *design* lattice and `MachineSetpoints.apply_in_place` overwrites the very
#: elements they are derived from.  A supply taken through zero would otherwise
#: lose its wiring for good: QE.1.L3 is [+, -, +] by design, but once its
#: magnets are all at zero there is nothing left to say so, and the next
#: setpoint would come out [+, +, +].
#:
#: This is sound because the only way this package writes to the lattice is
#: through a Beamline, so the first beamline built in a process necessarily
#: sees pristine elements.  Mutating a generated element by hand before any
#: beamline exists would defeat it.
_DESIGN_FACTORS: dict[str, tuple[float, ...]] = {}

#: The kick each supply's ratios are relative to, remembered for the same
#: reason.  Ratios alone do not place a group against its neighbours: the laser
#: heater chicane spans three supplies, and within each the ratios are (1, -1),
#: (1,) and (1,), which says nothing about the [-, +, +, -] pattern the four
#: dipoles form.  Multiplying by the reference recovers the design kicks, and
#: those do.
_DESIGN_REFERENCE: dict[str, float] = {}


def _remembered(supply: str, elements) -> tuple[tuple[float, ...], float]:
    """The design ratios and reference for ``supply``, computed once."""
    cached = _DESIGN_FACTORS.get(supply)
    # The element count guards against a differently sized group -- a supply
    # that gained or lost a magnet is a different supply, not a cache hit.
    if cached is not None and len(cached) == len(elements):
        return cached, _DESIGN_REFERENCE[supply]
    factors = design_factors(elements)
    reference = reference_kick(elements)
    _DESIGN_FACTORS[supply] = factors
    _DESIGN_REFERENCE[supply] = reference
    return factors, reference


def clear_design_factors() -> None:
    """Forget the remembered ratios, so the next beamline re-reads them.

    For tests, and after regenerating the lattice within a live process.
    """
    _DESIGN_FACTORS.clear()
    _DESIGN_REFERENCE.clear()


class UnknownKeyError(KeyError):
    """Raised when a name matches neither an element nor a power supply."""

    def __str__(self) -> str:  # KeyError repr()s its argument, which is noisy
        return self.args[0]


class AmbiguousKeyError(Exception):
    """Raised when a name is both an element id and a power supply id, and the
    two readings disagree about which elements are meant."""


class GangedMagnetError(Exception):
    """Raised when a magnet sharing a power supply is set on its own."""


class KnobOwnedError(Exception):
    """Raised when a magnet whose geometry a knob owns is set directly."""


@dataclass(frozen=True)
class Group:
    """The elements one setpoint controls, and how it is distributed.

    ``factors`` are captured from the design lattice, so applying ``setpoint``
    gives element ``i`` a kick of ``setpoint * factors[i]``.  Opposite wiring is
    a factor of ``-1``; unequal magnets keep their design ratio.

    Reading is always allowed.  Writing is not, in the two cases where the value
    that lands would not be one the machine could hold: see :meth:`write`.
    """

    key: str
    elements: tuple = field(repr=False)
    factors: tuple[float, ...] = ()
    is_supply: bool = False
    #: The knob that owns these elements' geometry, if any.
    owned_by: str | None = None
    #: The supply this single magnet was split out of, if it shares one.
    split_from: str | None = None
    #: The other magnets on that supply, for the error message.
    siblings: tuple[str, ...] = ()
    #: The matched section this sits in, if any -- informational, not a guard.
    #: A stretch of machine whose settings this model decides for itself, so
    #: setpoints swept in from a file hold it back.  Writing here is still free:
    #: naming a magnet is choosing it.  See :data:`euxfel.machine.MATCHED_SECTIONS`.
    matched_by: str | None = None

    def __len__(self) -> int:
        return len(self.elements)

    @property
    def ids(self) -> tuple[str, ...]:
        return tuple(element.id for element in self.elements)

    def read(self) -> float:
        """The current setpoint: the kick of largest magnitude in the group."""
        return max((read_kick(element) for element in self.elements), key=abs)

    def write(self, setpoint: float, *, ignore_knob: bool = False) -> None:
        """Apply ``setpoint`` across the group, preserving design ratios.

        Refused in two cases, because writing the kick is only half of what the
        setting means:

        A knob owns the geometry
            A chicane dipole's angle cannot move on its own -- the drifts
            between the dipoles have to lengthen with it, or the chicane stops
            closing.  Measured on BC0, writing the supply directly leaves the
            exit 5.9 mm downstream of where it should be and R56 0.4% out.  Use
            the knob, which rescales the drifts.

        The magnet shares a supply
            One magnet of a ganged set cannot be moved alone on the real
            machine, and the result cannot be written back to a Sascha file.

        ``ignore_knob=True`` writes anyway.  It is for the caller that has
        already decided -- a setpoints file that names a chicane supply its knob
        could not take, or an ``id:``-prefixed key asking for the split on
        purpose -- and has said so to the user.
        """
        if not ignore_knob:
            if self.owned_by:
                raise KnobOwnedError(self._owned_message())
            if self.split_from:
                raise GangedMagnetError(self._ganged_message())
        write_group(self.elements, self.factors, setpoint)

    def _owned_message(self) -> str:
        what = (
            f"feeds the {len(self)} dipoles of chicane {self.owned_by!r}"
            if self.is_supply
            else f"is a dipole of chicane {self.owned_by!r}"
        )
        return (
            f"{self.key!r} {what}, whose geometry cannot be set one magnet at a "
            f"time: the drifts between the dipoles have to lengthen with the "
            f"angle or the chicane stops closing -- the survey downstream moves "
            f"and R56 comes out wrong. Set the chicane instead:\n"
            f"    setpoints.{self.owned_by}.r56 = <value>      # or .angle, or .rho\n"
            f"or, to write the kick alone and accept the open geometry, "
            f"write(..., ignore_knob=True)."
        )

    def _ganged_message(self) -> str:
        return (
            f"{self.key!r} shares power supply {self.split_from!r} with "
            f"{', '.join(self.siblings)} and cannot be set individually -- that "
            f"is not realisable on the machine. Use the supply name:\n"
            f"    {self.split_from}: <value>\n"
            f"or, to set this one magnet anyway (simulation only):\n"
            f"    {{id: {self.key}}}: <value>"
        )


class Beamline(Sequence):
    """A sequence of elements, addressable by element or power supply name."""

    def __init__(self, cell):
        # Keep each element once.  The targets share a common prefix, so a
        # concatenation of several of them repeats the same objects, and a
        # repeated element would give `between` the wrong neighbours.
        seen_once: set[int] = set()
        self._cell: list = []
        for element in cell:
            if id(element) in seen_once:
                continue
            seen_once.add(id(element))
            self._cell.append(element)

        self._by_id: dict[str, list] = {}
        self._by_supply: dict[str, list] = {}
        self._positions: dict[int, int] = {}
        seen: set[int] = set()
        for position, element in enumerate(self._cell):
            self._positions.setdefault(id(element), position)
            if id(element) in seen:
                continue
            seen.add(id(element))
            self._by_id.setdefault(element.id, []).append(element)
            supply = getattr(element, "ps_id", None)
            if supply:
                self._by_supply.setdefault(supply, []).append(element)

        self._matched: dict[str, str] = self._find_matched_supplies()

        # Design ratios must come from the pristine lattice, before anything is
        # applied, or repeated application would compound them.
        self._factors: dict[str, tuple[float, ...]] = {}
        self._references: dict[str, float] = {}
        self.partly_unpowered: tuple[str, ...] = ()
        unpowered = []
        for supply, elements in self._by_supply.items():
            if not all(is_kickable(element) for element in elements):
                continue
            self._factors[supply], self._references[supply] = _remembered(
                supply, elements
            )
            if partially_zero(elements):
                unpowered.append(supply)

        if unpowered:
            self.partly_unpowered = tuple(unpowered)
            warnings.warn(
                f"{len(unpowered)} power supplies have a zero design kick on "
                f"some but not all of their magnets, so those magnets stay at "
                f"zero whatever setpoint is applied: "
                f"{', '.join(unpowered[:5])}"
                f"{', ...' if len(unpowered) > 5 else ''}.",
                stacklevel=2,
            )

    def _find_matched_supplies(self) -> dict[str, str]:
        """Supply -> matched section, for every supply upstream of a marker.

        Positional, and derived rather than listed, because that is what the
        rule actually is: everything the model decides for itself sits *before*
        the match point.  A magnet added upstream is covered the day it is
        added, and a sequence that does not contain the marker -- a subsequence,
        or a dump line that branches off earlier -- simply has no matched
        section, which is the right answer for it.
        """
        found: dict[str, str] = {}
        for spec in machine.MATCHED_SECTIONS.values():
            end = next(
                (i for i, e in enumerate(self._cell) if e.id == spec.marker), None
            )
            # No marker, no section.  "Everything before a point that is not in
            # this sequence" is not "everything in this sequence" -- reading it
            # that way would hold back the whole of a subsequence that happens
            # to start downstream of the injector.
            if end is None:
                continue
            for element in self._cell[:end]:
                supply = getattr(element, "ps_id", None)
                if supply:
                    found.setdefault(supply, spec.name)
        return found

    @property
    def matched_supplies(self) -> dict[str, str]:
        """Every supply a matched section covers, mapped to that section.

        A copy: this is a fact about the lattice, not a knob to turn.
        """
        return dict(self._matched)

    @classmethod
    def from_cell(cls, cell, *, copy_elements: bool = True) -> Beamline:
        """Build a beamline over ``cell``, deep-copying it by default.

        Pass ``copy_elements=False`` only when you intend to mutate the caller's
        elements in place -- which, for the module-level generated cells, means
        mutating global state seen by every other consumer in the process.
        """
        flat = list(flatten(cell))
        if copy_elements:
            flat = copy.deepcopy(flat)
        return cls(flat)

    # ------------------------------------------------------------------ #
    # Sequence protocol
    # ------------------------------------------------------------------ #

    def __len__(self) -> int:
        return len(self._cell)

    def __iter__(self):
        return iter(self._cell)

    def __getitem__(self, key):
        """``beamline[3]`` positionally, ``beamline["QI.1.I1"]`` by name.

        A slice gives a plain list rather than another ``Beamline``: the design
        ratios are a property of a whole power supply, and half a supply has
        none, so a sliced beamline would be quietly wrong to write to.
        """
        if isinstance(key, str):
            return self.resolve(key)
        return self._cell[key]

    def __contains__(self, key) -> bool:
        """``"QI.1.I1" in beamline`` by name, ``element in beamline`` by identity.

        Without this, `Sequence` would compare the string against each element
        and answer False for every name in the machine.
        """
        if isinstance(key, str):
            return key in self._by_id or key in self._by_supply
        return any(element is key for element in self._cell)

    @property
    def cell(self) -> list:
        """The elements as a plain list, for callers that need to concatenate.

        A copy, so appending to it does not lengthen the beamline; the elements
        in it are the beamline's own, so writing to them does.
        """
        return list(self._cell)

    # ------------------------------------------------------------------ #
    # Lookup
    # ------------------------------------------------------------------ #

    @property
    def supplies(self) -> tuple[str, ...]:
        return tuple(self._by_supply)

    def supply_of(self, element) -> str | None:
        """The power supply feeding ``element``, if it has one."""
        return getattr(element, "ps_id", None) or None

    def design_kicks(self, supply: str) -> tuple[float, ...]:
        """What each magnet on ``supply`` was set to in the design lattice.

        Ratios are relative to their own supply, so they cannot be compared
        across supplies; these can.  A chicane spread over several supplies
        needs them to work out its polarity pattern.
        """
        reference = self._references[supply]
        return tuple(factor * reference for factor in self._factors[supply])

    def position(self, element) -> int:
        """Index of ``element`` within the sequence.

        Needed to find what sits *between* two elements -- the shoulder drifts
        of a chicane, for instance.
        """
        try:
            return self._positions[id(element)]
        except KeyError:
            raise UnknownKeyError(
                f"{element.id!r} is not in this sequence. Elements are matched "
                f"by identity, so it may be a copy from another lattice."
            ) from None

    def between(self, first, second) -> list:
        """The elements strictly between ``first`` and ``second``."""
        return self._cell[self.position(first) + 1 : self.position(second)]

    def siblings(self, element) -> tuple:
        """Other elements sharing ``element``'s power supply."""
        supply = self.supply_of(element)
        if not supply:
            return ()
        return tuple(other for other in self._by_supply[supply] if other is not element)

    def group(self, supply: str) -> Group:
        """The :class:`Group` for a power supply name."""
        elements = self._by_supply[supply]
        return Group(
            key=supply,
            elements=tuple(elements),
            factors=self._factors.get(supply, (1.0,) * len(elements)),
            is_supply=True,
            owned_by=GEOMETRY_OWNERS.get(supply),
            matched_by=self._matched.get(supply),
        )

    def resolve(self, key: str, *, namespace: str | None = None) -> Group:
        """Resolve ``key`` to the elements it names.

        A lookup, and nothing more: every name in the machine resolves, whether
        or not it would be sensible to write to.  Looking a magnet up is
        harmless, and 1287 element ids share a power supply -- refusing to name
        them would make the beamline unusable for reading.

        Whether the result may be *written* is decided by :meth:`Group.write`,
        which knows both why it might not be allowed and how to say so.

        Parameters
        ----------
        key
            An element id or a power supply id.
        namespace
            ``"id"`` or ``"ps"`` to force one namespace; ``None`` to search both.

        Raises
        ------
        UnknownKeyError, AmbiguousKeyError
        """
        if namespace not in (None, "id", "ps"):
            raise ValueError(f"namespace must be 'id', 'ps' or None, not {namespace!r}")

        as_supply = key in self._by_supply and namespace in (None, "ps")
        as_element = key in self._by_id and namespace in (None, "id")

        if not as_supply and not as_element:
            raise UnknownKeyError(self._unknown_key_message(key, namespace))

        if as_supply and as_element:
            supply_elements = self._by_supply[key]
            element_matches = self._by_id[key]
            if {id(e) for e in supply_elements} != {id(e) for e in element_matches}:
                raise AmbiguousKeyError(
                    f"{key!r} is both an element id and a power supply id, and "
                    f"they mean different things: as a supply it feeds "
                    f"{', '.join(e.id for e in supply_elements)}. Disambiguate "
                    f"with {{ps: {key}}} or {{id: {key}}}."
                )
            # Same element either way -- prefer the supply reading.
            as_element = False

        if as_supply:
            return self.group(key)

        matches = self._by_id[key]
        if len(matches) > 1:
            raise AmbiguousKeyError(
                f"{key!r} matches {len(matches)} elements in this sequence. "
                f"Duplicate element ids cannot be addressed individually."
            )
        element = matches[0]

        supply = self.supply_of(element)
        ganged = bool(supply) and len(self._by_supply[supply]) > 1
        return Group(
            key=key,
            elements=(element,),
            factors=(1.0,),
            is_supply=False,
            owned_by=GEOMETRY_OWNERS.get(supply) if supply else None,
            split_from=supply if ganged else None,
            siblings=tuple(other.id for other in self.siblings(element))
            if ganged
            else (),
            matched_by=self._matched.get(supply) if supply else None,
        )

    # ------------------------------------------------------------------ #
    # Error messages
    # ------------------------------------------------------------------ #

    def _unknown_key_message(self, key: str, namespace: str | None) -> str:
        if namespace == "id":
            pool, what = self._by_id, "element id"
        elif namespace == "ps":
            pool, what = self._by_supply, "power supply"
        else:
            pool, what = {**self._by_id, **self._by_supply}, "element or power supply"

        message = f"{key!r} is not a known {what} in this sequence."
        close = difflib.get_close_matches(key, pool, n=3, cutoff=0.7)
        if close:
            message += f" Did you mean {', '.join(repr(c) for c in close)}?"
        return message

    def __repr__(self) -> str:
        return (
            f"<Beamline {len(self._cell)} elements, "
            f"{len(self._by_supply)} power supplies>"
        )
