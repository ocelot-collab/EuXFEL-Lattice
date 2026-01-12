# EuXFEL-Lattice
Unofficial Ocelot EuXFEL lattice repository. Created by Bianca,  Sergey and Stuart.

This is the repository for the EuXFEL ocelot repository.  The idea
 should be one transparent model that everyone uses and we can all
 contribute to and benefit from.

Currently the OCELOT Python EuXFEL sequences are generated from the
"Component List", an Excel spreadsheet generated internally by the
group leader as the "single source of truth" for what actually is in
the tunnel.  These files can be found here https://xfel.desy.de/operation/component_list/.


Repository structure:
* Lattices - lattice files in ocelot format
  * LL2ocelot - scripts to generate ocelot lattice files from MS Excel LongList
  * longlist_2024_07_04
    * check_optics - comparison scripts for plotting the beta functions and dispersions calculated with Ocelot and read from the longlist (obtained with Mad8)
    * ocelot lattice files for each section of the machine (building up s2e-lines as explained in the list below)
    * readme.txt lists the modifications done to the excel file or to the generated python lattice files in order to accurately model all the elements
* s2e_sections - EuXFEL accelerator section descriptions
* wakes - database of wakefield files (cavities, collimators, dechirpers etc)
* beam_files - particle distributions
  * gun - initial beam distribution from gun (3.2 m position)
  * gun_2019 - initial beam distribution used in the settings https://www.desy.de/fel-beam/s2e/xfel/Nominal/nom250pC.html used for the 2019 simulation studies published in [this article](https://www.sciencedirect.com/science/article/abs/pii/S0168900221000954)
* Astra_gun_simulation/250pC_phi42 - by downloading the Astra executables from the official page https://www.desy.de/~mpyflo/ and adjusting the parameters in generator.in first (the laser pulse length sig_clock) and in the rfgun.in file later (phi(1)), it is possible to simulate the particle distribution from the gun till the position specified in the ZSTOP parameter. The current setting was developed by Igor Zagorodnov for 250pC. The radial_smear.m is a Matlab script for smoothing the profile obtain by the generator
* scripts - s2e main scripts
* utils - beam matching script
* src/euxfel - the location of a new Python package that aims to
  encapsulate all or most of the above and will replace many of these
  features.


## Getting started

Clone the repository and install the package.

```
$ cd EuXFEL-Lattice
pip install .
```

Some key functionality can then be accessed from the command line:

```bash
$ euxfel convert # Regenerate the Python subsequences
$ euxfel compare # Compare the OCELOT optics for all the paths through the machine with the Component List.
$ euxfel plot i1d # Just plot for I1D.
```

Otherwise you can use it in Python, for example to access the sequence from the cathode to I1D in Python

```python
import euxfel.sequences as sequences
from ocelot import *
import matplotlib.pyplot as plt
twiss0 = sequences.CATHODE_TWISS0
sequence = sequences.cathode_to_i1d
# Example of use with plain OCELOT:
plot_opt_funct(MagneticLattice(sequence), twiss0)
plt.show()
```

## I Just Want to  Run the Conversion Now

Clone the repository and install the Python package.  Put the
component list you want to convert in `src/euxfel/longlists`, or use
one that is already there.  Run:

```bash
$ euxfel convert
```

This will run, and the output will automatically be written to
`src/euxfel/subsequences/`.


## Conversion Configuration

The conversion should be as transparent as possible, and absolutely no
hand edits of the output Python modules should be necessary.  To this
end, the configuration is fully described in the file
conversion-config.yaml.  I'll try to explain some of the sections of
this config file here.

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

Warning: It is up to the user to ensure that these markers are not inside of
other elements!

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
        position: { reference: BZ.1980.TLD, s: 0.4724 }
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

Currently no other element types besides the `SlicedElement` may be
inserted into the lattice at conversion time.


## TODO:

- [ ] Integration of physics processes stuff (i.e. SectionTrack and
      friends) into package
- [ ] Particle tracking helper stuff into Python package.
- [ ] Python to Longlist (i.e. full round trip) converter.


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
