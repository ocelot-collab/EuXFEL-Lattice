"""A tour of the setpoints API, in one runnable script.

    python examples/setpoints_tour.py

Everything here runs against a private copy of the lattice, so nothing you do
leaves the process and you can rerun it as often as you like.  Each section is
numbered and independent -- comment out the ones you are not interested in, or
paste them into a REPL and poke at them.

The two objects to keep straight:

    Beamline          what *is*.  A sequence of elements, bound to one lattice,
                      addressable by element or power supply name.
    MachineSetpoints  what you *ask for*.  Knob settings and magnet strengths,
                      with no lattice in sight -- loadable, mergeable, diffable,
                      and only then applied to a Beamline.
"""

import warnings

from ocelot.cpbd.magnetic_lattice import MagneticLattice
from ocelot.cpbd.track import twiss

from euxfel import (
    Beamline,
    GangedMagnetError,
    KnobOwnedError,
    all_machine_elements,
    sequences,
    set_design_optics,
)
from euxfel.volts import ChicaneKnob, MachineSetpoints, read_sascha
from euxfel.volts.knobs import RFModuleKnob, chicane_dipoles
from euxfel.machine import CHICANES

SASCHA = "special-optics-files/BC2_TDS.txt"


def heading(number: int | str, title: str) -> None:
    print(f"\n\033[1m{number}. {title}\033[0m\n" + "-" * 72)


