from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 2.6096907242276925
tws0.beta_y = 7.150678422205259
tws0.alpha_x = 0.22820424990918614
tws0.alpha_y = -2.165836718254254
tws0.E = 0.13
tws0.s = 62.089004999999936

# Drifts
d_2 = Drift(l=0.5, eid='D_2')
d_3 = Drift(l=0.74, eid='D_3')
d_4 = Drift(l=0.08115, eid='D_4')
d_5 = Drift(l=0.13115, eid='D_5')
d_6 = Drift(l=1.45, eid='D_6')
d_7 = Drift(l=0.63115, eid='D_7')
d_8 = Drift(l=2.8623, eid='D_8')
d_9 = Drift(l=1.7623, eid='D_9')
d_10 = Drift(l=0.68115, eid='D_10')
d_11 = Drift(l=0.18115, eid='D_11')
d_13 = Drift(l=0.2, eid='D_13')
d_15 = Drift(l=0.182428, eid='D_15')
d_16 = Drift(l=5.1e-05, eid='D_16')
d_17 = Drift(l=0.135, eid='D_17')
d_18 = Drift(l=0.239432, eid='D_18')
d_19 = Drift(l=0.0751, eid='D_19')
d_21 = Drift(l=0.13494, eid='D_21')
d_22 = Drift(l=0.158616, eid='D_22')
d_23 = Drift(l=0.1325, eid='D_23')
d_24 = Drift(l=0.09865, eid='D_24')
d_25 = Drift(l=0.11615, eid='D_25')
d_26 = Drift(l=0.273615, eid='D_26')
d_30 = Drift(l=0.324432, eid='D_30')
d_31 = Drift(l=0.150051, eid='D_31')
d_33 = Drift(l=0.182429, eid='D_33')
d_39 = Drift(l=0.134939, eid='D_39')
d_44 = Drift(l=0.273616, eid='D_44')
d_48 = Drift(l=0.324431, eid='D_48')
d_49 = Drift(l=0.150052, eid='D_49')
d_52 = Drift(l=5.2e-05, eid='D_52')
d_54 = Drift(l=0.239431, eid='D_54')
d_76 = Drift(l=8e-06, eid='D_76')
d_77 = Drift(l=0.158608, eid='D_77')
d_80 = Drift(l=0.489766, eid='D_80')
d_84 = Drift(l=0.091932, eid='D_84')
id_30609505_ = Drift(l=1.08128, eid='ID_30609505_')
d_90 = Drift(l=0.09115, eid='D_90')
id_7554339_ = Drift(l=0.37715, eid='ID_7554339_')
d_93 = Drift(l=0.204, eid='D_93')
d_95 = Drift(l=0.38115, eid='D_95')
d_96 = Drift(l=0.100597, eid='D_96')
d_97 = Drift(l=1.008384, eid='D_97')
d_98 = Drift(l=0.000597, eid='D_98')
d_99 = Drift(l=0.865, eid='D_99')
id_79103439_ = Drift(l=0.635597, eid='ID_79103439_')
d_103 = Drift(l=1.007788, eid='D_103')
d_104 = Drift(l=0.000596, eid='D_104')
d_105 = Drift(l=0.1, eid='D_105')
d_106 = Drift(l=0.39115, eid='D_106')
id_14888141_ = Drift(l=0.346, eid='ID_14888141_')
d_110 = Drift(l=0.144, eid='D_110')
d_113 = Drift(l=0.56, eid='D_113')
d_116 = Drift(l=1.89, eid='D_116')
id_34013725_ = Drift(l=2.04, eid='ID_34013725_')
id_28166788_ = Drift(l=1.2650000000000001, eid='ID_28166788_')
d_131 = Drift(l=0.13965, eid='D_131')
id_50015017_ = Drift(l=1.5315, eid='ID_50015017_')
d_136 = Drift(l=0.14395, eid='D_136')
id_70254102_ = Drift(l=3.923801, eid='ID_70254102_')
d_140 = Drift(l=0.345899, eid='D_140')
d_141 = Drift(l=0.3459, eid='D_141')
d_143 = Drift(l=0.34589999999999743, eid='D_143')
d_146 = Drift(l=0.345901, eid='D_146')
d_147 = Drift(l=0.247499, eid='D_147')
d_148 = Drift(l=0.043201, eid='D_148')
d_149 = Drift(l=0.084999, eid='D_149')
id_82567243_ = Drift(l=0.679501, eid='ID_82567243_')
d_155 = Drift(l=0.3459000000000091, eid='D_155')
d_159 = Drift(l=0.2475, eid='D_159')
d_160 = Drift(l=0.0432, eid='D_160')
d_161 = Drift(l=0.085001, eid='D_161')
id_85517094_ = Drift(l=0.679499, eid='ID_85517094_')
d_167 = Drift(l=0.34590000000001164, eid='D_167')
d_172 = Drift(l=0.043199, eid='D_172')
d_173 = Drift(l=0.085, eid='D_173')
id_36296974_ = Drift(l=0.6795009999999999, eid='ID_36296974_')
id_70317273_ = Drift(l=5.501900000000001, eid='ID_70317273_')
d_191 = Drift(l=0.15215, eid='D_191')
d_192 = Drift(l=0.082149, eid='D_192')
id_78014327_ = Drift(l=1.215001, eid='ID_78014327_')
id_45736562_ = Drift(l=1.613, eid='ID_45736562_')
d_199 = Drift(l=0.15265, eid='D_199')
d_200 = Drift(l=0.131649, eid='D_200')
id_33800950_ = Drift(l=0.88165, eid='ID_33800950_')
d_204 = Drift(l=0.10165, eid='D_204')
id_17795282_ = Drift(l=0.4515, eid='ID_17795282_')
id_98284636_ = Drift(l=0.3285, eid='ID_98284636_')
d_210 = Drift(l=0.100105, eid='D_210')
d_211 = Drift(l=8.510829, eid='D_211')
d_212 = Drift(l=0.000104, eid='D_212')
id_83151514_ = Drift(l=0.635104, eid='ID_83151514_')
id_13055336_ = Drift(l=8.510725, eid='ID_13055336_')
id_54429047_ = Drift(l=0.579, eid='ID_54429047_')
id_1463922_ = Drift(l=0.4508, eid='ID_1463922_')
d_226 = Drift(l=0.1542, eid='D_226')
d_227 = Drift(l=0.09715, eid='D_227')
id_36362924_ = Drift(l=0.66515, eid='ID_36362924_')
id_76253336_ = Drift(l=1.15915, eid='ID_76253336_')
d_236 = Drift(l=0.15315, eid='D_236')
id_52070203_ = Drift(l=0.53115, eid='ID_52070203_')
d_243 = Drift(l=0.379, eid='D_243')
d_245 = Drift(l=0.13165, eid='D_245')
d_246 = Drift(l=1.03115, eid='D_246')
d_247 = Drift(l=1.23015, eid='D_247')
d_248 = Drift(l=0.18, eid='D_248')
id_30815182_ = Drift(l=1.329, eid='ID_30815182_')
d_256 = Drift(l=1.066, eid='D_256')
d_257 = Drift(l=0.147, eid='D_257')
d_259 = Drift(l=0.83115, eid='D_259')
id_53584452_ = Drift(l=0.6990000000000001, eid='ID_53584452_')
d_263 = Drift(l=0.13265, eid='D_263')
id_53716454_ = Drift(l=1.51065, eid='ID_53716454_')
d_267 = Drift(l=0.10765, eid='D_267')
id_4929001_ = Drift(l=1.303, eid='ID_4929001_')
d_272 = Drift(l=0.18165, eid='D_272')
id_32207144_ = Drift(l=0.89615, eid='ID_32207144_')
d_277 = Drift(l=1.22815, eid='D_277')
d_278 = Drift(l=0.152151, eid='D_278')
d_279 = Drift(l=0.081151, eid='D_279')
d_280 = Drift(l=0.15, eid='D_280')
id_65131257_ = Drift(l=1.4944009999999999, eid='ID_65131257_')

