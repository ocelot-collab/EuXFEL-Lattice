import sys
sys.path.insert(1, "../")
import copy
from ocelot import *
from ocelot.cpbd.match import beam_matching, match_beam
from ocelot.cpbd.physics_proc import IBS
from ocelot.gui import *
import lattices.longlist_2024_07_04.i1 as i1
import lattices.longlist_2024_07_04.i1d as i1d


parray = load_particle_array("../beam_files/gun/gun.npz")


# TRACK first trough A1
lat_a1 = MagneticLattice(i1.cell , start=i1.start_sim, stop=i1.a1_sim_stop, method={"global": SecondTM})
navi_a1 = Navigator(lat_a1, unit_step=0.01)

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

navi_a1.add_physics_proc(smooth, i1.start_sim, i1.start_sim)
navi_a1.add_physics_proc(sc, i1.start_sim, i1.a1_1_stop)
navi_a1.add_physics_proc(sc2, i1.a1_1_stop, navi_a1.lat.sequence[-1])
navi_a1.add_physics_proc(wake, i1.c_a1_1_1_i1, i1.a1_sim_stop)




#tws_track, parray = track(lat_a1, p_array=parray, navi=navi_a1)
#save_particle_array("parray_a1.npz", parray)

parray_a1 = load_particle_array("parray_a1.npz")
tws_a1 = get_envelope(parray_a1)
print(tws_a1)
#parray_a1 = copy.deepcopy(parray)
show_e_beam(p_array=parray_a1)
plt.show()

# ***************** FROM A1.stop to  MATCH.52.I1 ***********************
parray = copy.deepcopy(parray_a1.thin_out(10))
acc39_stop = i1.stlat_47_i1
lat_m52 = MagneticLattice(i1.cell, start=i1.a1_sim_stop, stop=i1.match_52_i1, method={"global": SecondTM})

navi_m52 = Navigator(lat_m52, unit_step=0.01)
navi_m52.add_physics_proc(sc3, i1.a1_sim_stop, i1.match_52_i1)
navi_m52.add_physics_proc(wake_ah1, i1.c3_ah1_1_1_i1, acc39_stop)
#navi_track.add_physics_proc(wake_tds, i1.tds_start, i1.tds_stop)


betx = 3.131695851; alfx = -0.9249364470
bety = 5.417462794; alfy = +1.730107901
tws_end = Twiss(beta_x=betx, beta_y=bety, alpha_x=alfx, alpha_y=alfy, E=0.13)

vars = [i1.q_37_i1, i1.q_38_i1, i1.qi_46_i1, i1.qi_47_i1, i1.qi_50_i1]

quads = beam_matching(parray, navi=navi_m52, tws_end=tws_end, vars=vars, iter=2)
for q in quads:
    print(q)

# i1.q_37_i1.k1=-1.5346634683471154
# i1.q_38_i1.k1=1.6294120856150203
# i1.qi_46_i1.k1=0.17290161041033697
# i1.qi_47_i1.k1=-0.03485462369332516
# i1.qi_50_i1.k1=-0.8572077738072157


constr = {i1.match_52_i1:{'beta_x':betx, 'beta_y':bety, "alpha_x": alfx, "alpha_y": alfy}}
match_beam(navi_m52.lat, constr, vars=vars, p_array=parray, navi=navi_m52, verbose=True, max_iter=30, method='simplex',
               vary_bend_angle=False, min_i5=False)
#
#for q in vars:
#    print(q)

#lat.save_as_py_file("i1_r56_12.py")

