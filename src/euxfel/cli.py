import pathlib
import pickle
import tomllib
from importlib.resources import files
from euxfel.complist_draw import draw_to_target

import click
import latdraw
import matplotlib.pyplot as plt
from click import Path, argument, echo, group, option
from ocelot.cpbd.magnetic_lattice import MagneticLattice

from euxfel.complist import (
    DEFAULT_COMPONENT_LIST_INDEX,
    ComponentList,
    get_component_list_paths,
    get_default_component_list_path,
    select_xls_file
)
from euxfel.sequences import TARGET_NAMES
from euxfel.conversion import (
    longlist_to_ocelot,
)
from euxfel.conversion import DEFAULT_CONVERSION_CONFIG_PATH
from euxfel.optics import print_match_point_optics, print_surveyed_match_points
from euxfel.plot import compare_cathode_to_target, plot_cathode_to_target


@click.group()
def main():
    """Main entrypoint."""
    name = "oxfel"
    echo(name)
    echo("=" * len(name))
    echo("Build OCELOT models from longlists")

@main.command()
@click.option("--list", is_flag=True, help="Show the long list.")
# @main.option("--list")
def longlists(list):
    if list:
        for i, path in enumerate(get_component_list_paths()):
            if i == DEFAULT_COMPONENT_LIST_INDEX:
                print(f"({i}, default) {path}")
            else:
                print(f"({i}) {path}")

@main.command()
@option("--longlist", help="index or filename")
@option("--in-place", is_flag=True, default=True)
@option("--outdir")
@option("--config")
# @argument("longlist", nargs=1, type=Path(exists=True, dir_okay=False))
def convert(in_place, outdir, longlist, config):
    """Convert longlist to a set of ocelot files"""
    if not outdir:
        outdir = files("euxfel.subsequences")

    if not config:
        config = DEFAULT_CONVERSION_CONFIG_PATH

    
    # longlist_to_ocelot(get_default_component_list_path(), config, outdir)
    longlist_to_ocelot(select_xls_file(), config, outdir)


@main.command()
@option("--optics", is_flag=True, default=True)
@option("--tracking", is_flag=False)
@option("--compare", is_flag=True)
@argument("targets", nargs=-1)
def check(optics, tracking, targets, compare):
    clist = ComponentList(get_default_component_list_path())
    selected_targets = targets or reversed(TARGET_NAMES)
    for target in selected_targets:
        print(f"Target: {target}")
        twiss, mlat, _ = compare_cathode_to_target(target.lower(), clist)
        print("Optics:")
        print_match_point_optics(twiss)
        print("Marker Positions:")
        print_surveyed_match_points(mlat)

    plt.show()


# @main.command()
# def match():
#     match_real_injector()


@main.command()
@argument("target", nargs=1)
def plot(target):
    twiss, _, _ = plot_cathode_to_target(target)
    # print_match_point_analysis(twiss)

    plt.show()


# @main.command()
# @argument("target", nargs=1)
# def lattice(target):
#     fig = compare_ocelot_lattice_component_list(target)


# @main.command()
# def sizes():
#     parray032 = load_reference_0320_10k_distribution()
#     for model_name, model in all_models(model_type="tracking").items():
#         destination = model_name.split("cat_to_")
#         print(f"Generating beam size data for {model_name}")
#         update_bunch_size_data(destination, model, parray032)


if __name__ == "__main__":
    main()  # pragma: no cover, pylint: disable=no-value-for-parameter
