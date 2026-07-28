"""Audit the component list's own survey geometry.

Every bending magnet in the component list is bracketed by BENDIN and BENDOUT
markers, and the rows carry the surveyed position and orientation at each.  That
makes the spreadsheet checkable against itself: seed a survey from the BENDIN
row, propagate through the magnet using that magnet's own LENGTH/STRENGTH/TILT,
and the result must land on the BENDOUT row.

This is the acceptance criterion for the geometry round-trip.  It catches two
distinct classes of problem: a conversion that models bends wrongly (which would
fail broadly), and rows in the spreadsheet that disagree with their own
neighbours (which fail individually).
"""

import math

import pytest
from euxfel.complist import ComponentList
from euxfel.subsequences import USED_COMPONENT_LIST
from ocelot.cpbd.elements import SBend
from ocelot.cpbd.magnetic_lattice import MagneticLattice

# Sheets covering every branch of the machine.  I1toT4D and I1toT5D between them
# contain every bending magnet; the shorter sheets are prefixes of these.
AUDITED_SHEETS = ["I1toT4D", "I1toT5D"]

# Rows either side of a bend are surveyed to ~0.1 urad, so anything at the
# micro-radian level is a genuine disagreement rather than rounding.
ANGLE_TOLERANCE_URAD = 0.5

# Bends known to disagree with their own BENDIN/BENDOUT markers, and by how much.
#
# BZ.2030.T1: the BENDOUT roll is 4.298e-06 where propagating from its own
# BENDIN row gives -5.471e-06, a difference of 9.769 urad.  X, Y, Z, THETA and
# PHI on that row all agree to better than 0.1 um / 0.1 urad, so it is isolated
# to CHI.  The value is inherited by the rows downstream, which leaves the T5
# branch rolled by ~9.8 urad and displaced by ~2.3 mm at the dump.  Whether the
# value is wrong, or whether CHI at BENDOUT means something other than the exit
# roll, is an open question with the component list's maintainers -- it is
# identical to the BENDSTR value on every bend, and this is the only one where
# that differs from the propagated exit.  Present in the 2026.01.21 and
# 2026.02.13 releases alike.
KNOWN_INCONSISTENT_BENDS = {"BZ.2030.T1"}


@pytest.fixture(scope="module")
def component_list() -> ComponentList:
    return ComponentList(str(USED_COMPONENT_LIST))


def _bend_blocks(rows: list[dict]):
    """Yield (bendin_row, magnet_row, bendout_row) for each angled bend."""
    for i, row in enumerate(rows):
        if row["CLASS"] != "BENDIN":
            continue
        # Nothing but the magnet and the other BEND* markers lies in between.
        block = rows[i : i + 5]
        magnet = next((r for r in block if r["CLASS"] in ("SBEN", "RBEN")), None)
        bendout = next((r for r in block if r["CLASS"] == "BENDOUT"), None)
        if magnet is None or bendout is None or not magnet["STRENGTH"]:
            continue
        yield row, magnet, bendout


def _propagate_through(bendin: dict, magnet: dict, bendout: dict) -> dict:
    """Survey from the BENDIN row through the magnet, returning the exit state."""
    lattice = MagneticLattice(
        [
            SBend(
                l=bendout["S"] - bendin["S"],
                angle=magnet["STRENGTH"],
                e1=magnet["E1/LAG"],
                e2=magnet["E2/FREQ"],
                tilt=magnet["TILT"],
                eid=magnet["NAME1"],
            )
        ]
    )
    _, end_points = lattice.survey_longlist(
        X0=bendin["X"],
        Y0=bendin["Y"],
        Z0=bendin["Z"],
        theta0=bendin["THETA"],
        phi0=bendin["PHI"],
        chi0=bendin["CHI"],
    )
    return end_points[1]


def test_bend_markers_are_self_consistent(component_list: ComponentList) -> None:
    """Each bend's BENDOUT row must follow from its own BENDIN row.

    Asserts on the exact set of disagreeing magnets rather than on there being
    none, so that a newly broken bend and a newly *fixed* one both fail loudly.
    """
    offenders: dict[str, float] = {}
    tested = 0

    for sheet in AUDITED_SHEETS:
        rows = component_list.get_sheet(sheet).to_dicts()
        for bendin, magnet, bendout in _bend_blocks(rows):
            tested += 1
            exit_state = _propagate_through(bendin, magnet, bendout)
            worst = max(
                abs((exit_state[angle].item() - bendout[angle]) * 1e6)
                for angle in ("THETA", "PHI", "CHI")
            )
            if worst > ANGLE_TOLERANCE_URAD:
                offenders[magnet["NAME1"]] = max(
                    worst, offenders.get(magnet["NAME1"], 0.0)
                )

    assert tested > 100, f"expected to audit the whole machine, only saw {tested} bends"

    unexpected = set(offenders) - KNOWN_INCONSISTENT_BENDS
    assert not unexpected, (
        f"bends newly disagreeing with their own BENDIN/BENDOUT markers: "
        f"{ {name: f'{offenders[name]:.3f} urad' for name in unexpected} }"
    )

    fixed = KNOWN_INCONSISTENT_BENDS - set(offenders)
    assert not fixed, (
        f"{sorted(fixed)} now agrees with its markers -- the component list has "
        f"been corrected, so remove it from KNOWN_INCONSISTENT_BENDS"
    )


def test_bend_arc_length_comes_from_the_markers(
    component_list: ComponentList,
) -> None:
    """The BENDIN/BENDOUT span is the arc, and LENGTH is not.

    `LongListConverter` sizes and positions bends from these markers precisely
    because the LENGTH column follows no single convention -- for some magnets
    it is the chord, for others the projection onto the straight axis.  This
    pins that down: the span must agree with the arc implied by the 3D chord
    between the markers and the bend angle, which LENGTH generally does not.
    """
    rows = component_list.get_sheet("I1toT5D").to_dicts()
    checked = disagreeing_with_length = 0

    for bendin, magnet, bendout in _bend_blocks(rows):
        angle = abs(magnet["STRENGTH"])
        span = bendout["S"] - bendin["S"]
        chord = math.dist(
            (bendin["X"], bendin["Y"], bendin["Z"]),
            (bendout["X"], bendout["Y"], bendout["Z"]),
        )
        arc_from_chord = chord * angle / (2 * math.sin(angle / 2))

        assert span == pytest.approx(arc_from_chord, abs=2e-6), (
            f"{magnet['NAME1']}: BENDIN->BENDOUT span {span} disagrees with the "
            f"arc implied by the 3D chord, {arc_from_chord}"
        )
        checked += 1
        if abs(span - magnet["LENGTH"]) > 2e-6:
            disagreeing_with_length += 1

    assert checked > 30
    assert disagreeing_with_length > 0.5 * checked, (
        "LENGTH now matches the marker span for most bends, which would mean the "
        "component list has changed convention -- revisit LongListConverter"
    )
