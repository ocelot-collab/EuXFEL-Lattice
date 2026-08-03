"""The setpoints file format, and the :class:`MachineSetpoints` object behind it.

A set of setpoints is what the machine is asked to do: high-level knobs (an R56,
a chirp) plus individual magnet strengths.  It can be applied to a lattice, read
back off one, and round-tripped to and from the control room's Sascha format.

The Python object is primary and YAML is a thin layer over it -- nothing in the
knob, index or kick layers knows that files exist.  A file looks like::

    version: 1
    lattice: component_list_2026.02.13
    name: BC2 TDS optics
    extends: bc2_tds.yaml            # optional, single level

    knobs:
      bc2: {r56: -0.0432}
      l1:  {sum_voltage: 0.57872, chirp: -9.1}

    elements:
      QI.1.I1: -0.053430             # generalised kick, searched in both namespaces
      ps:QI.1.I1: -0.053430          # force the power supply reading
      id:BB.96.I1: -0.13             # force one magnet, splitting a shared supply
      QI.63.I1D: {k1: -2.9974}       # explicit OCELOT attributes

Values under ``elements`` are generalised kicks (see :mod:`euxfel.volts.kicks`)
unless given as a mapping, in which case they are OCELOT attributes verbatim.

Chicane dipoles route to their knob
    ``BB.1.I1`` is a plain line in a Sascha file, but writing its angle without
    also rescaling the drifts between the dipoles leaves a chicane whose
    geometry no longer closes.  So an ``elements`` entry naming a supply a knob
    owns is converted into a knob setting rather than written directly.
"""

from __future__ import annotations

import os
import warnings
from pathlib import Path
from typing import Any, ClassVar

import yaml
from pydantic import BaseModel, ConfigDict, Field

from . import library
from .index import LatticeIndex
from .kicks import is_sascha_representable
from .knobs import ChicaneKnob, InjectorRFKnob, LinacKnob, TDSKnob
from .sascha import dumps_sascha, read_sascha, sascha_sign, write_sascha

__all__ = ["ConflictError", "Knobs", "MachineSetpoints"]


class ConflictError(Exception):
    """Raised when a config sets the same thing two different ways."""


def _split_namespace(key: str) -> tuple[str, str | None]:
    """Split an optional ``id:``/``ps:`` prefix off an element key."""
    for prefix, namespace in (("id:", "id"), ("ps:", "ps")):
        if key.startswith(prefix):
            return key[len(prefix) :].strip(), namespace
    return key, None


class Knobs(BaseModel):
    """The machine's high-level controls, one field per real piece of hardware.

    Declared as named fields rather than an open mapping so that editors can
    complete them and ``knobs.bc2.chrip`` is an error rather than a silently
    ignored key.
    """

    model_config = ConfigDict(extra="forbid", validate_assignment=True)

    i1: InjectorRFKnob = Field(default_factory=InjectorRFKnob)
    i1_tds: TDSKnob = Field(default_factory=TDSKnob)
    bc0: ChicaneKnob = Field(default_factory=ChicaneKnob)
    l1: LinacKnob = Field(default_factory=LinacKnob)
    bc1: ChicaneKnob = Field(default_factory=ChicaneKnob)
    b1_tds: TDSKnob = Field(default_factory=TDSKnob)
    l2: LinacKnob = Field(default_factory=LinacKnob)
    bc2: ChicaneKnob = Field(default_factory=ChicaneKnob)
    b2_tds: TDSKnob = Field(default_factory=TDSKnob)
    l3: LinacKnob = Field(default_factory=LinacKnob)

    def items(self):
        """``(name, knob)`` for every knob, in beamline order."""
        return [(name, getattr(self, name)) for name in library.KNOB_NAMES]

    def set_items(self):
        """``(name, knob)`` for the knobs that carry a setting."""
        return [(name, knob) for name, knob in self.items() if knob.is_set()]


