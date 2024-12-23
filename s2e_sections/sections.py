from ocelot.utils.section_track import *
import accelerator.lattice.i1 as i1
import accelerator.lattice.l1 as l1
import accelerator.lattice.l2 as l2
import accelerator.lattice.l3 as l3
import accelerator.lattice.cl as cl
import accelerator.lattice.tl34 as tl34
import accelerator.lattice.sase1 as sase1
import accelerator.lattice.t4 as t4
import accelerator.lattice.sase3 as sase3
import accelerator.lattice.t4d as t4d

import accelerator.lattice.sase2_branch.t1 as t1
#import accelerator.lattice.sase2_branch.t3 as t3
import accelerator.lattice.sase2_branch.tl34_sa2 as tl34_sa2
import accelerator.lattice.sase2_branch.t3_bump_fin as t3
import accelerator.lattice.sase2_branch.t5 as t5
import accelerator.lattice.sase2_branch.sase2 as sase2
import accelerator.lattice.sase2_branch.t5d as t5d
from ocelot import *
from ocelot.cpbd.physics_proc import *
import os

Sig_Z=(0.0019996320155001497, 0.0006893836215002082, 0.0001020391309281775, 1.25044082708419e-05) #500pC 5kA
#Sig_Z=(0.0019996320155001497, 0.0006817907866411071, 9.947650872824487e-05, 7.13045869665955e-06)  #500pC 10kA
#Sig_Z=(0.0018761888067590127, 0.0006359220169656093, 9.204477386791353e-05, 7.032551498646372e-06) #250pC 5kA

Sig_Z=(0.0012761713706630296, 0.0004330848338445355, 6.154708486466915e-05, 5.015501546574598e-06)
Sig_Z = (0.0012761713706630296, 0.000411, 5.88e-05, 5.132214278750506e-06)

SmoothPar=1000

# LHE=0*5000e-9  # GeV for article about LPS dynamics
LHE=0.9*10000e-9 # GeV
WakeSampling=1000
WakeFilterOrder=10
CSRBin = 400
CSRSigmaFactor=0.1
SCmesh = [63, 63, 63]
bISR=True
bRandomMesh=True

root_dir = "/Users/tomins/Nextcloud/DESY/repository/ocelot/projects/1_XFEL_s2e_for_dechirper/"

