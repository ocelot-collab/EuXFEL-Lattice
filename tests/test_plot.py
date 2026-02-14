import pytest

from euxfel.plot import compare_cathode_to_target, plot_cathode_to_target
from euxfel.sequences import TARGET_NAMES


@pytest.fixture
def component_list():
    pass


@pytest.mark.parametrize("target_name", TARGET_NAMES)
def test_plot_cathode_to_target_doesnt_crash_for_all_targets(target_name: str) -> None:
    plot_cathode_to_target(target_name)


# @pytest.mark.slow
# @pytest.mark.parametrize("target_name", TARGET_NAMES)
# def test_compare_cathode_to_target_doesnt_crash_for_all_targets(target_name: str) -> None:
#     compare_cathode_to_target(target_name)
