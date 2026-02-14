import polars as pl
from ocelot.cpbd.magnetic_lattice import MagneticLattice

from euxfel.subsequences import USED_COMPONENT_LIST

from .complist import ComponentList

FIXED_MATCH_POINTS: list[str] = [
    # In front of TDS must be fixed
    "MATCH.52.I1",
    # In front of dogleg must be fixed
    "MATCH.73.I1",
    # ??? Why must this be fixed ???
    "MATCH.104.I1",
    # In front of BC1 TDS must be fixed
    "MATCH.218.B1",
    "MATCH.446.B2",
    # Entrance to L3 must be fixed
    "MATCH.525.L3",
    # Entrance to collimation dogleg must be fixed
    "MATCH.1673.CL",
    # Ask nina the precise meaning of these:
    "MATCH.2248.SA1",
    "MATCH.2813.SA3",
    "MATCH.2197.SA2",
]

_OCELOT_OPTICS_NAMES = ["beta_x", "alpha_x", "beta_y", "alpha_y"]
_OCELOT_OTHER_NAMES = ["id", "s"]
_OCELOT_TWISS_NAMES = _OCELOT_OTHER_NAMES + _OCELOT_OPTICS_NAMES


def _longlist_optics_column_names_to_ocelot_names(df: pl.DataFrame) -> pl.DataFrame:
    """
    Rename component longlist column names to OCELOT-compatible Twiss names.

    This helper function maps common longlist column conventions to the
    corresponding OCELOT-style column names used throughout the optics
    analysis code. Columns that are not present are ignored.

    Parameters
    ----------
    df : pl.DataFrame
        Polars DataFrame containing optics data from a component longlist.

    Returns
    -------
    pl.DataFrame
        A DataFrame with columns renamed to OCELOT-compatible names where
        applicable.
    """
    return df.rename(
        {
            "BETX": "beta_x",
            "SUML": "s",
            "BETY": "beta_y",
            "ALFX": "alpha_x",
            "ALFY": "alpha_y",
            "ENERGY": "E",
            "S": "s",
            "NAME1": "id",
            "NAME": "id",
        },
        strict=False,
    )


def get_optics_at_points(
    twiss_df: pl.DataFrame, markers: list[str] | None = None
) -> pl.DataFrame:
    twiss_df = _longlist_optics_column_names_to_ocelot_names(twiss_df)

    markers = markers or []
    point_names = FIXED_MATCH_POINTS + markers

    names = [name for name in point_names if name in twiss_df["id"]]

    try:
        # Just select the rows corresponding to FIXED_MATCH_POINT ids and any additional marker names
        # this gives us a df with nrows = len(names), if all names are in the id column and all strings
        # in the id column are unique.
        df_at_ids = twiss_df.filter(pl.col("id").is_in(names))
        # Now just get the columsn corresponding to the optics that we care about.
        return df_at_ids.select(_OCELOT_TWISS_NAMES)
    except TypeError:
        raise ValueError(
            "Unable to extract, possibly duplicate names in twiss_df id column"
        )


def optics_at_points_from_longlist(markers: list[str] | None = None) -> pl.DataFrame:
    """
    Extract reference optics parameters at selected points
    from the default component longlist.

    Parameters
    ----------
    markers : list[str] | None, optional
        Additional marker IDs to include beyond the predefined fixed match
        points. If None, only fixed match points are used.

    Returns
    -------
    pl.DataFrame
        A Polars DataFrame containing some key optics parameters at the given match points

    """
    df = ComponentList(USED_COMPONENT_LIST).longlist
    df = _longlist_optics_column_names_to_ocelot_names(df)

    markers = markers or []

    # First filter to keep only the IDs we are interested in (i.e. markers)
    df_just_at_points = df.filter(pl.col("id").is_in(FIXED_MATCH_POINTS + markers))
    # Now also filter to just keep the columns (optics) we are interested in.
    optics_just_at_points = df_just_at_points[_OCELOT_TWISS_NAMES]
    return optics_just_at_points


def print_optics_at_points(
    twiss_or_twiss_df: pl.DataFrame, markers: list[str] | None = None
) -> None:
    """
    Print optics parameters and Bmag values at selected points, by default, only at the fixed match points
    (given by FIXED_MATCH_POINTS) will be printed.

    Parameters
    ----------
    twiss_or_twiss_df : pl.DataFrame
        Twiss optics DataFrame containing the calculated lattice optics.
    markers : list[str] | None, optional
        Additional marker IDs to include beyond the predefined fixed match
        points. If None, only the fixed match points are used.

    Returns
    -------
    None
    """
    with pl.Config(
        tbl_cols=-1,
        tbl_rows=-1,
        tbl_hide_dataframe_shape=True,
        tbl_hide_column_data_types=True,
    ):
        print(get_optics_with_bmags_at_points(twiss_or_twiss_df, markers=markers))


