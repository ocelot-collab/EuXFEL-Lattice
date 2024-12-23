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
id_26522109_ = Drift(l=0.75275, eid='ID_26522109_')
id_2007636_ = Drift(l=1.981646, eid='ID_2007636_')
d_5 = Drift(l=0.11165, eid='D_5')
d_6 = Drift(l=0.30165, eid='D_6')
d_7 = Drift(l=0.12165, eid='D_7')
d_8 = Drift(l=0.15, eid='D_8')
d_9 = Drift(l=0.14165, eid='D_9')
id_43621455_ = Drift(l=5.11825, eid='ID_43621455_')
d_14 = Drift(l=0.3459, eid='D_14')
d_17 = Drift(l=0.34590000000001164, eid='D_17')
d_21 = Drift(l=0.2475, eid='D_21')
d_22 = Drift(l=0.0432, eid='D_22')
d_23 = Drift(l=0.085, eid='D_23')
id_16561622_ = Drift(l=0.6795, eid='ID_16561622_')
id_28816941_ = Drift(l=5.501779999999999, eid='ID_28816941_')
d_160 = Drift(l=0.15277, eid='D_160')
d_161 = Drift(l=0.13165, eid='D_161')
id_4454691_ = Drift(l=0.62763, eid='ID_4454691_')
d_164 = Drift(l=0.13567, eid='D_164')
id_65238679_ = Drift(l=1.7788800000000002, eid='ID_65238679_')
d_170 = Drift(l=0.10065, eid='D_170')
id_33313242_ = Drift(l=0.56265, eid='ID_33313242_')
d_173 = Drift(l=0.08163, eid='D_173')
id_99063270_ = Drift(l=0.6944, eid='ID_99063270_')
id_72656274_ = Drift(l=0.655693, eid='ID_72656274_')
d_181 = Drift(l=8.507518, eid='D_181')
d_182 = Drift(l=7.2e-05, eid='D_182')
d_183 = Drift(l=0.865, eid='D_183')
id_1242906_ = Drift(l=0.635073, eid='ID_1242906_')
id_74547950_ = Drift(l=8.507446, eid='ID_74547950_')
d_190 = Drift(l=0.1, eid='D_190')
id_93237090_ = Drift(l=0.47848, eid='ID_93237090_')
id_66588577_ = Drift(l=0.56015, eid='ID_66588577_')
d_196 = Drift(l=0.14465, eid='D_196')
d_197 = Drift(l=0.15002, eid='D_197')
id_84954588_ = Drift(l=0.9316500000000001, eid='ID_84954588_')
d_200 = Drift(l=0.78165, eid='D_200')
d_202 = Drift(l=0.17888, eid='D_202')
id_99369969_ = Drift(l=6.53163, eid='ID_99369969_')
d_207 = Drift(l=0.17165, eid='D_207')
d_208 = Drift(l=0.19165, eid='D_208')
id_86197077_ = Drift(l=0.6369, eid='ID_86197077_')
d_211 = Drift(l=0.43477, eid='D_211')
id_35620920_ = Drift(l=0.38593, eid='ID_35620920_')
d_215 = Drift(l=0.4, eid='D_215')
d_216 = Drift(l=0.17835, eid='D_216')
d_217 = Drift(l=0.09065, eid='D_217')
d_218 = Drift(l=0.3223, eid='D_218')
id_34645513_ = Drift(l=1.90937, eid='ID_34645513_')
d_223 = Drift(l=2.23165, eid='D_223')
id_22588271_ = Drift(l=3.41053, eid='ID_22588271_')
id_2932158_ = Drift(l=3.17888, eid='ID_2932158_')
d_234 = Drift(l=1.78153, eid='D_234')
id_63862942_ = Drift(l=0.9001199999999999, eid='ID_63862942_')
d_238 = Drift(l=0.62888, eid='D_238')
id_55269868_ = Drift(l=3.20488, eid='ID_55269868_')
d_245 = Drift(l=0.15285, eid='D_245')
id_60824773_ = Drift(l=2.10555, eid='ID_60824773_')
d_248 = Drift(l=1.1789, eid='D_248')
id_21118484_ = Drift(l=3.1788800000000004, eid='ID_21118484_')
id_19882239_ = Drift(l=2.6288799999999997, eid='ID_19882239_')
d_261 = Drift(l=0.15275, eid='D_261')
id_59258793_ = Drift(l=0.8316699999999999, eid='ID_59258793_')
d_264 = Drift(l=0.33165, eid='D_264')
d_266 = Drift(l=0.35, eid='D_266')
id_57211269_ = Drift(l=0.53165, eid='ID_57211269_')

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
qd_459_b2 = Quadrupole(l=0.2367, k1=-1.263284384000845, eid='QD.459.B2')
qd_463_b2 = Quadrupole(l=0.2367, k1=-0.569607097600338, eid='QD.463.B2')
qd_464_b2 = Quadrupole(l=0.2367, k1=1.2982678500000002, eid='QD.464.B2')
qd_465_b2 = Quadrupole(l=0.2367, k1=-0.24686100550063372, eid='QD.465.B2')

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
tdsb_428_b2 = Cavity(l=1.5, freq=2800000000.0, eid='TDSB.428.B2')
tdsb_430_b2 = Cavity(l=1.5, freq=2800000000.0, eid='TDSB.430.B2')

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
match_414_b2 = Marker(eid='MATCH.414.B2')
match_428_b2 = Marker(eid='MATCH.428.B2')
match_446_b2 = Marker(eid='MATCH.446.B2')
ensub_466_b2 = Marker(eid='ENSUB.466.B2')

