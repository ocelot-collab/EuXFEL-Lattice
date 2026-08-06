"""Tests for the setpoints configuration format.

The load-bearing ones are the round trips: a control-room file that survives
import, application and export byte for byte, and a design setpoint that applies
as an exact no-op.  Between them they pin the two conventions that are silent
when wrong -- the bend sign flip and the per-supply design ratios.
"""

import math
import warnings
from pathlib import Path

import pytest
from ocelot.cpbd.elements import Drift, Quadrupole, SBend
from ocelot.cpbd.magnetic_lattice import MagneticLattice

from euxfel import (
    MATCHED_SECTIONS,
    AmbiguousKeyError,
    Beamline,
    GangedMagnetError,
    KnobOwnedError,
    UnknownKeyError,
    all_machine_elements,
)
from euxfel.volts import (
    ChicaneKnob,
    ConflictError,
    InjectorRFKnob,
    LinacKnob,
    MachineSetpoints,
)
from euxfel.volts.config import valid_attributes
from euxfel.kicks import read_kick
from euxfel.volts.knobs import chicane_dipoles, measure_r56, yoke_length
from euxfel.machine import CHICANES, INJECTOR, LINACS
from euxfel.volts.sascha import dumps_sascha, read_sascha, sascha_sign

SASCHA_DIR = Path(__file__).parent.parent / "special-optics-files"

#: The files the control room emitted, as opposed to the ones we wrote.  Only
#: these are expected to round trip byte for byte -- a hand-written file may
#: carry comments, which the writer does not reproduce.
SASCHA_FILES = sorted(
    path
    for path in SASCHA_DIR.glob("*.txt")
    if not path.read_text().lstrip().startswith("#")
)

# Building a beamline reports supplies whose magnets sit at zero by design.  True
# and worth saying once in anger, but not what these tests are about.
pytestmark = pytest.mark.filterwarnings(
    "ignore:.*zero design kick.*:UserWarning",
)


@pytest.fixture(scope="module")
def cell():
    """The whole machine, shared: building it copies ~8000 elements."""
    return all_machine_elements()


@pytest.fixture
def beamline(cell):
    return Beamline.from_cell(cell)


#: Everything a setpoint can write.  Used to put the shared lattice back.
_MUTABLE = ("k1", "k2", "k3", "angle", "l", "e1", "e2", "v", "phi")


@pytest.fixture
def restores_the_lattice(cell):
    """Undo whatever the test does to the module-level cells.

    `apply_in_place` mutates the generated elements, which are shared by every
    section and every `cathode_to_*`, so without this a test leaks into the ones
    after it.  A copy is not an option here: `SectionLattice` builds its sections
    from those cells whatever sequence you hand it, so the globals genuinely have
    to change.
    """
    saved = [
        (
            element,
            {
                name: getattr(element, name)
                for name in _MUTABLE
                if hasattr(element, name)
            },
        )
        for element in cell
    ]
    yield
    for element, attributes in saved:
        for name, value in attributes.items():
            setattr(element, name, value)


# --------------------------------------------------------------------------- #
# The Sascha format
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("path", SASCHA_FILES, ids=lambda p: p.name)
def test_sascha_text_round_trips_byte_for_byte(path):
    assert dumps_sascha(read_sascha(path)) == path.read_text()


@pytest.mark.parametrize("path", SASCHA_FILES, ids=lambda p: p.name)
def test_every_sascha_key_resolves(path, beamline):
    unresolved = [key for key in read_sascha(path) if not _resolves(beamline, key)]
    assert not unresolved


def _resolves(beamline, key):
    try:
        beamline.resolve(key, namespace="ps")
    except UnknownKeyError:
        return False
    return True


@pytest.mark.parametrize("path", SASCHA_FILES, ids=lambda p: p.name)
def test_sascha_survives_import_apply_and_export(path, cell):
    """The whole pipeline, including routing chicanes through their knobs."""
    setpoints = MachineSetpoints.from_sascha(path, cell)
    exported = setpoints.to_sascha(cell, keys=list(read_sascha(path)))
    assert exported == path.read_text()


def test_bend_signs_are_flipped_and_quadrupole_signs_are_not(beamline):
    """The convention that would silently reverse every dipole if missed."""
    values = read_sascha(SASCHA_DIR / "BC2_TDS.txt")
    flipped = same = 0
    for key, value in values.items():
        group = beamline.resolve(key, namespace="ps")
        design = group.read()
        if value == 0 or design == 0:
            continue
        if isinstance(group.elements[0], SBend):
            assert sascha_sign(group.elements[0]) == -1.0
            flipped += 1
        elif isinstance(group.elements[0], Quadrupole):
            assert sascha_sign(group.elements[0]) == 1.0
            same += 1
    assert flipped == 10
    assert same > 90


# --------------------------------------------------------------------------- #
# A beamline is a sequence
# --------------------------------------------------------------------------- #


def test_a_beamline_goes_into_magnetic_lattice_where_a_list_would(beamline):
    """The point of the sequence protocol: no `.cell` at the call site."""
    from ocelot.cpbd.magnetic_lattice import MagneticLattice

    direct = MagneticLattice(beamline)
    via_list = MagneticLattice(beamline.cell)
    assert len(direct.sequence) == len(beamline)
    assert all(x is y for x, y in zip(direct.sequence, via_list.sequence, strict=True))


def test_subscripting_dispatches_on_the_key(beamline):
    """An int means a position, a string means a name."""
    assert beamline[0] is beamline.cell[0]
    assert [e.id for e in beamline[:3]] == [e.id for e in beamline.cell[:3]]
    assert beamline["QI.1.I1"] == beamline.resolve("QI.1.I1")


def test_membership_answers_for_names_as_well_as_elements(beamline):
    """`Sequence` alone would compare the string to each element and say no."""
    assert "QI.46.I1" in beamline  # an element id
    assert "QI.1.I1" in beamline  # a power supply
    assert "QI.999.XX" not in beamline
    assert beamline[0] in beamline


def test_the_cell_property_is_a_copy_of_the_list_but_not_of_the_elements(beamline):
    """So it can be concatenated, but writing through it still reaches here."""
    detached = beamline.cell
    detached.append(None)
    assert len(beamline) == len(detached) - 1
    assert beamline.cell[0] is beamline[0]


# --------------------------------------------------------------------------- #
# Addressing
# --------------------------------------------------------------------------- #


