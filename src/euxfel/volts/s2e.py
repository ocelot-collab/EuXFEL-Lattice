"""Bridge from an setpoints to the start-to-end tracking model.

``SectionLattice`` handles per-magnet setpoints and section-level knobs through
two different channels, so an setpoints reaches a tracking run two ways:

Per-magnet setpoints (quadrupoles, sextupoles, individual bends)
    Written onto the module-level cells *in place*, before ``SectionLattice`` is
    constructed.  ``update_sections`` has no per-magnet channel at all, and
    ``SectionLattice`` takes a list of section *classes* rather than a sequence
    -- each ``SectionTrack`` builds its own ``MagneticLattice`` from
    ``i1.cell``, ``t5.cell`` and so on inside its ``__init__``.  So there is
    nowhere to hand a freshly built sequence: the elements the sections are
    about to pick up have to be changed where they sit.  That is process-global
    and irreversible; see :meth:`~euxfel.volts.config.MachineSetpoints.apply_in_place`.

Chicane rho and cavity voltage/phase
    Emitted into the per-section ``config`` dict.  ``update_sections`` calls
    ``update_cavity``/``update_bunch_compressor``, which would overwrite
    anything set directly on the elements, so these *must* go through the dict.

So an s2e script becomes::

    setpoints = load_setpoints("sase2_14gev.yaml")
    setpoints.apply_in_place(full_machine_cell())      # quadrupoles, sextupoles

    section_lat = SectionLattice(sequence=all_sections, tws0=tws0,
                                 data_dir=data_dir)

    config = setpoints.section_config({                # rho / v / phi merged in
        A1:  {"SC": SC_exec, "smooth": True, "wake": wake_exec},
        BC0: {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec},
        ...
    })

The toggles the script already has -- ``SC``, ``CSR``, ``wake``, ``smooth``,
``match``, ``bounds`` -- are left exactly as given.  They describe the tracking
model rather than the setpoints and have no business in an setpoints file.
"""

from __future__ import annotations

import math
import warnings

from . import library
from .knobs import ChicaneKnob, InjectorRFKnob, LinacKnob, chicane_dipoles, yoke_length

__all__ = ["SECTION_FOR_KNOB", "section_config"]

#: Which ``sections.py`` class each knob drives.  The injector knob drives two,
#: since A1 and AH1 are separate sections but one RF system.
SECTION_FOR_KNOB: dict[str, tuple[str, ...]] = {
    "injector": ("A1", "AH1"),
    "bc0": ("BC0",),
    "l1": ("L1",),
    "bc1": ("BC1",),
    "l2": ("L2",),
    "bc2": ("BC2",),
    "l3": ("L3",),
}


def _section_classes() -> dict[str, type]:
    from euxfel import sections

    classes = {}
    for names in SECTION_FOR_KNOB.values():
        for name in names:
            section = getattr(sections, name, None)
            if section is not None:
                classes[name] = section
    return classes


def _chicane_settings(knob: ChicaneKnob, spec, index) -> dict[str, float]:
    """``{"rho": ...}`` for a bunch compressor section.

    ``update_bunch_compressor`` is parameterised by bending radius, so an R56 is
    solved to an angle first and then converted.
    """
    angle = knob.target_angle(index, spec)
    if not angle:
        return {"rho": 0.0}
    dipoles, _ = chicane_dipoles(index, spec)
    return {"rho": yoke_length(dipoles[0]) / math.sin(angle)}


def _cavity_count(index, supplies) -> int:
    return sum(len(index.group(supply).elements) for supply in supplies)


def section_config(setpoints, toggles: dict, index) -> dict:
    """Merge an setpoints' knob settings into a per-section tracking config.

    Parameters
    ----------
    setpoints
        The :class:`~euxfel.volts.config.MachineSetpoints` to take settings from.
    toggles
        The script's existing ``{SectionClass: {physics process toggles}}``.
        Returned unchanged apart from the added ``rho``/``v``/``phi`` keys.
    index
        A :class:`~euxfel.volts.index.LatticeIndex` over the sequence being
        tracked, used to count cavities and read chicane geometry.

    Returns
    -------
    dict
        A new config dict; ``toggles`` is not modified.
    """
    config = {section: dict(entry) for section, entry in toggles.items()}
    classes = _section_classes()
    by_class = {section: name for name, section in classes.items()}

    for name, knob in setpoints.knobs.set_items():
        spec = library.spec_for(name)
        settings: dict[str, dict[str, float]] = {}

        if isinstance(knob, ChicaneKnob):
            settings[SECTION_FOR_KNOB[name][0]] = _chicane_settings(knob, spec, index)

        elif isinstance(knob, LinacKnob):
            voltage, phase = knob.rf(spec)
            count = _cavity_count(index, spec.supplies)
            settings[SECTION_FOR_KNOB[name][0]] = {
                "v": voltage / count,
                "phi": phase,
            }

        elif isinstance(knob, InjectorRFKnob):
            v1, phi1, vh, phih = knob.rf(spec)
            settings["A1"] = {
                "v": v1 / _cavity_count(index, [spec.fundamental]),
                "phi": phi1,
            }
            settings["AH1"] = {
                "v": vh / _cavity_count(index, [spec.harmonic]),
                "phi": phih,
            }

        for section_name, values in settings.items():
            section = classes.get(section_name)
            if section is None or section not in config:
                warnings.warn(
                    f"Knob {name!r} is set but section {section_name} is not in "
                    f"this config, so its setting will not reach the tracking.",
                    stacklevel=2,
                )
                continue
            config[section].update(values)

    # Anything the script still sets by hand that an setpoints now owns is a
    # duplicate waiting to disagree; say so rather than silently overriding.
    for section, entry in toggles.items():
        name = by_class.get(section)
        if name is None:
            continue
        overridden = {key for key in ("rho", "v", "phi") if key in entry} & set(
            config[section]
        )
        if overridden and any(
            SECTION_FOR_KNOB.get(knob_name, ()) and name in SECTION_FOR_KNOB[knob_name]
            for knob_name, _ in setpoints.knobs.set_items()
        ):
            warnings.warn(
                f"{name}: {', '.join(sorted(overridden))} was given in the "
                f"config dict and is also set by the setpoints; the setpoints wins.",
                stacklevel=2,
            )

    return config
