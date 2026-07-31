# Ocelot against MAD-8

MAD-8 is the upstream authority this lattice is derived from, and the intent is
to retire it. That is only defensible if we can say precisely where the two
models agree and where they do not. This page records the measurements.

Everything here was produced against the MAD-8 tapes archived in
`src/euxfel/mad8/2026.01.22/tapes/`, and is reproducible from
`tests/test_mad8_names.py` and `tests/test_mad8_optics.py`.

## Summary

| what | agreement |
|---|---|
| Geometry, element by element | **3e-6 m** over 3.1 km — the tape's own print floor |
| Optics, cathode to dump, every element | beta **~1e-4** relative; dispersion **1e-9 – 1e-6 m** |
| Per-element transfer maps, all types except cavities | **≤ 2e-6** |
| Per-element transfer maps, on-crest cavities | **5e-9** |
| Per-element transfer maps, off-crest cavities | **3.0e-5** |

**There is exactly one physics disagreement between Ocelot and MAD-8 on this
lattice: the transverse map of an off-crest accelerating cavity.** Everything
else agrees to numerical precision or to the precision the tape is printed at.

## The three comparisons, and why all three are needed

**1. Geometry.** Build the sequence from the SURVEY tape, survey it, compare
element for element. Agreement is 3e-6 m, which is not our error: the tape prints
coordinates as `E16.9`, ten significant figures, so at Z ~ 3000 m its own
positions are quantised at ~3e-6 m. Measured directly, the tape disagrees with
*itself* — its printed straight-element lengths against its own coordinates — by
up to 9.9e-7 m. Nothing built from it can close better.

**2. Whole path optics.** Track cathode to dump in one pass, seeded only from the
tape's `INITIAL` row, and compare all ~9000 elements. Nothing is re-seeded along
the way, so any disagreement is carried to the end.

This matters because the weaker version is misleading. `tests/test_mad8_convert.py`
checks optics continuity across the 23 module boundaries, but each module there
starts from MAD-8's own numbers, so errors cannot accumulate. That test catches a
mis-sliced boundary and almost nothing else.

**3. Per-element transfer maps.** Propagate each element *alone* from the tape's
own upstream values. This localises a disagreement to the element responsible
rather than reporting one number for 3 km of machine, and it is the only one of
the three that identified the cause.

Measured on B1D and B2D:

```
('Cavity',     'LCAV')   n=  784   max=3.04e-05   <- the only real disagreement
('Undulator',  'MATR')   n=    2   max=2.56e-06
('Drift',      'DRIF')   n= 5739   max=4.75e-07
('SBend',      'SBEN')   n=   81   max=3.23e-07
('Quadrupole', 'QUAD')   n=  381   max=4.21e-09
('Undulator',  'DRIF')   n=   61   max=9.54e-10
('Vcor',       'VKIC')   n=  285   max=9.18e-10
('Hcor',       'HKIC')   n=  362   max=7.46e-10
```

## The cavity difference

It is confined to cavities that run off crest, and it decays with energy:

| cavity | phase | E in | Ocelot vs tape |
|---|---:|---:|---:|
| `C.A1.1.1.I1` | 0° | 0.0050 GeV | 5.2e-09 |
| `C.A1.1.8.I1` | 0° | 0.1319 GeV | 1.9e-09 |
| `C.A2.1.1.L1` | 25° | 0.1300 GeV | **3.04e-05** |
| `C.A2.1.2.L1` | 25° | 0.1494 GeV | 2.00e-05 |
| `C.A2.1.3.L1` | 25° | 0.1689 GeV | 1.39e-05 |
| `C.A2.2.4.L1` | 25° | 0.3410 GeV | 1.61e-06 |

On-crest cavities at the *same energies* agree to 5e-9, so it is the phase that
separates the two models, not the energy.

### Why

MAD-8's `tmlcav` builds a TRANSPORT matrix with thin edge lenses
(`mad8.ss`, `subroutine tmlcav`):

```fortran
re(1,2) = el * (ener1/denergy) * log(one + denergy/ener1)
re(2,2) = ener1 / (ener1 + denergy)
re(4,4) = ener1 / (ener1 + denergy)
if (dodefl) then
   rw(2,1) = -denergy / el / two / en0                  ! entrance edge
   rw(2,1) = +denergy / el / two / (en0 + denergy)      ! exit edge
```

**None of those terms depends on the RF phase.** `phirf` enters only through the
energy gain, `denergy = vrf * cos(phirf)`.

Ocelot uses the Rosenzweig-Serafini matrix
(`ocelot/cpbd/elements/cavity_atom.py`), in which the phase appears explicitly,
both in `alpha` and in all four transverse terms:

```python
alpha = np.sqrt(eta / 8.) / cos_phi * np.log(Ef / Ei)
r11 = cos_alpha - np.sqrt(2. / eta) * cos_phi * sin_alpha
r12 = np.sqrt(8. / eta) * Ei / Ep * cos_phi * sin_alpha
r21 = -Ep / Ef * (cos_phi / np.sqrt(2. * eta)
                  + np.sqrt(eta / 8.) / cos_phi) * sin_alpha
r22 = Ei / Ef * (cos_alpha + np.sqrt(2. / eta) * cos_phi * sin_alpha)
```

That is precisely the observed signature: the two agree where `cos_phi = 1` and
part company as the phase moves off crest.

Rosenzweig-Serafini is the standard treatment of phase-dependent RF focusing, so
on the face of it Ocelot's is the more complete model. **This page does not
settle which is preferable** — that is a physics decision, and the version
caveat below has to be resolved first.

### Open: we have not read the source that made these tapes

The tapes were produced by **MAD-8 8.51.18**. What is available is not that:

