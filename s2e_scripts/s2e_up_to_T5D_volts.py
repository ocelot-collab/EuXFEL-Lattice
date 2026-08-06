"""Cathode to T5D, driven by setpoints rather than hardcoded constants.

The same run as ``s2e_up_to_SA2.py``, continued through T3 and T5 to the T5D
dump, with the ~60 line RF preamble replaced by a handful of knob settings.

Run it from inside ``s2e_scripts/`` -- ``data_dir`` is relative::

    cd s2e_scripts && python s2e_up_to_T5D_volts.py

This is a full tracking run: long, and it writes intermediate .npz beams back
into ../beam_files/.  To check the setpoints *without* tracking, use
``euxfel setpoints apply <file> --target T5D`` instead.
"""

import time

import matplotlib.pyplot as plt
from ocelot.gui.accelerator import show_e_beam
from euxfel.section_track import SectionLattice

from euxfel.sections import (
    A1,
    AH1,
    BC0,
    BC1,
    BC2,
    CL1,
    CL2,
    CL3,
    DL,
    L1,
    L2,
    L3,
    LH,
    SASE2,
    T1,
    T3,
    T5,
)
from euxfel.volts import MachineSetpoints
from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.io import load_particle_array

data_dir = "../beam_files/"

# ------------------------------------------------------------------ #
# Physics processes.  These describe the tracking model, not the setpoints,
# so they stay here and the setpoints file never mentions them.
# ------------------------------------------------------------------ #
match_exec = True
smooth_exec = True
wake_exec = True
SC_exec = True
CSR_exec = True
coupler_kick_exec = False

all_sections = [
    A1,
    AH1,
    LH,
    DL,
    BC0,
    L1,
    BC1,
    L2,
    BC2,
    L3,
    CL1,
    CL2,
    CL3,
    T1,
    SASE2,
    T3,
    T5,
]

tws0 = Twiss()
tws0.E = 0.005
tws0.beta_x = 0.2865426867699372
tws0.beta_y = 0.2865426867699381
tws0.alpha_x = -0.8390696483216487
tws0.alpha_y = -0.8390696483216522

start = time.time()

# ------------------------------------------------------------------ #
# The setpoints.  Everything that used to be beam2rf calls and hand-copied
# constants now lives in one object, which can equally be loaded from a file
# with load_setpoints("setpoints/nominal_14gev.yaml") or imported from the
# control room with MachineSetpoints.from_sascha("BEAM_T5D.txt", cell).
# ------------------------------------------------------------------ #
p_array_init = load_particle_array(data_dir + "gun/rf_gun_new.npz", print_params=True)

setpoints = MachineSetpoints.design()
setpoints.name = "T5D 14 GeV"

# A1 + AH1 are solved together: the 3.9 GHz module linearises the 1.3 GHz one.
# The gun energy has to be the beam's, and has to be set before the setpoints
# are applied, since the injector RF is solved against it.
setpoints.i1.gun_energy = p_array_init.E
setpoints.i1.E1 = 0.130
setpoints.i1.chirp = -8.92
setpoints.i1.curvature = 180.5
setpoints.i1.skewness = 20332

setpoints.l1.sum_voltage, setpoints.l1.chirp = 0.57872, -9.1
setpoints.l2.sum_voltage, setpoints.l2.chirp = 1.7349, -9.3
# L3 on crest to the final energy: 14 GeV total, 2.4 GeV already delivered.
setpoints.l3.sum_voltage, setpoints.l3.chirp = 14.000 - 2.400, 0.0

# Compression.  R56 is solved against the real transfer matrix, and the drifts
# between the dipoles rescale with the angle so the chicane still closes.
# `angle` or `rho` work just as well -- setting one clears the others.
setpoints.bc0.r56 = -0.0555
setpoints.bc1.r56 = -0.0507
setpoints.bc2.r56 = -0.0305

# Individual magnets, by power supply or by element id:
#     setpoints["QI.1.I1"] = -0.05343
#     setpoints["QI.63.I1D"] = {"k1": -2.9974}      # explicit OCELOT attributes

# ------------------------------------------------------------------ #
# Apply the setpoints to the lattice.
#
# This mutates the module-level cells in place, which is process-global and
# irreversible.  It has to: SectionLattice takes a list of section *classes*,
# and each SectionTrack builds its own MagneticLattice from i1.cell / t5.cell
# inside __init__, so there is nowhere to hand a freshly built sequence.  Fine
# in a script that runs once and exits; everywhere else setpoints.build(cell)
# returns a private copy and leaves the design alone.
#
# It must happen *before* SectionLattice is constructed, because each section
# calculates its design twiss as it is built.
# ------------------------------------------------------------------ #
setpoints.apply_in_place(verbose=True)

section_lat = SectionLattice(sequence=all_sections, tws0=tws0, data_dir=data_dir)

# ------------------------------------------------------------------ #
# Physics processes only.  Magnets and RF are not here: the lattice is owned
# by the setpoints above, and passing "rho", "v" or "phi" now raises rather
# than quietly overwriting what was applied.
# ------------------------------------------------------------------ #
config = {
    A1: {"SC": SC_exec, "smooth": True, "wake": wake_exec},
    AH1: {"match": False, "SC": SC_exec, "wake": wake_exec},
    LH: {"SC": SC_exec, "CSR": False, "wake": wake_exec, "match": match_exec},
    DL: {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    BC0: {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    L1: {"match": match_exec, "SC": SC_exec, "wake": wake_exec, "smooth": smooth_exec},
    BC1: {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    L2: {"match": match_exec, "SC": SC_exec, "wake": wake_exec, "smooth": smooth_exec},
    BC2: {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    L3: {"match": match_exec, "SC": SC_exec, "wake": wake_exec},
    CL1: {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    CL2: {"match": match_exec},
    CL3: {"SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    T1: {"match": match_exec, "SC": False, "CSR": CSR_exec, "wake": wake_exec},
    SASE2: {"match": match_exec, "SC": False, "CSR": CSR_exec, "wake": wake_exec},
    T3: {"match": match_exec, "SC": False, "wake": wake_exec},
    T5: {"match": match_exec, "SC": False, "CSR": CSR_exec, "wake": wake_exec},
}

# What the setpoints actually resolved to, worth having in the log next to the run.
for name, knob in setpoints.knobs.set_items():
    print(f"{name:9s} {knob}")

show_e_beam(p_array_init)
plt.show()

p_array = section_lat.track_sections(
    sections=all_sections,
    p_array=p_array_init,
    config=config,
    force_ext_p_array=True,
    coupler_kick=coupler_kick_exec,
)

print(f"\nduration = {time.time() - start}")
show_e_beam(p_array)
plt.show()

# Save what was run, so the next person can reproduce it exactly:
#     setpoints.to_yaml("t5d_14gev.yaml")
#     setpoints.to_sascha(path="T5D_14GEV.txt")
