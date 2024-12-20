from ocelot.adaptors.longlist2ocelot import *

folder = "C:/Users/veglia/Desktop/EuXFEL-Lattice/lattices/longlist_2024_07_04/"
#folder = "/Users/tomins/Nextcloud/DESY/repository/EuXFEL-Lattice/lattices/longlist_2024_07_04/"

# TL2 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
tl2_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=2313, pos_stop=2427, sbend_l_corr=False)

lattice = MagneticLattice(tl2_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, Octupole, TDCavity],
       remaining_elems=['STSEC.1854.TL','ENSUB.1980.TL'], init_energy=14)

tws = Twiss()
tws.beta_x  = 0.5790415663071324
tws.beta_y  = 2.787247754647999
tws.alpha_x = -1.4029863567200784
tws.alpha_y = 0.16729234667447596
tws.E = 14
tws.s = 1854.412579000024

lattice.sequence = lattice.sequence[2:]
lattice.save_as_py_file(folder + "tl2.py", tws0=tws, power_supply=True)


