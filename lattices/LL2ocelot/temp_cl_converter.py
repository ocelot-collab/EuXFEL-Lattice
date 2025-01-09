from ocelot.adaptors.longlist2ocelot import *

folder = "C:/Users/veglia/Desktop/EuXFEL-Lattice/lattices/longlist_2024_07_04/"
#folder = "/Users/tomins/Nextcloud/DESY/repository/EuXFEL-Lattice/lattices/longlist_2024_07_04/"

# CL START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
t1_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=2095, pos_stop=2313, sbend_l_corr=False)

lattice = MagneticLattice(t1_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, Octupole, TDCavity],
       remaining_elems=['STSEC.1652.CL','MATCH.1673.CL','ENSEC.1854.CL'], init_energy=14)

tws = Twiss()
tws.beta_x  = 41.66496631816343
tws.beta_y  = 53.55111570484648
tws.alpha_x = -0.9889897612957868
tws.alpha_y = 2.004822139010063
tws.E = 14
tws.s = 1652.902800000028

lattice.sequence = lattice.sequence[2:]
lattice.save_as_py_file(folder + "cl.py", tws0=tws, power_supply=True)


