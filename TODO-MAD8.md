# TODO — MAD-8 as the source of truth

## Where we are

`euxfel convert-mad8` builds the Ocelot model from the archived MAD-8 SURVEY
tapes. It is verified against MAD-8 itself:

| | |
|---|---|
| Geometry, element by element | 3e-6 m over 3.1 km — the tape's own print floor |
| `NAME1` regeneration | exact on all seven sheets |
| Optics, cathode→dump, every element | beta ~1e-4, dispersion 1e-9–1e-6 m |
| Per-element transfer maps | ≤2e-6 except off-crest cavities at 3e-5 |
| Elements dropped | none |

The conversion is **literal**: one element per tape record, in tape order, with
the tape's numbers. Nothing injected, nothing dropped. `tests/test_mad8_convert.py`
pins that.

What blocks the cutover: `sections.py` slices physics processes at markers that
MAD-8 does not have, so it cannot slice the converted modules.
`src/euxfel/subsequences/` is still generated from the component list.

## Decisions

1. **Anchor on MAD-8's own elements, not injected markers.**
2. **Tracking starts at `STAC.26.I1`**, not at 3.2 m. This replaces the last
   bare-position anchor with a real element and makes the handover point a
   lattice fact.
3. **The Ocelot → component list converter is wanted but not urgent.**
   `longlist_writer.ComponentListWriter` exists and round-trips `I1toG1D`.

### What decision 2 costs

`STAC.26.I1` is at s = 3.2996, **99.6 mm downstream** of the present 3.2 m. The
ASTRA distribution is defined at 3.2 m, so either it is drifted 99.6 mm on load,
or ASTRA is re-run to the new point. Space charge over 99.6 mm at 5 MeV is not
nothing; drifting the distribution is an approximation, re-running is not. Decide
which before relying on the results.

## Work

### 1. Replace the "before" anchors — exact, no cost

Nine injected markers sit *before* a named element. Ocelot resolves `start=` and
`stop=` to an element's **entrance**, so the marker and the element it precedes
are the same point. Replace directly in `sections.py`:

| marker | becomes |
|---|---|
| `lh_start` | `U74.49.I1` |
| `i1_tds_start` | `TDSA.52.I1` |
| `dogleg_start` | `CIX.65.I1` |
| `dogleg_stop_bc0_start` | `STLAT.96.I1` |
| `bc0_stop_l1_start` | `QI.103.I1` |
| `l1_stop_bc1_start` | `STLAT.182.B1` |
| `l2_stop_bc2_start` | `STLAT.393.B2` |
| `stop_l3` | `CFY.1651.L3` |
| `t3_csr_stop` | `QH.2569.T3` |

Keep readability with a local variable, which `sections.py` already does
elsewhere (`bc0_stop = l1.enlat_101_i1`):

```python
lh_start = i1.u74_49_i1
```

### 2. The "after" anchors need a helper — this is the awkward part

Ten markers sit *after* an element, and **none has a zero-length MAD-8 marker
following it**. Measured on the tape-built model:

```
a1_sim_stop        after C.A1.1.8.I1  -> next is D02043  (drift, 204 mm)
lh_stop            after U74.49.I1    -> next is D0041   (drift,  41 mm)
i1_tds_stop        after TDSA.52.I1   -> next is D005115 (drift,  51 mm)
bc1_stop_l2_start  after TORA.203.B1  -> next is D01542  (drift, 154 mm)
t4_csr_stop        after BPMA.2606.T4 -> next is D0100   (drift, 100 mm)
... 5 more, all drifts
```

So naming the next *named* element moves the boundary by 41–204 mm. The exact
replacement is the drift immediately following, whose entrance is precisely the
reference element's exit — but drift names repeat (`D0100` occurs hundreds of
times), so it has no stable name to write in `sections.py`.

**Resolve it with a lookup rather than a name.** A helper returning the pair that
covers exactly one element:

```python
def span(lattice, element):
    """(element, the one after it) -- covers exactly `element`."""
    for index, candidate in enumerate(lattice.sequence):
        if candidate is element:
            return element, lattice.sequence[index + 1]
    raise ValueError(...)
```

```python
self.add_physics_process(lh, *span(self.lattice, i1.u74_49_i1))
```

Measured equivalent to the marker (`start=U, stop=NEXT` and `start=U, stop=MARKER`
both give span 1.0; `start=U, stop=U` gives 0.0 and is *not* the same thing —
`sections.py:189` uses a zero span deliberately for a point-like process).

This only works because every element is now a distinct object (`1d914c0`):
`navi._find_unique_index` matches anchors by identity and raises on a repeat, so
a shared drift here would fail.

Where a process spans several elements rather than one, name the endpoints
directly; `span` is for the single-element case.

### 3. Tracking start at `STAC.26.I1`

Replace `ocelot_start` / `astra_stop` in `sections.py` with `i1.stac_26_i1`, and
settle the 99.6 mm question above. `s2e_scripts/` load the ASTRA distribution;
those need the same treatment.

### 4. Delete the marker declarations

Once 1–3 are done, `new_markers` in
`src/euxfel/longlists/conversion-config-2026.02.13.yaml` should be empty for
every section. Removing it is the check that nothing still depends on an
injected marker.

### 5. Cut over

Point `convert-mad8` at `src/euxfel/subsequences/`.
`tests/test_subsequences.py` (Twiss continuity) and `tests/test_sections.py`
(s2e slicing) are the acceptance gates and already exist.

### 6. Carry `extras` and `matching`

