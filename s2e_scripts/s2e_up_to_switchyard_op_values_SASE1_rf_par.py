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
all_sections = [A1, AH1, LH, DL, BC0, L1, BC1, L2, BC2]#, L3, CL1, CL2, CL3, TL, SASE1, T4, SASE3, T4D]

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
#r1 = 4.1218                 # deflecting radius in BC0
#r2 = 8.3934                 # deflecting radius in BC1
#r3 = 14.4111                # deflecting radius in BC2
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
plot_opt_func(lat, section_lat.tws)
plt.show()

# sequence of sections for tracking.
sections = [A1, AH1, LH, DL, BC0, L1, BC1, L2, BC2]#, L3, CL1, CL2, CL3, TL]
section_lat = SectionLattice(sequence=sections, tws0=tws0, data_dir=data_dir)
# plot twiss parameters
lat = MagneticLattice(section_lat.elem_seq)
plot_opt_func(lat, section_lat.tws)
plt.show()

p_array_init = load_particle_array(data_dir + "gun/gun.npz", print_params=True)


E1 = 129.9e-3 
E0 = p_array_init.E

from ocelot.utils.acc_utils import beam2rf,beam2rf_xfel_linac 
v11,phi11,v13,phi13 = beam2rf(E1=E1,chirp=-9.08,curvature=240,skewness=22002,n=3, freq=1.3e9, E0=E0)
v21,phi21 = beam2rf_xfel_linac(sum_voltage=578.56e-3, chirp=-9.27, init_energy=0.13)
v31,phi31 = beam2rf_xfel_linac(sum_voltage=1742.53e-3, chirp=-10.31, init_energy=0.7)