class A1(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'A1'
        self.unit_step = 0.02
        self.input_beam_file = self.particle_dir + 'rfgun.0320_42_2ps7.ast'
        self.output_beam_file = self.particle_dir + 'section_A1.npz'
        self.tws_file = self.tws_dir + "tws_section_A1.npz"
        # init tracking lattice
        start_sim = i1.start_sim
        acc1_stop = i1.a1_sim_stop
        self.lattice = MagneticLattice(i1.cell, start=start_sim,stop=acc1_stop, method=self.method)
        # init physics processes
        sc = SpaceCharge()
        sc.step = 1
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bRandomMesh

        sc2 = SpaceCharge()
        sc2.step = 2
        sc2.nmesh_xyz = SCmesh
        sc2.random_mesh = bRandomMesh

        wake = Wake()
        wake.wake_table = WakeTable(root_dir + 'accelerator/wakes/RF/wake_table_A1.dat')
        wake.factor = 1
        wake.step = 10
        wake.w_sampling = WakeSampling
        wake.filter_order = WakeFilterOrder

        smooth = SmoothBeam()
        smooth.mslice = SmoothPar
        # adding physics processes
        acc1_1_stop = i1.a1_1_stop
        self.add_physics_process(smooth, start=start_sim, stop=start_sim)
        self.add_physics_process(sc, start=start_sim, stop=acc1_1_stop)
        self.add_physics_process(sc2, start=acc1_1_stop, stop=acc1_stop)
        self.add_physics_process(wake, start=i1.c_a1_1_1_i1, stop=acc1_stop)


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
        acc1_stop = i1.a1_sim_stop
        acc39_stop = i1.stlat_47_i1
        self.lattice = MagneticLattice(i1.cell, start=acc1_stop, stop=acc39_stop, method=self.method)
        # init physics processes
        sc = SpaceCharge()
        sc.step = 5
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bRandomMesh
        wake = Wake()
        wake.wake_table = WakeTable(root_dir + 'accelerator/wakes/RF/wake_table_AH1.dat')
        wake.factor = 1
        wake.step = 10
        wake.w_sampling = WakeSampling
        wake.filter_order = WakeFilterOrder
        # adding physics processes
        self.add_physics_process(sc, start=acc1_stop, stop=acc39_stop)
        self.add_physics_process(wake, start=i1.c3_ah1_1_1_i1, stop= acc39_stop)


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
        acc39_stop = i1.stlat_47_i1
        #lhm_stop = l1.id_90904668_ #for s2e
        #lhm_stop = l1.cix_65_i1    #approx. corresponds to the position of the screen in I1D.
        lhm_stop = l1.dl_start #for going in I1D
        self.lattice = MagneticLattice(i1.cell + l1.cell, start=acc39_stop, stop=lhm_stop, method=self.method)
        # init physics processes
        csr = CSR()
        csr.rk_traj = True
        csr.energy = 0.13
        csr.sigma_min = Sig_Z[0] * CSRSigmaFactor
        csr.traj_step = 0.0005
        csr.apply_step = 0.005
        sc = SpaceCharge()
        sc.step = 5
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bRandomMesh
        wake = Wake()
        wake.wake_table = WakeTable(root_dir + 'accelerator/wakes/RF/wake_table_TDS1.dat')
        wake.factor = 1
        wake.step = 10
        wake.w_sampling = WakeSampling
        wake.filter_order = WakeFilterOrder

        lh = LaserModulator()
        lh.dE = LHE
        lh.Lu = 0.74
        lh.sigma_l = 300
        lh.sigma_x = 300e-6
        lh.sigma_y = 300e-6
        lh.z_waist = None

        self.add_physics_process(sc, start=acc39_stop, stop=lhm_stop)
        self.add_physics_process(csr, start=acc39_stop, stop=i1.bpmf_52_i1)
        self.add_physics_process(wake, start=i1.tds_start, stop=i1.tds_stop)
        self.add_physics_process(lh, start=i1.lh_start, stop=i1.lh_stop)


class DL(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'DOGLEG'
        self.unit_step = 0.02
        self.input_beam_file = self.particle_dir + 'section_LH.npz'
        self.output_beam_file = self.particle_dir + 'section_DL.npz'
        self.tws_file = self.tws_dir + "tws_section_DL.npz"

        #if "suffix" in kwargs:
        #    filename, file_extension = os.path.splitext(self.input_beam_file)
        #    self.input_beam_file = filename + str(kwargs["suffix"]) + file_extension
        #    filename, file_extension = os.path.splitext(self.output_beam_file)
        #    self.output_beam_file = filename + str(kwargs["suffix"]) + file_extension
        #    filename, file_extension = os.path.splitext(self.tws_file)
        #    self.tws_file = filename + str(kwargs["suffix"]) + file_extension

        # init tracking lattice
        st2_stop = l1.dl_start
        dogleg_stop = l1.stlat_96_i1
        self.lattice = MagneticLattice(l1.cell, start=st2_stop, stop=dogleg_stop, method=self.method)
        # init physics processes
        csr = CSR()
        csr.n_bin = CSRBin
        csr.sigma_min = Sig_Z[0]*CSRSigmaFactor
        #csr.traj_step = 0.0005
        #csr.apply_step = 0.005
        wake_add = Wake()
        wake_add.wake_table = WakeTable('accelerator/wakes/mod_wake_0070.030_0073.450_MONO.dat')
        wake_add.factor = 1
        wake_add.w_sampling = WakeSampling
        wake_add.filter_order = WakeFilterOrder

        sc = SpaceCharge()
        sc.step = 25
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bRandomMesh
        self.add_physics_process(csr, start=st2_stop, stop=dogleg_stop)
        #self.add_physics_process(sc, start=st2_stop, stop=dogleg_stop)
        self.add_physics_process(wake_add, start=dogleg_stop, stop=dogleg_stop)



class BC0(SectionTrack):

    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'BC0'
        self.unit_step = 0.02


        self.input_beam_file = self.particle_dir + 'section_DL.npz'
        self.output_beam_file = self.particle_dir + 'section_BC0.npz'
        self.tws_file = self.tws_dir + "tws_section_BC0.npz"


        #if "suffix" in kwargs:
        #    filename, file_extension = os.path.splitext(self.input_beam_file)
        #    self.input_beam_file = filename + str(kwargs["suffix"]) + file_extension
        #    filename, file_extension = os.path.splitext(self.output_beam_file)
        #    self.output_beam_file = filename + str(kwargs["suffix"]) + file_extension
        #    filename, file_extension = os.path.splitext(self.tws_file)
        #    self.tws_file = filename + str(kwargs["suffix"]) + file_extension

        # init tracking lattice
        st4_stop = l1.stlat_96_i1
        bc0_stop = l1.enlat_101_i1
        self.lattice = MagneticLattice(l1.cell, start=st4_stop, stop=bc0_stop, method=self.method)

        # init physics processes

        # init physics processes
        csr = CSR()
        csr.step = 1
        csr.n_bin = CSRBin
        csr.sigma_min = Sig_Z[1]*CSRSigmaFactor
        #csr.traj_step = 0.0005
        #csr.apply_step = 0.001

        sc = SpaceCharge()
        sc.step = 40
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bRandomMesh
        match_bc0 = st4_stop
        #self.add_physics_process(sc, start=match_bc0, stop=bc0_stop)
        self.add_physics_process(csr, start=match_bc0, stop=bc0_stop)
        self.dipoles = [l1.bb_96_i1, l1.bb_98_i1, l1.bb_100_i1, l1.bb_101_i1]
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

        #if "suffix" in kwargs:
        #    filename, file_extension = os.path.splitext(self.input_beam_file)
        #    suff = str(kwargs["suffix"])
        #    indx = suff.find("_chirpL1_")
        #    input_suff = suff[:indx]
        #    self.input_beam_file = filename + input_suff + file_extension
        #    print("SECTION L1: ", self.input_beam_file)
        #    filename, file_extension = os.path.splitext(self.output_beam_file)
        #    self.output_beam_file = filename + str(kwargs["suffix"]) + file_extension
        #    filename, file_extension = os.path.splitext(self.tws_file)
        #    self.tws_file = filename + str(kwargs["suffix"]) + file_extension


        bc0_stop = l1.enlat_101_i1
        acc2_stop = l1.stlat_182_b1

        if "coupler_kick" in kwargs:
            self.coupler_kick = kwargs["coupler_kick"]
        else:
            self.coupler_kick = True

        # init tracking lattice
        self.lattice = MagneticLattice(l1.cell, start=bc0_stop, stop=acc2_stop, method=self.method)

        # init physics processes
        smooth = SmoothBeam()
        smooth.mslice = SmoothPar

        sc = SpaceCharge()
        sc.step = 50
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bRandomMesh
        wake = Wake()
        wake.wake_table = WakeTable('accelerator/wakes/RF/mod_TESLA_MODULE_WAKE_TAYLOR.dat')
        wake.factor = 4
        wake.step = 100
        wake.w_sampling = WakeSampling
        wake.filter_order = WakeFilterOrder
        wake_add = Wake()
        wake_add.wake_table = WakeTable('accelerator/wakes/mod_wake_0078.970_0159.280_MONO.dat')
        wake_add.factor = 1
        wake_add.w_sampling = WakeSampling
        wake_add.filter_order = WakeFilterOrder

        match_acc2 = bc0_stop
        L1_wake_kick = acc2_stop
        self.add_physics_process(smooth, start=match_acc2, stop=match_acc2)
        self.add_physics_process(sc, start=match_acc2, stop=L1_wake_kick)
        self.add_physics_process(wake, start=l1.c_a2_1_1_l1, stop=l1.c_a2_4_8_l1)
        self.add_physics_process(wake_add, start=L1_wake_kick, stop=L1_wake_kick)


class BC1(SectionTrack):

    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'BC1'
        self.unit_step = 0.05

        self.input_beam_file = self.particle_dir + 'section_L1.npz'
        self.output_beam_file = self.particle_dir + 'section_BC1.npz'
        self.tws_file = self.tws_dir + "tws_section_BC1.npz"

        #if "suffix" in kwargs:
        #    filename, file_extension = os.path.splitext(self.input_beam_file)
        #    self.input_beam_file = filename + str(kwargs["suffix"]) + file_extension
        #    print("SECTION B1: ", self.input_beam_file)
        #    filename, file_extension = os.path.splitext(self.output_beam_file)
        #    self.output_beam_file = filename + str(kwargs["suffix"]) + file_extension
        #    filename, file_extension = os.path.splitext(self.tws_file)
        #    self.tws_file = filename + str(kwargs["suffix"]) + file_extension

        acc2_stop = l1.stlat_182_b1
        bc1_stop = l1.tora_203_b1
        # init tracking lattice
        self.lattice = MagneticLattice(l1.cell, start=acc2_stop, stop=bc1_stop, method=self.method)

        # init physics processes

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
        sc.random_mesh = bRandomMesh

        match_bc1 = acc2_stop
        self.add_physics_process(csr, start=match_bc1, stop=bc1_stop)
        #self.add_physics_process(sc, start=match_bc1, stop=bc1_stop)
        self.dipoles = [l1.bb_182_b1, l1.bb_191_b1, l1.bb_193_b1, l1.bb_202_b1]
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

        #if "suffix" in kwargs:
        #    filename, file_extension = os.path.splitext(self.input_beam_file)
        #    suff = str(kwargs["suffix"])
        #    indx = suff.find("_chirpL2_")
        #    input_suff = suff[:indx]
        #    self.input_beam_file = filename + input_suff + file_extension
        #    print("SECTION L2: ", self.input_beam_file)
        #    filename, file_extension = os.path.splitext(self.output_beam_file)
        #    self.output_beam_file = filename + str(kwargs["suffix"]) + file_extension
        #    filename, file_extension = os.path.splitext(self.tws_file)
        #    self.tws_file = filename + str(kwargs["suffix"]) + file_extension



        bc1_stop = l1.tora_203_b1
        acc3t5_stop = l2.stlat_393_b2

        if "coupler_kick" in kwargs:
            self.coupler_kick = kwargs["coupler_kick"]
        else:
            self.coupler_kick = True

        # init tracking lattice
        self.lattice = MagneticLattice(l1.cell + l2.cell, start=bc1_stop, stop=acc3t5_stop, method=self.method)

        # init physics processes
        smooth = SmoothBeam()
        smooth.mslice = SmoothPar

        sc = SpaceCharge()
        sc.step = 100
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bRandomMesh

        wake = Wake()
        wake.wake_table = WakeTable(root_dir + 'accelerator/wakes/RF/mod_TESLA_MODULE_WAKE_TAYLOR.dat')
        wake.factor = 4 * 3
        wake.step = 200
        wake_add = Wake()
        wake_add.wake_table = WakeTable(root_dir + 'accelerator/wakes/mod_wake_0179.810_0370.840_MONO.dat')
        wake_add.factor = 1
        self.add_physics_process(smooth, start=bc1_stop, stop=bc1_stop)
        self.add_physics_process(sc, start=bc1_stop, stop=acc3t5_stop)
        self.add_physics_process(wake, start=l2.c_a3_1_1_l2, stop=l2.c_a5_4_8_l2)
        self.add_physics_process(wake_add, start=acc3t5_stop, stop=acc3t5_stop)


class BC2(SectionTrack):
    
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'BC2'
        self.dipoles = [l2.bb_393_b2, l2.bb_402_b2, l2.bb_404_b2, l2.bb_413_b2]
        self.dipole_len = 0.5
        self.bc_gap = 8.5

        self.unit_step = 0.02

        self.input_beam_file = self.particle_dir + 'section_L2.npz'
        self.output_beam_file = self.particle_dir + 'section_BC2.npz'
        self.tws_file = self.tws_dir + "tws_section_BC2.npz"

        #if "suffix" in kwargs:
        #    filename, file_extension = os.path.splitext(self.input_beam_file)
        #
        #    self.input_beam_file = filename + str(kwargs["suffix"]) + file_extension
        #    print("SECTION B2: ", self.input_beam_file)
        #    filename, file_extension = os.path.splitext(self.output_beam_file)
        #    self.output_beam_file = filename + str(kwargs["suffix"]) + file_extension
        #    filename, file_extension = os.path.splitext(self.tws_file)
        #    self.tws_file = filename + str(kwargs["suffix"]) + file_extension

        acc3t5_stop = l2.stlat_393_b2
        bc2_stop = l2.tora_415_b2
        # init tracking lattice
        self.lattice = MagneticLattice(l2.cell, start=acc3t5_stop, stop=bc2_stop, method=self.method)

        # init physics processes

        csr = CSR()
        csr.step = 1
        csr.n_bin = CSRBin
        csr.sigma_min = Sig_Z[2]*0.1
        csr.traj_step = 0.0005
        csr.apply_step = 0.005

        sc = SpaceCharge()
        sc.step = 50
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bRandomMesh


        self.add_physics_process(csr, start=acc3t5_stop, stop=bc2_stop)
        #self.add_physics_process(sc, start=acc3t5_stop, stop=bc2_stop)


class L3(SectionTrack):
    
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'L3'
        self.unit_step = 5.0


        self.input_beam_file = self.particle_dir + 'section_BC2.npz'
        self.output_beam_file = self.particle_dir + 'section_L3.npz'
        self.tws_file = self.tws_dir + "tws_section_L3.npz"

        bc2_stop = l2.tora_415_b2
        acc6t26_stop = cl.match_1673_cl
        # init tracking lattice
        self.lattice = MagneticLattice(l2.cell + l3.cell + cl.cell, start=bc2_stop, stop=acc6t26_stop, method=self.method)
        #self.cav_list = [".A23.", ".A22.", ".A21.", ".A20.", ".A19.", ".A18.", ".A17.", ".A16."]
        #for elem in self.lattice.sequence:
        #    if elem.__class__ == Cavity:
        #        for cav_num in self.cav_list:
        #            if cav_num in elem.id:
        #                print(elem.id)
        #                elem.v = 0.
        #self.lattice.update_transfer_maps()

        # init physics processes
        smooth = SmoothBeam()
        smooth.mslice = SmoothPar

        sc = SpaceCharge()
        sc.step = 1
        sc.nmesh_xyz = SCmesh
        sc.random_mesh = bRandomMesh

        wake = Wake()
        wake.wake_table = WakeTable(root_dir + 'accelerator/wakes/RF/mod_TESLA_MODULE_WAKE_TAYLOR.dat')
        wake.factor = 4 * 21
        wake.step = 2
        wake_add = Wake()
        wake_add.wake_table = WakeTable(root_dir + 'accelerator/wakes/mod_wake_0391.350_1629.700_MONO.dat')
        wake_add.factor = 1

        app = PhaseSpaceAperture()
        app.taumin = -5
        app.taumaxmax = 4

        self.add_physics_process(app, start=bc2_stop, stop=bc2_stop)
        self.add_physics_process(smooth, start=bc2_stop, stop=bc2_stop)
        self.add_physics_process(wake, start=l3.c_a6_1_1_l3,stop=l3.c_a25_4_8_l3)
        self.add_physics_process(sc, start=bc2_stop, stop=acc6t26_stop)
        self.add_physics_process(wake_add, start=acc6t26_stop, stop=acc6t26_stop)


class CL1(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'CL1'
        self.unit_step = 0.2


        self.input_beam_file = self.particle_dir + 'section_L3.npz'
        self.output_beam_file = self.particle_dir + 'section_CL1.npz'
        self.tws_file = self.tws_dir + "tws_section_CL1.npz"

        acc6t26_stop = cl.match_1673_cl
        collimator1_stop = cl.bpma_1746_cl
        # init tracking lattice
        self.lattice = MagneticLattice(cl.cell, start=acc6t26_stop,stop=collimator1_stop, method=self.method)

        # init physics processes

        sc = SpaceCharge()
        sc.step = 10
        sc.nmesh_xyz = SCmesh
        sc.low_order_kick = False
        sc.random_mesh = bRandomMesh

        csr = CSR()
        csr.traj_step = 0.0005
        csr.apply_step = 0.005
        csr.n_bin = 300
        csr.sigma_min = Sig_Z[3]*0.1

        self.add_physics_process(csr, start=acc6t26_stop, stop=collimator1_stop)
        self.add_physics_process(sc, start=acc6t26_stop, stop=collimator1_stop)


class CL2(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'CL2'
        self.unit_step = 1


        self.input_beam_file = self.particle_dir + 'section_CL1.npz'
        self.output_beam_file = self.particle_dir + 'section_CL2.npz'
        self.tws_file = self.tws_dir + "tws_section_CL2.npz"

        collimator1_stop = cl.bpma_1746_cl
        collimator2_stop = cl.bpma_1783_cl
        # init tracking lattice
        self.lattice = MagneticLattice(cl.cell, start=collimator1_stop, stop=collimator2_stop, method=self.method)

        # init physics processes

        sc = SpaceCharge()
        sc.step = 1
        sc.nmesh_xyz = [31, 31, 31]
        sc.low_order_kick = False
        self.add_physics_process(sc, start=collimator1_stop, stop=collimator2_stop)


class CL3(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'CL3'
        self.unit_step = 0.2


        self.input_beam_file = self.particle_dir + 'section_CL2.npz'
        self.output_beam_file = self.particle_dir + 'section_CL3.npz'
        self.tws_file = self.tws_dir + "tws_section_CL3.npz"

        if "suffix" in kwargs:
            filename, file_extension = os.path.splitext(self.input_beam_file)
            self.input_beam_file = filename + str(kwargs["suffix"]) + file_extension
            filename, file_extension = os.path.splitext(self.output_beam_file)
            self.output_beam_file = filename + str(kwargs["suffix"]) + file_extension
            filename, file_extension = os.path.splitext(self.tws_file)
            self.tws_file = filename + str(kwargs["suffix"]) + file_extension

        collimator2_stop = cl.bpma_1783_cl
        collimator3_stop = cl.bpma_1853_cl
        # init tracking lattice
        self.lattice = MagneticLattice(cl.cell, start=collimator2_stop, stop=collimator3_stop, method=self.method)

        # init physics processes

        sc = SpaceCharge()
        sc.step = 10
        sc.nmesh_xyz = [31, 31, 31]
        sc.low_order_kick = False

        csr = CSR()
        csr.traj_step = 0.0005
        csr.apply_step = 0.005
        csr.n_bin = 300
        csr.sigma_min = Sig_Z[3]*0.1

        wake_add = Wake()
        wake_add.wake_table = WakeTable('accelerator/wakes/mod_wake_1629.700_1831.200_MONO.dat')
        wake_add.factor = 1

        self.add_physics_process(csr, start=collimator2_stop, stop=collimator3_stop)
        self.add_physics_process(sc, start=collimator2_stop, stop=collimator3_stop)
        self.add_physics_process(wake_add, start=collimator3_stop, stop=collimator3_stop)


class STN10(SectionTrack):
    def __init__(self, data_dir):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'ST10'
        self.unit_step = 10

        self.input_beam_file = self.particle_dir + 'section_CL3.npz'
        self.output_beam_file = self.particle_dir + 'section_STN10.npz'
        self.tws_file = self.tws_dir + "tws_section_STN10.npz"

        collimator3_stop = cl.bpma_1853_cl
        stN10_stop = sase1.bpme_2235_t2
        # init tracking lattice
        self.lattice = MagneticLattice(cl.cell + tl34.cell + sase1.cell, start=collimator3_stop, stop=stN10_stop, method=self.method)

        # init physics processes

        sc = SpaceCharge()
        sc.step = 1
        sc.nmesh_xyz = [31, 31, 31]
        sc.low_order_kick = False

        wake_add = Wake()
        wake_add.wake_table = WakeTable('accelerator/wakes/mod_wake_1831.200_2035.190_MONO.dat')
        wake_add.factor = 1
        wake_add1 = Wake()
        wake_add1.wake_table = WakeTable('accelerator/wakes/mod_wake_2035.190_2213.000_MONO.dat')
        wake_add1.factor = 1

        self.add_physics_process(sc, start=collimator3_stop, stop=stN10_stop)
        self.add_physics_process(wake_add, start=collimator3_stop, stop=collimator3_stop)
        self.add_physics_process(wake_add1, start=stN10_stop, stop=stN10_stop)


class SASE1(SectionTrack):
    def __init__(self, data_dir):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'SASE1'
        self.unit_step = 5

        self.input_beam_file = self.particle_dir + 'section_STN10.npz'
        self.output_beam_file = self.particle_dir + 'section_SASE1.npz'
        self.tws_file = self.tws_dir + "tws_section_SASE1.npz"
        # last element sase1 - stsec_2461_t4
        stN10_stop = sase1.bpme_2235_t2
        sase1_stop = sase1.stsec_2461_t4
        # init tracking lattice
        self.lattice = MagneticLattice(sase1.cell, start=stN10_stop, stop=sase1_stop, method=self.method)

        # init physics processes
        wake = Wake()
        wake.wake_table = WakeTable('accelerator/wakes/Undulator/wake_undulator_OCELOT.txt')
        wake.step = 15
        wake.w_sampling = 500
        sc = SpaceCharge()
        sc.step = 1
        sc.nmesh_xyz = [31, 31, 31]
        sc.low_order_kick = False
        self.add_physics_process(wake, start=sase1.match_2247_sa1,stop=sase1_stop)
        self.add_physics_process(sc, start=stN10_stop, stop=sase1_stop)


class T4(SectionTrack):
    def __init__(self, data_dir):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'T4'
        self.unit_step = 0.2

        self.input_beam_file = self.particle_dir + 'section_SASE1.npz'
        self.output_beam_file = self.particle_dir + 'section_T4.npz'
        self.tws_file = self.tws_dir + "tws_section_T4.npz"
        # last element sase1 - stsec_2461_t4
        sase1_stop = sase1.stsec_2461_t4
        t4_stop = t4.ensub_2800_t4
        csr_start = t4.t4_start_csr
        csr_stop = t4.bpma_2606_t4
        # init tracking lattice
        self.lattice = MagneticLattice(sase1.cell + t4.cell, start=sase1_stop, stop=t4_stop, method=self.method)

        # init physics processes

        sc = SpaceCharge()
        sc.step = 25
        sc.nmesh_xyz = [31, 31, 31]

        csr = CSR()
        csr.traj_step = 0.0005
        csr.apply_step = 0.005
        csr.n_bin = 300
        csr.sigma_min = Sig_Z[3]*0.1

        sc2 = SpaceCharge()
        sc2.step = 25
        sc2.nmesh_xyz = [31, 31, 31]


        # creation of wake object with parameters
        wake = Wake()
        #wake.wake_table = WakeTable('accelerator/wakes/wake_hor_1m_500mkm.txt')
        wake.wake_table = WakeTable('accelerator/wakes/Dechirper/wake_hor_axis_500um.txt')
        # w_sampling - defines the number of the equidistant sampling points for the one-dimensional
        # wake coefficients in the Taylor expansion of the 3D wake function.
        wake.w_sampling = 500
        wake.factor = 1
        wake.step = 1  # step in Navigator.unit_step, dz = Navigator.unit_step * wake.step [m]


        # creation of wake object with parameters
        wake_vert = Wake()
        wake_vert.factor = 1
        #wake_vert.wake_table = WakeTable('accelerator/wakes/wake_vert_1m_500mkm.txt')
        wake_vert.wake_table = WakeTable('accelerator/wakes/Dechirper/wake_vert_axis_500um.txt')
        wake_vert.w_sampling = 500
        wake_vert.step = 1  # step in Navigator.unit_step, dz = Navigator.unit_step * wake.step [m]




        self.add_physics_process(wake, start=t4.wake_start, stop=t4.m_tds)

        svb4 = SaveBeam(filename=self.particle_dir + "before_structure.npz")
        self.add_physics_process(svb4, start=t4.wake_start, stop=t4.wake_start)

        self.add_physics_process(wake_vert, start=t4.m_tds, stop=t4.wake_stop)


        svb3 = SaveBeam(filename=self.particle_dir + "after_structure.npz")
        self.add_physics_process(svb3, start=t4.wake_stop, stop=t4.wake_stop)

        svb1 = SaveBeam(filename=self.particle_dir + "screen1.npz")
        self.add_physics_process(svb1, start=t4.m_img1, stop=t4.m_img1)

        svb2 = SaveBeam(filename=self.particle_dir + "screen2.npz")
        self.add_physics_process(svb2, start=t4.m_img2, stop=t4.m_img2)

        #self.add_physics_process(sc, start=sase1_stop, stop=csr_start)
        self.add_physics_process(sc, start=sase1_stop, stop=csr_start)
        self.add_physics_process(csr, start=csr_start, stop=csr_stop)
        self.add_physics_process(sc2, start=csr_stop, stop=t4.ensub_2800_t4)

        sc_in_bend = SpaceCharge()
        sc_in_bend.step = 25
        sc_in_bend.nmesh_xyz = [31, 31, 31]
        #self.add_physics_process(sc_in_bend, start=csr_start, stop=csr_stop)


class SASE3(SectionTrack):
    def __init__(self, data_dir):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'SASE3'
        self.unit_step = 1

        self.input_beam_file = self.particle_dir + 'section_T4.npz'
        self.output_beam_file = self.particle_dir + 'section_SASE3.npz'
        self.tws_file = self.tws_dir + "tws_section_SASE3.npz"

        start = sase3.ensec_2800_t4
        stop = sase3.ensec_2940_sa3
        # init tracking lattice
        self.lattice = MagneticLattice(sase3.cell, start=start, stop=stop, method=self.method)

        # init physics processes

        sc = SpaceCharge()
        sc.step = 10
        sc.nmesh_xyz = [31, 31, 31]
        self.add_physics_process(sc, start=start, stop=stop)


class T4D(SectionTrack):
    def __init__(self, data_dir):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'SASE3'
        self.unit_step = 1

        self.input_beam_file = self.particle_dir + 'section_SASE3.npz'
        self.output_beam_file = self.particle_dir + 'section_T4D.npz'
        self.tws_file = self.tws_dir + "tws_section_tT4D.npz"

        start = t4d.stsec_2940_t4d
        stop = t4d.ensec_3106_t4d
        # init tracking lattice
        self.lattice = MagneticLattice(t4d.cell, start=start, stop=stop, method=self.method)

        # init physics processes

        sc = SpaceCharge()
        sc.step = 10
        sc.nmesh_xyz = [31, 31, 31]
        self.add_physics_process(sc, start=start, stop=stop)

        csr = CSR()
        csr.traj_step = 0.0005
        csr.apply_step = 0.005
        csr.n_bin = 300
        csr.sigma_min = Sig_Z[3]*0.1

        self.add_physics_process(csr, start=t4d.tora_3065_t4d, stop=t4d.qk_3090_t4d)


class T4_short(SectionTrack):
    def __init__(self, data_dir):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'T4'
        self.unit_step = 1
        self.calc_tws = False

        self.input_beam_file = self.particle_dir + 'before_structure.npz'
        self.output_beam_file = self.particle_dir + 'section_T4.npz'
        self.tws_file = self.tws_dir + "tws_section_T4.npz"
        # last element sase1 - stsec_2461_t4
        sase1_stop = t4.wake_start# sase1.stsec_2461_t4
        t4_stop = t4.m_img1 #t4.ensub_2800_t4
        csr_start = t4.t4_start_csr
        csr_stop = t4.bpma_2606_t4
        # init tracking lattice
        self.lattice = MagneticLattice(sase1.cell + t4.cell, start=sase1_stop, stop=t4_stop, method=self.method)

        # init physics processes

        sc = SpaceCharge()
        sc.step = 25
        sc.nmesh_xyz = [31, 31, 31]

        csr = CSR()
        csr.traj_step = 0.0005
        csr.apply_step = 0.005
        csr.n_bin = 300
        csr.sigma_min = Sig_Z[3]*0.1

        sc2 = SpaceCharge()
        sc2.step = 25
        sc2.nmesh_xyz = [31, 31, 31]


        # creation of wake object with parameters
        wake = Wake()
        wake.wake_table = WakeTable('accelerator/wakes/tt.txt')

        # w_sampling - defines the number of the equidistant sampling points for the one-dimensional
        # wake coefficients in the Taylor expansion of the 3D wake function.
        wake.w_sampling = 500
        wake.factor = 1
        wake.step = 1  # step in Navigator.unit_step, dz = Navigator.unit_step * wake.step [m]


        # creation of wake object with parameters
        wake_vert = Wake()
        wake_vert.factor = 1
        wake_vert.wake_table = WakeTable('accelerator/wakes/tt.txt')
        wake_vert.w_sampling = 500
        wake_vert.step = 1  # step in Navigator.unit_step, dz = Navigator.unit_step * wake.step [m]


        #svb1 = SaveBeam(filename=self.particle_dir + "screen1.npz")

        #self.add_physics_process(svb1, start=t4.m_img1, stop=t4.m_img1)

        #svb2 = SaveBeam(filename=self.particle_dir + "screen2.npz")
        svb3 = SaveBeam(filename=self.particle_dir + "after_structure.npz")
        #svb4 = SaveBeam(filename=self.particle_dir + "before_structure.npz")
        #self.add_physics_process(svb2, start=t4.m_img2, stop=t4.m_img2)

        self.add_physics_process(wake_vert, start=t4.wake_start, stop=t4.m_tds)
        #self.add_physics_process(wake, start=t4.m_tds, stop=t4.wake_stop)

        #self.add_physics_process(svb3, start=t4.wake_stop, stop=t4.wake_stop)
        #self.add_physics_process(svb4, start=t4.wake_start, stop=t4.wake_start)

        #self.add_physics_process(sc, start=sase1_stop, stop=csr_start)
        #self.add_physics_process(sc, start=sase1_stop, stop=csr_start)
        #self.add_physics_process(csr, start=csr_start, stop=csr_stop)
        #self.add_physics_process(sc2, start=csr_stop, stop=t4.ensub_2800_t4)

        sc_in_bend = SpaceCharge()
        sc_in_bend.step = 25
        sc_in_bend.nmesh_xyz = [31, 31, 31]
        #self.add_physics_process(sc_in_bend, start=csr_start, stop=csr_stop)

################  SASE2 branch ####################################################


class T1(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)

        # setting parameters
        self.lattice_name = 'T1'
        self.unit_step = 0.2

        self.input_beam_file = self.particle_dir + 'section_CL3.npz'
        self.output_beam_file = self.particle_dir + 'section_T1.npz'
        self.tws_file = self.tws_dir + "tws_section_T1.npz"

        collimator3_stop = cl.bpma_1853_cl
        t1_stop = t1.ensec_2197_t1
        # init tracking lattice
        method = MethodTM()
        method.global_method = SecondTM
        method.params[Octupole] = KickTM
        method.params["nkick"] = 5
        self.lattice = MagneticLattice(cl.cell + tl34_sa2.cell + t1.cell, start=collimator3_stop, stop=t1_stop,
                                       method={"global": SecondTM, Octupole: KickTM, "nkick": 5})

        # init physics processes
        csr = CSR()
        csr.rk_traj = True
        csr.energy = 14
        csr.traj_step = 0.0005
        csr.apply_step = 0.001
        csr.n_bin = 400
        csr.sigma_min = Sig_Z[3] * 0.1
        #csr.rk_traj=True
        #csr.energy = 17.5

        csr2 = CSR()
        csr2.traj_step = 0.0005
        csr2.apply_step = 0.001
        csr2.n_bin = 400
        csr2.sigma_min = Sig_Z[3] * 0.1

        csr3 = CSR()
        csr3.traj_step = 0.0005
        csr3.apply_step = 0.001
        csr3.n_bin = 400
        csr3.sigma_min = Sig_Z[3] * 0.1

        wake_add = Wake()
        wake_add.wake_table = WakeTable('accelerator/wakes/mod_wake_1831.200_2035.190_MONO.dat')
        wake_add.factor = 1
        wake_add1 = Wake()
        wake_add1.wake_table = WakeTable('accelerator/wakes/mod_wake_2035.190_2213.000_MONO.dat')
        wake_add1.factor = 1

        self.add_physics_process(wake_add, start=collimator3_stop, stop=collimator3_stop)
        self.add_physics_process(wake_add1, start=t1_stop, stop=t1_stop)
        self.add_physics_process(csr, start=tl34_sa2.chy_1997_tl, stop=t1.cfx_2098_t1)
        #self.add_physics_process(csr, start=tl34_sa2.chy_1997_tl, stop=t1.before_XYQuad_sa2)
        #self.add_physics_process(csr2, start=t1.after_XYQuad_sa2, stop=t1.bend1_stop_sa2)
        #self.add_physics_process(csr3, start=t1.bend1_stop_sa2, stop=t1.bend_stop_sa2)


class SASE2(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'SASE2'
        self.unit_step = 2
        self.input_beam_file = self.particle_dir + 'section_T1.npz'
        self.output_beam_file = self.particle_dir + 'section_SASE2.npz'
        self.tws_file = self.tws_dir + "tws_section_SASE2.npz"

        sase2_start = t1.ensec_2197_t1
        sase2_stop = sase2.ensec_2423_sa2

        self.lattice = MagneticLattice(t1.cell + sase2.cell, start=sase2_start, stop=sase2_stop,
                                           method=self.method)
        # init physics processes
        wake = Wake()
        wake.wake_table = WakeTable('accelerator/wakes/Undulator/wake_undulator_OCELOT.txt')
        wake.step = 10
        wake.w_sampling = 1000
        wake.factor = 35*6.1
        sc = SpaceCharge()
        sc.step = 1
        sc.nmesh_xyz = [63, 63, 63]

        sre = SpontanRadEffects()
        sre.K = 3.9
        sre.lperiod = 0.04
        sre.filling_coeff=5/6.1

        self.add_physics_process(wake, start=sase2_stop, stop=sase2_stop)
        self.add_physics_process(sc, start=sase2_start, stop=sase2_stop)
        #self.add_physics_process(sre, start=sase2_start, stop=sase2_stop)


class T3(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'T3'
        self.unit_step = 10
        self.input_beam_file = self.particle_dir + 'section_SASE2.npz'
        self.output_beam_file = self.particle_dir + 'section_T3.npz'
        self.tws_file = self.tws_dir + "tws_section_T3.npz"
        sase2_stop = sase2.ensec_2423_sa2
        t3_stop = t3.ensec_2743_un1
        self.lattice = MagneticLattice(sase2.cell + t3.cell, start=sase2_stop, stop=t3_stop,
                                           method=self.method)

        csr = CSR()
        csr.traj_step = 0.0005
        csr.apply_step = 0.001
        csr.n_bin = 400
        csr.sigma_min = Sig_Z[3] * 0.1

        sc = SpaceCharge()
        sc.step = 1
        sc.nmesh_xyz = [63, 63, 63]

        sc2 = SpaceCharge()
        sc2.step = 1
        sc2.nmesh_xyz = [63, 63, 63]

        self.add_physics_process(csr, t3.csr_start, t3.chy_2569_t3)

        self.add_physics_process(sc, sase2_stop, t3.csr_start)
        self.add_physics_process(sc2, t3.csr_start, t3.ensec_2743_un1)


class T3_chirper(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'T3_chirper'
        self.unit_step = 0.5
        self.input_beam_file = self.particle_dir + 'section_SASE2.npz'
        self.output_beam_file = self.particle_dir + 'section_T3.npz'
        self.tws_file = self.tws_dir + "tws_section_T3.npz"
        sase2_stop = sase2.ensec_2423_sa2
        #t3_stop = t3.ensec_2743_un1
        t3_stop = t3.chy_2569_t3
        self.lattice = MagneticLattice(sase2.cell + t3.cell, start=sase2_stop, stop=t3_stop,
                                           method=self.method)

        csr = CSR()
        csr.traj_step = 0.0005
        csr.apply_step = 0.001
        csr.n_bin = 400
        csr.sigma_min = Sig_Z[3] * 0.1
        csr.step = 2

        sc = SpaceCharge()
        sc.step = 10
        sc.nmesh_xyz = [63, 63, 63]

        sc2 = SpaceCharge()
        sc2.step = 10
        sc2.nmesh_xyz = [63, 63, 63]

        self.add_physics_process(csr, t3.csr_start, t3.chy_2569_t3)

        self.add_physics_process(sc, sase2_stop, t3.csr_start)
        #self.add_physics_process(sc2, t3.csr_start, t3.ensec_2743_un1)

        # additional elements

        svb = SaveBeam(filename=self.particle_dir + "screen.npz")
        self.add_physics_process(svb, start=t3.otrb_2560_t3, stop=t3.otrb_2560_t3)

        #svb_scr2 = SaveBeam(filename=self.particle_dir + "screen2.npz")
        #self.add_physics_process(svb_scr2, start=t3.screen2, stop=t3.screen2)

        svb2 = SaveBeam(filename=self.particle_dir + "before_ws.npz")
        self.add_physics_process(svb2, start=t3.ws_start, stop=t3.ws_start)

        svb3 = SaveBeam(filename=self.particle_dir + "after_ws.npz")
        self.add_physics_process(svb3, start=t3.ws_stop, stop=t3.ws_stop)

        svb4 = SaveBeam(filename=self.particle_dir + "center_ws.npz")
        self.add_physics_process(svb4, start=t3.ws_center, stop=t3.ws_center)

        wk_tv_kick = WakeTableDechirperOffAxis(b=700 * 1e-6,  # distance from the plate in [m]
                                               a=0.01,  # half gap between plates in [m]
                                               width=0.02,  # width of the corrugated structure in [m]
                                               t=0.25 * 1e-3,  # longitudinal gap in [m]
                                               p=0.5 * 1e-3,  # period of corrugation in [m]
                                               length=5.,  # length of the corrugated structure in [m]
                                               sigma=42e-6,  # characteristic (rms) longitudinal beam size in [m]
                                               orient="horz")  # "horz" or "vert" plate orientation

        ws = Wake()
        # w_sampling - defines the number of the equidistant sampling points for the one-dimensional
        # wake coefficients in the Taylor expansion of the 3D wake function.
        ws.w_sampling = 500
        ws.wake_table = wk_tv_kick
        ws.step = 1 # step in Navigator.unit_step, dz = Navigator.unit_step * wake.step [m]
        self.add_physics_process(ws, start=t3.ws_start, stop=t3.ws_stop)


class T5(SectionTrack):
    def __init__(self, data_dir, *args, **kwargs):
        super().__init__(data_dir)
        # setting parameters
        self.lattice_name = 'T5'
        self.unit_step = 10
        self.input_beam_file = self.particle_dir + 'section_T3.npz'
        self.output_beam_file = self.particle_dir + 'section_T5.npz'
        self.tws_file = self.tws_dir + "tws_section_T5.npz"

        self.lattice = MagneticLattice(t5.cell, start=t5.stsec_2743_t5, stop=t5.stsec_3039_t5d,
                                           method=self.method)
