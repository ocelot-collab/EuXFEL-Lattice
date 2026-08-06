"""What hardware the machine has, and how it is grouped into knobs.

This is a *machine description*, not an optics.  It is versioned alongside the
component list and is loaded from ``euxfel-knobs.yaml``.  Setpoints files refer to
these knobs by name and never spell out dipole or cavity names themselves.

There are exactly three bunch compressors and five RF systems, and that will not
change without a component-list change, so the knobs are declared once here
rather than constructed at every call site.
"""

from __future__ import annotations

from importlib.resources import files

import yaml
from pydantic import BaseModel, ConfigDict

__all__ = [
    "CHICANES",
    "INJECTOR",
    "KNOB_NAMES",
    "LINACS",
    "MATCHED_SECTIONS",
    "MODULES",
    "MODULE_PREFIX",
    "TDS",
    "ChicaneSpec",
    "InjectorSpec",
    "LinacSpec",
    "MatchedSectionSpec",
    "RFModuleSpec",
    "TDSSpec",
    "spec_for",
]

KNOBS_PATH = files("euxfel") / "euxfel-knobs.yaml"


class Spec(BaseModel):
    """Base for machine descriptions loaded from YAML.

    These are pydantic models rather than plain dataclasses for one concrete
    reason: PyYAML parses ``1.3e9`` as the *string* ``"1.3e9"`` (YAML 1.1 wants
    an explicit sign in the exponent), which would otherwise reach the physics
    as a string and fail somewhere far from the cause.  Coercion happens here,
    and ``extra="forbid"`` catches typos in the YAML itself.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)


class ChicaneSpec(Spec):
    """A four-dipole C-chicane.

    Only the power supplies and a reference energy are recorded.  The yoke
    length and the projected gap between dipoles are read from the design
    lattice, so they cannot fall out of step with the component list.

    Several supplies, because a chicane is not always on one: the bunch
    compressors each sit on a single supply, but the laser heater chicane is
    spread over three.
    """

    name: str
    supplies: tuple[str, ...]
    energy: float
    description: str = ""


class LinacSpec(Spec):
    """A single-harmonic accelerating section driven by sum voltage and chirp."""

    name: str
    supplies: tuple[str, ...]
    init_energy: float
    description: str = ""


class TDSSpec(Spec):
    """A transverse deflecting structure, or a pair sharing one supply."""

    name: str
    supply: str
    frequency: float = 2.8e9
    description: str = ""


class RFModuleSpec(Spec):
    """A single RF module -- one cryomodule's worth of cavities on one supply.

    Derived from the linac and injector specs rather than listed separately, so
    the two cannot drift apart: every supply a linac names is one of its
    modules.
    """

    name: str
    supply: str
    linac: str
    description: str = ""


class InjectorSpec(Spec):
    """The A1 + AH1 pair, solved together.

    The 3.9 GHz module exists to linearise the 1.3 GHz section, so their
    voltages and phases follow jointly from the beam parameters and cannot
    sensibly be set apart.
    """

    name: str
    fundamental: str
    harmonic: str
    harmonic_number: int = 3
    frequency: float = 1.3e9
    gun_energy: float = 0.00675
    description: str = ""


class MatchedSectionSpec(Spec):
    """A stretch of machine this model decides for itself, up to ``marker``.

    Its settings are outputs rather than inputs -- the answer to "what RF and
    what quadrupoles put the design beam at ``marker``?" -- so a control-room
    file's values for the same supplies are a different answer to a different
    question, fitted to the real machine's beam.  Neither is wrong; they are
    not interchangeable.

    Note there is no ``supplies`` field.  The membership rule is *positional* --
    everything with a ``ps_id`` upstream of ``marker`` -- so the supplies are
    derived from the lattice by :class:`~euxfel.beamline.Beamline`, which
    has one, rather than listed here, where they could fall out of date.
    """

    name: str
    marker: str
    description: str = ""


def _load(path=KNOBS_PATH) -> tuple[dict, dict, dict, InjectorSpec, dict, int]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))

    chicanes = {}
    for name, entry in raw.get("chicanes", {}).items():
        entry = dict(entry)
        # `supply:` for the common single-supply case, `supplies:` for a list.
        supplies = entry.pop("supplies", None) or [entry.pop("supply")]
        chicanes[name] = ChicaneSpec(name=name, supplies=tuple(supplies), **entry)

    linacs = {}
    for name, entry in raw.get("linacs", {}).items():
        entry = dict(entry)
        linacs[name] = LinacSpec(
            name=name, supplies=tuple(entry.pop("supplies")), **entry
        )

    tds = {
        name: TDSSpec(name=name, **entry) for name, entry in raw.get("tds", {}).items()
    }

    # A single spec rather than a dict, unlike the other categories: there is
    # one injector RF system.  Named "i1" after the section it drives.
    injector = InjectorSpec(name="i1", **raw["i1"])

    matched = {
        name: MatchedSectionSpec(name=name, **entry)
        for name, entry in raw.get("matching", {}).items()
    }

    return chicanes, linacs, tds, injector, matched, raw.get("version", 1)


CHICANES, LINACS, TDS, INJECTOR, MATCHED_SECTIONS, LIBRARY_VERSION = _load()


def _module_name(supply: str) -> str:
    """``C.A2.L1`` -> ``A2``, ``C3.AH1.I1`` -> ``AH1``."""
    return supply.split(".")[1]


def _modules() -> dict[str, RFModuleSpec]:
    found: dict[str, RFModuleSpec] = {}
    for linac in LINACS.values():
        for supply in linac.supplies:
            name = _module_name(supply)
            found[name] = RFModuleSpec(name=name, supply=supply, linac=linac.name)
    for supply in (INJECTOR.fundamental, INJECTOR.harmonic):
        name = _module_name(supply)
        found[name] = RFModuleSpec(name=name, supply=supply, linac=INJECTOR.name)
    return found


#: Every RF module, keyed by the name the control room uses: A1, AH1, A2 ... A25.
MODULES: dict[str, RFModuleSpec] = _modules()

#: How a module knob is addressed in a knob path, e.g. ``modules.A7``.
MODULE_PREFIX = "modules."

#: Every knob name, in beamline order.
KNOB_NAMES: tuple[str, ...] = (
    "i1",
    "i1_tds",
    "lh",
    "bc0",
    "l1",
    "bc1",
    "b1_tds",
    "l2",
    "bc2",
    "b2_tds",
    "l3",
)


def spec_for(
    name: str,
) -> ChicaneSpec | LinacSpec | TDSSpec | InjectorSpec | RFModuleSpec:
    """The specification for a knob name or path."""
    if name.startswith(MODULE_PREFIX):
        module = name[len(MODULE_PREFIX) :]
        try:
            return MODULES[module]
        except KeyError:
            raise KeyError(
                f"{module!r} is not a known RF module. Known modules: "
                f"{', '.join(MODULES)}."
            ) from None
    for table in (CHICANES, LINACS, TDS):
        if name in table:
            return table[name]
    if name == INJECTOR.name:
        return INJECTOR
    raise KeyError(
        f"{name!r} is not a known knob. Known knobs: {', '.join(KNOB_NAMES)}."
    )
