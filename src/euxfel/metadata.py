"""Component-list bookkeeping carried on Ocelot elements.

Ocelot describes a machine in terms of what the beam sees: a length, an angle, a
gradient.  The component list describes the same machine in terms of what is
bolted to the tunnel floor: which room it stands in, which subsection it belongs
to, what the engineering type code is, how wide the vacuum chamber is.  None of
that survives the forward conversion, because none of it affects the optics --
and all of it is needed to write the component list back out.

Rather than reconstruct those columns from rules, which works until it doesn't,
each element carries them in a `metadata` dict:

    qi_52_i1.metadata = {"section": "I1", "subsection": "I1T", ...}

Some of it looks derivable and is not.  `TYPE` is the first dot-separated token
of the name for most elements, but `makelist_release.m` assigns `TYPE` *before*
applying some fifty hardcoded renames, so the tokens and the types disagree
wherever a rename fired.  `CLASS` is worse: a longlist `HKIC` with a non-zero
length becomes an Ocelot `RBend`, indistinguishable on the way back from a real
dipole -- `KIX.24.I1` is exactly this case.  Reproducing MATLAB's rename list
and inverting the class collapse would be a large pile of special cases; storing
nine fields is not.

`ps_id` deliberately stays a first-class attribute rather than moving in here.
It is referenced by name in `sections.py` and the s2e scripts, and it is a real
physical relationship -- which power supply drives which magnet -- not
descriptive bookkeeping.
"""

from typing import Any

from ocelot.cpbd.elements.optic_element import OpticElement

#: The component-list columns that cannot be recovered from an Ocelot element.
#: Everything else in a longlist row -- `S`, the survey block, the optics block,
#: `LENGTH`, `STRENGTH`, `ST` -- is computed from the lattice itself.
FIELDS: tuple[str, ...] = (
    "section",
    "subsection",
    "cad_room",
    "group",
    "class",
    "type",
    "xaper",
    "yaper",
)

#: Longlist column name for each metadata field.
COLUMNS: dict[str, str] = {
    "section": "SECTION",
    "subsection": "SUBSECTION",
    "cad_room": "CADRoom",
    "group": "GROUP",
    "class": "CLASS",
    "type": "TYPE",
    "xaper": "XAPER",
    "yaper": "YAPER",
}


def of(element: OpticElement) -> dict[str, Any]:
    """Return an element's metadata, or an empty dict if it has none.

    Elements added by the conversion config rather than read from the component
    list -- markers like `ocelot_start`, the survey rotations -- legitimately
    have none.
    """
    return getattr(element, "metadata", None) or {}


def get(element: OpticElement, field: str, default: Any = None) -> Any:
    """Return one metadata field, or `default` if absent.

    Prefer this to `element.metadata[field]` so that an element without
    metadata reads as missing rather than raising `AttributeError`.
    """
    if field not in FIELDS:
        raise KeyError(f"{field!r} is not a metadata field; expected one of {FIELDS}")
    return of(element).get(field, default)


def attach(element: OpticElement, row: dict[str, Any]) -> OpticElement:
    """Record a component-list row's bookkeeping columns on an element."""
    element.metadata = {
        field: row[column] for field, column in COLUMNS.items() if column in row
    }
    return element
