"""Archived MAD-8 output — the upstream reference this lattice is checked against.

The European XFEL lattice originates as MAD-8 source (`.txm`).  DESY runs MAD-8
over it, and `makelist_release.m` turns the resulting SURVEY and TWISS tapes
into the component list that `euxfel convert` reads.  The spreadsheet is
therefore a *derived* artefact: it drops drifts and coordinate rotations,
synthesises element names from `floor(Z)`, and rounds bend lengths to 1e-4.

Keeping the tapes here gives us the undistorted reference.  They are what
`tests/test_mad8_survey.py` compares our Ocelot survey against, and they are the
frozen baseline that makes retiring MAD-8 possible rather than merely aspirational.

Layout of each dated release directory:

    tapes/{TWISS,SURVEY}_<PATH>.gz   MAD-8 output, gzipped (~10x)
    mad8_input/*.txm                 the lattice source that produced them
    makelist_release.m               DESY's component-list generator
    ReadMe_DESY.txt                  MAD-8 version and provenance

The MAD-8 binaries are deliberately absent: they are platform-specific and
2.5 MB each.  `ReadMe_DESY.txt` records the version (8.51.18, Mar-31-2009).

Tapes are read with `euxfel.pand8`, which decompresses `.gz` transparently.
"""

from pathlib import Path

MAD8_DIR = Path(__file__).parent

# The tapes currently used as the reference.  This is the MAD-8 run behind
# component_list_2026.01.22.xls, which is numerically identical to the
# 2026.02.13 list we convert from except for five added STERN diagnostic rows.
USED_MAD8_RELEASE = MAD8_DIR / "2026.01.22"

# One tape pair exists per dump path.  The T6-T10 and T20 branches were also
# run but are not archived until the LONGLIST sheet needs them.
TAPE_TARGETS = ("G1D", "I1D", "B1D", "B2D", "TLD", "T4D", "T5D")


def survey_tape(target: str, release: Path = USED_MAD8_RELEASE) -> Path:
    """Path to the SURVEY tape for a dump target, e.g. "T5D"."""
    return _tape("SURVEY", target, release)


def twiss_tape(target: str, release: Path = USED_MAD8_RELEASE) -> Path:
    """Path to the TWISS tape for a dump target, e.g. "T5D"."""
    return _tape("TWISS", target, release)


def _tape(kind: str, target: str, release: Path) -> Path:
    path = release / "tapes" / f"{kind}_{target.upper()}.gz"
    if not path.exists():
        raise FileNotFoundError(
            f"no {kind} tape for {target!r} in {release.name}; "
            f"archived targets are {', '.join(TAPE_TARGETS)}"
        )
    return path
