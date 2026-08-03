"""Name to element lookup, which OCELOT and the rest of this package lack.

Elements are reached everywhere else in this repository by attribute access on
the generated modules (``l1.bb_96_i1``).  There is no way to go from a name to
an element, and no way at all to go from a *power supply* name to the magnets it
feeds -- even though ``writer.py`` stamps a ``ps_id`` onto every powered element.
:class:`LatticeIndex` builds both maps.

Two namespaces, one flat lookup
    Keys are resolved against element ids *and* power supply ids.  Measured over
    the current lattice, 59 strings appear in both namespaces and **none** is
    genuinely ambiguous: in every case the supply feeds exactly one magnet, and
    that magnet has the same name.  So no prefix syntax is needed in the common
    case, and a key that ever does resolve two ways raises rather than silently
    picking one.

Copy on construction
    ``MagneticLattice`` does not copy its sequence, so ``i1.cell`` is the *same*
    objects seen by every section, by ``sequences.cathode_to_*`` and by ``euxfel
    plot``.  Mutating them would leak into every other consumer in the process
    and make applying one optics after another cumulative.  :meth:`from_cell`
    therefore deep-copies by default.
"""

from __future__ import annotations

import copy
import difflib
import warnings
from dataclasses import dataclass, field

from ocelot.cpbd.magnetic_lattice import flatten

from .kicks import (
    design_factors,
    is_kickable,
    partially_zero,
    read_kick,
    write_group,
)

__all__ = [
    "AmbiguousKeyError",
    "Group",
    "GangedMagnetError",
    "LatticeIndex",
    "UnknownKeyError",
    "clear_design_factors",
    "full_machine_cell",
]


