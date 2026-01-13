#ocelot_dir = "/Users/tomins/Nextcloud/DESY/repository/ocelot"
import sys

#sys.path.append(ocelot_dir)
sys.path.insert(1, "../")
#print(sys.path)
# from s2e_sections.sections_special_lattice import *
from s2e_sections.sections import *
from ocelot.utils.section_track import *
from ocelot.gui.accelerator import *
import time
from ocelot.common.globals import *
from ocelot import *
from ocelot.utils.acc_utils import beam2rf,beam2rf_xfel_linac

data_dir = "../beam_files/"

####################  Physics Effects control globaly ##################
match_exec = True # artificially (kick) match beam to design optics
smooth_exec = True # filtering
wake_exec = True
SC_exec = True
CSR_exec = True
coupler_kick_exec = False  # coupler effect in RF modules, quadrupole and dipole (usially off) component, which now is not in the lattice files


# all sections which can be potentially used in s2e
all_sections = [A1, AH1, LH, DL, BC0, L1, BC1, L2, BC2, B2D]  # , L3, CL1, CL2, CL3, STN10]#, SASE1, T4, SASE3, T4D]

######################### Initial Twiss paramters for design optics ##################
tws0 = Twiss()
tws0.E = 0.005
tws0.beta_x  = 0.2865426867699372
tws0.beta_y  = 0.2865426867699381
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
# BC magnet radius read from BKR
r1 = 0.5 / 0.1366592804  # 3.6587343247857467
r2 = 0.5 / 0.0532325422  # 9.392750737348779
r3 = 0.5 / 0.0411897704  # 12.138936321917445
#################################### Compression WP ################################

# init sections which can be used for tracking
#all_sections = [TL, SASE1]#, T4, SASE3, T4D]
section_lat = SectionLattice(sequence=all_sections, tws0=tws0, data_dir=data_dir)
# plot twiss parameters
lat = MagneticLattice(section_lat.elem_seq)
#plot_opt_func(lat, section_lat.tws)
#plt.show()

# sequence of sections for tracking.
sections = [A1, AH1, LH, DL, BC0, L1, BC1, L2, BC2, B2D]#, L3, CL1, CL2, CL3, TL]



E1 = 130e-3
E0 = 0.0065


v11,phi11,v13,phi13 = beam2rf(E1=E1, chirp=-9.11, curvature=222, skewness=28000, n=3, freq=1.3e9, E0=E0)#(E1=E1, chirp=-9.314, curvature=230, skewness=23101, n=3, freq=1.3e9, E0=E0)
v21,phi21 = beam2rf_xfel_linac(sum_voltage=570e-3, chirp=-5.4, init_energy=0.13)
v31,phi31 = beam2rf_xfel_linac(sum_voltage=1.7, chirp=-9.4, init_energy=0.7)

config = {
    A1:    {"phi": phi11, "v": v11 / 8,
           "SC": SC_exec, "smooth": True, "wake": wake_exec},
    AH1:   {"phi": phi13, "v": v13 / 8,
           "match": False, "SC": SC_exec, "wake": wake_exec}, ######### ************ "bounds": [-5, 5], 
    LH:    {"SC": SC_exec, "CSR": False, "wake": wake_exec, "match": match_exec},
    DL:    {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    BC0:   {"rho": r1,
           "match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    L1:    {"phi": phi21, "v": v21 / 32, "match": match_exec,
           "SC": SC_exec, "wake": wake_exec, "smooth": smooth_exec},
    BC1:   {"rho": r2,
           "match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    L2:    {"phi": phi31, "v": v31 / 96, "match": match_exec,
            "SC": SC_exec, "wake": wake_exec, "smooth": smooth_exec},
    BC2:   {"rho": r3,
            "match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    B2D:   {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec}
}

p_array = load_particle_array(data_dir + "gun/gun.npz")
#show_e_beam(p_array)
#plt.show()

p_array = section_lat.track_sections(sections=sections, p_array=p_array, config=config, force_ext_p_array=True,
                                     coupler_kick=coupler_kick_exec)


plot_opt_func(lat, section_lat.tws_track, top_plot=["E"], fig_name="Track Twiss")


show_e_beam(p_array)

plt.show()
