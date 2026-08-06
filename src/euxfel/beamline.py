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
from collections.abc import Mapping, Sequence
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
    "design_optics",
    "set_design_optics",
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


#: Supplies whose design *optics* has been replaced, and by what.
#:
#: Empty means every supply is compared against what the generated modules say,
#: which is the stamped :data:`~euxfel.kicks.DESIGN_KICK`.  Only the optics moves
#: -- the wiring is derived from the stamps and is never overridden, because how
#: magnets share a supply is a property of the cables and not of an optics.
_DESIGN_OPTICS: dict[str, float] = {}


def design_optics() -> dict[str, float]:
    """The supplies whose design optics has been replaced, and by what.

    A copy.  Empty is the normal state: everything compared against the
    generated lattice.
    """
    return dict(_DESIGN_OPTICS)


def set_design_optics(optics=None, cell=None) -> dict[str, float]:
    """Replace what setpoints are compared against.  Returns the previous.

    ``optics`` may be a Sascha file, a YAML setpoints file, a
    :class:`~euxfel.volts.config.MachineSetpoints`, a :class:`Beamline`, or
    ``None`` to go back to what ``subsequences/*.py`` says.

    Process-wide and consulted at call time, so a beamline built before this
    answers the new question rather than the one that was current when it was
    made -- and so :meth:`MachineSetpoints.to_sascha`, which builds its own
    beamline internally, can see it.

    Two supplies are left alone whatever ``optics`` says:

    Ones it does not name
        A Sascha file names 111 of 505 supplies.  Rebasing the rest to nothing
        would report every one of them as changed from nothing.

    Chicane supplies it sets to zero
        :meth:`Beamline.design_kicks` is also what tells a chicane which way its
        dipoles bend, and a zero has no sign -- ``set_chicane_angle`` would read
        ``np.sign(0 or 1.0)`` and send all four the same way.  Those keep their
        stamped value, and a warning names them.

        Only chicane supplies: a corrector or a quadrupole sitting at zero is a
        perfectly good thing to compare against, and refusing it would report
        every such supply as differing from an optics it matches exactly.
    """
    global _DESIGN_OPTICS
    previous = dict(_DESIGN_OPTICS)

    if optics is None:
        _DESIGN_OPTICS = {}
        return previous

    values = _resolve_optics(optics, cell)

    zeroed = sorted(
        key for key, value in values.items() if value == 0.0 and key in GEOMETRY_OWNERS
    )
    if zeroed:
        warnings.warn(
            f"This optics sets {', '.join(zeroed)} to zero, and a zero has no "
            f"sign to tell the chicane which way its dipoles bend. They keep "
            f"their generated values; everything else is rebased.",
            stacklevel=2,
        )

    _DESIGN_OPTICS = {key: value for key, value in values.items() if key not in zeroed}
    return previous


