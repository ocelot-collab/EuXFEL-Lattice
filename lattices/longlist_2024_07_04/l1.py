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
id_6161799_ = Drift(l=1.08128, eid='ID_6161799_')
d_89 = Drift(l=0.09115, eid='D_89')
id_83842682_ = Drift(l=0.37715, eid='ID_83842682_')
d_92 = Drift(l=0.204, eid='D_92')
id_80996332_ = Drift(l=0.481747, eid='ID_80996332_')
d_96 = Drift(l=1.008384, eid='D_96')
d_97 = Drift(l=0.000597, eid='D_97')
d_98 = Drift(l=0.865, eid='D_98')
id_36970828_ = Drift(l=0.635597, eid='ID_36970828_')
d_102 = Drift(l=1.007788, eid='D_102')
d_103 = Drift(l=0.000596, eid='D_103')
id_26568381_ = Drift(l=0.49115, eid='ID_26568381_')
id_97117542_ = Drift(l=0.346, eid='ID_97117542_')
d_109 = Drift(l=0.144, eid='D_109')
d_112 = Drift(l=0.56, eid='D_112')
d_115 = Drift(l=1.89, eid='D_115')
id_71584398_ = Drift(l=2.04, eid='ID_71584398_')
d_127 = Drift(l=1.265, eid='D_127')
d_129 = Drift(l=0.13965, eid='D_129')
id_67850901_ = Drift(l=1.5315, eid='ID_67850901_')
d_134 = Drift(l=0.14395, eid='D_134')
id_91009848_ = Drift(l=3.923801, eid='ID_91009848_')
d_138 = Drift(l=0.345899, eid='D_138')
d_139 = Drift(l=0.3459, eid='D_139')
d_141 = Drift(l=0.34589999999999743, eid='D_141')
d_144 = Drift(l=0.345901, eid='D_144')
d_145 = Drift(l=0.247499, eid='D_145')
d_146 = Drift(l=0.043201, eid='D_146')
d_147 = Drift(l=0.084999, eid='D_147')
id_14265913_ = Drift(l=0.679501, eid='ID_14265913_')
d_153 = Drift(l=0.3459000000000091, eid='D_153')
d_157 = Drift(l=0.2475, eid='D_157')
d_158 = Drift(l=0.0432, eid='D_158')
d_159 = Drift(l=0.085001, eid='D_159')
id_12304491_ = Drift(l=0.679499, eid='ID_12304491_')
d_165 = Drift(l=0.34590000000001164, eid='D_165')
d_170 = Drift(l=0.043199, eid='D_170')
d_171 = Drift(l=0.085, eid='D_171')
id_30325032_ = Drift(l=0.6795009999999999, eid='ID_30325032_')
id_11969122_ = Drift(l=5.5019, eid='ID_11969122_')
d_188 = Drift(l=0.15215, eid='D_188')
d_189 = Drift(l=0.082149, eid='D_189')
id_62666542_ = Drift(l=1.215001, eid='ID_62666542_')
id_49664260_ = Drift(l=1.613, eid='ID_49664260_')
d_196 = Drift(l=0.15265, eid='D_196')
d_197 = Drift(l=0.131649, eid='D_197')
id_77907075_ = Drift(l=0.88165, eid='ID_77907075_')
d_201 = Drift(l=0.10165, eid='D_201')
id_94824990_ = Drift(l=0.4515, eid='ID_94824990_')
id_39701602_ = Drift(l=0.428605, eid='ID_39701602_')
d_208 = Drift(l=8.510829, eid='D_208')
d_209 = Drift(l=0.000104, eid='D_209')
id_74995762_ = Drift(l=0.635104, eid='ID_74995762_')
id_79940265_ = Drift(l=8.510725, eid='ID_79940265_')
id_91265111_ = Drift(l=0.1, eid='ID_91265111_')
id_57147630_ = Drift(l=0.579, eid='ID_57147630_')
id_23905750_ = Drift(l=0.605, eid='ID_23905750_')
d_223 = Drift(l=0.09715, eid='D_223')
id_55530023_ = Drift(l=0.66515, eid='ID_55530023_')
id_22713406_ = Drift(l=1.15915, eid='ID_22713406_')
d_232 = Drift(l=0.15315, eid='D_232')
id_77795231_ = Drift(l=0.53115, eid='ID_77795231_')
d_239 = Drift(l=0.379, eid='D_239')
d_241 = Drift(l=0.13165, eid='D_241')
d_242 = Drift(l=1.03115, eid='D_242')
d_243 = Drift(l=1.23015, eid='D_243')
d_244 = Drift(l=0.18, eid='D_244')
id_74461398_ = Drift(l=1.329, eid='ID_74461398_')
d_252 = Drift(l=1.066, eid='D_252')
d_253 = Drift(l=0.147, eid='D_253')
d_255 = Drift(l=0.83115, eid='D_255')
id_44694527_ = Drift(l=0.6990000000000001, eid='ID_44694527_')
d_259 = Drift(l=0.13265, eid='D_259')
id_80557051_ = Drift(l=1.51065, eid='ID_80557051_')
d_263 = Drift(l=0.10765, eid='D_263')
id_74584989_ = Drift(l=1.303, eid='ID_74584989_')
d_268 = Drift(l=0.18165, eid='D_268')
id_28052257_ = Drift(l=0.89615, eid='ID_28052257_')
d_273 = Drift(l=1.22815, eid='D_273')
d_274 = Drift(l=0.152151, eid='D_274')
d_275 = Drift(l=0.081151, eid='D_275')
d_276 = Drift(l=0.15, eid='D_276')
id_18501197_ = Drift(l=1.4944009999999999, eid='ID_18501197_')

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
tdsb_208_b1 = Cavity(l=1.5, freq=2800000000.0, eid='TDSB.208.B1')

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
stlat_104_i1 = Marker(eid='STLAT.104.I1')
match_104_i1 = Marker(eid='MATCH.104.I1')
match_202_b1 = Marker(eid='MATCH.202.B1')
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
bpma_92_i1, d_31, bl_92_i1, d_15, qi_93_i1, id_6161799_, ciy_94_i1, d_89, qi_94_i1, id_83842682_, 
bpmf_95_i1, d_92, cix_95_i1, d_89, qi_95_i1, id_80996332_, bb_96_i1, d_96, bb_98_i1, d_97, 
cbb_98_i1, d_98, bpms_99_i1, id_36970828_, bb_100_i1, d_97, cbb_100_i1, d_102, bb_101_i1, d_103, 
cbb_101_i1, id_26568381_, qi_102_i1, d_89, cix_102_i1, id_97117542_, bpmf_103_i1, d_109, ciy_103_i1, d_89, 
qi_103_i1, d_11, bpma_103_i1, d_112, cix_104_i1, d_89, qi_104_i1, stlat_104_i1, match_104_i1, d_11, 
bpma_105_i1, d_115, ciy_107_i1, d_89, qi_107_i1, d_11, bpma_107_i1, d_115, cix_109_i1, d_89, 
qi_109_i1, d_11, bpma_110_i1, d_115, ciy_112_i1, d_89, qi_112_i1, d_11, bpma_112_i1, id_71584398_, 
cix_114_i1, d_89, qi_114_i1, d_11, bpma_115_i1, d_127, ciy_116_i1, d_89, qi_116_i1, d_129, 
bpma_117_i1, id_67850901_, cix_118_i1, d_89, qi_118_i1, d_134, bpma_119_i1, id_91009848_, c_a2_1_1_l1, d_138, 
c_a2_1_2_l1, d_139, c_a2_1_3_l1, d_139, c_a2_1_4_l1, d_141, c_a2_1_5_l1, d_139, c_a2_1_6_l1, d_139, 
c_a2_1_7_l1, d_144, c_a2_1_8_l1, d_145, q_134_l1, d_146, cx_134_l1, cy_134_l1, d_147, bpmc_134_l1, 
id_14265913_, c_a2_2_1_l1, d_139, c_a2_2_2_l1, d_139, c_a2_2_3_l1, d_139, c_a2_2_4_l1, d_153, c_a2_2_5_l1, 
d_138, c_a2_2_6_l1, d_139, c_a2_2_7_l1, d_139, c_a2_2_8_l1, d_157, q_146_l1, d_158, cx_146_l1, 
cy_146_l1, d_159, bpmr_146_l1, id_12304491_, c_a2_3_1_l1, d_139, c_a2_3_2_l1, d_139, c_a2_3_3_l1, d_144, 
c_a2_3_4_l1, d_165, c_a2_3_5_l1, d_139, c_a2_3_6_l1, d_139, c_a2_3_7_l1, d_139, c_a2_3_8_l1, d_157, 
q_158_l1, d_170, cx_158_l1, cy_158_l1, d_171, bpmc_158_l1, id_30325032_, c_a2_4_1_l1, d_139, c_a2_4_2_l1, 
d_139, c_a2_4_3_l1, d_139, c_a2_4_4_l1, d_165, c_a2_4_5_l1, d_139, c_a2_4_6_l1, d_139, c_a2_4_7_l1, 
d_139, c_a2_4_8_l1, d_145, q_170_l1, d_158, cx_170_l1, cy_170_l1, d_159, bpmr_170_l1, id_11969122_, 
bpma_175_b1, d_188, qi_176_b1, d_189, ciy_176_b1, id_62666542_, cix_177_b1, id_49664260_, bpma_179_b1, d_196, 
qd_179_b1, d_197, ccx_179_b1, id_77907075_, qd_181_b1, d_201, ccy_181_b1, id_94824990_, bpmf_181_b1, id_39701602_, 
bb_182_b1, d_208, bb_191_b1, d_209, cbb_191_b1, d_98, bpms_192_b1, id_74995762_, bb_193_b1, d_209, 
cbb_193_b1, id_79940265_, bb_202_b1, d_209, cbb_202_b1, id_91265111_, match_202_b1, id_57147630_, bpmf_203_b1, id_23905750_, 
ciy_204_b1, d_223, qi_204_b1, id_55530023_, cix_205_b1, d_223, qi_205_b1, id_22713406_, bpma_206_b1, d_232, 
qi_206_b1, d_4, match_207_b1, id_91265111_, tdsb_208_b1, d_11, qi_209_b1, id_77795231_, cix_209_b1, d_239, 
bpma_210_b1, d_196, qd_210_b1, d_241, ccy_210_b1, d_242, qi_211_b1, d_243, cix_213_b1, d_244, 
bpma_213_b1, d_188, qi_213_b1, d_4, ciy_214_b1, id_74461398_, bpma_215_b1, d_188, qi_215_b1, d_223, 
cix_216_b1, d_252, ccy_217_b1, d_253, bpma_217_b1, d_188, qi_217_b1, d_255, match_218_b1, id_44694527_, 
bpma_219_b1, d_259, qd_219_b1, id_80557051_, bpma_221_b1, d_196, qd_221_b1, d_263, ccy_221_b1, id_74584989_, 
bpma_223_b1, d_196, qd_223_b1, d_268, cfx_223_b1, id_28052257_, qi_224_b1, d_273, bpma_226_b1, d_274, 
qi_226_b1, d_275, ciy_226_b1, d_276, cfx_226_b1, d_244, bpma_227_b1, d_274, qi_227_b1, id_18501197_, 
ensub_229_b1)

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
