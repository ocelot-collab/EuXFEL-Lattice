import pytest
from euxfel.sections import (
    A1,
    AH1,
    LH,
    DL,
    I1D,
    BC0,
    L1,
    BC1,
    L2,
    BC2,
    B2D,
    L3,
    CL1,
    CL2,
    CL3,
    TL,
    SASE1,
    T4,
    SASE3,
    T4D,
    T1,
    SASE2,
    T3,
    T5,
)


@pytest.fixture
def data_dir():
    """Provide a test data directory path."""
    return "../beam_files/"


@pytest.mark.parametrize(
    "section_cls, expected_name, expected_step",
    [
        (A1, "A1", 0.02),
        (AH1, "Injector AH1", 0.02),
        (LH, "LASER HEATER MAGNETS", 0.02),
        (DL, "DOGLEG", 0.02),
        (I1D, "I1D", 0.02),
        (BC0, "BC0", 0.02),
        (L1, "L1", 0.02),
        (BC1, "BC1", 0.02),
        (L2, "L2", 0.02),
        (BC2, "BC2", 0.02),
        (B2D, "B2D", 0.02),
        (L3, "L3", 0.2),
        (CL1, "CL1", 0.2),
        (CL2, "CL2", 1),
        (CL3, "CL3", 0.2),
        (TL, "TL", 10),
        (SASE1, "SASE1", 5),
        (T4, "T4", 0.05),
        (SASE3, "SASE3", 1),
        (T4D, "T4D", 1),  # T4D uses 'SASE3' as lattice_name
        (T1, "T1", 0.2),
        (SASE2, "SASE2", 2),
        (T3, "T3", 10),
        # (T3_chirper, "T3_chirper", 0.5), # Missing markers for passive streaker I don't know where to put
        (T5, "T5", 10),
    ],
)
def test_section_initialization(data_dir, section_cls, expected_name, expected_step):
    section = section_cls(data_dir)
    assert section.lattice_name == expected_name
    assert section.unit_step == expected_step
