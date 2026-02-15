from dataclasses import dataclass, field
from textwrap import dedent

import pytest
from euxfel.slicing import SlicedElement
from euxfel.writer import PythonSubsequenceWriter
from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import (
    Cavity,
    Drift,
    Hcor,
    Marker,
    Monitor,
    Octupole,
    Quadrupole,
    RBend,
    SBend,
    Sextupole,
    TDCavity,
    Undulator,
    Vcor,
)
from ocelot.cpbd.elements.optic_element import OpticElement


@dataclass
class WriterFixture:
    writer: PythonSubsequenceWriter
    sequence: list[OpticElement]
    twiss0: Twiss
    cls_names_to_eles: dict[str, list[OpticElement]]


@pytest.fixture
def writer_fix() -> WriterFixture:
    d0 = Drift()
    r0 = RBend(angle=1, l=1)
    q0 = Quadrupole(l=0.5, k1=1)
    sequence = [d0, r0, q0]
    twiss0 = Twiss(beta_x=3, beta_y=5, alpha_x=10, alpha_y=-0.5, E=5)
    cls_names_to_eles = {"Drift": [d0], "RBend": [r0], "Quadrupole": [q0]}

    return WriterFixture(
        PythonSubsequenceWriter(sequence, twiss0), sequence, twiss0, cls_names_to_eles
    )


def test_PythonSubsequenceWriter_init(writer_fix: WriterFixture) -> None:
    writer = writer_fix.writer
    assert writer.sequence is writer_fix.sequence
    assert writer.twiss0 is writer_fix.twiss0


def test_PythonSubsequenceWriter_twiss_to_string(writer_fix: WriterFixture) -> None:
    twiss0 = writer_fix.twiss0
    writer = writer_fix.writer

    expected = dedent(f"""\
    twiss0 = Twiss()
    twiss0.E = {twiss0.E}
    twiss0.alpha_x = {twiss0.alpha_x}
    twiss0.alpha_y = {twiss0.alpha_y}
    twiss0.beta_x = {twiss0.beta_x}
    twiss0.beta_y = {twiss0.beta_y}
    """)

    assert writer.twiss_to_string() == expected


@pytest.mark.parametrize(
    "var_name,element,expected_string",
    [
        (
            "d_0",
            Drift(l=0.002879000000000076, eid="D_0"),
            'd_0 = Drift(l=0.002879000000000076, eid="D_0")',
        ),
        (
            "qi_63_i1d",
            Quadrupole(l=0.2377, k1=4.401795, eid="QI.63.I1D"),  # type: ignore
            'qi_63_i1d = Quadrupole(l=0.2377, k1=4.401795, eid="QI.63.I1D")',
        ),
        (
            "bb_62_i1d",
            SBend(
                l=0.5,
                angle=0.5235987756,
                e1=0.261799388,
                e2=0.261799388,
                eid="BB.62.I1D",
            ),
            'bb_62_i1d = SBend(l=0.5, angle=0.5235987756, e1=0.261799388, e2=0.261799388, eid="BB.62.I1D")',
        ),
        (
            "bpma_63_i1d",
            Monitor(eid="BPMA.63.I1D"),
            'bpma_63_i1d = Monitor(eid="BPMA.63.I1D")',
        ),
        (
            "c_a1_1_1_i1",
            Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid="C.A1.1.1.I1"),
            'c_a1_1_1_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid="C.A1.1.1.I1")',
        ),
        ("cly_23_i1", Vcor(eid="CLY.23.I1"), 'cly_23_i1 = Vcor(eid="CLY.23.I1")'),
        (
            "kjx_54_i1",
            Hcor(l=0.175, eid="KJX.54.I1"),
            'kjx_54_i1 = Hcor(l=0.175, eid="KJX.54.I1")',
        ),
        (
            "otrc_58_i1",
            Marker(eid="OTRC.58.I1"),
            'otrc_58_i1 = Marker(eid="OTRC.58.I1")',
        ),
        (
            "kl_1998_tl",
            RBend(
                l=0.93,
                angle=-0.000101914522,
                e1=0.0,
                e2=0.0,
                tilt=1.570796327,
                eid="KL.1998.TL",
            ),
            'kl_1998_tl = RBend(l=0.93, angle=-0.000101914522, e1=0.0, e2=0.0, tilt=1.570796327, eid="KL.1998.TL")',
        ),
        (
            "saox_2555_t3",
            Sextupole(l=0.3164, k2=12.57269279, eid="SAOX.2555.T3"),
            'saox_2555_t3 = Sextupole(l=0.3164, k2=12.57269279, eid="SAOX.2555.T3")',
        ),
        (
            "oa_2042_t1",
            Octupole(l=0.2113, k3=-132.8835386, tilt=-0.13962634, eid="OA.2042.T1"),
            'oa_2042_t1 = Octupole(l=0.2113, k3=-132.8835386, tilt=-0.13962634, eid="OA.2042.T1")',
        ),
        (
            "tdsa_52_i1",
            TDCavity(l=0.7, freq=2800000000.0, tilt=1.570796327, eid="TDSA.52.I1"),
            'tdsa_52_i1 = TDCavity(l=0.7, freq=2800000000.0, tilt=1.570796327, eid="TDSA.52.I1")',
        ),
        (
            "qk_1982_tl",
            SlicedElement(
                expression="(19 * [xslice1982] + [yslice1982]) * 10",
                elements={
                    "xslice1982": RBend(
                        l=0.005276,
                        angle=1.180477777265855e-05,
                        k1=0.090359600075815,
                        e1=0.0,
                        e2=0.0,
                        eid="xslice1982",
                    ),
                    "yslice1982": RBend(
                        l=0.005276,
                        angle=-7.780804909999998e-05,
                        k1=-0.090359600075815,
                        e1=0.0,
                        e2=0.0,
                        tilt=1.570796327,
                        eid="yslice1982",
                    ),
                },
            ),
            dedent(
                """\
            xslice1982 = RBend(l=0.005276, angle=1.180477777265855e-05, k1=0.090359600075815, e1=0.0, e2=0.0, eid="xslice1982")
            yslice1982 = RBend(l=0.005276, angle=-7.780804909999998e-05, k1=-0.090359600075815, e1=0.0, e2=0.0, tilt=1.570796327, eid="yslice1982")
            qk_1982_tl = (19 * [xslice1982] + [yslice1982]) * 10""",
            ),
        ),
    ],
)
def test_PythonSubsequenceWriter_element_to_string(
    var_name: str, element: OpticElement, expected_string: str
):
    # Not hugely exhaustitive, doesn't consider all possible combinations of kwargs
    # show that every element type is in principle writable.
    writer = PythonSubsequenceWriter([], Twiss())
    assert expected_string == writer.element_to_string(element, var_name)


def test_PythonSubsequenceWriter_make_element_class_names_to_instances_map(writer_fix):
    writer = writer_fix.writer
    actual = writer.make_element_class_names_to_instances_map()
    assert actual == writer_fix.cls_names_to_eles
