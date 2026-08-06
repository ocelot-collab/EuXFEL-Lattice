"""The setpoints file format, and the :class:`MachineSetpoints` object behind it.

A set of setpoints is what the machine is asked to do: high-level knobs (an R56,
a chirp) plus individual magnet strengths.  It can be applied to a lattice, read
back off one, and round-tripped to and from the control room's Sascha format.

The Python object is primary and YAML is a thin layer over it -- nothing in the
knob, beamline or kick layers knows that files exist.  A file looks like::

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

    matching:                        # held back, not applied -- see `matching`
      QI.1.I1: -0.053430

Values under ``elements`` are generalised kicks (see :mod:`euxfel.kicks`)
unless given as a mapping, in which case they are OCELOT attributes verbatim.

Chicane dipoles route to their knob
    ``BB.1.I1`` is a plain line in a Sascha file, but writing its angle without
    also rescaling the drifts between the dipoles leaves a chicane whose
    geometry no longer closes.  So an ``elements`` entry naming a supply a knob
    owns is converted into a knob setting rather than written directly.

A matched section is held back
    Some of the machine this model decides for itself -- the injector up to
    ``MATCH.52.I1``.  Setpoints swept in by an importer land in ``matching``
    rather than ``elements`` and are not applied unless asked for, because
    nobody chose them among the file's several hundred supplies.  Naming one
    yourself still sets it.
"""

from __future__ import annotations

import os
import warnings
from pathlib import Path
from typing import Any, ClassVar

import yaml
from pydantic import BaseModel, ConfigDict, Field

