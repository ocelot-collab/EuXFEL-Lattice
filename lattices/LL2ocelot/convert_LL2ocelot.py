from ocelot.adaptors.longlist2ocelot import *

folder = "/Users/tomins/Nextcloud/DESY/repository/EuXFEL-Lattice/lattices/longlist_2024_07_04/"
# INJECTOR START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
i1_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=3, pos_stop=145, sbend_l_corr=False)
lattice = MagneticLattice(i1_cell)
lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid, Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['STSEC.23.I1', 'MATCH.37.I1', 'OTRC.55.I1', 'OTRC.56.I1', 'OTRC.58.I1', 'OTRC.59.I1', 'STSUB.62.I1'], init_energy=0.005)

# for elem in lattice.sequence:
#      if elem.__class__ == Undulator:
#          elem.Kx = 1.315
#     if elem.__class__ == Cavity:
#         if "A1" in elem.id:
#
#             elem.vx_up = (-5.6813e-05 + 1.0751e-05j)
#             elem.vy_up = (-4.1091e-05 + 5.739e-07j)
#             elem.vxx_up = (0.00099943 - 0.00081401j)
#             elem.vxy_up = (0.0034065 - 0.0004146j)
#             elem.vx_down = (-2.4014e-05 + 1.2492e-05j)
#             elem.vy_down = (3.6481e-05 + 7.9888e-06j)
#             elem.vxx_down = (-0.004057 - 0.0001369j)
#             elem.vxy_down = (0.0029243 - 1.2891e-05j)
#
#         if "AH1" in elem.id:
#             elem.vx_up=(-0.00057076-1.3166e-05j)
#             elem.vy_up=(-3.5079e-05+0.00012636j)
#             elem.vxx_up=(-0.026045-0.042918j)
#             elem.vxy_up=(0.0055553-0.023455j)
#             elem.vx_down=(-8.8766e-05-0.00024852j)
#             elem.vy_down=(2.9889e-05+0.00014486j)
#             elem.vxx_down=(-0.0050593-0.013491j)
#             elem.vxy_down=(0.0051488+0.024771j)

tws = Twiss()
tws.E = 0.005
tws.beta_x  = 55.7981
tws.beta_y  = 55.7981
tws.alpha_x = 18.1886
tws.alpha_y = 18.1886
tws.s = 23.2

#lattice.save_as_py_file(folder + "i1.py", tws0=tws, power_supply=True)


# INJECTOR END ********

# L1 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
i1_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=145, pos_stop=579, sbend_l_corr=False)

lattice = MagneticLattice(i1_cell)


lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['STSUB.62.I1', 'MATCH.174.L1', 'MATCH.202.B1', 'ENSUB.229.B1'], init_energy=0.13)


for elem in lattice.sequence:
    if elem.__class__ == Cavity:
        elem.vx_up=(-5.6813e-05+1.0751e-05j)
        elem.vy_up=(-4.1091e-05+5.739e-07j)
        elem.vxx_up=(0.00099943-0.00081401j)
        elem.vxy_up=(0.0034065-0.0004146j)
        elem.vx_down=(-2.4014e-05+1.2492e-05j)
        elem.vy_down=(3.6481e-05+7.9888e-06j)
        elem.vxx_down=(-0.004057-0.0001369j)
        elem.vxy_down=(0.0029243-1.2891e-05j)
tws = Twiss()
tws.beta_x  = 2.6096907242276925
tws.beta_y  = 7.150678422205259
tws.alpha_x = 0.22820424990918614
tws.alpha_y = -2.165836718254254
tws.s = 62.089004999999936
tws.E = 0.13
lattice.sequence = lattice.sequence[2:]
lattice.save_as_py_file(folder + "l1.py", tws0=tws, power_supply=True)

# L1 END ********

exit()

# T3 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR", "CM"]
t3_cell = SC.Longlist2Ocelot('component_list_2023.07.01.xls', pos_start=4192, pos_stop=4295, sbend_l_corr=False)

lattice = MagneticLattice(t3_cell)


lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=["STSEC.2423.T3", 'OTRC.2560.T3', 'VCCHIRP_S.2462.T3', 'VCCHIRP.2464.T3', 'VCCHIRP_S.2467.T3',
                        "BPMAMARK.2455.T3", "ENSEC.2743.UN1", 'TORA.2424.T3', 'TORA.2682.T3'], init_energy=14)



tws = Twiss()
tws.beta_x  = 26.108255539772447
tws.beta_y  = 37.7162592662484
tws.alpha_x = -0.8360736180096779
tws.alpha_y = 1.1812735424648375
tws.E = 14
lattice.sequence = lattice.sequence[1:]
lattice.save_as_py_file("t3.py", tws0=tws, power_supply=True)

# L1 END ********
