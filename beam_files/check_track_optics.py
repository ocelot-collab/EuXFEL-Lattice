#ocelot_dir = "/Users/tomins/Nextcloud/DESY/repository/ocelot"
import sys

import matplotlib.pyplot as plt

#sys.path.append(ocelot_dir)
sys.path.insert(1, "../")

from s2e_sections.sections import *
from ocelot.utils.section_track import *
from ocelot.gui.accelerator import *
import time
from ocelot.common.globals import *
from ocelot import *
c = 299792458


data_dir = "../beam_files/"

####################  Physics Effects control globaly ##################
match_exec = True # artificially (kick) match beam to design optics
smooth_exec = True # filtering
wake_exec = True
SC_exec = True
CSR_exec = True
coupler_kick_exec = False  # coupler effect in RF modules, quadrupole and dipole (usually off) component, which now is not in the lattice files


# all sections which can be potentially used in s2e
all_sections = [A1, AH1, LH, DL, BC0, L1, BC1, L2, BC2, L3, CL1, CL2, CL3, TL]  #, SASE1, T4, SASE3, T4D]

######################### Initial Twiss paramters for design optics ##################
tws0 = Twiss()
tws0.E = 0.005
tws0.beta_x  =  0.2865426867699372
tws0.beta_y  =  0.2865426867699381
tws0.alpha_x = -0.8390696483216487
tws0.alpha_y = -0.8390696483216522
start = time.time()

#################################### Compression Working Point ################################
E40 = 14 
r1 = 4.1218                 # deflecting radius in BC0
r2 = 8.3934                 # deflecting radius in BC1
r3 = 14.4111                # deflecting radius in BC2
# RF settings
v11 = 0.148  # GV
phi11 = -12.07
v13 = 0.031384   # GV
phi13 = 131.85
v21 = 0.659  # GV
phi21 = 30.13
v31 = 1.7052  # GV
phi31 = -3.078
v41 = E40-2.4
phi41 = 0

# BC magnet radius
#r1 = 0.5 / 0.1366592804  # 3.6587343247857467
#r2 = 0.5 / 0.0532325422  # 9.392750737348779
#r3 = 0.5 / 0.0411897704  # 12.138936321917445
#################################### Compression WP ################################

# init sections which can be used for tracking
section_lat = SectionLattice(sequence=all_sections, tws0=tws0, data_dir=data_dir)
# plot twiss parameters
lat = MagneticLattice(section_lat.elem_seq)
#plot_opt_func(lat, section_lat.tws)
#plt.show()


sections = [A1, AH1, LH, DL, BC0, L1, BC1, L2, BC2]
s, bx, by = section_lat.load_twiss_track(sections)
plt.plot(s, bx, label = "beta_x")
plt.plot(s, by, label = "beta_y")
plt.legend()
plt.show()
