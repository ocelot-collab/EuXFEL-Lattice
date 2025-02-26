from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 7.865550253394325
tws0.beta_y = 8.698292442670796
tws0.alpha_x = -1.0418290882386196
tws0.alpha_y = -1.2234476587083056
tws0.E = 0.7
tws0.s = 229.3007540000002

# Drifts
id_14392663_ = Drift(l=0.75275, eid='ID_14392663_')
id_51114909_ = Drift(l=1.981646, eid='ID_51114909_')
d_5 = Drift(l=0.11165, eid='D_5')
id_30044875_ = Drift(l=0.30165, eid='ID_30044875_')
d_8 = Drift(l=0.12165, eid='D_8')
d_9 = Drift(l=0.15, eid='D_9')
d_10 = Drift(l=0.14165, eid='D_10')
id_87614399_ = Drift(l=5.11825, eid='ID_87614399_')
d_15 = Drift(l=0.3459, eid='D_15')
d_18 = Drift(l=0.34590000000001164, eid='D_18')
d_22 = Drift(l=0.2475, eid='D_22')
d_23 = Drift(l=0.0432, eid='D_23')
d_24 = Drift(l=0.085, eid='D_24')
id_96397212_ = Drift(l=0.6795, eid='ID_96397212_')
id_73897590_ = Drift(l=5.50178, eid='ID_73897590_')
d_162 = Drift(l=0.15277, eid='D_162')
d_163 = Drift(l=0.13165, eid='D_163')
id_77313796_ = Drift(l=0.62763, eid='ID_77313796_')
d_166 = Drift(l=0.13567, eid='D_166')
id_52631675_ = Drift(l=1.7788800000000002, eid='ID_52631675_')
d_172 = Drift(l=0.10065, eid='D_172')
id_80145267_ = Drift(l=0.56265, eid='ID_80145267_')
d_175 = Drift(l=0.08163, eid='D_175')
id_6596224_ = Drift(l=0.6944, eid='ID_6596224_')
id_53699920_ = Drift(l=0.55562, eid='ID_53699920_')
d_182 = Drift(l=0.100073, eid='D_182')
d_183 = Drift(l=8.507518, eid='D_183')
d_184 = Drift(l=7.2e-05, eid='D_184')
d_185 = Drift(l=0.865, eid='D_185')
id_89408864_ = Drift(l=0.635073, eid='ID_89408864_')
id_36281265_ = Drift(l=8.507446, eid='ID_36281265_')
d_192 = Drift(l=0.1, eid='D_192')
id_68782998_ = Drift(l=0.47848, eid='ID_68782998_')
id_79846102_ = Drift(l=0.40280000000000005, eid='ID_79846102_')
d_198 = Drift(l=0.15735, eid='D_198')
d_199 = Drift(l=0.14465, eid='D_199')
d_200 = Drift(l=0.15002, eid='D_200')
id_17322340_ = Drift(l=0.9316500000000001, eid='ID_17322340_')
d_203 = Drift(l=0.78165, eid='D_203')
d_205 = Drift(l=0.17888, eid='D_205')
id_34164022_ = Drift(l=6.53163, eid='ID_34164022_')
d_210 = Drift(l=0.17165, eid='D_210')
d_211 = Drift(l=0.19165, eid='D_211')
id_58358695_ = Drift(l=0.6369, eid='ID_58358695_')
d_214 = Drift(l=0.43477, eid='D_214')
id_97462571_ = Drift(l=0.38593, eid='ID_97462571_')
d_218_a = Drift(l=0.2, eid='D_218A')
d_218_b = Drift(l=0.2, eid='D_218B')
d_219 = Drift(l=0.17835, eid='D_219')
d_220 = Drift(l=0.09065, eid='D_220')
d_221 = Drift(l=0.3223, eid='D_221')
id_4070650_ = Drift(l=1.90937, eid='ID_4070650_')
d_226 = Drift(l=2.23165, eid='D_226')
id_59971044_ = Drift(l=3.41053, eid='ID_59971044_')
id_75923817_ = Drift(l=3.17888, eid='ID_75923817_')
d_237 = Drift(l=1.78153, eid='D_237')
id_1851905_ = Drift(l=0.9001199999999999, eid='ID_1851905_')
d_241 = Drift(l=0.62888, eid='D_241')
id_34805185_ = Drift(l=3.20488, eid='ID_34805185_')
d_248 = Drift(l=0.15285, eid='D_248')
id_78522273_ = Drift(l=2.10555, eid='ID_78522273_')
d_251 = Drift(l=1.1789, eid='D_251')
id_16339514_ = Drift(l=3.1788800000000004, eid='ID_16339514_')
id_18957204_ = Drift(l=2.6288799999999997, eid='ID_18957204_')
d_264 = Drift(l=0.15275, eid='D_264')
id_37030553_ = Drift(l=0.8316699999999999, eid='ID_37030553_')
d_267 = Drift(l=0.33165, eid='D_267')
d_269 = Drift(l=0.35, eid='D_269')
id_1421083_ = Drift(l=0.53165, eid='ID_1421083_')

