from ocelot.adaptors.longlist2ocelot import *

folder = "C:/Users/veglia/Desktop/EuXFEL-Lattice/lattices/longlist_2024_07_04/"
folder = "/Users/tomins/Nextcloud/DESY/repository/EuXFEL-Lattice/lattices/longlist_2024_07_04/"

# sase3 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
sase3_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=3190, pos_stop=3538, sbend_l_corr=False)
lattice = MagneticLattice(sase3_cell)
lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSEC.2800.T4','MATCH.2813.SA3','ENSEC.2955.SA3'], init_energy=14)

tws = Twiss()
tws.beta_x  = 22.6886
tws.beta_y  = 9.6311
tws.alpha_x = 1.5464
tws.alpha_y = -0.6632
tws.E = 14
tws.s = 2801.0155910000135

#lattice.sequence = lattice.sequence[2:]
lattice.save_as_py_file(folder + "sase3.py", tws0=tws, power_supply=True)

# sase3 END ********


# 3493 SA3	UE90	XTD4_003	CUSX.2942.SA3	CUSX.CELL24.SA3	MAGNET	HKIC	CUSX
# 3494 SA3	UE90	XTD4_003	CUSY.2942.SA3	CUSY.CELL24.SA3	MAGNET	HKIC	CUSY
# 3495 SA3	UE90	XTD4_003	QP.2941.SA3	QP.CELL24.SA3	PMAGNET	QUAD	QP
#
# 3508 SA3	UE90	XTD4_004	CUSX.2946.SA3	CUSX.CELL25.SA3	MAGNET	HKIC	CUSX
# 3509 SA3	UE90	XTD4_004	CUSY.2946.SA3	CUSY.CELL25.SA3	MAGNET	HKIC	CUSY
# 3510 SA3	UE90	XTD4_004	QP.2945.SA3	QP.CELL25.SA3	PMAGNET	QUAD	QP
#
# 3525 SA3	UE90	XTD4_004	CUSX.2949.SA3	CUSX.CELL26.SA3	MAGNET	HKIC	CUSX
# 3526 SA3	UE90	XTD4_004	CUSY.2949.SA3	CUSY.CELL26.SA3	MAGNET	HKIC	CUSY
# 3527 SA3	UE90	XTD4_004	QP.2948.SA3	QP.CELL26.SA3	PMAGNET	QUAD	QP
#
# 3540 SA3	UE90	XTD4_004	CUSX.2953.SA3	CUSX.CELL27.SA3	MAGNET	HKIC	CUSX
# 3541 SA3	UE90	XTD4_004	CUSY.2953.SA3	CUSY.CELL27.SA3	MAGNET	HKIC	CUSY
# 3542 SA3	UE90	XTD4_004	QP.2952.SA3	QP.CELL27.SA3	PMAGNET	QUAD	QP

# SA3	UE90	XTD4_004	QP.2954.SA3	QP.CELL27.SA3	PMAGNET	QUAD	QP
# SA3	UE90	XTD4_004	QP.2947.SA3	QP.CELL25.SA3	PMAGNET	QUAD	QP
# SA3	UE90	XTD4_003	QP.2943.SA3	QP.CELL24.SA3	PMAGNET	QUAD	QP
# SA3	UE90	XTD4_004	QP.2951.SA3	QP.CELL26.SA3	PMAGNET	QUAD	QP