# Lattice 
cell = (id_26522109_, cbb_229_b1d, id_2007636_, qd_231_b1, d_5, ccx_232_b1, d_6, qd_232_b1, d_7, 
ccy_232_b1, d_8, bpma_233_b1, d_9, qd_233_b1, id_43621455_, c_a3_1_1_l2, d_14, c_a3_1_2_l2, d_14, 
c_a3_1_3_l2, d_14, c_a3_1_4_l2, d_17, c_a3_1_5_l2, d_14, c_a3_1_6_l2, d_14, c_a3_1_7_l2, d_14, 
c_a3_1_8_l2, d_21, q_249_l2, d_22, cx_249_l2, d_23, bpmc_249_l2, id_16561622_, c_a3_2_1_l2, d_14, 
c_a3_2_2_l2, d_14, c_a3_2_3_l2, d_14, c_a3_2_4_l2, d_17, c_a3_2_5_l2, d_14, c_a3_2_6_l2, d_14, 
c_a3_2_7_l2, d_14, c_a3_2_8_l2, d_21, q_261_l2, d_22, cy_261_l2, d_23, bpmc_261_l2, id_16561622_, 
c_a3_3_1_l2, d_14, c_a3_3_2_l2, d_14, c_a3_3_3_l2, d_14, c_a3_3_4_l2, d_17, c_a3_3_5_l2, d_14, 
c_a3_3_6_l2, d_14, c_a3_3_7_l2, d_14, c_a3_3_8_l2, d_21, q_273_l2, d_22, cx_273_l2, d_23, 
bpmr_273_l2, id_16561622_, c_a3_4_1_l2, d_14, c_a3_4_2_l2, d_14, c_a3_4_3_l2, d_14, c_a3_4_4_l2, d_17, 
c_a3_4_5_l2, d_14, c_a3_4_6_l2, d_14, c_a3_4_7_l2, d_14, c_a3_4_8_l2, d_21, q_285_l2, d_22, 
cy_285_l2, d_23, bpmr_285_l2, id_16561622_, c_a4_1_1_l2, d_14, c_a4_1_2_l2, d_14, c_a4_1_3_l2, d_14, 
c_a4_1_4_l2, d_17, c_a4_1_5_l2, d_14, c_a4_1_6_l2, d_14, c_a4_1_7_l2, d_14, c_a4_1_8_l2, d_21, 
q_297_l2, d_22, cx_297_l2, d_23, bpmc_297_l2, id_16561622_, c_a4_2_1_l2, d_14, c_a4_2_2_l2, d_14, 
c_a4_2_3_l2, d_14, c_a4_2_4_l2, d_17, c_a4_2_5_l2, d_14, c_a4_2_6_l2, d_14, c_a4_2_7_l2, d_14, 
c_a4_2_8_l2, d_21, q_309_l2, d_22, cy_309_l2, d_23, bpmr_309_l2, id_16561622_, c_a4_3_1_l2, d_14, 
c_a4_3_2_l2, d_14, c_a4_3_3_l2, d_14, c_a4_3_4_l2, d_17, c_a4_3_5_l2, d_14, c_a4_3_6_l2, d_14, 
c_a4_3_7_l2, d_14, c_a4_3_8_l2, d_21, q_321_l2, d_22, cx_321_l2, d_23, bpmc_321_l2, id_16561622_, 
c_a4_4_1_l2, d_14, c_a4_4_2_l2, d_14, c_a4_4_3_l2, d_14, c_a4_4_4_l2, d_17, c_a4_4_5_l2, d_14, 
c_a4_4_6_l2, d_14, c_a4_4_7_l2, d_14, c_a4_4_8_l2, d_21, q_333_l2, d_22, cy_333_l2, d_23, 
bpmr_333_l2, id_16561622_, c_a5_1_1_l2, d_14, c_a5_1_2_l2, d_14, c_a5_1_3_l2, d_14, c_a5_1_4_l2, d_17, 
c_a5_1_5_l2, d_14, c_a5_1_6_l2, d_14, c_a5_1_7_l2, d_14, c_a5_1_8_l2, d_21, q_345_l2, d_22, 
cx_345_l2, d_23, bpmc_345_l2, id_16561622_, c_a5_2_1_l2, d_14, c_a5_2_2_l2, d_14, c_a5_2_3_l2, d_14, 
c_a5_2_4_l2, d_17, c_a5_2_5_l2, d_14, c_a5_2_6_l2, d_14, c_a5_2_7_l2, d_14, c_a5_2_8_l2, d_21, 
q_357_l2, d_22, cy_357_l2, d_23, bpmc_357_l2, id_16561622_, c_a5_3_1_l2, d_14, c_a5_3_2_l2, d_14, 
c_a5_3_3_l2, d_14, c_a5_3_4_l2, d_17, c_a5_3_5_l2, d_14, c_a5_3_6_l2, d_14, c_a5_3_7_l2, d_14, 
c_a5_3_8_l2, d_21, q_369_l2, d_22, cx_369_l2, d_23, bpmr_369_l2, id_16561622_, c_a5_4_1_l2, d_14, 
c_a5_4_2_l2, d_14, c_a5_4_3_l2, d_14, c_a5_4_4_l2, d_17, c_a5_4_5_l2, d_14, c_a5_4_6_l2, d_14, 
c_a5_4_7_l2, d_14, c_a5_4_8_l2, d_21, q_381_l2, d_22, cy_381_l2, d_23, bpmr_381_l2, id_28816941_, 
bpma_387_b2, d_160, qd_387_b2, d_161, ccy_387_b2, id_4454691_, qd_388_b2, d_164, ccx_388_b2, id_65238679_, 
bpma_390_b2, d_160, qd_391_b2, d_170, ccy_391_b2, id_33313242_, qd_392_b2, d_173, ccx_392_b2, id_99063270_, 
bpmf_393_b2, id_72656274_, bb_393_b2, d_181, bb_402_b2, d_182, cbb_403_b2, d_183, bpms_404_b2, id_1242906_, 
bb_404_b2, d_182, cbb_405_b2, id_74547950_, bb_413_b2, d_182, cbb_414_b2, d_190, match_414_b2, id_93237090_, 
bpmf_414_b2, id_66588577_, qd_415_b2, d_196, ccx_415_b2, d_197, ccy_416_b2, id_84954588_, qd_417_b2, d_200, 
ccx_418_b2, d_8, ccy_418_b2, d_202, bpma_418_b2, d_160, qd_418_b2, id_99369969_, ccx_425_b2, d_207, 
qd_425_b2, d_208, ccy_426_b2, id_86197077_, bpma_426_b2, d_211, qd_427_b2, id_35620920_, match_428_b2, tdsb_428_b2, 
d_215, tdsb_430_b2, d_216, qd_431_b2, d_217, ccx_431_b2, d_218, bpma_432_b2, id_34645513_, qd_434_b2, 
d_161, ccy_434_b2, d_223, qd_437_b2, id_22588271_, bpma_440_b2, d_160, qd_440_b2, d_161, ccx_441_b2, 
id_2932158_, bpma_444_b2, d_160, qd_444_b2, d_234, match_446_b2, id_63862942_, ccx_447_b2, d_238, bpma_448_b2, 
d_160, qd_448_b2, d_161, ccy_448_b2, id_55269868_, bpma_452_b2, d_245, qd_452_b2, id_60824773_, ccx_454_b2, 
d_248, bpma_455_b2, d_160, qd_456_b2, d_161, ccx_456_b2, id_21118484_, bpma_459_b2, d_160, qd_459_b2, 
d_161, ccy_460_b2, id_19882239_, bpma_462_b2, d_261, qd_463_b2, id_59258793_, ccx_464_b2, d_264, qd_464_b2, 
d_161, ccy_464_b2, d_266, ccx_465_b2, d_202, bpma_465_b2, d_160, qd_465_b2, id_57211269_, ensub_466_b2)

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