# Quadrupoles
qd_231_b1 = Quadrupole(l=0.2367, k1=1.6557307729995776, eid='QD.231.B1')
qd_232_b1 = Quadrupole(l=0.2367, k1=-1.2501718110012676, eid='QD.232.B1')
qd_233_b1 = Quadrupole(l=0.2367, k1=-0.4397248283016477, eid='QD.233.B1')
q_249_l2 = Quadrupole(l=0.2136, k1=0.424912906900749, eid='Q.249.L2')
q_261_l2 = Quadrupole(l=0.2136, k1=-0.39384852710205986, eid='Q.261.L2')
q_273_l2 = Quadrupole(l=0.2136, k1=0.387775731900749, eid='Q.273.L2')
q_285_l2 = Quadrupole(l=0.2136, k1=-0.4247537369990636, eid='Q.285.L2')
q_297_l2 = Quadrupole(l=0.2136, k1=0.48818981139981266, eid='Q.297.L2')
q_309_l2 = Quadrupole(l=0.2136, k1=-0.6058097569990636, eid='Q.309.L2')
q_321_l2 = Quadrupole(l=0.2136, k1=0.48818981139981266, eid='Q.321.L2')
q_333_l2 = Quadrupole(l=0.2136, k1=-0.6058097569990636, eid='Q.333.L2')
q_345_l2 = Quadrupole(l=0.2136, k1=0.6525829807022472, eid='Q.345.L2')
q_357_l2 = Quadrupole(l=0.2136, k1=-0.38908541679775277, eid='Q.357.L2')
q_369_l2 = Quadrupole(l=0.2136, k1=0.43128398199906365, eid='Q.369.L2')
q_381_l2 = Quadrupole(l=0.2136, k1=-0.38391488749999997, eid='Q.381.L2')
qd_387_b2 = Quadrupole(l=0.2367, k1=0.335173384799324, eid='QD.387.B2')
qd_388_b2 = Quadrupole(l=0.2367, k1=0.35599643220109844, eid='QD.388.B2')
qd_391_b2 = Quadrupole(l=0.2367, k1=-0.7255245525982257, eid='QD.391.B2')
qd_392_b2 = Quadrupole(l=0.2367, k1=0.19699609059991552, eid='QD.392.B2')
qd_415_b2 = Quadrupole(l=0.2367, k1=0.1806864174017744, eid='QD.415.B2')
qd_417_b2 = Quadrupole(l=0.2367, k1=-0.7502347655006337, eid='QD.417.B2')
qd_418_b2 = Quadrupole(l=0.2367, k1=0.6491929171989861, eid='QD.418.B2')
qd_425_b2 = Quadrupole(l=0.2367, k1=-1.3008034, eid='QD.425.B2')
qd_427_b2 = Quadrupole(l=0.2367, k1=0.9414835846007605, eid='QD.427.B2')
qd_431_b2 = Quadrupole(l=0.2367, k1=0.43518302749894383, eid='QD.431.B2')
qd_434_b2 = Quadrupole(l=0.2367, k1=-0.5278581910012674, eid='QD.434.B2')
qd_437_b2 = Quadrupole(l=0.2367, k1=0.4055492834980989, eid='QD.437.B2')
qd_440_b2 = Quadrupole(l=0.2367, k1=-0.6685246719983101, eid='QD.440.B2')
qd_444_b2 = Quadrupole(l=0.2367, k1=-0.4582186614997888, eid='QD.444.B2')
qd_448_b2 = Quadrupole(l=0.2367, k1=0.8960955489987327, eid='QD.448.B2')
qd_452_b2 = Quadrupole(l=0.2367, k1=-1.263284384000845, eid='QD.452.B2')
qd_456_b2 = Quadrupole(l=0.2367, k1=0.8960955489987327, eid='QD.456.B2')

# special optics in B2/B2D for energy spread measurements  
qd_459_b2 = Quadrupole(l=0.2367, k1=-0.6010, eid='QD.459.B2')
qd_463_b2 = Quadrupole(l=0.2367, k1=1.3346, eid='QD.463.B2')
qd_464_b2 = Quadrupole(l=0.2367, k1=0.7416, eid='QD.464.B2')
qd_465_b2 = Quadrupole(l=0.2367, k1=-1.7783, eid='QD.465.B2')

