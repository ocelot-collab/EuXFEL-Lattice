import matplotlib.patches as patches

from .complist import ComponentList
# from .conversion import SKIP_GROUP, SKIP_TYPE, SKIP_CLASS
from latdraw.latdraw import DEFAULT_COLOUR_MAP, MAGNET_WIDTH



def draw_to_target(ax, clist: ComponentList, sheet_name: str):
    target_df = clist.get_sheet(sheet_name=sheet_name)

    s_end = target_df[-1]["S"].item() + target_df[-1]["LENGTH"].item() / 2
    ax.set_prop_cycle(None) # Hack..
    ax.plot([0, s_end], [0, 0])

    for row in target_df.iter_rows(named=True):
        if not row["LENGTH"]:
            continue
            

        group = row["GROUP"]
        cls = row["CLASS"]
        type = row["TYPE"]
        mid_z, mid_x = row["S"], 0.0
        half_length = row["LENGTH"] / 2
        start_z = mid_z - half_length
        start_x = mid_x - 2 * MAGNET_WIDTH
        kick = row["STRENGTH"]
        width = 4 * MAGNET_WIDTH

        alpha = 1
        if kick == 0:
            alpha = 0.25
        if cls == "QUAD":
            colour = DEFAULT_COLOUR_MAP["Quadrupole"]
            width /= 2
            if kick > 0:
                start_x = 0
            elif kick < 0:
                start_x = -width
            else:
                start_x = -width / 2



        elif cls in ["SBEN", "RBEN"]:
            colour = DEFAULT_COLOUR_MAP["SBend"]
        elif cls in ["VKIC", "HKIC"]:
            width /= 2
            start_x = -width / 2
            colour = DEFAULT_COLOUR_MAP["HKicker"]
        elif cls in "SEXT":
            colour = DEFAULT_COLOUR_MAP["Sextupole"]
        elif cls in "OCTU":
            colour = DEFAULT_COLOUR_MAP["Octupole"]
        elif type.startswith("TDS"):
            colour = DEFAULT_COLOUR_MAP["TransverseDeflectingCavity"]
        elif cls == "LCAV":
            colour = DEFAULT_COLOUR_MAP["Cavity"]
        elif cls == "UNDULATOR":
            colour = DEFAULT_COLOUR_MAP["Undulator"]
        else:
            continue

        rectx = patches.Rectangle(
            (start_z, start_x),
            row["LENGTH"],
            width,
            linewidth=0.1,
            edgecolor="white",
            facecolor=colour,
            alpha=alpha,
        )

        ax.add_patch(rectx)
    
    ax.set_ylim(-0.25, 0.25)
    
