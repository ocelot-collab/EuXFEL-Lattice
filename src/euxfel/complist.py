from io import BytesIO

import polars as pl


class ComponentList:
    def __init__(self, xls_path: str):
        # Keep the original xls file in memory for lazy loading later
        # of arbitrary sheets.  Necessary as generally slow.
        self._comp_list = BytesIO()
        with open(xls_path, "rb") as f:
            self._comp_list.write(f.read())
        self._sheets: dict[str, pl.DataFrame] = {}

    def _lazy_load_sheet(self, sheet_name: str) -> None:
        self._comp_list.seek(0)
        df = pl.read_excel(
            self._comp_list, sheet_name=sheet_name, read_csv_options={"skip_rows": 1}
        )
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