# SBends
bb_393_b2 = SBend(l=0.5, angle=0.04163879892, e2=0.041638799, tilt=1.570796327, eid='BB.393.B2')
bb_402_b2 = SBend(l=0.5, angle=-0.04163879892, e1=-0.041638799, tilt=1.570796327, eid='BB.402.B2')
bb_404_b2 = SBend(l=0.5, angle=-0.04163879892, e2=-0.041638799, tilt=1.570796327, eid='BB.404.B2')
bb_413_b2 = SBend(l=0.5, angle=0.04163879892, e1=0.041638799, tilt=1.570796327, eid='BB.413.B2')

# Hcors
ccx_232_b1 = Hcor(l=0.1, eid='CCX.232.B1')
cx_249_l2 = Hcor(eid='CX.249.L2')
cx_273_l2 = Hcor(eid='CX.273.L2')
cx_297_l2 = Hcor(eid='CX.297.L2')
cx_321_l2 = Hcor(eid='CX.321.L2')
cx_345_l2 = Hcor(eid='CX.345.L2')
cx_369_l2 = Hcor(eid='CX.369.L2')
ccx_388_b2 = Hcor(l=0.1, eid='CCX.388.B2')
ccx_392_b2 = Hcor(l=0.1, eid='CCX.392.B2')
ccx_415_b2 = Hcor(l=0.1, eid='CCX.415.B2')
ccx_418_b2 = Hcor(l=0.1, eid='CCX.418.B2')
ccx_425_b2 = Hcor(l=0.1, eid='CCX.425.B2')
ccx_431_b2 = Hcor(l=0.1, eid='CCX.431.B2')
ccx_441_b2 = Hcor(l=0.1, eid='CCX.441.B2')
ccx_447_b2 = Hcor(l=0.1, eid='CCX.447.B2')
ccx_454_b2 = Hcor(l=0.1, eid='CCX.454.B2')
ccx_456_b2 = Hcor(l=0.1, eid='CCX.456.B2')
ccx_464_b2 = Hcor(l=0.1, eid='CCX.464.B2')
ccx_465_b2 = Hcor(l=0.1, eid='CCX.465.B2')

# Vcors
cbb_229_b1d = Vcor(eid='CBB.229.B1D')
ccy_232_b1 = Vcor(l=0.1, eid='CCY.232.B1')
cy_261_l2 = Vcor(eid='CY.261.L2')
cy_285_l2 = Vcor(eid='CY.285.L2')
cy_309_l2 = Vcor(eid='CY.309.L2')
cy_333_l2 = Vcor(eid='CY.333.L2')
cy_357_l2 = Vcor(eid='CY.357.L2')
cy_381_l2 = Vcor(eid='CY.381.L2')
ccy_387_b2 = Vcor(l=0.1, eid='CCY.387.B2')
ccy_391_b2 = Vcor(l=0.1, eid='CCY.391.B2')
cbb_403_b2 = Vcor(eid='CBB.403.B2')
cbb_405_b2 = Vcor(eid='CBB.405.B2')
cbb_414_b2 = Vcor(eid='CBB.414.B2')
ccy_416_b2 = Vcor(l=0.1, eid='CCY.416.B2')
ccy_418_b2 = Vcor(l=0.1, eid='CCY.418.B2')
ccy_426_b2 = Vcor(l=0.1, eid='CCY.426.B2')
ccy_434_b2 = Vcor(l=0.1, eid='CCY.434.B2')
ccy_448_b2 = Vcor(l=0.1, eid='CCY.448.B2')
ccy_460_b2 = Vcor(l=0.1, eid='CCY.460.B2')
ccy_464_b2 = Vcor(l=0.1, eid='CCY.464.B2')

