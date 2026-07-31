"""Optics configurations for the European XFEL.

A machine optics as data: magnet and RF setpoints that can be applied to a
lattice, read back out, and round-tripped to and from the DESY control room's
file format.

See :mod:`euxfel.volts.config` for the :class:`~euxfel.volts.config.Optics`
entry point.
"""

from .config import ConflictError, Knobs, Optics
from .index import (
    AmbiguousKeyError,
    GangedMagnetError,
    Group,
    LatticeIndex,
    UnknownKeyError,
    full_machine_cell,
)
from .kicks import KickError, read_kick, write_kick
from .knobs import ChicaneError, ChicaneKnob, InjectorRfKnob, LinacKnob
from .sascha import read_sascha, write_sascha


def load_optics(path):
    """Load an optics file. Shorthand for :meth:`Optics.from_yaml`."""
    return Optics.from_yaml(path)


__all__ = [
    "AmbiguousKeyError",
    "ChicaneError",
    "ChicaneKnob",
    "ConflictError",
    "GangedMagnetError",
    "Group",
    "InjectorRfKnob",
    "KickError",
    "Knobs",
    "LatticeIndex",
    "LinacKnob",
    "Optics",
    "UnknownKeyError",
    "full_machine_cell",
    "load_optics",
    "read_kick",
    "read_sascha",
    "write_kick",
    "write_sascha",
]