class MachineSetpoints(BaseModel):
    """What the machine is asked to do: knob settings plus magnet setpoints."""

    model_config = ConfigDict(extra="forbid", validate_assignment=True)

    #: Supplies that belong to a knob, and which knob owns them.
    _SUPPLY_OWNER: ClassVar[dict[str, str]] = {}

    version: int = 1
    lattice: str | None = None
    name: str | None = None
    description: str | None = None
    knobs: Knobs = Field(default_factory=Knobs)
    elements: dict[str, float | dict[str, float]] = Field(default_factory=dict)
    #: Optional snapshot of the fully resolved setpoints.  Knobs record intent,
    #: which resolves differently if the lattice changes underneath them; this
    #: records what they resolved to when the file was written.
    resolved: dict[str, float] | None = None

    # ------------------------------------------------------------------ #
    # Convenience access, so `setpoints.bc2.r56 = ...` works
    # ------------------------------------------------------------------ #

    @property
    def i1(self) -> InjectorRFKnob:
        return self.knobs.i1

    @property
    def bc0(self) -> ChicaneKnob:
        return self.knobs.bc0

    @property
    def bc1(self) -> ChicaneKnob:
        return self.knobs.bc1

    @property
    def bc2(self) -> ChicaneKnob:
        return self.knobs.bc2

    @property
    def l1(self) -> LinacKnob:
        return self.knobs.l1

    @property
    def l2(self) -> LinacKnob:
        return self.knobs.l2

    @property
    def l3(self) -> LinacKnob:
        return self.knobs.l3

    @property
    def i1_tds(self) -> TDSKnob:
        return self.knobs.i1_tds

    @property
    def b1_tds(self) -> TDSKnob:
        return self.knobs.b1_tds

    @property
    def b2_tds(self) -> TDSKnob:
        return self.knobs.b2_tds

    def __getitem__(self, key: str) -> float | dict[str, float]:
        return self.elements[key]

    def __setitem__(self, key: str, value: float | dict[str, float]) -> None:
        self.elements[key] = value

    # ------------------------------------------------------------------ #
    # Construction
    # ------------------------------------------------------------------ #

    @classmethod
    def design(cls) -> MachineSetpoints:
        """Empty setpoints: apply them and the lattice keeps its design values."""
        from euxfel.subsequences import USED_COMPONENT_LIST

        return cls(lattice=Path(str(USED_COMPONENT_LIST)).stem, name="design")

    @classmethod
    def from_yaml(cls, path: str | os.PathLike) -> MachineSetpoints:
        """Load a setpoints file, resolving a single level of ``extends``."""
        path = Path(path)
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

        parent_name = raw.pop("extends", None)
        setpoints = cls.model_validate(raw)

        if parent_name is None:
            return setpoints

        parent_path = Path(parent_name)
        if not parent_path.is_absolute():
            parent_path = path.parent / parent_path

        parent_raw = yaml.safe_load(parent_path.read_text(encoding="utf-8")) or {}
        if "extends" in parent_raw:
            raise ValueError(
                f"{path}: 'extends' is single level only, but its parent "
                f"{parent_path} also extends {parent_raw['extends']!r}."
            )

        return cls.model_validate(parent_raw).merged_with(setpoints)

    @classmethod
    def from_sascha(
        cls, path: str | os.PathLike, cell=None, **fields
    ) -> MachineSetpoints:
        """Import a control-room Sascha file.

        Bend signs are converted (see :func:`~euxfel.volts.sascha.sascha_sign`)
        and chicane supplies are routed to their knobs, so the drifts between
        the dipoles are rescaled rather than left inconsistent.
        """
        index = _index_for(cell)
        values = read_sascha(path)

        setpoints = cls(name=Path(path).stem, **fields)
        for key, value in values.items():
            group = index.resolve(key, namespace="ps")
            setpoints.elements[key] = value * sascha_sign(group.elements[0])
        return setpoints

    @classmethod
    def from_lattice(cls, cell, **fields) -> MachineSetpoints:
        """Read every knob and setpoint off a lattice."""
        index = _index_for(cell)
        setpoints = cls(**fields)

        for name, knob in setpoints.knobs.items():
            try:
                setattr(setpoints.knobs, name, knob.read(index, library.spec_for(name)))
            except Exception as error:  # a section absent from this sequence
                warnings.warn(
                    f"Could not read knob {name!r} from this lattice: {error}",
                    stacklevel=2,
                )

        owners = cls._supply_owner()
        for supply in index.supplies:
            if supply in owners:
                continue
            group = index.group(supply)
            if not all(is_sascha_representable(e) for e in group.elements):
                continue
            setpoints.elements[supply] = group.read()

        return setpoints

    def merged_with(self, child: MachineSetpoints) -> MachineSetpoints:
        """These setpoints overridden by ``child``.

        Knobs are replaced whole rather than field-wise, because a chicane's
        ``r56``/``angle``/``rho`` are three ways of saying one thing and mixing
        them across files would be ambiguous.
        """
        merged = self.model_copy(deep=True)

        for name, knob in child.knobs.items():
            if knob.is_set():
                setattr(merged.knobs, name, knob.model_copy(deep=True))

        merged.elements.update(child.elements)

        for field in ("name", "description", "lattice", "resolved"):
            value = getattr(child, field)
            if value is not None:
                setattr(merged, field, value)

        return merged

    # ------------------------------------------------------------------ #
    # Applying
    # ------------------------------------------------------------------ #

    @classmethod
    def _supply_owner(cls) -> dict[str, str]:
        if not cls._SUPPLY_OWNER:
            owners: dict[str, str] = {
                spec.supply: name for name, spec in library.CHICANES.items()
            }
            for name, spec in library.LINACS.items():
                owners.update({supply: name for supply in spec.supplies})
            owners[library.INJECTOR.name] = library.INJECTOR.name
            owners[library.INJECTOR.fundamental] = library.INJECTOR.name
            owners[library.INJECTOR.harmonic] = library.INJECTOR.name
            cls._SUPPLY_OWNER = owners
        return cls._SUPPLY_OWNER

    def _route(self, index: LatticeIndex) -> tuple[Knobs, list[tuple], list[str]]:
        """Split ``elements`` into knob settings and plain setpoints.

        Returns the knobs to apply (a copy, with routed entries folded in), the
        plain settings as ``(key, namespace, value)``, and a human-readable log
        of what was routed.
        """
        knobs = self.knobs.model_copy(deep=True)
        plain: list[tuple] = []
        routed: list[str] = []
        owners = self._supply_owner()

        for raw_key, value in self.elements.items():
            key, namespace = _split_namespace(raw_key)

            # An explicit `id:` is a deliberate request for one magnet, so it
            # never routes and never merges with a supply-level setting.
            owner = owners.get(key) if namespace != "id" else None

            if owner is None:
                plain.append((key, namespace, value))
                continue

            if not isinstance(value, (int, float)):
                raise ConflictError(
                    f"{raw_key!r} belongs to knob {owner!r}, so it takes a "
                    f"single setpoint, not explicit attributes."
                )

            knob = getattr(knobs, owner)
            if knob.is_set():
                raise ConflictError(
                    f"{raw_key!r} and knob {owner!r} both set the same "
                    f"hardware. Remove one of them."
                )

            if not isinstance(knob, ChicaneKnob):
                raise ConflictError(
                    f"{raw_key!r} belongs to knob {owner!r}, which cannot be "
                    f"set from a single number (an RF system needs both a "
                    f"voltage and a phase). Use knobs.{owner} instead."
                )

            angle = abs(float(value))
            knob.angle = angle
            routed.append(
                f"{raw_key} -> knob {owner} (angle={angle:.9g} rad); "
                f"drifts between the dipoles rescaled"
            )

        return knobs, plain, routed

    def apply(self, index: LatticeIndex, *, verbose: bool = False) -> LatticeIndex:
        """Apply these setpoints to an existing index, in place."""
        # Knobs tolerate partial states so they can be filled in field by field;
        # this is where a half-specified one has to be caught, since it would
        # otherwise be silently skipped.
        incomplete = [
            (name, knob.missing())
            for name, knob in self.knobs.items()
            if knob.missing()
        ]
        if incomplete:
            raise ConflictError(
                "These knobs are only partly set, so they cannot be applied: "
                + "; ".join(
                    f"{name} is missing {', '.join(fields)}"
                    for name, fields in incomplete
                )
                + "."
            )

        knobs, plain, routed = self._route(index)

        if verbose:
            for line in routed:
                print(line)

        claimed: dict[tuple[str, str], str] = {}
        for name, knob in knobs.set_items():
            spec = library.spec_for(name)
            for target in knob.owns(index, spec):
                claimed[target] = name

        # Reject a plain setpoint that fights a knob before changing anything.
        for key, namespace, value in plain:
            group = index.resolve(
                key, namespace=namespace, allow_split=namespace == "id"
            )
            attributes = (
                set(value) if isinstance(value, dict) else _kick_attributes(group)
            )
            for element in group.elements:
                for attribute in attributes:
                    owner = claimed.get((element.id, attribute))
                    if owner is not None:
                        raise ConflictError(
                            f"{key!r} sets {element.id}.{attribute}, which knob "
                            f"{owner!r} also controls. Remove one of them."
                        )

        for name, knob in knobs.set_items():
            knob.apply(index, library.spec_for(name))

        moved_geometry = []
        for key, namespace, value in plain:
            group = index.resolve(
                key, namespace=namespace, allow_split=namespace == "id"
            )
            if _moves_geometry(group, value):
                moved_geometry.append(key)
            if isinstance(value, dict):
                _write_attributes(group, value, key)
            else:
                group.write(float(value))

        if moved_geometry:
            warnings.warn(
                f"{', '.join(moved_geometry)} change bend angles outside any "
                f"chicane knob, so no drift lengths were adjusted and the "
                f"survey downstream of them moves. That is expected for a "
                f"dogleg or a spectrometer; check the result with "
                f"euxfel.optics.compare_match_point_surveys if it is not.",
                stacklevel=3,
            )

        self._check_resolved(index)
        return index

    def apply_in_place(self, cell, *, verbose: bool = False) -> list:
        """Apply these setpoints to ``cell`` itself, mutating the caller's elements.

        **This changes process-global state.** The generated cells are shared by
        every ``SectionTrack``, by ``sequences.cathode_to_*`` and by ``euxfel
        plot``, so after this call every one of them sees the new values, and
        there is no way back to the design short of re-importing.

        It exists because ``SectionLattice`` takes a list of section *classes*,
        not a sequence, and each ``SectionTrack`` builds its own
        ``MagneticLattice`` from the module-level cells in its ``__init__``.
        There is therefore nowhere to hand a freshly built sequence, and the only
        way per-magnet setpoints can reach a tracking run is to change the
        elements the sections will pick up.

        Prefer :meth:`build` for everything else -- optics, plots, exports,
        parameter scans -- where a private copy is both safer and free.
        """
        index = LatticeIndex.from_cell(cell, copy_elements=False)
        self.apply(index, verbose=verbose)
        return index.cell

    def build(self, cell, *, verbose: bool = False) -> list:
        """Apply these setpoints to a copy of ``cell`` and return the new sequence.

        The caller's elements are never touched: the generated cells are shared
        by every section and by ``sequences.cathode_to_*``, so mutating them
        would leak into the whole process.
        """
        index = LatticeIndex.from_cell(cell)
        self.apply(index, verbose=verbose)
        return index.cell

    def _check_resolved(self, index: LatticeIndex) -> None:
        """Warn if the recorded snapshot disagrees with what we just applied."""
        if not self.resolved:
            return
        drifted = []
        for key, expected in self.resolved.items():
            try:
                actual = index.resolve(key).read()
            except Exception:
                continue
            if abs(actual - expected) > 1e-9 * max(1.0, abs(expected)):
                drifted.append(f"{key}: recorded {expected:.9g}, got {actual:.9g}")
        if drifted:
            warnings.warn(
                "These setpoints no longer resolve to the values recorded when "
                "they were written, so the lattice has changed underneath "
                "them:\n  "
                + "\n  ".join(drifted[:10])
                + (
                    f"\n  ... and {len(drifted) - 10} more" if len(drifted) > 10 else ""
                ),
                stacklevel=3,
            )

    # ------------------------------------------------------------------ #
    # Writing
    # ------------------------------------------------------------------ #

    def resolve(self, cell) -> dict[str, float]:
        """Every supply setpoint these produce, as a flat mapping."""
        index = LatticeIndex.from_cell(cell)
        self.apply(index)
        return {
            supply: index.group(supply).read()
            for supply in index.supplies
            if all(is_sascha_representable(e) for e in index.group(supply).elements)
        }

    def to_dict(self, *, include_unset: bool = False) -> dict[str, Any]:
        data = self.model_dump(exclude_none=True, exclude_defaults=not include_unset)
        knobs = {
            name: knob.model_dump(exclude_none=True)
            for name, knob in self.knobs.set_items()
        }
        if knobs:
            data["knobs"] = knobs
        else:
            data.pop("knobs", None)
        return data

    def to_yaml(self, path: str | os.PathLike | None = None, **kwargs) -> str:
        """Serialise to YAML, writing to ``path`` if given."""
        text = yaml.safe_dump(
            self.to_dict(**kwargs), sort_keys=False, default_flow_style=False
        )
        if path is not None:
            Path(path).write_text(text, encoding="utf-8")
        return text

    def sascha_values(self, cell, *, keys=None) -> dict[str, float]:
        """These setpoints as ``{supply: Sascha value}``, signs converted."""
        index = LatticeIndex.from_cell(cell)

        # Check before applying: setpoints that cannot be exported should say so
        # rather than first doing all the work of building the lattice.
        split = []
        for raw_key in self.elements:
            key, namespace = _split_namespace(raw_key)
            if namespace != "id":
                continue
            element = index.resolve(key, namespace="id", allow_split=True).elements[0]
            if index.siblings(element):
                split.append(raw_key)
        if split:
            raise ValueError(
                f"These setpoints set {', '.join(split)} apart from the rest of "
                f"its power supply, which the Sascha format cannot represent -- "
                f"it stores one value per supply. Remove the 'id:' entries to "
                f"export."
            )

        self.apply(index)

        wanted = (
            list(keys)
            if keys is not None
            else [
                supply
                for supply in index.supplies
                if all(is_sascha_representable(e) for e in index.group(supply).elements)
            ]
        )

        values = {}
        for supply in wanted:
            group = index.group(supply)
            values[supply] = group.read() * sascha_sign(group.elements[0])
        return values

    def to_sascha(
        self, cell, path: str | os.PathLike | None = None, *, keys=None
    ) -> str:
        """Export to the control-room format."""
        values = self.sascha_values(cell, keys=keys)
        if path is not None:
            write_sascha(values, path, keys=keys)
        return dumps_sascha(values, keys=keys)


