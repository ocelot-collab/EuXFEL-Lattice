#ocelot_dir = "/Users/tomins/Nextcloud/DESY/repository/ocelot"
import sys

#sys.path.append(ocelot_dir)
sys.path.insert(1, "../")

from ocelot import *
from ocelot.cpbd.physics_proc import IBS
from ocelot.gui import *

from euxfel.subsequences import i1, i1d

lat = MagneticLattice(i1.cell + i1d.cell)

tws = twiss(lat, i1.twiss0)

plot_opt_func(lat, tws,fig_name="Design Optics", legend=False)
plt.show()

# different dispersions amplitude on screen OTRC.64.I1D
# DDx = {Dx: ['QI.60.I1'.k1, 'QI.61.I1'.k1, 'QI.63.I1D'.k1]}
DDx = {1.197: [-2.14371, 3.50288, -1.05],
       1.024: [ -2.1415, 3.50095, 0.45],
       0.801: [-2.14121, 3.45060, 2.45],
       0.592: [-2.14030, 3.32194, 4.401795] }

quads_to_change = [i1.qi_60_i1, i1.qi_61_i1, i1d.qi_63_i1d]

# check optics with dispersion Dx = 1.197 m

for i, q in enumerate(quads_to_change):
    q.k1 = DDx[1.197][i]

lat = MagneticLattice(i1.cell + i1d.cell, stop=i1d.otrc_64_i1d)
tws = twiss(lat, i1.twiss0)

plot_opt_func(lat, tws,fig_name="HiRes optics up to OTRC.64.I1D", legend=False)
plt.show()

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
acc1_1_stop = i1.a1_1_stop
acc39_stop = i1.stlat_47_i1

navi.add_physics_proc(smooth, i1.start_ocelot, i1.start_ocelot)
navi.add_physics_proc(sc, i1.start_ocelot, i1.a1_1_stop)
navi.add_physics_proc(sc2, i1.a1_1_stop, i1.a1_sim_stop)
navi.add_physics_proc(wake, i1.c_a1_1_1_i1, i1.a1_sim_stop)
navi.add_physics_proc(sc3, i1.a1_sim_stop, lat.sequence[-1])
navi.add_physics_proc(wake_ah1, i1.c3_ah1_1_1_i1, acc39_stop)
navi.add_physics_proc(wake_tds, i1.tds_start, i1.tds_stop)
navi.add_physics_proc(ibs, i1.start_ocelot, lat.sequence[-1])

parray = load_particle_array("../beam_files/gun/gun.npz")
tws_track, parray = track(lat, p_array=parray, navi=navi, bounds=[-1, 1], slice="Imax")

plot_opt_func(lat, tws_track, top_plot=["E"])
plt.show()
show_e_beam(p_array=parray)
plt.show()