def test_element_id_and_power_supply_reach_the_same_magnet(beamline):
    """QI.1.I1 is a supply feeding only QI.46.I1, so both names mean it."""
    by_supply = beamline.resolve("QI.1.I1", namespace="ps")
    by_id = beamline.resolve("QI.46.I1", namespace="id")
    assert by_supply.ids == by_id.ids == ("QI.46.I1",)


def test_supply_feeding_four_dipoles_sets_all_four(beamline):
    """`ignore_knob` because this is about the polarity pattern, not the drifts."""
    group = beamline.resolve("BB.1.I1")
    assert len(group) == 4
    group.write(0.1, ignore_knob=True)
    assert [round(read_kick(e), 9) for e in group.elements] == [0.1, -0.1, -0.1, 0.1]


def test_unknown_key_suggests_a_near_miss(beamline):
    with pytest.raises(UnknownKeyError, match="not a known"):
        beamline.resolve("QI.999.XX")


def test_a_name_in_both_namespaces_is_never_ambiguous(beamline):
    """59 names are both an element and a supply; all agree, so none raises."""
    overlapping = [
        supply for supply in beamline.supplies if _resolves_as_id(beamline, supply)
    ]
    assert overlapping, "expected some names to appear in both namespaces"
    for name in overlapping:
        assert beamline.resolve(name).ids == (name,)


def _resolves_as_id(beamline, key):
    try:
        beamline.resolve(key, namespace="id")
    except (UnknownKeyError, AmbiguousKeyError):
        # A handful of ids repeat across the branches (fast kickers), and a
        # repeated id cannot be addressed on its own.
        return False
    return True


# --------------------------------------------------------------------------- #
# Reading is free, writing is guarded
# --------------------------------------------------------------------------- #


def test_every_element_id_resolves_even_when_it_shares_a_supply(beamline):
    """Looking a magnet up is harmless, so nothing about a name refuses it."""
    group = beamline.resolve("BB.96.I1")
    assert group.ids == ("BB.96.I1",)
    assert group.split_from == "BB.1.I1"
    assert group.owned_by == "bc0"
    assert group.read() != 0


def test_setting_one_magnet_of_a_shared_supply_raises_and_names_its_siblings(beamline):
    """QI.73.I1 and QI.78.I1 are both on QI.18.I1; neither moves alone."""
    group = beamline.resolve("QI.73.I1")
    assert group.split_from == "QI.18.I1"
    assert group.owned_by is None, "wanted the ganged guard, not the geometry one"
    with pytest.raises(GangedMagnetError) as error:
        group.write(0.1)
    message = str(error.value)
    assert "QI.18.I1" in message
    assert "QI.78.I1" in message


def test_writing_a_chicane_supply_refuses_and_names_the_knob(beamline):
    """The 5.9 mm survey error the guard exists to prevent."""
    with pytest.raises(KnobOwnedError) as error:
        beamline["BB.1.I1"].write(0.1366)
    message = str(error.value)
    assert "bc0" in message
    assert "setpoints.bc0.r56" in message


def test_writing_one_chicane_dipole_refuses_for_the_geometry_first(beamline):
    """It is both ganged and knob-owned; the knob is the more useful answer."""
    with pytest.raises(KnobOwnedError, match="bc0"):
        beamline["BB.96.I1"].write(0.1366)


def test_ignore_knob_writes_anyway(beamline):
    """The escape hatch `apply` uses for the laser heater."""
    group = beamline["BB.1.I1"]
    group.write(0.1366, ignore_knob=True)
    assert round(abs(group.read()), 6) == 0.1366


@pytest.mark.parametrize("name", ["lh", "bc0", "bc1", "bc2"])
def test_every_chicane_supply_is_owned(name, beamline):
    """Including the laser heater's three, which is why apply must bypass."""
    for supply in CHICANES[name].supplies:
        assert beamline[supply].owned_by == name


def test_cavity_supplies_are_not_owned(beamline):
    """Only geometry is guarded -- a cavity voltage has no drifts to move."""
    assert beamline["C.A2.L1"].owned_by is None
    beamline["C.A2.L1"].write(0.1)


def test_the_explicit_id_form_splits_a_shared_supply(cell):
    """An `id:` key in a file is an explicit request, so it still goes through."""
    beamline = MachineSetpoints(elements={"id:BB.96.I1": 0.12}).build(cell)
    assert round(beamline.resolve("BB.96.I1").read(), 6) == 0.12


def test_a_split_supply_cannot_be_exported_to_sascha(cell):
    setpoints = MachineSetpoints(elements={"id:BB.96.I1": 0.12})
    with pytest.raises(ValueError, match="one value per supply"):
        setpoints.to_sascha(cell)


# --------------------------------------------------------------------------- #
# Design ratios
# --------------------------------------------------------------------------- #


def test_opposite_wiring_survives_a_setpoint(beamline):
    """QE.1.L3 is wired [+, -, +]; a single setpoint must not flatten it."""
    group = beamline.resolve("QE.1.L3")
    assert group.factors == (1.0, -1.0, 1.0)
    group.write(0.2)
    assert [round(read_kick(e), 9) for e in group.elements] == [0.2, -0.2, 0.2]


def test_unequal_magnets_keep_their_design_ratio(beamline):
    """QF.4.T5 pairs a 0.118 quadrupole with a 0.262 one on one supply."""
    group = beamline.resolve("QF.4.T5")
    before = [read_kick(e) for e in group.elements]
    ratio = before[1] / before[0]
    assert not math.isclose(abs(ratio), 1.0, rel_tol=0.1)

    group.write(group.read() * 2)
    after = [read_kick(e) for e in group.elements]
    assert math.isclose(after[1] / after[0], ratio, rel_tol=1e-12)


def test_applying_the_design_setpoint_changes_nothing_anywhere(beamline):
    """The strongest single check that the ratios were captured correctly."""
    changed = []
    for supply in beamline.supplies:
        group = beamline.group(supply)
        try:
            before = [read_kick(e) for e in group.elements]
            group.write(group.read())
            after = [read_kick(e) for e in group.elements]
        except Exception:
            continue
        if any(a != b for a, b in zip(before, after)):
            changed.append(supply)
    assert not changed


def test_applying_twice_equals_applying_once(beamline):
    group = beamline.resolve("QF.4.T5")
    group.write(0.3)
    once = [read_kick(e) for e in group.elements]
    group.write(0.3)
    assert [read_kick(e) for e in group.elements] == once


def test_partly_unpowered_supplies_are_reported_once(cell):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        beamline = Beamline.from_cell(cell)
    zero_warnings = [w for w in caught if "zero design kick" in str(w.message)]
    assert len(zero_warnings) == 1
    assert beamline.partly_unpowered


