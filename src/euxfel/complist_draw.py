import matplotlib.patches as patches
import polars as pl
from latdraw.latdraw import DEFAULT_COLOUR_MAP, MAGNET_WIDTH
from matplotlib.axes import Axes

from .complist import ComponentList


def draw_to_target(ax: Axes, clist: ComponentList, sheet_name: str) -> None:
    """
    Draw components from the given sheet onto the provided Axes.

    Assumes the following globals are available:
      - MAGNET_WIDTH: float
      - DEFAULT_COLOUR_MAP: dict-like mapping of component names to colours

    The function expects `clist.get_sheet(sheet_name=...)` to return a polars.DataFrame
    with columns including: "S", "LENGTH", "CLASS", "TYPE", "STRENGTH".
    """
    target_df: pl.DataFrame = clist.get_sheet(sheet_name=sheet_name)

    # Determine plotting extent and draw the baseline
    last_row = target_df[-1]
    s_end = last_row["S"].item() + last_row["LENGTH"].item() / 2
    ax.set_prop_cycle(None)  # reset cycle just in case, so that the
    # line always has the same colour.
    ax.plot([0, s_end], [0, 0])

    def _rect_params_from_row(
        row: dict,
    ) -> tuple[float, float, float, float, str, float] | None:
        """Return (start_z, start_x, length, width, colour, alpha) for a row dict."""
        length = row["LENGTH"]
        if not length:
            return None

        element_class = row.get("CLASS", "")
        element_type = row.get("TYPE", "")
        mid_z = row["S"]
        half_length = length / 2.0
        start_z = mid_z - half_length

        # Base rectangle parameters
        width = 4 * MAGNET_WIDTH
        start_x = -2 * MAGNET_WIDTH
        kick = row.get("STRENGTH", 0.0)

        # Transparency: weak/zero-strength elements are semi-transparent
        alpha = 0.25 if kick == 0 else 1.0

        # Default colour (if not matched, return None to skip)
        colour = None

        # Handle specific classes/types
        if element_class == "QUAD":
            colour = DEFAULT_COLOUR_MAP["Quadrupole"]
            width = width / 2.0
            if kick > 0:
                start_x = 0.0
            elif kick < 0:
                start_x = -width
            else:
                start_x = -width / 2.0

        elif element_class in ("SBEN", "RBEN"):
            colour = DEFAULT_COLOUR_MAP["SBend"]

        elif element_class in ("VKIC", "HKIC"):
            colour = DEFAULT_COLOUR_MAP["HKicker"]
            width = width / 2.0
            start_x = -width / 2.0

        elif element_class == "SEXT":
            colour = DEFAULT_COLOUR_MAP["Sextupole"]

        elif element_class == "OCTU":
            colour = DEFAULT_COLOUR_MAP["Octupole"]

        elif element_type.startswith("TDS"):
            colour = DEFAULT_COLOUR_MAP["TransverseDeflectingCavity"]

        elif element_class == "LCAV":
            colour = DEFAULT_COLOUR_MAP["Cavity"]

        elif element_class == "UNDULATOR":
            colour = DEFAULT_COLOUR_MAP["Undulator"]

        else:
            # Unhandled element: don't draw
            return None

        return start_z, start_x, length, width, colour, alpha

    # Iterate rows and add rectangles to the axes
    for row in target_df.iter_rows(named=True):
        params = _rect_params_from_row(row)
        if params is None:
            continue
        start_z, start_x, length, width, colour, alpha = params

        rectx = patches.Rectangle(
            (start_z, start_x),
            length,
            width,
            linewidth=0.1,
            edgecolor="white",
            facecolor=colour,
            alpha=alpha,
        )
        ax.add_patch(rectx)

    # Keep a small vertical range around the beamline
    ax.set_ylim(-0.25, 0.25)