from euxfel import machine
from euxfel.beamline import Beamline
from euxfel.kicks import is_sascha_representable
from .knobs import (
    ChicaneKnob,
    InjectorRFKnob,
    LinacKnob,
    RFModuleKnob,
    TDSKnob,
)
from .sascha import (
    VALUE_FORMAT,
    dumps_sascha,
    read_sascha,
    sascha_sign,
    write_sascha,
)

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
    lh: ChicaneKnob = Field(default_factory=ChicaneKnob)
    bc0: ChicaneKnob = Field(default_factory=ChicaneKnob)
    l1: LinacKnob = Field(default_factory=LinacKnob)
    bc1: ChicaneKnob = Field(default_factory=ChicaneKnob)
    b1_tds: TDSKnob = Field(default_factory=TDSKnob)
    l2: LinacKnob = Field(default_factory=LinacKnob)
    bc2: ChicaneKnob = Field(default_factory=ChicaneKnob)
    b2_tds: TDSKnob = Field(default_factory=TDSKnob)
    l3: LinacKnob = Field(default_factory=LinacKnob)

    #: Individual RF modules, for when one has to differ from its linac.
    #: Keyed by the control-room name -- A1, AH1, A2 ... A25.
    modules: dict[str, RFModuleKnob] = Field(default_factory=dict)

    def items(self):
        """``(path, knob)`` for every knob, in beamline order.

        Modules come last and are addressed by path -- ``modules.A7`` -- since
        there are twenty-six of them and naming each as a field would swamp the
        ten that describe the machine's sections.
        """
        named = [(name, getattr(self, name)) for name in machine.KNOB_NAMES]
        modules = [
            (f"{machine.MODULE_PREFIX}{name}", knob)
            for name, knob in self.modules.items()
        ]
        return named + modules

    def set_items(self):
        """``(path, knob)`` for the knobs that carry a setting."""
        return [(path, knob) for path, knob in self.items() if knob.is_set()]

    def get(self, path: str):
        """A knob by path, so that ``modules.A7`` works as well as ``bc2``."""
        if path.startswith(machine.MODULE_PREFIX):
            return self.modules[path[len(machine.MODULE_PREFIX) :]]
        return getattr(self, path)

    def replace(self, path: str, knob) -> None:
        """Swap in a whole knob by path.

        Named ``replace`` rather than ``set`` so it does not read like
        :meth:`Knob.set`, which sets parameters *on* a knob.
        """
        if path.startswith(machine.MODULE_PREFIX):
            self.modules[path[len(machine.MODULE_PREFIX) :]] = knob
        else:
            setattr(self, path, knob)


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
    #: Setpoints for a matched section, held back rather than applied.
    #:
    #: The importers put a supply here instead of in ``elements`` when it sits
    #: in a matched section -- a stretch of machine this model decides for
    #: itself, see :data:`euxfel.machine.MATCHED_SECTIONS`.  Nothing else
    #: writes here: setting ``setpoints["QI.1.I1"]`` yourself goes to
    #: ``elements`` and is applied, because naming a magnet is choosing it.
    #:
    #: Held values still export, so a file imported and written back out is
    #: unchanged.  Applying them takes :meth:`write_matching_section` or
    #: ``matching=True``.
    matching: dict[str, float] = Field(default_factory=dict)
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
    def lh(self) -> ChicaneKnob:
        return self.knobs.lh

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

    @property
    def modules(self) -> dict[str, RFModuleKnob]:
        """Individual RF modules, keyed A1, AH1, A2 ... A25.

        Assign one to override a single module: ``setpoints.modules["A7"] =
        RFModuleKnob(voltage=0.5, phase=0.0)``.  Its linac must then be left
        unset, since the two would fight over the same cavities.
        """
        return self.knobs.modules

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

        Bend signs are converted (see :func:`~euxfel.volts.sascha.sascha_sign`).
        Everything else is recorded verbatim, chicane supplies included, so the
        result stays a faithful copy of the file; the routing to chicane knobs
        that rescales the drifts happens later, in :meth:`apply`.

        Supplies in a matched section go to :attr:`matching` rather than
        :attr:`elements`: a file names every supply in the machine, so nobody
        chose those among them.  They still export.
        """
        beamline = _beamline_for(cell)
        values = read_sascha(path)

        setpoints = cls(name=Path(path).stem, **fields)
        matched = beamline.matched_supplies
        for key, value in values.items():
            group = beamline.resolve(key, namespace="ps")
            value *= sascha_sign(group.elements[0])
            if key in matched:
                setpoints.matching[key] = value
            else:
                setpoints.elements[key] = value
        return setpoints

    @classmethod
    def from_lattice(cls, cell=None, **fields) -> MachineSetpoints:
        """Read every knob and setpoint off a lattice.

        Like :meth:`from_sascha`, this sweeps up the whole machine, so a matched
        section's supplies land in :attr:`matching` rather than
        :attr:`elements`.
        """
        beamline = _beamline_for(cell)
        setpoints = cls(**fields)

        for name, knob in setpoints.knobs.items():
            try:
                setpoints.knobs.replace(
                    name, knob.read(beamline, machine.spec_for(name))
                )
            except Exception as error:  # a section absent from this sequence
                warnings.warn(
                    f"Could not read knob {name!r} from this lattice: {error}",
                    stacklevel=2,
                )

        owners = cls._supply_owner()
        matched = beamline.matched_supplies
        for supply in beamline.supplies:
            if supply in owners:
                continue
            group = beamline.group(supply)
            if not all(is_sascha_representable(e) for e in group.elements):
                continue
            where = setpoints.matching if supply in matched else setpoints.elements
            where[supply] = group.read()

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
                merged.knobs.replace(name, knob.model_copy(deep=True))

        merged.elements.update(child.elements)
        merged.matching.update(child.matching)

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
            owners: dict[str, str] = {}
            for name, spec in machine.CHICANES.items():
                owners.update({supply: name for supply in spec.supplies})
            for name, spec in machine.LINACS.items():
                owners.update({supply: name for supply in spec.supplies})
            owners[machine.INJECTOR.name] = machine.INJECTOR.name
            owners[machine.INJECTOR.fundamental] = machine.INJECTOR.name
            owners[machine.INJECTOR.harmonic] = machine.INJECTOR.name
            cls._SUPPLY_OWNER = owners
        return cls._SUPPLY_OWNER

    def _settings(self, *, matching: bool) -> dict:
        """The setpoints to apply: ``elements``, plus ``matching`` if asked.

        ``elements`` wins where the two name the same supply, and that is the
        provenance rule rather than an ordering accident: an entry in
        ``elements`` was put there by someone naming the supply, while one in
        ``matching`` arrived because an importer swept up the machine.  The
        deliberate one beats the incidental one.
        """
        if not matching:
            return dict(self.elements)
        return {**self.matching, **self.elements}

    def _shadowed_matching(self) -> list[str]:
        """Supplies ``elements`` overrides in ``matching``, for the verbose log."""
        return sorted(key for key in self.matching if key in self.elements)

    def _inconsistent_chicanes(self, settings: dict) -> set[str]:
        """Multi-supply chicanes whose supplies this file sets to different
        magnitudes, and which therefore cannot be routed through one angle.

        The laser heater chicane is the live case: in every control-room file
        shipped here, ``BL.3.I1`` runs about 1.75% weak against ``BL.1.I1`` and
        ``BL.4.I1``.  Folding those into a single angle would quietly discard a
        setting the machine is really running, so instead the magnets are set
        individually and a warning names the disagreement.
        """
        found: set[str] = set()
        for name, spec in machine.CHICANES.items():
            if len(spec.supplies) < 2:
                continue
            values = {
                supply: settings[supply]
                for supply in spec.supplies
                if supply in settings and isinstance(settings[supply], (int, float))
            }
            if len(values) < 2:
                continue
            magnitudes = {round(abs(float(v)), 9) for v in values.values()}
            if len(magnitudes) > 1:
                found.add(name)
                warnings.warn(
                    f"Chicane {name!r} spans {len(spec.supplies)} power "
                    f"supplies and this file sets them to different "
                    f"magnitudes ("
                    + ", ".join(f"{s}={v:+g}" for s, v in sorted(values.items()))
                    + f"), so it is not a symmetric chicane. The magnets are "
                    f"being set individually and the {name!r} knob is left "
                    f"out of it.",
                    stacklevel=4,
                )
        return found

    def _route(
        self, beamline: Beamline, settings: dict
    ) -> tuple[Knobs, list[tuple], list[str]]:
        """Split ``settings`` into knob settings and plain setpoints.

        Returns the knobs to apply (a copy, with routed entries folded in), the
        plain settings as ``(key, namespace, value)``, and a human-readable log
        of what was routed.
        """
        knobs = self.knobs.model_copy(deep=True)
        plain: list[tuple] = []
        routed: list[str] = []
        owners = self._supply_owner()
        inconsistent = self._inconsistent_chicanes(settings)
        routed_here: set[str] = set()

        for raw_key, value in settings.items():
            key, namespace = _split_namespace(raw_key)

            # An explicit `id:` is a deliberate request for one magnet, so it
            # never routes and never merges with a supply-level setting.
            owner = owners.get(key) if namespace != "id" else None

            # A chicane on several supplies can only be one angle, so it can
            # only be routed if the supplies agree.  When they do not, the
            # magnets are set individually and the asymmetry is preserved.
            if owner in inconsistent:
                owner = None

            if owner is None:
                plain.append((key, namespace, value))
                continue

            if not isinstance(value, (int, float)):
                raise ConflictError(
                    f"{raw_key!r} belongs to knob {owner!r}, so it takes a "
                    f"single setpoint, not explicit attributes."
                )

            knob = getattr(knobs, owner)
            if owner in routed_here:
                # Another supply of the same multi-supply chicane. They were
                # checked for agreement above, so this says nothing new.
                continue
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
            routed_here.add(owner)
            routed.append(
                f"{raw_key} -> knob {owner} (angle={angle:.9g} rad); "
                f"drifts between the dipoles rescaled"
            )

        return knobs, plain, routed

    def apply(
        self, beamline: Beamline, *, verbose: bool = False, matching: bool = False
    ) -> Beamline:
        """Apply these setpoints to an existing beamline, in place.

        :attr:`matching` is held back unless ``matching=True``, and a warning
        says which supplies were held and how to write them.
        """
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

        knobs, plain, routed = self._route(beamline, self._settings(matching=matching))

        if verbose:
            for line in routed:
                print(line)
            for key in self._shadowed_matching():
                print(f"{key} set in `elements`, overriding the held `matching` value")

        claimed: dict[tuple[str, str], str] = {}
        for name, knob in knobs.set_items():
            spec = machine.spec_for(name)
            for target in knob.owns(beamline, spec):
                # Two knobs over the same magnet: `l3` drives A6 to A25 as one
                # section while `modules.A7` drives A7 alone, so setting both
                # leaves the result depending on which is applied last.
                other = claimed.get(target)
                if other is not None and other != name:
                    element, attribute = target
                    raise ConflictError(
                        f"Knobs {other!r} and {name!r} both set "
                        f"{element}.{attribute}. A module belongs to its linac, "
                        f"so set the linac for the section as a whole or the "
                        f"module on its own, not both."
                    )
                claimed[target] = name

        # Reject a plain setpoint that fights a knob before changing anything.
        for key, namespace, value in plain:
            group = beamline.resolve(key, namespace=namespace)
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
            knob.apply(beamline, machine.spec_for(name))

        moved_geometry = []
        for key, namespace, value in plain:
            group = beamline.resolve(key, namespace=namespace)
            if _moves_geometry(group, value):
                moved_geometry.append(key)
            if isinstance(value, dict):
                _write_attributes(group, value, key)
            else:
                # `ignore_knob` because everything that reaches here has already
                # been decided: `_route` sent what it could to the knobs, an
                # `id:` prefix is an explicit request for the split, and the
                # warning below reports whatever geometry this moves.  Without
                # it the laser heater's three supplies -- which every shipped
                # control-room file sets to different magnitudes, so they cannot
                # be routed -- would refuse to load at all.
                group.write(float(value), ignore_knob=True)

        if moved_geometry:
            warnings.warn(
                f"{', '.join(moved_geometry)} change bend angles outside any "
                f"chicane knob, so no drift lengths were adjusted and the "
                f"survey downstream of them moves. That is expected for a "
                f"dogleg or a spectrometer; check the result with "
                f"euxfel.optics.compare_match_point_surveys if it is not.",
                stacklevel=3,
            )

        if not matching:
            self._warn_held(beamline)
        self._check_resolved(beamline, held=() if matching else self.matching)
        return beamline

    def _warn_held(self, beamline: Beamline) -> None:
        """Say what was held back, once, naming the way to write it."""
        held = sorted(key for key in self.matching if key not in self.elements)
        if not held:
            return
        sections = sorted({beamline.matched_supplies.get(key, "?") for key in held})
        warnings.warn(
            f"{len(held)} setpoints belong to matched section "
            f"{', '.join(repr(s) for s in sections)} -- a stretch of machine "
            f"this model decides for itself -- and were held at their design "
            f"values rather than applied: {', '.join(held)}. To write them "
            f"too:\n"
            f"    setpoints.write_matching_section(beamline)\n"
            f"or build with matching=True.",
            stacklevel=4,
        )

    def write_matching_section(self, beamline: Beamline) -> Beamline:
        """Write the held :attr:`matching` setpoints to ``beamline``.

        The deliberate second step: :meth:`build` gives you a beamline with the
        matched section left as this model solved it, and this overwrites it
        with what the setpoints say.

        Raises ``UnknownKeyError`` if a held supply is not in this sequence,
        rather than skipping it -- being asked to write a setpoint and silently
        not writing it is the failure this whole mechanism exists to avoid.
        """
        for key, value in self.matching.items():
            group = beamline.resolve(key, namespace="ps")
            group.write(float(value), ignore_knob=True)
        return beamline

    def apply_in_place(
        self, cell=None, *, verbose: bool = False, matching: bool = False
    ) -> Beamline:
        """Apply these setpoints to ``cell`` itself, mutating the caller's elements.

        ``cell`` defaults to the whole machine
        (:func:`~euxfel.beamline.all_machine_elements`), which is almost
        always what is meant here: the point of this method is to reach every
        section, and a setpoints file is machine-wide.

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

        The returned :class:`Beamline` wraps the caller's own elements, so it is
        a way to go on addressing them by name, not a copy to work in.
        """
        beamline = _beamline_for(cell, copy_elements=False)
        self.apply(beamline, verbose=verbose, matching=matching)
        return beamline

    def build(
        self, cell=None, *, verbose: bool = False, matching: bool = False
    ) -> Beamline:
        """Apply these setpoints to a copy of ``cell`` and return the new sequence.

        The caller's elements are never touched: the generated cells are shared
        by every section and by ``sequences.cathode_to_*``, so mutating them
        would leak into the whole process.

        The result is a :class:`Beamline`, which is a sequence -- hand it
        straight to ``MagneticLattice`` -- and is also still addressable by
        name, so the magnets can be read back or adjusted further.  Use
        ``.cell`` for a plain list to concatenate.

        ``cell`` defaults to the whole machine
        (:func:`~euxfel.beamline.all_machine_elements`), which is what you
        want when you are going to read setpoints back or export them.  **Pass
        the ``cathode_to_*`` you mean if you are going to track**, because the
        default is a catalogue of every element and not a beam path.
        """
        beamline = _beamline_for(cell)
        self.apply(beamline, verbose=verbose, matching=matching)
        return beamline

    def _check_resolved(self, beamline: Beamline, held=()) -> None:
        """Warn if the recorded snapshot disagrees with what we just applied.

        ``held`` names supplies deliberately not applied, which would otherwise
        all report as drifted -- a false alarm about the one thing we just chose
        to do.
        """
        if not self.resolved:
            return
        drifted = []
        for key, expected in self.resolved.items():
            if key in held:
                continue
            try:
                actual = beamline.resolve(key).read()
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

    def resolve(self, cell=None) -> dict[str, float]:
        """Every supply setpoint these produce, as a flat mapping.

        ``matching=True``: this is a serialisation of what these setpoints
        *say*, not a lattice to track, so a held value is still one of the
        things they say.
        """
        beamline = _beamline_for(cell)
        self.apply(beamline, matching=True)
        return {
            supply: beamline.group(supply).read()
            for supply in beamline.supplies
            if all(is_sascha_representable(e) for e in beamline.group(supply).elements)
        }

    def to_dict(self, *, include_unset: bool = False) -> dict[str, Any]:
        data = self.model_dump(exclude_none=True, exclude_defaults=not include_unset)
        knobs: dict[str, Any] = {}
        for path, knob in self.knobs.set_items():
            dumped = knob.model_dump(exclude_none=True)
            if path.startswith(machine.MODULE_PREFIX):
                name = path[len(machine.MODULE_PREFIX) :]
                knobs.setdefault("modules", {})[name] = dumped
            else:
                knobs[path] = dumped
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

    def sascha_values(
        self,
        cell=None,
        *,
        keys=None,
        names=None,
        between=None,
        within=None,
        changed: bool = False,
    ) -> dict[str, float]:
        """These setpoints as ``{supply: Sascha value}``, signs converted.

        Held :attr:`matching` values are included, so a file imported and
        written back out is unchanged.  Holding is about what reaches a
        *lattice*, not about what these setpoints contain.

        ``names``/``between``/``within``/``changed`` narrow what is written; see
        :meth:`~euxfel.beamline.Beamline.select`, which does the work.  A file
        naming every supply in the machine sets every supply in the machine when
        the control room applies it, so exporting only what you mean to change
        is the difference between a 108-line file and a 476-line one.

        ``changed`` here means *differs in the file*: a supply whose value
        rounds to the design value at six decimal places would be written as a
        line setting what is already set, so it is left out.  That is a
        narrower question than
        :meth:`~euxfel.beamline.Beamline.select`'s, which asks whether the
        numbers differ at all -- of the 108 supplies ``BC2_TDS.txt`` moves, only
        45 move by more than the format can record.

        ``keys`` is the other way of narrowing: exactly these, in this order.
        It is what makes a round trip byte identical, and so cannot be combined
        with a selection -- one says *which*, the other says *work it out*.
        """
        selection = {
            "names": names,
            "between": between,
            "within": within,
            "changed": changed or None,
        }
        selection = {key: value for key, value in selection.items() if value}
        if keys is not None and selection:
            raise ValueError(
                f"`keys` names the supplies to write, in order. A selection "
                f"({', '.join(sorted(selection))}) works them out instead. "
                f"Pass one or the other, not both."
            )

        beamline = _beamline_for(cell)

        # Check before applying: setpoints that cannot be exported should say so
        # rather than first doing all the work of building the lattice.
        split = []
        for raw_key in self.elements:
            key, namespace = _split_namespace(raw_key)
            if namespace != "id":
                continue
            if beamline.resolve(key, namespace="id").split_from:
                split.append(raw_key)
        if split:
            raise ValueError(
                f"These setpoints set {', '.join(split)} apart from the rest of "
                f"its power supply, which the Sascha format cannot represent -- "
                f"it stores one value per supply. Remove the 'id:' entries to "
                f"export."
            )

        self.apply(beamline, matching=True)

        def representable(supply):
            return all(
                is_sascha_representable(e) for e in beamline.group(supply).elements
            )

        def writes_the_same_value(supply):
            """Whether this supply's line would be the design value anyway.

            `changed` on a Beamline means "differs at all", which is the right
            answer for a lattice.  A file is written to six decimal places, so
            here it means "differs *in the file*" -- and of the 108 supplies
            BC2_TDS.txt moves, 63 move by less than the format can record.
            Writing those would be 63 lines setting what is already set, which
            is exactly the clobbering a selection exists to avoid.
            """
            group = beamline.group(supply)
            sign = sascha_sign(group.elements[0])
            return VALUE_FORMAT.format(group.read() * sign) == VALUE_FORMAT.format(
                beamline.design_reference(supply) * sign
            )

        if keys is not None:
            wanted = list(keys)
        elif selection:
            wanted = list(beamline.select(**{**selection, "changed": bool(changed)}))
            # A supply named outright but not writable is a mistake worth
            # raising; one merely swept up by a range is filtered, as the
            # unselected case has always done. Explicit beats incidental.
            unwritable = [
                supply
                for supply in beamline.select(names=names)
                if not representable(supply)
            ]
            if names and unwritable:
                raise ValueError(
                    f"{', '.join(unwritable)} cannot appear in a Sascha file -- "
                    f"a cavity voltage and a TDS are not generalised kicks. "
                    f"Remove them from `names`."
                )
            wanted = [supply for supply in wanted if representable(supply)]
            if changed:
                wanted = [
                    supply for supply in wanted if not writes_the_same_value(supply)
                ]
        else:
            wanted = [supply for supply in beamline.supplies if representable(supply)]

        values = {}
        for supply in wanted:
            group = beamline.group(supply)
            values[supply] = group.read() * sascha_sign(group.elements[0])
        return values

    def to_sascha(
        self,
        cell=None,
        path: str | os.PathLike | None = None,
        *,
        keys=None,
        names=None,
        between=None,
        within=None,
        changed: bool = False,
    ) -> str:
        """Export to the control-room format.

        Narrow what is written with ``names``/``between``/``within``/``changed``
        -- see :meth:`sascha_values`.
        """
        values = self.sascha_values(
            cell,
            keys=keys,
            names=names,
            between=between,
            within=within,
            changed=changed,
        )
        if path is not None:
            write_sascha(values, path, keys=keys)
        return dumps_sascha(values, keys=keys)


def _kick_attributes(group) -> set[str]:
    """The attributes a bare setpoint would write on a group."""
    from euxfel.kicks import kick_attribute

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
    from euxfel.kicks import kick_attribute

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


def _beamline_for(cell, *, copy_elements: bool = True) -> Beamline:
    """The beamline a ``cell=`` argument means.

    ``None`` means the whole machine -- see
    :func:`~euxfel.beamline.all_machine_elements`.  That is the right
    default because a setpoints file is machine-wide and no single
    ``cathode_to_*`` sequence is.  Pass the sequence you mean when you intend to
    track the result, because the catalogue is not a beam path.
    """
    from euxfel.beamline import all_machine_elements

    if cell is None:
        cell = all_machine_elements()
    if isinstance(cell, Beamline) and not copy_elements:
        return cell
    return Beamline.from_cell(cell, copy_elements=copy_elements)
