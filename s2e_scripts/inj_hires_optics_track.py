import sys
sys.path.insert(1, "../")

from ocelot import *
from ocelot.cpbd.physics_proc import IBS
from ocelot.gui import *
import lattices.longlist_2024_07_04.i1 as i1
import lattices.longlist_2024_07_04.i1d as i1d
from ocelot.utils.acc_utils import beam2rf, beam2rf_xfel_linac


i1.q_37_i1.k1 = -1.624560e+00
i1.q_38_i1.k1 = 1.823629e+00
i1.qi_46_i1.k1 = -6.922240e-01
i1.qi_47_i1.k1 = 4.536175e-01
i1.qi_50_i1.k1 = 4.122258e-01

v11, phi11, v13, phi13 = beam2rf(E1=130e-3, chirp=-2, curvature=222, skewness=28000, n=3, freq=1.3e9, E0=0.0065)
print(v11, phi11, v13, phi13)

for elem in i1.cell:
    if elem.__class__ == Cavity:
        if "C.A1.1" in elem.id:
            elem.v = v11/8
            elem.phi = phi11
        elif "C3.AH1.1" in elem.id:
            elem.v = v13/8
            elem.phi = phi13


DDx = {1.197: [-2.14371, 3.50288, -1.05],
       1.024: [ -2.1415, 3.50095, 0.45],
       0.801: [-2.14121, 3.45060, 2.45],
       0.592: [-2.14030, 3.32194, 4.401795] }

quads_to_change = [i1.qi_60_i1, i1.qi_61_i1, i1d.qi_63_i1d]

# check optics with dispersion Dx = 1.197 m

for i, q in enumerate(quads_to_change):
    q.k1 = DDx[1.197][i]

lat = MagneticLattice(i1.cell + i1d.cell,start=i1.start_sim,  stop=i1d.otrc_64_i1d)

# TRACKING with collective effects
navi = Navigator(lat, unit_step=0.01)

sc_mesh = [63, 63, 63]
bool_sc_rand_mesh = True # if True, SC effect shifts mesh randomly to avoid numerical 'MBI effect'

sc = SpaceCharge(step=1, nmesh_xyz=sc_mesh, random_mesh=bool_sc_rand_mesh)

sc2 = SpaceCharge(step=2, nmesh_xyz=sc_mesh, random_mesh=bool_sc_rand_mesh)

sc3 = SpaceCharge(step=5, nmesh_xyz=sc_mesh, random_mesh=bool_sc_rand_mesh)

wake_sampling = 1000
wake_filter_order = 10

wake = Wake(step=10, factor=1, w_sampling=wake_sampling, filter_order=wake_filter_order)
wake.wake_table = WakeTable('../wakes/RF/wake_table_A1.dat')


wake_ah1 = Wake(step=10, factor=1, w_sampling=wake_sampling, filter_order=wake_filter_order)
wake_ah1.wake_table = WakeTable('../wakes/RF/wake_table_AH1.dat')

wake_tds = Wake(step=10, factor=1, w_sampling=wake_sampling, filter_order=wake_filter_order)
wake_tds.wake_table = WakeTable('../wakes/RF/wake_table_TDS1.dat')

smooth_par = 1000
smooth = SmoothBeam(mslice = smooth_par)

ibs = IBS(step=10, method="Huang", bound=[-0.1, 0.1])


navi.add_physics_proc(smooth, i1.start_sim, i1.start_sim)
# space charge exclude LH chicane and dumb line
navi.add_physics_proc(sc, i1.start_sim, i1.a1_1_stop)
navi.add_physics_proc(sc2, i1.a1_1_stop, i1.bl_48i_i1)
navi.add_physics_proc(sc3, i1.qi_50_i1, i1.stsub_62_i1)
# wakes
navi.add_physics_proc(wake, i1.c_a1_1_1_i1, i1.a1_sim_stop)
navi.add_physics_proc(wake_ah1, i1.c3_ah1_1_1_i1, i1.ah_stop)
navi.add_physics_proc(wake_tds, i1.tds_start, i1.tds_stop)
# ibs, optional
#navi.add_physics_proc(ibs, i1_track.start_sim, lat.sequence[-1])

parray = load_particle_array("../beam_files/gun/gun.npz")
print(parray)
tws_track, parray = track(lat, p_array=parray, navi=navi)

plot_opt_func(lat, tws_track, top_plot=["E"])
plt.show()
show_e_beam(p_array=parray)
plt.show()