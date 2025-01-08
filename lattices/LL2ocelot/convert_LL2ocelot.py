from ocelot.adaptors.longlist2ocelot import *

folder = "C:/Users/veglia/Desktop/EuXFEL-Lattice/lattices/longlist_2024_07_04/"
folder = "/Users/tomins/Nextcloud/DESY/repository/EuXFEL-Lattice/lattices/longlist_2024_07_04/"
# INJECTOR START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
i1_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=3, pos_stop=145, sbend_l_corr=False)
lattice = MagneticLattice(i1_cell)
lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid, Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['STSEC.23.I1', 'MATCH.37.I1', "STLAT.47.I1", 'MATCH.52.I1','MATCH.55.I1', 
                        'OTRC.55.I1', 'OTRC.56.I1', 'OTRC.58.I1', 'OTRC.59.I1', 'STSUB.62.I1'], init_energy=0.005)

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

#lattice.save_as_py_file(folder + "i1_tmp.py", tws0=tws, power_supply=True)

# INJECTOR END ********


# L1 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR", "CM"]
l1_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=145, pos_stop=579, sbend_l_corr=False)
lattice = MagneticLattice(l1_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['STSUB.62.I1', 'MATCH.73.I1', 'STLAT.73.I1', 'STLAT.96.I1', 'ENLAT.101.I1', 'MATCH.104.I1', 'MATCH.174.L1', 'STLAT.182.B1', 'MATCH.202.B1',
                        'TORA.203.B1',
                        'MATCH.207.B1', 'MATCH.218.B1', 'ENSUB.229.B1'], init_energy=0.13)

# for elem in lattice.sequence:
#     if elem.__class__ == Cavity:
#         elem.vx_up=(-5.6813e-05+1.0751e-05j)
#         elem.vy_up=(-4.1091e-05+5.739e-07j)
#         elem.vxx_up=(0.00099943-0.00081401j)
#         elem.vxy_up=(0.0034065-0.0004146j)
#         elem.vx_down=(-2.4014e-05+1.2492e-05j)
#         elem.vy_down=(3.6481e-05+7.9888e-06j)
#         elem.vxx_down=(-0.004057-0.0001369j)
#         elem.vxy_down=(0.0029243-1.2891e-05j)

tws = Twiss()
tws.beta_x  = 2.6096907242276925
tws.beta_y  = 7.150678422205259
tws.alpha_x = 0.22820424990918614
tws.alpha_y = -2.165836718254254
tws.s = 62.089004999999936
tws.E = 0.13
lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "l1.py", tws0=tws, power_supply=True)

# L1 END ********


# L2 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR", "CM"]
l2_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=579, pos_stop=920, sbend_l_corr=False)

lattice = MagneticLattice(l2_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSUB.229.B1', 'STLAT.393.B2', 'MATCH.414.B2', 'TORA.415.B2', 'MATCH.428.B2','MATCH.446.B2', 'ENSUB.466.B2'], init_energy=0.7)

# for elem in lattice.sequence:
#     if elem.__class__ == Cavity:
#         elem.vx_up=(-5.6813e-05+1.0751e-05j)
#         elem.vy_up=(-4.1091e-05+5.739e-07j)
#         elem.vxx_up=(0.00099943-0.00081401j)
#         elem.vxy_up=(0.0034065-0.0004146j)
#         elem.vx_down=(-2.4014e-05+1.2492e-05j)
#         elem.vy_down=(3.6481e-05+7.9888e-06j)
#         elem.vxx_down=(-0.004057-0.0001369j)
#         elem.vxy_down=(0.0029243-1.2891e-05j)

tws = Twiss()

tws.beta_x  = 7.865550253394325
tws.beta_y  = 8.698292442670796
tws.alpha_x = -1.0418290882386196
tws.alpha_y = -1.2234476587083056
tws.E = 0.7
tws.s = 229.3007540000002

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "l2.py", tws0=tws, power_supply=True)

# L2 END ********


# L3 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
l3_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=920, pos_stop=2095, sbend_l_corr=False)

lattice = MagneticLattice(l3_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSUB.466.B2','MATCH.525.L3','ENSEC.1652.L3'], init_energy=2.4)

# for elem in lattice.sequence:
#     if elem.__class__ == Cavity:
#         elem.vx_up=(-5.6813e-05+1.0751e-05j)
#         elem.vy_up=(-4.1091e-05+5.739e-07j)
#         elem.vxx_up=(0.00099943-0.00081401j)
#         elem.vxy_up=(0.0034065-0.0004146j)
#         elem.vx_down=(-2.4014e-05+1.2492e-05j)
#         elem.vy_down=(3.6481e-05+7.9888e-06j)
#         elem.vxx_down=(-0.004057-0.0001369j)
#         elem.vxy_down=(0.0029243-1.2891e-05j)

tws = Twiss()
tws.beta_x  = 29.41686175122868
tws.beta_y  = 5.144745537053657
tws.alpha_x = 2.626251558631553
tws.alpha_y = -1.253808202141189
tws.E = 2.4
tws.s = 466.82

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "l3.py", tws0=tws, power_supply=True)

