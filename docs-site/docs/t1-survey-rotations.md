# The T1 survey rotations

There are four zero-length coordinate rotations on the SASE2 branch that exist
in MAD-8 but have no representation in the Component List. Until they were
modelled explicitly, our SASE2 line was rolled by 9.769 µrad and the T5D dump
landed 2.3 mm away from where both MAD-8 and the spreadsheet's own coordinates
put it.

They are also the reason `BZ.2030.T1` is the one bend in 134 whose `BENDIN` and
`BENDOUT` marker rows contradict each other — the anomaly that started this
investigation.

Everything below is checkable against files in this repository:

| what | where |
|---|---|
| MAD-8 lattice source | `src/euxfel/mad8/2026.01.22/mad8_input/*.txm` |
| MAD-8 survey output | `src/euxfel/mad8/2026.01.22/tapes/SURVEY_T5D.gz` |
| DESY's spreadsheet generator | `src/euxfel/mad8/2026.01.22/makelist_release.m` |
| Component List | `src/euxfel/longlists/component_list_2026.02.13.xls`, sheet `I1toT5D` |
| our model | `src/euxfel/rotations.py`, `src/euxfel/subsequences/t1.py` |

---

## 1. What MAD-8 does

The three T1 rotations are declared in the *run* file, not the lattice file:

**`Run_South_2025.txm:305-314`**

```
!--- Nov 2016: New RotSystemTD1
az1  = -0.00440392786446921;
ay   = +9.27121409529346e-08;
az2  = +0.00441369699554469;

Rot.Z1.T1: Srot, angle = az1;
Rot.Y.T1:  Yrot, angle =  ay;
Rot.Z2.T1: Srot, angle = az2;

RotSystemTD1: Line = (Rot.Z1.T1, Rot.Y.T1, Rot.Z2.T1);
```

and a fourth at the SASE2 entrance:

**`Run_South_2025.txm:318`**

```
Rot.Y.Sa2:  Yrot, angle = -2.365095999996847e-06;   ! if RotSytemTD1 is used
```

The roll–pitch–roll sandwich is the usual way to pitch about an axis that is
not the local vertical: roll into a convenient frame, apply the pitch, roll
back. But `az1` and `az2` do **not** cancel:

```
az1 + az2 = -0.00440392786446921 + 0.00441369699554469
          = +9.76913107548e-06 rad
```

That residual roll is deliberate. It is a geometry patch fitting the design
lattice to the as-built XTD1 tunnel — the same family as the hand-tuned
"magical drifts" a few lines away in `XFEL_South_2025.txm:262-271`, and the
`D4750C: Drift, L = 4.750 - 1.4e-5;` at `XFEL_South_2025.txm:271`. The header
comment dates the current values to a survey refit in November 2016.

### They apply to SURVEY only

This is the crux. There are two versions of the T1 line:

**`Run_South_2025.txm:322`** — used for `SURVEY`

```
T1_survey: Line = (RotSystemTD1, T1M, T1D, ENSEC.T1.T1);
```

**`XFEL_South_2025.txm:401`** — used for `TWISS`

```
T1:  Line = (T1M, T1D, ENSEC.T1.T1);
```

and the top-level lines that select between them, **`Run_South_2025.txm:346`**:

```
I1TT5D_sur:      LINE = (I1, L1, B1, L2, B2, L3, CL,        &
                        CLtoSouth, T1_survey, SA2_survey,   &
```

So the rotations move where the beamline *points* without touching the optics.
That is exactly right for MAD-8, and it is why they are easy to lose: nothing
in the optics ever notices them.

`RotSystemTD1` is prepended to `T1M`, whose first element is the first untilted
septum (**`XFEL_South_2025.txm:274`**):

```
T1M: Line = (BZ.2.T1, D0500, BZ.2.T1, D0500, BZ.2.T1, D4750C,     &   ! three untilted septa
```

So the rotations sit **immediately before `BZ.2.T1`** — which
`makelist_release.m` renames `BZ.2030.T1`.

---

## 2. What the survey tape shows

`SURVEY_T5D`, records 6768–6772 (file lines 27075, 27079, 27083, 27087, 27091 —
a SURVEY record is 4 lines, starting after a 2-line header):

