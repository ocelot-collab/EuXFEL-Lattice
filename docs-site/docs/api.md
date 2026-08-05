# API

The public surface, by what you are trying to do. Each entry points at the page
that explains it properly.

## The lattice

```python
from euxfel import sequences

sequences.cathode_to_t5d       # flat list of OCELOT elements, cathode to T5D
sequences.CATHODE_TWISS0       # initial Twiss for every target
sequences.TARGET_NAMES         # ("I1D", "B1D", "B2D", "TLD", "T4D", "T5D")
```

The six targets share element objects; see [Layout](layout.md).

```python
from euxfel.volts import full_machine_cell
full_machine_cell()            # every element exactly once, across all branches
```

## Machine setpoints

Full documentation in [Machine setpoints](setpoints.md).

```python
from euxfel.volts import MachineSetpoints, load_setpoints

setpoints = MachineSetpoints.design()          # empty; the lattice keeps design values
setpoints = load_setpoints("optics.yaml")      # from a YAML file
setpoints = MachineSetpoints.from_sascha(path, cell)   # from a control-room file
setpoints = MachineSetpoints.from_lattice(cell)        # read back off a lattice
```

| Method | Does |
|---|---|
| `build(cell)` | Apply to a **copy**; returns a new sequence. Use this by default. |
| `apply_in_place(cell)` | Apply to the caller's elements. Process-global; only for s2e scripts. |
| `merged_with(other)` | This, overridden by `other` |
| `resolve(cell)` | Every supply setpoint as a flat mapping |
| `to_yaml(path)` / `to_sascha(cell, path)` | Write it out |

Knobs are reached as attributes: `setpoints.bc2.r56`, `setpoints.l1.chirp`,
`setpoints.i1.curvature`, `setpoints.b2_tds.voltage`. Individual magnets
by subscript: `setpoints["QI.1.I1"] = -0.05343`.

### Finding elements

```python
from euxfel.volts import Beamline

beamline = Beamline.from_cell(cell)    # deep-copies by default
group = beamline["QI.1.I1"]            # by power supply or by element id
group.read()                           # the current setpoint
group.write(-0.053)                    # set it, preserving design ratios
```

A `Beamline` is a sequence of elements you can also address by name — the
name-to-element lookup OCELOT does not provide. Being a sequence, it goes
straight into `MagneticLattice` where a list would:

```python
len(beamline); beamline[0]; list(beamline)     # an ordinary sequence
MagneticLattice(beamline, start=..., stop=...) # no `.cell` needed
"QI.1.I1" in beamline                          # membership by name
beamline.cell                                  # a plain list, to concatenate
```

`build()` and `apply_in_place()` both return one, so the magnets stay reachable
by name after a file is applied. It also offers `resolve` (the explicit spelling
of the string subscript, and the one that takes `namespace=`), `position`,
`between`, `siblings`, `supply_of` and `design_kicks`.

Slicing gives a plain list rather than another `Beamline`: design ratios belong
to a whole power supply, and half a supply has none.

### Exceptions

| Raised when |  |
|---|---|
| `UnknownKeyError` | The name matches no element and no supply |
| `GangedMagnetError` | A magnet sharing a supply was addressed alone |
| `AmbiguousKeyError` | A name resolves two different ways |
| `ConflictError` | Two settings claim the same attribute |
| `ChicaneError` | A chicane cannot be configured as asked |
| `KickError` | The element has no generalised-kick representation |

## Tracking

See [Start to end simulations](s2e.md).

```python
from euxfel.section_track import SectionLattice
from euxfel.sections import A1, AH1, BC0    # ... and the rest

section_lat = SectionLattice(sequence=sections, tws0=tws0, data_dir=data_dir)
p_array = section_lat.track_sections(sections=sections, p_array=beam, config=config)
```

The `config` dict carries physics-process toggles only. Magnet and RF values
belong in `MachineSetpoints`.

## Optics and comparison

```python
from euxfel.optics import (
    print_optics_at_points,        # Twiss at the fixed match points, with Bmag
    print_surveyed_match_points,   # surveyed positions vs the component list
    bmag,                          # the mismatch parameter
)
from euxfel.plot import plot_cathode_to_target, compare_cathode_to_target
```

Note the name collision: `euxfel.optics` is this comparison module. The
setpoints class lives in `euxfel.volts`.

## The component list

See [Conversion](conversion.md).

```python
from euxfel.complist import ComponentList
from euxfel.conversion import longlist_to_ocelot

ComponentList(path).longlist          # a polars DataFrame
longlist_to_ocelot(config, outdir)    # regenerate the subsequence modules
```

## Command line

```
euxfel convert                       regenerate subsequences from the component list
euxfel plot [TARGET...]              design optics, cathode to each dump
euxfel compare [TARGET...]           OCELOT optics vs the component list's own columns
euxfel subsequence --list            subsequence names per target
euxfel setpoints apply CONFIG        apply setpoints and show the resulting optics
euxfel setpoints dump                read the setpoints off the lattice as YAML
euxfel setpoints to-sascha CONFIG    export to the control-room format
euxfel setpoints diff A B            compare two sets of setpoints
euxfel version
```
