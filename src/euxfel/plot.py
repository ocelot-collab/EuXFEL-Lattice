from typing import Sequence

import matplotlib.pyplot as plt
import polars as pl
from ocelot.cpbd.beam import Twiss
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


#: The four independent answers to "what are this machine's optics?", and how
#: each is obtained.  They are not interchangeable, and the point of naming them
#: separately is that a disagreement between any two means something specific:
#:
#:   mad8            MAD-8's own TWISS tape.  The upstream authority.
#:   ocelot-mad8     our model built from the MAD-8 tapes, tracked by Ocelot.
#:                   Differs from `mad8` only where Ocelot's physics differs.
#:   longlist        the component list's own optics columns -- MAD-8's numbers
#:                   after `makelist_release.m` has rounded and re-rendered them.
#:   ocelot-longlist our model built from the component list.  Differs from
#:                   `ocelot-mad8` where the spreadsheet lost something.
SOURCES = ("mad8", "ocelot-mad8", "longlist", "ocelot-longlist")

#: Colour and dash per source, held the same across all three panels so a series
#: can be followed between them.
SOURCE_STYLE = {
    "mad8": {"color": "k", "linestyle": ":", "linewidth": 1.4},
    "ocelot-mad8": {"color": "crimson", "linestyle": (0, (5, 2)), "linewidth": 1.2},
    "longlist": {"color": "steelblue", "linestyle": "--", "linewidth": 1.2},
    "ocelot-longlist": {"color": "seagreen", "linestyle": "-", "linewidth": 1.1},
}

#: The vertical series is drawn from the same colour, lightened, so x and y stay
#: distinguishable without doubling the number of colours in the legend.
VERTICAL_ALPHA = 0.55


class UnknownSource(Exception):
    """A source name that is not one of `SOURCES`."""


def resolve_sources(requested: Sequence[str] | None) -> list[str]:
    """Turn user input into an ordered, de-duplicated list of source names.

    `all` expands to everything.  Unambiguous prefixes are accepted, so `mad8`
    and `ocelot-m` both work, but `ocelot` alone is rejected rather than guessed
    at -- there are two Ocelot models and picking one silently is exactly the
    confusion this whole selection mechanism exists to remove.
    """
    if not requested:
        return ["longlist", "ocelot-longlist"]

    chosen: list[str] = []
    for name in requested:
        for part in str(name).replace(",", " ").split():
            part = part.strip().lower()
            if part == "all":
                chosen.extend(SOURCES)
                continue
            matches = [s for s in SOURCES if s == part] or [
                s for s in SOURCES if s.startswith(part)
            ]
            if len(matches) != 1:
                raise UnknownSource(
                    f"{part!r} matches {matches or 'nothing'}; "
                    f"choose from {', '.join(SOURCES)} (or 'all')"
                )
            chosen.append(matches[0])

    return list(dict.fromkeys(chosen))


def _twiss_seed_from_tape(tape: pl.DataFrame) -> Twiss:
    row = tape.row(0, named=True)
    seed = Twiss()
    for column, attribute in (
        ("BETX", "beta_x"), ("ALFX", "alpha_x"), ("BETY", "beta_y"),
        ("ALFY", "alpha_y"), ("DX", "Dx"), ("DPX", "Dxp"),
        ("DY", "Dy"), ("DPY", "Dyp"),
    ):  # fmt: skip
        setattr(seed, attribute, float(row[column]))
    # MAD-8 prints E = 0 on the INITIAL row; take it from the first element.
    seed.E = float(tape.filter(pl.col("E") > 0)["E"][0])
    return seed


def _from_ocelot_twiss(points) -> pl.DataFrame:
    return pl.DataFrame(
        {
            "s": [p.s for p in points],
            "beta_x": [p.beta_x for p in points],
            "beta_y": [p.beta_y for p in points],
            "Dx": [p.Dx for p in points],
            "Dy": [p.Dy for p in points],
            "E": [p.E for p in points],
        }
    )