- `~/repos/mad8/files/madpackage_SLAC.tgz` contains **8.51/15s**, the SLAC
  baseline. This is where the `tmlcav` listing above comes from.
- `~/repos/mad8/files/mad8.ss_mad8.51.16wd_.patch` is W. Decking's patch for
  **8.51/16**, adding an exact Rosenzweig-Serafini matrix.
- `ReadMe_DESY.txt` records a further change in **8.51.17** by M. Vogt:
  *"Modified OPTICS command (twopsv, twoptc) to use LACAV properly; Modified
  tmlcav routine."*

So there are two `tmlcav` revisions between the source we can read and the binary
that produced the tapes.

The 8.51/16 patch is demonstrably **not** what built them. Transcribing its
formula and propagating the tape's own Twiss through it reproduces the tape's
next row to only 3.5e-1 on-crest, against Ocelot's 5.2e-9. Either it sits inside
an uncompiled `+if desy` block, or 8.51.17 replaced it.

**To close this we need `tmlcav` from 8.51.18.** It is a single subroutine.
Until then the empirical statement stands on its own — Ocelot reproduces the tape
to 5e-9 on crest and 3e-5 off it, and the cavity is the only element type that
disagrees at all — but the *mechanism* above is inferred from a version we know
is not the one used.

## What this costs in practice

Nothing that matters for design work, but it is worth knowing where it surfaces.

The per-cavity 3e-5 accumulates through L1 into a betatron mismatch of ~1e-4,
which then persists. At a dump it looks much larger than it is:

```
T4D dump ENSEC.3106.T4D
  tracked from the cathode     : beta_y 200449.228 vs 200303.286   rel 7.29e-04
  re-seeded at MATCH.2813.SA3  : beta_y 200303.267                 rel 9.64e-08

T5D dump ENSEC.3189.T5D
  tracked from the cathode     : beta_x 201118.253 vs 201097.630   rel 1.03e-04
  re-seeded at MATCH.2197.SA2  : beta_x 201097.632                 rel 9.99e-09
```

Given MAD-8's own Twiss at the last match point, the final ~300 m including the
dump line reproduces MAD-8 to **1e-8**. The dump optics are not wrong; the
mismatch arrives there.

It looks dramatic because beta at a dump is ~200 km — the beam is in a long drift
past the last quadrupole. A mismatch does not grow, but a small error in alpha
shifts the waist longitudinally, and 300 m of drift turns that into a large
beta. 146 m in 200 449 m is 0.07%. The same mismatch lands at different betatron
phases in the two planes, which is why x and y differ so much (2.0e-5 against
7.3e-4) at the same point.

Dispersion at the dumps is the same illusion in reverse. T5D's dump `Dx` is
-0.000679 against MAD-8's -0.000439, which reads as 55% but is **0.24 mm**, next
to a zero crossing. T4D's dump `Dx` agrees exactly at 0.000181.

## Things that are *not* disagreements

Recorded because each cost time to establish, and each looks like a bug until
measured.

**Bend arc lengths.** The tape prints `L` as `F12.6` but coordinates as `E16.9`,
and a bend's length is computed rather than declared — `XFEL_I1.txm:489` has
`arc_lh = LEN_BL*ang_lh/sin(ang_lh)`, giving 0.2003302835 m printed as
`0.200330`. That 1.4e-6 relative truncation puts `BL.1.1.I1`'s exit 283 nm short,
and every element downstream inherits it. `mad8_import` recovers each bend's arc
length from the survey chord instead. Drifts are deliberately left alone: their
lengths are literals in the MAD-8 source, so the printed value *is* the
definition and the surveyed chord only adds round-off. Recovering those made the
geometry worse.

**SASE undulator focusing.** All 63 undulators in T4D carry `Kx = 0` and so act
as drifts. This is not a defect for the purpose of matching MAD-8: 61 of them are
plain `DRIF` records in MAD-8, which is also a drift, and they agree to 9.5e-10.
Only 2 are `MATR`, at 2.6e-6. `Kx` cannot come from the tape in any case — MAD-8
has no undulator element and K is a gap setting rather than lattice geometry.

**Angle conventions.** MAD-8 and the component list do not use the same one.
`makelist_release.m:210-212` swaps `THETA` and `PHI` on read, and its `fprintf`
negates `PHI` again on the way out:

```
sheet.THETA = tape.PHI     sheet.PHI = -tape.THETA     sheet.CHI = tape.PSI
```

The model holds **MAD-8's** convention, because MAD-8 is what it is built from
and checked against. The transformation belongs in the longlist writer, on the
way out, and nowhere else.

**T5D dispersion.** Was wrong, and is now fixed upstream. The T5D twiss command
carried a `couple` flag (`Run_South_2025.txm:260`) that no other path had; it
scaled that path's dispersion by `E/E_ref`, leaving `DX` a factor 26 low against
every other path across the shared injector. W. Decking re-ran the south branch
without it. See `ReadMe_DESY.txt` in the release directory.

## Reproducing this

```bash
pytest tests/test_mad8_optics.py     # levels 2 and 3
pytest tests/test_mad8_names.py      # geometry and name generation

euxfel compare b1d --show mad8,ocelot-mad8 --plane x
euxfel compare t4d --show all
```

`euxfel compare` prints, after each plot, one table of optics and one of survey
at every fixed match point and at the dump, one row per (point, source). Four
sources are selectable and each pairing isolates one thing:

| pair | isolates |
|---|---|
| `mad8` vs `ocelot-mad8` | Ocelot's physics — same lattice, different code |
| `ocelot-mad8` vs `ocelot-longlist` | what the spreadsheet lost — same code, different input |
| `mad8` vs `longlist` | `makelist_release.m` itself |