# Quadrupoles
qi_63_i1 = Quadrupole(l=0.2377, k1=-1.824087238998738, eid='QI.63.I1')
qi_66_i1 = Quadrupole(l=0.2377, k1=2.142575757000421, eid='QI.66.I1')
qi_69_i1 = Quadrupole(l=0.2377, k1=-2.1265116389987377, eid='QI.69.I1')
qi_71_i1 = Quadrupole(l=0.2377, k1=3.4033787980016825, eid='QI.71.I1')
qi_72_i1 = Quadrupole(l=0.2377, k1=-4.43452895, eid='QI.72.I1')
qi_73_i1 = Quadrupole(l=0.2377, k1=4.632555991998317, eid='QI.73.I1')
qi_74_i1 = Quadrupole(l=0.2377, k1=-4.991375219999999, eid='QI.74.I1')
qi_75_i1 = Quadrupole(l=0.2377, k1=5.027338701001262, eid='QI.75.I1')
qi_77_i1 = Quadrupole(l=0.2377, k1=-4.991375219999999, eid='QI.77.I1')
qi_78_i1 = Quadrupole(l=0.2377, k1=4.632555991998317, eid='QI.78.I1')
qi_79_i1 = Quadrupole(l=0.2377, k1=-4.991375219999999, eid='QI.79.I1')
qi_80_i1 = Quadrupole(l=0.2377, k1=5.027338701001262, eid='QI.80.I1')
qi_82_i1 = Quadrupole(l=0.2377, k1=-4.991375219999999, eid='QI.82.I1')
qi_83_i1 = Quadrupole(l=0.2377, k1=4.632555991998317, eid='QI.83.I1')
qi_84_i1 = Quadrupole(l=0.2377, k1=-4.991375219999999, eid='QI.84.I1')
qi_85_i1 = Quadrupole(l=0.2377, k1=5.027338701001262, eid='QI.85.I1')
qi_86_i1 = Quadrupole(l=0.2377, k1=-4.991375219999999, eid='QI.86.I1')
qi_88_i1 = Quadrupole(l=0.2377, k1=4.632555991998317, eid='QI.88.I1')
qi_89_i1 = Quadrupole(l=0.2377, k1=-4.991375219999999, eid='QI.89.I1')
qi_90_i1 = Quadrupole(l=0.2377, k1=5.027338701001262, eid='QI.90.I1')
qi_92_i1 = Quadrupole(l=0.2377, k1=-4.991375219999999, eid='QI.92.I1')
qi_93_i1 = Quadrupole(l=0.2377, k1=-0.7125210101009677, eid='QI.93.I1')
qi_94_i1 = Quadrupole(l=0.2377, k1=3.3764224510012624, eid='QI.94.I1')
qi_95_i1 = Quadrupole(l=0.2377, k1=-3.0503922929995793, eid='QI.95.I1')
qi_102_i1 = Quadrupole(l=0.2377, k1=0.6879609419983171, eid='QI.102.I1')
qi_103_i1 = Quadrupole(l=0.2377, k1=-1.3591500629995792, eid='QI.103.I1')
qi_104_i1 = Quadrupole(l=0.2377, k1=1.497501211998317, eid='QI.104.I1')
qi_107_i1 = Quadrupole(l=0.2377, k1=-1.5226412540008414, eid='QI.107.I1')
qi_109_i1 = Quadrupole(l=0.2377, k1=1.5226410680016829, eid='QI.109.I1')
qi_112_i1 = Quadrupole(l=0.2377, k1=-1.5226412540008414, eid='QI.112.I1')
qi_114_i1 = Quadrupole(l=0.2377, k1=0.9967996614009255, eid='QI.114.I1')
qi_116_i1 = Quadrupole(l=0.2377, k1=0.5375414028986117, eid='QI.116.I1')
qi_118_i1 = Quadrupole(l=0.2377, k1=-0.94121992, eid='QI.118.I1')
q_134_l1 = Quadrupole(l=0.2136, k1=0.2857947439981273, eid='Q.134.L1')
q_146_l1 = Quadrupole(l=0.2136, k1=-0.29239645940074904, eid='Q.146.L1')
q_158_l1 = Quadrupole(l=0.2136, k1=0.21577324690074903, eid='Q.158.L1')
q_170_l1 = Quadrupole(l=0.2136, k1=-0.22084659039794005, eid='Q.170.L1')
qi_176_b1 = Quadrupole(l=0.2377, eid='QI.176.B1')
qd_179_b1 = Quadrupole(l=0.2367, k1=0.7960126531009717, eid='QD.179.B1')
qd_181_b1 = Quadrupole(l=0.2367, k1=-0.7285956364005071, eid='QD.181.B1')
qi_204_b1 = Quadrupole(l=0.2377, k1=-0.9137399601009676, eid='QI.204.B1')
qi_205_b1 = Quadrupole(l=0.2377, k1=0.0415357294110223, eid='QI.205.B1')
qi_206_b1 = Quadrupole(l=0.2377, k1=0.6755384867017249, eid='QI.206.B1')
qi_209_b1 = Quadrupole(l=0.2377, k1=1.0443862489987379, eid='QI.209.B1')
qd_210_b1 = Quadrupole(l=0.2367, k1=-2.1831505249978878, eid='QD.210.B1')
qi_211_b1 = Quadrupole(l=0.2377, k1=0.6386118848001683, eid='QI.211.B1')
qi_213_b1 = Quadrupole(l=0.2377, k1=1.186969648998738, eid='QI.213.B1')
qi_215_b1 = Quadrupole(l=0.2377, k1=-1.1237338750021033, eid='QI.215.B1')
qi_217_b1 = Quadrupole(l=0.2377, k1=-1.43507582, eid='QI.217.B1')
qd_219_b1 = Quadrupole(l=0.2367, k1=2.859590704000845, eid='QD.219.B1')
qd_221_b1 = Quadrupole(l=0.2367, k1=-2.8595909289987325, eid='QD.221.B1')
qd_223_b1 = Quadrupole(l=0.2367, k1=2.859590704000845, eid='QD.223.B1')
qi_224_b1 = Quadrupole(l=0.2377, k1=-0.8565833407993269, eid='QI.224.B1')
qi_226_b1 = Quadrupole(l=0.2377, k1=-1.5618567640008414, eid='QI.226.B1')
qi_227_b1 = Quadrupole(l=0.2377, k1=1.5235329029995792, eid='QI.227.B1')

