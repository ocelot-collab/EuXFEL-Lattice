from typing import Optional
import os

import numpy as np
import numpy.typing as npt
from ocelot.cpbd.beam import Twiss

import polars as pl

from .complist import ComponentList, get_default_component_list_path

INJECTOR_MATCHING_QUAD_NAMES: list[str] = [
    "Q.37.I1",
    "Q.38.I1",
    "QI.46.I1",
    "QI.47.I1",
    "QI.50.I1",
]
B2_MATCHING_QUAD_NAMES: list[str] = [
    "Q.333.L2",
    "Q.345.L2",
    "Q.357.L2",
    "Q.369.L2",
    "Q.381.L2",
]

#
START_SIM: str = "start_ocelot"
MATCH_37: str = "MATCH.37.I1"
MATCH_52: str = "MATCH.52.I1"


# Not a tru "fixed" point, just in front of the TDS2
MATCH_428: str = "MATCH.428.B2"



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
    # Ask nina the meaing of these..
    "MATCH.2248.SA1",
    "MATCH.2813.SA3",
    "MATCH.2197.SA2"
]



# FIXED_MATCH_POINTS: list[str] = [
#     # In front of TDS must be fixed
#     "MATCH.52.I1",
#     # In front of dogleg must be fixed
#     "MATCH.73.I1",
#     # ??? Why must this be fixed ???
#     "MATCH.104.I1",
#     # In front of BC1 TDS must be fixed
#     "MATCH.218.B1",
#     "MATCH.446.B2",
#     # Entrance to L3 must be fixed
#     "MATCH.525.L3",
#     # Entrance to collimation dogleg must be fixed
#     "MATCH.1673.CL"
# ]

ALL_INTERESTING_MATCH_POINTS = FIXED_MATCH_POINTS + [MATCH_428]

FIXED_MATCH_POINTS = ALL_INTERESTING_MATCH_POINTS

_OCELOT_OPTICS_NAMES = ["beta_x", "alpha_x", "beta_y", "alpha_y"]
_OCELOT_OTHER_NAMES = ["id", "s"]
_OCELOT_TWISS_NAMES = _OCELOT_OTHER_NAMES + _OCELOT_OPTICS_NAMES



def get_name2_fixed_match_points(additional_names: Optional[list[str]] = None):
    if additional_names is None:
        additional_names = []
    ll = ComponentList(get_default_component_list_path())
    
    return [
        ll.name1_to_name2(name1).item()
        for name1 in FIXED_MATCH_POINTS + additional_names
    ]


def get_match_point_constraints(clist: Optional[XFELComponentList] = None) -> dict[str, dict[str, float]]:
    if clist is None:
        clist = ComponentList(get_default_component_list_path())
    points = ALL_INTERESTING_MATCH_POINTS

    tups = [x for x in clist.df.itertuples() if x.NAME1 in points]

    constraints = {}
    for tup in tups:
        odict = {"alpha_x": tup.ALFX,
                 "beta_x": tup.BETX,
                 "alpha_y": tup.ALFY,
                 "beta_y": tup.BETY}
        
        constraints[tup.NAME1] = odict

    return constraints


