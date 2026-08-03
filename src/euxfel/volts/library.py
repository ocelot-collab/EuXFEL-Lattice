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
    "TDS",
    "ChicaneSpec",
    "InjectorSpec",
    "LinacSpec",
    "TDSSpec",
    "spec_for",
]

KNOBS_PATH = files("euxfel.volts") / "euxfel-knobs.yaml"


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

    Only the power supply and a reference energy are recorded.  The yoke length
    and the projected gap between dipoles are read from the design lattice, so
    they cannot fall out of step with the component list.
    """

    name: str
    supply: str
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


def _load(path=KNOBS_PATH) -> tuple[dict, dict, dict, InjectorSpec, int]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))

    chicanes = {
        name: ChicaneSpec(name=name, **entry)
        for name, entry in raw.get("chicanes", {}).items()
    }

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

    return chicanes, linacs, tds, injector, raw.get("version", 1)


CHICANES, LINACS, TDS, INJECTOR, LIBRARY_VERSION = _load()

#: Every knob name, in beamline order.
KNOB_NAMES: tuple[str, ...] = (
    "i1",
    "i1_tds",
    "bc0",
    "l1",
    "bc1",
    "b1_tds",
    "l2",
    "bc2",
    "b2_tds",
    "l3",
)


def spec_for(name: str) -> ChicaneSpec | LinacSpec | TDSSpec | InjectorSpec:
    """The specification for a knob name."""
    for table in (CHICANES, LINACS, TDS):
        if name in table:
            return table[name]
    if name == INJECTOR.name:
        return INJECTOR
    raise KeyError(
        f"{name!r} is not a known knob. Known knobs: {', '.join(KNOB_NAMES)}."
    )