def optics_for(
    source: str, target: str, complist: ComponentList | None = None
) -> pl.DataFrame | None:
    """One source's optics, in a common schema: s, beta_x, beta_y, Dx, Dy, E.

    Returns None when the source is unavailable for this target -- no archived
    tape, no generated sequence -- so a missing one is left off the plot rather
    than aborting it.
    """
    target = target.upper()

    if source == "mad8":
        try:
            tape = pand8.read_twiss(twiss_tape(target))
        except FileNotFoundError:
            return None
        return tape.select(
            pl.col("SUML").alias("s"),
            pl.col("BETX").alias("beta_x"), pl.col("BETY").alias("beta_y"),
            pl.col("DX").alias("Dx"), pl.col("DY").alias("Dy"), "E",
        )  # fmt: skip

    if source == "ocelot-mad8":
        from euxfel.mad8_import import build_sequence

        try:
            tape = pand8.read_twiss(twiss_tape(target))
        except FileNotFoundError:
            return None
        lattice = MagneticLattice(build_sequence(target))
        return _from_ocelot_twiss(twiss(lattice, tws0=_twiss_seed_from_tape(tape)))

    if source == "longlist":
        if complist is None:
            return None
        sheet = complist.get_sheet(f"I1to{target}")
        return sheet.select(
            pl.col("S").alias("s"),
            pl.col("BETX").alias("beta_x"), pl.col("BETY").alias("beta_y"),
            pl.col("DX").alias("Dx"), pl.col("DY").alias("Dy"),
            pl.col("ENERGY").alias("E"),
        )  # fmt: skip

    if source == "ocelot-longlist":
        sequence = getattr(sequences, f"cathode_to_{target.lower()}", None)
        if sequence is None:
            return None
        lattice = MagneticLattice(sequence)
        return _from_ocelot_twiss(twiss(lattice, tws0=sequences.CATHODE_TWISS0))

    raise UnknownSource(source)


def compare_cathode_to_target(
    target: str,
    complist: ComponentList | None = None,
    sources: Sequence[str] | None = None,
    planes: str = "xy",
) -> tuple[dict[str, pl.DataFrame], MagneticLattice | None, plt.Figure]:
    """Plot the chosen sources' optics against each other.

    `sources` names which of `SOURCES` to draw; the default keeps the historical
    pair.  `planes` restricts to `"x"` or `"y"` -- with four sources on a panel,
    dropping one plane is usually what makes it readable.
    """
    names = resolve_sources(sources)
    target = target.upper()

    data = {}
    for name in names:
        frame = optics_for(name, target, complist)
        if frame is not None:
            data[name] = frame
    if not data:
        raise UnknownSource(f"no sources available for {target}")

    sequence = getattr(sequences, f"cathode_to_{target.lower()}", None)
    lattice = MagneticLattice(sequence) if sequence is not None else None

    top = [Beamline([]), from_ocelot(sequence) if sequence else Beamline([])]
    fig, (mx1, mx2, ax1, ax2, ax3) = subplots_with_lattices([*top, None, None, None])
    if complist is not None:
        draw_to_target(mx1, complist, f"I1to{target}")
    for spine in ("left", "right"):
        mx1.spines[spine].set_visible(False)
    mx1.set_yticks([], [])
    mx1.set_title(f"Cathode to {target} Optics")
    mx1.set_ylabel("Comp. List", fontsize=8)
    mx2.set_ylabel("OCELOT", fontsize=8)
    mx1.sharey(mx2)

    show_x, show_y = "x" in planes, "y" in planes
    for name, frame in data.items():
        style = SOURCE_STYLE[name]
        if show_x:
            ax1.plot(frame["s"], frame["beta_x"], label=f"$x$, {name}", **style)
            ax2.plot(frame["s"], frame["Dx"], **style)
        if show_y:
            faded = dict(style, alpha=VERTICAL_ALPHA)
            ax1.plot(frame["s"], frame["beta_y"], label=f"$y$, {name}", **faded)
            ax2.plot(frame["s"], frame["Dy"], **faded)
        ax3.plot(frame["s"], frame["E"], label=name, **style)

    ax1.legend(ncol=2, fontsize=8)
    ax3.legend(fontsize=8)

    ax1.set_ylabel(r"$\beta$ / m")
    ax2.set_ylabel("$D$ / m")
    ax3.set_ylabel("$E$ / GeV")

    # Keep the huge betas in the dumps from flattening everything upstream.
    reference = next(iter(data.values()))
    ax1.set_ylim(0, float(reference["beta_x"].median()) * 10)

    s_label(ax3)
    return data, lattice, fig


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