def _normalise_twiss_df(df: pl.DataFrame) -> pl.DataFrame:
    # Change columns to ocelot column names
    # Change NAME2 to NAME1s.
    try: # if pandas...
        df = df.rename(
            mapper={
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
            axis=1,
        )
    except: # If polars...
        df = df.rename(
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
            strict=False
        )
    return df


def get_match_point_optics(twiss_df: pl.DataFrame, additional_names: Optional[list[str]] = None) -> pl.DataFrame:
    twiss_df = _normalise_twiss_df(twiss_df)

    if additional_names is None:
        additional_names = []

    point_names = FIXED_MATCH_POINTS + additional_names
    names = [name for name in point_names if name in np.array(twiss_df["id"])]

    try:
        # Just select the rows corresponding to FIXED_MATCH_POINT ids and any additional_names
        # this gives us a df with nrows = len(names), if all names are in the id column and all strings
        # in the id column are unique.
        df_at_ids = twiss_df.filter(pl.col("id").is_in(names))
        # Now just get the columsn corresponding to the optics that we care about.
        return df_at_ids.select(_OCELOT_TWISS_NAMES)
    except TypeError:
        raise ValueError("Unable to extract, possibly duplicate names in twiss_df id column")
    
    

def default_match_point_optics():
    df = ComponentList(get_default_component_list_path()).longlist
    df = _normalise_twiss_df(df)

    just_match_points_df = df.filter(pl.col("id").is_in(FIXED_MATCH_POINTS))
    optics_just_match_points_df = just_match_points_df[_OCELOT_TWISS_NAMES]
    return optics_just_match_points_df


def get_default_match_point(match_name: str) -> Twiss:
    df = default_match_point_optics()
    twiss_series = df[df.id == match_name]
    
    return Twiss.from_series(twiss_series)

def print_match_point_optics(twiss_or_twiss_df: pl.DataFrame,
                               additional_names: Optional[list[str]] = None) -> None:
    try:
        with pl.Config(tbl_cols=-1, tbl_rows=-1, tbl_hide_dataframe_shape=True):
            print(get_match_point(twiss_or_twiss_df, additional_names=additional_names))
        return
    except AttributeError:
        pass
    except:
        raise TypeError(f"Unknown Twiss type: {twiss_or_twiss_df}")

    print(get_match_point(twiss_or_twiss_df, additional_names=additional_names))

def get_match_point(twiss_df: pl.DataFrame, additional_names: Optional[list[str]] = None) -> pl.DataFrame:
    # What we have calculated ourselves and wish to check:
    twiss_match = get_match_point_optics(twiss_df, additional_names=additional_names)
    # What we are comparing to, this comes from the component list:
    twiss_match_reference = default_match_point_optics()

    # Calculate relative difference
    # from IPython import embed; embed()
    result = twiss_match.clone()
    # filter twiss_match_reference to keep only rows with ids in our twiss_df of interest
    twiss_match_reference = twiss_match_reference.filter(pl.col("id").is_in(twiss_match["id"]))

    # use id as index here so that the correct rows are used with each other.
    # twiss_match = twiss_match.set_index("id")
    # twiss_match_reference = twiss_match_reference.set_index("id")

    result = twiss_match.clone()
    # First we sort with respect to s to get correct order

    # Calculate bmag_x for our calculated optics w.r.t the component list (reference) optics
    result = (
        result
        .join(twiss_match_reference, on="id", how="left", suffix="_right")
        .with_columns(
            pl.struct(["beta_x", "alpha_x", "beta_x_right", "alpha_x_right"])
            .map_elements(lambda r: bmag(r["beta_x"], r["alpha_x"], r["beta_x_right"], r["alpha_x_right"]),
                          return_dtype=pl.Float64)
            .alias("bmag_x")
            ).drop(pl.selectors.ends_with("_right"),
                   )
    )

    # Calculate bmag_y
    result = (
        result
        .join(twiss_match_reference, on="id", how="left", suffix="_right")
        .with_columns(
            pl.struct(["beta_y", "alpha_y", "beta_y_right", "alpha_y_right"])
            .map_elements(lambda r: bmag(r["beta_y"], r["alpha_y"], r["beta_y_right"], r["alpha_y_right"]),
                          return_dtype=pl.Float64)
            .alias("bmag_y")
            ).drop(pl.selectors.ends_with("_right")# ,
                   )
    )

    # result = result.drop(["gamma_x", "gamma_y"])

    # Ensure that it is sorted w.r.t s if it isn't..:
    return result.sort("s")


def read_mad8(fname: os.PathLike) -> pl.DataFrame:
    import pand8

    df8 = pand8.read(fname)
    df8 = df8.rename(mapper={"NAME": "NAME2"}, axis=1)

    ll = LongList(get_default_longlist_path())

    di = dict(zip(ll.df.NAME2, ll.df.NAME1))

    name1s = [di.get(name2, name2) for name2 in df8.NAME2]

    df8["NAME1"] = name1s

    return _normalise_twiss_df(df8)


def bmag(beta, alpha, beta_design, alpha_design) -> float:
    result = 0.5 * (
        (beta / beta_design + beta_design / beta)
        + (beta * beta_design * ((alpha_design / beta_design) - (alpha / beta)) ** 2)
    )
    return result

def compare_match_point_surveys(mlat) -> pl.DataFrame:
    df = ComponentList(get_default_component_list_path()).longlist

    r0 = df[0]
    x, y, z, ang_x, ang_y = mlat.survey(x0=r0["X"].item(),
                                    y0=r0["Y"].item(),
                                    z0=r0["Z"].item(),
                                    ang_x=r0["PHI"].item(),
                                    ang_y=r0["THETA"].item())

    names = [e.id for e in mlat.sequence]
    match_points = [name for name in names if name in FIXED_MATCH_POINTS]
    end_marker_name = mlat.sequence[-1].id
    marker_names = match_points + [end_marker_name]



    columns = {"NAME1": [], "SOURCE": [], "X": [], "Y": [], "Z": [], "THETA": [], "PHI": []}
    for marker_name in marker_names:
        survey_idx = next(
            i for (i, ele) in enumerate(mlat.sequence) if ele.id == marker_name
        )
        survey_idx += 1  # Add one because mlat.survey inserts the initial offset as first point


        columns["NAME1"].append(f"{marker_name}")
        columns["SOURCE"].append(f"OCELOT")
        columns["X"].append(x[survey_idx].item())
        columns["Y"].append(y[survey_idx].item())
        columns["Z"].append(z[survey_idx].item())
        columns["THETA"].append(ang_y[survey_idx].item())
        columns["PHI"].append(ang_x[survey_idx].item())

        lldf = df.filter(pl.col("NAME1") == marker_name)[
            "NAME1", "X", "Y", "Z", "THETA", "PHI"
        ]

        columns["NAME1"].append(f"{marker_name}")
        columns["SOURCE"].append("LONGLIST")
        columns["X"].append(lldf["X"].item())
        columns["Y"].append(lldf["Y"].item())
        columns["Z"].append(lldf["Z"].item())
        columns["THETA"].append(lldf["THETA"].item())
        columns["PHI"].append(lldf["PHI"].item())
        
    return pl.DataFrame(columns)

def print_surveyed_match_points(mlat) -> None:
    with pl.Config(tbl_cols=-1, tbl_rows=-1, tbl_hide_dataframe_shape=True):
        print(compare_match_point_surveys(mlat))