# --------------------------------------------------------------------------- #
# Chicanes
# --------------------------------------------------------------------------- #


def survey_end(beamline, dipoles):
    _, end = MagneticLattice(beamline, start=dipoles[0], stop=dipoles[3]).survey()
    return end[-1]


@pytest.mark.parametrize("name", ["bc0", "bc1", "bc2"])
def test_requested_r56_is_reached_exactly(name, beamline):
    spec = CHICANES[name]
    dipoles, _ = chicane_dipoles(beamline, spec)
    ChicaneKnob(r56=-0.020).apply(beamline, spec)
    assert measure_r56(beamline, dipoles, spec.energy) == pytest.approx(
        -0.020, abs=1e-12
    )


@pytest.mark.parametrize("name", ["bc0", "bc1", "bc2"])
def test_changing_r56_leaves_the_chicane_geometry_closed(name, beamline):
    """The magnets are bolted down: only the path between them may change."""
    spec = CHICANES[name]
    dipoles, _ = chicane_dipoles(beamline, spec)
    before = survey_end(beamline, dipoles)

    ChicaneKnob(r56=-0.020).apply(beamline, spec)
    after = survey_end(beamline, dipoles)

    for axis in ("X", "Y", "Z", "THETA", "PHI"):
        assert after[axis] == pytest.approx(before[axis], abs=1e-7)


@pytest.mark.parametrize("name", ["bc0", "bc1", "bc2"])
def test_the_three_ways_of_setting_a_chicane_agree(name, beamline):
    spec = CHICANES[name]
    dipoles, _ = chicane_dipoles(beamline, spec)

    ChicaneKnob(r56=-0.025).apply(beamline, spec)
    reference = ChicaneKnob().report(beamline, spec)

    ChicaneKnob(angle=reference.angle).apply(beamline, spec)
    assert measure_r56(beamline, dipoles, spec.energy) == pytest.approx(
        -0.025, abs=1e-9
    )

    ChicaneKnob(rho=reference.rho).apply(beamline, spec)
    assert measure_r56(beamline, dipoles, spec.energy) == pytest.approx(
        -0.025, abs=1e-9
    )


def test_only_drifts_absorb_a_chicane_change(beamline):
    spec = CHICANES["bc2"]
    dipoles, _ = chicane_dipoles(beamline, spec)
    shoulder = beamline.between(dipoles[0], dipoles[1])
    non_drift = {id(e): e.l for e in shoulder if not isinstance(e, Drift)}

    ChicaneKnob(r56=-0.020).apply(beamline, spec)

    for element in shoulder:
        if id(element) in non_drift:
            assert element.l == non_drift[id(element)]


def test_setting_a_chicane_dipole_directly_still_rescales_the_drifts(cell):
    """A plain BB.1.I1 entry is what a control-room file contains."""
    spec = CHICANES["bc0"]

    by_element = MachineSetpoints(elements={"BB.1.I1": 0.1366592804})
    by_knob = MachineSetpoints(knobs={"bc0": {"angle": 0.1366592804}})

    from_element = Beamline.from_cell(cell)
    by_element.apply(from_element)
    from_knob = Beamline.from_cell(cell)
    by_knob.apply(from_knob)

    a, _ = chicane_dipoles(from_element, spec)
    b, _ = chicane_dipoles(from_knob, spec)
    assert [d.angle for d in a] == [d.angle for d in b]
    assert [d.l for d in a] == [d.l for d in b]
    assert [e.l for e in from_element.between(a[0], a[1])] == [
        e.l for e in from_knob.between(b[0], b[1])
    ]


def test_setting_a_chicane_twice_over_is_rejected(cell, beamline):
    setpoints = MachineSetpoints(
        knobs={"bc0": {"r56": -0.03}}, elements={"BB.1.I1": 0.1366592804}
    )
    with pytest.raises(ConflictError, match="both set the same hardware"):
        setpoints.apply(beamline)


def test_a_bend_outside_any_knob_warns_that_the_survey_moves(beamline):
    """BL.6.I1 is part of the I1 dogleg, not a chicane."""
    setpoints = MachineSetpoints(elements={"BL.6.I1": -0.111})
    with pytest.warns(UserWarning, match="survey downstream"):
        setpoints.apply(beamline)


# --------------------------------------------------------------------------- #
# Knob round trips
# --------------------------------------------------------------------------- #


def test_linac_knob_round_trips(beamline):
    spec = LINACS["l1"]
    knob = LinacKnob(sum_voltage=0.57872, chirp=-9.1)
    knob.apply(beamline, spec)
    back = knob.read(beamline, spec)
    assert back.sum_voltage == pytest.approx(0.57872, abs=1e-12)
    assert back.chirp == pytest.approx(-9.1, abs=1e-12)


def test_injector_knob_round_trips(beamline):
    knob = InjectorRFKnob(E1=0.130, chirp=-8.92, curvature=180.5, skewness=20332)
    knob.apply(beamline, INJECTOR)
    back = knob.read(beamline, INJECTOR)
    assert back.E1 == pytest.approx(0.130, rel=1e-12)
    assert back.chirp == pytest.approx(-8.92, rel=1e-12)
    assert back.curvature == pytest.approx(180.5, rel=1e-9)
    assert back.skewness == pytest.approx(20332, rel=1e-9)


def test_chicane_knob_round_trips(beamline):
    spec = CHICANES["bc1"]
    ChicaneKnob(r56=-0.0432).apply(beamline, spec)
    back = ChicaneKnob().report(beamline, spec)
    assert back.r56 == pytest.approx(-0.0432, abs=1e-12)
    dipoles, _ = chicane_dipoles(beamline, spec)
    assert back.angle == pytest.approx(abs(dipoles[0].angle))
    assert back.rho == pytest.approx(yoke_length(dipoles[0]) / math.sin(back.angle))


# --------------------------------------------------------------------------- #
# Schema
# --------------------------------------------------------------------------- #


def test_a_misspelt_knob_parameter_is_rejected():
    with pytest.raises(Exception, match="chrip"):
        LinacKnob(chrip=-9.1)


def test_setting_two_chicane_parameters_at_once_is_rejected():
    with pytest.raises(Exception, match="exactly one"):
        ChicaneKnob(r56=-0.03, angle=0.04)


def test_assigning_a_chicane_parameter_clears_the_others():
    knob = ChicaneKnob(r56=-0.03)
    knob.angle = 0.04
    assert knob.r56 is None
    assert knob.angle == 0.04


