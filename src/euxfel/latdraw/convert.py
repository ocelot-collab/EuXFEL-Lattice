"""Conversion of Ocelot sequences into drawable :class:`~.lattice.Beamline`s."""

from collections.abc import Generator, Iterable
from typing import Any

from ocelot.cpbd import elements as ole

from . import elements, lattice


class UnknownElementType(RuntimeError):
    pass


def _flatten(sequence: Iterable[Any]) -> Generator[Any, None, None]:
    """Flatten nested lists and tuples of Ocelot elements.

    Needed because an XY-quadrupole ``SlicedElement`` expands to a plain list
    inside ``cell`` -- see ``subsequences.t1`` and ``subsequences.tl2tld``,
    which each embed a 200-element list.
    """
    for item in sequence:
        if isinstance(item, (list, tuple)):
            yield from _flatten(item)
        else:
            yield item


def from_ocelot(ocelot_lattice: Any) -> lattice.Beamline:
    """Convert an Ocelot sequence or ``MagneticLattice`` into a ``Beamline``."""
    sequence = getattr(ocelot_lattice, "sequence", ocelot_lattice)
    return lattice.Beamline(_loop_lattice_from_ocelot(sequence))


def _coerce(some_beamline: Any) -> lattice.Beamline:
    """Accept either an already-converted ``Beamline`` or an Ocelot sequence."""
    if isinstance(some_beamline, lattice.Beamline):
        return some_beamline
    return from_ocelot(some_beamline)


def _loop_lattice_from_ocelot(
    ocelot_sequence: Any,
) -> Generator[elements.Element, None, None]:
    assert not isinstance(ocelot_sequence, str)

    for ele in _flatten(ocelot_sequence):
        name = ele.id
        length = ele.l
        if isinstance(ele, ole.Marker):
            yield elements.Marker(name)
        elif isinstance(ele, ole.Monitor):
            yield elements.Monitor(name)
        elif isinstance(ele, ole.Drift):
            yield elements.Drift(name, length)
        elif isinstance(ele, ole.RBend):
            yield elements.RBend(name, length, ele.angle)
        elif isinstance(ele, ole.SBend):
            yield elements.SBend(name, length, ele.angle)
        elif isinstance(ele, ole.Quadrupole):
            yield elements.Quadrupole(name, length, ele.k1)
        elif isinstance(ele, ole.Sextupole):
            yield elements.Sextupole(name, length, ele.k2)
        elif isinstance(ele, ole.TDCavity):
            yield elements.TransverseDeflectingCavity(name, length, ele.v)
        elif isinstance(ele, ole.Vcor):
            yield elements.VKicker(name, length, ele.angle)
        elif isinstance(ele, ole.Hcor):
            yield elements.HKicker(name, length, ele.angle)
        elif isinstance(ele, ole.Cavity):
            yield elements.RFCavity(name, length, ele.v, ele.phi)
        elif isinstance(ele, ole.Solenoid):
            yield elements.Solenoid(name, length, ele.k)
        elif isinstance(ele, ole.Undulator):
            undulator_length = ele.nperiods * ele.lperiod
            yield elements.Undulator(name, undulator_length, kx=ele.Kx, ky=ele.Ky)
        elif isinstance(ele, ole.Octupole):
            yield elements.Octupole(name, length, ele.k3)
        else:
            raise UnknownElementType(name, type(ele))
