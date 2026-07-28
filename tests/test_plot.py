import pytest

from euxfel.plot import plot_cathode_to_target
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


def test_subplots_with_lattices_matches_compare_layout() -> None:
    """The compare-only surface that test_plot_cathode_to_target misses.

    `compare_cathode_to_target` asks for five axes with an empty `Beamline` in
    the first slot -- the strip that `complist_draw.draw_to_target` then fills
    from the component list.  Needs no spreadsheet, so it stays fast.
    """
    from euxfel.complist_draw import DEFAULT_COLOUR_MAP, MAGNET_WIDTH  # noqa: F401
    from euxfel.latdraw.convert import from_ocelot
    from euxfel.latdraw.lattice import Beamline
    from euxfel.latdraw.plot import subplots_with_lattices
    from euxfel.sequences import cathode_to_i1d

    fig, axes = subplots_with_lattices(
        [Beamline([]), from_ocelot(cathode_to_i1d), None, None, None]
    )
    assert len(axes) == 5


@pytest.mark.parametrize("name", ["t1", "tl2tld"])
def test_plot_subsequence_flattens_sliced_elements(name: str) -> None:
    """t1 and tl2tld each embed a 200-element list from an XY-quad SlicedElement."""
    from euxfel.plot import plot_subsequence

    plot_subsequence(name)


def test_draw_survey_runs() -> None:
    """Guards the NameError fix: this raised for every element in latdraw 0.3.1.

    Upstream referenced an unbound `element` where the loop variable is `row`,
    and a NameError is not caught by the enclosing `except AttributeError`.
    """
    import matplotlib.pyplot as plt

    from euxfel import subsequences
    from euxfel.latdraw.convert import from_ocelot
    from euxfel.latdraw.draw import draw_survey

    beamline = from_ocelot(subsequences.b1d.cell)
    _, ax = plt.subplots()
    draw_survey(plt.gcf(), ax, beamline)
    assert len(ax.patches) == len(beamline)
