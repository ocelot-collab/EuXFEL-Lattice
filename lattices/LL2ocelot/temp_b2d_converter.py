from ocelot.adaptors.longlist2ocelot import *

folder = "C:/Users/veglia/Desktop/EuXFEL-Lattice/lattices/longlist_2024_07_04/"
#folder = "/Users/tomins/Nextcloud/DESY/repository/EuXFEL-Lattice/lattices/longlist_2024_07_04/"

# b2d START ****************
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR","OTRA","OTRC","OTRE","OTRD","OTRL","OTRBW","OTRB","OTRS","OTRO"]
b2d_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=4707, pos_stop=4739, sbend_l_corr=False)

lattice = MagneticLattice(b2d_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity, Monitor, Marker],
       remaining_elems=['STSEC.466.B2D','ENSEC.480.B2D'], init_energy=2.4)

tws = Twiss()
tws.beta_x  = 29.41686175122868
tws.beta_y  = 5.144745537053657
tws.alpha_x = 2.626251558631553
tws.alpha_y = -1.253808202141189
tws.E = 2.399999999680003
tws.s = 466.8192259999962

lattice.sequence = lattice.sequence[2:]
lattice.save_as_py_file(folder + "b2d.py", tws0=tws, power_supply=True)

# b2d END ********************