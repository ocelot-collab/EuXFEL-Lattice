"""Readers for MAD-8 TWISS, SURVEY and RMAT tape files.

Vendored from `mad8-pandas` 1.1.1 (https://github.com/st-walker/mad8-pandas),
MIT licensed, rather than taken as a dependency -- it is a few hundred lines and
this repository is the only consumer.  Two deliberate changes from upstream:

- **polars instead of pandas.**  Polars frames have no index, so the element
  name stays an ordinary `NAME` column, and no `.attrs`, so tape metadata is
  fetched with `read_metadata` rather than riding along with the frame.
- **no `fortranformat`.**  Every format MAD-8 emits is plain fixed-width, so
  `_fixed_width` replaces the dependency.  See its docstring for why slicing
  rather than splitting is required.

The tapes themselves live in `src/euxfel/mad8/`; they are what
`makelist_release.m` reads to build the component list, and are the reference
our own survey and optics are checked against.
"""

from .extras import (
    append_beam_size_columns,
    append_s_column,
    append_twiss_gamma,
    fix_initial_row_energy,
)
from .handler import (
    MAD8FileFormatError,
    get_file_type,
    read,
    read_metadata,
    read_rmat,
    read_survey,
    read_twiss,
)

__all__ = [
    "MAD8FileFormatError",
    "append_beam_size_columns",
    "append_s_column",
    "append_twiss_gamma",
    "fix_initial_row_energy",
    "get_file_type",
    "read",
    "read_metadata",
    "read_rmat",
    "read_survey",
    "read_twiss",
]
