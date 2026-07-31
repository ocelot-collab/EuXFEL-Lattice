"""Side-by-side tables of the four answers, at the points that matter.

The plot shows whether two sources agree in shape; these tables say by how much,
at the places the lattice is actually pinned: the fixed match points, any extra
markers asked for, and the dump at the end of the line.

One row per (point, source) so the sources for a point sit together and can be
read down.  A missing source is left out rather than filled with nulls -- not
every target has every source.

See `euxfel.plot.SOURCES` for what the four are and what a disagreement between
any given pair means.
"""

from __future__ import annotations

from typing import Sequence

import polars as pl
from ocelot.cpbd.magnetic_lattice import MagneticLattice
from ocelot.cpbd.track import twiss as ocelot_twiss

from euxfel import pand8, plot, sequences
from euxfel.complist import ComponentList
from euxfel.mad8 import survey_tape, twiss_tape
from euxfel.optics import FIXED_MATCH_POINTS

#: Optics reported at each point.
OPTICS_COLUMNS = ("beta_x", "alpha_x", "beta_y", "alpha_y", "Dx", "Dy", "E")

#: Survey reported at each point, in **MAD-8's** angle convention.
#:
#: The component list uses a different one: `makelist_release.m:210-212` swaps
#: THETA and PHI on read, and its `fprintf` negates PHI again on the way out, so
#:
#:     sheet.THETA =  tape.PHI      sheet.PHI = -tape.THETA    sheet.CHI = tape.PSI
#:
#: That transformation belongs in the longlist writer, on the way *out*, and
#: nowhere else -- the model itself holds MAD-8's convention, because MAD-8 is
#: what it is built from and checked against.  So this table converts the
#: component-list source *into* MAD-8's convention rather than the other way
#: about, and the tape is shown exactly as it is printed.
SURVEY_COLUMNS = ("X", "Y", "Z", "THETA", "PHI", "PSI")


def _tape_name1(target: str, drop_rotations: bool) -> list[str]:
    """The generated NAME1 for each tape row, in order.

    The tape carries MAD-8's names, which are not identities -- `D0100` occurs
    hundreds of times -- so a match point cannot be found in it by name.  The
    sequence built from that same tape has one element per row in the same order
    and carries the generated NAME1, which is what supplies it.

    `drop_rotations` selects the TWISS tape's row set, which omits `SROT`/`YROT`.
    """
    from euxfel.mad8_import import build_sequence, read_tape

    sequence = build_sequence(target)
    keywords = read_tape(target)["KEYWORD"].to_list()
    if not drop_rotations:
        return [element.id for element in sequence]
    return [
        element.id
        for element, keyword in zip(sequence, keywords)
        if keyword not in ("SROT", "YROT")
    ]


def _survey_seed(target: str) -> dict[str, float]:
    """MAD-8's own survey initial conditions for a path."""
    row = pand8.read_survey(survey_tape(target)).row(0, named=True)
    return {
        "X0": row["X"], "Y0": row["Y"], "Z0": row["Z"],
        "theta0": row["THETA"], "phi0": row["PHI"], "psi0": row["PSI"],
    }  # fmt: skip


def _named_optics(
    source: str, target: str, complist: ComponentList | None
) -> pl.DataFrame | None:
    """A source's optics with a `name` column of generated NAME1s."""
    target = target.upper()

    if source == "mad8":
        try:
            tape = pand8.read_twiss(twiss_tape(target))
        except FileNotFoundError:
            return None
        # Row 0 is INITIAL, which is not an element.
        names = _tape_name1(target, drop_rotations=True)
        body = tape.slice(1)
        if body.height != len(names):
            return None
        return body.select(
            pl.Series("name", names),
            pl.col("SUML").alias("s"),
            pl.col("BETX").alias("beta_x"), pl.col("ALFX").alias("alpha_x"),
            pl.col("BETY").alias("beta_y"), pl.col("ALFY").alias("alpha_y"),
            pl.col("DX").alias("Dx"), pl.col("DY").alias("Dy"), "E",
        )  # fmt: skip

    if source == "longlist":
        if complist is None:
            return None
        sheet = complist.get_sheet(f"I1to{target}")
        return sheet.select(
            pl.col("NAME1").alias("name"),
            pl.col("S").alias("s"),
            pl.col("BETX").alias("beta_x"), pl.col("ALFX").alias("alpha_x"),
            pl.col("BETY").alias("beta_y"), pl.col("ALFY").alias("alpha_y"),
            pl.col("DX").alias("Dx"), pl.col("DY").alias("Dy"),
            pl.col("ENERGY").alias("E"),
        )  # fmt: skip

    sequence, seed = _sequence_and_seed(source, target)
    if sequence is None:
        return None
    points = ocelot_twiss(MagneticLattice(sequence), tws0=seed)
    return pl.DataFrame(
        {
            "name": [p.id for p in points],
            "s": [p.s for p in points],
            **{c: [getattr(p, c) for p in points] for c in OPTICS_COLUMNS},
        }
    )


