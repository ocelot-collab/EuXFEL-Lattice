import matplotlib.pyplot as plt

from euxfel.sections import *
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
    TL,
    SASE1,
    T4,
    SASE3,
    T4D,
]
######################### Initial Twiss paramters for design optics ##################
tws0 = Twiss()
tws0.E = 0.005
tws0.beta_x  =  0.2865426867699372
tws0.beta_y  =  0.2865426867699381
tws0.alpha_x = -0.8390696483216487
tws0.alpha_y = -0.8390696483216522
start = time.time()

####################################################################################
E40 = 14000                 # final beam energy
C10= 3                      # local compression in BC0
C20= 7                      # local compression in BC1
C30= 400/(C10*C20)          # local compression in BC2
R2 = 0                      # first derivative of the inverse compression function
R3 = 900                    # second derivative of the inverse compression function

v41 = E40-2400
phi41 = 0

# BC magnet radius read from BKR
r1 = 0.5 / 0.1366592804  # 3.6587343247857467
r2 = 0.5 / 0.0532325422  # 9.392750737348779
r3 = 0.5 / 0.0411897704  # 12.138936321917445
###################################################################################

# sequence of sections for tracking.
sections = [A1, AH1, LH, DL, BC0, L1, BC1, L2, BC2, L3, CL1, CL2, CL3, TL, SASE1, T4, SASE3]
section_lat = SectionLattice(sequence=sections, tws0=tws0, data_dir=data_dir)
# plot twiss parameters
lat = MagneticLattice(section_lat.elem_seq)
plot_opt_func(lat, section_lat.tws)
plt.show()

p_array_init = load_particle_array(data_dir + "gun/rf_gun_new.npz", print_params=True)

E1 = 130.0e-3 
E0 = p_array_init.E
######################################### RF Settings ################################
from ocelot.utils.acc_utils import beam2rf,beam2rf_xfel_linac 
v11,phi11,v13,phi13 = beam2rf(E1=E1,chirp=-8.92,curvature=180.5,skewness=20332,n=3, freq=1.3e9, E0=E0)
v21,phi21 = beam2rf_xfel_linac(sum_voltage=578.72e-3, chirp=-9.1, init_energy=0.13)
v31,phi31 = beam2rf_xfel_linac(sum_voltage=1734.9e-3, chirp=-9.3, init_energy=0.7)
######################################### RF Settings ################################

config = {
    A1: {"phi": phi11, "v": v11 / 8, "SC": SC_exec, "smooth": True, "wake": wake_exec},
    AH1: {
        "phi": phi13,
        "v": v13 / 8,
        "match": False,
        "SC": SC_exec,
        "wake": wake_exec,
    },  ######### ************ "bounds": [-5, 5],
    LH: {"SC": SC_exec, "CSR": False, "wake": wake_exec, "match": match_exec},
    DL: {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    BC0: {
        "rho": r1,
        "match": match_exec,
        "SC": SC_exec,
        "CSR": CSR_exec,
        "wake": wake_exec,
    },
    L1: {
        "phi": phi21,
        "v": v21 / 32,
        "match": match_exec,
        "SC": SC_exec,
        "wake": wake_exec,
        "smooth": smooth_exec,
    },
    BC1: {
        "rho": r2,
        "match": match_exec,
        "SC": SC_exec,
        "CSR": CSR_exec,
        "wake": wake_exec,
    },
    L2: {
        "phi": phi31 / grad,
        "v": v31 / 96,
        "match": match_exec,
        "SC": SC_exec,
        "wake": wake_exec,
        "smooth": smooth_exec,
    },
    BC2: {
        "rho": r3,
        "match": match_exec,
        "SC": SC_exec,
        "CSR": CSR_exec,
        "wake": wake_exec,
    },
    L3: {
        "phi": phi41,
        "v": v41*1e-3 / 640,
        "match": match_exec,  # "bounds":[-1,1],
        "SC": SC_exec,
        "wake": wake_exec,
    },  # "smooth": smooth_exec},
    CL1: {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    CL2: {
        "match": match_exec
    },  ####### ******, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    CL3: {"SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    TL: {"match": match_exec, "SC": False, "wake": wake_exec},  # "CSR": CSR_exec,
    SASE1: {"match": match_exec, "SC": False, "wake": wake_exec},  # "CSR": CSR_exec,
    T4: {"match": match_exec, "SC": False, "CSR": CSR_exec, "wake": wake_exec},
    T1: {"match": match_exec, "SC": False, "CSR": CSR_exec, "wake": wake_exec},
    T3: {"match": match_exec, "SC": False, "wake": wake_exec},  # "CSR": CSR_exec,
    SASE2: {"match": match_exec, "SC": False, "CSR": CSR_exec, "wake": wake_exec},
}
show_e_beam(p_array_init)
plt.show()
p_array = section_lat.track_sections(sections=sections, p_array=p_array_init, config=config, force_ext_p_array=True,
                                     coupler_kick=coupler_kick_exec)
end = time.time()
print(f'\nduration = {end-start}')
show_e_beam(p_array)
plt.show()