def test_exponent_notation_yaml_survives_as_a_number(tmp_path):
    """PyYAML reads 1e-3 as a string; pydantic coercion has to absorb that."""
    path = tmp_path / "exponents.yaml"
    path.write_text("knobs:\n  bc2: {r56: -3e-2}\n")
    assert MachineSetpoints.from_yaml(path).bc2.r56 == pytest.approx(-0.03)


def test_a_half_specified_knob_is_not_silently_ignored(beamline):
    setpoints = MachineSetpoints()
    setpoints.l1.chirp = -9.1
    with pytest.raises(ConflictError, match="missing sum_voltage"):
        setpoints.apply(beamline)


def test_an_unknown_element_attribute_is_rejected(beamline):
    setpoints = MachineSetpoints(elements={"QI.63.I1D": {"kl": -2.9}})
    with pytest.raises(AttributeError, match="no 'kl' parameter"):
        setpoints.apply(beamline)


def test_valid_attributes_come_from_the_element_signature():
    attributes = valid_attributes(Quadrupole())
    assert {"l", "k1", "k2", "tilt"} <= attributes
    assert "eid" not in attributes


# --------------------------------------------------------------------------- #
# The Python object, files and layering
# --------------------------------------------------------------------------- #


def test_building_never_touches_the_callers_elements(cell):
    """The generated cells are shared by every section in the process."""
    dipole = next(e for e in cell if e.id == "BB.96.I1")
    quadrupole = next(e for e in cell if e.id == "QI.46.I1")
    before = (dipole.angle, dipole.l, quadrupole.k1)

    MachineSetpoints(knobs={"bc0": {"r56": -0.02}}, elements={"QI.1.I1": -0.9}).build(
        cell
    )

    assert (dipole.angle, dipole.l, quadrupole.k1) == before


def test_the_python_object_and_the_yaml_agree(cell, tmp_path):
    built_in_python = MachineSetpoints()
    built_in_python.bc2.r56 = -0.0432
    built_in_python.l1.sum_voltage = 0.57872
    built_in_python.l1.chirp = -9.1
    built_in_python["QI.1.I1"] = -0.05343

    path = tmp_path / "setpoints.yaml"
    path.write_text(
        "knobs:\n"
        "  bc2: {r56: -0.0432}\n"
        "  l1: {sum_voltage: 0.57872, chirp: -9.1}\n"
        "elements:\n"
        "  QI.1.I1: -0.05343\n"
    )
    from_file = MachineSetpoints.from_yaml(path)

    assert built_in_python.resolve(cell) == from_file.resolve(cell)


def test_a_knob_scan_does_not_accumulate(cell):
    setpoints = MachineSetpoints()
    results = []
    for r56 in (-0.020, -0.025, -0.030):
        setpoints.bc2.r56 = r56
        beamline = Beamline.from_cell(cell)
        setpoints.apply(beamline)
        dipoles, _ = chicane_dipoles(beamline, CHICANES["bc2"])
        results.append(measure_r56(beamline, dipoles, CHICANES["bc2"].energy))

    assert results == pytest.approx([-0.020, -0.025, -0.030], abs=1e-12)


def test_extends_overrides_only_what_the_child_names(tmp_path, cell):
    (tmp_path / "base.yaml").write_text(
        "knobs:\n"
        "  bc2: {r56: -0.030}\n"
        "  l1: {sum_voltage: 0.5, chirp: -9.0}\n"
        "elements:\n"
        "  QI.1.I1: -0.05\n"
        "  QI.2.I1: 0.16\n"
    )
    child = tmp_path / "child.yaml"
    child.write_text(
        "extends: base.yaml\nknobs:\n  bc2: {r56: -0.015}\nelements:\n  QI.1.I1: -0.07\n"
    )

    setpoints = MachineSetpoints.from_yaml(child)
    assert setpoints.bc2.r56 == pytest.approx(-0.015)
    assert setpoints.l1.sum_voltage == pytest.approx(0.5)
    assert setpoints.elements["QI.1.I1"] == pytest.approx(-0.07)
    assert setpoints.elements["QI.2.I1"] == pytest.approx(0.16)


def test_extends_is_single_level(tmp_path):
    (tmp_path / "a.yaml").write_text("name: a\n")
    (tmp_path / "b.yaml").write_text("extends: a.yaml\nname: b\n")
    (tmp_path / "c.yaml").write_text("extends: b.yaml\nname: c\n")
    with pytest.raises(ValueError, match="single level"):
        MachineSetpoints.from_yaml(tmp_path / "c.yaml")


def test_a_stale_resolved_block_warns(cell, beamline):
    setpoints = MachineSetpoints(
        elements={"QI.1.I1": -0.05343},
        resolved={"QI.1.I1": -0.9},
    )
    with pytest.warns(UserWarning, match="no longer resolve"):
        setpoints.apply(beamline)


def test_reading_an_optics_back_off_a_lattice(cell):
    written = MachineSetpoints(knobs={"bc2": {"r56": -0.0255}})
    rebuilt = MachineSetpoints.from_lattice(written.build(cell))
    assert rebuilt.bc2.r56 == pytest.approx(-0.0255, abs=1e-9)


# --------------------------------------------------------------------------- #
# Start-to-end tracking: the lattice is owned by the setpoints
# --------------------------------------------------------------------------- #


def build_section_lattice(section_names, tmp_path):
    """A SectionLattice over the given sections, reading the module-level cells."""
    from ocelot.cpbd.beam import Twiss

    from euxfel import sections
    from euxfel.section_track import SectionLattice

    tws0 = Twiss()
    tws0.E = 0.005
    tws0.beta_x = tws0.beta_y = 0.2865426867699372
    tws0.alpha_x = tws0.alpha_y = -0.8390696483216487
    classes = [getattr(sections, name) for name in section_names]
    return SectionLattice(sequence=classes, tws0=tws0, data_dir=str(tmp_path))


def test_a_config_that_still_sets_the_machine_is_rejected(tmp_path):
    """Silently ignoring 'rho' would let a run finish at design compression."""
    from euxfel import sections

    section_lat = build_section_lattice(["A1"], tmp_path)
    with pytest.raises(ValueError, match="no longer belong in the section config"):
        section_lat.update_sections([sections.A1], config={sections.A1: {"rho": 3.6}})
    with pytest.raises(ValueError, match="MachineSetpoints"):
        section_lat.update_sections(
            [sections.A1], config={sections.A1: {"v": 0.018, "phi": 12.0}}
        )