def _kick_attributes(group) -> set[str]:
    """The attributes a bare setpoint would write on a group."""
    from .kicks import kick_attribute

    return {kick_attribute(element)[0] for element in group.elements}


def _moves_geometry(group, value) -> bool:
    """Whether writing ``value`` would change a bend angle, moving the survey.

    Only reached for bends no chicane knob owns -- the I1 dogleg, the dump
    spectrometers.  There is no invariant to preserve for those: changing them
    is *supposed* to move the machine geometry, which is worth saying out loud.
    """
    from ocelot.cpbd.elements import RBend, SBend

    if not any(isinstance(element, (SBend, RBend)) for element in group.elements):
        return False
    if isinstance(value, dict):
        return "angle" in value
    return abs(float(value) - group.read()) > 1e-12
    from .kicks import kick_attribute

    return {kick_attribute(element)[0] for element in group.elements}


def valid_attributes(element) -> set[str]:
    """The OCELOT parameters that may be set on ``element``.

    Taken from the class's ``__init__`` signature, the same introspection
    ``writer.py`` uses to decide what to emit.  Validating against it is what
    stops a typo of ``k1`` from silently creating a junk attribute while you go
    on tracking design optics.
    """
    import inspect

    parameters = inspect.signature(type(element).__init__).parameters
    return {
        name
        for name, parameter in parameters.items()
        if name not in ("self", "tm", "eid")
        and parameter.kind
        not in (inspect.Parameter.VAR_KEYWORD, inspect.Parameter.VAR_POSITIONAL)
    }


def _write_attributes(group, attributes: dict[str, float], key: str) -> None:
    for element in group.elements:
        allowed = valid_attributes(element)
        for attribute, value in attributes.items():
            if attribute not in allowed:
                raise AttributeError(
                    f"{key!r}: {type(element).__name__} has no {attribute!r} "
                    f"parameter. Valid ones: {', '.join(sorted(allowed))}."
                )
            setattr(element, attribute, value)


def _index_for(cell) -> LatticeIndex:
    from .index import full_machine_cell

    if isinstance(cell, LatticeIndex):
        return cell
    if cell is None:
        cell = full_machine_cell()
    return LatticeIndex.from_cell(cell)