# SBends
bl_73_i1 = SBend(l=0.2, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, tilt=1.570796327, eid='BL.73.I1')
bl_75_i1 = SBend(l=0.2, angle=0.0426524581, e1=0.021326229, e2=0.021326229, tilt=1.570796327, eid='BL.75.I1')
bl_76_i1 = SBend(l=0.2, angle=0.0426524581, e1=0.021326229, e2=0.021326229, tilt=1.570796327, eid='BL.76.I1')
bl_77_i1 = SBend(l=0.2, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, tilt=1.570796327, eid='BL.77.I1')
bl_78_i1 = SBend(l=0.2, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, tilt=1.570796327, eid='BL.78.I1')
bl_80_i1 = SBend(l=0.2, angle=0.0426524581, e1=0.021326229, e2=0.021326229, tilt=1.570796327, eid='BL.80.I1')
bl_81_i1 = SBend(l=0.2, angle=0.0426524581, e1=0.021326229, e2=0.021326229, tilt=1.570796327, eid='BL.81.I1')
bl_82_i1 = SBend(l=0.2, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, tilt=1.570796327, eid='BL.82.I1')
bl_83_i1 = SBend(l=0.2, angle=0.1109740393, e1=0.05548702, e2=0.05548702, tilt=1.570796327, eid='BL.83.I1')
bl_85_i1 = SBend(l=0.2, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, tilt=1.570796327, eid='BL.85.I1')
bl_86_i1 = SBend(l=0.2, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, tilt=1.570796327, eid='BL.86.I1')
bl_87_i1 = SBend(l=0.2, angle=0.1109740393, e1=0.05548702, e2=0.05548702, tilt=1.570796327, eid='BL.87.I1')
bl_88_i1 = SBend(l=0.2, angle=0.1109740393, e1=0.05548702, e2=0.05548702, tilt=1.570796327, eid='BL.88.I1')
bl_90_i1 = SBend(l=0.2, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, tilt=1.570796327, eid='BL.90.I1')
bl_91_i1 = SBend(l=0.2, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, tilt=1.570796327, eid='BL.91.I1')
bl_92_i1 = SBend(l=0.2, angle=0.1109740393, e1=0.05548702, e2=0.05548702, tilt=1.570796327, eid='BL.92.I1')
bb_96_i1 = SBend(l=0.5, angle=0.11957038, e2=0.11957038, tilt=1.570796327, eid='BB.96.I1')
bb_98_i1 = SBend(l=0.5, angle=-0.11957038, e1=-0.11957038, tilt=1.570796327, eid='BB.98.I1')
bb_100_i1 = SBend(l=0.5, angle=-0.11957038, e2=-0.11957038, tilt=1.570796327, eid='BB.100.I1')
bb_101_i1 = SBend(l=0.5, angle=0.11957038, e1=0.11957038, tilt=1.570796327, eid='BB.101.I1')
bb_182_b1 = SBend(l=0.5, angle=0.04996493936, e2=0.049964939, tilt=1.570796327, eid='BB.182.B1')
bb_191_b1 = SBend(l=0.5, angle=-0.04996493936, e1=-0.049964939, tilt=1.570796327, eid='BB.191.B1')
bb_193_b1 = SBend(l=0.5, angle=-0.04996493936, e2=-0.049964939, tilt=1.570796327, eid='BB.193.B1')
bb_202_b1 = SBend(l=0.5, angle=0.04996493936, e1=0.049964939, tilt=1.570796327, eid='BB.202.B1')

