import pathlib
from importlib.metadata import version as md_version
from importlib.resources import files

import click
import matplotlib.pyplot as plt
from click import argument, echo, option

from euxfel import sequences
from euxfel.complist import (
    ComponentList,
)
from euxfel.conversion import (
    DEFAULT_CONVERSION_CONFIG_PATH,
    longlist_to_ocelot,
)
from euxfel.comparison import optics_table, print_table, survey_table
from euxfel.plot import (
    UnknownSource,
    compare_cathode_to_target,
    plot_cathode_to_target,
    plot_subsequence,
)
from euxfel.sequences import TARGET_NAMES
from euxfel.subsequences import USED_COMPONENT_LIST


@click.group()
def main():
    """Command line interface for the euxfel package."""
    pass


@main.command(help="Convert Component List files to a set of Python modules")
@option("--outdir", help="Directory in which to write the Python modules")
@option(
    "--config",
    help="Configuration file for altering the Component List to Python conversion",
)
def convert(outdir, config):
    if not outdir:
        outdir = str(files("euxfel.subsequences"))

    if not config:
        config = DEFAULT_CONVERSION_CONFIG_PATH

    print(f"Using Conversion Config file: {pathlib.Path(config).resolve()}")

    longlist_to_ocelot(config, outdir)


@main.command(
    "convert-mad8",
    help="Build the Python subsequence modules from the MAD-8 SURVEY tapes",
)
@option("--outdir", help="Directory in which to write the Python modules")
def convert_mad8(outdir):
    """The upstream sibling of `convert`.

    `convert` reads the component list, which is itself a lossy render of the
    MAD-8 tapes; this reads the tapes.  Element names are regenerated rather than
    copied -- see `euxfel.mad8_names` -- so the spreadsheet is not consulted at
    all.
    """
    from euxfel.mad8 import config_path
    from euxfel.mad8_convert import mad8_to_ocelot

    if not outdir:
        outdir = str(files("euxfel.subsequences"))

    print(f"Using MAD-8 conversion config: {config_path()}")
    print(f"Writing to: {outdir}")
    mad8_to_ocelot(outdir)


@main.command(help="Check the OCELOT optics against the Component List")
@argument("targets", nargs=-1)
@click.option(
    "--marker",
    multiple=True,
    help="One or more marker strings",
)
@click.option(
    "--show",
    "show",
    multiple=True,
    help=(
        "Which optics to plot; repeat or comma-separate.  One of: "
        "mad8 (MAD-8's own TWISS tape), ocelot-mad8 (our model built from those "
        "tapes), longlist (the Component List's optics columns), "
        "ocelot-longlist (our model built from the Component List), or 'all'.  "
        "Unambiguous prefixes work.  Default: longlist, ocelot-longlist."
    ),
)
@click.option(
    "--plane",
    type=click.Choice(["x", "y", "xy"]),
    default="xy",
    show_default=True,
    help="Restrict to one plane.  With several sources this is usually what "
    "makes the plot readable.",
)
@click.option(
    "--mad8",
    is_flag=True,
    help="Deprecated shorthand for `--show longlist,ocelot-longlist,mad8`.",
)
@click.option(
    "--no-tables",
    is_flag=True,
    help="Plot only; skip the match-point and dump comparison tables.",
)
def compare(targets, marker, show, plane, mad8, no_tables):
    clist = ComponentList(str(USED_COMPONENT_LIST))
    if mad8 and not show:
        show = ("longlist", "ocelot-longlist", "mad8")

    selected_targets = targets or reversed(TARGET_NAMES)
    for target in selected_targets:
        print(f"Target: {target}")
        try:
            data, mlat, fig = compare_cathode_to_target(
                target.lower(), clist, sources=show, planes=plane
            )
        except UnknownSource as error:
            raise click.BadParameter(str(error), param_hint="--show") from None
        fig.suptitle(USED_COMPONENT_LIST.name)
        print(f"Plotted: {', '.join(data)}")

        if not no_tables:
            shown = list(data)
            print_table(
                optics_table(target, shown, clist, markers=list(marker)),
                f"Optics at the match points and the {target.upper()} dump:",
            )
            print_table(
                survey_table(target, shown, clist, markers=list(marker)),
                f"Survey at the match points and the {target.upper()} dump:",
            )

    plt.show()


@main.command(
    help="Plot the OCELOT model's optics from the cathode to one of the dumps."
)
@argument("targets", nargs=-1)
def plot(targets: list[str]):
    selected_targets = targets or reversed(TARGET_NAMES)
    for target in selected_targets:
        plot_cathode_to_target(target)
    plt.show()


@main.command(help="Plot the OCELOT model's optics for one of the subsequences.")
@argument("names", nargs=-1)
@option("--list", "list_", is_flag=True, help="List available subsequences")
def subsequence(names: list[str], list_):
    if list_:
        for target_name in TARGET_NAMES:
            echo(f"{target_name}:")
            for i, subseq_name in enumerate(
                getattr(sequences, f"{target_name}_SUBSEQUENCES"), start=1
            ):
                echo(f"  {i}. {subseq_name}")
        return

    names = names or []
    for name in names:
        plot_subsequence(name)
    plt.show()


@main.command(help="Print the version of the euxfel package and exit")
def version():
    echo(md_version("euxfel"))


if __name__ == "__main__":
    main()  # pragma: no cover, pylint: disable=no-value-for-parameter