def _sequence_and_seed(source: str, target: str):
    """The element sequence and initial Twiss for one of the two Ocelot models."""
    if source == "ocelot-mad8":
        from euxfel.mad8_import import build_sequence

        try:
            tape = pand8.read_twiss(twiss_tape(target))
        except FileNotFoundError:
            return None, None
        return build_sequence(target), plot._twiss_seed_from_tape(tape)

    if source == "ocelot-longlist":
        sequence = getattr(sequences, f"cathode_to_{target.lower()}", None)
        if sequence is None:
            return None, None
        return sequence, sequences.CATHODE_TWISS0

    raise plot.UnknownSource(source)


def _named_survey(
    source: str, target: str, complist: ComponentList | None
) -> pl.DataFrame | None:
    """A source's survey with a `name` column of generated NAME1s."""
    target = target.upper()

    if source == "mad8":
        try:
            tape = pand8.read_survey(survey_tape(target))
        except FileNotFoundError:
            return None
        names = _tape_name1(target, drop_rotations=False)
        body = tape.slice(1)
        if body.height != len(names):
            return None
        # Shown exactly as printed: MAD-8's convention is the one the model
        # holds, so the tape needs no conversion here.
        return body.select(pl.Series("name", names), *SURVEY_COLUMNS)

    if source == "longlist":
        if complist is None:
            return None
        sheet = complist.get_sheet(f"I1to{target}")
        # Undo makelist's swap-and-negate so the sheet can be read against the
        # tape.  This is the only place the transformation appears on the way in.
        return sheet.select(
            pl.col("NAME1").alias("name"),
            "X", "Y", "Z",
            (-pl.col("PHI")).alias("THETA"),
            pl.col("THETA").alias("PHI"),
            pl.col("CHI").alias("PSI"),
        )  # fmt: skip

    sequence, _ = _sequence_and_seed(source, target)
    if sequence is None:
        return None
    try:
        seed = _survey_seed(target)
    except FileNotFoundError:
        return None
    # `survey`, not `survey_longlist`: the latter emits the component list's
    # angle convention, and that transformation belongs on the way out to the
    # spreadsheet, not inside the model.
    _, exits = MagneticLattice(sequence).survey(**seed)
    # survey prepends the seed point, so element i's exit is at i + 1.
    return pl.DataFrame(
        {
            "name": [element.id for element in sequence],
            **{
                column: [float(exits[i + 1][column]) for i in range(len(sequence))]
                for column in SURVEY_COLUMNS
            },
        }
    )


def points_of_interest(target: str, markers: Sequence[str] | None = None) -> list[str]:
    """Match points present in this target, plus any extras, plus the dump.

    The dump is the last element of the line, which is the one place a
    geometry error has nowhere left to be absorbed -- it is where a
    disagreement upstream shows its full accumulated size.
    """
    sequence = getattr(sequences, f"cathode_to_{target.lower()}", None)
    if sequence is None:
        from euxfel.mad8_import import build_sequence

        sequence = build_sequence(target.upper())

    identifiers = [element.id for element in sequence]
    wanted = FIXED_MATCH_POINTS + list(markers or [])
    present = [name for name in identifiers if name in wanted]
    dump = identifiers[-1]
    return present + ([dump] if dump not in present else [])


def _table(getter, target, sources, complist, markers) -> pl.DataFrame:
    names = plot.resolve_sources(sources)
    points = points_of_interest(target, markers)
    order = {name: index for index, name in enumerate(points)}

    frames = []
    for source in names:
        frame = getter(source, target, complist)
        if frame is None:
            continue
        selected = frame.filter(pl.col("name").is_in(points))
        if selected.height == 0:
            continue
        # The component list stores some columns as integers where the models
        # give floats; concat needs one schema.
        frames.append(
            selected.with_columns(
                pl.lit(source).alias("source"),
                pl.exclude("name").cast(pl.Float64),
            )
        )

    if not frames:
        return pl.DataFrame()

    table = pl.concat(frames, how="diagonal")
    return (
        table.with_columns(
            pl.col("name").replace_strict(order, default=len(order)).alias("_order")
        )
        .sort("_order", "source")
        .drop("_order")
    )


def optics_table(
    target: str,
    sources: Sequence[str] | None = None,
    complist: ComponentList | None = None,
    markers: Sequence[str] | None = None,
) -> pl.DataFrame:
    """Optics at every match point and the dump, one row per (point, source)."""
    table = _table(_named_optics, target, sources, complist, markers)
    if table.height == 0:
        return table
    return table.select(
        "name", "source", *[c for c in ("s", *OPTICS_COLUMNS) if c in table.columns]
    )


def survey_table(
    target: str,
    sources: Sequence[str] | None = None,
    complist: ComponentList | None = None,
    markers: Sequence[str] | None = None,
) -> pl.DataFrame:
    """Survey at every match point and the dump, one row per (point, source)."""
    table = _table(_named_survey, target, sources, complist, markers)
    if table.height == 0:
        return table
    return table.select("name", "source", *SURVEY_COLUMNS)


def print_table(table: pl.DataFrame, title: str) -> None:
    """Print a comparison table in full, without polars' row elision."""
    print(f"\n{title}")
    if table.height == 0:
        print("  (no sources available)")
        return
    with pl.Config(
        tbl_cols=-1,
        tbl_rows=-1,
        tbl_hide_dataframe_shape=True,
        tbl_hide_column_data_types=True,
    ):
        print(table)
