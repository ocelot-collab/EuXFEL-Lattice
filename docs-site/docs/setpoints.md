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

!!! note "Where things live"
    `euxfel.volts` names the **file format**, so it holds only what is about
    files or about the knobs a file sets: `MachineSetpoints`, the knob classes,
    and the Sascha reader. What a setpoint *means* is a property of the lattice
    and sits above it — `euxfel.Beamline` (addressing elements by name),
    `euxfel.kicks` (generalised kicks) and `euxfel.machine` (what hardware
    exists). None of those knows that files exist.

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

matching:                     # held back, not applied — see below
  Q.A1.1.I1: -0.309370
  QI.1.I1: -0.053430
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

### Reading is free, writing is guarded

Every name in the machine resolves. Looking a magnet up tells you nothing you
should not know, and 1287 element ids share a power supply, so refusing to name
them would make the beamline useless for reading:

```python
group = beamline["BB.96.I1"]
group.read()          # fine, always
group.split_from      # 'BB.1.I1' -- it shares a supply
group.owned_by        # 'bc0'     -- it is a chicane dipole
```

What is refused is **writing**, in the two cases where the kick that lands would
not be a state the machine could hold.

#### A knob owns the geometry

A chicane's dipole angle cannot move on its own: the drifts between the dipoles
must lengthen with it, or the chicane stops closing. Measured on BC0, writing
`BB.1.I1` directly leaves the exit **5.9 mm** downstream of where it belongs and
R56 **0.4 %** out. So `Group.write` refuses and names the knob that does it
properly:

```
'BB.1.I1' feeds the 4 dipoles of chicane 'bc0', whose geometry cannot be set
one magnet at a time: the drifts between the dipoles have to lengthen with the
angle or the chicane stops closing -- the survey downstream moves and R56 comes
out wrong. Set the chicane instead:
    setpoints.bc0.r56 = <value>      # or .angle, or .rho
```

Only chicanes are guarded — a cavity voltage has no drifts to move, so
`beamline["C.A2.L1"].write(0.1)` just works.

#### The magnet shares a supply

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
the split. In Python the equivalent is `write(..., ignore_knob=True)`.

!!! note "Why a file can still set a chicane dipole"
    Applying a setpoints file uses that same escape hatch, because by then the
    decision has been made: what could be routed to a knob already has been, and
    what is left is reported. The laser heater is the case that needs it — every
    shipped control-room file sets its three supplies to slightly different
    magnitudes, which is not a symmetric chicane, so its magnets are written
    individually and a warning says so.

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

## The matched section

Some of the machine this model decides for itself. The injector up to
`MATCH.52.I1` is the case that exists today: the A1 and AH1 voltages come from
`beam2rf` given the beam parameters, and `Q.A1.1.I1`, `Q.AH1.1.I1` and
`QI.1–3.I1` are re-matched *at conversion time* to restore the design optics at
that marker with the laser-heater undulator closed. Those values are outputs of
the model, not inputs to it.

A control-room file answers the same questions about the real gun's beam, and
the answers differ — `QI.1.I1` by a sign, `QI.2.I1` by a factor of three:

| supply | design `k1·l` | file `k1·l` | ratio |
| --- | --- | --- | --- |
| `Q.A1.1.I1` | −0.311228 | −0.309370 | 0.994 |
| `Q.AH1.1.I1` | 0.307795 | 0.310489 | 1.009 |
| `QI.1.I1` | 0.049480 | −0.053430 | −1.080 |
| `QI.2.I1` | 0.052617 | 0.164670 | 3.130 |
| `QI.3.I1` | −0.165365 | −0.205530 | 1.243 |

Applying them moves `beta_y` by 16 % through the injector while still arriving
within `bmag` 1.03 at `MATCH.52.I1`. Same match point, different route — and the
route is what an s2e run tracks through, under space charge.

### Provenance decides

The line is not file-versus-object; it is **swept in** versus **named**.

`from_sascha` and `from_lattice` take the whole machine, so nobody chose the
injector among the ~500 supplies they return. Those land in `matching` rather
than `elements`, and are held:

```python
setpoints = MachineSetpoints.from_sascha("BC2_TDS.txt")
beamline = setpoints.build(cell)        # injector left as the model solved it
                                        # ...and a warning says which supplies
```

Setting one yourself is a choice, and is applied like anything else:

```python
setpoints["QI.1.I1"] = 0.06             # goes to `elements` -> written
```

Where both name the same supply, `elements` wins — the deliberate entry beats
the incidental one.

### Writing it anyway

```python
setpoints.write_matching_section(beamline)   # after the fact
setpoints.build(cell, matching=True)         # or in one go
euxfel setpoints apply optics.yaml --matching
```

