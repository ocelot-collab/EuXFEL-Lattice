![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Focelot-collab%2FEuXFEL-Lattice%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&style=flat&logo=python)
[![Static Badge](https://img.shields.io/badge/10.1103%2FPhysRevAccelBeams.22.024401-purple?label=PRAB&link=https%3A%2F%2Fdoi.org%2F10.1103%2FPhysRevAccelBeams.22.024401)](https://doi.org/10.1103/PhysRevAccelBeams.22.024401)
[![Static Badge](https://img.shields.io/badge/10.18429%2FJACoW--IPAC2017--WEPAB031-purple?label=IPAC&link=https%3A%2F%2Fdoi.org%2F10.18429%2FJACoW-IPAC2017-WEPAB031)](https://doi.org/10.18429/JACoW-IPAC2017-WEPAB031)


# EuXFEL-Lattice
Unofficial Ocelot EuXFEL lattice repository. Created by Bianca,  Sergey and Stuart.

This is the repository for the EuXFEL ocelot repository.  The idea
 behind it is to have one transparent model that everyone uses, everyone can 
 contribute to, and in turn everyone can benefit from.

Currently the OCELOT Python EuXFEL sequences are generated from the
"Component List", an Excel spreadsheet generated internally by the
group leader as the "single source of truth" for what actually is in
the tunnel.  These files can be found [here](https://xfel.desy.de/operation/component_list/).

## Repository structure
* src/euxfel - the main Python package for the Ocelot lattices and so on.  See below for more detailed explanation of the contents.
  For a deeper explanation of the package's layout, see [here](#the-layout-of-srceuxfel).
* beam_files - particle distributions
  * gun - initial beam distribution from gun (3.2 m position)
  * gun_2019 - initial beam distribution used in the settings https://www.desy.de/fel-beam/s2e/xfel/Nominal/nom250pC.html used for the 2019 simulation studies published in [this article](https://www.sciencedirect.com/science/article/abs/pii/S0168900221000954)
* Astra_gun_simulation/250pC_phi42 - by downloading the Astra executables from the official page https://www.desy.de/~mpyflo/ and adjusting the parameters in generator.in first (the laser pulse length sig_clock) and in the rfgun.in file later (phi(1)), it is possible to simulate the particle distribution from the gun till the position specified in the ZSTOP parameter. The current setting was developed by Igor Zagorodnov for 250pC. The radial_smear.m is a Matlab script for smoothing the profile obtain by the generator
* s2e_scripts - example scripts for running a start to end simulation from 3.2m to anywhere in the machine.
* tests - tests for the euxfel package.
* utils - beam matching script

## Getting started

Clone the repository and install the package.

```
$ cd EuXFEL-Lattice
pip install .
```

### Command Line Interface

Some key functionality can then be accessed from the command line:

```bash
$ euxfel convert  # Regenerate the Python subsequences
$ euxfel compare  # Compare the OCELOT optics for all the paths through the machine with the Component List.
$ euxfel compare  # Just compare for I1D.
$ euxfel plot     # Plot all OCELOT optics
$ euxfel plot b1d # Just plot for B1D
```

For example, `$ euxfel compare b1d` gives the following image and prints the following two tables to the terminal:

<img width="2696" height="1702" alt="Bildschirmfoto 2026-01-19 um 15 33 06" src="https://github.com/user-attachments/assets/716a1569-5474-453d-bb6a-8be9f18fe7e3" />

<img width="2082" height="778" alt="Bildschirmfoto 2026-01-19 um 15 38 05" src="https://github.com/user-attachments/assets/6820d3e5-bc47-49ad-a314-a0de44e0ed34" />

### Optics in Plain Python

You can of course use the euxfel package in Python as a normal library, for example to access the sequence from the cathode to I1D in Python:

```python
import euxfel.sequences as sequences
from ocelot import *
from ocelot.gui.accelerator import *
import matplotlib.pyplot as plt
twiss0 = sequences.CATHODE_TWISS0
mlat_i1d = MagneticLattice(sequences.cathode_to_i1d)
machine_twiss = twiss(mlat_i1d, twiss0)
# Example of use with plain OCELOT:
plot_opt_func(mlat_i1d, machine_twiss)
plt.show()
```
In addition to `sequences.cathode_to_i1d`, there is also a `squences.cathode_to_` attribute for `b1d`, `b2d`, `tld`, `t4d` and `t5d`.

### Full Start to End Simulations

Look in the top-level directory `s2e_scripts` for examples of start to end simulation scripts from 3.2m to various targets downstream.

## How to Run the Conversion Now

Clone the repository and install the Python package.  Put the
component list you want to convert in `src/euxfel/longlists`, or use
one that is already there.  The converter will look for a file called
`conversion-config.yaml` to drive the entire conversion process.
Either use the existing one, make a new one, or make a symlink with
the name `conversion-config.yaml` that points to one of the
explicitly named (i.e. dated) yaml files. Look at one of the other conversion
yaml files for guidance on how to write your own for a given component list. 
Further details on the makeup of these conversion-config.yaml files is
follows [here](#conversion-configuration).

```bash
$ euxfel convert
```

This will run, and the output will automatically be written to
`src/euxfel/subsequences/`.


## Changing OCELOT Lattice Versions

If you want to use a different version of the lattice, then the
easiest way is to check out a different tagged release.
Always use the latest version for a given model type:

To use v0.2 (at the time of writing the latest version) of the July 2024 model:

```
$ git checkout 0.2.0+componentlist.20240704
```

To use v0.2 of the January 2026 model:

```
$ git checkout 0.2.0+componentlist.20260121
```

API changes should be separate from lattice versions and the two packages
should be functionally identical except for the lattice files.


## Conversion Configuration

The conversion should be as transparent as possible, and absolutely no
hand edits of the output Python modules should be necessary.  To this
end, the configuration is fully described in the file
conversion-config.yaml.  I'll try to explain some of the sections of
this config file here.

The filename is chosen as:

```
component_list: component_list_2026.01.21.xls
```

### Writer

Configure the writing of the output Python files with the `writer`
heading.  Currently the only setting is `writer_types_power_supplies`
with which you can configure which element types have their power
supply IDs written.

```
writer:
  write_types_power_supplies: ["Quadrupole", "Sextupole", "Octupole", "Cavity", "RBend", "SBend"]
```

### Rows

Row based edits with `rows` header.  Subheaders include `skip` for
skipping certain elements altogether based on TYPE, CLASS, GROUP and
NAME1 from the component list.  `edit` provides for a crude update to
the component list row dictionary immediately prior to generating the
OCELOT component.  The below skips all of the listed `TYPE`, `CLASS`
and `GROUP`, as well as setting all "CAX", "CAY", "CBX" and "CBY"
lengths to zero (these are the aircoils, which in pairs are directly
on top of each other in the component list, yet with non-zero length,
which is not permitted).


```
rows:
  skip:
    TYPE: ["BENDMARK", "RF", "CTBI", "CUX"]
    CLASS: ["CRYO", "UNDPLACEH"]
    GROUP: ["CRYO",
            "VACUUM",
            "MOVER",
            "PHOTON",
            "DUMP"]
    NAME1: []

  edit:
    TYPE:
      CAX: { LENGTH: 0.0 }
      CAY: { LENGTH: 0.0 }
      CBX: { LENGTH: 0.0 }
      CBY: { LENGTH: 0.0 }
    CLASS: {}
    GROUP: {}
```

### Sections

With `sections` header the modules themselves are defined.  The basic
definition requires a name, for example I1D (which would then become
i1d.py), a sheet name from the Component List to use (not LONGLIST, in
order to ensure the correct extraction are powered for each path
through the machine), and two *marker* names from the Component List,
one for start and one for stop.

#### New Markers

For the effective inclusion of physics processes, it's necessary to
introduce additional markers.  For example, the OCELOT simulation
starts at 3.2m after the cathode, but there is no marker at this point
in the component list.  These can all be added with the `new_markers`
section.  For example, in I1:

```yaml
sections:
  I1:
    [...]
    new_markers:
      stop_astra: { s: 3.2 }
      start_ocelot: { s: 3.2 }
      lh_start: { reference: U74.49.I1, adjacent: before }
      lh_stop: { reference: U74.49.I1, adjacent: after }
      DUMP.CSR.START: { s: 38.789005 }
```

This introduces two markers at 3.2m and one at 38.789m (just befor the
I1D dump dipole).

⚠️ **Warning:**: It is up to the user to ensure that these inserted markers are not placed inside of
other elements!  There is no checking done on this and it may fail cryptically.

Additionaly, the laser heater undulator `U74.49.I1` is wrapped with
two markers, one immediately `before` and one immediately `after` in
order to attach the laser heater process correctly.

#### Additional Element Properties


In I1D it is necessary to introduce two additional element properties
which are missing in the component list.  Firstly, the TDS must be
rotated by 90 degrees, and the undulator must be closed.  This is done
with the `extras` section of the section definition:

```yaml
sections:
  I1:
    [...]
    extras:
      TDSA.52.I1:
        tilt: 1.570796327
      U74.49.I1:
        Kx: 1.294
        Ky: 0
```

#### Rematching at Conversion Time


Finally, due to the focusing from the undulator, when the undulator is
closed, the matching from the cathode will now be wrong.  We need to
rematch whilst converting to calculate the correct quadrupole
strengths.  The snippet below states to rematch at the given market
with respect to the reference optics, using hte listed quadrupoles.

```yaml
sections:
  I1:
    [...]
    matching:
      marker: MATCH.52.I1
      quadrupoles:
        - Q.37.I1
        - Q.38.I1
        - QI.46.I1
        - QI.47.I1
        - QI.50.I1
```

#### Inserting Additional Elements

The so-called XY-quadrupoles are not in the component list, but they
are needed in order to get the correct optics.  For example for the TL
section, the XY-quadrupole is approximated with 190 slices of a
horizontal combined function magnet and 10 slices of a vertical
combined function magnet, interleaved with each other.  The position
is set with reference to the previous dipole, set to start 0.4724m
past the *end* of BZ.1980.TLD.

```
sections:
  [...]
  Tl2TLD:
    [...]
    new_elements:
      QK.1982.TL:
        position: { reference: MBZ.1980d.TLD, s: 0.4724 }
        type: SlicedElement
        expression: "(19 * [xslice1982] + [yslice1982]) * 10"
        elements:
          xslice1982:
            type: RBend
            l: 0.005276
            angle: 1.180477777265855e-05
            k1: 0.090359600075815
          yslice1982:
            type: RBend
            l: 0.005276
            angle: -7.780804909999998e-05
            k1: -0.090359600075815
            tilt: 1.570796327
```

⚠️ **Warning:** the named refrence element *must* have no other elements between it and the
newly inserted element.  Otherwise it will most likely fail and it will fail mysteriously, most
likely with cryptic complains about negative drift lengths!  I never added special checks on this.

Currently no other element types besides the `SlicedElement` may be
inserted into the lattice at conversion time.


## The Layout of src/euxfel

```
src
└── euxfel
    ├── __init__.py
    ├── cli.py              # The command line interface for 
    ├── complist_draw.py    # Draw Component Lists directly onto maptlotlib axes
    ├── complist.py         # Load Component Lists
    ├── conversion.py       # Convert component lists to OCELOT
    ├── longlists           # Contains longlists and conversion configs for each one.
    │   │                   # `conversion-config.yaml` is a symlink pointing to the one to be used for conversion.
    │   ├── __init__.py
    │   ├── component_list_2024.07.04.xls
    │   ├── component_list_2026.01.21.xls
    │   ├── conversion-config-2024.07.04.yaml
    │   ├── conversion-config-2026.01.21.yaml
    │   └── conversion-config.yaml -> conversion-config-2026.01.21.yaml
    ├── optics.py           # Some utilities for checking optics
    ├── plot.py             # Functions for plotting OCELOT optics and comparing with the Component List
    ├── sections.py         # Set of classes inheriting SectionTrack.  This is where physics processes are added.
    ├── sequences.py        # A set of sequences that 
    ├── slicing.py          # Special class for implementing symbolically sliced elements in ocelot
    ├── subsequences        # All the subsequence Python modules live here.
    │   ├── i1.py
    │   ├── i1d.py
    │   ├── …
    │   └── t4d.py
    ├── wakes               # All the wake files live in this directory
    │   ├── __init__.py
    │   ├── Dechirper
    │   │   ├── __init__.py
    │   │   ├── …
    │   │   └── wake_vert_axis_700um.txt
    │   ├── …
    │   ├── mod_wake_2035.190_2213.000_MONO.dat
    │   ├── RF
    │   │   ├── …
    │   │   └── wake_table_TDS1.dat
    │   └── Undulator
    │       ├── …
    │       └── wake_undulator_OCELOTnew.txt
    └── writer.py            # The custom writer for writing the Python modules out one by one.
```



## Further Comments

######  IMPORTANT ######
In the distribution section two beams (straight and kicked) are going through the same quadrupoles and hence see the different magnetic fields:
          • straight beam only quadrupole component
          • kicked beam - main quadrupole component and additional dipole components.
The model of the magnets for the kicked beams needs to take into account these components.

Specifically, the extraction to T5D and the extraction to TLD lines have offsets on bot horizontal and vertical planes. The magnet needs to be split into N slices: sequence of horizontal and vertical combine function magnets.
More details about the modelling of the magnetic elements for the kicked beams can be found in [ this presentation ](NewModel_T1_TLD_Jan2025.pdf), courtesy of *Nina Golubeva*.


### NOTE:
1. LH undulator.
   - The length of 0.74 m is the iron length.
   - The model of natural focusing has been created using measured field profiles which are longer (0.918 m).

2. Natural focusing
   - In the design optics the natural undulator focusing is not taking into account (drift).
   - To take into account the natural focusing you have
     to set up the beam parameters (energy) and the undulator setup (gap).
     The natural focusing effect (matrices) is then calculated using analytical formulas. One example can be found in the file:
     SET_LHund_closed_130MeV_42mm.txm
   - If the natural focusing is taken into account, it needs to rematch the beam in the injector.

3. Coupler kick in all RF cavities are off.

📚 Citation Notice

If you use the s2e scripts from this repository or any of their derivatives in your work, please cite the following:
1. S. Tomin, I. Agapov, M. Dohlus, and I. Zagorodnov, Ocelot as a framework for beam dynamics simulations of x-ray sources,
in Proceedings of the International Particle Accelerator Conference (IPAC), Copenhagen, Denmark (2017), WEPAB031.
2. I. Zagorodnov, M. Dohlus, and S. Tomin, Accelerator beam dynamics at the European X-ray free-electron laser,
Phys. Rev. Accel. Beams 22, 024401 (2019). https://doi.org/10.1103/PhysRevAccelBeams.22.024401