def full_machine_cell() -> list:
    """Every element of the machine, once, in a sliceable order.

    The EuXFEL branches, so no single ``cathode_to_*`` sequence contains
    everything: the dump lines and the two SASE branches each have elements the
    others do not.  This walks the targets longest-first and appends only what
    has not been seen, giving a sequence in which every element appears exactly
    once and adjacency is preserved within each branch.  The junction between
    one branch's end and the next branch's tail is artificial, but nothing needs
    to slice across it -- the bunch compressors all live in the shared prefix.
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
#: through a LatticeIndex, so the first index built in a process necessarily
#: sees pristine elements.  Mutating a generated element by hand before any
#: index exists would defeat it.
_DESIGN_FACTORS: dict[str, tuple[float, ...]] = {}


def _remembered_factors(supply: str, elements) -> tuple[float, ...]:
    """The design ratios for ``supply``, computing them only the first time."""
    cached = _DESIGN_FACTORS.get(supply)
    # The element count guards against a differently sized group -- a supply
    # that gained or lost a magnet is a different supply, not a cache hit.
    if cached is not None and len(cached) == len(elements):
        return cached
    factors = design_factors(elements)
    _DESIGN_FACTORS[supply] = factors
    return factors


def clear_design_factors() -> None:
    """Forget the remembered ratios, so the next index re-reads them.

    For tests, and after regenerating the lattice within a live process.
    """
    _DESIGN_FACTORS.clear()


class UnknownKeyError(KeyError):
    """Raised when a name matches neither an element nor a power supply."""

    def __str__(self) -> str:  # KeyError repr()s its argument, which is noisy
        return self.args[0]


class AmbiguousKeyError(Exception):
    """Raised when a name is both an element id and a power supply id, and the
    two readings disagree about which elements are meant."""


class GangedMagnetError(Exception):
    """Raised when a magnet sharing a power supply is addressed on its own."""


@dataclass(frozen=True)
class Group:
    """The elements one setpoint controls, and how it is distributed.

    ``factors`` are captured from the design lattice, so applying ``setpoint``
    gives element ``i`` a kick of ``setpoint * factors[i]``.  Opposite wiring is
    a factor of ``-1``; unequal magnets keep their design ratio.
    """

    key: str
    elements: tuple = field(repr=False)
    factors: tuple[float, ...] = ()
    is_supply: bool = False

    def __len__(self) -> int:
        return len(self.elements)

    @property
    def ids(self) -> tuple[str, ...]:
        return tuple(element.id for element in self.elements)

    def read(self) -> float:
        """The current setpoint: the kick of largest magnitude in the group."""
        return max((read_kick(element) for element in self.elements), key=abs)

    def write(self, setpoint: float) -> None:
        """Apply ``setpoint`` across the group, preserving design ratios."""
        write_group(self.elements, self.factors, setpoint)


class LatticeIndex:
    """Resolves names to elements for a single sequence."""

    def __init__(self, cell):
        # Keep each element once.  The targets share a common prefix, so a
        # concatenation of several of them repeats the same objects, and a
        # repeated element would give `between` the wrong neighbours.
        seen_once: set[int] = set()
        self.cell = []
        for element in cell:
            if id(element) in seen_once:
                continue
            seen_once.add(id(element))
            self.cell.append(element)

        self._by_id: dict[str, list] = {}
        self._by_supply: dict[str, list] = {}
        self._positions: dict[int, int] = {}
        seen: set[int] = set()
        for position, element in enumerate(self.cell):
            self._positions.setdefault(id(element), position)
            if id(element) in seen:
                continue
            seen.add(id(element))
            self._by_id.setdefault(element.id, []).append(element)
            supply = getattr(element, "ps_id", None)
            if supply:
                self._by_supply.setdefault(supply, []).append(element)

        # Design ratios must come from the pristine lattice, before anything is
        # applied, or repeated application would compound them.
        self._factors: dict[str, tuple[float, ...]] = {}
        self.partly_unpowered: tuple[str, ...] = ()
        unpowered = []
        for supply, elements in self._by_supply.items():
            if not all(is_kickable(element) for element in elements):
                continue
            self._factors[supply] = _remembered_factors(supply, elements)
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

    @classmethod
    def from_cell(cls, cell, *, copy_elements: bool = True) -> LatticeIndex:
        """Build an index over ``cell``, deep-copying it by default.

        Pass ``copy_elements=False`` only when you intend to mutate the caller's
        elements in place -- which, for the module-level generated cells, means
        mutating global state seen by every other consumer in the process.
        """
        flat = list(flatten(cell))
        if copy_elements:
            flat = copy.deepcopy(flat)
        return cls(flat)

    # ------------------------------------------------------------------ #
    # Lookup
    # ------------------------------------------------------------------ #

    @property
    def supplies(self) -> tuple[str, ...]:
        return tuple(self._by_supply)

    def supply_of(self, element) -> str | None:
        """The power supply feeding ``element``, if it has one."""
        return getattr(element, "ps_id", None) or None

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
        return self.cell[self.position(first) + 1 : self.position(second)]

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
        )

    def resolve(
        self,
        key: str,
        *,
        namespace: str | None = None,
        allow_split: bool = False,
    ) -> Group:
        """Resolve ``key`` to the elements it names.

        Parameters
        ----------
        key
            An element id or a power supply id.
        namespace
            ``"id"`` or ``"ps"`` to force one namespace; ``None`` to search both.
        allow_split
            Permit addressing a single magnet that shares a power supply with
            others.  Such a setting is not realisable on the machine and cannot
            be written back to a Sascha file, so it is off by default.

        Raises
        ------
        UnknownKeyError, AmbiguousKeyError, GangedMagnetError
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
        if supply and len(self._by_supply[supply]) > 1 and not allow_split:
            raise GangedMagnetError(self._ganged_message(element, supply))

        factors = (1.0,)
        return Group(key=key, elements=(element,), factors=factors, is_supply=False)

    # ------------------------------------------------------------------ #
    # Error messages
    # ------------------------------------------------------------------ #

    def _ganged_message(self, element, supply: str) -> str:
        others = ", ".join(other.id for other in self.siblings(element))
        return (
            f"{element.id!r} shares power supply {supply!r} with {others} and "
            f"cannot be set individually -- that is not realisable on the "
            f"machine. Use the supply name:\n"
            f"    {supply}: <value>\n"
            f"or, to set this one magnet anyway (simulation only):\n"
            f"    {{id: {element.id}}}: <value>"
        )

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
            f"<LatticeIndex {len(self.cell)} elements, "
            f"{len(self._by_supply)} power supplies>"
        )
