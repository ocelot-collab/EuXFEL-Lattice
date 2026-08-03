"""Check that we regenerate the component list's element names from MAD-8.

`NAME1` is not in the MAD-8 output.  It is synthesised by `makelist_release.m`
as `TYPE.floor(Z).SECTION` -- plus a cavity rule, a chicane rule, Roman-numeral
disambiguation and about twenty hand corrections -- and it is the name the
control system, `sections.py` and the s2e scripts all use.

Regenerating it rather than copying it out of the spreadsheet is what makes the
spreadsheet an output of this repository.  This test is the evidence that the
regeneration is faithful: every `NAME1` in every path sheet, in order.

The rules live in `mad8/<release>/mad8-config.yaml`, transcribed from the
`makelist_release.m` archived beside it.  If DESY changes the generator, this is
what notices.
"""

import difflib

import pytest

from euxfel.complist import ComponentList
from euxfel.mad8 import TAPE_TARGETS
from euxfel.mad8_import import build_sequence, generated_names
from euxfel.subsequences import USED_COMPONENT_LIST

#: `makelist_release.m:233-331` synthesises four marker rows around every bend.
#: They are not elements and have no tape record; `longlist_writer` puts them
#: back on the way out.
BEND_MARKER_CLASSES = ("BENDIN", "BENDSTR", "BENDARC", "BENDOUT")

#: Rows in the 2026.02.13 component list that postdate the 2026.01.22 MAD-8 run
#: archived here -- the STERN diagnostics on the T5 dump line.  They are in no
#: `.txm` file in the drop, so no amount of correct naming can produce them; the
#: gap closes when DESY supplies a newer tape set.
ROWS_NEWER_THAN_THE_TAPES = {
    "CAM1.2952.T5",
    "CDR.2952.T5",
    "ELPHI.2953.T5",
    "MIROUT.2953.T5",
    "CAM2.2954.T5",
}


@pytest.fixture(scope="module")
def complist() -> ComponentList:
    return ComponentList(str(USED_COMPONENT_LIST))


def _sheet_names(complist: ComponentList, target: str) -> list[str]:
    sheet = complist.get_sheet(f"I1to{target}")
    return [
        row["NAME1"]
        for row in sheet.iter_rows(named=True)
        if row["CLASS"] not in BEND_MARKER_CLASSES
    ]


@pytest.mark.parametrize("target", TAPE_TARGETS)
def test_generated_names_match_the_component_list(complist, target):
    """Every NAME1 the spreadsheet has, in order, from the tape alone."""
    expected = _sheet_names(complist, target)
    generated = generated_names(target)

    missing, extra = [], []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(
        a=generated, b=expected, autojunk=False
    ).get_opcodes():
        if tag == "equal":
            continue
        extra.extend(generated[i1:i2])
        missing.extend(expected[j1:j2])

    assert not extra, f"{target}: names we generate that the sheet does not have"
    assert set(missing) <= ROWS_NEWER_THAN_THE_TAPES, (
        f"{target}: sheet rows we failed to name: "
        f"{sorted(set(missing) - ROWS_NEWER_THAN_THE_TAPES)}"
    )


@pytest.mark.parametrize("target", TAPE_TARGETS)
def test_every_tape_record_becomes_an_element(target):
    """Nothing is dropped on the way in.

    The component list omits the drifts, the coordinate rotations and the
    zero-strength `HELP.*` survey handles; a model built from the tape keeps all
    of them, because what the spreadsheet leaves out is a fact about the
    spreadsheet rather than about the machine.
    """
    from euxfel.mad8_import import read_tape

    assert len(build_sequence(target)) == read_tape(target).height


