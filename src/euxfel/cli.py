import pathlib
import pickle
import tomllib
from importlib.resources import files
from euxfel.complist_draw import draw_to_target
from euxfel.subsequences import USED_COMPONENT_LIST

import click
import latdraw
import matplotlib.pyplot as plt
from click import Path, argument, echo, group, option
from ocelot.cpbd.magnetic_lattice import MagneticLattice

from euxfel.complist import (
    ComponentList,
)
from euxfel.sequences import TARGET_NAMES
from euxfel.conversion import (
    longlist_to_ocelot,
)
from euxfel.conversion import DEFAULT_CONVERSION_CONFIG_PATH
from euxfel.optics import print_optics_at_points, print_surveyed_match_points
from euxfel.plot import compare_cathode_to_target, plot_cathode_to_target


@click.group()
def main():
    """Main entrypoint."""
    name = "euxfel"
    echo(name)
    echo("=" * len(name))
    echo("Package for the OCELOT simulations of the EuXFEL")

@main.command(help="Convert Component List files to a set of Python modules")
@option("--outdir", help="Directory in which to write the Python modules")
@option("--config", help="Configuration file for altering the Component List to Python conversion")
def convert(outdir, config):
    if not outdir:
        outdir = files("euxfel.subsequences")

    if not config:
        config = DEFAULT_CONVERSION_CONFIG_PATH

    longlist_to_ocelot(config, outdir)


@main.command(help="Check the OCELOT optics against the Component List")
@argument("targets", nargs=-1)
@click.option(
    "--marker",
    multiple=True,
    help="One or more marker strings",
)
def compare(targets, marker):
    clist = ComponentList(USED_COMPONENT_LIST)
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


@main.command(help="Plot the OCELOT model's optics")
@argument("targets", nargs=-1)
def plot(targets: list[str]):
    selected_targets = targets or reversed(TARGET_NAMES)
    for target in selected_targets:
        plot_cathode_to_target(target)
    plt.show()



if __name__ == "__main__":
    main()  # pragma: no cover, pylint: disable=no-value-for-parameter
