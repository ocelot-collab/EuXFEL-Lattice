"""Readers for MAD-8 TWISS, SURVEY and RMAT tape files.

Vendored from `mad8-pandas` (see `__init__.py`) with two changes: pandas is
replaced by polars, and `fortranformat` by `_fixed_width`.

A tape is a two-line header followed by `NPOS` fixed-length records and a
trailer.  Every record begins with the same two lines -- keyword, name and the
element's own attributes -- after which TWISS adds three lines of optics,
SURVEY two lines of geometry, and RMAT six lines of transfer matrix.

Because polars has no equivalent of pandas' `DataFrame.attrs`, the header and
trailer are not attached to the frame; use `read_metadata` for those.
"""

import gzip
import os
from typing import Any, Iterator, TextIO

import polars as pl

from . import _fixed_width as fw

COMMON_COLUMNS: list[str] = [
    "KEYWORD",
    "NAME",
    "ANGLE",
    "APER",
    "E",
    "E1",
    "E2",
    "EFIELD",
    "FREQ",
    "H1",
    "H2",
    "HKICK",
    "K0L",
    "K1",
    "K1L",
    "K2",
    "K2L",
    "K3",
    "K3L",
    "KS",
    "L",
    "LAG",
    "NOTE",
    "T0",
    "T1",
    "T2",
    "T3",
    "TILT",
    "VKICK",
    "VOLT",
    "XSIZE",
    "YSIZE",
]

SURVEY_COLUMNS: list[str] = ["X", "Y", "Z", "SUML", "THETA", "PHI", "PSI"]

# Columns that hold text rather than a number; everything else is Float64.
STRING_COLUMNS: frozenset[str] = frozenset({"KEYWORD", "NAME", "NOTE"})

# Which of the twelve common data slots each MAD-8 keyword actually uses.  The
# slots themselves are positional and shared, so a bend's slot 2 is K1 while a
# collimator's slot 4 is XSIZE.
COMMON_COLUMN_POSITIONS: dict[str, dict[str, int]] = {
    "DRIF": {"L": 0, "APER": 9, "NOTE": 10, "E": 11},
    "RBEN": {
        "L": 0,
        "ANGLE": 1,
        "K1": 2,
        "K2": 3,
        "TILT": 4,
        "E1": 5,
        "E2": 6,
        "H1": 7,
        "H2": 8,
        "APER": 9,
        "NOTE": 10,
        "E": 11,
    },
    "SBEN": {
        "L": 0,
        "ANGLE": 1,
        "K1": 2,
        "K2": 3,
        "TILT": 4,
        "E1": 5,
        "E2": 6,
        "H1": 7,
        "H2": 8,
        "APER": 9,
        "NOTE": 10,
        "E": 11,
    },
    "QUAD": {"L": 0, "K1": 2, "TILT": 4, "APER": 9, "NOTE": 10, "E": 11},
    "SEXT": {"L": 0, "K2": 3, "TILT": 4, "APER": 9, "NOTE": 10, "E": 11},
    "OCTU": {"L": 0, "TILT": 4, "K3": 5, "APER": 9, "NOTE": 10, "E": 11},
    "MULT": {
        "K0L": 1,
        "K1L": 2,
        "K2L": 3,
        "T0": 4,
        "K3L": 5,
        "T1": 6,
        "T2": 7,
        "T3": 8,
        "APER": 9,
        "NOTE": 10,
        "E": 11,
    },
    "SOLE": {"L": 0, "KS": 5, "APER": 9, "NOTE": 10, "E": 11},
    "RFCAVITY": {
        "L": 0,
        "FREQ": 5,
        "VOLT": 6,
        "LAG": 7,
        "APER": 9,
        "NOTE": 10,
        "E": 11,
    },
    "ELSEPARATOR": {"L": 0, "TILT": 4, "EFIELD": 5, "APER": 9, "NOTE": 10, "E": 11},
    "KICK": {"L": 0, "HKICK": 4, "VKICK": 5, "APER": 9, "NOTE": 10, "E": 11},
    "HKIC": {"L": 0, "HKICK": 4, "APER": 9, "NOTE": 10, "E": 11},
    "VKIC": {"L": 0, "VKICK": 5, "APER": 9, "NOTE": 10, "E": 11},
    "SROT": {"L": 0, "ANGLE": 5, "APER": 9, "NOTE": 10, "E": 11},
    "YROT": {"L": 0, "ANGLE": 5, "APER": 9, "NOTE": 10, "E": 11},
    "MONI": {"L": 0, "APER": 9, "NOTE": 10, "E": 11},
    "HMONITOR": {"L": 0, "APER": 9, "NOTE": 10, "E": 11},
    "VMONITOR": {"L": 0, "APER": 9, "NOTE": 10, "E": 11},
    "ECOL": {"L": 0, "XSIZE": 4, "YSIZE": 5, "APER": 9, "NOTE": 10, "E": 11},
    "RCOL": {"L": 0, "XSIZE": 4, "YSIZE": 5, "APER": 9, "NOTE": 10, "E": 11},
    "MARK": {"L": 0, "NOTE": 10, "E": 11},
    "INST": {"L": 0, "NOTE": 10, "E": 11},
    "WIRE": {"L": 0, "NOTE": 10, "E": 11},
    "IMON": {"L": 0, "NOTE": 10, "E": 11},
    "PROF": {"L": 0, "NOTE": 10, "E": 11},
    "BLMO": {"L": 0, "NOTE": 10, "E": 11},
    "LCAV": {"L": 0, "FREQ": 5, "VOLT": 6, "LAG": 7, "APER": 9, "NOTE": 10, "E": 11},
    "MATR": {"L": 0, "APER": 9, "E": 11},
}

