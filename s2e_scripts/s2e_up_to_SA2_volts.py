"""Cathode to SASE2, driven by a setpoints file.

The same run as ``s2e_up_to_SA2.py``, with the RF preamble and the r1/r2/r3
constants replaced by ``setpoints/nominal_14gev.yaml``.  Every value is the
one that script carried; see the file for the mapping.

Run it from inside ``s2e_scripts/`` -- ``data_dir`` is relative::

    cd s2e_scripts && python s2e_up_to_SA2_volts.py

This is a full tracking run: long, and it writes intermediate .npz beams back
into ../beam_files/.  To check the setpoints *without* tracking, use
``euxfel setpoints apply setpoints/nominal_14gev.yaml`` instead.
"""

import time

import matplotlib.pyplot as plt
from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.io import load_particle_array
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
)
from euxfel.volts import load_setpoints

data_dir = "../beam_files/"

# Physics processes.  These describe the tracking model, not the machine, so
# they stay here and the setpoints file never mentions them.
match_exec = True
smooth_exec = True
wake_exec = True
SC_exec = True
CSR_exec = True
coupler_kick_exec = False

sections = [A1, AH1, LH, DL, BC0, L1, BC1, L2, BC2, L3, CL1, CL2, CL3, T1, SASE2]

tws0 = Twiss()
tws0.E = 0.005
tws0.beta_x = 0.2865426867699372
tws0.beta_y = 0.2865426867699381
tws0.alpha_x = -0.8390696483216487
tws0.alpha_y = -0.8390696483216522

start = time.time()

p_array_init = load_particle_array(data_dir + "gun/rf_gun_new.npz", print_params=True)

setpoints = load_setpoints("setpoints/nominal_14gev.yaml")
# The gun energy the injector RF is solved against is the beam's own.
setpoints.i1.gun_energy = p_array_init.E

# Apply before SectionLattice is built: each section calculates its design twiss
# as it is constructed, and apply_matching later transforms the beam onto that.
# This mutates the module-level cells, which is process-global and irreversible
# -- fine for a script that runs once and exits, but it is why setpoints.build()
# exists for everything else.
setpoints.apply_in_place(verbose=True)

section_lat = SectionLattice(sequence=sections, tws0=tws0, data_dir=data_dir)

# Physics processes only.  Magnets and RF are owned by the setpoints above, and
# passing "rho", "v" or "phi" here now raises rather than silently overwriting
# what was applied.
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
}

for name, knob in setpoints.knobs.set_items():
    print(f"{name:9s} {knob}")

show_e_beam(p_array_init)
plt.show()

p_array = section_lat.track_sections(
    sections=sections,
    p_array=p_array_init,
    config=config,
    force_ext_p_array=True,
    coupler_kick=coupler_kick_exec,
)

print(f"\nduration = {time.time() - start}")
show_e_beam(p_array)
plt.show()
