from dataclasses import dataclass

import numpy as np
import pytest
from euxfel.slicing import SlicedElement
from ocelot.cpbd.elements import RBend
from ocelot.cpbd.magnetic_lattice import flatten


@dataclass
class SlicedFixture:
    xslice: RBend
    yslice: RBend
    se: SlicedElement
    expression: str


@pytest.fixture
def sliced_fixture() -> SlicedFixture:
    x = RBend(l=0.25, angle=0.1)
    y = RBend(l=0.25, angle=0.2, tilt=np.pi / 2)

    expression = "(2*[y] + [x]) * 2"
    se = SlicedElement(elements={"x": x, "y": y}, expression=expression)
    return SlicedFixture(x, y, se, expression)


def test_SlicedElement_init(sliced_fixture: SlicedFixture) -> None:
    sliced_element = sliced_fixture.se
    x = sliced_fixture.xslice
    y = sliced_fixture.yslice

    assert sliced_element.expression == sliced_fixture.expression
    assert sliced_element.elements == {"x": x, "y": y}
    assert sliced_element.elements["x"] is x
    assert sliced_element.elements["y"] is y


def test_SlicedElement_read_l(sliced_fixture: SlicedFixture) -> None:
    assert sliced_fixture.se.l == 1.5

def test_SlicedElement_l_cant_be_set(sliced_fixture: SlicedFixture) -> None:
    with pytest.raises(AttributeError):
        sliced_fixture.se.l = 2

def test_SlicedEelment_expand(sliced_fixture: SlicedFixture) -> None:
    x = sliced_fixture.xslice
    y = sliced_fixture.yslice
    # We use standard Python list multiplication and flatten to
    # reproduce what we know we expect
    expanded = list(flatten([2 * [y] + [x]] * 2)) # type: ignore

    assert expanded[0] is y
    assert expanded[2] is x
    assert sliced_fixture.se.expand() == expanded
