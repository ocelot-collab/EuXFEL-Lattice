"""Generate control-system element names the way `makelist_release.m` does.

A MAD-8 name is not an identity.  `D0100` occurs 256 times in the T5D tape, only
13% of records have a unique name, and nothing in the name says where the element
is.  The names everything downstream actually uses -- `BZ.2030.T1`,
`QI.52.I1`, `C.A1.1.I1` -- are synthesised by `makelist_release.m` on the way
into the component list, out of three ingredients:

    NAME1 = TYPE . <position> . SECTION

with `TYPE` the MAD-8 name up to its first dot, `SECTION` the text after its
last, and `<position>` the floor of the element's centre in global survey `Z`.

Reproducing that here rather than copying the names out of the spreadsheet is
what lets the spreadsheet be an *output* of this repository.  Every rule below is
declared in the conversion config's `naming:` block and cites the
`makelist_release.m` line it comes from; nothing is hardcoded here that a future
component list might change.

**The position corrections move the name, not the element.**  `makelist` shifts
elements bodily -- a component list records where hardware stands, so the gun
solenoid is booked 102 mm upstream of where the beam meets it and the `CAX`/`CAY`
pair is collapsed onto one point.  Our model keeps every element where MAD-8 puts
it and applies those offsets only when deciding what to call it.  That is the
compromise: the names match the control system, the geometry matches the beam.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any

#: `makelist` writes integers with MATLAB's `num2str`, which for a negative
#: position gives `-3`.  Python's `str(int)` agrees, so no special casing.
NamingConfig = dict[str, Any]


def reclassify(keyword: str, mad_name: str, table: list[dict[str, Any]]) -> str:
    """What a MAD-8 `DRIF` or `MARK` record really is (makelist:86-160).

    MAD-8 has no element type for a vacuum chamber, a cryo feedbox or an
    undulator, so they are written as drifts and markers and told apart by name.
    Returns the reclassified keyword, or the original if nothing matches.

    An entry ending in `*` anchors to the start of the name; otherwise it matches
    anywhere, following `strncmp` versus `strfind` in the source.  Each rule also
    names the keyword it applies to, which is what stops the `SCU` undulator rule
    from firing on the marker `STSUB.SCU.SA2`.
    """
    for rule in table:
        if rule["from"] != keyword:
            continue
        for pattern in rule["patterns"]:
            anchored = pattern.endswith("*")
            stem = pattern[:-1] if anchored else pattern
            if mad_name.startswith(stem) if anchored else stem in mad_name:
                return rule["to"]
    return keyword


@dataclass
class Record:
    """What naming needs to know about one element.

    Deliberately not an Ocelot element: naming runs before the sequence is
    final, and keeping it to plain data makes the rules testable without
    building a lattice.
    """

    mad_name: str
    #: Global survey Z of the element's centre, in metres.
    z: float
    #: Global survey X of the centre, needed only by the chicane rule.
    x: float = 0.0
    #: Direction cosines of the local axis, for resolving declared offsets into
    #: a change in `Z`.  Defaults to a beamline running along +Z.
    dz_dlocal_z: float = 1.0
    dz_dlocal_x: float = 0.0
    #: Filled in by `name_sequence`.
    type_: str = field(default="", init=False)
    section: str = field(default="", init=False)
    subsection: str = field(default="", init=False)
    name: str = field(default="", init=False)


def _split(mad_name: str) -> tuple[str, str]:
    """TYPE and SECTION from a MAD-8 name (makelist:437-442).

    A name with no dot at all is entirely TYPE, and has no section -- `makelist`
    writes `_` there.
    """
    if "." not in mad_name:
        return mad_name, "_"
    return mad_name.split(".", 1)[0], mad_name.rsplit(".", 1)[1]


def _subsections(records: list[Record]) -> None:
    """Tag each record with its subsection (makelist:524-535).

    `STSUB.<name>.<section>` opens a span and `ENSUB` closes it, both inclusive.
    Outside any span the subsection is just the section.
    """
    current: str | None = None
    for record in records:
        opening = record.type_ == "STSUB"
        if opening:
            parts = record.mad_name.split(".")
            current = parts[1] if len(parts) > 2 else record.section
        record.subsection = current if current is not None else record.section
        if record.type_ == "ENSUB":
            current = None


def _position_shift(record: Record, config: NamingConfig) -> float:
    """Declared naming offsets for a record, in metres along the local axis."""
    shift = 0.0
    for stem, delta in (config.get("position_corrections") or {}).items():
        if stem in record.mad_name:
            shift += float(delta)
            # makelist's if/elseif chain takes the first match only.
            break

    markers = config.get("marker_shifts") or {}
    if markers and record.mad_name.startswith(markers.get("prefix", "\0")):
        for key, delta in markers.items():
            if key in ("prefix", "default"):
                continue
            if key in record.mad_name:
                return shift + float(delta)
        shift += float(markers.get("default", 0.0))
    return shift


def _namepos(record: Record, config: NamingConfig) -> int:
    """The integer that goes in the middle of the name (makelist:537-543)."""
    z = record.z + _position_shift(record, config) * record.dz_dlocal_z

    rule = config.get("round_instead_of_floor") or {}
    rounded = record.section.startswith(
        rule.get("section_prefix", "\0")
    ) and record.type_.startswith(rule.get("type_prefix", "\0"))
    # MATLAB's round() is half-away-from-zero, unlike Python's banker's rounding.
    return math.floor(z + 0.5) if rounded else math.floor(z)


def _positional_names(records: list[Record], config: NamingConfig) -> None:
    for record in records:
        record.name = f"{record.type_}.{_namepos(record, config)}.{record.section}"


def _cavity_names(records: list[Record], config: NamingConfig) -> None:
    """Number the cavities within their RF station (makelist:545-557).

    A cavity is not named after its position at all.  `STAC.<station>.<...>`
    markers punctuate the linac, and each cavity takes the station name plus a
    counter that wraps every eight -- one XFEL cryomodule.
    """
    rule = config.get("cavity") or {}
    types = set(rule.get("types") or ())
    if not types:
        return
    wrap = int(rule.get("counter_wraps_at", 8))
    marker = rule.get("station_marker", "STAC")

    station, count = None, 0
    for record in records:
        if record.type_ == marker:
            # STAC.A1.1.I1 -> everything between the first and last dot.
            parts = record.mad_name.split(".")
            station = ".".join(parts[1:-1]) if len(parts) > 2 else None
        if record.type_ in types and station is not None:
            count += 1
            record.name = f"{record.type_}.{station}.{count}.{record.section}"
            count %= wrap


def _neighbour_names(records: list[Record], config: NamingConfig) -> None:
    """Elements that take their number from a neighbouring marker (:1288-1295).

    A 2 m fast kicker is modelled as two 1 m halves either side of a `KS`
    marker, and a stripline BPM as two pickups either side of a `MIDBPMF`.  Both
    halves must carry the marker's number so the pair reads as one device.
    """
    for borrower, lender in (config.get("number_from_neighbour") or {}).items():
        takers = [r for r in records if r.type_ == borrower]
        givers = [r for r in records if r.type_ == lender]
        # makelist indexes the two lists in step and would error on a mismatch;
        # zip stopping at the shorter is the same behaviour without the crash.
        for taker, giver in zip(takers, givers):
            taker.name = f"{taker.type_}.{math.floor(giver.z)}.{taker.section}"


def _chicane_names(records: list[Record], config: NamingConfig) -> None:
    """Undulator-chicane magnets, named from a displaced point (:944-1090).

    These sit off-axis in their own chamber, so `makelist` shifts them
    transversely before reading off the naming position.  The shift is in the
    local x direction and so only reaches `Z` through the beamline angle -- tiny,
    but enough to tip a floor() over, which is why the fixup tables exist.
    """
    for rule in config.get("chicane_offsets") or ():
        # A few of the blocks shift the element without renaming it.
        if rule.get("renames_position") is False:
            continue
        sections = set(rule.get("sections") or ())
        types = set(rule.get("types") or ())
        dx = float(rule.get("dx", 0.0))
        fixups = {int(k): int(v) for k, v in (rule.get("fixups") or {}).items()}
        for record in records:
            if record.section not in sections or record.type_ not in types:
                continue
            # makelist adds the displacement to Z and then again inside floor(),
            # a double-count we reproduce rather than correct: the names it
            # produced are the names the control system uses.
            z = record.z + 2 * dx * record.dz_dlocal_x
            position = fixups.get(math.floor(z), math.floor(z))
            record.name = f"{record.type_}.{position}.{record.section}"


def _partner_names(records: list[Record], config: NamingConfig) -> None:
    """Correctors that borrow a neighbour's whole name (makelist:762-772).

    A `CBP` is a corrector wound onto a `BP` beam-position monitor's body, so it
    is called `C` + the monitor's name rather than being numbered from its own
    position.  `find(..., 1)` in the source means only the first of each type is
    ever paired, which is reproduced rather than generalised.
    """
    for rule in config.get("name_from_partner") or ():
        borrowers = [r for r in records if r.type_ == rule["type"]]
        partners = [r for r in records if r.type_ == rule["partner"]]
        if not borrowers or not partners:
            continue
        if rule.get("first_only"):
            borrowers, partners = borrowers[:1], partners[:1]
        within = float(rule.get("within_m", 0.3))
        for borrower in borrowers:
            for partner in partners:
                if abs(borrower.z - partner.z) < within:
                    borrower.name = f"{rule.get('prefix', '')}{partner.name}"


def _disambiguate(records: list[Record], config: NamingConfig) -> None:
    """Roman-numeral suffixes for repeated names (makelist:694-717).

    Two rows sharing a name are only a clash if they are different things.  When
    they are the same element recorded twice -- same MAD-8 name, within a
    millimetre -- `makelist` leaves both alone, and so do we.
    """
    suffixes = config.get("duplicate_suffixes") or ["I", "II", "III", "IV", "V", "VI"]
    groups: dict[str, list[Record]] = {}
    for record in records:
        groups.setdefault(record.name, []).append(record)

    for group in groups.values():
        if len(group) < 2:
            continue
        same_thing = len({r.mad_name for r in group}) < len(group)
        if same_thing and abs(group[0].z - group[1].z) < 1e-3:
            continue
        for index, record in enumerate(group):
            stem, _, section = record.name.rpartition(".")
            record.name = f"{stem}{suffixes[index % len(suffixes)]}.{section}"


def _renames(records: list[Record], config: NamingConfig) -> None:
    """The hand corrections, applied last (makelist:775-801, :1131-1223)."""
    by_subsection = config.get("renames_in_subsection") or {}
    for record in records:
        scoped = by_subsection.get(record.subsection) or {}
        if record.name in scoped:
            record.name = scoped[record.name]

    flat = config.get("renames") or {}
    for record in records:
        if record.name in flat:
            record.name = flat[record.name]

    # Suffixes keyed on the MAD-8 name rather than the generated one, so they
    # survive whatever the positional rule produced (makelist:919-926).
    for mad_name, suffix in (config.get("suffix_by_mad_name") or {}).items():
        for record in records:
            if record.mad_name == mad_name:
                stem, _, section = record.name.rpartition(".")
                record.name = f"{stem}{suffix}.{section}"


def name_records(records: list[Record], config: NamingConfig) -> list[Record]:
    """Assign `name` to every record, in `makelist_release.m`'s own order.

    The order matters: the positional rule is the default, the cavity, neighbour
    and chicane rules overwrite it for the elements they own, disambiguation sees
    whatever those produced, and the hand renames go last so they can correct
    anything.
    """
    section_overrides = config.get("section_overrides") or {}
    for record in records:
        record.type_, record.section = _split(record.mad_name)
        record.section = section_overrides.get(record.mad_name, record.section)

    _subsections(records)
    _positional_names(records, config)
    _cavity_names(records, config)
    _neighbour_names(records, config)
    _chicane_names(records, config)
    _disambiguate(records, config)
    _partner_names(records, config)
    _renames(records, config)
    return records