# Sextupoles
sc_74i_i1 = Sextupole(l=0.1121, k2=-87.57825836, tilt=1.570796327, eid='SC.74I.I1')
sc_74ii_i1 = Sextupole(l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid='SC.74II.I1')
sc_76_i1 = Sextupole(l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid='SC.76.I1')
sc_77_i1 = Sextupole(l=0.1121, k2=-87.57825836, tilt=1.570796327, eid='SC.77.I1')
sc_79i_i1 = Sextupole(l=0.1121, k2=-87.57825836, tilt=1.570796327, eid='SC.79I.I1')
sc_79ii_i1 = Sextupole(l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid='SC.79II.I1')
sc_81_i1 = Sextupole(l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid='SC.81.I1')
sc_82_i1 = Sextupole(l=0.1121, k2=-87.57825836, tilt=1.570796327, eid='SC.82.I1')
sc_84i_i1 = Sextupole(l=0.1121, k2=87.57825836, tilt=1.570796327, eid='SC.84I.I1')
sc_84ii_i1 = Sextupole(l=0.1121, k2=53.061653289999995, tilt=1.570796327, eid='SC.84II.I1')
sc_86_i1 = Sextupole(l=0.1121, k2=53.061653289999995, tilt=1.570796327, eid='SC.86.I1')
sc_87_i1 = Sextupole(l=0.1121, k2=87.57825836, tilt=1.570796327, eid='SC.87.I1')
sc_89i_i1 = Sextupole(l=0.1121, k2=87.57825836, tilt=1.570796327, eid='SC.89I.I1')
sc_89ii_i1 = Sextupole(l=0.1121, k2=53.061653289999995, tilt=1.570796327, eid='SC.89II.I1')
sc_91_i1 = Sextupole(l=0.1121, k2=53.061653289999995, tilt=1.570796327, eid='SC.91.I1')
sc_92_i1 = Sextupole(l=0.1121, k2=87.57825836, tilt=1.570796327, eid='SC.92.I1')

# Hcors
cbb_62_i1d = Hcor(eid='CBB.62.I1D')
cix_65_i1 = Hcor(l=0.1, eid='CIX.65.I1')
cix_73i_i1 = Hcor(l=0.1, eid='CIX.73I.I1')
cix_73ii_i1 = Hcor(l=0.1, eid='CIX.73II.I1')
cix_76_i1 = Hcor(l=0.1, eid='CIX.76.I1')
cix_78_i1 = Hcor(l=0.1, eid='CIX.78.I1')
cix_81_i1 = Hcor(l=0.1, eid='CIX.81.I1')
cix_83_i1 = Hcor(l=0.1, eid='CIX.83.I1')
cix_86_i1 = Hcor(l=0.1, eid='CIX.86.I1')
cix_88_i1 = Hcor(l=0.1, eid='CIX.88.I1')
cix_90_i1 = Hcor(l=0.1, eid='CIX.90.I1')
cix_95_i1 = Hcor(l=0.1, eid='CIX.95.I1')
cix_102_i1 = Hcor(l=0.1, eid='CIX.102.I1')
cix_104_i1 = Hcor(l=0.1, eid='CIX.104.I1')
cix_109_i1 = Hcor(l=0.1, eid='CIX.109.I1')
cix_114_i1 = Hcor(l=0.1, eid='CIX.114.I1')
cix_118_i1 = Hcor(l=0.1, eid='CIX.118.I1')
cx_134_l1 = Hcor(eid='CX.134.L1')
cx_146_l1 = Hcor(eid='CX.146.L1')
cx_158_l1 = Hcor(eid='CX.158.L1')
cx_170_l1 = Hcor(eid='CX.170.L1')
cix_177_b1 = Hcor(l=0.1, eid='CIX.177.B1')
ccx_179_b1 = Hcor(l=0.1, eid='CCX.179.B1')
cix_205_b1 = Hcor(l=0.1, eid='CIX.205.B1')
cix_209_b1 = Hcor(l=0.1, eid='CIX.209.B1')
cix_213_b1 = Hcor(l=0.1, eid='CIX.213.B1')
cix_216_b1 = Hcor(l=0.1, eid='CIX.216.B1')
cfx_223_b1 = Hcor(l=0.1, eid='CFX.223.B1')
cfx_226_b1 = Hcor(l=0.1, eid='CFX.226.B1')

