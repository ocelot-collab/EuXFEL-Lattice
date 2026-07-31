"""Turn the design model into a model of the machine as it actually runs.

The design model is MAD-8 converted and nothing else: `euxfel convert-mad8`
reproduces the tapes to 3e-6 m in geometry and ~1e-4 in beta, and that is the
whole of its job.  Keeping it that pure is what lets
`tests/test_mad8_optics.py` hold it to MAD-8 with tolerances that never have to
be relaxed, and what makes it the right thing to generate the component list
from.

This is the second stage.  Everything it applies is a **deliberate divergence**
from MAD-8, declared in `real-model.yaml`:

* `new_markers` -- the points `sections.py` slices s2e sections at.  MAD-8 has
  no reason to carry `ocelot_start` or `lh_start`; we do.  Geometry-neutral.
* `extras` -- attributes MAD-8 cannot express, such as the laser-heater
  undulator's `Kx` or the rotated TDS.  These change the optics on purpose.
* `matching` -- quadrupole strengths re-matched at a marker.
* `new_elements` -- elements absent from MAD-8 entirely.

Separating the two stages means a disagreement with MAD-8 is always one of two
things and never ambiguous: either a conversion bug, which the design model's
tests catch, or a change declared here on purpose.
"""

from __future__ import annotations

from dataclasses import dataclass
from importlib.resources import files
from typing import Any, Iterable

import yaml
from ocelot.cpbd.elements import Drift, Marker
from ocelot.cpbd.elements.optic_element import OpticElement

#: Ours, not MAD-8's and not the component list's, so it sits with the package
#: rather than beside either release directory.
DEFAULT_REAL_MODEL_CONFIG = files("euxfel") / "real-model.yaml"

#: How close to an existing element boundary a requested marker position has to
#: be before it is snapped there instead of splitting a drift.  A nanometre is
#: far below any real placement intent and far above floating-point noise.
SNAP_TOLERANCE_M = 1e-9


class PlacementError(Exception):
    """A marker could not be placed where it was asked for."""


@dataclass(frozen=True)
class Placement:
    """One requested marker, and where it goes.

    Three forms, matching what the conversion config has always supported:

    * `reference` + `adjacent` -- immediately before or after a named element.
      Exact, and the only form that cannot be knocked off by a length changing
      upstream, so it is preferred wherever a natural anchor exists.
    * `reference` + `delta_s` -- that far past the reference element's exit.
    * `delta_s` alone -- that far from the start of the section.
    """

    name: str
    reference: str | None = None
    adjacent: str | None = None
    delta_s: float | None = None

    @classmethod
    def from_config(cls, name: str, spec: dict[str, Any]) -> "Placement":
        return cls(
            name=name,
            reference=spec.get("reference"),
            adjacent=spec.get("adjacent"),
            delta_s=spec.get("delta_s"),
        )


def load_config(path: Any = None) -> dict[str, Any]:
    """Read the real-model config, defaulting to the packaged one."""
    with open(path or DEFAULT_REAL_MODEL_CONFIG, "rb") as stream:
        return yaml.safe_load(stream) or {}


def placements_for(section: str, config: dict[str, Any]) -> list[Placement]:
    """Every marker declared for a section, in declaration order."""
    sections = config.get("sections") or {}
    declared = (sections.get(section) or {}).get("new_markers") or {}
    return [Placement.from_config(name, spec) for name, spec in declared.items()]


def _positions(sequence: Iterable[OpticElement]) -> list[float]:
    """Arc length at the entrance of each element, plus the total at the end."""
    positions, arc = [], 0.0
    for element in sequence:
        positions.append(arc)
        arc += getattr(element, "l", 0.0) or 0.0
    positions.append(arc)
    return positions


def _index_of(sequence: list[OpticElement], name: str, section: str) -> int:
    for index, element in enumerate(sequence):
        if element.id == name:
            return index
    raise PlacementError(f"{section}: no element named {name!r} to place against")


def _target_arc(
    sequence: list[OpticElement], placement: Placement, section: str
) -> float:
    """The arc length a placement asks for, measured from the section start."""
    positions = _positions(sequence)
    if placement.reference is None:
        if placement.delta_s is None:
            raise PlacementError(
                f"{section}: {placement.name!r} declares neither a reference "
                f"nor a delta_s"
            )
        return float(placement.delta_s)

    index = _index_of(sequence, placement.reference, section)
    exit_arc = positions[index] + (getattr(sequence[index], "l", 0.0) or 0.0)
    return exit_arc + float(placement.delta_s or 0.0)


def insert_markers(
    sequence: list[OpticElement],
    placements: Iterable[Placement],
    section: str = "",
) -> list[OpticElement]:
    """A copy of `sequence` with the declared markers inserted.

    Adjacent placements go in by index, which is exact.  Positional ones go in at
    the requested arc length, splitting a drift if the position falls inside one
    -- the alternative is snapping to the nearest boundary, which moves a section
    edge silently and is exactly the sort of thing that is painful to debug in a
    tracking run months later.

    A split preserves total length, so the survey is untouched; that is what
    `tests/test_real_model.py` asserts.
    """
    result = list(sequence)

    for placement in placements:
        if placement.adjacent is not None:
            index = _index_of(result, placement.reference, section)
            at = index if placement.adjacent.lower() == "before" else index + 1
            result.insert(at, Marker(eid=placement.name))
            continue

        arc = _target_arc(result, placement, section)
        result = _insert_at_arc(result, arc, placement, section)

    return result


def _insert_at_arc(
    sequence: list[OpticElement], arc: float, placement: Placement, section: str
) -> list[OpticElement]:
    """Insert a marker at an arc length, splitting a drift if need be."""
    positions = _positions(sequence)
    total = positions[-1]
    if arc < -SNAP_TOLERANCE_M or arc > total + SNAP_TOLERANCE_M:
        raise PlacementError(
            f"{section}: {placement.name!r} wants s = {arc:.6f} m, but the "
            f"section is only {total:.6f} m long"
        )

    for index, boundary in enumerate(positions):
        if abs(boundary - arc) <= SNAP_TOLERANCE_M:
            result = list(sequence)
            result.insert(index, Marker(eid=placement.name))
            return result

    # Falls strictly inside an element.  Only a drift may be split: cutting a
    # magnet in half would change what the model says the machine contains.
    for index, element in enumerate(sequence):
        start, end = positions[index], positions[index + 1]
        if not (start < arc < end):
            continue
        if not isinstance(element, Drift):
            raise PlacementError(
                f"{section}: {placement.name!r} at s = {arc:.6f} m falls inside "
                f"{element.id} ({type(element).__name__}), which cannot be split"
            )
        head = Drift(l=arc - start, eid=f"{element.id}A")
        tail = Drift(l=end - arc, eid=f"{element.id}B")
        return [
            *sequence[:index],
            head,
            Marker(eid=placement.name),
            tail,
            *sequence[index + 1 :],
        ]

    raise PlacementError(f"{section}: could not place {placement.name!r} at {arc}")