def test_rf_matches_what_update_cavity_used_to_produce(beamline):
    """Moving RF out of section_track must not change a single cavity."""
    from ocelot.utils.acc_utils import beam2rf_xfel_linac

    spec = LINACS["l1"]
    LinacKnob(sum_voltage=0.57872, chirp=-9.1).apply(beamline, spec)

    total, phase = beam2rf_xfel_linac(
        sum_voltage=0.57872, chirp=-9.1, init_energy=spec.init_energy
    )
    cavities = beamline.group("C.A2.L1").elements
    for cavity in cavities:
        assert cavity.v == total / len(cavities)  # what update_cavity did
        assert cavity.phi == phase


def test_the_chicane_angle_survives_a_section_lattice(
    tmp_path, cell, restores_the_lattice
):
    """Nothing re-derives the angle from a radius any more, so it is exact."""
    from euxfel import sections

    setpoints = MachineSetpoints(knobs={"bc0": {"r56": -0.045}})
    setpoints.apply_in_place(cell)

    wanted = abs(next(e for e in cell if e.id == "BB.96.I1").angle)
    section_lat = build_section_lattice(["BC0"], tmp_path)
    section_lat.update_sections([sections.BC0], config={sections.BC0: {"SC": False}})

    dipoles = [
        e
        for e in section_lat.dict_sections[sections.BC0].lattice.sequence
        if e.id.startswith("BB.")
    ]
    assert dipoles
    for dipole in dipoles:
        assert abs(dipole.angle) == pytest.approx(wanted, abs=1e-12)


def test_a_chicane_still_closes_after_a_section_lattice(
    tmp_path, cell, restores_the_lattice
):
    """Dropping change_bc_shoulders must not lose the drift rescaling."""

    before = Beamline.from_cell(cell)
    dipoles_before, _ = chicane_dipoles(before, CHICANES["bc0"])
    reference = survey_end(before, dipoles_before)

    setpoints = MachineSetpoints(knobs={"bc0": {"r56": -0.045}})
    setpoints.apply_in_place(cell)
    build_section_lattice(["BC0"], tmp_path)

    after = Beamline.from_cell(cell)
    dipoles_after, _ = chicane_dipoles(after, CHICANES["bc0"])
    moved = survey_end(after, dipoles_after)
    for axis in ("X", "Y", "Z", "THETA"):
        assert moved[axis] == pytest.approx(reference[axis], abs=1e-7)


# --------------------------------------------------------------------------- #
# Transverse deflecting structures
# --------------------------------------------------------------------------- #


def test_tds_knob_round_trips(beamline):
    from euxfel.volts.knobs import TDSKnob
    from euxfel.machine import TDS

    knob = TDSKnob(voltage=0.004, phase=90.0)
    knob.apply(beamline, TDS["b1_tds"])
    back = knob.read(beamline, TDS["b1_tds"])
    assert back.voltage == pytest.approx(0.004)
    assert back.phase == pytest.approx(90.0)


def test_one_supply_drives_both_b2_structures(beamline):
    """TDSB.B2 feeds TDSB.428.B2 and TDSB.430.B2, so both must move."""
    from euxfel.volts.knobs import TDSKnob
    from euxfel.machine import TDS

    group = beamline.resolve("TDSB.B2", namespace="ps")
    assert set(group.ids) == {"TDSB.428.B2", "TDSB.430.B2"}

    TDSKnob(voltage=0.006, phase=0.0).apply(beamline, TDS["b2_tds"])
    assert [s.v for s in group.elements] == [0.003, 0.003]


def test_the_tds_are_off_in_the_design_lattice(beamline):
    for supply in ("TDSA.I1", "TDSB.B1", "TDSB.B2"):
        assert all(s.v == 0.0 for s in beamline.resolve(supply).elements)


def test_the_shipped_example_optics_matches_its_source(cell):
    """special-optics-files/bc2_tds.yaml is BC2_TDS.txt in the new format."""
    from_yaml = MachineSetpoints.from_yaml(SASCHA_DIR / "bc2_tds.yaml")
    from_txt = MachineSetpoints.from_sascha(SASCHA_DIR / "BC2_TDS.txt", cell)
    assert from_yaml.resolve(cell) == from_txt.resolve(cell)


def test_design_ratios_survive_a_supply_passing_through_zero(cell):
    """apply_in_place overwrites the data the ratios are derived from.

    Once QE.1.L3's three magnets are all at zero, nothing in the lattice says it
    is wired [+, -, +] any more, so the ratios have to be remembered rather than
    re-read.
    """
    beamline = Beamline.from_cell(cell)
    group = beamline.resolve("QE.1.L3")
    assert group.factors == (1.0, -1.0, 1.0)

    group.write(0.0)
    assert [read_kick(e) for e in group.elements] == [0.0, -0.0, 0.0]

    # A fresh beamline over the zeroed lattice: nothing left to infer from.
    zeroed = Beamline.from_cell(beamline, copy_elements=False)
    again = zeroed.resolve("QE.1.L3")
    assert again.factors == (1.0, -1.0, 1.0)

    again.write(0.2)
    assert [round(read_kick(e), 9) for e in again.elements] == [0.2, -0.2, 0.2]


def test_clearing_the_cache_makes_the_ratios_be_re_read(cell):
    from euxfel import clear_design_factors

    beamline = Beamline.from_cell(cell)
    group = beamline.resolve("QE.1.L3")
    group.write(0.0)

    clear_design_factors()
    try:
        stale = Beamline.from_cell(beamline, copy_elements=False)
        # Re-read from an all-zero group, the ratios are genuinely unrecoverable.
        assert stale.resolve("QE.1.L3").factors == (1.0, 1.0, 1.0)
    finally:
        # Leave the cache populated from a pristine lattice for later tests.
        clear_design_factors()
        Beamline.from_cell(all_machine_elements())


# --------------------------------------------------------------------------- #
# The migrated s2e scripts
# --------------------------------------------------------------------------- #

SETPOINT_FILES = Path(__file__).parent.parent / "s2e_scripts" / "setpoints"