# Vcors
ciy_63_i1 = Vcor(l=0.1, eid='CIY.63.I1')
ciy_72_i1 = Vcor(l=0.1, eid='CIY.72.I1')
cbl_73_i1 = Vcor(eid='CBL.73.I1')
ciy_75_i1 = Vcor(l=0.1, eid='CIY.75.I1')
cbl_78_i1 = Vcor(eid='CBL.78.I1')
ciy_80_i1 = Vcor(l=0.1, eid='CIY.80.I1')
cbl_83_i1 = Vcor(eid='CBL.83.I1')
ciy_85_i1 = Vcor(l=0.1, eid='CIY.85.I1')
cbl_88_i1 = Vcor(eid='CBL.88.I1')
cbl_90_i1 = Vcor(eid='CBL.90.I1')
ciy_92_i1 = Vcor(l=0.1, eid='CIY.92.I1')
ciy_94_i1 = Vcor(l=0.1, eid='CIY.94.I1')
cbb_98_i1 = Vcor(eid='CBB.98.I1')
cbb_100_i1 = Vcor(eid='CBB.100.I1')
cbb_101_i1 = Vcor(eid='CBB.101.I1')
ciy_103_i1 = Vcor(l=0.1, eid='CIY.103.I1')
ciy_107_i1 = Vcor(l=0.1, eid='CIY.107.I1')
ciy_112_i1 = Vcor(l=0.1, eid='CIY.112.I1')
ciy_116_i1 = Vcor(l=0.1, eid='CIY.116.I1')
cy_134_l1 = Vcor(eid='CY.134.L1')
cy_146_l1 = Vcor(eid='CY.146.L1')
cy_158_l1 = Vcor(eid='CY.158.L1')
cy_170_l1 = Vcor(eid='CY.170.L1')
ciy_176_b1 = Vcor(l=0.1, eid='CIY.176.B1')
ccy_181_b1 = Vcor(l=0.1, eid='CCY.181.B1')
cbb_191_b1 = Vcor(eid='CBB.191.B1')
cbb_193_b1 = Vcor(eid='CBB.193.B1')
cbb_202_b1 = Vcor(eid='CBB.202.B1')
ciy_204_b1 = Vcor(l=0.1, eid='CIY.204.B1')
ccy_210_b1 = Vcor(l=0.1, eid='CCY.210.B1')
ciy_214_b1 = Vcor(l=0.1, eid='CIY.214.B1')
ccy_217_b1 = Vcor(l=0.1, eid='CCY.217.B1')
ccy_221_b1 = Vcor(l=0.1, eid='CCY.221.B1')
ciy_226_b1 = Vcor(l=0.1, eid='CIY.226.B1')

# Cavitys
c_a2_1_1_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.1.1.L1')
c_a2_1_2_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.1.2.L1')
c_a2_1_3_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.1.3.L1')
c_a2_1_4_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.1.4.L1')
c_a2_1_5_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.1.5.L1')
c_a2_1_6_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.1.6.L1')
c_a2_1_7_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.1.7.L1')
c_a2_1_8_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.1.8.L1')
c_a2_2_1_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.2.1.L1')
c_a2_2_2_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.2.2.L1')
c_a2_2_3_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.2.3.L1')
c_a2_2_4_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.2.4.L1')
c_a2_2_5_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.2.5.L1')
c_a2_2_6_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.2.6.L1')
c_a2_2_7_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.2.7.L1')
c_a2_2_8_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.2.8.L1')
c_a2_3_1_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.3.1.L1')
c_a2_3_2_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.3.2.L1')
c_a2_3_3_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.3.3.L1')
c_a2_3_4_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.3.4.L1')
c_a2_3_5_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.3.5.L1')
c_a2_3_6_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.3.6.L1')
c_a2_3_7_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.3.7.L1')
c_a2_3_8_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.3.8.L1')
c_a2_4_1_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.4.1.L1')
c_a2_4_2_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.4.2.L1')
c_a2_4_3_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.4.3.L1')
c_a2_4_4_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.4.4.L1')
c_a2_4_5_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.4.5.L1')
c_a2_4_6_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.4.6.L1')
c_a2_4_7_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.4.7.L1')
c_a2_4_8_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid='C.A2.4.8.L1')
tdsb_208_b1 = TDCavity(l=1.5, freq=3_000_000_000.0, eid='TDSB.208.B1')

# Monitors
bpma_63_i1 = Monitor(eid='BPMA.63.I1')
bpma_72_i1 = Monitor(eid='BPMA.72.I1')
bpma_75_i1 = Monitor(eid='BPMA.75.I1')
bpma_77_i1 = Monitor(eid='BPMA.77.I1')
bpma_80_i1 = Monitor(eid='BPMA.80.I1')
bpma_82_i1 = Monitor(eid='BPMA.82.I1')
bpma_85_i1 = Monitor(eid='BPMA.85.I1')
bpma_87_i1 = Monitor(eid='BPMA.87.I1')
bpma_90_i1 = Monitor(eid='BPMA.90.I1')
bpma_92_i1 = Monitor(eid='BPMA.92.I1')
bpmf_95_i1 = Monitor(eid='BPMF.95.I1')
bpms_99_i1 = Monitor(eid='BPMS.99.I1')
bpmf_103_i1 = Monitor(eid='BPMF.103.I1')
bpma_103_i1 = Monitor(eid='BPMA.103.I1')
bpma_105_i1 = Monitor(eid='BPMA.105.I1')
bpma_107_i1 = Monitor(eid='BPMA.107.I1')
bpma_110_i1 = Monitor(eid='BPMA.110.I1')
bpma_112_i1 = Monitor(eid='BPMA.112.I1')
bpma_115_i1 = Monitor(eid='BPMA.115.I1')
bpma_117_i1 = Monitor(eid='BPMA.117.I1')
bpma_119_i1 = Monitor(eid='BPMA.119.I1')
bpmc_134_l1 = Monitor(eid='BPMC.134.L1')
bpmr_146_l1 = Monitor(eid='BPMR.146.L1')
bpmc_158_l1 = Monitor(eid='BPMC.158.L1')
bpmr_170_l1 = Monitor(eid='BPMR.170.L1')
bpma_175_b1 = Monitor(eid='BPMA.175.B1')
bpma_179_b1 = Monitor(eid='BPMA.179.B1')
bpmf_181_b1 = Monitor(eid='BPMF.181.B1')
bpms_192_b1 = Monitor(eid='BPMS.192.B1')
bpmf_203_b1 = Monitor(eid='BPMF.203.B1')
bpma_206_b1 = Monitor(eid='BPMA.206.B1')
bpma_210_b1 = Monitor(eid='BPMA.210.B1')
bpma_213_b1 = Monitor(eid='BPMA.213.B1')
bpma_215_b1 = Monitor(eid='BPMA.215.B1')
bpma_217_b1 = Monitor(eid='BPMA.217.B1')
bpma_219_b1 = Monitor(eid='BPMA.219.B1')
bpma_221_b1 = Monitor(eid='BPMA.221.B1')
bpma_223_b1 = Monitor(eid='BPMA.223.B1')
bpma_226_b1 = Monitor(eid='BPMA.226.B1')
bpma_227_b1 = Monitor(eid='BPMA.227.B1')

