import pytest
from euxfel.sequences import (
    I1D_SUBSEQUENCES,
    B1D_SUBSEQUENCES,
    B2D_SUBSEQUENCES,
    TLD_SUBSEQUENCES,
    T4D_SUBSEQUENCES,
    T5D_SUBSEQUENCES,
    TARGET_NAMES,
)
from euxfel import subsequences
from ocelot.cpbd.optics import twiss as calc_twiss
from ocelot.cpbd.magnetic_lattice import MagneticLattice
from euxfel.writer import PythonSubsequenceWriter

ALL_TARGETS_SUBSEQUENCES = [
    I1D_SUBSEQUENCES,
    B1D_SUBSEQUENCES,
    B2D_SUBSEQUENCES,
    TLD_SUBSEQUENCES,
    T4D_SUBSEQUENCES,
    T5D_SUBSEQUENCES,
]


@pytest.mark.parametrize(
    "target_subsequences", ALL_TARGETS_SUBSEQUENCES, ids=TARGET_NAMES
)
def test_subsequences_linear_optics(target_subsequences: list[str]) -> None:
    for module_name, module_name_next in zip(
        target_subsequences, target_subsequences[1:]
    ):
        module = getattr(subsequences, module_name)
        module_next = getattr(subsequences, module_name_next)

        twiss0 = getattr(module, "twiss0")
        twiss_end = calc_twiss(MagneticLattice(module.cell), tws0=twiss0)[-1]  # type: ignore
        twiss_next = getattr(module_next, "twiss0")

        # Increase the absolute tolerance for checking small
        # dispersions This is necessary because whereas I could write
        # out all the dispersions strictly as I calculate them during
        # conversion, I don't want to, because I don't want to include
        # sub-micron dispersions, I just want them go be treated as 0.
        # But this then also means that when I calculate the
        # dispersions here to make sure everything is consistemt, it
        # will always be slightly inconsisted for very small
        # dispersions.  So I correct that here by increasing the
        # absolute tolerance.  I only need to do this forthe
        # dispersions, though, as they're the only parameters here
        # that can be 0 or close to 0.
        atol_dispersion = 10 * PythonSubsequenceWriter.ABS_TOL_FOR_DEFAULT_BEAM_PARAMETERS
        atol = 1e-10

        assert twiss_end.E == twiss_next.E
        # I have to insert this because for different python versions
        # this may not be exactly equal.  Not sure why, but tolerance
        # is tiny anyway so it's fine to just get the tests to pass.
        assert twiss_end.beta_x == pytest.approx(twiss_next.beta_x, abs=atol)
        assert twiss_end.beta_y == pytest.approx(twiss_next.beta_y, abs=atol)
        assert twiss_end.alpha_x == pytest.approx(twiss_next.alpha_x, abs=atol)
        assert twiss_end.alpha_y == pytest.approx(twiss_next.alpha_y, abs=atol)
        assert twiss_end.Dx == pytest.approx(twiss_next.Dx, abs=atol_dispersion)
        assert twiss_end.Dy == pytest.approx(twiss_next.Dy, abs=atol_dispersion)
        assert twiss_end.Dxp == pytest.approx(twiss_next.Dxp, abs=atol_dispersion)
        assert twiss_end.Dyp == pytest.approx(twiss_next.Dyp, abs=atol_dispersion)
        assert twiss_end.s == twiss_next.s
