# Optics configurations

An **optics** is a set of setpoints: high-level knobs such as an R56 or a chirp,
plus individual magnet strengths. It can be applied to a lattice, read back off
one, and round-tripped to and from the control room's file format.

Before this existed, machine settings lived in three disconnected places: design
values baked into the generated `subsequences/*.py`, operational values in
`special-optics-files/*.txt` that nothing read, and literals typed into each s2e
script. The constant `r1 = 0.5 / 0.1366592804`, copy-pasted across six scripts,
is exactly the value of `BB.1.I1` in `BC2_TDS.txt` — a real BC0 bend angle,
transcribed by hand out of a file the code could not open.

## Quick start

```python
from euxfel import sequences
from euxfel.volts import Optics

optics = Optics.design()
optics.bc2.r56 = -0.0432          # metres; drifts follow automatically
optics.l1.sum_voltage = 0.57872   # GV
optics.l1.chirp = -9.1
optics["QI.1.I1"] = -0.05343      # by power supply, or by element id

cell = optics.build(sequences.cathode_to_t4d)
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
  injector: {E1: 0.130, chirp: -8.92, curvature: 180.5, skewness: 20332}

elements:
  QI.1.I1: -0.053430          # generalised kick; both namespaces searched
  ps:QI.1.I1: -0.053430       # force the power supply reading
  id:BB.96.I1: -0.13          # force one magnet, splitting a shared supply
  QI.63.I1D: {k1: -2.9974}    # explicit OCELOT attributes
```

Load with `Optics.from_yaml(path)` or `euxfel.volts.load_optics(path)`.

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
named attributes — so editors can complete them and `optics.bc2.chrip` is an
`AttributeError` rather than a silently ignored key.

| Knob | Parameters | Hardware |
|---|---|---|
| `injector` | `E1`, `chirp`, `curvature`, `skewness` | A1 (1.3 GHz) + AH1 (3.9 GHz), solved together |
| `bc0`, `bc1`, `bc2` | exactly one of `r56`, `angle`, `rho` | The four-dipole bunch compressors |
| `l1`, `l2`, `l3` | `sum_voltage`, `chirp` | A2 / A3–A5 / A6–A25 |

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
euxfel optics diff special-optics-files/BC2_TDS.txt special-optics-files/BEAM_B2D.txt
euxfel optics to-sascha my_optics.yaml --like special-optics-files/BC2_TDS.txt
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

`SectionLattice` handles per-magnet setpoints and section knobs through different
channels, so an optics reaches a tracking run two ways:

| What | Channel |
|---|---|
| Quadrupoles, sextupoles, individual bends | Applied to the sequence **before** `SectionLattice` is built |
| Chicane `rho`, cavity `v`/`phi` | Emitted into the per-section `config` dict |

```python
optics = load_optics("sase1_14gev.yaml")
cell = optics.build(sequences.cathode_to_t4d)
section_lat = SectionLattice(sequence=cell, tws0=tws0, data_dir=data_dir)

config = optics.section_config({
    A1:  {"SC": SC_exec, "smooth": True, "wake": wake_exec},
    BC0: {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec},
    ...
})
```

`section_config` fills in `rho`, `v` and `phi` and leaves the physics-process
toggles exactly as given — they describe the tracking model, not the optics.

!!! warning "This corrects the hardcoded chicane radii"

    The s2e scripts compute `r1 = 0.5 / 0.1366592804`, but
    `update_bunch_compressor` inverts its argument as `arcsin(yoke / rho)`. The
    missing sine makes BC0 bend about **0.31 %** harder than the control-room
    file asks for (0.047 % for BC1, 0.028 % for BC2). `section_config` emits
    `yoke / sin(angle)`, so the angle that reaches the tracking is the one the
    file actually specifies. Every RF value it produces is bit-identical to the
    scripts.

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
euxfel optics apply CONFIG [--target T4D]     # apply and show the optics
euxfel optics dump [--from-sascha FILE]       # lattice state -> YAML
euxfel optics to-sascha CONFIG [--like FILE]  # YAML -> control-room format
euxfel optics diff A B                        # compare two optics, either format
```

`--target full` gives every element of the machine once. The EuXFEL branches, so
no single cathode-to-dump sequence holds all of it — `BG.1.B2D` exists only in
the B2D line — and the control-room format spans the whole machine.