# Markers
stlat_73_i1 = Marker(eid='STLAT.73.I1')
match_73_i1 = Marker(eid='MATCH.73.I1')
stlat_96_i1 = Marker(eid='STLAT.96.I1')
enlat_101_i1 = Marker(eid='ENLAT.101.I1')
stlat_104_i1 = Marker(eid='STLAT.104.I1')
match_104_i1 = Marker(eid='MATCH.104.I1')
stlat_182_b1 = Marker(eid='STLAT.182.B1')
match_202_b1 = Marker(eid='MATCH.202.B1')
tora_203_b1 = Marker(eid='TORA.203.B1')
match_207_b1 = Marker(eid='MATCH.207.B1')
match_218_b1 = Marker(eid='MATCH.218.B1')
ensub_229_b1 = Marker(eid='ENSUB.229.B1')

# Lattice 
cell = (d_2, cbb_62_i1d, d_3, ciy_63_i1, d_4, qi_63_i1, d_5, bpma_63_i1, d_6, 
cix_65_i1, d_7, qi_66_i1, d_8, qi_69_i1, d_9, qi_71_i1, d_10, bpma_72_i1, d_11, 
qi_72_i1, d_11, ciy_72_i1, d_13, cix_73i_i1, d_4, stlat_73_i1, match_73_i1, qi_73_i1, d_15, 
bl_73_i1, d_16, cbl_73_i1, d_17, cix_73ii_i1, d_18, sc_74i_i1, d_19, qi_74_i1, d_19, 
sc_74ii_i1, d_21, bl_75_i1, d_22, bpma_75_i1, d_23, ciy_75_i1, d_24, qi_75_i1, d_25, 
cix_76_i1, d_26, bl_76_i1, d_21, sc_76_i1, d_19, qi_77_i1, d_19, sc_77_i1, d_30, 
bpma_77_i1, d_31, bl_77_i1, d_15, qi_78_i1, d_33, bl_78_i1, d_16, cbl_78_i1, d_17, 
cix_78_i1, d_18, sc_79i_i1, d_19, qi_79_i1, d_19, sc_79ii_i1, d_39, bl_80_i1, d_22, 
bpma_80_i1, d_23, ciy_80_i1, d_24, qi_80_i1, d_25, cix_81_i1, d_44, bl_81_i1, d_21, 
sc_81_i1, d_19, qi_82_i1, d_19, sc_82_i1, d_48, bpma_82_i1, d_49, bl_82_i1, d_15, 
qi_83_i1, d_15, bl_83_i1, d_52, cbl_83_i1, d_17, cix_83_i1, d_54, sc_84i_i1, d_19, 
qi_84_i1, d_19, sc_84ii_i1, d_21, bl_85_i1, d_22, bpma_85_i1, d_23, ciy_85_i1, d_24, 
qi_85_i1, d_25, cix_86_i1, d_44, bl_86_i1, d_39, sc_86_i1, d_19, qi_86_i1, d_19, 
sc_87_i1, d_30, bpma_87_i1, d_49, bl_87_i1, d_15, qi_88_i1, d_15, bl_88_i1, d_16, 
cbl_88_i1, d_17, cix_88_i1, d_18, sc_89i_i1, d_19, qi_89_i1, d_19, sc_89ii_i1, d_39, 
bl_90_i1, d_76, cbl_90_i1, d_77, bpma_90_i1, d_23, cix_90_i1, d_24, qi_90_i1, d_80, 
bl_91_i1, d_21, sc_91_i1, d_19, qi_92_i1, d_19, sc_92_i1, d_84, ciy_92_i1, d_23, 
bpma_92_i1, d_31, bl_92_i1, d_15, qi_93_i1, id_30609505_, ciy_94_i1, d_90, qi_94_i1, id_7554339_, 
bpmf_95_i1, d_93, cix_95_i1, d_90, qi_95_i1, d_95, stlat_96_i1, d_96, bb_96_i1, d_97, 
bb_98_i1, d_98, cbb_98_i1, d_99, bpms_99_i1, id_79103439_, bb_100_i1, d_98, cbb_100_i1, d_103, 
bb_101_i1, d_104, cbb_101_i1, d_105, enlat_101_i1, d_106, qi_102_i1, d_90, cix_102_i1, id_14888141_, 
bpmf_103_i1, d_110, ciy_103_i1, d_90, qi_103_i1, d_11, bpma_103_i1, d_113, cix_104_i1, d_90, 
qi_104_i1, stlat_104_i1, match_104_i1, d_11, bpma_105_i1, d_116, ciy_107_i1, d_90, qi_107_i1, d_11, 
bpma_107_i1, d_116, cix_109_i1, d_90, qi_109_i1, d_11, bpma_110_i1, d_116, ciy_112_i1, d_90, 
qi_112_i1, d_11, bpma_112_i1, id_34013725_, cix_114_i1, d_90, qi_114_i1, d_11, bpma_115_i1, id_28166788_, 
ciy_116_i1, d_90, qi_116_i1, d_131, bpma_117_i1, id_50015017_, cix_118_i1, d_90, qi_118_i1, d_136, 
bpma_119_i1, id_70254102_, c_a2_1_1_l1, d_140, c_a2_1_2_l1, d_141, c_a2_1_3_l1, d_141, c_a2_1_4_l1, d_143, 
c_a2_1_5_l1, d_141, c_a2_1_6_l1, d_141, c_a2_1_7_l1, d_146, c_a2_1_8_l1, d_147, q_134_l1, d_148, 
cx_134_l1, cy_134_l1, d_149, bpmc_134_l1, id_82567243_, c_a2_2_1_l1, d_141, c_a2_2_2_l1, d_141, c_a2_2_3_l1, 
d_141, c_a2_2_4_l1, d_155, c_a2_2_5_l1, d_140, c_a2_2_6_l1, d_141, c_a2_2_7_l1, d_141, c_a2_2_8_l1, 
d_159, q_146_l1, d_160, cx_146_l1, cy_146_l1, d_161, bpmr_146_l1, id_85517094_, c_a2_3_1_l1, d_141, 
c_a2_3_2_l1, d_141, c_a2_3_3_l1, d_146, c_a2_3_4_l1, d_167, c_a2_3_5_l1, d_141, c_a2_3_6_l1, d_141, 
c_a2_3_7_l1, d_141, c_a2_3_8_l1, d_159, q_158_l1, d_172, cx_158_l1, cy_158_l1, d_173, bpmc_158_l1, 
id_36296974_, c_a2_4_1_l1, d_141, c_a2_4_2_l1, d_141, c_a2_4_3_l1, d_141, c_a2_4_4_l1, d_167, c_a2_4_5_l1, 
d_141, c_a2_4_6_l1, d_141, c_a2_4_7_l1, d_141, c_a2_4_8_l1, d_147, q_170_l1, d_160, cx_170_l1, 
cy_170_l1, d_161, bpmr_170_l1, id_70317273_, bpma_175_b1, d_191, qi_176_b1, d_192, ciy_176_b1, id_78014327_, 
cix_177_b1, id_45736562_, bpma_179_b1, d_199, qd_179_b1, d_200, ccx_179_b1, id_33800950_, qd_181_b1, d_204, 
ccy_181_b1, id_17795282_, bpmf_181_b1, id_98284636_, stlat_182_b1, d_210, bb_182_b1, d_211, bb_191_b1, d_212, 
cbb_191_b1, d_99, bpms_192_b1, id_83151514_, bb_193_b1, d_212, cbb_193_b1, id_13055336_, bb_202_b1, d_212, 
cbb_202_b1, d_105, match_202_b1, id_54429047_, bpmf_203_b1, id_1463922_, tora_203_b1, d_226, ciy_204_b1, d_227, 
qi_204_b1, id_36362924_, cix_205_b1, d_227, qi_205_b1, id_76253336_, bpma_206_b1, d_236, qi_206_b1, d_4, 
match_207_b1, d_105, tdsb_208_b1, d_11, qi_209_b1, id_52070203_, cix_209_b1, d_243, bpma_210_b1, d_199, 
qd_210_b1, d_245, ccy_210_b1, d_246, qi_211_b1, d_247, cix_213_b1, d_248, bpma_213_b1, d_191, 
qi_213_b1, d_4, ciy_214_b1, id_30815182_, bpma_215_b1, d_191, qi_215_b1, d_227, cix_216_b1, d_256, 
ccy_217_b1, d_257, bpma_217_b1, d_191, qi_217_b1, d_259, match_218_b1, id_53584452_, bpma_219_b1, d_263, 
qd_219_b1, id_53716454_, bpma_221_b1, d_199, qd_221_b1, d_267, ccy_221_b1, id_4929001_, bpma_223_b1, d_199, 
qd_223_b1, d_272, cfx_223_b1, id_32207144_, qi_224_b1, d_277, bpma_226_b1, d_278, qi_226_b1, d_279, 
ciy_226_b1, d_280, cfx_226_b1, d_248, bpma_227_b1, d_278, qi_227_b1, id_65131257_, ensub_229_b1)