def main() -> None:
    # Roughly 500 supplies have a magnet at zero by design; the warning is true
    # but it is not what this script is about.
    warnings.filterwarnings("ignore", message=".*zero design kick.*")

    cell = all_machine_elements()

    # ---------------------------------------------------------------- 1
    heading(1, "A Beamline is an ordinary sequence")

    beamline = Beamline.from_cell(cell)  # deep-copies, so `cell` is untouched
    print(f"{beamline!r}")
    print(f"len(beamline)          {len(beamline)}")
    print(f"beamline[0].id         {beamline[0].id}")
    print(f"beamline[:3]           {[e.id for e in beamline[:3]]}")
    print(f"sum(e.l for e in ...)  {sum(e.l for e in beamline):.1f} m of machine")

    # Which means it goes straight into OCELOT, with no `.cell` at the call site.
    lattice = MagneticLattice(beamline)
    print(f"MagneticLattice(beamline) -> {len(lattice.sequence)} elements")

    # ---------------------------------------------------------------- 2
    heading(2, "Names resolve, in both namespaces")

    # A power supply name and an element id are searched together.  You do not
    # have to say which you meant unless the two would disagree, and over this
    # lattice they never do.
    print(f'beamline["QI.1.I1"]    {beamline["QI.1.I1"].ids}   (a power supply)')
    print(f'beamline["QI.46.I1"]   {beamline["QI.46.I1"].ids}   (the element it feeds)')
    print(f'beamline["BB.1.I1"]    {beamline["BB.1.I1"].ids}')
    print(f'"QI.46.I1" in beamline {"QI.46.I1" in beamline}')

    # A near miss tells you what you probably meant.
    try:
        beamline["QI.46.I2"]
    except KeyError as error:
        print(f"\ntypo -> {error}")

    # ---------------------------------------------------------------- 3
    heading(3, "Reading a group, and writing one")

    group = beamline["QE.1.L3"]
    print(f"{group.key} feeds {len(group)}: {', '.join(group.ids)}")
    print(f"design ratios          {group.factors}   <- note the sign")
    print(f"read()                 {group.read():+.6f}")

    # Writing preserves the wiring.  QE.1.L3 is [+, -, +] by design, and it
    # stays that way however far you move it -- including through zero, which
    # is where a naive "remember the sign" would lose it.
    group.write(0.5)
    print(f"after write(0.5)       {[round(e.k1 * e.l, 6) for e in group.elements]}")
    group.write(0.0)
    group.write(-0.25)
    print(f"through zero, then     {[round(e.k1 * e.l, 6) for e in group.elements]}")

    # ---------------------------------------------------------------- 4
    heading(4, "Reading is free; writing is guarded")

    # Every name in the machine resolves.  Looking a magnet up is harmless.
    dipole = beamline["BB.96.I1"]
    print(f"BB.96.I1  read()       {dipole.read():+.6f}")
    print(f"          split_from   {dipole.split_from}   (it shares a supply)")
    print(f"          owned_by     {dipole.owned_by}        (it is a chicane dipole)")

    # But writing it is refused, because the kick is only half of what the
    # setting means: a chicane's drifts have to move with its angle.
    try:
        beamline["BB.1.I1"].write(0.1366)
    except KnobOwnedError as error:
        print(f"\n{error}")

    # And a magnet that merely shares a supply is refused for the other reason.
    try:
        beamline["QI.73.I1"].write(0.1)
    except GangedMagnetError as error:
        print(f"\n{error}")

    # A cavity has no geometry to break, so nothing stands in the way.
    beamline["C.A2.L1"].write(0.1)
    print("\nC.A2.L1.write(0.1) -> fine, a voltage moves no drifts")

    # ---------------------------------------------------------------- 4b
    heading("4b", "...and the matched section is held, not guarded")

    # The injector up to MATCH.52.I1 is a stretch this model decides for
    # itself: the A1/AH1 voltages come from beam2rf, and five quadrupoles are
    # re-matched at conversion time.  A control-room file answers the same
    # questions about the real gun's beam, and answers differently.
    print(f"matched supplies: {len(beamline.matched_supplies)} upstream of MATCH.52.I1")
    print(f"  {', '.join(beamline.matched_supplies)}")
    print(f'beamline["QI.1.I1"].matched_by  {beamline["QI.1.I1"].matched_by!r}')
    print(f'beamline["QI.4.I1"].matched_by  {beamline["QI.4.I1"].matched_by!r}')

    # Nothing stops you writing one: naming a magnet is choosing it.  The hold
    # is about setpoints swept in wholesale -- see section 11.
    beamline["QI.1.I1"].write(0.06)
    print("\nQI.1.I1.write(0.06) -> fine, that write is correct; just not a default")

    # ---------------------------------------------------------------- 5
    heading(5, "Why the chicane guard exists")

    fresh = Beamline.from_cell(cell)
    dipoles, _ = chicane_dipoles(fresh, CHICANES["bc0"])

    def survey_exit(bl):
        _, ends = MagneticLattice(bl, start=dipoles[0], stop=dipoles[3]).survey()
        return ends[-1]

    def shoulder(bl):
        return sum(e.l for e in bl.between(dipoles[0], dipoles[1]))

    before, gap0 = survey_exit(fresh), shoulder(fresh)

    # The knob way: the drifts between the dipoles lengthen as 1/cos(angle),
    # so the projected gap is held and the chicane still closes.
    ChicaneKnob(angle=0.1366592804).apply(fresh, CHICANES["bc0"])
    after = survey_exit(fresh)
    print(f"via the knob:   shoulder {gap0:.6f} -> {shoulder(fresh):.6f} m")
    print(f"                exit moves dZ = {after['Z'] - before['Z']:+.1e} m")

    # The blunt way, for comparison.  This is what the guard refuses.
    blunt = Beamline.from_cell(cell)
    dipoles, _ = chicane_dipoles(blunt, CHICANES["bc0"])
    before, gap0 = survey_exit(blunt), shoulder(blunt)
    blunt["BB.1.I1"].write(0.1366592804, ignore_knob=True)
    after = survey_exit(blunt)
    print(f"ignore_knob:    shoulder {gap0:.6f} -> {shoulder(blunt):.6f} m")
    print(
        f"                exit moves dZ = {after['Z'] - before['Z']:+.1e} m  <- 5.9 mm"
    )

    # ---------------------------------------------------------------- 6
    heading(6, "Knobs: three views of one chicane")

    setpoints = MachineSetpoints(name="a tour")

    # r56, angle and rho are the same geometry said three ways.  Setting one
    # clears the other two, so the last thing you set is what is meant.
    setpoints.bc0.r56 = -0.055
    print(f"bc0.r56 = -0.055  ->  angle={setpoints.bc0.angle} rho={setpoints.bc0.rho}")
    setpoints.bc0.angle = 0.14
    print(f"bc0.angle = 0.14  ->  r56={setpoints.bc0.r56} rho={setpoints.bc0.rho}")
    setpoints.bc0.r56 = -0.055

    # `report` gives all three at once, off a real lattice.
    reading = ChicaneKnob(r56=-0.055).report(Beamline.from_cell(cell), CHICANES["bc0"])
    print(
        f"\nr56 = -0.055 means: angle {reading.angle:.6f} rad, rho {reading.rho:.3f} m"
    )

    # ---------------------------------------------------------------- 7
    heading(7, "The compact setter")

    # Anything with more than one parameter takes them together.  It returns
    # the knob, so it composes.
    setpoints.b2_tds.set(voltage=0.005, phase=90.0)
    setpoints.l1.set(sum_voltage=0.15, chirp=-2.0)
    setpoints.i1.set(E1=0.13, chirp=-1.5, curvature=-50.0, skewness=0.0)
    print(f"b2_tds  {setpoints.b2_tds}")
    print(f"l1      {setpoints.l1}")
    print(f"i1      {setpoints.i1}")

    # A misspelling is caught, listing what does exist.
    try:
        setpoints.l1.set(chrip=-2.0)
    except ValueError as error:
        print(f"\ntypo -> {error}")

    # And so is asking for two views of the same geometry at once.
    try:
        setpoints.bc1.set(r56=-0.04, angle=0.1)
    except ValueError as error:
        print(f"clash -> {error}")

    # ---------------------------------------------------------------- 8
    heading(8, "Per-module RF, when one module must differ from its linac")

    # L3 is 20 modules on one knob.  To detune a single one, set the module and
    # leave its linac alone -- setting both would be two claims on the same
    # cavities, and `apply` raises rather than picking one.
    detuned = MachineSetpoints(name="A7 off")
    detuned.modules["A7"] = RFModuleKnob(voltage=0.0, phase=0.0)
    print(f'modules["A7"] = {detuned.modules["A7"]}')

    detuned.l3.set(sum_voltage=10.0, chirp=0.0)
    try:
        detuned.build(cell)
    except Exception as error:
        print(f"\nwith l3 set as well -> {type(error).__name__}: {error}")

    # ---------------------------------------------------------------- 9
    heading(9, "Individual magnets alongside the knobs")

    setpoints["QI.1.I1"] = -0.0534  # a generalised kick, k1 * l
    setpoints["QI.63.I1D"] = {"k1": -2.9974}  # or OCELOT attributes verbatim
    setpoints["id:QI.73.I1"] = -0.20  # deliberately split a shared supply
    print(f"elements: {setpoints.elements}")

    # A magnet and a knob cannot both claim the same thing.  bc0 is set above,
    # so naming one of its dipoles here is caught before anything is written --
    # this is the file-level counterpart of the guard in section 4.
    clashing = setpoints.model_copy(deep=True)
    clashing["id:BB.96.I1"] = -0.13
    try:
        clashing.build(cell)
    except Exception as error:
        print(f"\nwith bc0 also set -> {type(error).__name__}: {error}")

    # --------------------------------------------------------------- 10
    heading(10, "Applying: build (a copy) vs apply_in_place (the globals)")

    applied = setpoints.build(cell)  # `cell` is untouched
    print(f"build(cell) -> {applied!r}")
    print(f"bc0 landed at r56  {ChicaneKnob().read(applied, CHICANES['bc0']).r56:+.6f}")
    print(f"QI.1.I1 landed at  {applied['QI.1.I1'].read():+.6f}")

    # The result is still a Beamline, so it is both trackable and addressable.
    print(f"and still a sequence: {len(applied)} elements")

    # `apply_in_place` mutates the shared module-level cells instead.  That is
    # what the s2e scripts need, because SectionTrack builds its own lattice
    # from the globals -- but it is process-wide, so it is not used here.

    # --------------------------------------------------------------- 11
    heading(11, "Round trips: YAML and the control-room format")

    text = setpoints.to_yaml()
    print(text.rstrip())

    # Sascha is DESY's `NAME VALUE` format: one line per power supply, and
    # every bend sign flipped relative to OCELOT's convention.
    from_control_room = MachineSetpoints.from_sascha(SASCHA, cell)
    print(
        f"\nBC2_TDS.txt -> {len(from_control_room.elements)} supplies applied, "
        f"{len(from_control_room.matching)} held"
    )
    print(f"  held: {', '.join(from_control_room.matching)}")

    # Nobody chose those eight among the file's hundred-odd supplies -- an
    # importer swept up the machine -- so they go to `matching` and stay there.
    # Everything else records what the file said, verbatim: the chicanes are
    # still plain `elements` entries and the routing happens when it is
    # *applied*, so the object stays a faithful copy of the file and only the
    # lattice sees the drifts move.  `verbose=True` shows what got routed:
    print()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        from_control_room.build(cell, verbose=True)
    for warning in caught:
        if "matched section" in str(warning.message):
            print(f"\n{warning.message}")

    # Ask for them and you get them -- along with the laser-heater warning the
    # hold was suppressing: the file runs BL.3.I1 about 1.75% weak against the
    # other two, which is not a symmetric chicane, so its four dipoles are
    # written individually rather than through the `lh` knob.
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        from_control_room.build(cell, matching=True)
    for warning in caught:
        if "symmetric chicane" in str(warning.message):
            print(f"\n{warning.message}")

    # It survives the whole way back out, byte for byte -- held values included,
    # because holding is about what reaches a lattice, not what a file contains.
    exported = from_control_room.to_sascha(cell, keys=list(read_sascha(SASCHA)))
    print(f"\nre-exported identical to the original: {exported == open(SASCHA).read()}")

    # -------------------------------------------------------------- 11b
    heading("11b", "Writing only part of a machine")

    # Every line in a Sascha file moves a supply when the control room applies
    # it, so writing all 476 to change 45 clobbers 431 settings nobody asked to
    # touch.  `changed` is measured against the design optics -- which is what
    # `subsequences/*.py` says, stamped onto each element at import.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        everything = from_control_room.to_sascha(cell)
        moved = from_control_room.to_sascha(cell, changed=True)
    print(f"everything    {len(everything.splitlines()):3} lines")
    print(f"changed=True  {len(moved.splitlines()):3} lines")

    # The whole file differs from design in 108 supplies, but 63 of those differ
    # by less than the format's six decimal places -- lines that would set what
    # is already set.  A Beamline answers the wider question:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        applied_file = from_control_room.build(cell, matching=True)
    print(f"differ at all {len(applied_file.select(changed=True)):3} supplies")

    # Ranges name supplies, not magnets, and there are two honest readings of a
    # partial overlap.  QA.1.SA1 feeds 19 quadrupoles across all of SASE1.
    t4d = Beamline.from_cell(sequences.cathode_to_t4d)
    span = ("MATCH.2248.SA1", "QA.2296.SA1")
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        touching = t4d.select(between=span)
        enclosed = t4d.select(within=span)
    print(f"\nbetween {span[0]} .. {span[1]}: {touching}")
    print(f"within  {span[0]} .. {span[1]}: {enclosed}")
    for warning in caught:
        print(f"  -> {warning.message}")

    # And the baseline itself can be moved.  Rebased onto the file it came from,
    # nothing has changed -- which is the sharpest check that it works.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        previous = set_design_optics(SASCHA, cell)
        print(
            f"\nrebased onto {SASCHA}: {len(applied_file.select(changed=True))} changed"
        )
        set_design_optics(previous)

    # The wiring is untouched by that: it is how the magnets are cabled, not
    # something an optics can say.
    print(f"QE.1.L3 factors, still: {beamline['QE.1.L3'].factors}")

    # --------------------------------------------------------------- 12
    heading(12, "Merging, and reading setpoints back off a lattice")

    base = MachineSetpoints(name="base", knobs={"bc0": {"r56": -0.05}})
    tweak = MachineSetpoints(name="tweak", knobs={"bc1": {"r56": -0.04}})
    merged = base.merged_with(tweak)
    print(f"merged: bc0={merged.bc0.r56} bc1={merged.bc1.r56} name={merged.name!r}")

    # And the reverse direction: what is this lattice currently set to?
    read_back = MachineSetpoints.from_lattice(applied, name="as built")
    print(f"from_lattice: {len(read_back.elements)} supplies, bc0 {read_back.bc0}")

    # --------------------------------------------------------------- 13
    heading(13, "It still tracks")

    # The whole point: optics through a beamline you configured.  B1D rather
    # than I1D because the I1 dump line branches off before BC0, so a bc0 knob
    # applied to `cathode_to_i1d` raises -- correctly, since the magnets it
    # names are genuinely not in that sequence.
    for r56 in (-0.045, -0.055):
        b1d = MachineSetpoints(knobs={"bc0": {"r56": r56}}).build(
            sequences.cathode_to_b1d
        )
        end = twiss(MagneticLattice(b1d), tws0=sequences.CATHODE_TWISS0)[-1]
        print(
            f"bc0 r56 = {r56}  ->  cathode -> B1D, s = {end.s:.2f} m, "
            f"beta_x = {end.beta_x:.3f} m, beta_y = {end.beta_y:.3f} m"
        )

    print("\nEverything above ran on private copies. Nothing was left changed.\n")


if __name__ == "__main__":
    main()