# L3 END *******************


# CL START *********************
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
cl_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=2095, pos_stop=2427, sbend_l_corr=False)

lattice = MagneticLattice(cl_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSEC.1652.L3', 'MATCH.1673.CL','ENSUB.1980.TL'], init_energy=14)

tws = Twiss()
tws.beta_x  = 41.66496631816343
tws.beta_y  = 53.55111570484648
tws.alpha_x = -0.9889897612957868
tws.alpha_y = 2.004822139010063
tws.E = 14
tws.s = 1652.902800000028

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "cl.py", tws0=tws, power_supply=True)

# CL END ***************************

# TLD START ************************
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
tld_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=4514, pos_stop=4656, sbend_l_corr=False)
# In the longlist Excel file the TLD section is way down the order
lattice = MagneticLattice(tld_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['STSEC.1980.TLD', 'OTRC.1995.TLD','ENSEC.2130.TLD'], init_energy=14)

tws = Twiss()
tws.beta_x  = 43.11647525647555
tws.beta_y  = 10.860573729512675
tws.alpha_x = -2.1790120506947406
tws.alpha_y = 0.6184659724795544
tws.E = 14
tws.s = 1980.3864730000207

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "tld.py", tws0=tws, power_supply=True)

# TLD END ***************************


# TL34 START ************************
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
tl34_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=2427, pos_stop=2458, sbend_l_corr=False)

lattice = MagneticLattice(tl34_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSUB.1980.TL', 'ENSUB.2025.TL'], init_energy=14)

tws = Twiss()
tws.beta_x  = 43.11647525647555
tws.beta_y  = 10.860573729512675
tws.alpha_x = -2.1790120506947406
tws.alpha_y = 0.6184659724795544
tws.E = 14
tws.s = 1980.3864730000207

lattice.sequence = lattice.sequence[2:]
lattice.save_as_py_file(folder + "tl34.py", tws0=tws, power_supply=True)
# TL34 END ********


# sase1 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
l3_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=2458, pos_stop=3069, sbend_l_corr=False)

lattice = MagneticLattice(l3_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSUB.2025.TL','MATCH.2248.SA1','ENSEC.2461.SA1' ], init_energy=14)

tws = Twiss()
tws.beta_x  = 10.776023018690426
tws.beta_y  = 39.48730762141566
tws.alpha_x = 0.6698245190372976
tws.alpha_y = -2.0320682898456615
tws.E = 14
tws.s = 2025.3865970000204

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "sase1.py", tws0=tws, power_supply=True)

# sase1 END ********

# T4 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
t4_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=3069, pos_stop=3191, sbend_l_corr=False)

lattice = MagneticLattice(t4_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSEC.2461.SA1', 'ENSEC.2800.T4'], init_energy=14)

tws = Twiss()
tws.beta_x  = 25.263665891080947
tws.beta_y  = 40.54159948158437
tws.alpha_x = -0.7944632639752688
tws.alpha_y = 1.26958806877402
tws.E = 14
tws.s = 2461.7178630000176

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "t4.py", tws0=tws, power_supply=True)

# T4 END ********

# sase3 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
#sase3_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=3191, pos_stop=3554, sbend_l_corr=False)
#lattice = MagneticLattice(sase3_cell)
#lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
#                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
#       remaining_elems=['ENSEC.2800.T4','MATCH.2813.SA3','ENSEC.2955.SA3'], init_energy=14)

tws = Twiss()
tws.beta_x  = 22.071972008019717
tws.beta_y  = 10.22271243325217
tws.alpha_x = 1.5225255474012378
tws.alpha_y = -0.7348186593318795
tws.E = 14
tws.s = 2801.0155910000135

#lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "sase3.py", tws0=tws, power_supply=True)

# sase3 END ********

# T4D START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
t4d_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=3539, pos_stop=3618, sbend_l_corr=False)

lattice = MagneticLattice(t4d_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSEC.2955.SA3','ENSEC.3106.T4D'], init_energy=14)

tws = Twiss()
tws.beta_x  = 9.429026330526568
tws.beta_y  = 22.189275259818615
tws.alpha_x = -0.6621363588705478
tws.alpha_y = 1.509023055887539
tws.E = 14
tws.s = 2956

#lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "t4d.py", tws0=tws, power_supply=True)

# T4D END ********


# TL34_sa2 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
t34_sa2_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=2427, pos_stop=2458, sbend_l_corr=False)

lattice = MagneticLattice(t34_sa2_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, Octupole, TDCavity],
       remaining_elems=['ENSUB.1980.TL', 'ENSUB.2025.TL'], init_energy=14)

tws = Twiss()
tws.beta_x  = 43.11647525647555
tws.beta_y  = 10.860573729512675
tws.alpha_x = -2.1790120506947406
tws.alpha_y = 0.6184659724795544
tws.E = 14
tws.s = 1980.3864730000207

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "tl34_sa2.py", tws0=tws, power_supply=True)
# TL34_sa2 END ********


