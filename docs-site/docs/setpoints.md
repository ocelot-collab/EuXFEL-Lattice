# Machine setpoints

A **setpoints** file records what the machine is asked to do: high-level knobs
such as an R56 or a chirp, plus individual magnet strengths. It can be applied to
a lattice, read back off one, and round-tripped to and from the control room's
file format.

Not "optics", because it carries RF voltage, phase and chirp as well as magnet
strengths, and only the latter are optics in the usual sense. "Setpoint" is the
control-system word for a demanded value, which is what all of it is.

Before this existed, machine settings lived in three disconnected places: design
values baked into the generated `subsequences/*.py`, operational values in
`special-optics-files/*.txt` that nothing read, and literals typed into each s2e
script. The constant `r1 = 0.5 / 0.1366592804`, copy-pasted across six scripts,
is exactly the value of `BB.1.I1` in `BC2_TDS.txt` — a real BC0 bend angle,
transcribed by hand out of a file the code could not open.

## Quick start

```python
from euxfel import sequences
from euxfel.volts import MachineSetpoints

setpoints = MachineSetpoints.design()
setpoints.bc2.r56 = -0.0432          # metres; drifts follow automatically
setpoints.l1.sum_voltage = 0.57872   # GV
setpoints.l1.chirp = -9.1
setpoints["QI.1.I1"] = -0.05343      # by power supply, or by element id

cell = setpoints.build(sequences.cathode_to_t4d)
```

`build` returns a **new** sequence. It never touches the one you passed: the
generated cells are shared by every `SectionTrack` and by `euxfel plot`, so
mutating them would leak into everything else in the process.

## The file format

The Python object is primary; YAML is a thin layer over it.

```yaml
version: 1
lattice: component_list_2026.02.13   # guards against a stale config
name: BC2 TDS optics
extends: bc2_tds.yaml                # optional, single level

knobs:
  bc2: {r56: -0.0432}
  l1:  {sum_voltage: 0.57872, chirp: -9.1}
  i1: {E1: 0.130, chirp: -8.92, curvature: 180.5, skewness: 20332}

elements:
  QI.1.I1: -0.053430          # generalised kick; both namespaces searched
  ps:QI.1.I1: -0.053430       # force the power supply reading
  id:BB.96.I1: -0.13          # force one magnet, splitting a shared supply
  QI.63.I1D: {k1: -2.9974}    # explicit OCELOT attributes
```

Load with `MachineSetpoints.from_yaml(path)` or `euxfel.volts.load_setpoints(path)`.

Unknown keys are errors rather than silent no-ops, attribute names are checked
against the element's `__init__` signature, and `extra="forbid"` catches a
misspelt `chrip`.

## Addressing: `id` and `ps_id`

Every powered element carries a `ps_id` — the power supply feeding it. All four
BC0 dipoles share `BB.1.I1`; all 32 L1 cavities share `C.A2.L1`. Keys are
resolved against **both** namespaces, so you can write whichever you are
thinking in.

Measured over the current lattice (8178 elements, 502 supplies):

- 59 names appear in both namespaces and **none** is ambiguous — in every case
  the supply feeds exactly one magnet, of that same name.
- 360 of 476 supplies feed exactly one element, so for most quadrupoles the two
  namespaces are equally precise.
- Elements without a `ps_id` (markers, drifts, monitors) are reachable by `id`
  only.

### Ganged magnets

A magnet whose supply feeds others **cannot** be set on its own in the real
machine, so trying to raises:

```
'BB.96.I1' shares power supply 'BB.1.I1' with BB.98.I1, BB.100.I1, BB.101.I1
and cannot be set individually -- that is not realisable on the machine.
Use the supply name:
    BB.1.I1: <value>
or, to set this one magnet anyway (simulation only):
    {id: BB.96.I1}: <value>
```

The `id:` prefix is the deliberate opt-out, for gradient-error and single-magnet
sensitivity studies. Such an optics cannot be exported to the Sascha format,
which stores one value per supply, and `to_sascha` refuses rather than losing
the split.