!!! note "Holding is about lattices, not files"
    A held value still exports. `to_sascha` and `resolve` serialise what the
    setpoints *say*, so a control-room file imported and written back out is
    unchanged, byte for byte, injector included.

The membership rule is positional and derived from the lattice — every supply
with a `ps_id` upstream of the marker — so a magnet added there is covered the
day it is added. Nothing lists the supplies; `euxfel-knobs.yaml` names only the
marker. A sequence that does not contain the marker has no matched section at
all, which is the right answer for a subsequence starting downstream.

That is also why the laser heater is in it. `BL.1.I1`, `BL.3.I1` and `BL.4.I1`
sit upstream of `MATCH.52.I1`, so a control-room file's 1.75 % asymmetry on
`BL.3.I1` is held too and the chicane stays symmetric. The asymmetry warning
then fires only when you ask for the file's values.

Unlike the [chicane guard](#a-knob-owns-the-geometry), this is not enforced on
`Group.write()`. `beamline["QI.1.I1"].write(x)` is free: that write is *correct*,
merely unwanted in bulk, and a single-quadrupole scan is a real thing to want.
`Group.matched_by` tells you where you are without stopping you.

## Knobs

The knobs are fixed hardware, declared once in `euxfel-knobs.yaml` and exposed as
named attributes — so editors can complete them and `setpoints.bc2.chrip` is an
`AttributeError` rather than a silently ignored key.

| Knob | Parameters | Hardware |
|---|---|---|
| `i1` | `E1`, `chirp`, `curvature`, `skewness` | A1 (1.3 GHz) + AH1 (3.9 GHz), solved together |
| `bc0`, `bc1`, `bc2` | exactly one of `r56`, `angle`, `rho` | The four-dipole bunch compressors |
| `lh` | exactly one of `r56`, `angle`, `rho` | The laser heater chicane, with the LH undulator in its middle |
| `l1`, `l2`, `l3` | `sum_voltage`, `chirp` | A2 / A3–A5 / A6–A25 |
| `i1_tds`, `b1_tds`, `b2_tds` | `voltage`, `phase` | The transverse deflecting structures; `b2_tds` drives both B2 structures |
| `modules["A7"]` | `voltage`, `phase` | One RF module on its own; see below |

Assigning one chicane parameter clears the others, so the last thing you set is
what is used. `report()` gives all three at once for display.

Every knob takes several parameters at once, which is usually shorter:

```python
setpoints.b2_tds.set(voltage=0.005, phase=90.0)
setpoints.i1.set(E1=0.130, chirp=-8.92, curvature=180.5, skewness=20332)
```

`set` behaves exactly like assigning each in turn — so a chicane still clears
its other two — and returns the knob. Passing more than one of `r56`, `angle`
and `rho` is refused rather than quietly keeping the last, and a misspelt name
raises listing the ones that exist.

An R56 is solved numerically against the real transfer matrix, seeded from the
small-angle closed form, and reaches the requested value to ~1e-12 m. The drifts
between the dipoles rescale to hold the projected geometry fixed — the magnets
are bolted to the floor, so bending harder lengthens the *path* between them by
`1/cos(angle)` while leaving their separation alone. Only `Drift` elements
absorb the change; a BPM between the dipoles has a fixed physical length.

The RF knobs wrap OCELOT's `beam2rf`/`rf2beam` and their linac wrappers, which
are exact inverses, so a chirp survives a round trip to machine precision.

### Setting a single RF module

`l3` drives all twenty modules of L3 together, which is usually what you want.
When one module has to differ — detuned, or off — set it on its own:

```python
from euxfel.volts.knobs import RFModuleKnob
setpoints.modules["A7"] = RFModuleKnob(voltage=0.5, phase=10.0)
```

`voltage` is the module total in GV, divided across its cavities, and `phase` is
in degrees. Unlike `l1`/`l2`/`l3` there is no beam-parameter inversion: this
writes what you give it.

The modules are `A1`, `AH1`, and `A2` through `A25`, derived from the linac and
injector specs rather than listed separately so the two cannot drift apart.

A module belongs to a linac, so setting both is refused:

```
Knobs 'l3' and 'modules.A7' both set C.A7.2.2.L3.phi. A module belongs to its
linac, so set the linac for the section as a whole or the module on its own,
not both.
```

Set the linac for the section, or the module alone — not both.

### A chicane need not be on one power supply

The bunch compressors each sit on a single supply, so `BB.1.I1` names all four
of BC0's dipoles. The laser heater is spread over three — `BL.1.I1` drives two
magnets, `BL.3.I1` and `BL.4.I1` one each — which has two consequences.

Polarity comes from the **design kicks**, not from the ratios within each
supply. Those ratios are `(1, -1)`, `(1,)` and `(1,)`, which say nothing about
how the supplies sit against one another; multiplying by each supply's design
reference recovers `[−, +, +, −]`, which is the chicane.

And a file can disagree with itself. In every control-room file shipped here,
`BL.3.I1` runs about 1.75 % weak against its two partners, so those four magnets
are **not** a symmetric chicane in practice. A single angle cannot express that,
so when a file sets a multi-supply chicane's supplies to different magnitudes
the magnets are applied individually, a warning names the disagreement, and the
`lh` knob stays out of it — which is why those files still round trip byte for
byte. Set `lh` yourself and it drives all four as a proper chicane.

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

### Writing part of a machine

Every line in a Sascha file *moves a supply* when the control room applies it, so
a file naming 476 supplies to change 45 of them clobbers 431 settings nobody
asked to touch. Narrow it:

```python
setpoints.to_sascha(cell, path="changed.txt", changed=True)
setpoints.to_sascha(cell, path="injector.txt", within=(cell[0], "MATCH.52.I1"))
setpoints.to_sascha(cell, path="two.txt", names=["QI.1.I1", "BB.96.I1"])
```

```bash
euxfel setpoints to-sascha my_optics.yaml --changed
euxfel setpoints to-sascha my_optics.yaml --within ocelot_start MATCH.52.I1
```

The criteria combine with **and**, and the same question can be asked of a
beamline directly with [`select`](api.md#finding-elements). `keys=` is the other
way to narrow — *exactly these, in this order*, which is what makes a round trip
byte identical — and cannot be combined with a selection.

#### Two ranges, because a supply is not a magnet

A Sascha line always sets a *whole* supply, so a range that only partly covers
one is not an error — the value written is that supply's value, correct for every
magnet on it. What it costs is a known footprint. Hence two words:

| | Selects | Warns about |
|---|---|---|
| `between=(a, b)` | supplies with **any** magnet in the range, included whole | the ones reaching past it, and how far |
| `within=(a, b)` | supplies with **every** magnet in the range | the ones it dropped for reaching past |

"Widen the range until nothing straddles" is not a remedy: `QA.1.SA1` feeds 19
quadrupoles across the whole SASE1 undulator, so widening to take it in drags in
every other supply there too.

`names=` follows the same rule — naming a magnet names its supply, with a warning
about the siblings that come with it. Naming something a Sascha file cannot hold
(a cavity supply, a TDS) is an error; a range that merely sweeps one up skips it
silently. Explicit beats incidental, the same rule as the [matched
section](#the-matched-section).

!!! warning "Do not range over the catalogue"
    `all_machine_elements()` stitches the branches together, so 53 supplies have
    magnets far apart in it and `QH.5.TL` has one magnet in each of two branches.
    Nothing raises, but expect a great many warnings. Pass the `cathode_to_*` you
    mean.

#### What "changed" compares against

By default, the values in `subsequences/*.py` — stamped onto each element as
`design_kick` when those modules import, so they are read rather than remembered
and cannot be lost by writing to the lattice.

Load a different baseline when you want to diff against a real machine setting:

```python
previous = set_design_optics("special-optics-files/BEAM_B2D.txt")
setpoints.to_sascha(path="diff.txt", changed=True)   # what differs from BEAM_B2D
set_design_optics(previous)                          # hand it back to restore
```

It takes a Sascha file, a YAML file, a `MachineSetpoints`, a `Beamline`, a plain
mapping, or `None` for the generated values. It is process-wide and read at call
time, so a beamline built earlier answers the new question — and `to_sascha`,
which builds its own beamline internally, can see it.

Only the **optics** moves. The **wiring** — `QE.1.L3` is `[+, −, +]` — is derived
from the stamps and never moves, because that is how the magnets are cabled and
not something an optics can say. Two supplies are left alone: ones the optics
does not name (a Sascha file names 111 of 505, and the rest are not "changed from
nothing") and chicane supplies it sets to zero (a zero has no sign, and the
design kicks are what tell a chicane which way its dipoles bend).

!!! note "`changed` means something narrower on export"
    `beamline.select(changed=True)` asks whether the numbers differ at all.
    `to_sascha(changed=True)` asks whether they differ *in the file*, at the six
    decimal places the format records. Of the 108 supplies `BC2_TDS.txt` moves,
    only **45** move by more than that — the other 63 would be lines setting what
    is already set.

## Start-to-end tracking

`MachineSetpoints` owns the lattice. `SectionTrack` attaches physics processes
and tracks; it does not write magnet or RF values any more.

```python
setpoints = load_setpoints("sase2_14gev.yaml")
setpoints.apply_in_place()

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