| rec | line | KEYWORD | NAME | L | SUML | PSI (roll) |
|---:|---:|---|---|---:|---:|---:|
| 6768 | 27075 | `DRIF` | `D0500` | 0.5 | 2006.685850 | **−7.479365e−06** |
| 6769 | 27079 | `SROT` | `ROT.Z1.T1` | 0.0 | 2006.685850 | −4.411407230e−03 |
| 6770 | 27083 | `YROT` | `ROT.Y.T1` | 0.0 | 2006.685850 | −4.411407264e−03 |
| 6771 | 27087 | `SROT` | `ROT.Z2.T1` | 0.0 | 2006.685850 | **+2.289732e−06** |
| 6772 | 27091 | `SBEN` | `BZ.2.T1` | 1.000005 | 2007.685855 | +4.297838e−06 |

Read the roll column:

```
-7.479365e-06  +  az1  =  -4.411407230e-03     (SROT adds its angle straight to PSI)
-4.411407230e-03 + (tiny YROT effect) = -4.411407264e-03
-4.411407264e-03 + az2 = +2.289732e-06

net across the three:  +2.289732e-06 - (-7.479365e-06) = +9.769097e-06
```

All three happen at the same `SUML` — they have no length. They change
orientation, not position.

---

## 3. What the spreadsheet lost

**`makelist_release.m:56`**

```matlab
layout = layout(strncmp('ROT',{layout.NAME},3)==0);
```

Every row whose name begins `ROT` is deleted, and this happens *before* the
bend markers are inserted at `makelist_release.m:235`:

```matlab
list = [list(1:j-1) list(j-1) list(j) list(j) list(j) list(j:end)];
```

That line duplicates rows to build the five-row bend block. `BENDIN` is
`list(j-1)` — a copy of **the row before the bend**. But the rotations are
already gone, so "the row before the bend" is no longer `ROT.Z2.T1`; it is
`D0500`, from *before* the rotations. `BENDOUT` is the original bend row, from
*after* them.

The deleted rotation therefore reappears as a gap between two marker rows that
are supposed to be consistent with each other.

### Seen in the spreadsheet

Sheet `I1toT5D`, Excel rows 2487 and 2491 (angles are in the Component List's
own convention: `THETA` = MAD-8 `PHI`, `PHI` = −MAD-8 `THETA`, `CHI` = MAD-8
`PSI`, per `makelist_release.m:206-207`):

| Excel row | NAME1 | NAME2 | CLASS | X | Z | CHI |
|---:|---|---|---|---:|---:|---:|
| 2487 | `MBZ.2030a.T1` | `MBZ.2.T1` | `BENDIN` | 0.023411 | 2029.555358 | **−7.479e−06** |
| 2488 | `BZ.2030.T1` | `BZ.2.T1` | `SBEN` | — | — | 0.0 |
| 2489 | `MBZ.2030b.T1` | `MBZ.2.T1` | `BENDSTR` | 0.026488 | 2030.055352 | +4.298e−06 |
| 2490 | `MBZ.2030c.T1` | `MBZ.2.T1` | `BENDARC` | 0.027176 | 2030.055346 | −6.475e−06 |
| 2491 | `MBZ.2030d.T1` | `MBZ.2.T1` | `BENDOUT` | 0.032315 | 2030.555322 | **+4.298e−06** |

Row 2487's `X` and `CHI` are record **6768**'s (`D0500`, pre-rotation) and row
2491's are record **6772**'s (`BZ.2.T1`, post-rotation). The three records in
between are simply absent.

Propagating a bend of angle −5.500028 mrad from row 2487 gives an exit roll of
−5.471e−06, not the +4.298e−06 on row 2491. The difference is 9.769 µrad.

### Why only this bend

`BZ.2025.T1` (Excel rows 2482–2486) is the *tilted* septum, defined at
**`XFEL_South_2025.txm:170`**:

```
BZ.1.T1: Sbend, L  = ARC_BZ_T1, ANGLE = ANG_BZ_T1,  &
                E1 = 0, E2 = ANG_BZ_T1,             &
                TILT = TILT_BZ1_T1;
```

It lives at the end of `TL3T1` (**`XFEL_TL.txm:507`**), upstream of
`RotSystemTD1`, so no rotation falls inside its marker block and it
round-trips perfectly. Of the 134 bends in the machine, `BZ.2030.T1` is the
only one that straddles a rotation — hence exactly one failure.

---

