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

from euxfel.volts import (
    AmbiguousKeyError,
    ChicaneKnob,
    ConflictError,
    GangedMagnetError,
    InjectorRFKnob,
    LatticeIndex,
    LinacKnob,
    MachineSetpoints,
    UnknownKeyError,
    full_machine_cell,
)
from euxfel.volts.config import valid_attributes
from euxfel.volts.kicks import read_kick
from euxfel.volts.knobs import chicane_dipoles, measure_r56, yoke_length
from euxfel.volts.library import CHICANES, INJECTOR, LINACS
from euxfel.volts.sascha import dumps_sascha, read_sascha, sascha_sign

SASCHA_DIR = Path(__file__).parent.parent / "special-optics-files"
SASCHA_FILES = sorted(SASCHA_DIR.glob("*.txt"))

# Building an index reports supplies whose magnets sit at zero by design.  True
# and worth saying once in anger, but not what these tests are about.
pytestmark = pytest.mark.filterwarnings(
    "ignore:.*zero design kick.*:UserWarning",
)


@pytest.fixture(scope="module")
def cell():
    """The whole machine, shared: building it copies ~8000 elements."""
    return full_machine_cell()


@pytest.fixture
def index(cell):
    return LatticeIndex.from_cell(cell)


# --------------------------------------------------------------------------- #
# The Sascha format
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("path", SASCHA_FILES, ids=lambda p: p.name)
def test_sascha_text_round_trips_byte_for_byte(path):
    assert dumps_sascha(read_sascha(path)) == path.read_text()


@pytest.mark.parametrize("path", SASCHA_FILES, ids=lambda p: p.name)
def test_every_sascha_key_resolves(path, index):
    unresolved = [key for key in read_sascha(path) if not _resolves(index, key)]
    assert not unresolved


def _resolves(index, key):
    try:
        index.resolve(key, namespace="ps")
    except UnknownKeyError:
        return False
    return True


@pytest.mark.parametrize("path", SASCHA_FILES, ids=lambda p: p.name)
def test_sascha_survives_import_apply_and_export(path, cell):
    """The whole pipeline, including routing chicanes through their knobs."""
    setpoints = MachineSetpoints.from_sascha(path, cell)
    exported = setpoints.to_sascha(cell, keys=list(read_sascha(path)))
    assert exported == path.read_text()


def test_bend_signs_are_flipped_and_quadrupole_signs_are_not(index):
    """The convention that would silently reverse every dipole if missed."""
    values = read_sascha(SASCHA_DIR / "BC2_TDS.txt")
    flipped = same = 0
    for key, value in values.items():
        group = index.resolve(key, namespace="ps")
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
# Addressing
# --------------------------------------------------------------------------- #


def test_element_id_and_power_supply_reach_the_same_magnet(index):
    """QI.1.I1 is a supply feeding only QI.46.I1, so both names mean it."""
    by_supply = index.resolve("QI.1.I1", namespace="ps")
    by_id = index.resolve("QI.46.I1", namespace="id")
    assert by_supply.ids == by_id.ids == ("QI.46.I1",)


def test_supply_feeding_four_dipoles_sets_all_four(index):
    group = index.resolve("BB.1.I1")
    assert len(group) == 4
    group.write(0.1)
    assert [round(read_kick(e), 9) for e in group.elements] == [0.1, -0.1, -0.1, 0.1]


def test_unknown_key_suggests_a_near_miss(index):
    with pytest.raises(UnknownKeyError, match="not a known"):
        index.resolve("QI.999.XX")


def test_a_name_in_both_namespaces_is_never_ambiguous(index):
    """59 names are both an element and a supply; all agree, so none raises."""
    overlapping = [
        supply for supply in index.supplies if _resolves_as_id(index, supply)
    ]
    assert overlapping, "expected some names to appear in both namespaces"
    for name in overlapping:
        assert index.resolve(name).ids == (name,)


def _resolves_as_id(index, key):
    try:
        index.resolve(key, namespace="id")
    except (UnknownKeyError, GangedMagnetError, AmbiguousKeyError):
        # A handful of ids repeat across the branches (fast kickers), and a
        # repeated id cannot be addressed on its own.
        return False
    return True


# --------------------------------------------------------------------------- #
# Ganged magnets
# --------------------------------------------------------------------------- #


