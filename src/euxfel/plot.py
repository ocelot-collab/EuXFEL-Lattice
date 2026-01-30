import latdraw
import matplotlib.pyplot as plt
import polars as pl
from latdraw.interfaces import lattice_from_ocelot
from latdraw.lattice import Beamline
from latdraw.plot import subplots_with_lattices
from ocelot.cpbd.magnetic_lattice import MagneticLattice
from ocelot.cpbd.track import twiss

from euxfel.complist import ComponentList
from euxfel.complist_draw import draw_to_target

from . import complist_draw, sequences
from .complist import ComponentList

from latdraw.plot import s_label


def plot_cathode_to_target(target: str) -> tuple[pl.DataFrame, MagneticLattice, plt.Figure]:
    sequence = getattr(sequences, f"cathode_to_{target.lower()}")
    twiss0 = sequences.CATHODE_TWISS0

    mlat = MagneticLattice(sequence)
    optics_df = twiss(mlat, tws0=twiss0, return_df=True)
    optics_df = pl.from_pandas(optics_df)

    title = f"Cathode to {target.upper()} Optics"

    fig, (_, ax1, ax2, ax3) = latdraw.plot.three_axes_figure(
        sequence, title=title
    )

    ax1.plot(optics_df["s"], optics_df["beta_x"], label=r"$\beta_x$")
    ax1.plot(optics_df["s"], optics_df["beta_y"], label=r"$\beta_y$")

    ax2.plot(optics_df["s"], optics_df["Dx"], label="$D_x$")
    ax2.plot(optics_df["s"], optics_df["Dy"], label="$D_y$")

    ax1.legend()
    ax2.legend()

    ax3.plot(optics_df["s"], optics_df["E"])

    ax1.set_ylabel(r"$\beta$ / m")
    ax2.set_ylabel("$D$ / m")
    ax3.set_ylabel("$E$ / GeV")

    ax1.set_ylim(0, optics_df["beta_x"].median() * 10)

    return twiss, mlat, fig


def compare_cathode_to_target(target: str, complist: ComponentList) -> tuple[pl.DataFrame, MagneticLattice, plt.Figure]:
    sequence = getattr(sequences, f"cathode_to_{target}")
    twiss0 = sequences.CATHODE_TWISS0

    target = target.upper()

    mlat = MagneticLattice(sequence)

    title = f"Cathode to {target} Optics"

    optics_df = twiss(mlat, tws0=twiss0, return_df=True)
    optics_df = pl.from_pandas(optics_df)

    fig, (mx1, mx2, ax1, ax2, ax3) = subplots_with_lattices(
        [Beamline([]), lattice_from_ocelot(sequence), None, None, None]
    )
    draw_to_target(mx1, complist, f"I1to{target}")
    mx1.spines["left"].set_visible(False)
    mx1.spines["right"].set_visible(False)
    mx1.set_yticks([], [])
    mx1.set_title(title)
    mx1.set_ylabel("Comp. List", fontsize=8)
    mx2.set_ylabel("OCELOT", fontsize=8)
    mx1.sharey(mx2)

    ll = complist
    lldf = ll.get_sheet(f"I1to{target}")

    l1, = ax1.plot(lldf["S"], lldf["BETX"], label=r"$x$, Long List",linestyle="--")
    ax1.plot(optics_df["s"], optics_df["beta_x"],  color=l1.get_color(), label=r"$x$, OCELOT")

    l1, = ax1.plot(lldf["S"], lldf["BETY"], label=r"$y$, Long List", linestyle="--")
    ax1.plot(optics_df["s"], optics_df["beta_y"], label=r"$y$, OCELOT", color=l1.get_color())

    l1, = ax2.plot(lldf["S"], lldf["DX"], # label=r"$D_x$, Long List",
              linestyle="--")
    ax2.plot(optics_df["s"], optics_df["Dx"],# , label="$D_x$, OCELOT"
                   color=l1.get_color())
    l1, = ax2.plot(lldf["S"], lldf["DY"], # label=r"$D_y$, Long List",
              linestyle="--")
    ax2.plot(optics_df["s"], optics_df["Dy"],# , label="$D_y$, OCELOT"
                   color=l1.get_color())

    ax1.legend(ncol=2)
    # ax2.legend(ncol=2)

    l1, = ax3.plot(lldf["S"], lldf["ENERGY"], label="Long List", linestyle="--")
    ax3.plot(optics_df["s"], optics_df["E"], label="OCELOT", color=l1.get_color())

    ax3.legend()

    ax1.set_ylabel(r"$\beta$ / m")
    ax2.set_ylabel("$D$ / m")
    ax3.set_ylabel("$E$ / GeV")

    # A little something to try to stop the huge betas in the dumps
    # ruining the plot.
    ax1.set_ylim(0, optics_df["beta_x"].median() * 10)

    s_label(ax3)

    return optics_df, mlat, fig