# Cavitys
c_a3_1_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.1.1.L2')
c_a3_1_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.1.2.L2')
c_a3_1_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.1.3.L2')
c_a3_1_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.1.4.L2')
c_a3_1_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.1.5.L2')
c_a3_1_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.1.6.L2')
c_a3_1_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.1.7.L2')
c_a3_1_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.1.8.L2')
c_a3_2_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.2.1.L2')
c_a3_2_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.2.2.L2')
c_a3_2_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.2.3.L2')
c_a3_2_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.2.4.L2')
c_a3_2_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.2.5.L2')
c_a3_2_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.2.6.L2')
c_a3_2_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.2.7.L2')
c_a3_2_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.2.8.L2')
c_a3_3_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.3.1.L2')
c_a3_3_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.3.2.L2')
c_a3_3_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.3.3.L2')
c_a3_3_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.3.4.L2')
c_a3_3_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.3.5.L2')
c_a3_3_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.3.6.L2')
c_a3_3_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.3.7.L2')
c_a3_3_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.3.8.L2')
c_a3_4_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.4.1.L2')
c_a3_4_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.4.2.L2')
c_a3_4_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.4.3.L2')
c_a3_4_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.4.4.L2')
c_a3_4_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.4.5.L2')
c_a3_4_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.4.6.L2')
c_a3_4_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.4.7.L2')
c_a3_4_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A3.4.8.L2')
c_a4_1_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.1.1.L2')
c_a4_1_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.1.2.L2')
c_a4_1_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.1.3.L2')
c_a4_1_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.1.4.L2')
c_a4_1_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.1.5.L2')
c_a4_1_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.1.6.L2')
c_a4_1_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.1.7.L2')
c_a4_1_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.1.8.L2')
c_a4_2_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.2.1.L2')
c_a4_2_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.2.2.L2')
c_a4_2_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.2.3.L2')
c_a4_2_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.2.4.L2')
c_a4_2_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.2.5.L2')
c_a4_2_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.2.6.L2')
c_a4_2_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.2.7.L2')
c_a4_2_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.2.8.L2')
c_a4_3_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.3.1.L2')
c_a4_3_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.3.2.L2')
c_a4_3_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.3.3.L2')
c_a4_3_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.3.4.L2')
c_a4_3_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.3.5.L2')
c_a4_3_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.3.6.L2')
c_a4_3_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.3.7.L2')
c_a4_3_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.3.8.L2')
c_a4_4_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.4.1.L2')
c_a4_4_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.4.2.L2')
c_a4_4_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.4.3.L2')
c_a4_4_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.4.4.L2')
c_a4_4_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.4.5.L2')
c_a4_4_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.4.6.L2')
c_a4_4_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.4.7.L2')
c_a4_4_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A4.4.8.L2')
c_a5_1_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.1.1.L2')
c_a5_1_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.1.2.L2')
c_a5_1_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.1.3.L2')
c_a5_1_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.1.4.L2')
c_a5_1_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.1.5.L2')
c_a5_1_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.1.6.L2')
c_a5_1_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.1.7.L2')
c_a5_1_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.1.8.L2')
c_a5_2_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.2.1.L2')
c_a5_2_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.2.2.L2')
c_a5_2_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.2.3.L2')
c_a5_2_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.2.4.L2')
c_a5_2_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.2.5.L2')
c_a5_2_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.2.6.L2')
c_a5_2_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.2.7.L2')
c_a5_2_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.2.8.L2')
c_a5_3_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.3.1.L2')
c_a5_3_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.3.2.L2')
c_a5_3_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.3.3.L2')
c_a5_3_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.3.4.L2')
c_a5_3_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.3.5.L2')
c_a5_3_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.3.6.L2')
c_a5_3_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.3.7.L2')
c_a5_3_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.3.8.L2')
c_a5_4_1_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.4.1.L2')
c_a5_4_2_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.4.2.L2')
c_a5_4_3_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.4.3.L2')
c_a5_4_4_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.4.4.L2')
c_a5_4_5_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.4.5.L2')
c_a5_4_6_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.4.6.L2')
c_a5_4_7_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.4.7.L2')
c_a5_4_8_l2 = Cavity(l=1.0377, v=0.01770833333, freq=1300000000.0, eid='C.A5.4.8.L2')
tdsb_428_b2 = TDCavity(l=1.5, freq=2800000000.0, eid='TDSB.428.B2')
tdsb_430_b2 = TDCavity(l=1.5, freq=2800000000.0, eid='TDSB.430.B2')

# Monitors
bpma_233_b1 = Monitor(eid='BPMA.233.B1')
bpmc_249_l2 = Monitor(eid='BPMC.249.L2')
bpmc_261_l2 = Monitor(eid='BPMC.261.L2')
bpmr_273_l2 = Monitor(eid='BPMR.273.L2')
bpmr_285_l2 = Monitor(eid='BPMR.285.L2')
bpmc_297_l2 = Monitor(eid='BPMC.297.L2')
bpmr_309_l2 = Monitor(eid='BPMR.309.L2')
bpmc_321_l2 = Monitor(eid='BPMC.321.L2')
bpmr_333_l2 = Monitor(eid='BPMR.333.L2')
bpmc_345_l2 = Monitor(eid='BPMC.345.L2')
bpmc_357_l2 = Monitor(eid='BPMC.357.L2')
bpmr_369_l2 = Monitor(eid='BPMR.369.L2')
bpmr_381_l2 = Monitor(eid='BPMR.381.L2')
bpma_387_b2 = Monitor(eid='BPMA.387.B2')
bpma_390_b2 = Monitor(eid='BPMA.390.B2')
bpmf_393_b2 = Monitor(eid='BPMF.393.B2')
bpms_404_b2 = Monitor(eid='BPMS.404.B2')
bpmf_414_b2 = Monitor(eid='BPMF.414.B2')
bpma_418_b2 = Monitor(eid='BPMA.418.B2')
bpma_426_b2 = Monitor(eid='BPMA.426.B2')
bpma_432_b2 = Monitor(eid='BPMA.432.B2')
bpma_440_b2 = Monitor(eid='BPMA.440.B2')
bpma_444_b2 = Monitor(eid='BPMA.444.B2')
bpma_448_b2 = Monitor(eid='BPMA.448.B2')
bpma_452_b2 = Monitor(eid='BPMA.452.B2')
bpma_455_b2 = Monitor(eid='BPMA.455.B2')
bpma_459_b2 = Monitor(eid='BPMA.459.B2')
bpma_462_b2 = Monitor(eid='BPMA.462.B2')
bpma_465_b2 = Monitor(eid='BPMA.465.B2')