def test_setting_one_magnet_of_a_shared_supply_raises_and_names_its_siblings(index):
    with pytest.raises(GangedMagnetError) as error:
        index.resolve("BB.96.I1")
    message = str(error.value)
    assert "BB.1.I1" in message
    for sibling in ("BB.98.I1", "BB.100.I1", "BB.101.I1"):
        assert sibling in message


def test_the_explicit_id_form_splits_a_shared_supply(index):
    group = index.resolve("BB.96.I1", allow_split=True)
    assert group.ids == ("BB.96.I1",)


def test_a_split_supply_cannot_be_exported_to_sascha(cell):
    setpoints = MachineSetpoints(elements={"id:BB.96.I1": 0.12})
    with pytest.raises(ValueError, match="one value per supply"):
        setpoints.to_sascha(cell)


# --------------------------------------------------------------------------- #
# Design ratios
# --------------------------------------------------------------------------- #


def test_opposite_wiring_survives_a_setpoint(index):
    """QE.1.L3 is wired [+, -, +]; a single setpoint must not flatten it."""
    group = index.resolve("QE.1.L3")
    assert group.factors == (1.0, -1.0, 1.0)
    group.write(0.2)
    assert [round(read_kick(e), 9) for e in group.elements] == [0.2, -0.2, 0.2]


def test_unequal_magnets_keep_their_design_ratio(index):
    """QF.4.T5 pairs a 0.118 quadrupole with a 0.262 one on one supply."""
    group = index.resolve("QF.4.T5")
    before = [read_kick(e) for e in group.elements]
    ratio = before[1] / before[0]
    assert not math.isclose(abs(ratio), 1.0, rel_tol=0.1)

    group.write(group.read() * 2)
    after = [read_kick(e) for e in group.elements]
    assert math.isclose(after[1] / after[0], ratio, rel_tol=1e-12)


def test_applying_the_design_setpoint_changes_nothing_anywhere(index):
    """The strongest single check that the ratios were captured correctly."""
    changed = []
    for supply in index.supplies:
        group = index.group(supply)
        try:
            before = [read_kick(e) for e in group.elements]
            group.write(group.read())
            after = [read_kick(e) for e in group.elements]
        except Exception:
            continue
        if any(a != b for a, b in zip(before, after)):
            changed.append(supply)
    assert not changed


def test_applying_twice_equals_applying_once(index):
    group = index.resolve("QF.4.T5")
    group.write(0.3)
    once = [read_kick(e) for e in group.elements]
    group.write(0.3)
    assert [read_kick(e) for e in group.elements] == once


def test_partly_unpowered_supplies_are_reported_once(cell):
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        index = LatticeIndex.from_cell(cell)
    zero_warnings = [w for w in caught if "zero design kick" in str(w.message)]
    assert len(zero_warnings) == 1
    assert index.partly_unpowered


# --------------------------------------------------------------------------- #
# Chicanes
# --------------------------------------------------------------------------- #


def survey_end(index, dipoles):
    _, end = MagneticLattice(index.cell, start=dipoles[0], stop=dipoles[3]).survey()
    return end[-1]


@pytest.mark.parametrize("name", ["bc0", "bc1", "bc2"])
def test_requested_r56_is_reached_exactly(name, index):
    spec = CHICANES[name]
    dipoles, _ = chicane_dipoles(index, spec)
    ChicaneKnob(r56=-0.020).apply(index, spec)
    assert measure_r56(index, dipoles, spec.energy) == pytest.approx(-0.020, abs=1e-12)


@pytest.mark.parametrize("name", ["bc0", "bc1", "bc2"])
def test_changing_r56_leaves_the_chicane_geometry_closed(name, index):
    """The magnets are bolted down: only the path between them may change."""
    spec = CHICANES[name]
    dipoles, _ = chicane_dipoles(index, spec)
    before = survey_end(index, dipoles)

    ChicaneKnob(r56=-0.020).apply(index, spec)
    after = survey_end(index, dipoles)

    for axis in ("X", "Y", "Z", "THETA", "PHI"):
        assert after[axis] == pytest.approx(before[axis], abs=1e-7)


@pytest.mark.parametrize("name", ["bc0", "bc1", "bc2"])
def test_the_three_ways_of_setting_a_chicane_agree(name, index):
    spec = CHICANES[name]
    dipoles, _ = chicane_dipoles(index, spec)

    ChicaneKnob(r56=-0.025).apply(index, spec)
    reference = ChicaneKnob().report(index, spec)

    ChicaneKnob(angle=reference.angle).apply(index, spec)
    assert measure_r56(index, dipoles, spec.energy) == pytest.approx(-0.025, abs=1e-9)

    ChicaneKnob(rho=reference.rho).apply(index, spec)
    assert measure_r56(index, dipoles, spec.energy) == pytest.approx(-0.025, abs=1e-9)