def get_optics_with_bmags_at_points(
    twiss_df: pl.DataFrame, markers: list[str] | None = None
) -> pl.DataFrame:
    """
    Compute optics parameters at selected match points and evaluate mismatch
    (Bmag) relative to reference optics from the component longlist.

    Parameters
    ----------
    twiss_df : pl.DataFrame
        Twiss optics DataFrame containing at least `id`, `s`, `beta_x`,
        `alpha_x`, `beta_y`, and `alpha_y` columns.
    markers : list[str] | None, optional
        Additional marker IDs to include beyond the predefined fixed match
        points. If None, only fixed match points given by FIXED_MATCH_POINTS are used.

    Returns
    -------
    pl.DataFrame
        A Polars DataFrame containing the optics at the selected points with
        additional columns `bmag_x` and `bmag_y` quantifying the mismatch
        relative to the component-list reference optics.
    """
    # What we have calculated ourselves and wish to check:
    twiss_match = get_optics_at_points(twiss_df, markers=markers)
    # What we are comparing to, this comes from the component list:
    twiss_match_reference = optics_at_points_from_longlist(markers=markers)

    # Calculate relative difference
    result = twiss_match.clone()
    # filter twiss_match_reference to keep only rows with ids in our twiss_df of interest
    twiss_match_reference = twiss_match_reference.filter(
        pl.col("id").is_in(twiss_match["id"])
    )

    # use id as index here so that the correct rows are used with each other.
    # twiss_match = twiss_match.set_index("id")
    # twiss_match_reference = twiss_match_reference.set_index("id")

    result = twiss_match.clone()
    # First we sort with respect to s to get correct order

    # Calculate bmag_x for our calculated optics w.r.t the component list (reference) optics
    result = (
        result.join(twiss_match_reference, on="id", how="left", suffix="_right")
        .with_columns(
            pl.struct(["beta_x", "alpha_x", "beta_x_right", "alpha_x_right"])
            .map_elements(
                lambda r: bmag(
                    r["beta_x"], r["alpha_x"], r["beta_x_right"], r["alpha_x_right"]
                ),
                return_dtype=pl.Float64,
            )
            .alias("bmag_x")
        )
        .drop(
            pl.selectors.ends_with("_right"),
        )
    )

    # Calculate bmag_y
    result = (
        result.join(twiss_match_reference, on="id", how="left", suffix="_right")
        .with_columns(
            pl.struct(["beta_y", "alpha_y", "beta_y_right", "alpha_y_right"])
            .map_elements(
                lambda r: bmag(
                    r["beta_y"], r["alpha_y"], r["beta_y_right"], r["alpha_y_right"]
                ),
                return_dtype=pl.Float64,
            )
            .alias("bmag_y")
        )
        .drop(pl.selectors.ends_with("_right"))  # ,
    )

    # Ensure that it is sorted w.r.t s if it isn't..:
    return result.sort("s")


def bmag(beta: float, alpha: float, beta0: float, alpha0: float) -> float:
    """
    Compute the optical mismatch parameter (Bmag) between two sets of Twiss parameters.

    Parameters
    ----------
    beta : float
        Beta function of the optics being evaluated.
    alpha : float
        Alpha function of the optics being evaluated.
    beta0 : float
        Reference (design) beta function.
    alpha0 : float
        Reference (design) alpha function.

    Returns
    -------
    float
        The Bmag mismatch parameter.
    """
    result = 0.5 * (
        (beta / beta0 + beta0 / beta)
        + (beta * beta0 * ((alpha0 / beta0) - (alpha / beta)) ** 2)
    )
    return result


