from ocelot.adaptors.longlist2ocelot import *

folder = "C:/Users/veglia/Desktop/EuXFEL-Lattice/lattices/longlist_2024_07_04/"
folder = "/Users/tomins/Nextcloud/DESY/repository/EuXFEL-Lattice/lattices/longlist_2024_07_04/"

# T1 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
t1_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=3619, pos_stop=3754, sbend_l_corr=False)

lattice = MagneticLattice(t1_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, Octupole, TDCavity],
       remaining_elems=['STSEC.2025.T1','ENSEC.2197.T1'], init_energy=14)

tws = Twiss()
tws.beta_x  = 10.776023018690426
tws.beta_y  = 39.48730762141566
tws.alpha_x = 0.6698245190372976
tws.alpha_y = -2.0320682898456615
tws.E = 14
tws.s = 2025.3865970000204

lattice.sequence = lattice.sequence[2:]
lattice.save_as_py_file(folder + "t1_tmp.py", tws0=tws, power_supply=True)