Still needed, still not designed. `extras` sets what MAD-8 cannot express
(`U74.49.I1` `Kx = 1.294`, the rotated TDS); `matching` re-matches injector
quadrupoles and writes a corrected `twiss0`, which collides with taking `twiss0`
from the TWISS tape — a section that re-matches must own its `twiss0`.

**Neither belongs inside the converter.** Keeping it literal is what lets
`tests/test_mad8_optics.py` hold the model to MAD-8 at the measurement floor.

### 7. Correct the TDS frequency — MAD-8 says 2800 MHz, the machine is 2998

The tape carries `FREQ = 2800.0` for `TDSA.I1` and `TDSB.B1`, and both converters
reproduce it faithfully, so the committed subsequences are wrong too:

```
src/euxfel/subsequences/i1.py:200  tdsa_52_i1  = TDCavity(l=0.7, freq=2800000000.0, ...)
src/euxfel/subsequences/l1.py:531  tdsb_208_b1 = TDCavity(l=1.5, freq=2800000000.0, ...)
src/euxfel/subsequences/l2.py:500  tdsb_428_b2 = TDCavity(l=1.5, freq=2800000000.0, ...)
```

The spreadsheet is not the origin — MAD-8 is.

**Not a one-line constant change.** `TDS_FREQUENCY_MHZ = 2800.0` in
`mad8_import.py` does two jobs: it *identifies* a TDS among the `LCAV` records
(`kind = TDCavity if record["FREQ"] == TDS_FREQUENCY_MHZ else Cavity`) and it is
the value written. Setting it to 2998 stops TDS cavities being recognised, and
they silently become ordinary `Cavity` objects. Detection must stay on the tape's
2800; only the written value changes.

Put it in a declared `tape_corrections:` block in
`src/euxfel/mad8/<release>/mad8-config.yaml`, not a hardcoded constant. This is
the same category as the bend arc-length recovery already in `_lengths_from_survey`
— the tape's printed value is wrong and we override it — and that precedent
should be followed visibly rather than buried.

`conversion.py:1351` (`row["E2/FREQ"] * 1000000`) needs the same treatment for
the longlist route.

**Confirmed:** all three structures are 2998 MHz — `TDSA.52.I1` (0.7 m) and both
`TDSB` (1.5 m). One correction covers them, so it can key on the tape's 2800 for
every `LCAV` at that frequency rather than needing a per-element table.

**Confirmed latent**, which is why it survived: every TDS still has `v = 0.0`, so
frequency affects nothing until `SectionTrack.update_tds` is called. The change
is therefore safe — no current result moves — but it does change the streak
calibration for anyone who turns a TDS on, which is the point of making it.

Because nothing observable changes, no existing test will catch a mistake here.
Add one asserting the built `TDCavity` objects carry 2.998e9 and that they are
still `TDCavity` rather than `Cavity` — the second is the failure mode that would
otherwise pass silently.

## Also outstanding

Ordered by how much they would cost to leave.

- **`longlist_writer._bend_rows` is wrong.** It uses the same survey point for
  the magnet row and `BENDARC`; they differ by the sagitta — the magnet is the
  chord midpoint, `BENDARC` the arc midpoint. G1D has no bends, so the round-trip
  test cannot see it. This will corrupt every bend in a regenerated sheet.
- **CSR at the injector dump starts on the dipole entry face.** `5a979c0` applied
  a CSR process that had been built and never added, so `BB.62.I1D` had none at
  all. It cannot be given a lead-in without moving the LH/DL/I1D boundary, and
  whether it is needed at all is unmeasured. A with/without test bed would
  settle it; the per-section `CSR` toggle already exists in the s2e `config`, and
  `beam_files/compare_parrays.py` already compares particle arrays, but
  `beam_files/` holds no `.npz` so the injector must run once first.
- **The off-crest cavity discrepancy** — 3e-5 per cavity, the only physics
  disagreement with MAD-8. Blocked on `tmlcav` from MAD-8 **8.51.18**; the source
  available is 8.51/15s, two revisions earlier, so the mechanism in
  `docs-site/docs/mad8-comparison.md` is inferred rather than confirmed.
- **The comparison tables have no test**, despite catching a sign error on their
  first run.
- **Match-point rule 4 is unreconciled.** N. Golubeva's sketch fixes "the FODO in
  T4 and T2", but no T2/T4 point is in `FIXED_MATCH_POINTS`. See
  `docs-site/docs/matchpoints.md`.
- **The ±0.1 match tolerance is not implemented**, only documented.
- **`rows.skip` and `ROWS_ABSENT_FROM_OCELOT`** declare the same fact twice.
- **Movers**: 111 `CMVQA` are dropped as zero-length rows inside their host
  quadrupole. The two `CMVQI` survive by luck of landing on a face.
- **Still to request from DESY**: `tmlcav` from 8.51.18; `Rooms.xlsx` (five
  columns `NAME, Zmin, Zmax, BRANCH, PBRANCH`); the helper `.m` files
  (`read_survey_raw`, `bendmidtrans`, `rotation3d`, `LAtoPD`, `nameparser`);
  T6–T10 tapes when the `LONGLIST` sheet is wanted.

## Not doing

- **The longlist → Ocelot converter stays**, deliberately lossy, as a consistency
  check. It is not a second source of truth and should not grow toward one.
- **A separate "design" and "real" model.** One lattice; anything beyond MAD-8 is
  applied on top, downstream of the converter.

## Verification

```bash
pytest                                    # 212 at time of writing
euxfel convert-mad8 --outdir /tmp/check   # 24 modules, import and track
euxfel compare b1d --show mad8,ocelot-mad8 --plane x
```

The invariant the whole arrangement protects: the converted model reproduces
MAD-8 at the tolerances above. Any step that loosens them has introduced
something that does not belong in the converter.