TWISS_KEYS: dict[str, int] = {
    "ALFX": 0,
    "BETX": 1,
    "MUX": 2,
    "DX": 3,
    "DPX": 4,
    "ALFY": 5,
    "BETY": 6,
    "MUY": 7,
    "DY": 8,
    "DPY": 9,
    "X": 10,
    "PX": 11,
    "Y": 12,
    "PY": 13,
    "SUML": 14,
}

RMAT_KEYS: dict[str, int] = {
    f"R{i}{j}": 6 * (i - 1) + (j - 1) for i in range(1, 7) for j in range(1, 7)
} | {"SUML": 36}

# (A4,A16,F12.6,4E16.9,A19,E16.9) -- the first line of every record.
_RECORD_LINE_1 = [
    ("A", 4),
    ("A", 16),
    ("F", 12),
    ("E", 16),
    ("E", 16),
    ("E", 16),
    ("E", 16),
    ("A", 19),
    ("E", 16),
]

# (5A8,I8,L8,I8) -- the first line of the header.
_HEADER_LINE_1 = [("A", 8)] * 5 + [("I", 8), ("L", 8), ("I", 8)]

_HEADER_KEYS = [
    "PROGVRSN",
    "DATAVRSN",
    "DATE",
    "TIME",
    "JOBNAME",
    "SUPER",
    "SYMM",
    "NPOS",
]


class MAD8FileFormatError(Exception):
    pass


def _open(path: os.PathLike | str) -> TextIO:
    """Open a tape, transparently decompressing a gzipped one."""
    if str(path).endswith(".gz"):
        return gzip.open(path, "rt")
    return open(path, "r")


def read(path: os.PathLike | str) -> pl.DataFrame:
    """Read any MAD-8 tape, dispatching on its declared type."""
    file_type = get_file_type(path)
    if file_type == "TWISS":
        return read_twiss(path)
    if file_type == "SURVEY":
        return read_survey(path)
    if file_type == "RMAT":
        return read_rmat(path)
    if file_type == "CHROM":
        raise NotImplementedError("CHROM loading is not supported")
    raise MAD8FileFormatError(f"Unknown DATAVRSN: {file_type}")


def get_file_type(path: os.PathLike | str) -> str:
    with _open(path) as f:
        return parse_header(f.readline(), f.readline())["DATAVRSN"]


def read_metadata(path: os.PathLike | str) -> dict[str, Any]:
    """Return a tape's header and trailer.

    Polars frames carry no `attrs`, so metadata is fetched separately rather
    than riding along with the data as it did under pandas.
    """
    _, metadata = _read_tape(path)
    return metadata


def read_twiss(twiss: os.PathLike | str) -> pl.DataFrame:
    rows, _ = _read_tape(twiss, expected="TWISS")
    return _make_df(rows, list(TWISS_KEYS))


def read_survey(survey: os.PathLike | str) -> pl.DataFrame:
    rows, _ = _read_tape(survey, expected="SURVEY")
    return _make_df(rows, SURVEY_COLUMNS)


def read_rmat(rmat: os.PathLike | str) -> pl.DataFrame:
    rows, _ = _read_tape(rmat, expected="RMAT")
    return _make_df(rows, list(RMAT_KEYS))