# T1 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
t1_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=3635, pos_stop=3770, sbend_l_corr=False)

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
#lattice.save_as_py_file(folder + "t1.py", tws0=tws, power_supply=True)

# T1 END ********

# sase2 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
sase2_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=3770, pos_stop=4259, sbend_l_corr=False)

lattice = MagneticLattice(sase2_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSEC.2197.T1', 'MATCH.2197.SA2','ENSEC.2423.SA2' ], init_energy=14)

tws = Twiss()
tws.beta_x  = 53.015297404432516
tws.beta_y  = 79.56279633228925
tws.alpha_x = 0.8005655864098374
tws.alpha_y = 5.39236677329033
tws.E = 14
tws.s = 2198.0091950000196

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "sase2.py", tws0=tws, power_supply=True)

# sase2 END ********


# T3 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
t3_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=4259, pos_stop=4365, sbend_l_corr=False)
lattice = MagneticLattice(t3_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSEC.2423.SA2','ENSEC.2743.UN1'], init_energy=14)

tws = Twiss()
tws.beta_x  = 56.797212917921975
tws.beta_y  = 262.99048996645803
tws.alpha_x = -1.517388900059324
tws.alpha_y = -2.4145325077606694
tws.E = 14
tws.s = 2423.709195000019

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "t3.py", tws0=tws, power_supply=True)
# T3 END ********


# T5 START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
t5_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=4365, pos_stop=4454, sbend_l_corr=False)

lattice = MagneticLattice(t5_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSEC.2743.UN1','ENSEC.3039.UN2'], init_energy=14)

tws = Twiss()
tws.beta_x  = 45.844278111396584
tws.beta_y  = 42.542767032006005
tws.alpha_x = 1.201808970069004
tws.alpha_y = -1.1037998266496247
tws.E = 14
tws.s = 2743.9245999999944

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "t5.py", tws0=tws, power_supply=True)

# T5 END ************************


# T5d START *********************
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
t5_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=4439, pos_stop=4513, sbend_l_corr=False)

lattice = MagneticLattice(t5_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['ENSEC.3039.UN2', 'ENSEC.3189.T5D'], init_energy=14)

tws = Twiss()
tws.beta_x  = 38.45542292280062
tws.beta_y  = 49.754948691305444
tws.alpha_x = -1.0273576528473884
tws.alpha_y = 1.3083708330446713
tws.E = 14
tws.s = 3039.372919999988

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "t5d.py", tws0=tws, power_supply=True)

# T5d END ******************************


# i1d START ****************************
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
i1d_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=4668, pos_stop=4687, sbend_l_corr=False)

lattice = MagneticLattice(i1d_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['STSEC.62.I1D','OTRC.64.I1D','ENSEC.66.I1D'], init_energy=0.13)

tws = Twiss()
tws.beta_x  = 3.020685835329106
tws.beta_y  = 7.0413164056761035
tws.alpha_x = 0.23961060835472217
tws.alpha_y = -2.1828482259048667
tws.E = 0.12999999999999998
tws.s = 62.08900499999993

lattice.sequence = lattice.sequence[2:]
lattice.save_as_py_file(folder + "i1d.py", tws0=tws, power_supply=True)

# i1d END ********
exit()
# b1d START ********
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
b1d_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=4703, pos_stop=4722, sbend_l_corr=False)

lattice = MagneticLattice(b1d_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['STSEC.229.B1D','DUFLANGE.237.B1D','DUABSORB.237.B1D','ENSEC.237.B1D'], init_energy=0.7)

tws = Twiss()
tws.beta_x  = 7.865550253394325
tws.beta_y  = 8.698292442670796
tws.alpha_x = -1.0418290882386196
tws.alpha_y = -1.2234476587083056
tws.E = 0.7000000007706801
tws.s = 229.3007540000002

#lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "b1d.py", tws0=tws, power_supply=True)

# b1d END *******************


# b2d START ****************
SC = StructureConverter()
SC.types = ["HKIC", "VKIC", "MONI", "MARK", "INSTR"]
b2d_cell = SC.Longlist2Ocelot(folder + 'component_list_2024.07.04.xls', pos_start=4722, pos_stop=4755, sbend_l_corr=False)

lattice = MagneticLattice(b2d_cell)

lattice = merger(lattice, remaining_types=[SBend, RBend, Bend, Monitor, Quadrupole, Undulator, Solenoid,
                                           Hcor, Vcor, Sextupole, Cavity, TDCavity],
       remaining_elems=['STSEC.466.B2DS','ENSEC.480.B2D'], init_energy=2.4)

tws = Twiss()
tws.beta_x  = 29.41686175122868
tws.beta_y  = 5.144745537053657
tws.alpha_x = 2.626251558631553
tws.alpha_y = -1.253808202141189
tws.E = 2.399999999680003
tws.s = 466.8192259999962

lattice.sequence = lattice.sequence[2:]
#lattice.save_as_py_file(folder + "b2d.py", tws0=tws, power_supply=True)

# b2d END ********************