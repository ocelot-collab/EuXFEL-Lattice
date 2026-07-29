"""Fixed-width readers for the Fortran formats MAD-8 writes its tapes in.

Upstream `pand8` used the `fortranformat` package for this.  Every format MAD-8
actually emits is plain fixed-width -- no repeat counts, no scale factors, no
edit descriptors beyond `A`, `I`, `L`, `F` and `E` -- so slicing replaces the
dependency in a few dozen lines.

Slicing rather than whitespace splitting is not a stylistic choice: adjacent
`E16.9` fields butt directly together when a value is negative, e.g.

    " 0.000000000E+00-2.750000000E+00 2.320000000E+01"

which `str.split()` reads as two numbers instead of three.
"""

from typing import Any

# MAD-8 writes every real as E16.9 and every header field as 8 characters.
REAL_WIDTH = 16
HEADER_FIELD_WIDTH = 8


def _slice(line: str, start: int, width: int) -> str:
    """Return one fixed-width field, tolerating a line truncated before it.

    MAD-8 strips trailing blanks, so the final fields of a record are often
    simply absent rather than blank-padded.
    """
    return line[start : start + width]


def real(line: str, start: int, width: int = REAL_WIDTH) -> float | None:
    """Read one `E`/`F` field.  Blank or absent yields None, not 0.0."""
    text = _slice(line, start, width).strip()
    if not text:
        return None
    return float(text)


def reals(line: str, count: int, start: int = 0) -> list[float | None]:
    """Read `count` consecutive `E16.9` fields, as in `(5E16.9)`."""
    return [real(line, start + i * REAL_WIDTH) for i in range(count)]


def text(line: str, start: int, width: int) -> str:
    """Read one `A` field, stripped."""
    return _slice(line, start, width).strip()


def logical(line: str, start: int, width: int = HEADER_FIELD_WIDTH) -> bool:
    """Read a Fortran `L` field, written as `T` or `F`."""
    return text(line, start, width).upper().startswith("T")


def integer(line: str, start: int, width: int = HEADER_FIELD_WIDTH) -> int | None:
    """Read an `I` field."""
    field = text(line, start, width)
    return int(field) if field else None


def record(line: str, spec: list[tuple[str, int]]) -> list[Any]:
    """Read a whole record from a list of (kind, width) pairs.

    `kind` is one of "A" (text), "E"/"F" (real), "I" (integer) or "L" (logical),
    mirroring the Fortran edit descriptor.  Widths are consumed left to right.
    """
    readers = {"A": text, "E": real, "F": real, "I": integer, "L": logical}
    values, offset = [], 0
    for kind, width in spec:
        values.append(readers[kind](line, offset, width))
        offset += width
    return values
