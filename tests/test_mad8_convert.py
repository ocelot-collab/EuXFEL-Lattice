"""Check the MAD-8 tapes can actually be turned into subsequence modules.

`tests/test_mad8_names.py` shows the names come out right and the geometry
closes.  This is the next question: do the declared section boundaries exist in
a tape-built sequence, do the modules write, and does the optics chain across
them the way `tests/test_subsequences.py` requires of the component-list route?
"""

import pytest
from ocelot.cpbd.magnetic_lattice import MagneticLattice
from ocelot.cpbd.track import twiss as ocelot_twiss

from euxfel.mad8 import load_config
from euxfel.mad8_convert import build_subsequences, mad8_to_ocelot

#: Twiss parameters that must chain across a module boundary.
#:
#: `Dy` is in this list, which it could not have been before 2026-07-31: the T5D
#: TWISS tape used to report DY ~ 0 through TL34_SA2 and T1 although its own
#: elements bend 1.08 mrad vertically there -- five KL extraction kickers at
#: -1.019e-4 rad each plus QF.2012.TL at -5.715e-4 -- leaving us disagreeing with
#: it by 2.7e-2.  The cause was `couple` on the T5D twiss call
#: (`Run_South_2025.txm:260`), which scaled that path's dispersion by E/E_ref and
#: left it a factor 26 low against every other path in the shared injector.  With
#: the flag removed and MAD-8 re-run, T5D's DX matches T4D's to 1e-17 over the
#: 6526 elements they share, and this boundary closes at 4.8e-7.
CHAINED = ("beta_x", "beta_y", "alpha_x", "alpha_y", "Dx", "Dxp", "Dy", "Dyp", "E")

#: Design optics agree with MAD-8's own to about 1e-4 relative across a
#: boundary.  The residue is the difference between Ocelot's transfer maps and
#: MAD-8's, not a lattice disagreement -- the geometry closes to 3e-6 m.
CHAIN_TOLERANCE = 2e-3


@pytest.fixture(scope="module")
def subsequences():
    return build_subsequences()


def test_every_declared_section_exists(subsequences):
    """Both boundary markers of every section are findable by generated name."""
    declared = set(load_config()["sections"])
    assert set(subsequences) == declared
    for name, (_, elements) in subsequences.items():
        assert elements, f"{name} sliced to nothing"


@pytest.mark.parametrize("target", sorted(load_config()["targets"]))
def test_optics_chain_across_module_boundaries(subsequences, target):
    """Tracking a module from its twiss0 lands on the next module's twiss0.

    The same property `tests/test_subsequences.py` asserts of the component-list
    route, and the one that catches a mis-sliced boundary: a section that starts
    one element early still writes and still imports, but its optics no longer
    join.
    """
    chain = load_config()["targets"][target]
    for upstream, downstream in zip(chain, chain[1:]):
        twiss0, elements = subsequences[upstream.upper()]
        arrived = ocelot_twiss(MagneticLattice(elements), tws0=twiss0)[-1]
        expected = subsequences[downstream.upper()][0]

        for field in CHAINED:
            got, want = getattr(arrived, field), getattr(expected, field)
            error = abs(got - want) / max(abs(want), 1.0)
            assert error < CHAIN_TOLERANCE, (
                f"{target}: {upstream} -> {downstream}: {field} "
                f"tracked to {got:.6f}, next module starts at {want:.6f}"
            )


def test_modules_write_and_import(tmp_path):
    """The written modules are importable Python with a cell and a twiss0."""
    import importlib.util

    mad8_to_ocelot(tmp_path)
    for name in ("g1d", "i1", "sase1"):
        path = tmp_path / f"{name}.py"
        assert path.exists(), f"{name}.py was not written"
        spec = importlib.util.spec_from_file_location(f"_mad8_{name}", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        assert module.cell, f"{name} has an empty cell"
        assert module.twiss0.beta_x > 0


def test_modules_contain_only_tape_elements(subsequences):
    """No element in any written module is absent from the tape.

    Compared by name, which is deterministic across builds -- `build_sequence`
    constructs fresh objects each call, so identity cannot be used here.  Every
    element either carries a generated NAME1 or, where the component list has no
    row for it, its MAD-8 name; an injected `ocelot_start` or a split `D0100A`
    would match neither.

    The guard is against drift rather than a specific bug.  Marker insertion,
    drift splitting and a setpoint layer were all at various points planned into
    this converter, and every one of them would have been invisible to the survey
    and optics tests -- injected markers are physically inert, which is precisely
    what makes them easy to add without noticing.  Names are what notice.
    """
    from euxfel.mad8_import import build_sequence

    declared = load_config()["sections"]
    universe: dict[str, set[str]] = {}

    for name, (_, elements) in subsequences.items():
        target = declared[name]["target"]
        if target not in universe:
            universe[target] = {e.id for e in build_sequence(target)}
        foreign = sorted({e.id for e in elements} - universe[target])
        assert not foreign, (
            f"{name}: {len(foreign)} element name(s) the {target} tape does not "
            f"produce, e.g. {foreign[:3]} -- the conversion should be literal"
        )


def test_module_lengths_sum_to_the_tape(subsequences):
    """Each target's modules tile its tape without inventing or losing length.

    A module chain covers its path exactly once, so the arc lengths add up to the
    tape's total.  Catches a split or a dropped element that happened to keep the
    element *names* valid.
    """
    from euxfel.mad8_import import read_tape

    chains = load_config()["targets"]

    for target, chain in chains.items():
        modules = [subsequences[n.upper()] for n in chain if n.upper() in subsequences]
        if len(modules) != len(chain):
            continue
        total = sum(
            sum(getattr(e, "l", 0.0) or 0.0 for e in elements)
            for _, elements in modules
        )
        # The chain's own dump target, not its first section's source: a chain
        # draws its modules from several tapes (I1 from I1D, L1 from B1D, ...)
        # but tiles exactly one path.
        tape_total = (
            read_tape(target.upper()).select("L").to_series().fill_null(0.0).sum()
        )
        assert abs(total - tape_total) < 1e-6, (
            f"{target}: modules total {total:.6f} m against the tape's "
            f"{tape_total:.6f} m"
        )
