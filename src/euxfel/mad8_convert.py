"""Write the Ocelot subsequence modules from the MAD-8 tapes.

The mirror of `conversion.longlist_to_ocelot`, one layer up the provenance
chain.  That reads the component list, which is a lossy render of these tapes;
this reads the tapes.

Each module is one slice of one dump path, cut between two markers named in the
MAD-8 config's `sections:` block.  The cut points are ours -- they are the module
split this repository chooses, not anything MAD-8 states -- but they are
expressed as generated `NAME1`s, so `euxfel.mad8_names` is what makes them
findable in a tape-built sequence at all.

`twiss0` comes from the TWISS tape rather than being propagated: MAD-8 has
already computed the optics at every element, and the TWISS tape is the SURVEY
tape minus the coordinate rotations, name for name, so the optics at a section
boundary can be read straight off.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterator

import polars as pl
from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements.optic_element import OpticElement

from euxfel import pand8
from euxfel.mad8 import load_config, twiss_tape
from euxfel.mad8_import import build_sequence
from euxfel.writer import PythonSubsequenceWriter

#: MAD-8 prints the phase advance in units of 2*pi; Ocelot uses radians.
MU_TO_RADIANS = 2.0 * 3.141592653589793

#: TWISS column -> Ocelot `Twiss` attribute.  MAD-8's energies are already in
#: GeV and its dispersions already in metres, so only the names change.
TWISS_COLUMNS = {
    "BETX": "beta_x",
    "ALFX": "alpha_x",
    "BETY": "beta_y",
    "ALFY": "alpha_y",
    "DX": "Dx",
    "DPX": "Dxp",
    "DY": "Dy",
    "DPY": "Dyp",
    "E": "E",
}


class SectionNotFound(Exception):
    """A section's start or stop marker is not in its target's sequence."""


def optics_tape(target: str) -> pl.DataFrame:
    """MAD-8's own optics for a dump path, indexed the way the sequence is.

    The TWISS tape omits `SROT`/`YROT` -- T5D has 9008 rows against the SURVEY
    tape's 9012 -- so it cannot be indexed positionally against a tape-built
    sequence.  It is name-for-name identical once the rotations are dropped,
    which is what the caller matches on.
    """
    return pand8.read_twiss(twiss_tape(target))


def twiss_at(optics: pl.DataFrame, mad_name: str, occurrence: int = 0) -> Twiss:
    """MAD-8's optics at the exit of a named element.

    Section boundaries are markers, which have no length, so their exit is also
    the entrance of whatever follows -- exactly what `twiss0` has to be.
    """
    rows = optics.filter(pl.col("NAME") == mad_name)
    if rows.height <= occurrence:
        raise SectionNotFound(f"{mad_name!r} not in the TWISS tape")
    row = rows.row(occurrence, named=True)

    twiss = Twiss()
    for column, attribute in TWISS_COLUMNS.items():
        setattr(twiss, attribute, float(row[column]))
    twiss.s = float(row["SUML"])
    twiss.mux = float(row["MUX"]) * MU_TO_RADIANS
    twiss.muy = float(row["MUY"]) * MU_TO_RADIANS
    return twiss


def _slice(
    sequence: list[OpticElement], start: str, stop: str, section: str
) -> tuple[list[OpticElement], int]:
    """The elements from `start` to `stop` inclusive, and where the slice began.

    Both markers are matched on the generated `NAME1`, which is unique across a
    path -- `makelist_release.m` disambiguates duplicates with Roman numerals and
    we reproduce that, so a boundary can never be ambiguous.
    """
    identifiers = [element.id for element in sequence]
    try:
        first = identifiers.index(start)
    except ValueError:
        raise SectionNotFound(f"{section}: no element named {start!r}") from None
    try:
        last = identifiers.index(stop, first)
    except ValueError:
        raise SectionNotFound(
            f"{section}: no element named {stop!r} after {start!r}"
        ) from None
    return sequence[first : last + 1], first


def build_subsequences(
    config: dict[str, Any] | None = None,
) -> dict[str, tuple[Twiss, list[OpticElement]]]:
    """Every declared subsequence, as `{name: (twiss0, elements)}`.

    One tape is read per dump path rather than per section, since most paths
    supply several.
    """
    if config is None:
        config = load_config()

    sections = config.get("sections") or {}
    built: dict[str, tuple[Twiss, list[OpticElement]]] = {}
    sequences: dict[str, list[OpticElement]] = {}
    optics: dict[str, pl.DataFrame] = {}

    for name, section in sections.items():
        target = section["target"]
        if target not in sequences:
            sequences[target] = build_sequence(target)
            optics[target] = optics_tape(target)

        elements, first = _slice(
            sequences[target], section["start"], section["stop"], name
        )
        # The optics entering the slice are those leaving the element before it,
        # or the tape's own initial conditions if the slice starts at the origin.
        preceding = sequences[target][first - 1] if first else None
        twiss0 = _twiss_entering(optics[target], preceding, elements[0])
        built[name] = (twiss0, elements)

    return built


def _twiss_entering(
    optics: pl.DataFrame, preceding: OpticElement | None, first: OpticElement
) -> Twiss:
    """Optics at the upstream face of a slice.

    Read at the *first element of the slice* rather than the one before it: every
    declared boundary is a zero-length marker, so its own row already holds the
    optics entering the section, and looking it up by name avoids depending on
    what happens to sit upstream.
    """
    name = getattr(first, "ps_id", None) or first.id
    return twiss_at(optics, name)


def mad8_to_ocelot(outdir: str | Path, config: dict[str, Any] | None = None) -> None:
    """Write one Python module per subsequence, plus the package `__init__`."""
    if config is None:
        config = load_config()

    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    written = config.get("writer") or {}
    power_supplies = written.get("write_types_power_supplies", set())

    module_names = []
    for name, (twiss0, sequence) in build_subsequences(config).items():
        module_name = name.lower()
        module_names.append(module_name)
        PythonSubsequenceWriter(sequence, twiss0).write_module(
            fname=outdir / f"{module_name}.py",
            write_types_power_supplies=power_supplies,
            comment="Converted from the MAD-8 SURVEY tapes",
        )

    _write_init(outdir, module_names)


def _write_init(outdir: Path, module_names: list[str]) -> None:
    """The package `__init__`, degrading a broken conversion to a warning.

    Same contract as the component-list route's: a half-written conversion still
    leaves an importable package, so the failure surfaces as a warning rather
    than an unimportable `euxfel`.
    """
    with open(outdir / "__init__.py", "w") as stream:
        stream.write("# Automatically generated from the MAD-8 SURVEY tapes\n")
        stream.write("import warnings\n\n")
        stream.write("try:\n")
        for module_name in module_names:
            stream.write(f"    from . import {module_name}\n")
        stream.write("except Exception as error:  # noqa: BLE001\n")
        stream.write('    warnings.warn(f"incomplete conversion: {error}")\n')


def iter_module_names(config: dict[str, Any] | None = None) -> Iterator[str]:
    """The module names a conversion would write, without doing the work."""
    if config is None:
        config = load_config()
    for name in config.get("sections") or {}:
        yield name.lower()
