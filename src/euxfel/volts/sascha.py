"""The DESY control room optics file format.

Referred to here as the *Sascha format*, after the person who wrote it.  This is
a live interchange format used on the machine, so reading and writing it
faithfully is a requirement rather than a convenience.

The format is one ``NAME VALUE`` pair per line, space separated, values written
to six decimal places, LF line endings and **no trailing newline**::

    Q.A1.1.I1 -0.309370
    QI.1.I1 -0.053430
    BL.1.I1 0.099484

Names are power supplies (see :mod:`euxfel.beamline`) and values are
generalised kicks (see :mod:`euxfel.kicks`) -- energy independent, which
is exactly what makes the file meaningful on its own.

The three files shipped in ``special-optics-files/`` all carry the same 111
keys, differing only in their values, so key order is a property of the format
rather than of any one file and is preserved on round trip.
"""

from __future__ import annotations

import os
from collections.abc import Iterable, Mapping

from ocelot.cpbd.elements import RBend, SBend

__all__ = [
    "dumps_sascha",
    "is_sign_flipped",
    "read_sascha",
    "sascha_sign",
    "write_sascha",
]

#: Values are written to six decimal places, matching the shipped files.
VALUE_FORMAT = "{:.6f}"


def is_sign_flipped(element) -> bool:
    """Whether ``element``'s Sascha value has the opposite sign to the lattice.

    Bend angles do; quadrupoles and sextupoles do not.  This is measured, not
    assumed: across all three shipped files every one of the ten bend supplies
    has the opposite sign to the design lattice, six of them at a ratio of
    exactly -1, while 95 of 99 quadrupoles agree in sign (the disagreements
    being real differences between those optics and the design).

    Applying this on read *and* on write keeps round trips exact.  Ignoring it
    would quietly reverse every dipole in the machine.
    """
    return isinstance(element, (SBend, RBend))


def sascha_sign(element) -> float:
    """``-1.0`` if ``element``'s Sascha value is negated, else ``+1.0``."""
    return -1.0 if is_sign_flipped(element) else 1.0


def read_sascha(path: str | os.PathLike) -> dict[str, float]:
    """Read a Sascha file into ``{power supply: generalised kick}``.

    Key order follows the file.  Blank lines are skipped; anything after a ``#``
    is treated as a comment, though the shipped files contain neither.

    Raises
    ------
    ValueError
        On a malformed line or a repeated key, both of which would otherwise
        silently lose a setpoint.
    """
    values: dict[str, float] = {}
    with open(path, encoding="utf-8") as f:
        for lineno, raw in enumerate(f, start=1):
            line = raw.split("#", 1)[0].strip()
            if not line:
                continue

            fields = line.split()
            if len(fields) != 2:
                raise ValueError(
                    f"{path}:{lineno}: expected 'NAME VALUE', got {raw.strip()!r}"
                )

            name, text = fields
            try:
                value = float(text)
            except ValueError:
                raise ValueError(f"{path}:{lineno}: {text!r} is not a number") from None

            if name in values:
                raise ValueError(f"{path}:{lineno}: {name!r} appears more than once")

            values[name] = value

    return values


def dumps_sascha(
    values: Mapping[str, float], *, keys: Iterable[str] | None = None
) -> str:
    """Render ``values`` as Sascha-format text.

    Parameters
    ----------
    values
        ``{power supply: generalised kick}``.
    keys
        Key order to emit.  Defaults to the order of ``values``.  Passing the
        key order of an original file makes the round trip byte identical.

    Raises
    ------
    KeyError
        If ``keys`` names something absent from ``values``, rather than quietly
        dropping it.
    """
    order = list(values) if keys is None else list(keys)

    missing = [key for key in order if key not in values]
    if missing:
        raise KeyError(
            f"No value for {', '.join(repr(k) for k in missing)}, so the file "
            f"would be incomplete."
        )

    lines = [f"{key} {VALUE_FORMAT.format(values[key])}" for key in order]
    # The shipped files have no trailing newline; match them exactly.
    return "\n".join(lines)


def write_sascha(
    values: Mapping[str, float],
    path: str | os.PathLike,
    *,
    keys: Iterable[str] | None = None,
) -> None:
    """Write ``values`` to ``path`` in Sascha format."""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(dumps_sascha(values, keys=keys))