# power supplies 

#  
qi_63_i1.ps_id = 'QI.13.I1'
qi_66_i1.ps_id = 'QI.14.I1'
qi_69_i1.ps_id = 'QI.15.I1'
qi_71_i1.ps_id = 'QI.16.I1'
qi_72_i1.ps_id = 'QI.17.I1'
qi_73_i1.ps_id = 'QI.18.I1'
qi_74_i1.ps_id = 'QI.19.I1'
qi_75_i1.ps_id = 'QI.20.I1'
qi_77_i1.ps_id = 'QI.19.I1'
qi_78_i1.ps_id = 'QI.18.I1'
qi_79_i1.ps_id = 'QI.19.I1'
qi_80_i1.ps_id = 'QI.20.I1'
qi_82_i1.ps_id = 'QI.21.I1'
qi_83_i1.ps_id = 'QI.22.I1'
qi_84_i1.ps_id = 'QI.21.I1'
qi_85_i1.ps_id = 'QI.24.I1'
qi_86_i1.ps_id = 'QI.23.I1'
qi_88_i1.ps_id = 'QI.22.I1'
qi_89_i1.ps_id = 'QI.23.I1'
qi_90_i1.ps_id = 'QI.24.I1'
qi_92_i1.ps_id = 'QI.23.I1'
qi_93_i1.ps_id = 'QI.25.I1'
qi_94_i1.ps_id = 'QI.26.I1'
qi_95_i1.ps_id = 'QI.27.I1'
qi_102_i1.ps_id = 'QI.28.I1'
qi_103_i1.ps_id = 'QI.29.I1'
qi_104_i1.ps_id = 'QI.30.I1'
qi_107_i1.ps_id = 'QI.31.I1'
qi_109_i1.ps_id = 'QI.32.I1'
qi_112_i1.ps_id = 'QI.31.I1'
qi_114_i1.ps_id = 'QI.33.I1'
qi_116_i1.ps_id = 'QI.34.I1'
qi_118_i1.ps_id = 'QI.35.I1'
q_134_l1.ps_id = 'Q.A2.1.L1'
q_146_l1.ps_id = 'Q.A2.2.L1'
q_158_l1.ps_id = 'Q.A2.3.L1'
q_170_l1.ps_id = 'Q.A2.4.L1'
qi_176_b1.ps_id = 'QI.1.B1'
qd_179_b1.ps_id = 'QD.3.B1'
qd_181_b1.ps_id = 'QD.4.B1'
qi_204_b1.ps_id = 'QI.5.B1'
qi_205_b1.ps_id = 'QI.6.B1'
qi_206_b1.ps_id = 'QI.7.B1'
qi_209_b1.ps_id = 'QI.8.B1'
qd_210_b1.ps_id = 'QD.9.B1'
qi_211_b1.ps_id = 'QI.10.B1'
qi_213_b1.ps_id = 'QI.11.B1'
qi_215_b1.ps_id = 'QI.12.B1'
qi_217_b1.ps_id = 'QI.13.B1'
qd_219_b1.ps_id = 'QD.14.B1'
qd_221_b1.ps_id = 'QD.15.B1'
qd_223_b1.ps_id = 'QD.16.B1'
qi_224_b1.ps_id = 'QI.17.B1'
qi_226_b1.ps_id = 'QI.18.B1'
qi_227_b1.ps_id = 'QI.19.B1'

