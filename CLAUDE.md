# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The European XFEL accelerator lattice as an [Ocelot](https://github.com/ocelot-collab/ocelot) model: a Python
description of every magnet, cavity and marker in the machine, plus start-to-end
(s2e) tracking scripts that push a particle distribution from 3.2 m after the
cathode to the undulators or dumps.

The lattice is **not** written by hand. It is generated from the "Component
List", an Excel spreadsheet maintained at DESY as the single source of truth for
what is physically in the tunnel.

## Commands

```bash
pip install --editable .          # editable install needed to regenerate lattice files
uv sync                           # alternative; uv.lock is committed

pytest                            # full suite (coverage is on by default via addopts)
pytest tests/test_subsequences.py::test_subsequences_linear_optics   # single test
pytest --no-cov -k sections       # faster iteration, skip coverage

tox                               # lint + format + tests on 3.12/3.13/3.14
tox -e lint                       # ruff check --fix src
tox -e format                     # ruff isort + ruff format on src

euxfel convert                    # regenerate src/euxfel/subsequences/ from the component list
euxfel plot [TARGET...]           # design optics cathode -> each dump
euxfel compare [TARGET...]        # Ocelot optics vs. the component list's own optics columns
euxfel subsequence --list         # show subsequence names per target

cd docs-site && mkdocs serve      # docs (dependency-group `docs`)
```

Targets are `G1D I1D B1D B2D TLD T4D T5D`. Python >= 3.12 (`.python-version` pins
3.14). Ocelot is pinned to an exact git rev in `[tool.uv.sources]` — lattice
generation is sensitive to Ocelot's element `__init__` signatures, so bumping
that rev can silently change generated output.

## Architecture

### The generation pipeline

```
component_list_<date>.xls   (src/euxfel/longlists/, ~17 MB, one sheet per path through the machine)
        |
        |  complist.py — ComponentList, lazy per-sheet polars DataFrames
        v
conversion-config.yaml  ──drives──>  conversion.py — LongListConverter
        |                                 (row skips/edits, marker insertion,
        |                                  extras, conversion-time rematching)
        v
writer.py — PythonSubsequenceWriter  (introspects each element's __init__, writes
        |                             only non-default kwargs, then runs ruff on the output)
        v
src/euxfel/subsequences/{i1,l1,l2,l3,cl,sase1,...}.py   +  __init__.py
        |
        v
sequences.py — flattens ordered subsequence lists into cathode_to_<target> cells
```

**`src/euxfel/subsequences/*.py` are generated artifacts. Never hand-edit them.**
Every change belongs in `src/euxfel/longlists/conversion-config.yaml` (a symlink
to the dated config for the current component list), followed by `euxfel convert`.
`docs-site/docs/conversion.md` documents every config section — read it before
touching the YAML.

### Two layers, easily confused

- **Static lattice** (`subsequences/`, `sequences.py`): geometry and design
  optics only. Pure Ocelot element objects plus a `cell` tuple and a `twiss0`.
- **Tracking model** (`sections.py`): one `SectionTrack` subclass per s2e section
  (`A1`, `AH1`, `LH`, `BC0`, `L1`, ... `SASE1`, `T4D`). Each slices a subsequence
  `cell` between two markers and attaches physics processes (space charge, CSR,
  wakes from `src/euxfel/wakes/`, laser heater, apertures). Global tracking
  constants (`Sig_Z`, `SCmesh`, `CSRBin`, `SmoothPar`) live at the top of
  `sections.py` and apply to every s2e script.

A section boundary can only exist where a marker exists. Markers such as
`ocelot_start`, `a1_sim_stop`, `lh_start` are **not** in the component list — they
are injected by the YAML's `new_markers` block. So adding or moving a
physics-process boundary means: edit the YAML, re-run `euxfel convert`, then use
the new marker in `sections.py`.

### Element naming

`PythonSubsequenceWriter.make_var_names` lowercases the component-list ID and maps
`. : - '` to `_`, prefixing the class initial when the name starts with a digit.
`C.A1.1.1.I1` becomes `i1.c_a1_1_1_i1`. This is why `sections.py` is full of
opaque identifiers — they are mechanical transforms of real tunnel component names.

### Things that must be kept in sync by hand

- `sequences.py`'s `*_SUBSEQUENCES` lists duplicate the `targets:` mapping in the
  conversion YAML. The converter does not generate `sequences.py`; update both.
- The package version encodes the component list date
  (`0.3.0+componentlist.20260121`). Converting from a new spreadsheet means a new
  dated `.xls`, a new dated config, a re-pointed `conversion-config.yaml` symlink,
  and a version bump. Lattice versions are released as git tags
  (`<api-version>+componentlist.<date>`); API changes are meant to be independent
  of lattice changes.

### Import degradation is deliberate

`euxfel/__init__.py`, `subsequences/__init__.py` and `sequences.py` each wrap
their imports in `try/except Exception` and downgrade failures to a warning, so a
broken or half-written conversion still leaves an importable package. A missing
`euxfel.subsequences.l3` therefore surfaces as an `AttributeError` far from the
real cause — check for the conversion warning first.

### Special cases the component list can't express

- **XY-quadrupoles** are absent from the spreadsheet and are inserted via
  `new_elements` as a `SlicedElement` (`slicing.py`): a named dict of elements plus
  a restricted arithmetic expression like `"(19 * [xslice1982] + [yslice1982]) * 10"`,
  evaluated through a whitelisted AST walker (`+` and `*` only).
- **Closed undulators / rotated TDS** come from the YAML `extras` block, and
  because a closed undulator changes the focusing, the affected section declares a
  `matching:` block so the converter re-matches quadrupole strengths at conversion
  time and writes the corrected `twiss0`.
- RBend `e1`/`e2` are rewritten as `value - angle/2` on the way out
  (`writer.rbend_to_string`) — the component list and Ocelot disagree on the convention.

## Running s2e simulations

Scripts in `s2e_scripts/` hardcode `data_dir = "../beam_files/"`, so they must be
run from inside that directory (`cd s2e_scripts && python s2e_up_to_SA1.py`). Each
builds an `all_sections` list, a `tws0`, RF settings derived from beam parameters
via `beam2rf`/`beam2rf_xfel_linac`, and a `config` dict of per-section toggles
(`match`, `SC`, `CSR`, `wake`, `smooth`). These are full tracking runs — long, and
they write intermediate `.npz` beams back into `beam_files/`. Don't launch one
casually to check a change; prefer `euxfel plot`/`compare` or the tests.

## Tests

`tests/test_subsequences.py` is the load-bearing one: it tracks design optics
through each subsequence and asserts the resulting Twiss matches the *next*
subsequence's stored `twiss0`, catching discontinuities at module boundaries after
a conversion. `test_writer.py` covers the element-to-source round trip;
`test_sections.py` checks section names and step sizes.
