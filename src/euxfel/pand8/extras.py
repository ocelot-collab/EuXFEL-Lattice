"""Derived columns for a TWISS frame.

Vendored from `mad8-pandas` (see `__init__.py`), rewritten for polars.  Each
function returns a new frame rather than mutating in place, including
`fix_initial_row_energy`, which upstream modified through pandas' `.at`.
"""

import polars as pl

MASS_ELECTRON_GEV = 0.511e-3


def _twiss_gamma(alpha: str, beta: str) -> pl.Expr:
    return (1 + pl.col(alpha) ** 2) / pl.col(beta)


def append_twiss_gamma(twiss_df: pl.DataFrame) -> pl.DataFrame:
    return twiss_df.with_columns(
        _twiss_gamma("ALFX", "BETX").alias("GAMX"),
        _twiss_gamma("ALFY", "BETY").alias("GAMY"),
    )


def append_s_column(twiss_df: pl.DataFrame) -> pl.DataFrame:
    return twiss_df.with_columns(pl.col("SUML").alias("S"))


def fix_initial_row_energy(twiss_df: pl.DataFrame) -> pl.DataFrame:
    """Give the INITIAL row the energy of the element that follows it.

    MAD-8 writes zero energy on the initial row.  Borrowing the next element's
    value is right unless that element itself changes the energy, which no
    first element in this lattice does.
    """
    if twiss_df.height < 2 or twiss_df["E"][0] != 0.0:
        return twiss_df
    return twiss_df.with_columns(
        pl.when(pl.int_range(pl.len()) == 0)
        .then(pl.lit(twiss_df["E"][1]))
        .otherwise(pl.col("E"))
        .alias("E")
    )


def append_beam_size_columns(
    twiss_df: pl.DataFrame,
    emitnx: float,
    emitny: float,
    espread_norm: float,
) -> pl.DataFrame:
    twiss_df = fix_initial_row_energy(twiss_df)

    relgamma = pl.col("E") / MASS_ELECTRON_GEV
    emitx = emitnx / relgamma
    emity = emitny / relgamma

    return twiss_df.with_columns(
        (emitx * pl.col("BETX") + (pl.col("DX") * espread_norm) ** 2)
        .sqrt()
        .alias("SIGMAX"),
        (emity * pl.col("BETY") + (pl.col("DY") * espread_norm) ** 2)
        .sqrt()
        .alias("SIGMAY"),
        (emitx * _twiss_gamma("ALFX", "BETX") + (pl.col("DPX") * espread_norm) ** 2)
        .sqrt()
        .alias("SIGMAXP"),
        (emity * _twiss_gamma("ALFY", "BETY") + (pl.col("DPY") * espread_norm) ** 2)
        .sqrt()
        .alias("SIGMAYP"),
    )
