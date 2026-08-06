# Layout

How the machine is cut up, and where each piece lives in the package.

## Targets

The EuXFEL branches, so there is no single sequence containing the whole
machine. Instead there are six **targets** — cathode-to-dump paths — each built
by flattening an ordered list of subsequences:

| Target | Subsequences |
|---|---|
| `I1D` | i1 → i1d |
| `B1D` | i1 → l1 → b1d |
| `B2D` | i1 → l1 → l2 → b2d |
| `TLD` | i1 → l1 → l2 → l3 → cl → tl2tld |
| `T4D` | i1 → l1 → l2 → l3 → cl → tl2 → tl34 → sase1 → t4 → sase3 → t4d |
| `T5D` | i1 → l1 → l2 → l3 → cl → tl2 → tl34_sa2 → t1 → sase2 → t3 → t5 → t5d |

Each becomes a module-level cell:

```python
from euxfel import sequences
sequences.cathode_to_t5d      # a flat list of OCELOT elements
sequences.CATHODE_TWISS0      # the initial Twiss for all of them
```

They share their leading subsequences, and therefore share **the same element
objects** — `cathode_to_i1d` and `cathode_to_t5d` hand back the same
`QI.46.I1`. Mutating one changes all of them; see
[Machine setpoints](setpoints.md) for what that means in practice.

Where you need every element exactly once — the control-room format spans the
whole machine, and `BG.1.B2D` exists only in the B2D line — use:

```python
from euxfel.volts import all_machine_elements
cell = all_machine_elements()    # every element, once, in a sliceable order
```

## Subsequences

`src/euxfel/subsequences/*.py` are **generated artefacts**. Each holds a
`twiss0`, the element definitions, a `cell` tuple, and the `ps_id` power-supply
assignments. Never hand-edit them: change
`src/euxfel/longlists/conversion-config.yaml` and re-run `euxfel convert`. The
process is documented in [Conversion](conversion.md).

Element names are mechanical transforms of the component-list IDs —
`C.A1.1.1.I1` becomes `i1.c_a1_1_1_i1` — which is why the code is full of opaque
identifiers.

## Sections

A **section** is a slice of a target between two markers, with physics processes
attached. These are the units an s2e run tracks through, defined in
`src/euxfel/sections.py`:

```
A1  AH1  LH  DL  I1D  BC0  L1  BC1  L2  BC2  B2D  L3  CL1  CL2  CL3
TL  SASE1  T4  SASE3  T4D  T1  SASE2  T3  T3_chirper  T5
```

A section boundary can only exist where a marker exists. Markers such as
`ocelot_start`, `a1_sim_stop` and `lh_start` are **not** in the component list —
they are injected by the conversion YAML's `new_markers` block. Moving a
boundary therefore means editing that YAML and regenerating, not editing
`sections.py`.

See [Start to end simulations](s2e.md) for running them.

## Two layers, easily confused

| | Holds | Where |
|---|---|---|
| **Static lattice** | Geometry and design optics: element objects, a `cell`, a `twiss0` | `subsequences/`, `sequences.py` |
| **Tracking model** | Section slices plus space charge, CSR, wakes, apertures | `sections.py`, `section_track.py` |

The static lattice is what `euxfel plot` and `euxfel compare` work on. The
tracking model is what an s2e script runs.

## Package modules

| Module | Role |
|---|---|
| `sequences.py` | The six targets |
| `subsequences/` | Generated element definitions (21 modules) |
| `sections.py` | The 25 section definitions and the global tracking constants |
| `section_track.py` | `SectionLattice`/`SectionTrack`, vendored from OCELOT |
| `volts/` | Machine setpoints — see [Machine setpoints](setpoints.md) |
| `conversion.py`, `writer.py` | Component list → Python, and the code generator |
| `complist.py`, `complist_draw.py` | Reading and drawing the component list |
| `optics.py` | Optics and survey comparison against the component list |
| `plot.py`, `latdraw/` | Optics plots with machine-layout strips |
| `slicing.py` | XY-quadrupole slice expressions |
| `cli.py` | The `euxfel` command |
| `longlists/` | The component-list spreadsheets and conversion configs |
| `wakes/` | Wake tables |

## Import degradation is deliberate

`euxfel/__init__.py`, `subsequences/__init__.py` and `sequences.py` each wrap
their imports in `try/except` and downgrade failures to a warning, so a broken
or half-written conversion still leaves an importable package.

The cost is that a missing `euxfel.subsequences.l3` surfaces as an
`AttributeError` far from the real cause. If something is unexpectedly absent,
look for the conversion warning first.
