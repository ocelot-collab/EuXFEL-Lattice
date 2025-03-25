from ocelot.adaptors.longlist2ocelot import *

folder = "C:/Users/veglia/Desktop/EuXFEL-Lattice/lattices/longlist_2024_07_04/"
#folder = "/Users/tomins/Nextcloud/DESY/repository/EuXFEL-Lattice/lattices/longlist_2024_07_04/"

# b2d START ****************
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR","OTRA","OTRC","OTRE","OTRD","OTRL","OTRBW","OTRB","OTRS","OTRO"]
b2d_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=579, pos_stop=920, sbend_l_corr=False)

lattice = MagneticLattice(b2d_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity, Monitor, Marker],
       remaining_elems=['ENSUB.229.B1', 'STLAT.393.B2', 'MATCH.414.B2', 'TORA.415.B2', 'MATCH.428.B2','MATCH.446.B2', 'ENSUB.466.B2'], init_energy=0.7)

tws = Twiss()

tws.beta_x  = 7.865550253394325
tws.beta_y  = 8.698292442670796
tws.alpha_x = -1.0418290882386196
tws.alpha_y = -1.2234476587083056
tws.E = 0.7
tws.s = 229.3007540000002

lattice.sequence = lattice.sequence[2:]
lattice.save_as_py_file(folder + "l2.py", tws0=tws, power_supply=True)

# b2d END ********************