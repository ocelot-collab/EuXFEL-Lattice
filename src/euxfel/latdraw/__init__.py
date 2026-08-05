"""Drawing of machine layouts, derived from latdraw 0.3.1.

Vendored from https://github.com/st-walker/latdraw so that `euxfel` carries no
external dependency for its layout strips.  Reduced to the Ocelot-only case:
the MAD-X/elegant/BDSIM input coercion and the optics-file readers are gone,
but both drawing modes -- curvilinear (`draw`) and survey/cartesian
(`draw_survey`) -- are kept in full.

    MIT License, Copyright (c) 2022, Stuart Derek Walker
"""

from .convert import from_ocelot
from .draw import DEFAULT_COLOUR_MAP, MAGNET_WIDTH, draw, draw_line, draw_survey
from .lattice import Lattice
from .plot import (
    alpha_label,
    beta_label,
    dispersion_label,
    energy_label,
    four_axes_figure,
    s_label,
    simple_figure,
    subplots_with_lattice,
    subplots_with_lattices,
    three_axes_figure,
    two_axes_figure,
)

__all__ = [
    "DEFAULT_COLOUR_MAP",
    "MAGNET_WIDTH",
    "Lattice",
    "alpha_label",
    "beta_label",
    "dispersion_label",
    "draw",
    "draw_line",
    "draw_survey",
    "energy_label",
    "four_axes_figure",
    "from_ocelot",
    "s_label",
    "simple_figure",
    "subplots_with_lattice",
    "subplots_with_lattices",
    "three_axes_figure",
    "two_axes_figure",
]
