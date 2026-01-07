
import glob
import os
import re
from datetime import datetime
from dataclasses import dataclass
from enum import Enum, auto
from importlib.resources import files
from io import BytesIO
from pathlib import Path

import polars as pl

# class DumpTarget(Enum):
#     I1D = auto()
#     B1D = auto()
#     B2D = auto()
#     TLD = auto()
#     T4D = auto()
#     T5D = auto()

DEFAULT_COMPONENT_LIST_INDEX = 0

COMPONENT_LISTS_DIR = str(files("euxfel.longlists"))

def select_xls_file(directory=COMPONENT_LISTS_DIR):
    pattern = re.compile(r"component_list_(\d{4}\.\d{2}\.\d{2})\.xls$")

    dated = []
    undated = []

    for path in glob.glob(os.path.join(directory, "*.xls")):
        name = os.path.basename(path)
        m = pattern.match(name)
        if m:
            date = datetime.strptime(m.group(1), "%Y.%m.%d")
            dated.append((path, date))
        else:
            undated.append(path)

    files = []

    if dated:
        dated.sort(key=lambda x: x[1], reverse=True)
        files.extend((p, d) for p, d in dated)

    if undated:
        files.extend((p, None) for p in sorted(undated))

    if not files:
        raise SystemExit("No .xls files found.")

    if len(files) == 1:
        return files[0][0]

    print("Available .xls files:\n")
    for i, (path, date) in enumerate(files, start=1):
        if date:
            print(f"{i:2d}: {os.path.basename(path)}  ({date:%Y-%m-%d})")
        else:
            print(f"{i:2d}: {os.path.basename(path)}")

    choice = input("\nSelect a file by number [1]: ").strip()

    if choice == "":
        return files[0][0]

    try:
        choice = int(choice)
        if not (1 <= choice <= len(files)):
            raise ValueError
        return files[choice - 1][0]
    except ValueError:
        raise SystemExit("Invalid selection.")


def get_component_list_paths() -> list[str]:
    paths = []
    for path in Path(COMPONENT_LISTS_DIR).glob("component_list*.xls"):
        paths.append(str(path))
    return paths

def get_default_component_list_path() -> str:
    return get_component_list_paths()[DEFAULT_COMPONENT_LIST_INDEX]
    

# def get_component_list_to_target(target="i1d", component_list_path=None):
#     sheet_name = f"I1to{target.upper()}"
#     if component_list_path is None:
#         return get_default_component_list()
#     return ComponentList(component_list_path, sheet=sheet_name)


class ComponentList:
    def __init__(self, xls_path: str):
        # Keep the original xls file in memory for lazy loading later
        # of arbitrary sheets.  Necessary as generally slow.
        self._comp_list = BytesIO()
        with open(xls_path, 'rb') as f:
            self._comp_list.write(f.read())
        self._sheets = {}

    def _lazy_load_sheet(self, sheet_name: str) -> None:
        self._comp_list.seek(0)
        df = pl.read_excel(self._comp_list, sheet_name=sheet_name, read_csv_options={"skip_rows": 1})
        # df = df.rename({"E1/LAG": "E1_LAG", "E2/FREQ": "E2_FREQ"})
        self._sheets[sheet_name] = df

    def get_sheet(self, sheet_name: str) -> pl.DataFrame:
        try:
            df = self._sheets[sheet_name]
        except KeyError:
            self._lazy_load_sheet(sheet_name)
            df = self._sheets[sheet_name]
        return df.clone()

    @property
    def longlist(self) -> pl.DataFrame:
        return self.get_sheet("LONGLIST")

    def name2_to_name1(self, name2: str) -> str:
        df = self.longlist
        return df[df.NAME2 == name2].NAME1

    def name1_to_name2(self, name1: str) -> str:
        ldf = self.longlist
        return ldf[ldf.NAME1 == name1].NAME2

    def quadrupole_k1s(self) -> dict[str, dict[str, float]]:
        df = self.longlist
        quads = df[df["CLASS"] == "QUAD"]
        quad_k1ls = quads["STRENGTH"]
        lengths = quads["LENGTH"]
        name2s = quads["NAME1"]

        quad_k1s = quad_k1ls / lengths

        result = {}
        for name2, quad_k1 in zip(name2s, quad_k1s):
            result[name2] = {"k1": quad_k1}

        return result

    def cavity_settings(self) -> dict[str, dict[str, float]]:
        df = self.longlist
        cavities = df[df["CLASS"] == "LCAV"]
        # Filter TDSs, just pick actual accelerating cavities (and also AH1)
        cavities = cavities[(cavities.TYPE == "C") | (cavities.TYPE == "C3")]

        voltages = cavities["STRENGTH"] * 1e-3  # to GV
        # Phases are in units of 2pi (360).
        # Want htem in degrees for OCELOT...
        phases = cavities["E1/LAG"] * 360
        names = cavities["NAME1"]
        result = {}

        for name, voltage, phase in zip(names, voltages, phases):
            result[name] = {"v": voltage, "phi": phase}
        return result

    def chicane_settings(self) -> dict:
        bc0 = ["BB.96.I1", "BB.98.I1", "BB.100.I1", "BB.101.I1"]
        bc1 = ["BB.182.B1", "BB.191.B1", "BB.193.B1", "BB.202.B1"]
        bc2 = ["BB.393.B2", "BB.402.B2", "BB.404.B2", "BB.413.B2"]

        bc_dipoles = self.df.set_index("NAME1").loc[bc0 + bc1 + bc2]

        # Rename so they can be accessed in the tuple below
        bc_dipoles["E1"] = bc_dipoles["E1/LAG"]
        bc_dipoles["E2"] = bc_dipoles["E2/FREQ"]

        result = {}
        for tup in bc_dipoles.itertuples():
            result[tup.Index] = {"angle": tup.STRENGTH, "e1": tup.E1, "e2": tup.E2}
        return result

    def focussing_settings(self):
        return self.cavity_settings() | self.quadrupole_k1s() | self.chicane_settings()

    def get_optics_constraint(self, name1) -> dict[str : dict[str, float]]:
        row = self.item_from_name(name1)
        return {
            name1: {
                "beta_x": row.BETX,
                "beta_y": row.BETY,
                "alpha_x": row.ALFX,
                "alpha_y": row.ALFY,
            }
        }

    def item_from_name(self, name12: str):
        """Get row given element name can be either a NAME1 or NAME2, will try NAME1 first"""
        df = self.longlist
        try:
            return df.set_index("NAME1").loc[name12]
        except KeyError:
            return df.set_index("NAME2").loc[name12]