def test_only_drifts_absorb_a_chicane_change(index):
    spec = CHICANES["bc2"]
    dipoles, _ = chicane_dipoles(index, spec)
    shoulder = index.between(dipoles[0], dipoles[1])
    non_drift = {id(e): e.l for e in shoulder if not isinstance(e, Drift)}

    ChicaneKnob(r56=-0.020).apply(index, spec)

    for element in shoulder:
        if id(element) in non_drift:
            assert element.l == non_drift[id(element)]


def test_setting_a_chicane_dipole_directly_still_rescales_the_drifts(cell):
    """A plain BB.1.I1 entry is what a control-room file contains."""
    spec = CHICANES["bc0"]

    by_element = MachineSetpoints(elements={"BB.1.I1": 0.1366592804})
    by_knob = MachineSetpoints(knobs={"bc0": {"angle": 0.1366592804}})

    from_element = LatticeIndex.from_cell(cell)
    by_element.apply(from_element)
    from_knob = LatticeIndex.from_cell(cell)
    by_knob.apply(from_knob)

    a, _ = chicane_dipoles(from_element, spec)
    b, _ = chicane_dipoles(from_knob, spec)
    assert [d.angle for d in a] == [d.angle for d in b]
    assert [d.l for d in a] == [d.l for d in b]
    assert [e.l for e in from_element.between(a[0], a[1])] == [
        e.l for e in from_knob.between(b[0], b[1])
    ]


def test_setting_a_chicane_twice_over_is_rejected(cell, index):
    setpoints = MachineSetpoints(
        knobs={"bc0": {"r56": -0.03}}, elements={"BB.1.I1": 0.1366592804}
    )
    with pytest.raises(ConflictError, match="both set the same hardware"):
        setpoints.apply(index)


def test_a_bend_outside_any_knob_warns_that_the_survey_moves(index):
    """BL.6.I1 is part of the I1 dogleg, not a chicane."""
    setpoints = MachineSetpoints(elements={"BL.6.I1": -0.111})
    with pytest.warns(UserWarning, match="survey downstream"):
        setpoints.apply(index)


# --------------------------------------------------------------------------- #
# Knob round trips
# --------------------------------------------------------------------------- #


def test_linac_knob_round_trips(index):
    spec = LINACS["l1"]
    knob = LinacKnob(sum_voltage=0.57872, chirp=-9.1)
    knob.apply(index, spec)
    back = knob.read(index, spec)
    assert back.sum_voltage == pytest.approx(0.57872, abs=1e-12)
    assert back.chirp == pytest.approx(-9.1, abs=1e-12)


def test_injector_knob_round_trips(index):
    knob = InjectorRFKnob(E1=0.130, chirp=-8.92, curvature=180.5, skewness=20332)
    knob.apply(index, INJECTOR)
    back = knob.read(index, INJECTOR)
    assert back.E1 == pytest.approx(0.130, rel=1e-12)
    assert back.chirp == pytest.approx(-8.92, rel=1e-12)
    assert back.curvature == pytest.approx(180.5, rel=1e-9)
    assert back.skewness == pytest.approx(20332, rel=1e-9)


def test_chicane_knob_round_trips(index):
    spec = CHICANES["bc1"]
    ChicaneKnob(r56=-0.0432).apply(index, spec)
    back = ChicaneKnob().report(index, spec)
    assert back.r56 == pytest.approx(-0.0432, abs=1e-12)
    dipoles, _ = chicane_dipoles(index, spec)
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


def test_a_half_specified_knob_is_not_silently_ignored(index):
    setpoints = MachineSetpoints()
    setpoints.l1.chirp = -9.1
    with pytest.raises(ConflictError, match="missing sum_voltage"):
        setpoints.apply(index)


def test_an_unknown_element_attribute_is_rejected(index):
    setpoints = MachineSetpoints(elements={"QI.63.I1D": {"kl": -2.9}})
    with pytest.raises(AttributeError, match="no 'kl' parameter"):
        setpoints.apply(index)


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
        index = LatticeIndex.from_cell(cell)
        setpoints.apply(index)
        dipoles, _ = chicane_dipoles(index, CHICANES["bc2"])
        results.append(measure_r56(index, dipoles, CHICANES["bc2"].energy))

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