# Markers
stlat_393_b2 = Marker(eid='STLAT.393.B2')
match_414_b2 = Marker(eid='MATCH.414.B2')
tora_415_b2 = Marker(eid='TORA.415.B2')
match_428_b2 = Marker(eid='MATCH.428.B2')
marker_tds_b2 = Marker(eid='MARKER.TDS.B2')
match_446_b2 = Marker(eid='MATCH.446.B2')
ensub_466_b2 = Marker(eid='ENSUB.466.B2')

# Lattice 
cell = (id_14392663_, cbb_229_b1d, id_51114909_, qd_231_b1, d_5, ccx_232_b1, id_30044875_, qd_232_b1, d_8, 
ccy_232_b1, d_9, bpma_233_b1, d_10, qd_233_b1, id_87614399_, c_a3_1_1_l2, d_15, c_a3_1_2_l2, d_15, 
c_a3_1_3_l2, d_15, c_a3_1_4_l2, d_18, c_a3_1_5_l2, d_15, c_a3_1_6_l2, d_15, c_a3_1_7_l2, d_15, 
c_a3_1_8_l2, d_22, q_249_l2, d_23, cx_249_l2, d_24, bpmc_249_l2, id_96397212_, c_a3_2_1_l2, d_15, 
c_a3_2_2_l2, d_15, c_a3_2_3_l2, d_15, c_a3_2_4_l2, d_18, c_a3_2_5_l2, d_15, c_a3_2_6_l2, d_15, 
c_a3_2_7_l2, d_15, c_a3_2_8_l2, d_22, q_261_l2, d_23, cy_261_l2, d_24, bpmc_261_l2, id_96397212_, 
c_a3_3_1_l2, d_15, c_a3_3_2_l2, d_15, c_a3_3_3_l2, d_15, c_a3_3_4_l2, d_18, c_a3_3_5_l2, d_15, 
c_a3_3_6_l2, d_15, c_a3_3_7_l2, d_15, c_a3_3_8_l2, d_22, q_273_l2, d_23, cx_273_l2, d_24, 
bpmr_273_l2, id_96397212_, c_a3_4_1_l2, d_15, c_a3_4_2_l2, d_15, c_a3_4_3_l2, d_15, c_a3_4_4_l2, d_18, 
c_a3_4_5_l2, d_15, c_a3_4_6_l2, d_15, c_a3_4_7_l2, d_15, c_a3_4_8_l2, d_22, q_285_l2, d_23, 
cy_285_l2, d_24, bpmr_285_l2, id_96397212_, c_a4_1_1_l2, d_15, c_a4_1_2_l2, d_15, c_a4_1_3_l2, d_15, 
c_a4_1_4_l2, d_18, c_a4_1_5_l2, d_15, c_a4_1_6_l2, d_15, c_a4_1_7_l2, d_15, c_a4_1_8_l2, d_22, 
q_297_l2, d_23, cx_297_l2, d_24, bpmc_297_l2, id_96397212_, c_a4_2_1_l2, d_15, c_a4_2_2_l2, d_15, 
c_a4_2_3_l2, d_15, c_a4_2_4_l2, d_18, c_a4_2_5_l2, d_15, c_a4_2_6_l2, d_15, c_a4_2_7_l2, d_15, 
c_a4_2_8_l2, d_22, q_309_l2, d_23, cy_309_l2, d_24, bpmr_309_l2, id_96397212_, c_a4_3_1_l2, d_15, 
c_a4_3_2_l2, d_15, c_a4_3_3_l2, d_15, c_a4_3_4_l2, d_18, c_a4_3_5_l2, d_15, c_a4_3_6_l2, d_15, 
c_a4_3_7_l2, d_15, c_a4_3_8_l2, d_22, q_321_l2, d_23, cx_321_l2, d_24, bpmc_321_l2, id_96397212_, 
c_a4_4_1_l2, d_15, c_a4_4_2_l2, d_15, c_a4_4_3_l2, d_15, c_a4_4_4_l2, d_18, c_a4_4_5_l2, d_15, 
c_a4_4_6_l2, d_15, c_a4_4_7_l2, d_15, c_a4_4_8_l2, d_22, q_333_l2, d_23, cy_333_l2, d_24, 
bpmr_333_l2, id_96397212_, c_a5_1_1_l2, d_15, c_a5_1_2_l2, d_15, c_a5_1_3_l2, d_15, c_a5_1_4_l2, d_18, 
c_a5_1_5_l2, d_15, c_a5_1_6_l2, d_15, c_a5_1_7_l2, d_15, c_a5_1_8_l2, d_22, q_345_l2, d_23, 
cx_345_l2, d_24, bpmc_345_l2, id_96397212_, c_a5_2_1_l2, d_15, c_a5_2_2_l2, d_15, c_a5_2_3_l2, d_15, 
c_a5_2_4_l2, d_18, c_a5_2_5_l2, d_15, c_a5_2_6_l2, d_15, c_a5_2_7_l2, d_15, c_a5_2_8_l2, d_22, 
q_357_l2, d_23, cy_357_l2, d_24, bpmc_357_l2, id_96397212_, c_a5_3_1_l2, d_15, c_a5_3_2_l2, d_15, 
c_a5_3_3_l2, d_15, c_a5_3_4_l2, d_18, c_a5_3_5_l2, d_15, c_a5_3_6_l2, d_15, c_a5_3_7_l2, d_15, 
c_a5_3_8_l2, d_22, q_369_l2, d_23, cx_369_l2, d_24, bpmr_369_l2, id_96397212_, c_a5_4_1_l2, d_15, 
c_a5_4_2_l2, d_15, c_a5_4_3_l2, d_15, c_a5_4_4_l2, d_18, c_a5_4_5_l2, d_15, c_a5_4_6_l2, d_15, 
c_a5_4_7_l2, d_15, c_a5_4_8_l2, d_22, q_381_l2, d_23, cy_381_l2, d_24, bpmr_381_l2, id_73897590_,
bpma_387_b2, d_162, qd_387_b2, d_163, ccy_387_b2, id_77313796_, qd_388_b2, d_166, ccx_388_b2, id_52631675_, 
bpma_390_b2, d_162, qd_391_b2, d_172, ccy_391_b2, id_80145267_, qd_392_b2, d_175, ccx_392_b2, id_6596224_, 
bpmf_393_b2, id_53699920_, stlat_393_b2, d_182, bb_393_b2, d_183, bb_402_b2, d_184, cbb_403_b2, d_185, 
bpms_404_b2, id_89408864_, bb_404_b2, d_184, cbb_405_b2, id_36281265_, bb_413_b2, d_184, cbb_414_b2, d_192, 
match_414_b2, id_68782998_, bpmf_414_b2, id_79846102_, tora_415_b2, d_198, qd_415_b2, d_199, ccx_415_b2, d_200, 
ccy_416_b2, id_17322340_, qd_417_b2, d_203, ccx_418_b2, d_9, ccy_418_b2, d_205, bpma_418_b2, d_162, 
qd_418_b2, id_34164022_, ccx_425_b2, d_210, qd_425_b2, d_211, ccy_426_b2, id_58358695_, bpma_426_b2, d_214, 
qd_427_b2, id_97462571_, match_428_b2, tdsb_428_b2, d_218_a, marker_tds_b2, d_218_b, tdsb_430_b2, d_219, qd_431_b2, d_220, ccx_431_b2, 
d_221, bpma_432_b2, id_4070650_, qd_434_b2, d_163, ccy_434_b2, d_226, qd_437_b2, id_59971044_, bpma_440_b2, 
d_162, qd_440_b2, d_163, ccx_441_b2, id_75923817_, bpma_444_b2, d_162, qd_444_b2, d_237, match_446_b2, 
id_1851905_, ccx_447_b2, d_241, bpma_448_b2, d_162, qd_448_b2, d_163, ccy_448_b2, id_34805185_, bpma_452_b2, 
d_248, qd_452_b2, id_78522273_, ccx_454_b2, d_251, bpma_455_b2, d_162, qd_456_b2, d_163, ccx_456_b2, 
id_16339514_, bpma_459_b2, d_162, qd_459_b2, d_163, ccy_460_b2, id_18957204_, bpma_462_b2, d_264, qd_463_b2, 
id_37030553_, ccx_464_b2, d_267, qd_464_b2, d_163, ccy_464_b2, d_269, ccx_465_b2, d_205, bpma_465_b2, 
d_162, qd_465_b2, id_1421083_, ensub_466_b2)