config = {
    A1:    {"phi": phi11, "v": v11*1e3 / 8*1e-3,
           "SC": SC_exec, "smooth": True, "wake": wake_exec},
    AH1:   {"phi": phi13, "v": v13*1e3 / 8*1e-3,
           "match": False, "SC": SC_exec, "wake": wake_exec}, ######### ************ "bounds": [-5, 5], 
    LH:    {"SC": SC_exec, "CSR": False, "wake": wake_exec, "match": match_exec},
    DL:    {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    BC0:   {"rho": r1,
           "match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    L1:    {"phi": phi21, "v": v21*1e3 / 32*1e-3, "match": match_exec,
           "SC": SC_exec, "wake": wake_exec, "smooth": smooth_exec},
    BC1:   {"rho": r2,
           "match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    L2:    {"phi": phi31, "v": v31*1e3 / 96*1e-3, "match": match_exec,
            "SC": SC_exec, "wake": wake_exec, "smooth": smooth_exec},
    BC2:   {"rho": r3,
            "match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    L3:    {"phi": phi41 / grad, "v": v41 / 640*1e-3,
            "match": match_exec, #"bounds":[-1,1],
            "SC": SC_exec, "wake": wake_exec},# "smooth": smooth_exec},
    CL1:   {"match": match_exec, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    CL2:   {"match": match_exec}, ####### ******, "SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    CL3:   {"SC": SC_exec, "CSR": CSR_exec, "wake": wake_exec},
    TL:    {"match": match_exec, "SC": False,  "wake": wake_exec},#"CSR": CSR_exec,
    SASE1: {"match": match_exec, "SC": False, "wake": wake_exec},#"CSR": CSR_exec,
    T4:    {"match": match_exec, "SC": False, "CSR": CSR_exec, "wake": wake_exec},
    T1:    {"match": match_exec, "SC": False, "CSR": CSR_exec, "wake": wake_exec},
    T3:    {"match": match_exec, "SC": False, "wake": wake_exec},#"CSR": CSR_exec,
    SASE2: {"match": match_exec, "SC": False, "CSR": CSR_exec, "wake": wake_exec},
}

show_e_beam(p_array_init)
plt.show()

#reducing the number of particles to speed up the 
p_array_less = p_array_init.thin_out(nth=4) 

s_start = deepcopy(p_array_init.s)
p_array = section_lat.track_sections(sections=sections, p_array=p_array_less, config=config, force_ext_p_array=True,
                                     coupler_kick=coupler_kick_exec)

end = time.time()
print(f'\nduration = {end-start}')
# collect tws for all sections
seq_global = []
tws_track_global = []
L = 0
for s in sections:
    sec = section_lat.dict_sections[s]
    seq_global.append(sec.lattice.sequence)
    for tws in sec.tws_track:
        tws.s += L
    tws_track_global = np.append(tws_track_global, sec.tws_track)
    L += sec.lattice.totalLen

# postprocessing
S = [tw.s+3.2 for tw in section_lat.tws]
s_max=max(S)
BetaX = [tw.beta_x for tw in section_lat.tws]
BetaY = [tw.beta_y for tw in section_lat.tws]
AlphaX = [tw.alpha_x for tw in section_lat.tws]
AlphaY = [tw.alpha_y for tw in section_lat.tws]
GammaX = [tw.gamma_x for tw in section_lat.tws]
GammaY = [tw.gamma_y for tw in section_lat.tws]
E = [tw.E for tw in section_lat.tws]


S_tr = np.array([tw.s for tw in tws_track_global])
S_tr = S_tr + s_start
BetaX_tr = [tw.beta_x for tw in tws_track_global]
BetaY_tr = [tw.beta_y for tw in tws_track_global]
AlphaX_tr = [tw.alpha_x for tw in tws_track_global]
AlphaY_tr = [tw.alpha_y for tw in tws_track_global]
EmitX_tr = [tw.emit_x for tw in tws_track_global]
EmitY_tr = [tw.emit_y for tw in tws_track_global]
E_tr=[tw.E for tw in tws_track_global]
sig_tau = np.sqrt([tw.tautau for tw in tws_track_global])
Q=np.sum(p_array.q_array)
I = c*Q/np.sqrt(2*pi)/sig_tau
Sx=np.zeros(len(S_tr))
Sy=np.zeros(len(S_tr))
for i in range(len(S_tr)):
    gamma=E_tr[i-1]/m_e_GeV
    EmitX_tr[i-1]=EmitX_tr[i-1]*gamma*1e6
    EmitY_tr[i-1]=EmitY_tr[i-1]*gamma*1e6
    Sx[i-1] = I[i-1]  * BetaX_tr[i-1] / (1.7045e+04 * gamma * gamma * EmitX_tr[i-1]*1e-6)
    Sy[i - 1] = I[i - 1] * BetaY_tr[i - 1] / (1.7045e+04 * gamma * gamma * EmitY_tr[i - 1] * 1e-6)

s0 = 0; s1 = s_max
plt.figure()
plt.subplot(221)
plt.plot(S,BetaX,label='design');plt.plot(S_tr,BetaX_tr,label='beam')
plt.legend(); plt.ylabel(r"$\beta_x$[m]")
plt.axis([s0, s1,-1,100])
plt.subplot(222)
plt.plot(S,BetaY,S_tr,BetaY_tr)
plt.xlim([s0, s1])
plt.subplot(223)
plt.plot(S,AlphaX,S_tr,AlphaX_tr)
plt.xlabel("s[m]");plt.ylabel(r"$\alpha_x$")
plt.xlim([s0, s1])
plt.subplot(224)
plt.plot(S,AlphaY,S_tr,AlphaY_tr)
plt.xlabel("s[m]")
plt.xlim([s0, s1])

plt.figure()
plt.subplot(211)
plt.plot(S_tr,EmitX_tr,S_tr,EmitY_tr)
plt.grid(True); plt.title("Emittances"); plt.xlabel("s[m]"); plt.ylabel(r"$\epsilon_x,\epsilon_y [\mu m]$")
plt.xlim([s0, s1])
plt.subplot(212)
plt.plot(S,E,S_tr,E_tr)
plt.grid(True); plt.title("Energy"); plt.xlabel("s[m]"); plt.ylabel(r"E [GeV]")
#plt.axis([s0, s1, 0, 3])

plt.figure()
plt.subplot(211)
plt.plot(S_tr,sig_tau*1e3)
plt.grid(False); #plt.title("Sigma_tau");
plt.ylabel("$\sigma_z$ [mm]")
plt.xlim([s0, s1])
plt.subplot(212)
plt.plot(S_tr,Sx,S_tr,Sy)
plt.plot(S_tr,Sx, "b", label=r"$k_x^{sc}$")
plt.plot(S_tr,Sy, "r", label=r"$k_y^{sc}$")
plt.legend()
plt.grid(False)
plt.xlabel("z[m]")
plt.xlim([s0, s1])

show_e_beam(p_array, nparts_in_slice=5000, smooth_param=0.01, nfig=13, title="")
n_out = len(S_tr)
out = np.zeros((n_out, 8))
out[:, 0] = S_tr
out[:, 1] = AlphaX_tr
out[:, 2] = BetaX_tr
out[:, 3] = EmitX_tr
out[:, 4] = AlphaY_tr
out[:, 5] = BetaY_tr
out[:, 6] = EmitY_tr
out[:, 7] = E_tr

np.savetxt("Optics.txt", out)

plt.show()

v11,phi11,v13,phi13 = beam2rf(E1=E1,chirp=-9.7,curvature=240,skewness=23050,n=3, freq=1.3e9, E0=E0)
v21,phi21 = beam2rf_xfel_linac(sum_voltage=578.72e-3, chirp=-7.69, init_energy=0.13)
v31,phi31 = beam2rf_xfel_linac(sum_voltage=1734.9e-3, chirp=-9.70, init_energy=0.7)