"""Round-trip a component-list sheet: spreadsheet -> Ocelot -> spreadsheet.

`euxfel convert` turns an `I1toXXX` sheet into a Python subsequence;
`ComponentListWriter` turns it back.  This checks the two are inverses, which is
the acceptance criterion for the repository becoming the source of truth rather
than a derived artefact: until the reverse direction reproduces the sheet, the
spreadsheet cannot be regenerated from here.

`I1toG1D` is the first sheet to pass.  At 28 rows it is small enough to check by
eye and still exercises the hard parts -- a 60 degree bend with its four
synthesised markers, a row at negative `S` that no sequence can hold, and the
`ST` state machine.

Where the two disagree and why:

- **Eighteen of the forty columns must match exactly**, including every text
  column and everything describing the component itself.
- **Geometry agrees to 1e-6**, which is the precision the spreadsheet stores
  `S`, `ST`, `X`, `Y` and `Z` to.
- **Optics agree to 1e-4**, from two effects that cannot be removed: the sheet
  keeps four decimals, and our Twiss differs from MAD-8's by about 1e-6
  relatively.  At `ENSUB.24.I1` the MAD-8 tape gives `BETX = 16.549946` and
  Ocelot `16.549960`; the sheet records `16.5499`.
"""

import polars as pl
import pytest

from ocelot.cpbd.magnetic_lattice import MagneticLattice

from euxfel import sequences
from euxfel.complist import ComponentList
from euxfel.conversion import written_s_offsets
from euxfel.longlist_writer import (
    COLUMNS,
    ROWS_ABSENT_FROM_OCELOT,
    ComponentListWriter,
)
from euxfel.subsequences import USED_COMPONENT_LIST

SHEET = "I1toG1D"
TARGET = "g1d"

#: Columns that must be reproduced bit for bit.
EXACT_COLUMNS = (
    "SECTION", "SUBSECTION", "CADRoom", "NAME1", "NAME2", "GROUP", "CLASS", "TYPE",
    "LENGTH", "STRENGTH", "E1/LAG", "E2/FREQ", "TILT", "S",
    "XPD", "YPD", "ZPD", "THETAPD", "PHIPD", "CHIPD",
    "ENERGY", "XAPER", "YAPER",
)  # fmt: skip

#: The spreadsheet stores these to six decimals.
GEOMETRY_COLUMNS = ("ST", "X", "Y", "Z", "THETA", "PHI", "CHI")
GEOMETRY_TOLERANCE = 1e-6

#: Four decimals in the sheet, plus our ~1e-6 relative difference from MAD-8.
OPTICS_COLUMNS = (
    "BETX", "ALFX", "MUX", "BETY", "ALFY", "MUY", "DX", "DPX", "DY", "DPY",
)  # fmt: skip
OPTICS_TOLERANCE = 1e-4


@pytest.fixture(scope="module")
def sheets() -> tuple[pl.DataFrame, pl.DataFrame]:
    """(the original sheet, the one we generate from the model)."""
    original = ComponentList(str(USED_COMPONENT_LIST)).get_sheet(SHEET)
    regenerated = ComponentListWriter(
        getattr(sequences, f"cathode_to_{TARGET}"),
        sequences.CATHODE_TWISS0,
        reinsert=ROWS_ABSENT_FROM_OCELOT[SHEET],
        previous=original,
    ).rows()
    return original, regenerated


def test_every_column_is_accounted_for() -> None:
    """No column may be silently skipped by the comparison below."""
    compared = set(EXACT_COLUMNS) | set(GEOMETRY_COLUMNS) | set(OPTICS_COLUMNS)
    assert compared == set(COLUMNS), (
        f"columns not compared: {set(COLUMNS) - compared}; "
        f"unknown columns compared: {compared - set(COLUMNS)}"
    )


def test_shape_and_column_order(sheets) -> None:
    original, regenerated = sheets
    assert regenerated.columns == original.columns
    assert regenerated.height == original.height


def test_rows_are_in_the_same_order(sheets) -> None:
    """Same components, same order -- including the four synthesised markers.

    Only BENDIN and BENDOUT survive the forward conversion; BENDSTR and BENDARC
    lie inside the magnet and are dropped, so they have to be rebuilt here.
    """
    original, regenerated = sheets
    assert list(regenerated["NAME1"]) == list(original["NAME1"])


@pytest.mark.parametrize("column", EXACT_COLUMNS)
def test_column_matches_exactly(column: str, sheets) -> None:
    original, regenerated = sheets
    mismatches = [
        (name, want, got)
        for name, want, got in zip(
            original["NAME1"], original[column], regenerated[column]
        )
        if want != got
    ]
    assert not mismatches, f"{column}: {mismatches[:3]}"


@pytest.mark.parametrize("column", GEOMETRY_COLUMNS)
def test_geometry_matches_to_written_precision(column: str, sheets) -> None:
    _assert_close(column, sheets, GEOMETRY_TOLERANCE)


@pytest.mark.parametrize("column", OPTICS_COLUMNS)
def test_optics_match_to_written_precision(column: str, sheets) -> None:
    _assert_close(column, sheets, OPTICS_TOLERANCE)


def test_displaced_elements_are_modelled_where_they_act(sheets) -> None:
    """The gun solenoid sits at the cathode in the model, at -0.102 in the sheet.

    `SOLA.23.I1` is a real MAD-8 element at s = 0 (`XFEL_I1.txm:138,193`, and
    `SURVEY_G1D` record 4 at `SUML = 0`).  `makelist_release.m:392-397` writes it
    102 mm earlier, to record where the solenoid stands rather than where the
    beam meets it.  The conversion config's `written_s_offsets` block declares
    that displacement once; the forward conversion subtracts it and this writer
    adds it back.

    Both halves are asserted here, because either alone would look fine: drop
    the subtraction and the row has a negative `S` and is silently discarded;
    drop the addition and the regenerated sheet quietly disagrees.
    """
    original, regenerated = sheets

    assert written_s_offsets().get("SOLA.23.I1") == -0.102, (
        "the gun solenoid's displacement is no longer declared in the "
        "conversion config's written_s_offsets block"
    )

    # Modelled at the cathode, alongside GUN.
    lattice = MagneticLattice(sequences.cathode_to_g1d)
    arc = 0.0
    for element in lattice.sequence:
        if element.id == "SOLA.23.I1":
            break
        arc += getattr(element, "l", 0.0)
    else:
        raise AssertionError("SOLA.23.I1 is not in the lattice at all")
    assert arc == pytest.approx(0.0, abs=1e-12)

    # Written back displaced, matching the sheet.
    row = regenerated.filter(pl.col("NAME1") == "SOLA.23.I1").row(0, named=True)
    want = original.filter(pl.col("NAME1") == "SOLA.23.I1").row(0, named=True)
    assert row["S"] == want["S"] == -0.102
    assert row["Z"] == pytest.approx(want["Z"], abs=1e-9)


def _assert_close(column: str, sheets, tolerance: float) -> None:
    original, regenerated = sheets
    difference = (original[column].cast(pl.Float64) - regenerated[column]).abs()
    worst = float(difference.max())
    assert worst < tolerance, (
        f"{column}: worst disagreement {worst:.3e} at "
        f"{original['NAME1'][int(difference.arg_max())]}"
    )
