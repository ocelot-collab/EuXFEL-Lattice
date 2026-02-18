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
from euxfel.optics import print_optics_at_points, print_surveyed_match_points
from euxfel.plot import (
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


@main.command(help="Check the OCELOT optics against the Component List")
@argument("targets", nargs=-1)
@click.option(
    "--marker",
    multiple=True,
    help="One or more marker strings",
)
def compare(targets, marker):
    clist = ComponentList(str(USED_COMPONENT_LIST))
    selected_targets = targets or reversed(TARGET_NAMES)
    for target in selected_targets:
        print(f"Target: {target}")
        twiss, mlat, fig = compare_cathode_to_target(target.lower(), clist)
        fig.suptitle(USED_COMPONENT_LIST.name)
        print("Optics:")
        print_optics_at_points(twiss, markers=list(marker))
        print("Marker Positions:")
        print_surveyed_match_points(mlat, markers=list(marker))

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