# power supplies 

#  
qd_231_b1.ps_id = 'QD.20.B1'
qd_232_b1.ps_id = 'QD.21.B1'
qd_233_b1.ps_id = 'QD.22.B1'
q_249_l2.ps_id = 'Q.A3.1.L2'
q_261_l2.ps_id = 'Q.A3.2.L2'
q_273_l2.ps_id = 'Q.A3.3.L2'
q_285_l2.ps_id = 'Q.A3.4.L2'
q_297_l2.ps_id = 'Q.A4.1.L2'
q_309_l2.ps_id = 'Q.A4.2.L2'
q_321_l2.ps_id = 'Q.A4.3.L2'
q_333_l2.ps_id = 'Q.A4.4.L2'
q_345_l2.ps_id = 'Q.A5.1.L2'
q_357_l2.ps_id = 'Q.A5.2.L2'
q_369_l2.ps_id = 'Q.A5.3.L2'
q_381_l2.ps_id = 'Q.A5.4.L2'
qd_387_b2.ps_id = 'QD.1.B2'
qd_388_b2.ps_id = 'QD.2.B2'
qd_391_b2.ps_id = 'QD.3.B2'
qd_392_b2.ps_id = 'QD.4.B2'
qd_415_b2.ps_id = 'QD.6.B2'
qd_417_b2.ps_id = 'QD.7.B2'
qd_418_b2.ps_id = 'QD.8.B2'
qd_425_b2.ps_id = 'QD.9.B2'
qd_427_b2.ps_id = 'QD.10.B2'
qd_431_b2.ps_id = 'QD.11.B2'
qd_434_b2.ps_id = 'QD.12.B2'
qd_437_b2.ps_id = 'QD.13.B2'
qd_440_b2.ps_id = 'QD.14.B2'
qd_444_b2.ps_id = 'QD.15.B2'
qd_448_b2.ps_id = 'QD.16.B2'
qd_452_b2.ps_id = 'QD.17.B2'
qd_456_b2.ps_id = 'QD.18.B2'
qd_459_b2.ps_id = 'QD.19.B2'
qd_463_b2.ps_id = 'QD.21.B2'
qd_464_b2.ps_id = 'QD.22.B2'
qd_465_b2.ps_id = 'QD.23.B2'