def _read_tape(
    path: os.PathLike | str, expected: str | None = None
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Read a whole tape into (rows, metadata)."""
    with _open(path) as f:
        metadata = parse_header(f.readline(), f.readline())
        file_type = metadata["DATAVRSN"]
        if expected is not None and file_type != expected:
            raise MAD8FileFormatError(
                f"{path} is a {file_type} tape, expected {expected}"
            )

        # NPOS counts the records; if this runs off the end of the file the
        # tape has probably been hand-edited.
        rows = []
        for _ in range(metadata["NPOS"]):
            row = parse_common_two_lines(f.readline(), f.readline())
            if file_type == "TWISS":
                row.update(parse_twiss_row(*_n_readline(f, 3)))
            elif file_type == "SURVEY":
                row.update(parse_survey_rows(*_n_readline(f, 2)))
            elif file_type == "RMAT":
                row.update(parse_rmat_lines(_n_readline(f, 6)))
            else:
                raise MAD8FileFormatError(f"Unknown DATAVRSN: {file_type}")
            rows.append(row)

        if file_type == "TWISS":
            metadata.update(parse_twiss_trailer(*_n_readline(f, 3)))
        elif file_type == "SURVEY":
            metadata.update(parse_survey_trailer(*_n_readline(f, 2)))

    return rows, metadata


def parse_survey_rows(line3: str, line4: str) -> dict[str, Any]:
    position = fw.reals(line3, 4)
    orientation = fw.reals(line4, 3)
    return dict(zip(SURVEY_COLUMNS, position + orientation))


def parse_twiss_row(line1: str, line2: str, line3: str) -> dict[str, Any]:
    values = fw.reals(line1, 5) + fw.reals(line2, 5) + fw.reals(line3, 5)
    return {key: values[index] for key, index in TWISS_KEYS.items()}


def parse_rmat_lines(lines: Iterator[str]) -> dict[str, Any]:
    lines = list(lines)
    values = [v for line in lines[:-1] for v in fw.reals(line, 6)]
    values += fw.reals(lines[-1], 7)
    return {key: values[index] for key, index in RMAT_KEYS.items()}


def parse_common_two_lines(line1: str, line2: str) -> dict[str, Any]:
    parsed = fw.record(line1, _RECORD_LINE_1)
    keyword, name = parsed[0], parsed[1]

    row: dict[str, Any] = {key: 0.0 for key in COMMON_COLUMNS + SURVEY_COLUMNS}
    row["KEYWORD"] = keyword
    row["NAME"] = name
    row["NOTE"] = ""

    if not keyword:
        return row

    # Slots 0-3 come from line 1, 4-8 from line 2, then APER, NOTE and E from
    # the tail of line 1.
    data = parsed[2:6] + fw.reals(line2, 5) + [parsed[6], parsed[7], parsed[8]]
    for key, index in COMMON_COLUMN_POSITIONS[keyword].items():
        row[key] = data[index]

    return row


def parse_twiss_trailer(line1: str, line2: str, line3: str) -> dict[str, Any]:
    keys = [
        "DELTAP",
        "GAMTR",
        "C",
        "COSMUX",
        "QX",
        "QX'",
        "BXMAX",
        "DXMAX",
        "COSMUY",
        "QY",
        "QY'",
        "BYMAX",
        "DYMAX",
    ]
    values = fw.reals(line1, 3) + fw.reals(line2, 5) + fw.reals(line3, 5)
    return dict(zip(keys, values))


def parse_survey_trailer(line1: str, line2: str) -> dict[str, Any]:
    # RMIN/RMAX are written only for a ring.  For a linac the second line holds
    # the length alone, so parsing it positionally would silently report a
    # machine radius of zero -- hence the field count test.
    circular = len(line2.split()) == 3

    centre = fw.reals(line1, 3)
    tail = fw.reals(line2, 3)

    metadata: dict[str, Any] = dict(zip(("X", "Y", "Z"), centre))
    metadata["RMIN"], metadata["RMAX"] = (
        (tail[0], tail[1]) if circular else (None, None)
    )
    # Circumference for a ring, overall length for a linac.
    metadata["C"] = tail[2]
    return metadata


def parse_header(header_line_1: str, header_line_2: str) -> dict[str, Any]:
    values = fw.record(header_line_1, _HEADER_LINE_1)
    result: dict[str, Any] = dict(zip(_HEADER_KEYS, values))
    result["TITLE"] = header_line_2.rstrip("\n").strip()
    return result


def _n_readline(f: TextIO, n: int) -> Iterator[str]:
    for _ in range(n):
        yield f.readline()


def _make_df(rows: list[dict[str, Any]], extra_columns: list[str]) -> pl.DataFrame:
    """Build the frame with an explicit schema.

    Upstream indexed the frame by element name; polars has no index, so NAME
    stays an ordinary column.
    """
    columns = COMMON_COLUMNS + extra_columns
    schema = {
        name: (pl.String if name in STRING_COLUMNS else pl.Float64) for name in columns
    }
    return pl.DataFrame(rows, schema=schema)