## 4. Sketch

Arc length runs left to right. Everything in the `2006.68585` column is
zero-length and happens at one point.

```
        s = 2006.185850        s = 2006.685850                    s = 2007.685855
              |                       |                                  |
  MAD-8       |        D0500          |  Z1   Y   Z2                     |
  SURVEY  ----+-----------------------+---#---#---#--[   BZ.2.T1    ]----+---->
  tape        |                       |   |   |   |                      |
  rec       6767                    6768  |6769|6770|6771              6772
              |                       |   |   |   |                      |
  PSI    -7.479e-06            -7.479e-06 |   |   |  +2.290e-06    +4.298e-06
                                          |   |   |
                                       SROT YROT SROT
                                        az1  ay   az2
                                          \_________/
                                               |
                                     net roll +9.769 urad
                                     zero length, survey line only


  makelist_release.m:56 deletes the three ROT rows
                    |
                    v

  Component  ----+-----------------------+---------------[  BZ.2030.T1  ]----+---->
  List       (row 2486)              row 2487                              row 2491
  I1toT5D                             BENDIN                                BENDOUT
                                    copy of rec 6768                     = rec 6772
                                    CHI = -7.479e-06                   CHI = +4.298e-06
                                          |                                  |
                                          +-------- must be consistent ------+
                                                 but differ by 9.769 urad
                                                 (the deleted rotation)
```

And in plan view, hugely exaggerated — the roll tips the whole downstream
branch about the beam axis:

```
                                    ROT block
                                        |
   CL / TL ------------------ BZ.2025 --+-- BZ.2030 -- BZ.2031 -- ... -- SA2 -- T5 -- T5D
   (rolled frame carried all the way)   |                                              |
                                        |                                              |
                              +9.769 urad roll                                    2.3 mm
                              applied once here                                displacement
                                                                              at the dump

   Without the ROT block the branch is rolled by -9.769 urad relative to MAD-8, and the
   error is *never corrected* downstream -- every subsequent element inherits the frame.
```

---

## 5. What we do about it

`src/euxfel/rotations.py` defines `SRot` and `YRot`, subclassing Ocelot's
`Marker` so the transfer map stays the identity — these change where the
beamline points, not what happens to the beam. Ocelot itself is a pinned
dependency and is not modified.

They are inserted by the conversion config
(`src/euxfel/longlists/conversion-config-2026.02.13.yaml`), since the
Component List cannot supply them:

```yaml
      ROT.Z1.T1:
        position: { reference: MBZ.2030a.T1, adjacent: before }
        type: SRot
        angle: -0.00440392786446921
```

with `ROT.Y.T1` and `ROT.Z2.T1` following, and `ROT.Y.SA2` placed after
`STSEC.2197.SA2` in the `SASE2` section.

!!! note "The YROT sign"

    `YRot`'s rotation matrix is the **opposite** sense to the `theta0` seed
    matrix Ocelot's own `survey()` builds. This was measured against the tape,
    not derived: taking the seed's sense left `THETA` wrong by exactly `2·ay`.

### Result

`tests/test_mad8_survey.py` compares every dump path against its MAD-8 tape at
each arc length present in both.

| target | before | after |
|---|---:|---:|
| I1D, B1D, B2D, TLD, T4D | ≤ 9.5e−07 m | unchanged |
| **T5D** | **2.29e−03 m, 9.92e−06 rad** | **9.3e−07 m, 2.0e−10 rad** |

Against the Component List's own surveyed match points, `MATCH.2197.SA2` and
the T5D dump now agree to under a micron and a nanoradian, having been 2.3 mm
and 9.8 µrad out.

### What stays broken

`BZ.2030.T1` remains in `KNOWN_INCONSISTENT_BENDS` in `tests/test_survey.py`.
That test audits the spreadsheet against *itself*, and the spreadsheet is still
missing the rotations — rows 2487 and 2491 will go on disagreeing until the
Component List gains some way of representing a coordinate rotation. Our model
no longer has the error; the source data still does.

This is worth raising with the Component List's maintainers. The concrete
suggestion would be to keep the `ROT` rows rather than filtering them at
`makelist_release.m:56` — they would need a `GROUP`/`CLASS` of their own, but
the spreadsheet would then be self-consistent and any downstream consumer could
reconstruct the geometry without reading the MAD-8 source.