#  
sc_74i_i1.ps_id = 'SC.1.I1'
sc_74ii_i1.ps_id = 'SC.2.I1'
sc_76_i1.ps_id = 'SC.2.I1'
sc_77_i1.ps_id = 'SC.1.I1'
sc_79i_i1.ps_id = 'SC.1.I1'
sc_79ii_i1.ps_id = 'SC.2.I1'
sc_81_i1.ps_id = 'SC.2.I1'
sc_82_i1.ps_id = 'SC.1.I1'
sc_84i_i1.ps_id = 'SC.1.I1'
sc_84ii_i1.ps_id = 'SC.2.I1'
sc_86_i1.ps_id = 'SC.2.I1'
sc_87_i1.ps_id = 'SC.1.I1'
sc_89i_i1.ps_id = 'SC.1.I1'
sc_89ii_i1.ps_id = 'SC.2.I1'
sc_91_i1.ps_id = 'SC.2.I1'
sc_92_i1.ps_id = 'SC.1.I1'

#  

#  
c_a2_1_1_l1.ps_id = 'C.A2.L1'
c_a2_1_2_l1.ps_id = 'C.A2.L1'
c_a2_1_3_l1.ps_id = 'C.A2.L1'
c_a2_1_4_l1.ps_id = 'C.A2.L1'
c_a2_1_5_l1.ps_id = 'C.A2.L1'
c_a2_1_6_l1.ps_id = 'C.A2.L1'
c_a2_1_7_l1.ps_id = 'C.A2.L1'
c_a2_1_8_l1.ps_id = 'C.A2.L1'
c_a2_2_1_l1.ps_id = 'C.A2.L1'
c_a2_2_2_l1.ps_id = 'C.A2.L1'
c_a2_2_3_l1.ps_id = 'C.A2.L1'
c_a2_2_4_l1.ps_id = 'C.A2.L1'
c_a2_2_5_l1.ps_id = 'C.A2.L1'
c_a2_2_6_l1.ps_id = 'C.A2.L1'
c_a2_2_7_l1.ps_id = 'C.A2.L1'
c_a2_2_8_l1.ps_id = 'C.A2.L1'
c_a2_3_1_l1.ps_id = 'C.A2.L1'
c_a2_3_2_l1.ps_id = 'C.A2.L1'
c_a2_3_3_l1.ps_id = 'C.A2.L1'
c_a2_3_4_l1.ps_id = 'C.A2.L1'
c_a2_3_5_l1.ps_id = 'C.A2.L1'
c_a2_3_6_l1.ps_id = 'C.A2.L1'
c_a2_3_7_l1.ps_id = 'C.A2.L1'
c_a2_3_8_l1.ps_id = 'C.A2.L1'
c_a2_4_1_l1.ps_id = 'C.A2.L1'
c_a2_4_2_l1.ps_id = 'C.A2.L1'
c_a2_4_3_l1.ps_id = 'C.A2.L1'
c_a2_4_4_l1.ps_id = 'C.A2.L1'
c_a2_4_5_l1.ps_id = 'C.A2.L1'
c_a2_4_6_l1.ps_id = 'C.A2.L1'
c_a2_4_7_l1.ps_id = 'C.A2.L1'
c_a2_4_8_l1.ps_id = 'C.A2.L1'
tdsb_208_b1.ps_id = 'TDSB.B1'

#  
bl_73_i1.ps_id = 'BL.6.I1'
bl_75_i1.ps_id = 'BL.7.I1'
bl_76_i1.ps_id = 'BL.7.I1'
bl_77_i1.ps_id = 'BL.6.I1'
bl_78_i1.ps_id = 'BL.6.I1'
bl_80_i1.ps_id = 'BL.7.I1'
bl_81_i1.ps_id = 'BL.7.I1'
bl_82_i1.ps_id = 'BL.6.I1'
bl_83_i1.ps_id = 'BL.8.I1'
bl_85_i1.ps_id = 'BL.7.I1'
bl_86_i1.ps_id = 'BL.7.I1'
bl_87_i1.ps_id = 'BL.8.I1'
bl_88_i1.ps_id = 'BL.8.I1'
bl_90_i1.ps_id = 'BL.7.I1'
bl_91_i1.ps_id = 'BL.7.I1'
bl_92_i1.ps_id = 'BL.8.I1'
bb_96_i1.ps_id = 'BB.1.I1'
bb_98_i1.ps_id = 'BB.1.I1'
bb_100_i1.ps_id = 'BB.1.I1'
bb_101_i1.ps_id = 'BB.1.I1'
bb_182_b1.ps_id = 'BB.1.B1'
bb_191_b1.ps_id = 'BB.1.B1'
bb_193_b1.ps_id = 'BB.1.B1'
bb_202_b1.ps_id = 'BB.1.B1'
