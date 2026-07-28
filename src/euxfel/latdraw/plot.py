"""Figures with a machine-layout strip above the plotting axes."""

from typing import Any

import matplotlib.pyplot as plt
import numpy as np

from .convert import _coerce
from .draw import draw
from .lattice import Beamline


def subplots_with_lattice(
    lattice: Beamline | Any | None,
    s_offset: float = 0,
    nrows: int = 1,
    gridspec_kw=None,
    **kwargs,
) -> tuple[plt.Figure, list[plt.Axes]]:
    # Layout strip goes at the top.
    pattern = [lattice]
    pattern.extend(nrows * [None])
    return subplots_with_lattices(pattern, s_offset=s_offset, **kwargs)


def subplots_with_lattices(
    pattern, s_offset: float = 0, **draw_kwargs
) -> tuple[plt.Figure, list[plt.Axes]]:
    pattern = np.array(pattern, dtype=object)

    height_ratios = np.full_like(pattern, 1.0, dtype=float)
    # Get indices of where machines should be plotted
    indices = [index for (index, value) in enumerate(pattern) if value is not None]
    height_ratios[indices] = 0.25

    the_gridspec_kw = {"height_ratios": height_ratios, "hspace": 0.05}

    fig, axes = plt.subplots(
        nrows=len(pattern), sharex=True, gridspec_kw=the_gridspec_kw
    )

    for lattice, ax in zip(pattern, axes):
        if lattice is None:
            continue

        lattice = _coerce(lattice)
        draw(fig, ax, lattice, s_offset=s_offset, **draw_kwargs)

        ax.set_yticks([], [])

        ax.tick_params(
            top=False,
            bottom=False,
            left=False,
            right=False,
            labelleft=False,
            labelbottom=False,
        )

        ax.spines["left"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.set_ylim(-0.25, 0.25)

    return fig, axes


def simple_figure(
    some_beamline, title: str = "", **drawkwargs
) -> tuple[plt.Figure, list[plt.Axes]]:
    bl = _coerce(some_beamline)

    fig, axes = subplots_with_lattice(bl, nrows=1, **drawkwargs)
    s_label(axes[-1])
    axes[0].set_title(title)
    return fig, axes


def two_axes_figure(
    some_beamline, title: str = ""
) -> tuple[plt.Figure, list[plt.Axes]]:
    bl = _coerce(some_beamline)

    fig, axes = subplots_with_lattice(bl, nrows=2)
    s_label(axes[-1])
    axes[0].set_title(title)
    return fig, axes


def three_axes_figure(
    some_beamline, title: str = ""
) -> tuple[plt.Figure, list[plt.Axes]]:
    bl = _coerce(some_beamline)

    fig, axes = subplots_with_lattice(bl, nrows=3)
    s_label(axes[-1])
    axes[0].set_title(title)
    return fig, axes


def four_axes_figure(
    some_beamline, title: str = ""
) -> tuple[plt.Figure, list[plt.Axes]]:
    bl = _coerce(some_beamline)

    fig, axes = subplots_with_lattice(bl, nrows=4)
    s_label(axes[-1])
    axes[0].set_title(title)
    return fig, axes


def beta_label(ax: plt.Axes, subscript: str = "") -> None:
    if not subscript:
        ax.set_ylabel(r"$\beta$ / m")
    else:
        ax.set_ylabel(rf"$\beta_{subscript}$ / m")


def alpha_label(ax: plt.Axes, subscript: str = "") -> None:
    if not subscript:
        ax.set_ylabel(r"$\alpha$ / m")
    else:
        ax.set_ylabel(rf"$\alpha_{subscript}$")


def dispersion_label(ax: plt.Axes, subscript: str = "") -> None:
    if not subscript:
        ax.set_ylabel(r"$D$ / m")
    else:
        ax.set_ylabel(rf"$D_{{{subscript}}}$ / m")


def s_label(ax: plt.Axes) -> None:
    ax.set_xlabel(r"$s$ / m")


def energy_label(ax: plt.Axes, unit: str = "GeV") -> None:
    ax.set_ylabel(f"$E$ / {unit}")
