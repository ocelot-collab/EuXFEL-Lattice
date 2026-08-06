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


@main.group(help="Read, write and apply machine setpoints")
def setpoints():
    pass


def _cell_for(target: str):
    """The sequence to work on.

    ``full`` gives every element of the machine once, which the control-room
    format needs: the EuXFEL branches, so no single cathode-to-dump sequence
    holds all of it (``BG.1.B2D`` is only in the B2D line, for instance).
    """
    from euxfel.volts import all_machine_elements

    if target.lower() == "full":
        return all_machine_elements()
    return getattr(sequences, f"cathode_to_{target.lower()}")


@setpoints.command("apply", help="Apply a setpoints file and show the resulting optics")
@argument("config", type=click.Path(exists=True, dir_okay=False))
@option("--target", default="T4D", help="Which cathode-to-dump sequence to apply to")
@option("--marker", multiple=True, help="Extra markers to report optics at")
@option(
    "--matching",
    is_flag=True,
    help="Also write the matched section, which is otherwise held at design",
)
def setpoints_apply(config, target, marker, matching):
    from ocelot.cpbd.magnetic_lattice import MagneticLattice
    from ocelot.cpbd.track import twiss

    from euxfel.volts import MachineSetpoints

    import polars as pl

    echo(f"Applying {config} to cathode_to_{target.lower()}")
    cell = MachineSetpoints.from_yaml(config).build(
        _cell_for(target), verbose=True, matching=matching
    )
    optics_df = twiss(
        MagneticLattice(cell), tws0=sequences.CATHODE_TWISS0, return_df=True
    )
    # OCELOT returns pandas; the rest of euxfel.optics works in polars.
    print_optics_at_points(pl.from_pandas(optics_df), markers=list(marker))


@setpoints.command(
    "dump", help="Read the setpoints off the lattice and write them as YAML"
)
@option(
    "--target", default="full", help="Sequence to read; 'full' is the whole machine"
)
@option(
    "--from-sascha",
    "from_sascha",
    type=click.Path(exists=True, dir_okay=False),
    help="Apply this control-room file first",
)
@option("-o", "--output", type=click.Path(dir_okay=False), help="Write here")
def setpoints_dump(target, from_sascha, output):
    from euxfel.volts import MachineSetpoints

    cell = _cell_for(target)
    if from_sascha:
        cell = MachineSetpoints.from_sascha(from_sascha, cell).build(cell)

    text = MachineSetpoints.from_lattice(
        cell, name=from_sascha or f"{target} as built"
    ).to_yaml(output)
    if not output:
        echo(text)


@setpoints.command(
    "to-sascha", help="Export a setpoints file to the control-room format"
)
@argument("config", type=click.Path(exists=True, dir_okay=False))
@option("--target", default="full", help="Sequence to use; 'full' is the whole machine")
@option(
    "--like",
    type=click.Path(exists=True, dir_okay=False),
    help="Use this file's key set and order",
)
@option("-o", "--output", type=click.Path(dir_okay=False), help="Write here")
def setpoints_to_sascha(config, target, like, output):
    from euxfel.volts import MachineSetpoints, read_sascha

    keys = list(read_sascha(like)) if like else None
    text = MachineSetpoints.from_yaml(config).to_sascha(
        _cell_for(target), output, keys=keys
    )
    if not output:
        echo(text)


@setpoints.command("diff", help="Compare two sets of setpoints, in either format")
@argument("first", type=click.Path(exists=True, dir_okay=False))
@argument("second", type=click.Path(exists=True, dir_okay=False))
@option("--target", default="full", help="Sequence to use; 'full' is the whole machine")
@option(
    "--rtol", default=1e-9, help="Relative tolerance before a value counts as changed"
)
def setpoints_diff(first, second, target, rtol):
    from euxfel.volts import MachineSetpoints

    cell = _cell_for(target)

    def load(path):
        if str(path).endswith((".yaml", ".yml")):
            return MachineSetpoints.from_yaml(path)
        return MachineSetpoints.from_sascha(path, cell)

    left, right = load(first), load(second)
    before, after = left.resolve(cell), right.resolve(cell)

    rows = []
    for key in sorted(set(before) | set(after)):
        a, b = before.get(key), after.get(key)
        if a is None or b is None:
            rows.append((key, a, b, None))
        elif abs(a - b) > rtol * max(1.0, abs(a)):
            rows.append((key, a, b, (b - a) / a if a else float("inf")))

    if not rows:
        echo("No differences.")
        return

    echo(f"{'supply':<16} {'first':>14} {'second':>14} {'change':>10}")
    for key, a, b, rel in rows:
        fa = "-" if a is None else f"{a:14.6f}"
        fb = "-" if b is None else f"{b:14.6f}"
        fr = "-" if rel is None else f"{rel:9.2%}"
        echo(f"{key:<16} {fa} {fb} {fr:>10}")
    echo(f"\n{len(rows)} of {len(set(before) | set(after))} supplies differ.")


@main.command(help="Print the version of the euxfel package and exit")
def version():
    echo(md_version("euxfel"))


if __name__ == "__main__":
    main()  # pragma: no cover, pylint: disable=no-value-for-parameter
