# Welcome to the EuXFEL Lattice OCELOT Model Documentation


## Installation

Clone the repository and install the package using pip:

```
git clone git@github.com:ocelot-collab/EuXFEL-Lattice.git
cd EuXFEL-Lattice
pip install .
```

Optionally you can install in editable mode:

```bash
pip install --editable .
```

This is necessary if you wish to update the repository model by converting from a component list.


## Command Line Interface

The package comes with a simple command line interface (CLI) for some
basic operations.  The CLI can accessed with the `euxfel` command once
the package has been installed:

```bash
$ euxfel --help
Usage: euxfel [OPTIONS] COMMAND [ARGS]...

  Main entrypoint.

Options:
  --help  Show this message and exit.

Commands:
  compare      Check the OCELOT optics against the Component List
  convert      Convert Component List files to a set of Python modules
  plot         Plot the full optics from the cathode to one of the dumps
  subsequence  Plot the OCELOT model'
```

You are unlikely to need to do any conversions yourself, but it may be
useful to inspect the optics in different parts of the machine.  See

## Start to End Simulations

The scripts for running start-to-end simulations live in `s2e_scripts`. Each
one tracks a distribution from s = 3.2 m after the cathode to a specific point
downstream, at compression settings giving a final peak current of 5-6 kA.

```bash
cd s2e_scripts && python s2e_up_to_SA1_volts.py
```

Which script goes where, how the setpoints reach the lattice, and how to migrate
an older script are covered in
[Start to end simulations](s2e.md).


## Optics

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

How the machine is divided into targets, subsequences and sections, and where
each part of the package lives, is described in [Layout](layout.md).