### Design ratios are preserved

Magnets on one supply are not identical. Twelve supplies have mixed polarity —
`QE.1.L3` is `[+, −, +]`, `QF.4.CL` is an alternating FODO of 18 quadrupoles —
and five have unequal magnitudes, such as `QF.4.T5` at `[0.118, 0.262]`. So a
setpoint is distributed in proportion to the **design** kicks:

```
factor[i] = design_kick[i] / reference        # reference = largest |kick|
kick[i]   = setpoint * factor[i]
```

Opposite wiring is just `factor = -1`. Factors are captured from the pristine
lattice when the index is built, so repeated application never compounds them,
and applying a supply's design value is an exact no-op.

## Knobs

The knobs are fixed hardware, declared once in `euxfel-knobs.yaml` and exposed as
named attributes — so editors can complete them and `setpoints.bc2.chrip` is an
`AttributeError` rather than a silently ignored key.

| Knob | Parameters | Hardware |
|---|---|---|
| `i1` | `E1`, `chirp`, `curvature`, `skewness` | A1 (1.3 GHz) + AH1 (3.9 GHz), solved together |
| `bc0`, `bc1`, `bc2` | exactly one of `r56`, `angle`, `rho` | The four-dipole bunch compressors |
| `l1`, `l2`, `l3` | `sum_voltage`, `chirp` | A2 / A3–A5 / A6–A25 |
| `i1_tds`, `b1_tds`, `b2_tds` | `voltage`, `phase` | The transverse deflecting structures; `b2_tds` drives both B2 structures |

Assigning one chicane parameter clears the others, so the last thing you set is
what is used. `report()` gives all three at once for display.

An R56 is solved numerically against the real transfer matrix, seeded from the
small-angle closed form, and reaches the requested value to ~1e-12 m. The drifts
between the dipoles rescale to hold the projected geometry fixed — the magnets
are bolted to the floor, so bending harder lengthens the *path* between them by
`1/cos(angle)` while leaving their separation alone. Only `Drift` elements
absorb the change; a BPM between the dipoles has a fixed physical length.

The RF knobs wrap OCELOT's `beam2rf`/`rf2beam` and their linac wrappers, which
are exact inverses, so a chirp survives a round trip to machine precision.

### What the linac parameters mean

Worth stating because OCELOT's own docstring says "chirp: in control system
[GeV]", which is wrong.

`sum_voltage` is the **energy gain**, in GV — not the final energy. Setting
`l1.sum_voltage = 0.57872` adds 0.57872 GeV to the 0.13 GeV entering L1, giving
0.70872 GeV out. The knob solves it into a cavity voltage and phase, so the
voltage that actually appears on a cavity is larger: 0.625258 GV total here,
because the section runs off crest.

`chirp` is `−k·v·sin(φ) / E₁` in **1/m**, where `k = 2πf/c ≈ 27.246 1/m` and E₁
is that section's *final* energy. It is the relative energy chirp per metre:
`chirp = -9.1` means dδ/dz of −9.1 m⁻¹, so about −0.9 % of relative energy spread
across a 1 mm bunch.

`init_energy` is not a knob parameter at all — it is a property of the section,
recorded once in `euxfel-knobs.yaml` (0.13, 0.7 and 2.4 GeV for L1, L2 and L3).

## The control-room (Sascha) format

`special-optics-files/*.txt` are the live DESY format: one `NAME VALUE` pair per
line, six decimal places, no trailing newline. Values are **generalised kicks**,
energy-independent, which is what makes the file meaningful on its own:

| Element | Value | OCELOT attribute |
|---|---|---|
| `Quadrupole` | `k1·l` [rad/m] | `k1 = value / l` |
| `Sextupole` | `k2·l` [rad/m²] | `k2 = value / l` |
| `SBend` / `RBend` | `angle` [rad] | `angle` |

```bash
euxfel setpoints diff special-optics-files/BC2_TDS.txt special-optics-files/BEAM_B2D.txt
euxfel setpoints to-sascha my_optics.yaml --like special-optics-files/BC2_TDS.txt
```

