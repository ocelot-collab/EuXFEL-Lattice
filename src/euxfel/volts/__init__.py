"""Machine setpoints for the European XFEL, in the VOLTS format.

A machine's settings as data: magnet strengths and RF setpoints that can be
applied to a lattice, read back off one, and round-tripped to and from the DESY
control room's file format.

"Setpoints" rather than "optics" because it carries RF voltage, phase and chirp
as well as magnet strengths, and only the latter are optics in the usual sense.

See :mod:`euxfel.volts.config` for the
:class:`~euxfel.volts.config.MachineSetpoints` entry point.
"""

from .beamline import (
    AmbiguousKeyError,
    Beamline,
    GangedMagnetError,
    Group,
    KnobOwnedError,
    UnknownKeyError,
    clear_design_factors,
    all_machine_elements,
)
from .config import ConflictError, Knobs, MachineSetpoints
from .kicks import KickError, read_kick, write_kick
from .knobs import ChicaneError, ChicaneKnob, InjectorRFKnob, LinacKnob
from .sascha import read_sascha, write_sascha


def load_setpoints(path):
    """Load a setpoints file. Shorthand for :meth:`MachineSetpoints.from_yaml`."""
    return MachineSetpoints.from_yaml(path)


__all__ = [
    "AmbiguousKeyError",
    "Beamline",
    "ChicaneError",
    "ChicaneKnob",
    "ConflictError",
    "GangedMagnetError",
    "Group",
    "InjectorRFKnob",
    "KickError",
    "KnobOwnedError",
    "Knobs",
    "LinacKnob",
    "MachineSetpoints",
    "UnknownKeyError",
    "clear_design_factors",
    "all_machine_elements",
    "load_setpoints",
    "read_kick",
    "read_sascha",
    "write_kick",
    "write_sascha",
]
