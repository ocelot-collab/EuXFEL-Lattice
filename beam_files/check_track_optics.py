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

# RF settings
v11 = 0.148  # GV
phi1 = -12.07
v13 = 0.031384   # GV
phi13 = 131.85
v21 = 0.659  # GV
phi21 = 30.13
v31 = 1.7052  # GV
phi31 = -3.078

c = 299792458
grad = pi/180
f = 1.3e9
k = 2*pi*f/c
# RF parameters from 2019 reference simulations
RFpars=np.array([[150.6490695436200156,  -12.45143229398958340],
                 [34.71451849662050648, 133.0130880849731909],
                 [612.3662881523496253, 21.42357967251925999],
                 [2387.170005428192326, 44.53398073107610600]])

E40 = 14000                 # final beam energy
r1 = 4.1218                 # deflecting radius in BC0
r2 = 8.3934                 # deflecting radius in BC1
r3 = 14.4111                # deflecting radius in BC2
C10= 3                      # local compression in BC0
C20= 7                      # local compression in BC1
C30= 400/(C10*C20)          # local compression in BC2
R2 = 0                      # first derivative of the inverse compression function
R3 = 900                    # second derivative of the inverse compression function

v11 =   RFpars[0,0]
phi11 = RFpars[0,1] * grad
v13 =   RFpars[1, 0]
phi13 = RFpars[1, 1] * grad
v21 =   RFpars[2, 0]
phi21 = RFpars[2, 1] * grad
v31 =   RFpars[3,0]
phi31 = RFpars[3,1] * grad
v41 = E40-2400
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
