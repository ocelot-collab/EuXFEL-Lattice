# Start-to-end simulations

An s2e run pushes a particle distribution from 3.2 m after the cathode to one of
the undulators or dumps, through every magnet, cavity and wake in between. The
scripts live in `s2e_scripts/`.

They are long — hours, not minutes — and they write intermediate `.npz` beams
back into `beam_files/`. To check an optics *without* tracking, use
`euxfel setpoints apply` instead.

## Running one

`data_dir` is relative, so run from inside the directory:

```bash
cd s2e_scripts && python s2e_up_to_SA1_volts.py
```

| Script | Tracks as far as |
|---|---|
| `s2e_up_to_I1D_screen_volts.py` | the injector dump screen |
| `s2e_up_to_B2D_volts.py` | the B2 dump |
| `s2e_up_to_switchyard_volts.py` | the end of TL |
| `s2e_up_to_SA1_volts.py` | SASE1 |
| `s2e_up_to_SA2_volts.py` | SASE2 |
| `s2e_up_to_SA3_volts.py` | SASE3 |
| `s2e_up_to_T5D_volts.py` | SASE2, then T3 and T5 |

The scripts without the `_volts` suffix are the previous generation. They still
put `rho`, `v` and `phi` in the section config, which now raises — see
[What changed](#what-changed).

## The shape of a script

Four steps, in this order.

```python
# 1. The beam.
p_array_init = load_particle_array(data_dir + "gun/rf_gun_new.npz")

# 2. The setpoints: what the machine is asked to do.
setpoints = load_setpoints("setpoints/nominal_14gev.yaml")
setpoints.i1.gun_energy = p_array_init.E

# 3. Apply them to the lattice, before the sections are built.
setpoints.apply_in_place(full_machine_cell(), verbose=True)
section_lat = SectionLattice(sequence=sections, tws0=tws0, data_dir=data_dir)

# 4. Physics processes, and track.
config = {
    A1:  {"SC": SC_exec, "smooth": True, "wake": wake_exec},
    BC0: {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    ...
}
p_array = section_lat.track_sections(
    sections=sections, p_array=p_array_init, config=config,
    force_ext_p_array=True, coupler_kick=coupler_kick_exec,
)
```

### Why the order matters

`apply_in_place` **must** come before `SectionLattice` is constructed. Each
section calculates its design Twiss as it is built, and `apply_matching` later
transforms the particle distribution onto that Twiss. Apply the setpoints
afterwards and every section keeps its *design* optics, so `match=True` quietly
pulls the beam back to the design and undoes what you set.

### Why it is `apply_in_place` and not `build`

`apply_in_place` mutates the module-level generated cells. That is
process-global and irreversible: the same element objects are shared by every
section, by every `sequences.cathode_to_*`, and by `euxfel plot`.

It has to be. `SectionLattice` takes a list of section *classes*, and each
`SectionTrack` builds its own `MagneticLattice` from `i1.cell` / `t5.cell` inside
its `__init__`, so there is nowhere to hand a freshly built sequence — the only
way setpoints can reach a tracking run is to change the elements the sections
are about to pick up.

That is fine for a script that runs once and exits, which is what these are. For
anything else — plots, exports, parameter scans, notebooks — use
`setpoints.build(cell)`, which returns a private copy and leaves the design
alone.

## The setpoints files

The RF values and compressor angles live in `s2e_scripts/setpoints/`:

| File | Used by |
|---|---|
| `nominal_14gev.yaml` | SA1, SA2, SA3, B2D, switchyard |
| `i1d_screen.yaml` | I1D_screen |

Five scripts share one file rather than carrying five copies of the same
numbers. Editing the working point is one edit, in one place.

`gun_energy` is deliberately not in `nominal_14gev.yaml`: it is the energy of
whichever beam file the script loads, so each script sets it from
`p_array_init.E` after loading and before applying. `i1d_screen.yaml` does pin
it, because that script always hardcoded `E0 = 0.0065` rather than reading it
from the beam.

The format itself — knobs, addressing, the control-room files — is documented in
[Machine setpoints](setpoints.md).

## The config dict

It carries **physics processes only**:

| Key | Effect |
|---|---|
| `SC` | space charge |
| `CSR` | coherent synchrotron radiation |
| `wake` | wakefields |
| `smooth` | current-profile smoothing |
| `match` | re-match the beam to the section's design Twiss on entry |
| `bounds`, `remove_offsets` | passed to the matching |
| `IBS` | intra-beam scattering |
| `save_output_files` | write the section's beam and Twiss |

A section absent from the dict keeps its defaults.

## What changed

Magnets and RF used to be set from inside tracking: `update_sections` called
`update_bunch_compressor(rho)` and `update_cavity(phi, v)`. They no longer
exist, and a config dict carrying `rho`, `v`, `phi` or `tds.*` raises:

```
A1: 'phi', 'v' (cavity phase, cavity voltage) no longer belong in the section
config -- the lattice is owned by euxfel.volts.MachineSetpoints. Set them there
and apply the setpoints before building the SectionLattice.
```

It raises rather than being ignored on purpose: a silently dropped `rho` would
let a run finish with its compression quietly at the design value, and the
result would look plausible.

Two consequences worth knowing:

**Compression changed slightly.** The old scripts computed a bend radius as
`0.5 / angle`, but `update_bunch_compressor` inverted it as
`arcsin(dipole_len / rho)`. The missing sine made BC0 bend about 0.31 % harder
than the control-room value asked for (0.047 % at BC1, 0.028 % at BC2). The
angle is now written straight onto the dipoles, so it is exactly the value you
set.

**RF did not change.** The per-cavity voltage and phase are bit-identical to
what the previous scripts produced from the same beam parameters; a test pins
this.

## Migrating a script of your own

Every value you need is already in the old script, as an argument to `beam2rf`:

```python
# was
v11, phi11, v13, phi13 = beam2rf(E1=E1, chirp=-8.92, curvature=180.5,
                                 skewness=20332, n=3, freq=1.3e9, E0=E0)
v21, phi21 = beam2rf_xfel_linac(sum_voltage=578.72e-3, chirp=-9.1, init_energy=0.13)
r1 = 0.5 / 0.1366592804          # "BC magnet radius read from BKR"

# becomes
setpoints.i1.E1, setpoints.i1.chirp = 0.130, -8.92
setpoints.i1.curvature, setpoints.i1.skewness = 180.5, 20332
setpoints.l1.sum_voltage, setpoints.l1.chirp = 0.57872, -9.1
setpoints.bc0.angle = 0.1366592804
```

Note the last line: the comment above `r1` said the number came from BKR, and
`BB.1.I1` in a control-room file is indeed `0.136659`. Setting the angle
restores that number directly instead of encoding it as a radius.

Then move the `SectionLattice` construction to *after* the beam load and the
`apply_in_place` call, and delete the `rho`/`v`/`phi` entries from the config
dict. Nothing else moves.

## Per-magnet settings

Quadrupole settings that go with a particular optics belong in a control-room
file rather than a dict in the script. `s2e_up_to_I1D_screen_volts.py` loads
one:

```python
setpoints = setpoints.merged_with(
    MachineSetpoints.from_sascha("../special-optics-files/DX12_I1D.txt",
                                 full_machine_cell())
)
```

!!! warning "That script does not currently run"

    `DX12_I1D.txt` contains `QI.62.I1`, which is not an element in the lattice —
    and is absent from all three component lists, so it never was. The dict it
    came from matched on element id, so that setpoint has silently never been
    applied in any run. It is kept so the discrepancy fails loudly instead of
    continuing to do nothing. Resolve the name or drop the line from the file.

## Global tracking constants

`Sig_Z`, `SCmesh`, `CSRBin` and `SmoothPar` sit at the top of
`src/euxfel/sections.py` and apply to every run. They are not setpoints — they
describe the numerical model, not the machine — so they are not in the setpoints
files.
