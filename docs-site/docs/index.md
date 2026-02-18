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

The top-level directory containing all the scripts for running the
start to end simulations is `s2e_scripts`:

```bash
$ cd s2e_scripts
$ ls -1
inj_hires_optics_track.py
injector_hires_optics.py
s2e_up_to_B2D.py
s2e_up_to_I1D_screen.py
s2e_up_to_SA1.py
s2e_up_to_SA2.py
s2e_up_to_SA3.py
s2e_up_to_switchyard_op_values_SASE1_rf_par.py
s2e_up_to_switchyard_op_values_SASE2_rf_par.py
s2e_up_to_switchyard_operational_values.py
s2e_up_to_switchyard.py
```

Each one of these corresponds to a simulation from s = 3.2m after the
cathode to a specific point downstream.  The compression settings used
are standard ones corresponding to a final peak current of (5-6)kA.

Run one of the simulations with

```bash
python s2e_up_to_SA1.py
```


## Optics

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
