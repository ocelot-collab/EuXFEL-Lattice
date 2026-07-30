import matplotlib.pyplot as plt
import polars as pl
from ocelot.cpbd.magnetic_lattice import MagneticLattice
from ocelot.cpbd.track import twiss

from euxfel import pand8, subsequences
from euxfel.complist import ComponentList
from euxfel.complist_draw import draw_to_target
from euxfel.latdraw.convert import from_ocelot
from euxfel.mad8 import twiss_tape
from euxfel.latdraw.lattice import Beamline
from euxfel.latdraw.plot import (
    beta_label,
    s_label,
    subplots_with_lattices,
    three_axes_figure,
)

from . import sequences


def plot_cathode_to_target(
    target: str,
) -> tuple[pl.DataFrame, MagneticLattice, plt.Figure]:
    sequence = getattr(sequences, f"cathode_to_{target.lower()}")
    twiss0 = sequences.CATHODE_TWISS0

    mlat = MagneticLattice(sequence)
    optics_df = twiss(mlat, tws0=twiss0, return_df=True)
    optics_df = pl.from_pandas(optics_df)

    title = f"Cathode to {target.upper()} Optics"

    fig, (_, ax1, ax2, ax3) = three_axes_figure(sequence, title=title)

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


def _mad8_optics(target: str) -> pl.DataFrame | None:
    """MAD-8's own optics for a target, or None if no tape is archived.

    `MUX`/`MUY` are in units of 2*pi on the tape, matching the component list;
    `SUML` is the same arc length Ocelot and the list both use, so all three
    series share an abscissa without any rescaling.
    """
    try:
        path = twiss_tape(target)
    except FileNotFoundError:
        return None
    return pand8.read_twiss(path)


def compare_cathode_to_target(
    target: str, complist: ComponentList, mad8: bool = False
) -> tuple[pl.DataFrame, MagneticLattice, plt.Figure]:
    sequence = getattr(sequences, f"cathode_to_{target}")
    twiss0 = sequences.CATHODE_TWISS0

    target = target.upper()

    mlat = MagneticLattice(sequence)

    title = f"Cathode to {target} Optics"

    optics_df = twiss(mlat, tws0=twiss0, return_df=True)
    optics_df = pl.from_pandas(optics_df)

    fig, (mx1, mx2, ax1, ax2, ax3) = subplots_with_lattices(
        [Beamline([]), from_ocelot(sequence), None, None, None]
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

    (l1,) = ax1.plot(lldf["S"], lldf["BETX"], label=r"$x$, Long List", linestyle="--")
    ax1.plot(
        optics_df["s"], optics_df["beta_x"], color=l1.get_color(), label=r"$x$, OCELOT"
    )

    (l1,) = ax1.plot(lldf["S"], lldf["BETY"], label=r"$y$, Long List", linestyle="--")
    ax1.plot(
        optics_df["s"], optics_df["beta_y"], label=r"$y$, OCELOT", color=l1.get_color()
    )

    (l1,) = ax2.plot(
        lldf["S"],
        lldf["DX"],
        linestyle="--",  # label=r"$D_x$, Long List",
    )
    ax2.plot(
        optics_df["s"],
        optics_df["Dx"],
        color=l1.get_color(),  # , label="$D_x$, OCELOT"
    )
    (l1,) = ax2.plot(
        lldf["S"],
        lldf["DY"],
        linestyle="--",  # label=r"$D_y$, Long List",
    )
    ax2.plot(
        optics_df["s"],
        optics_df["Dy"],
        color=l1.get_color(),  # , label="$D_y$, OCELOT"
    )

    # MAD-8's own optics, the upstream both of the others derive from.  Dotted
    # so it reads as a third opinion rather than competing with the pair above.
    tape = _mad8_optics(target) if mad8 else None
    if tape is not None:
        ax1.plot(tape["SUML"], tape["BETX"], label=r"$x$, MAD-8", linestyle=":",
                 color="k", linewidth=1.3, zorder=10)  # fmt: skip
        ax1.plot(tape["SUML"], tape["BETY"], label=r"$y$, MAD-8", linestyle=":",
                 color="dimgrey", linewidth=1.3, zorder=10)  # fmt: skip
        ax2.plot(
            tape["SUML"], tape["DX"], linestyle=":", color="k", linewidth=1.3, zorder=10
        )
        ax2.plot(tape["SUML"], tape["DY"], linestyle=":", color="dimgrey",
                 linewidth=1.0)  # fmt: skip

    ax1.legend(ncol=2)
    # ax2.legend(ncol=2)

    (l1,) = ax3.plot(lldf["S"], lldf["ENERGY"], label="Long List", linestyle="--")
    ax3.plot(optics_df["s"], optics_df["E"], label="OCELOT", color=l1.get_color())
    if tape is not None:
        ax3.plot(tape["SUML"], tape["E"], label="MAD-8", linestyle=":", color="k",
                 linewidth=1.0)  # fmt: skip

    ax3.legend()

    ax1.set_ylabel(r"$\beta$ / m")
    ax2.set_ylabel("$D$ / m")
    ax3.set_ylabel("$E$ / GeV")

    # A little something to try to stop the huge betas in the dumps
    # ruining the plot.
    ax1.set_ylim(0, optics_df["beta_x"].median() * 10)

    s_label(ax3)

    return optics_df, mlat, fig


def plot_subsequence(name: str) -> plt.Figure:
    module = getattr(subsequences, name)
    sequence = module.cell
    twiss0 = module.twiss0

    mlat = MagneticLattice(sequence)  # type: ignore
    optics_df = twiss(mlat, tws0=twiss0, return_df=True)
    optics_df = pl.from_pandas(optics_df)  # type: ignore

    fig, (mx, ax1, ax2, ax3) = subplots_with_lattices(
        [from_ocelot(sequence), None, None, None], s_offset=twiss0.s
    )

    ax1.plot(optics_df["s"], optics_df["beta_x"], label=r"$x$")
    ax1.plot(optics_df["s"], optics_df["beta_y"], label=r"$y$")

    ax2.plot(optics_df["s"], optics_df["Dx"])
    ax2.plot(optics_df["s"], optics_df["Dy"])

    ax1.legend()

    ax3.plot(optics_df["s"], optics_df["E"])

    mx.set_title(name.upper())
    ax1.set_ylabel(r"$\beta$ / m")
    ax2.set_ylabel("$D$ / m")
    ax3.set_ylabel("$E$ / GeV")
    beta_label(ax1)
    s_label(ax3)

    return fig
