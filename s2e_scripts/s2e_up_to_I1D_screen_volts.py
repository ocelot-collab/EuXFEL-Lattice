"""Cathode to the I1 dump screen, driven by a setpoints file.

The same run as ``s2e_up_to_I1D_screen.py``, with the RF preamble and the r1/r2/r3
constants replaced by ``setpoints/i1d_screen.yaml``.  Every value is the
one that script carried; see the file for the mapping.

Run it from inside ``s2e_scripts/`` -- ``data_dir`` is relative::

    cd s2e_scripts && python s2e_up_to_I1D_screen_volts.py

This is a full tracking run: long, and it writes intermediate .npz beams back
into ../beam_files/.  To check the setpoints *without* tracking, use
``euxfel setpoints apply setpoints/i1d_screen.yaml`` instead.

.. warning::

   This does not run yet.  ``DX12_I1D.txt`` contains ``QI.62.I1``, which is not
   an element in the current lattice -- the quadrupoles there run QI.55, 57, 59,
   60, 61 before the line branches, so that name looks like older numbering.
   The original script matched on ``element.id`` and so skipped it silently,
   meaning the setpoint has never actually been applied.  It is kept so that
   loading fails loudly instead; resolve the name or drop the line from the file.
"""

import time

import matplotlib.pyplot as plt
from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.io import load_particle_array
from ocelot.gui.accelerator import show_e_beam

from euxfel.section_track import SectionLattice
from euxfel.sections import A1, AH1, I1D, LH
from euxfel.volts import full_machine_cell, load_setpoints, MachineSetpoints

data_dir = "../beam_files/"

# Physics processes.  These describe the tracking model, not the machine, so
# they stay here and the setpoints file never mentions them.
match_exec = True
smooth_exec = True
wake_exec = True
SC_exec = True
CSR_exec = True
coupler_kick_exec = False

sections = [A1, AH1, LH, I1D]

tws0 = Twiss()
tws0.E = 0.005
tws0.beta_x = 0.2865426867699372
tws0.beta_y = 0.2865426867699381
tws0.alpha_x = -0.8390696483216487
tws0.alpha_y = -0.8390696483216522

start = time.time()

p_array_init = load_particle_array(data_dir + "gun/rf_gun_new.npz", print_params=True)

setpoints = load_setpoints("setpoints/i1d_screen.yaml")

# The DX12 quadrupole settings that go with this optics.  Was
# SPECIAL_DX12_OPTICS_I1D, a dict applied by a hand-written loop.
setpoints = setpoints.merged_with(
    MachineSetpoints.from_sascha(
        "../special-optics-files/DX12_I1D.txt", full_machine_cell()
    )
)

# Apply before SectionLattice is built: each section calculates its design twiss
# as it is constructed, and apply_matching later transforms the beam onto that.
# This mutates the module-level cells, which is process-global and irreversible
# -- fine for a script that runs once and exits, but it is why setpoints.build()
# exists for everything else.
setpoints.apply_in_place(full_machine_cell(), verbose=True)

section_lat = SectionLattice(sequence=sections, tws0=tws0, data_dir=data_dir)

# Physics processes only.  Magnets and RF are owned by the setpoints above, and
# passing "rho", "v" or "phi" here now raises rather than silently overwriting
# what was applied.
config = {
    A1: {"SC": SC_exec, "smooth": True, "wake": wake_exec},
    AH1: {"match": False, "SC": SC_exec, "wake": wake_exec},
    LH: {"SC": SC_exec, "CSR": False, "wake": wake_exec, "match": match_exec},
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