def test_the_nominal_setpoints_reproduce_the_scripts_rf_exactly(cell):
    """The whole point of the migration: not one cavity moves.

    Every number in nominal_14gev.yaml was a beam2rf argument in the original
    scripts, so the per-cavity voltage and phase must come out bit-identical.
    """
    from ocelot.utils.acc_utils import beam2rf, beam2rf_xfel_linac

    from euxfel.volts import load_setpoints

    gun = 0.0065
    setpoints = load_setpoints(SETPOINT_FILES / "nominal_14gev.yaml")
    setpoints.i1.gun_energy = gun
    beamline = Beamline.from_cell(cell)
    setpoints.apply(beamline)

    v11, phi11, v13, phi13 = beam2rf(
        E1=0.130,
        chirp=-8.92,
        curvature=180.5,
        skewness=20332,
        n=3,
        freq=1.3e9,
        E0=gun,
    )
    v21, phi21 = beam2rf_xfel_linac(sum_voltage=0.57872, chirp=-9.1, init_energy=0.13)
    v31, phi31 = beam2rf_xfel_linac(sum_voltage=1.7349, chirp=-9.3, init_energy=0.7)

    expected = {
        "C.A1.I1": (v11 / 8, phi11),  # was v11 / 8 in the script
        "C3.AH1.I1": (v13 / 8, phi13),
        "C.A2.L1": (v21 / 32, phi21),
        "C.A3.L2": (v31 / 96, phi31),
        "C.A6.L3": (11.6 / 640, 0.0),  # was v41 * 1e-3 / 640
    }
    for supply, (voltage, phase) in expected.items():
        for cavity in beamline.resolve(supply, namespace="ps").elements:
            assert cavity.v == voltage
            assert cavity.phi == phase


def test_the_nominal_setpoints_use_the_bkr_chicane_angles(cell):
    """Where the originals were 0.31 % / 0.047 % / 0.028 % off."""
    from euxfel.volts import load_setpoints

    beamline = Beamline.from_cell(cell)
    load_setpoints(SETPOINT_FILES / "nominal_14gev.yaml").apply(beamline)

    for supply, bkr in (
        ("BB.1.I1", 0.1366592804),
        ("BB.1.B1", 0.0532325422),
        ("BB.1.B2", 0.0411897704),
    ):
        for dipole in beamline.resolve(supply, namespace="ps").elements:
            assert abs(dipole.angle) == pytest.approx(bkr, abs=1e-12)


def test_the_dx12_file_reproduces_the_old_quadrupole_loop(cell):
    """DX12_I1D.txt replaces a loop that assigned k1 directly.

    Two conversions happen at once -- k1 to a generalised kick, and element id
    to power supply -- so this pins both.  The tolerance is the Sascha format's
    six decimal places, which quantises k1 by at most 2.6e-7 relative here.
    """
    original = {
        "QI.55.I1": -2.9974,
        "QI.57.I1": 2.9974,
        "QI.59.I1": -2.9974,
        "QI.61.I1": -2.14371,
        "QI.63.I1D": -1.05,
        "QI.64.I1D": 3.5,
    }
    beamline = Beamline.from_cell(cell)
    values = read_sascha(SASCHA_DIR / "DX12_I1D.txt")

    for supply, kick in values.items():
        if supply == "QI.62.I1":
            continue  # deliberately unresolvable; see the test below
        beamline.resolve(supply, namespace="ps").write(kick)

    for name, k1 in original.items():
        assert beamline.resolve(name, namespace="id").elements[0].k1 == pytest.approx(
            k1, rel=1e-6
        )


def test_the_dx12_file_still_names_a_magnet_that_does_not_exist(cell):
    """QI.62.I1 was silently skipped by the old loop; now it fails loudly."""
    from euxfel.volts import MachineSetpoints

    assert "QI.62.I1" in read_sascha(SASCHA_DIR / "DX12_I1D.txt")
    with pytest.raises(UnknownKeyError, match="QI.62.I1"):
        MachineSetpoints.from_sascha(SASCHA_DIR / "DX12_I1D.txt", cell)


# --------------------------------------------------------------------------- #
# The laser heater chicane, which spans three power supplies
# --------------------------------------------------------------------------- #


def test_a_chicane_can_span_several_supplies(beamline):
    """LH's four dipoles sit on BL.1.I1 (two of them), BL.3.I1 and BL.4.I1."""
    dipoles, _ = chicane_dipoles(beamline, CHICANES["lh"])
    assert [d.id for d in dipoles] == [
        "BL.48I.I1",
        "BL.48II.I1",
        "BL.50I.I1",
        "BL.50II.I1",
    ]
    assert {d.ps_id for d in dipoles} == {"BL.1.I1", "BL.3.I1", "BL.4.I1"}


def test_polarity_comes_from_design_kicks_not_per_supply_ratios(beamline):
    """The ratios within each supply are (1, -1), (1,) and (1,).

    Concatenating those would give [+, -, +, +]; the chicane is [-, +, +, -].
    Only the design kicks place the supplies against each other.
    """
    _, factors = chicane_dipoles(beamline, CHICANES["lh"])
    assert [f > 0 for f in factors] == [False, True, True, False]

    ChicaneKnob(angle=0.05).apply(beamline, CHICANES["lh"])
    dipoles, _ = chicane_dipoles(beamline, CHICANES["lh"])
    assert [round(d.angle, 9) for d in dipoles] == [-0.05, 0.05, 0.05, -0.05]


def test_the_lh_knob_reaches_a_requested_r56(beamline):
    spec = CHICANES["lh"]
    ChicaneKnob(r56=-0.002).apply(beamline, spec)
    dipoles, _ = chicane_dipoles(beamline, spec)
    assert measure_r56(beamline, dipoles, spec.energy) == pytest.approx(
        -0.002, abs=1e-12
    )


@pytest.mark.parametrize("path", SASCHA_FILES, ids=lambda p: p.name)
def test_an_asymmetric_lh_chicane_is_not_routed(path, cell):
    """Every shipped file runs BL.3.I1 about 1.75 % weak against its partners.

    Folding that into one angle would discard a setting the machine is really
    running, so those magnets are set individually instead and the file still
    round trips byte for byte.
    """
    values = read_sascha(path)
    magnitudes = {round(abs(values[s]), 9) for s in ("BL.1.I1", "BL.3.I1", "BL.4.I1")}
    assert len(magnitudes) > 1, "expected the shipped files to be asymmetric here"

    with pytest.warns(UserWarning, match="spans 3 power supplies"):
        setpoints = MachineSetpoints.from_sascha(path, cell)
        exported = setpoints.to_sascha(cell, keys=list(values))
    assert exported == path.read_text()