Two conventions are handled automatically, both of which are silent when wrong:

**Bend angles are sign-flipped.** Across all three shipped files, every one of
the ten bend supplies has the opposite sign to the design lattice — six at a
ratio of exactly −1 — while quadrupoles and sextupoles agree. Importing without
this would reverse every dipole in the machine.

**Chicane dipoles route to their knob.** `BB.1.I1` is a plain line in a Sascha
file, but writing its angle without rescaling the drifts leaves a chicane whose
geometry no longer closes. Such an entry is converted into a knob setting, and
the conversion is reported rather than silent.

Bends that *no* knob owns — `BL.6/7/8.I1` in the I1 dogleg, `BG.1.B2D` in the
dump line — are written directly with no drift compensation, and warn that the
downstream survey moves. That is correct: changing a dogleg is *supposed* to move
the geometry.

## Start-to-end tracking

`MachineSetpoints` owns the lattice. `SectionTrack` attaches physics processes
and tracks; it does not write magnet or RF values any more.

```python
setpoints = load_setpoints("sase2_14gev.yaml")
setpoints.apply_in_place(full_machine_cell())

section_lat = SectionLattice(sequence=all_sections, tws0=tws0, data_dir=data_dir)

config = {                                   # physics processes only
    A1:  {"SC": SC_exec, "smooth": True, "wake": wake_exec},
    BC0: {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec},
    ...
}
```

`apply_in_place` mutates the module-level cells, which is process-global and
irreversible. It has to: `SectionLattice` takes a list of section *classes*, and
each `SectionTrack` builds its own `MagneticLattice` from `i1.cell` / `t5.cell`
inside `__init__`, so there is nowhere to hand a freshly built sequence. That is
fine for a script that runs once and exits. Everywhere else — plots, exports,
knob scans — use `build(cell)`, which returns a private copy.

It must run **before** `SectionLattice` is constructed, since each section
calculates its design twiss as it is built.

!!! warning "`rho`, `v` and `phi` in a config dict now raise"

    They used to be applied by `update_bunch_compressor` and `update_cavity`
    during tracking. Silently ignoring them would let a run finish with its
    compression quietly at the design value, so they raise instead, pointing at
    the knob that replaces them. Every s2e script written before this change
    needs migrating.

!!! note "The chicane angle is now exact"

    Previously a requested angle was converted to a radius, put in the config
    dict, and converted back by `arcsin(dipole_len / rho)` using a `dipole_len`
    hardcoded in `sections.py` — a constant that existed twice and could
    disagree with the lattice. It did, by ~1e-6. Now the angle is written
    straight onto the dipoles and nothing re-derives it.

## Layering

`extends` pulls in one parent file, so a study variant is two lines rather than a
copied 110-line file:

```yaml
extends: bc2_tds.yaml
knobs:
  bc2: {r56: -0.015}
```

Knobs are replaced whole rather than field-wise — a chicane's `r56`, `angle` and
`rho` are three ways of saying one thing, and mixing them across files would be
ambiguous. Element entries merge key by key. Nesting is one level deep so the
resolution order stays obvious.

## Version drift

`to_yaml` can record a `resolved:` block of the fully expanded setpoints. Knobs
record *intent*, and `bc2.r56 = -0.0432` resolves to different dipole angles if
the lattice changes underneath it; the snapshot records what it resolved to when
written. Applying warns if the two no longer agree — which the `lattice:` field
alone cannot catch.

## Command line

```
euxfel setpoints apply CONFIG [--target T4D]     # apply and show the optics
euxfel setpoints dump [--from-sascha FILE]       # lattice state -> YAML
euxfel setpoints to-sascha CONFIG [--like FILE]  # YAML -> control-room format
euxfel setpoints diff A B                        # compare two optics, either format
```

`--target full` gives every element of the machine once. The EuXFEL branches, so
no single cathode-to-dump sequence holds all of it — `BG.1.B2D` exists only in
the B2D line — and the control-room format spans the whole machine.