#  

#  

#  
c_a3_1_1_l2.ps_id = 'C.A3.L2'
c_a3_1_2_l2.ps_id = 'C.A3.L2'
c_a3_1_3_l2.ps_id = 'C.A3.L2'
c_a3_1_4_l2.ps_id = 'C.A3.L2'
c_a3_1_5_l2.ps_id = 'C.A3.L2'
c_a3_1_6_l2.ps_id = 'C.A3.L2'
c_a3_1_7_l2.ps_id = 'C.A3.L2'
c_a3_1_8_l2.ps_id = 'C.A3.L2'
c_a3_2_1_l2.ps_id = 'C.A3.L2'
c_a3_2_2_l2.ps_id = 'C.A3.L2'
c_a3_2_3_l2.ps_id = 'C.A3.L2'
c_a3_2_4_l2.ps_id = 'C.A3.L2'
c_a3_2_5_l2.ps_id = 'C.A3.L2'
c_a3_2_6_l2.ps_id = 'C.A3.L2'
c_a3_2_7_l2.ps_id = 'C.A3.L2'
c_a3_2_8_l2.ps_id = 'C.A3.L2'
c_a3_3_1_l2.ps_id = 'C.A3.L2'
c_a3_3_2_l2.ps_id = 'C.A3.L2'
c_a3_3_3_l2.ps_id = 'C.A3.L2'
c_a3_3_4_l2.ps_id = 'C.A3.L2'
c_a3_3_5_l2.ps_id = 'C.A3.L2'
c_a3_3_6_l2.ps_id = 'C.A3.L2'
c_a3_3_7_l2.ps_id = 'C.A3.L2'
c_a3_3_8_l2.ps_id = 'C.A3.L2'
c_a3_4_1_l2.ps_id = 'C.A3.L2'
c_a3_4_2_l2.ps_id = 'C.A3.L2'
c_a3_4_3_l2.ps_id = 'C.A3.L2'
c_a3_4_4_l2.ps_id = 'C.A3.L2'
c_a3_4_5_l2.ps_id = 'C.A3.L2'
c_a3_4_6_l2.ps_id = 'C.A3.L2'
c_a3_4_7_l2.ps_id = 'C.A3.L2'
c_a3_4_8_l2.ps_id = 'C.A3.L2'
c_a4_1_1_l2.ps_id = 'C.A4.L2'
c_a4_1_2_l2.ps_id = 'C.A4.L2'
c_a4_1_3_l2.ps_id = 'C.A4.L2'
c_a4_1_4_l2.ps_id = 'C.A4.L2'
c_a4_1_5_l2.ps_id = 'C.A4.L2'
c_a4_1_6_l2.ps_id = 'C.A4.L2'
c_a4_1_7_l2.ps_id = 'C.A4.L2'
c_a4_1_8_l2.ps_id = 'C.A4.L2'
c_a4_2_1_l2.ps_id = 'C.A4.L2'
c_a4_2_2_l2.ps_id = 'C.A4.L2'
c_a4_2_3_l2.ps_id = 'C.A4.L2'
c_a4_2_4_l2.ps_id = 'C.A4.L2'
c_a4_2_5_l2.ps_id = 'C.A4.L2'
c_a4_2_6_l2.ps_id = 'C.A4.L2'
c_a4_2_7_l2.ps_id = 'C.A4.L2'
c_a4_2_8_l2.ps_id = 'C.A4.L2'
c_a4_3_1_l2.ps_id = 'C.A4.L2'
c_a4_3_2_l2.ps_id = 'C.A4.L2'
c_a4_3_3_l2.ps_id = 'C.A4.L2'
c_a4_3_4_l2.ps_id = 'C.A4.L2'
c_a4_3_5_l2.ps_id = 'C.A4.L2'
c_a4_3_6_l2.ps_id = 'C.A4.L2'
c_a4_3_7_l2.ps_id = 'C.A4.L2'
c_a4_3_8_l2.ps_id = 'C.A4.L2'
c_a4_4_1_l2.ps_id = 'C.A4.L2'
c_a4_4_2_l2.ps_id = 'C.A4.L2'
c_a4_4_3_l2.ps_id = 'C.A4.L2'
c_a4_4_4_l2.ps_id = 'C.A4.L2'
c_a4_4_5_l2.ps_id = 'C.A4.L2'
c_a4_4_6_l2.ps_id = 'C.A4.L2'
c_a4_4_7_l2.ps_id = 'C.A4.L2'
c_a4_4_8_l2.ps_id = 'C.A4.L2'
c_a5_1_1_l2.ps_id = 'C.A5.L2'
c_a5_1_2_l2.ps_id = 'C.A5.L2'
c_a5_1_3_l2.ps_id = 'C.A5.L2'
c_a5_1_4_l2.ps_id = 'C.A5.L2'
c_a5_1_5_l2.ps_id = 'C.A5.L2'
c_a5_1_6_l2.ps_id = 'C.A5.L2'
c_a5_1_7_l2.ps_id = 'C.A5.L2'
c_a5_1_8_l2.ps_id = 'C.A5.L2'
c_a5_2_1_l2.ps_id = 'C.A5.L2'
c_a5_2_2_l2.ps_id = 'C.A5.L2'
c_a5_2_3_l2.ps_id = 'C.A5.L2'
c_a5_2_4_l2.ps_id = 'C.A5.L2'
c_a5_2_5_l2.ps_id = 'C.A5.L2'
c_a5_2_6_l2.ps_id = 'C.A5.L2'
c_a5_2_7_l2.ps_id = 'C.A5.L2'
c_a5_2_8_l2.ps_id = 'C.A5.L2'
c_a5_3_1_l2.ps_id = 'C.A5.L2'
c_a5_3_2_l2.ps_id = 'C.A5.L2'
c_a5_3_3_l2.ps_id = 'C.A5.L2'
c_a5_3_4_l2.ps_id = 'C.A5.L2'
c_a5_3_5_l2.ps_id = 'C.A5.L2'
c_a5_3_6_l2.ps_id = 'C.A5.L2'
c_a5_3_7_l2.ps_id = 'C.A5.L2'
c_a5_3_8_l2.ps_id = 'C.A5.L2'
c_a5_4_1_l2.ps_id = 'C.A5.L2'
c_a5_4_2_l2.ps_id = 'C.A5.L2'
c_a5_4_3_l2.ps_id = 'C.A5.L2'
c_a5_4_4_l2.ps_id = 'C.A5.L2'
c_a5_4_5_l2.ps_id = 'C.A5.L2'
c_a5_4_6_l2.ps_id = 'C.A5.L2'
c_a5_4_7_l2.ps_id = 'C.A5.L2'
c_a5_4_8_l2.ps_id = 'C.A5.L2'
tdsb_428_b2.ps_id = 'TDSB.B2'
tdsb_430_b2.ps_id = 'TDSB.B2'

#  
bb_393_b2.ps_id = 'BB.1.B2'
bb_402_b2.ps_id = 'BB.1.B2'
bb_404_b2.ps_id = 'BB.1.B2'
bb_413_b2.ps_id = 'BB.1.B2'