def test_a_symmetric_multi_supply_chicane_does_route(cell):
    """When the supplies agree, the knob takes it as one angle."""
    setpoints = MachineSetpoints(
        elements={"BL.1.I1": -0.08, "BL.3.I1": 0.08, "BL.4.I1": -0.08}
    )
    beamline = Beamline.from_cell(cell)
    setpoints.apply(beamline)

    dipoles, _ = chicane_dipoles(beamline, CHICANES["lh"])
    assert [round(abs(d.angle), 9) for d in dipoles] == [0.08] * 4
    # Routed, so the drifts moved with it and the chicane still closes.
    end = survey_end(beamline, dipoles)
    assert end["X"] == pytest.approx(0.0, abs=1e-7)


# --------------------------------------------------------------------------- #
# Per-module RF
# --------------------------------------------------------------------------- #


def test_every_module_is_derived_from_a_linac_or_the_injector():
    """The module list is derived, not listed, so it cannot drift."""
    from euxfel.machine import INJECTOR, LINACS, MODULES

    supplies = {spec.supply for spec in MODULES.values()}
    expected = {s for linac in LINACS.values() for s in linac.supplies}
    expected |= {INJECTOR.fundamental, INJECTOR.harmonic}
    assert supplies == expected
    assert MODULES["A7"].linac == "l3"
    assert MODULES["AH1"].linac == "i1"


def test_a_module_can_be_set_on_its_own(cell):
    from euxfel.volts.knobs import RFModuleKnob

    setpoints = MachineSetpoints()
    setpoints.modules["A7"] = RFModuleKnob(voltage=0.5, phase=10.0)
    beamline = Beamline.from_cell(cell)
    setpoints.apply(beamline)

    a7 = beamline.resolve("C.A7.L3", namespace="ps").elements
    assert len(a7) == 32
    assert all(c.v == pytest.approx(0.5 / 32) for c in a7)
    assert all(c.phi == 10.0 for c in a7)

    # Its neighbours in the same linac are untouched.
    a6 = beamline.resolve("C.A6.L3", namespace="ps").elements
    assert all(c.v == pytest.approx(0.018125) for c in a6)


def test_a_module_and_its_linac_cannot_both_be_set(cell, beamline):
    """Otherwise the result depends on which is applied last."""
    from euxfel.volts.knobs import RFModuleKnob

    setpoints = MachineSetpoints()
    setpoints.modules["A7"] = RFModuleKnob(voltage=0.5, phase=0.0)
    setpoints.l3.sum_voltage, setpoints.l3.chirp = 11.6, 0.0

    with pytest.raises(ConflictError, match="both set"):
        setpoints.apply(beamline)


def test_a_module_knob_round_trips(beamline):
    from euxfel.volts.knobs import RFModuleKnob
    from euxfel.machine import MODULES

    knob = RFModuleKnob(voltage=0.42, phase=-15.0)
    knob.apply(beamline, MODULES["A4"])
    back = knob.read(beamline, MODULES["A4"])
    assert back.voltage == pytest.approx(0.42)
    assert back.phase == pytest.approx(-15.0)


def test_modules_serialise_under_their_own_key(tmp_path, cell):
    from euxfel.volts.knobs import RFModuleKnob

    setpoints = MachineSetpoints()
    setpoints.modules["A7"] = RFModuleKnob(voltage=0.5, phase=10.0)
    path = tmp_path / "one_module.yaml"
    setpoints.to_yaml(path)

    assert "modules:" in path.read_text()
    reloaded = MachineSetpoints.from_yaml(path)
    assert reloaded.modules["A7"].voltage == pytest.approx(0.5)
    assert reloaded.resolve(cell) == setpoints.resolve(cell)


# --------------------------------------------------------------------------- #
# The compact setter
# --------------------------------------------------------------------------- #


def test_set_takes_several_parameters_at_once():
    setpoints = MachineSetpoints()
    setpoints.b2_tds.set(voltage=0.005, phase=90.0)
    assert setpoints.b2_tds.voltage == pytest.approx(0.005)
    assert setpoints.b2_tds.phase == pytest.approx(90.0)


def test_set_returns_the_knob_so_it_can_be_chained():
    setpoints = MachineSetpoints()
    assert setpoints.l1.set(sum_voltage=0.57872, chirp=-9.1) is setpoints.l1


def test_set_still_clears_a_chicane_s_other_parameters():
    """`.set(angle=...)` must behave like `.angle = ...`, not accumulate."""
    setpoints = MachineSetpoints()
    setpoints.bc2.set(r56=-0.03)
    assert setpoints.bc2.r56 == pytest.approx(-0.03)

    setpoints.bc2.set(angle=0.04)
    assert setpoints.bc2.angle == pytest.approx(0.04)
    assert setpoints.bc2.r56 is None


def test_set_refuses_two_ways_of_saying_the_same_thing():
    """Assigning both in turn would silently keep whichever came last."""
    setpoints = MachineSetpoints()
    with pytest.raises(ValueError, match="only one can be given"):
        setpoints.bc0.set(r56=-0.03, angle=0.04)


def test_set_names_the_valid_parameters_when_one_is_misspelt():
    setpoints = MachineSetpoints()
    with pytest.raises(ValueError, match="no parameter 'chrip'"):
        setpoints.l2.set(sum_voltage=1.7, chrip=-9.3)


# --------------------------------------------------------------------------- #
# The matched section
# --------------------------------------------------------------------------- #


def test_the_matched_section_is_every_supply_upstream_of_the_marker(beamline):
    """The membership rule, checked against the lattice rather than a list.

    Positional, not "the quadrupoles the converter solved for": the A1/AH1
    voltages and the laser heater are equally this model's own business.
    """
    spec = MATCHED_SECTIONS["i1"]
    expected = {}
    for element in beamline:
        if element.id == spec.marker:
            break
        supply = getattr(element, "ps_id", None)
        if supply:
            expected.setdefault(supply, "i1")

    assert beamline.matched_supplies == expected
    assert set(expected) == {
        "KIX.24.I1",
        "KIY.24.I1",
        "C.A1.I1",
        "C3.AH1.I1",
        "Q.A1.1.I1",
        "Q.AH1.1.I1",
        "QI.1.I1",
        "QI.2.I1",
        "QI.3.I1",
        "BL.1.I1",
        "BL.3.I1",
        "BL.4.I1",
    }


def test_a_sequence_without_the_marker_has_no_matched_section():
    """The bug the obvious loop has: no marker must mean nothing, not everything."""
    from euxfel.subsequences import l1

    assert Beamline.from_cell(l1.cell).matched_supplies == {}


def test_matched_by_reaches_a_magnet_as_well_as_its_supply(beamline):
    assert beamline["QI.1.I1"].matched_by == "i1"
    assert beamline["QI.46.I1"].matched_by == "i1"
    assert beamline["QI.4.I1"].matched_by is None


