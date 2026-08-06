"""Machine setpoints, and the file formats they are written in.

A machine's settings as data: magnet strengths and RF setpoints that can be
applied to a lattice, read back off one, and round-tripped to and from the DESY
control room's file format.

"Setpoints" rather than "optics" because it carries RF voltage, phase and chirp
as well as magnet strengths, and only the latter are optics in the usual sense.

VOLTS names the format, not the model.  What a setpoint *means* -- how a name
reaches a magnet, what a generalised kick is, what hardware exists -- belongs to
the lattice and lives above this package, in :mod:`euxfel.beamline`,
:mod:`euxfel.kicks` and :mod:`euxfel.machine`.  Nothing there knows that files
exist.  What lives here is the object those things are configured *by*
(:class:`~euxfel.volts.config.MachineSetpoints`), the physics of the high-level
knobs it exposes, and the two serialisations.

See :mod:`euxfel.volts.config` for the entry point.
"""

from .config import ConflictError, Knobs, MachineSetpoints
from .knobs import ChicaneError, ChicaneKnob, InjectorRFKnob, LinacKnob
from .sascha import read_sascha, write_sascha


def load_setpoints(path):
    """Load a setpoints file. Shorthand for :meth:`MachineSetpoints.from_yaml`."""
    return MachineSetpoints.from_yaml(path)


__all__ = [
    "ChicaneError",
    "ChicaneKnob",
    "ConflictError",
    "InjectorRFKnob",
    "Knobs",
    "LinacKnob",
    "MachineSetpoints",
    "load_setpoints",
    "read_sascha",
    "write_sascha",
]