def compare_match_point_surveys(
    mlat: MagneticLattice, markers: list[str] | None = None
) -> pl.DataFrame:
    """
    Compare surveyed match-point coordinates from an ocelot sequence against
    reference values from the Longlist.

    Parameters
    ----------
    mlat : MagneticLattice
    markers : list[str] | None, optional
        Additional marker names to include beyond the predefined fixed match
        points. If None, only fixed match points are used.

    Returns
    -------
    pl.DataFrame
        A Polars DataFrame with one row per (marker, source) pair, containing
        positions (X, Y, Z), angles (THETA, PHI, CHI), and first derivatives
        (XPD, YPD, ZPD), with a SOURCE column indicating "OCELOT" or "LONGLIST".
    """
    df = ComponentList(USED_COMPONENT_LIST).longlist

    r0 = df[0]
    mid_points, _ = mlat.survey_longlist(
        X0=r0["X"].item(),
        Y0=r0["Y"].item(),
        Z0=r0["Z"].item(),
        theta0=r0["THETA"].item(),
        phi0=r0["PHI"].item(),
        chi0=r0["CHI"].item(),
    )

    markers = markers or []

    names = [e.id for e in mlat.sequence]
    match_points = [name for name in names if name in FIXED_MATCH_POINTS + markers]
    end_marker_name = mlat.sequence[-1].id
    marker_names = match_points + [end_marker_name]

    columns = {
        "NAME1": [],
        "SOURCE": [],
        "X": [],
        "Y": [],
        "Z": [],
        "THETA": [],
        "PHI": [],
        "CHI": [],
        "XPD": [],
        "YPD": [],
        "ZPD": [],
        # "THETAPD": [],
        # "PHIPD": [],
        # "CHIPD": [],
    }
    for marker_name in marker_names:
        survey_idx = next(
            i for (i, ele) in enumerate(mlat.sequence) if ele.id == marker_name
        )
        survey_idx += (
            1  # Add one because mlat.survey inserts the initial offset as first point
        )

        columns["NAME1"].append(f"{marker_name}")
        columns["SOURCE"].append("OCELOT")

        # Positions/angles
        columns["X"].append(mid_points[survey_idx]["X"].item())
        columns["Y"].append(mid_points[survey_idx]["Y"].item())
        columns["Z"].append(mid_points[survey_idx]["Z"].item())
        columns["THETA"].append(mid_points[survey_idx]["THETA"].item())
        columns["PHI"].append(mid_points[survey_idx]["PHI"].item())
        columns["CHI"].append(mid_points[survey_idx]["CHI"].item())

        # PD (derivatives?)
        columns["XPD"].append(mid_points[survey_idx]["XPD"].item())
        columns["YPD"].append(mid_points[survey_idx]["YPD"].item())
        columns["ZPD"].append(mid_points[survey_idx]["ZPD"].item())
        # columns["THETAPD"].append(mid_points[survey_idx]["THETAPD"].item())
        # columns["PHIPD"].append(mid_points[survey_idx]["PHIPD"].item())
        # columns["CHIPD"].append(mid_points[survey_idx]["CHIPD"].item())

        lldf = df.filter(pl.col("NAME1") == marker_name)[
            "NAME1",
            "X",
            "Y",
            "Z",
            "THETA",
            "PHI",
            "CHI",
            "XPD",
            "YPD",
            "ZPD",
            "THETAPD",
            "PHIPD",
            "CHIPD",
        ]

        columns["NAME1"].append(f"{marker_name}")
        columns["SOURCE"].append("LONGLIST")
        columns["X"].append(lldf["X"].item())
        columns["Y"].append(lldf["Y"].item())
        columns["Z"].append(lldf["Z"].item())
        columns["THETA"].append(lldf["THETA"].item())
        columns["PHI"].append(lldf["PHI"].item())
        columns["CHI"].append(lldf["CHI"].item())

        columns["XPD"].append(lldf["XPD"].item())
        columns["YPD"].append(lldf["YPD"].item())
        columns["ZPD"].append(lldf["ZPD"].item())

        # columns["THETAPD"].append(lldf["THETAPD"].item())
        # columns["PHIPD"].append(lldf["PHIPD"].item())
        # columns["CHIPD"].append(lldf["CHIPD"].item())

    return pl.DataFrame(columns)


def print_surveyed_match_points(
    mlat: MagneticLattice, markers: list[str] | None = None
) -> None:
    """
    Print a comparison of surveyed coordinates at specific points for a magnetic lattice.  By default,
    only the fixed match points (given by FIXED_MATCH_POINTS) are printed.

    Parameters
    ----------
    mlat : MagneticLattice
    markers : list[str] | None, optional
        Additional marker names to include beyond the predefined fixed match
        points. If None, only the fixed match points are used.

    Returns
    -------
    None
    """
    with pl.Config(
        tbl_cols=-1,
        tbl_rows=-1,
        tbl_hide_dataframe_shape=True,
        tbl_hide_column_data_types=True,
    ):
        print(compare_match_point_surveys(mlat, markers=markers))