def test_repeated_drift_names_are_distinct_objects():
    """Names repeat as MAD-8 has them; the objects behind them do not.

    `D0100: DRIFT, L = 0.100` is a literal in the MAD-8 source and occurs
    hundreds of times, so the *name* recurs and should -- that is what the
    lattice actually says.  Sharing one object between those placements is a
    different thing, and Ocelot forbids it: `navi._find_unique_index` matches
    physics-process anchors with `is` and raises when an object appears twice,
    so a shared drift could never be a slice point.

    Reusing the name never required reusing the object.  This test pins the
    distinction, because it is invisible until someone tries to anchor on a
    drift and gets a ValueError a long way from the cause.
    """
    from ocelot.cpbd.elements import Drift

    sequence = build_sequence("T4D")
    drifts = [element for element in sequence if isinstance(element, Drift)]

    objects = {id(drift) for drift in drifts}
    assert len(objects) == len(drifts), (
        f"{len(drifts) - len(objects)} drift placements share an object; "
        "each placement needs its own instance to be anchorable"
    )

    names = {drift.id for drift in drifts}
    assert len(names) < len(drifts) / 3, (
        "expected MAD-8's drift names to repeat heavily; if they no longer do, "
        "the tape's naming has changed"
    )


def test_every_element_is_a_distinct_object():
    """No object appears twice anywhere in a built sequence.

    The general form of the rule above: any repeat makes that element unusable
    as a physics-process anchor, whatever its type.
    """
    sequence = build_sequence("T4D")
    seen = {}
    for element in sequence:
        seen.setdefault(id(element), []).append(element)
    repeated = {k: v for k, v in seen.items() if len(v) > 1}
    assert not repeated, (
        f"{len(repeated)} objects appear more than once, e.g. "
        f"{next(iter(repeated.values()))[0].id}"
    )


def test_generated_variable_names_are_unique():
    """Distinct objects sharing a name still get distinct Python variables.

    Without this the generated module would define `d0100` hundreds of times and
    every reference would resolve to the last one, silently collapsing the
    lattice.
    """
    from collections import Counter

    from ocelot.cpbd.beam import Twiss

    from euxfel.writer import PythonSubsequenceWriter

    sequence = build_sequence("B1D")
    names = PythonSubsequenceWriter(sequence, Twiss()).make_var_names(sequence)
    assert len(names) == len(sequence)
    collisions = [n for n, count in Counter(names.values()).items() if count > 1]
    assert not collisions, f"variable names reused: {collisions[:5]}"


#: The tape prints coordinates as `E16.9`, ten significant figures, so at
#: Z ~ 3000 m its own positions are quantised at ~3e-6 m.  Measured directly:
#: the tape disagrees with *itself* -- |P(i) - P(i-1)| against the printed L for
#: a straight element -- by up to 9.9e-7 m.  Nothing built from it can close
#: better than that, so this is the tape's floor rather than our tolerance.
SURVEY_TOLERANCE_M = 5e-6


@pytest.mark.parametrize("target", TAPE_TARGETS)
def test_tape_built_survey_reproduces_the_tape(target):
    """Build from the tape, survey it, and land back on the tape.

    Element for element, not at sampled arc lengths: the tape-built sequence has
    one element per tape record in the same order, so every row can be checked.
    """
    import numpy as np
    from ocelot.cpbd.magnetic_lattice import MagneticLattice

    from euxfel import pand8
    from euxfel.mad8 import survey_tape
    from euxfel.mad8_import import read_tape

    sequence = build_sequence(target)
    seed = pand8.read_survey(survey_tape(target)).row(0, named=True)
    _, exits = MagneticLattice(sequence).survey(
        X0=seed["X"], Y0=seed["Y"], Z0=seed["Z"],
        theta0=seed["THETA"], phi0=seed["PHI"], psi0=seed["PSI"],
    )  # fmt: skip

    tape = read_tape(target)
    # survey() prepends the seed point, so element i's exit is at index i + 1.
    ours = np.array(
        [[float(exits[i + 1][c]) for c in "XYZ"] for i in range(len(sequence))]
    )
    theirs = tape.select("X", "Y", "Z").to_numpy()
    worst = np.linalg.norm(ours - theirs, axis=1).max()
    assert worst < SURVEY_TOLERANCE_M, f"{target}: worst position error {worst:.3e} m"
