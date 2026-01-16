from ocelot import *
from ocelot.cpbd.physics_proc import *
import os
from ocelot.utils.section_track import *

import lattices.bolko_optics as bolko
import lattices.high_energy_res_optics as hires


# GLOBAL parameters

# Longitudinal beam size after BCx
#Sig_Z=(0.0019996320155001497, 0.0006893836215002082, 0.0001020391309281775, 1.25044082708419e-05) #500pC 5kA
#Sig_Z=(0.0019996320155001497, 0.0006817907866411071, 9.947650872824487e-05, 7.13045869665955e-06)  #500pC 10kA
Sig_Z = (0.0018761888067590127, 0.0006359220169656093, 9.204477386791353e-05, 7.032551498646372e-06) #250pC 5kA

# Global parameters for various Physics processes
SmoothPar=1000
LHE=6500e-9# GeV
#LHE=0.*10000e-9 # GeV
WakeSampling=500   #######***** 1000
WakeFilterOrder=20 #######***** 10
CSRBin = 400
CSRSigmaFactor=0.1
SCmesh = [63, 63, 63]
bISR=True
bool_sc_rand_mesh = True # if True, SC effect shifts mesh randomly to avoid numerical 'MBI effect'


class A1(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'A1'
        self.unit_step = 0.02
        self.input_beam_file = self.particle_dir + "gun/gun.npz"
        self.output_beam_file = self.particle_dir + 'section_A1.npz'
        self.tws_file = self.tws_dir + "tws_section_A1.npz"
        # init tracking lattice
        start_ocelot = bolko.start_ocelot
        acc1_stop = bolko.a1_sim_stop
        #start_ocelot = i1.id_22433449_
        #acc1_stop = i1.id_68749308_
        self.lattice = MagneticLattice(bolko.cell, start=start_ocelot,stop=acc1_stop, method=self.method)
        # init physics processes
        sc = SpaceCharge()
        sc.step = 1
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bool_sc_rand_mesh

        sc2 = SpaceCharge()
        sc2.step = 1 ####### ******* 2
        sc2.nmesh_xyz = SCmesh
        sc2.random_mesh = bool_sc_rand_mesh

        wake = Wake()
        wake.wake_table = WakeTable('../wakes/RF/wake_table_A1.dat')
        wake.factor = 1
        wake.step = 50 ####### ******
        wake.w_sampling = WakeSampling
        wake.filter_order = WakeFilterOrder

        smooth = SmoothBeam()
        smooth.mslice = SmoothPar
        # adding physics processes
        acc1_1_stop = bolko.a1_1_stop
        #acc1_1_stop = i1.id_75115473_
        self.add_physics_process(smooth, start=start_ocelot, stop=start_ocelot)
        self.add_physics_process(sc, start=start_ocelot, stop=acc1_1_stop)
        self.add_physics_process(sc2, start=acc1_1_stop, stop=acc1_stop)
        self.add_physics_process(wake, start=bolko.c_a1_1_1_i1, stop=acc1_stop)


class AH1(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'Injector AH1'
        self.unit_step = 0.02
        self.input_beam_file = self.particle_dir + 'section_A1.npz'
        self.output_beam_file = self.particle_dir + 'section_AH1.npz'
        self.tws_file = self.tws_dir + "tws_section_AH1.npz"
        # init tracking lattice
        acc1_stop = bolko.a1_sim_stop
        #acc1_stop = i1.id_68749308_
        acc39_stop = bolko.stlat_47_i1
        self.lattice = MagneticLattice(bolko.cell, start=acc1_stop, stop=acc39_stop, method=self.method)
        # init physics processes
        sc = SpaceCharge()
        sc.step = 5
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bool_sc_rand_mesh
        wake = Wake()
        wake.wake_table = WakeTable('../wakes/RF/wake_table_AH1.dat')
        #wake.factor = 2 ####### ******
        wake.step = 50 ###### ******10
        wake.w_sampling = WakeSampling
        wake.filter_order = WakeFilterOrder

        wake_add = Wake()
        wake_add.wake_table = WakeTable('../wakes/mod_wake_0002.700_0024.770_MONO.dat')
        wake_add.factor = 1
        wake_add.w_sampling = WakeSampling
        wake_add.filter_order = WakeFilterOrder

        # adding physics processes
       
        self.add_physics_process(sc, start=acc1_stop, stop=acc39_stop)
        self.add_physics_process(wake, start=bolko.c3_ah1_1_1_i1, stop= acc39_stop)
        self.add_physics_process(wake_add, start=bolko.stlat_47_i1, stop=bolko.stlat_47_i1) 


class LH(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'LASER HEATER MAGNETS'
        self.unit_step = 0.02
        self.input_beam_file = self.particle_dir + 'section_AH1.npz'
        self.output_beam_file = self.particle_dir + 'section_LH.npz'
        self.tws_file = self.tws_dir + "tws_section_LH.npz"
        # init tracking lattice
        acc39_stop = bolko.stlat_47_i1
        #lhm_stop = l1.match_73_i1 #start of dl # 
        lhm_stop = bolko.stsub_62_i1 
        #lhm_stop = l1.id_90904668_
        self.lattice = MagneticLattice(bolko.cell, start=acc39_stop, stop=lhm_stop, method=self.method)
        # init physics processes
        csr = CSR()
        #csr.rk_traj = True
        #csr.energy = 0.13
        csr.sigma_min = Sig_Z[0] * CSRSigmaFactor
        csr.traj_step = 0.0005
        csr.apply_step = 0.005
        sc = SpaceCharge()
        sc.step = 50 ######### **************5
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bool_sc_rand_mesh
        wake = Wake()
        wake.wake_table = WakeTable('../wakes/RF/wake_table_TDS1.dat')
        wake.factor = 1
        wake.step = 10
        wake.w_sampling = WakeSampling
        wake.filter_order = WakeFilterOrder

        wake_add = Wake()
        wake_add.wake_table = WakeTable('../wakes/mod_wake_0027.390_0050.080_MONO.dat')
        wake_add.factor = 1
        wake_add.w_sampling = WakeSampling
        wake_add.filter_order = WakeFilterOrder

        lh = LaserModulator()
        lh.dE = LHE
        lh.Lu = 0.9179999999999999
        lh.sigma_l = 300
        lh.sigma_x = 300e-6
        lh.sigma_y = 300e-6
        lh.z_waist = None

        self.add_physics_process(sc, start=acc39_stop, stop=lhm_stop)
        self.add_physics_process(csr, start=acc39_stop, stop=bolko.bpmf_52_i1)
        self.add_physics_process(wake, start=bolko.tds_start, stop=bolko.tds_stop)
        self.add_physics_process(wake_add, start=lhm_stop, stop=lhm_stop)
        self.add_physics_process(lh, start=bolko.lh_start, stop=bolko.lh_stop)


class DL(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'DOGLEG'
        self.unit_step = 0.02
        self.input_beam_file = self.particle_dir + 'section_LH.npz'
        self.output_beam_file = self.particle_dir + 'section_DL.npz'
        self.tws_file = self.tws_dir + "tws_section_DL.npz"

        # init tracking lattice
        #st2_stop = l1.id_90904668_ #i1.stsub_62_i1
        st2_stop = bolko.stsub_62_i1 #
        dogleg_stop = bolko.stlat_96_i1
        self.lattice = MagneticLattice(bolko.cell + bolko.cell, start=st2_stop, stop=dogleg_stop, method=self.method)
        # init physics processes
        csr = CSR()
        csr.n_bin = CSRBin
        csr.sigma_min = Sig_Z[0]*CSRSigmaFactor
        csr.traj_step = 0.0005
        csr.apply_step = 0.005
        wake_add = Wake()
        wake_add.wake_table = WakeTable('../wakes/mod_wake_0070.030_0073.450_MONO.dat')
        wake_add.factor = 1
        wake_add.w_sampling = WakeSampling
        wake_add.filter_order = WakeFilterOrder

        sc = SpaceCharge()
        sc.step = 25
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bool_sc_rand_mesh
        self.add_physics_process(csr, start=st2_stop, stop=dogleg_stop)
        self.add_physics_process(sc, start=st2_stop, stop=dogleg_stop)
        self.add_physics_process(wake_add, start=dogleg_stop, stop=dogleg_stop)

class I1D(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'I1D'
        self.unit_step = 0.02
        self.input_beam_file = self.particle_dir + 'section_LH.npz'
        self.output_beam_file = self.particle_dir + 'section_I1D.npz'
        self.tws_file = self.tws_dir + "tws_section_I1D.npz"

        # init tracking lattice
        st2_stop = bolko.stsub_62_i1
        dogleg_stop = bolko.ensec_66_i1d
        self.lattice = MagneticLattice(bolko.cell + bolko.cell, start=st2_stop, stop=dogleg_stop, method=self.method)
        # init physics processes
        csr = CSR()
        csr.n_bin = CSRBin
        csr.sigma_min = Sig_Z[0]*CSRSigmaFactor
        csr.traj_step = 0.0005
        csr.apply_step = 0.005

        sc = SpaceCharge()
        sc.step = 25
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bool_sc_rand_mesh
        #self.add_physics_process(csr, start=st2_stop, stop=dogleg_stop)
        self.add_physics_process(sc, start=st2_stop, stop=dogleg_stop)

class BC0(SectionTrack):

    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'BC0'
        self.unit_step = 0.02


        self.input_beam_file = self.particle_dir + 'section_DL.npz'
        self.output_beam_file = self.particle_dir + 'section_BC0.npz'
        self.tws_file = self.tws_dir + "tws_section_BC0.npz"

        # init tracking lattice
        st4_stop = bolko.stlat_96_i1
        bc0_stop = bolko.enlat_101_i1
        self.lattice = MagneticLattice(bolko.cell, start=st4_stop, stop=bc0_stop, method=self.method)

        # init physics processes
        csr = CSR()
        csr.step = 1
        csr.n_bin = CSRBin
        csr.sigma_min = Sig_Z[1]*CSRSigmaFactor
        csr.traj_step = 0.0005
        csr.apply_step = 0.001

        sc = SpaceCharge()
        sc.step = 40
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bool_sc_rand_mesh
        match_bc0 = st4_stop
        self.add_physics_process(sc, start=match_bc0, stop=bc0_stop)
        self.add_physics_process(csr, start=match_bc0, stop=bc0_stop)
        self.dipoles = [bolko.bb_96_i1, bolko.bb_98_i1, bolko.bb_100_i1, bolko.bb_101_i1]
        self.dipole_len = 0.5
        self.bc_gap=1.0

class L1(SectionTrack):
    
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'L1'
        self.unit_step = 0.02


        self.input_beam_file = self.particle_dir + 'section_BC0.npz'
        self.output_beam_file = self.particle_dir + 'section_L1.npz'
        self.tws_file = self.tws_dir + "tws_section_L1.npz"

        bc0_stop = bolko.enlat_101_i1
        acc2_stop = bolko.stlat_182_b1

        #if "coupler_kick" in kwargs:
        #    self.coupler_kick = kwargs["coupler_kick"]
        #else:
        #    self.coupler_kick = True

        # init tracking lattice
        self.lattice = MagneticLattice(bolko.cell, start=bc0_stop, stop=acc2_stop, method=self.method)

        # init physics processes
        smooth = SmoothBeam()
        smooth.mslice = SmoothPar

        sc = SpaceCharge()
        sc.step = 50
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bool_sc_rand_mesh
        wake = Wake()
        wake.wake_table = WakeTable('../wakes/RF/mod_TESLA_MODULE_WAKE_TAYLOR.dat') ###### ************ /wake_table_A1.dat')
        wake.factor = 4
        wake.step = 100
        wake.w_sampling = WakeSampling
        wake.filter_order = WakeFilterOrder
        wake_add = Wake()
        wake_add.wake_table = WakeTable('../wakes/mod_wake_0078.970_0159.280_MONO.dat') ######### ************ RF/wake_table_A1.dat')
        wake_add.factor = 1
        wake_add.w_sampling = WakeSampling
        wake_add.filter_order = WakeFilterOrder

        match_acc2 = bc0_stop
        L1_wake_kick = acc2_stop
        self.add_physics_process(smooth, start=match_acc2, stop=match_acc2)
        self.add_physics_process(sc, start=match_acc2, stop=L1_wake_kick)
        self.add_physics_process(wake, start=bolko.c_a2_1_1_l1, stop=bolko.c_a2_4_8_l1)
        self.add_physics_process(wake_add, start=L1_wake_kick, stop=L1_wake_kick)


class BC1(SectionTrack):

    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'BC1'
        self.unit_step = 0.02

        self.input_beam_file = self.particle_dir + 'section_L1.npz'
        self.output_beam_file = self.particle_dir + 'section_BC1.npz'
        self.tws_file = self.tws_dir + "tws_section_BC1.npz"


        acc2_stop = bolko.stlat_182_b1
        bc1_stop = bolko.tora_203_b1
        # init tracking lattice
        self.lattice = MagneticLattice(bolko.cell, start=acc2_stop, stop=bc1_stop, method=self.method)

        # init physics processes
        csr = CSR()
        csr.step = 1
        csr.n_bin = CSRBin
        csr.sigma_min = Sig_Z[2]*CSRSigmaFactor
        csr.traj_step = 0.0005
        csr.apply_step = 0.001

        sc = SpaceCharge()
        sc.step = 40
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bool_sc_rand_mesh

        match_bc1 = acc2_stop
        self.add_physics_process(csr, start=match_bc1, stop=bc1_stop)
        self.add_physics_process(sc, start=match_bc1, stop=bc1_stop)
        self.dipoles = [bolko.bb_182_b1, bolko.bb_191_b1, bolko.bb_193_b1, bolko.bb_202_b1]
        self.dipole_len = 0.5
        self.bc_gap=8.5


class L2(SectionTrack):

    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'L2'
        self.unit_step = 0.02

        self.input_beam_file = self.particle_dir + 'section_BC1.npz'
        self.output_beam_file = self.particle_dir + 'section_L2.npz'
        self.tws_file = self.tws_dir + "tws_section_L2.npz"

        bc1_stop = hires.tora_203_b1
        acc3t5_stop = hires.stlat_393_b2

        #if "coupler_kick" in kwargs:
        #    self.coupler_kick = kwargs["coupler_kick"]
        #else:
        #    self.coupler_kick = True

        # init tracking lattice
        self.lattice = MagneticLattice(hires.cell, start=bc1_stop, stop=acc3t5_stop, method=self.method)

        # init physics processes
        smooth = SmoothBeam()
        smooth.mslice = SmoothPar

        sc = SpaceCharge()
        sc.step = 100
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bool_sc_rand_mesh

        wake = Wake()
        wake.wake_table = WakeTable('../wakes/RF/mod_TESLA_MODULE_WAKE_TAYLOR.dat') ####### ********* wake_table_A1.dat')
        wake.factor = 4 * 3
        wake.step = 200
        wake_add = Wake()
        wake_add.wake_table = WakeTable('../wakes/mod_wake_0179.810_0370.840_MONO.dat') ########## ******** RF/wake_table_A1.dat')
        wake_add.factor = 1
        self.add_physics_process(smooth, start=bc1_stop, stop=bc1_stop)
        self.add_physics_process(sc, start=bc1_stop, stop=acc3t5_stop)
        self.add_physics_process(wake, start=hires.c_a3_1_1_l2, stop=hires.c_a5_4_8_l2)
        self.add_physics_process(wake_add, start=acc3t5_stop, stop=acc3t5_stop)



class BC2(SectionTrack):
    
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'BC2'
        self.dipoles = [hires.bb_393_b2, hires.bb_402_b2, hires.bb_404_b2, hires.bb_413_b2]
        self.dipole_len = 0.5
        self.bc_gap = 8.5

        self.unit_step = 0.02

        self.input_beam_file = self.particle_dir + 'section_L2.npz'
        self.output_beam_file = self.particle_dir + 'section_BC2.npz'
        self.tws_file = self.tws_dir + "tws_section_BC2.npz"

        acc3t5_stop = hires.stlat_393_b2
        bc2_stop = hires.tora_415_b2
        # init tracking lattice
        self.lattice = MagneticLattice(hires.cell, start=acc3t5_stop, stop=bc2_stop, method=self.method)

        # init physics processes

        csr = CSR()
        csr.step = 1
        csr.n_bin = CSRBin
        csr.sigma_min = Sig_Z[3]*CSRSigmaFactor #Sig_Z[2]
        csr.traj_step = 0.0005
        csr.apply_step = 0.001

        sc = SpaceCharge()
        sc.step = 50
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bool_sc_rand_mesh


        self.add_physics_process(csr, start=acc3t5_stop, stop=bc2_stop)
        self.add_physics_process(sc, start=acc3t5_stop, stop=bc2_stop)

class B2D(SectionTrack):
    
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'B2D'
        self.unit_step = 0.02

        self.input_beam_file = self.particle_dir + 'section_BC2.npz'
        self.output_beam_file = self.particle_dir + 'section_B2D.npz'
        self.tws_file = self.tws_dir + "tws_section_B2D.npz"

        bc2_stop = hires.tora_415_b2
        b2d_stop =hires.otra_473_b2d
        # init tracking lattice
        self.lattice = MagneticLattice(hires.cell, start=bc2_stop, stop=b2d_stop, method=self.method)

        # init physics processes

        csr = CSR()
        csr.step = 1
        csr.n_bin = CSRBin
        csr.sigma_min = Sig_Z[3] * CSRSigmaFactor #Sig_Z[2]
        csr.traj_step = 0.0005
        csr.apply_step = 0.001

        sc = SpaceCharge()
        sc.step = 50
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bool_sc_rand_mesh


        self.add_physics_process(csr, start=bc2_stop, stop=b2d_stop)
        self.add_physics_process(sc, start=bc2_stop, stop=b2d_stop)