def test_writing_a_matched_magnet_is_still_free(beamline, restores_the_lattice):
    """Unlike the chicane guard: naming a magnet is choosing it."""
    beamline["QI.1.I1"].write(0.06)
    assert round(beamline["QI.1.I1"].read(), 6) == 0.06


@pytest.mark.parametrize("path", SASCHA_FILES, ids=lambda p: p.name)
def test_import_diverts_the_matched_section(path, cell):
    setpoints = MachineSetpoints.from_sascha(path, cell)
    assert set(setpoints.matching) == {
        "Q.A1.1.I1",
        "Q.AH1.1.I1",
        "QI.1.I1",
        "QI.2.I1",
        "QI.3.I1",
        "BL.1.I1",
        "BL.3.I1",
        "BL.4.I1",
    }
    assert not set(setpoints.matching) & set(setpoints.elements)


def test_build_holds_the_matched_section_and_says_so(cell):
    setpoints = MachineSetpoints.from_sascha(SASCHA_DIR / "BC2_TDS.txt", cell)
    design = Beamline.from_cell(cell)

    with pytest.warns(UserWarning, match="write_matching_section"):
        beamline = setpoints.build(cell)

    for supply in setpoints.matching:
        assert beamline[supply].read() == pytest.approx(design[supply].read())
    # ...while everything downstream of the marker did land.
    assert beamline["QI.4.I1"].read() == pytest.approx(setpoints.elements["QI.4.I1"])


@pytest.mark.parametrize("how", ["flag", "method"])
def test_both_opt_ins_write_the_matched_section(how, cell):
    setpoints = MachineSetpoints.from_sascha(SASCHA_DIR / "BC2_TDS.txt", cell)

    if how == "flag":
        beamline = setpoints.build(cell, matching=True)
    else:
        with pytest.warns(UserWarning, match="write_matching_section"):
            beamline = setpoints.build(cell)
        setpoints.write_matching_section(beamline)

    for supply, value in setpoints.matching.items():
        assert beamline[supply].read() == pytest.approx(value)


def test_naming_a_matched_supply_yourself_applies_it(cell):
    """Provenance: `elements` is what someone chose, `matching` is what was swept."""
    setpoints = MachineSetpoints(elements={"QI.1.I1": 0.06})
    beamline = setpoints.build(cell)
    assert beamline["QI.1.I1"].read() == pytest.approx(0.06)


def test_elements_beats_matching_for_the_same_supply(cell):
    setpoints = MachineSetpoints.from_sascha(SASCHA_DIR / "BC2_TDS.txt", cell)
    setpoints.elements["QI.1.I1"] = 0.06

    beamline = setpoints.build(cell, matching=True)
    assert beamline["QI.1.I1"].read() == pytest.approx(0.06)
    # The rest of the section is unaffected by one supply being claimed.
    assert beamline["QI.2.I1"].read() == pytest.approx(setpoints.matching["QI.2.I1"])


def test_holding_the_laser_heater_leaves_it_a_symmetric_chicane(cell):
    """The asymmetry warning is a property of the file, not of every load.

    All three shipped files run BL.3.I1 about 1.75% weak, which is why the `lh`
    knob refuses them.  Held, the chicane stays as this model built it.
    """
    setpoints = MachineSetpoints.from_sascha(SASCHA_DIR / "BC2_TDS.txt", cell)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        beamline = setpoints.build(cell)

    assert not any("not a symmetric chicane" in str(w.message) for w in caught)
    magnitudes = {
        round(abs(beamline[supply].read()), 9) for supply in ("BL.1.I1", "BL.3.I1")
    }
    assert len(magnitudes) == 1


def test_the_matched_section_still_exports(cell):
    """Holding is about what reaches a lattice, not about what a file contains."""
    path = SASCHA_DIR / "BC2_TDS.txt"
    setpoints = MachineSetpoints.from_sascha(path, cell)
    exported = setpoints.to_sascha(cell, keys=list(read_sascha(path)))
    assert exported == path.read_text()


def test_a_held_supply_is_not_reported_as_drifted(cell):
    """`resolved` records intent; holding is not the lattice changing underneath."""
    setpoints = MachineSetpoints.from_sascha(SASCHA_DIR / "BC2_TDS.txt", cell)
    setpoints.resolved = dict(setpoints.matching)

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        setpoints.build(cell)

    assert not any("no longer resolve" in str(w.message) for w in caught)


def test_holding_costs_beta_through_the_injector_but_not_at_the_marker(cell):
    """Why this exists: same match point, different route.

    Both sets of quadrupoles arrive at MATCH.52.I1 within bmag 1.03, so nothing
    downstream notices -- but the beam takes a visibly different path through
    the injector to get there, and that path is what an s2e run tracks.
    """
    from ocelot.cpbd.track import twiss

    from euxfel import sequences
    from euxfel.optics import bmag

    # Only the held part: the rest of the file names BC2 and the B2 dump, which
    # are genuinely not in this sequence.
    imported = MachineSetpoints.from_sascha(SASCHA_DIR / "BC2_TDS.txt", cell)
    setpoints = MachineSetpoints(matching=imported.matching)

    def optics(**kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            beamline = setpoints.build(sequences.cathode_to_b1d, **kwargs)
        return twiss(MagneticLattice(beamline), tws0=sequences.CATHODE_TWISS0)

    held, written = optics(), optics(matching=True)

    design, machine = (
        next(t for t in run if t.id == "MATCH.52.I1") for run in (held, written)
    )
    mismatch = bmag(machine.beta_y, machine.alpha_y, design.beta_y, design.alpha_y)
    assert mismatch == pytest.approx(1.03, abs=0.02)

    worst = max(
        abs(a.beta_y - b.beta_y) / a.beta_y
        for a, b in zip(held, written)
        if a.s < 29.2 and a.beta_y > 1e-6
    )
    assert worst > 0.15


# --------------------------------------------------------------------------- #
# The default cell
# --------------------------------------------------------------------------- #


def test_build_with_no_cell_is_the_whole_machine(cell):
    setpoints = MachineSetpoints(elements={"QI.4.I1": -0.08})
    assert len(setpoints.build()) == len(setpoints.build(cell))


def test_the_catalogue_holds_every_element_exactly_once(cell):
    """What `all_machine_elements` is for: no cathode_to_* sequence is complete."""
    from euxfel import sequences

    assert len({id(element) for element in cell}) == len(cell)
    longest = {id(element) for element in sequences.cathode_to_t5d}
    assert len({id(element) for element in cell} - longest) > 2000