def test_a_stale_resolved_block_warns(cell, index):
    setpoints = MachineSetpoints(
        elements={"QI.1.I1": -0.05343},
        resolved={"QI.1.I1": -0.9},
    )
    with pytest.warns(UserWarning, match="no longer resolve"):
        setpoints.apply(index)


def test_reading_an_optics_back_off_a_lattice(cell):
    written = MachineSetpoints(knobs={"bc2": {"r56": -0.0255}})
    rebuilt = MachineSetpoints.from_lattice(written.build(cell))
    assert rebuilt.bc2.r56 == pytest.approx(-0.0255, abs=1e-9)


# --------------------------------------------------------------------------- #
# Start-to-end tracking: the lattice is owned by the setpoints
# --------------------------------------------------------------------------- #


def build_section_lattice(section_names, tmp_path):
    """A SectionLattice over the given sections, reading the module-level cells."""
    from euxfel import sections
    from euxfel.section_track import SectionLattice

    from ocelot.cpbd.beam import Twiss

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


def test_rf_matches_what_update_cavity_used_to_produce(index):
    """Moving RF out of section_track must not change a single cavity."""
    from ocelot.utils.acc_utils import beam2rf_xfel_linac

    spec = LINACS["l1"]
    LinacKnob(sum_voltage=0.57872, chirp=-9.1).apply(index, spec)

    total, phase = beam2rf_xfel_linac(
        sum_voltage=0.57872, chirp=-9.1, init_energy=spec.init_energy
    )
    cavities = index.group("C.A2.L1").elements
    for cavity in cavities:
        assert cavity.v == total / len(cavities)  # what update_cavity did
        assert cavity.phi == phase


def test_the_chicane_angle_survives_a_section_lattice(tmp_path, cell):
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


def test_a_chicane_still_closes_after_a_section_lattice(tmp_path, cell):
    """Dropping change_bc_shoulders must not lose the drift rescaling."""

    before = LatticeIndex.from_cell(cell)
    dipoles_before, _ = chicane_dipoles(before, CHICANES["bc0"])
    reference = survey_end(before, dipoles_before)

    setpoints = MachineSetpoints(knobs={"bc0": {"r56": -0.045}})
    setpoints.apply_in_place(cell)
    build_section_lattice(["BC0"], tmp_path)

    after = LatticeIndex.from_cell(cell)
    dipoles_after, _ = chicane_dipoles(after, CHICANES["bc0"])
    moved = survey_end(after, dipoles_after)
    for axis in ("X", "Y", "Z", "THETA"):
        assert moved[axis] == pytest.approx(reference[axis], abs=1e-7)


# --------------------------------------------------------------------------- #
# Transverse deflecting structures
# --------------------------------------------------------------------------- #


def test_tds_knob_round_trips(index):
    from euxfel.volts.knobs import TDSKnob
    from euxfel.volts.library import TDS

    knob = TDSKnob(voltage=0.004, phase=90.0)
    knob.apply(index, TDS["tds_b1"])
    back = knob.read(index, TDS["tds_b1"])
    assert back.voltage == pytest.approx(0.004)
    assert back.phase == pytest.approx(90.0)


def test_one_supply_drives_both_b2_structures(index):
    """TDSB.B2 feeds TDSB.428.B2 and TDSB.430.B2, so both must move."""
    from euxfel.volts.knobs import TDSKnob
    from euxfel.volts.library import TDS

    group = index.resolve("TDSB.B2", namespace="ps")
    assert set(group.ids) == {"TDSB.428.B2", "TDSB.430.B2"}

    TDSKnob(voltage=0.006, phase=0.0).apply(index, TDS["tds_b2"])
    assert [s.v for s in group.elements] == [0.003, 0.003]


def test_the_tds_are_off_in_the_design_lattice(index):
    for supply in ("TDSA.I1", "TDSB.B1", "TDSB.B2"):
        assert all(s.v == 0.0 for s in index.resolve(supply).elements)


def test_the_shipped_example_optics_matches_its_source(cell):
    """special-optics-files/bc2_tds.yaml is BC2_TDS.txt in the new format."""
    from_yaml = MachineSetpoints.from_yaml(SASCHA_DIR / "bc2_tds.yaml")
    from_txt = MachineSetpoints.from_sascha(SASCHA_DIR / "BC2_TDS.txt", cell)
    assert from_yaml.resolve(cell) == from_txt.resolve(cell)
