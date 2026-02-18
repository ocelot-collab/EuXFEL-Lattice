## How to Run the Conversion Now
Currently the OCELOT Python EuXFEL sequences are generated from the
"Component List", an Excel spreadsheet generated internally by the
group leader as the "single source of truth" for what actually is in
the tunnel.  These files can be found [here](https://xfel.desy.de/operation/component_list/).


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