def _resolve_optics(optics, cell) -> dict[str, float]:
    """``optics`` as ``{supply: generalised kick}``, whatever it arrived as."""
    from .volts.config import MachineSetpoints

    # A mapping is what this function *returns*, so it has to be accepted too:
    # restoring what `set_design_optics` handed back is the whole point of it
    # handing anything back.
    if isinstance(optics, Mapping):
        return dict(optics)
    if isinstance(optics, Beamline):
        return {
            supply: optics.group(supply).read()
            for supply in optics.supplies
            if supply in optics._factors
        }
    if isinstance(optics, MachineSetpoints):
        return optics.resolve(cell)
    # A path: Sascha if it reads as one, YAML otherwise.  `from_sascha` handles
    # the bend-sign flip, so neither branch needs to know about it here.
    path = str(optics)
    if path.endswith((".yaml", ".yml")):
        return MachineSetpoints.from_yaml(optics).resolve(cell)
    return MachineSetpoints.from_sascha(optics, cell).resolve(cell)


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

        # Both come from the stamped design kicks, so they can be computed here
        # and now regardless of what the elements have since been set to -- and
        # for exactly the elements this beamline holds, so half a supply is not
        # a special case.
        self._factors: dict[str, tuple[float, ...]] = {}
        self._references: dict[str, float] = {}
        self.partly_unpowered: tuple[str, ...] = ()
        unpowered = []
        for supply, elements in self._by_supply.items():
            if not all(is_kickable(element) for element in elements):
                continue
            self._factors[supply] = design_factors(elements)
            self._references[supply] = reference_kick(elements)
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

    def design_reference(self, supply: str) -> float:
        """The single value ``supply`` is compared against.

        The design *optics*: what the generated modules say, unless
        :func:`set_design_optics` has replaced it for this supply.
        """
        return _DESIGN_OPTICS.get(supply, self._references[supply])

    def design_kicks(self, supply: str) -> tuple[float, ...]:
        """What each magnet on ``supply`` sits at in the design optics.

        Ratios are relative to their own supply, so they cannot be compared
        across supplies; these can.  A chicane spread over several supplies
        needs them to work out its polarity pattern.

        The wiring is the beamline's own and never moves; only the reference it
        is multiplied by can be replaced, by :func:`set_design_optics`.
        """
        reference = self.design_reference(supply)
        return tuple(factor * reference for factor in self._factors[supply])

    def select(
        self, *, names=None, between=None, within=None, changed: bool = False
    ) -> tuple[str, ...]:
        """The power supplies matching every criterion given, in beamline order.

        Parameters
        ----------
        names
            Element ids or power supply ids, mixed freely.
        between
            ``(start, stop)``, inclusive: supplies with **any** magnet in the
            range.  Endpoints are marker/element names, or elements.
        within
            The same range, read the other way: supplies with **every** magnet
            in it.  Mutually exclusive with ``between``.
        changed
            Supplies whose value differs from the design optics.

        Ranges name supplies, not magnets
            A Sascha line always sets a whole supply, so there is nothing to
            refuse here -- including one whole is not wrong, and the value
            written is that supply's value, correct for every magnet on it.
            What a partial overlap costs is a *known footprint*, so the two
            words are the two honest readings and both say what they did:
            ``between`` warns about the supplies reaching past the range,
            ``within`` warns about the ones it dropped for doing so.

            "Widen the range until nothing straddles" is not a remedy:
            ``QA.1.SA1`` feeds 19 quadrupoles across the whole SASE1 undulator,
            so widening to take it in drags in every other supply there too.

        ``all_machine_elements()`` is a poor thing to range over -- its branches
        are stitched, so 53 supplies have magnets far apart in it and
        ``QH.5.TL`` has one magnet in each of two branches.  Nothing raises, but
        expect a lot of warnings; pass the ``cathode_to_*`` you mean.
        """
        if between is not None and within is not None:
            raise ValueError(
                "Give either `between` (supplies with any magnet in the range) "
                "or `within` (supplies with all of them), not both."
            )

        selected = set(self._factors) | {
            supply for supply in self._by_supply if supply not in self._factors
        }

        if names is not None:
            selected &= self._supplies_named(names)
        if between is not None:
            selected &= self._supplies_in_range(between, whole=True)
        if within is not None:
            selected &= self._supplies_in_range(within, whole=False)
        if changed:
            selected &= {
                supply for supply in self._factors if not self._at_design(supply)
            }

        return tuple(supply for supply in sorted(selected, key=self._first_position))

    def _first_position(self, supply: str) -> int:
        return min(self.position(element) for element in self._by_supply[supply])

    def _at_design(self, supply: str) -> bool:
        design = self.design_reference(supply)
        return abs(self.group(supply).read() - design) <= 1e-9 * max(1.0, abs(design))

    def _supplies_named(self, names) -> set[str]:
        """The supplies ``names`` reaches, warning about the siblings it brings.

        Naming a magnet names its supply, because that is the only thing a
        setpoint can address.  Worth saying out loud when one name turns into
        nineteen magnets.
        """
        found: set[str] = set()
        dragged: list[str] = []
        for name in names:
            group = self.resolve(name)
            supply = group.key if group.is_supply else self.supply_of(group.elements[0])
            if supply is None:
                raise UnknownKeyError(
                    f"{name!r} has no power supply, so it cannot be selected: "
                    f"a setpoint addresses a supply, not a bare element."
                )
            if not group.is_supply and len(self._by_supply[supply]) > 1:
                dragged.append(f"{name} -> {supply} ({len(self._by_supply[supply])})")
            found.add(supply)

        if dragged:
            warnings.warn(
                f"Naming a magnet names its supply, so these bring their "
                f"siblings with them: {'; '.join(dragged)}.",
                stacklevel=3,
            )
        return found

    def _supplies_in_range(self, endpoints, *, whole: bool) -> set[str]:
        """Supplies touching (``whole``) or enclosed by (not ``whole``) a range."""
        start, stop = (self._as_element(end) for end in endpoints)
        first, last = sorted((self.position(start), self.position(stop)))

        found: set[str] = set()
        overhanging: list[str] = []
        for supply, elements in self._by_supply.items():
            positions = [self.position(element) for element in elements]
            inside = [first <= position <= last for position in positions]
            if not any(inside):
                continue
            if all(inside):
                found.add(supply)
                continue
            outside = sum(1 for is_in in inside if not is_in)
            overhanging.append(f"{supply} ({outside} of {len(positions)} outside)")
            if whole:
                found.add(supply)

        if overhanging:
            what = (
                "reach past the range and are included whole, so the file "
                "touches magnets outside it"
                if whole
                else "were dropped for reaching past the range"
            )
            warnings.warn(
                f"{len(overhanging)} power supplies {what}: "
                f"{', '.join(sorted(overhanging)[:5])}"
                f"{', ...' if len(overhanging) > 5 else ''}.",
                stacklevel=3,
            )
        return found

    def _as_element(self, endpoint):
        """A range endpoint, given as a name or as an element itself."""
        if isinstance(endpoint, str):
            return self.resolve(endpoint).elements[0]
        return endpoint

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
