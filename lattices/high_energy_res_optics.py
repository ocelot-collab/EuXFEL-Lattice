from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 55.7981
tws0.beta_y = 55.7981
tws0.alpha_x = 18.1886
tws0.alpha_y = 18.1886
tws0.gamma_x = 5.946890126366311
tws0.gamma_y = 5.946890126366311
tws0.E = 0.005

# Drifts
id_97509745_ = Drift(l=0.276, eid='ID_97509745_')
d_2a = Drift(l=0.216, eid='D_2')
d_3a = Drift(l=0.311, eid='D_3')
d_4a = Drift(l=0.047, eid='D_4')
id_70110258_ = Drift(l=1.101, eid='ID_70110258_')
id_41101705_ = Drift(l=0.421, eid='ID_41101705_')
d_12a = Drift(l=0.5776, eid='D_12')
id_35969356_ = Drift(l=0.3216, eid='ID_35969356_')
d_13a = Drift(l=0.3459, eid='D_13')
d_16a = Drift(l=0.3458999999999992, eid='D_16')
d_20 = Drift(l=0.2043, eid='D_20')
d_21a = Drift(l=0.0432, eid='D_21')
d_23a = Drift(l=0.085, eid='D_23')
id_32151375_ = Drift(l=0.6789999999999999, eid='ID_32151375_')
d_26a = Drift(l=0.1282, eid='D_26')
d_28 = Drift(l=0.202, eid='D_28')
d_29 = Drift(l=0.262, eid='D_29')
id_95966272_ = Drift(l=2.8244499999999997, eid='ID_95966272_')
id_18462951_ = Drift(l=0.20765, eid='ID_18462951_')
id_94338373_ = Drift(l=0.096, eid='ID_94338373_')
id_7308930_ = Drift(l=0.33715, eid='ID_7308930_')
d_43 = Drift(l=0.08115, eid='D_43')
d_44a = Drift(l=0.051165, eid='D_44')
d_45 = Drift(l=0.100827, eid='D_45')
id_71696616_ = Drift(l=0.284415, eid='ID_71696616_')
id_19200616_ = Drift(l=0.28075, eid='ID_19200616_')
id_36806288_ = Drift(l=0.225165, eid='ID_36806288_')
d_52a = Drift(l=0.100828, eid='D_52')
id_32378225_ = Drift(l=0.13231500000000002, eid='ID_32378225_')
id_27968780_ = Drift(l=0.38964, eid='ID_27968780_')
d_57 = Drift(l=0.303, eid='D_57')
d_58 = Drift(l=0.1015, eid='D_58')
id_73735098_ = Drift(l=0.27965, eid='ID_73735098_')
d_61 = Drift(l=0.05115, eid='D_61')
d_63 = Drift(l=0.7143, eid='D_63')
id_61843027_ = Drift(l=0.75615, eid='ID_61843027_')
d_66 = Drift(l=0.175, eid='D_66')
d_67 = Drift(l=0.15, eid='D_67')
d_68 = Drift(l=0.13115, eid='D_68')
d_74 = Drift(l=0.275, eid='D_74')
d_75 = Drift(l=0.18115, eid='D_75')
d_76a = Drift(l=0.20115, eid='D_76')
d_77a = Drift(l=0.38, eid='D_77')
d_78 = Drift(l=0.28115, eid='D_78')
d_79 = Drift(l=0.62715, eid='D_79')
id_46725788_ = Drift(l=0.38515, eid='ID_46725788_')
id_62624181_ = Drift(l=0.53115, eid='ID_62624181_')
d_2b = Drift(l=0.5, eid='D_2')
d_3b = Drift(l=0.74, eid='D_3')
d_6a = Drift(l=1.45, eid='D_6')
d_7a = Drift(l=0.63115, eid='D_7')
d_8 = Drift(l=2.8623, eid='D_8')
d_9a = Drift(l=1.7623, eid='D_9')
d_10a = Drift(l=0.68115, eid='D_10')
d_13b = Drift(l=0.2, eid='D_13')
d_15 = Drift(l=0.182428, eid='D_15')
d_16b = Drift(l=5.1e-05, eid='D_16')
d_17 = Drift(l=0.135, eid='D_17')
d_18 = Drift(l=0.239432, eid='D_18')
d_19 = Drift(l=0.0751, eid='D_19')
d_21b = Drift(l=0.13494, eid='D_21')
d_22 = Drift(l=0.158616, eid='D_22')
d_23b = Drift(l=0.1325, eid='D_23')
d_24a = Drift(l=0.09865, eid='D_24')
d_25 = Drift(l=0.11615, eid='D_25')
d_26b = Drift(l=0.273615, eid='D_26')
d_30 = Drift(l=0.324432, eid='D_30')
d_31 = Drift(l=0.150051, eid='D_31')
d_33 = Drift(l=0.182429, eid='D_33')
d_39 = Drift(l=0.134939, eid='D_39')
d_44b = Drift(l=0.273616, eid='D_44')
d_48 = Drift(l=0.324431, eid='D_48')
d_49 = Drift(l=0.150052, eid='D_49')
d_52b = Drift(l=5.2e-05, eid='D_52')
d_54 = Drift(l=0.239431, eid='D_54')
d_76b = Drift(l=8e-06, eid='D_76')
d_77b = Drift(l=0.158608, eid='D_77')
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
d_143 = Drift(l=0.34589999999999743, eid='D_143')
d_146 = Drift(l=0.345901, eid='D_146')
d_147 = Drift(l=0.247499, eid='D_147')
d_148 = Drift(l=0.043201, eid='D_148')
d_149 = Drift(l=0.084999, eid='D_149')
id_82567243_ = Drift(l=0.679501, eid='ID_82567243_')
d_155 = Drift(l=0.3459000000000091, eid='D_155')
d_159a = Drift(l=0.2475, eid='D_159')
d_161 = Drift(l=0.085001, eid='D_161')
id_85517094_ = Drift(l=0.679499, eid='ID_85517094_')
d_167a = Drift(l=0.34590000000001164, eid='D_167')
d_172a = Drift(l=0.043199, eid='D_172')
id_36296974_ = Drift(l=0.6795009999999999, eid='ID_36296974_')
id_70317273_ = Drift(l=5.501900000000001, eid='ID_70317273_')
d_191a = Drift(l=0.15215, eid='D_191')
d_192a = Drift(l=0.082149, eid='D_192')
id_78014327_ = Drift(l=1.215001, eid='ID_78014327_')
id_45736562_ = Drift(l=1.613, eid='ID_45736562_')
d_199a = Drift(l=0.15265, eid='D_199')
d_200a = Drift(l=0.131649, eid='D_200')
id_33800950_ = Drift(l=0.88165, eid='ID_33800950_')
d_204 = Drift(l=0.10165, eid='D_204')
id_17795282_ = Drift(l=0.4515, eid='ID_17795282_')
id_98284636_ = Drift(l=0.3285, eid='ID_98284636_')
d_210a = Drift(l=0.100105, eid='D_210')
d_211a = Drift(l=8.510829, eid='D_211')
d_212a = Drift(l=0.000104, eid='D_212')
id_83151514_ = Drift(l=0.635104, eid='ID_83151514_')
id_13055336_ = Drift(l=8.510725, eid='ID_13055336_')
id_54429047_ = Drift(l=0.579, eid='ID_54429047_')
id_1463922_ = Drift(l=0.4508, eid='ID_1463922_')
d_226a = Drift(l=0.1542, eid='D_226')
d_227a = Drift(l=0.09715, eid='D_227')
id_36362924_ = Drift(l=0.66515, eid='ID_36362924_')
id_76253336_ = Drift(l=1.15915, eid='ID_76253336_')
d_236 = Drift(l=0.15315, eid='D_236')
d_243 = Drift(l=0.379, eid='D_243')
d_245a = Drift(l=0.13165, eid='D_245')
d_246a = Drift(l=1.03115, eid='D_246')
d_247a = Drift(l=1.23015, eid='D_247')
d_248a = Drift(l=0.18, eid='D_248')
id_30815182_ = Drift(l=1.329, eid='ID_30815182_')
d_256 = Drift(l=1.066, eid='D_256')
d_257a = Drift(l=0.147, eid='D_257')
d_259a = Drift(l=0.83115, eid='D_259')
id_53584452_ = Drift(l=0.6990000000000001, eid='ID_53584452_')
d_263a = Drift(l=0.13265, eid='D_263')
id_53716454_ = Drift(l=1.51065, eid='ID_53716454_')
d_267 = Drift(l=0.10765, eid='D_267')
id_4929001_ = Drift(l=1.303, eid='ID_4929001_')
d_272 = Drift(l=0.18165, eid='D_272')
id_32207144_ = Drift(l=0.89615, eid='ID_32207144_')
d_277 = Drift(l=1.22815, eid='D_277')
d_278 = Drift(l=0.152151, eid='D_278')
d_279 = Drift(l=0.081151, eid='D_279')
id_65131257_ = Drift(l=1.4944009999999999, eid='ID_65131257_')
d_2c = Drift(l=0.75275, eid='D_2')
d_3c = Drift(l=1.949996, eid='D_3')
d_4b = Drift(l=0.03165, eid='D_4')
d_5a = Drift(l=0.11165, eid='D_5')
d_6b = Drift(l=0.30165, eid='D_6')
d_7b = Drift(l=0.12165, eid='D_7')
d_9b = Drift(l=0.14165, eid='D_9')
d_11a = Drift(l=1.415, eid='D_11')
d_12b = Drift(l=3.35, eid='D_12')
d_13c = Drift(l=0.2216, eid='D_13')
d_24b = Drift(l=0.4579, eid='D_24')
d_157 = Drift(l=3.25, eid='D_157')
d_159b = Drift(l=0.37888, eid='D_159')
d_160 = Drift(l=0.15277, eid='D_160')
d_162 = Drift(l=0.30008, eid='D_162')
d_163 = Drift(l=0.32755, eid='D_163')
d_164 = Drift(l=0.13567, eid='D_164')
d_165 = Drift(l=1.05, eid='D_165')
d_167b = Drift(l=0.28888, eid='D_167')
d_168 = Drift(l=0.34, eid='D_168')
d_170 = Drift(l=0.10065, eid='D_170')
d_171 = Drift(l=0.29188, eid='D_171')
d_172b = Drift(l=0.27077, eid='D_172')
d_173 = Drift(l=0.08163, eid='D_173')
d_174 = Drift(l=0.3439, eid='D_174')
d_175 = Drift(l=0.194, eid='D_175')
d_176 = Drift(l=0.1565, eid='D_176')
d_178 = Drift(l=0.15962, eid='D_178')
d_179 = Drift(l=0.3, eid='D_179')
d_180 = Drift(l=0.100073, eid='D_180')
d_181 = Drift(l=8.507518, eid='D_181')
d_182 = Drift(l=7.2e-05, eid='D_182')
d_184 = Drift(l=0.31, eid='D_184')
d_185 = Drift(l=0.325073, eid='D_185')
d_187 = Drift(l=1.053189, eid='D_187')
d_188 = Drift(l=7.454257, eid='D_188')
d_191b = Drift(l=0.17, eid='D_191')
d_192b = Drift(l=0.15198, eid='D_192')
d_195 = Drift(l=0.46415, eid='D_195')
d_196 = Drift(l=0.14465, eid='D_196')
d_197 = Drift(l=0.15002, eid='D_197')
d_198 = Drift(l=0.34888, eid='D_198')
d_199b = Drift(l=0.58277, eid='D_199')
d_200b = Drift(l=0.78165, eid='D_200')
d_202 = Drift(l=0.17888, eid='D_202')
d_205 = Drift(l=4.0, eid='D_205')
d_206 = Drift(l=2.39998, eid='D_206')
d_207 = Drift(l=0.17165, eid='D_207')
d_208 = Drift(l=0.19165, eid='D_208')
d_209 = Drift(l=0.3899, eid='D_209')
d_210b = Drift(l=0.247, eid='D_210')
d_211b = Drift(l=0.43477, eid='D_211')
d_212b = Drift(l=0.09165, eid='D_212')
d_214 = Drift(l=0.09428, eid='D_214')
d_216 = Drift(l=0.17835, eid='D_216')
d_217 = Drift(l=0.09065, eid='D_217')
d_218 = Drift(l=0.3223, eid='D_218')
d_219 = Drift(l=0.17772, eid='D_219')
d_221 = Drift(l=1.53165, eid='D_221')
d_223 = Drift(l=2.23165, eid='D_223')
d_226b = Drift(l=1.44988, eid='D_226')
d_227b = Drift(l=1.629, eid='D_227')
d_230 = Drift(l=0.9, eid='D_230')
d_232 = Drift(l=2.07888, eid='D_232')
d_234 = Drift(l=1.78153, eid='D_234')
d_235 = Drift(l=0.35012, eid='D_235')
d_237 = Drift(l=0.35, eid='D_237')
d_238 = Drift(l=0.62888, eid='D_238')
d_241 = Drift(l=1.54988, eid='D_241')
d_242 = Drift(l=1.35012, eid='D_242')
d_244 = Drift(l=0.10488, eid='D_244')
d_245b = Drift(l=0.15285, eid='D_245')
d_246b = Drift(l=1.75545, eid='D_246')
d_247b = Drift(l=0.3501, eid='D_247')
d_248b = Drift(l=1.1789, eid='D_248')
d_253 = Drift(l=1.24988, eid='D_253')
d_257b = Drift(l=1.1, eid='D_257')
d_259b = Drift(l=0.24988, eid='D_259')
d_260 = Drift(l=1.079, eid='D_260')
d_261 = Drift(l=0.15275, eid='D_261')
d_262 = Drift(l=0.37055, eid='D_262')
d_263b = Drift(l=0.46112, eid='D_263')
d_264 = Drift(l=0.33165, eid='D_264')
d_215 = Drift(l=0.4, eid='D_215')
d_2d = Drift(l=0.00145, eid='D_2')
d_3d = Drift(l=0.58145, eid='D_3')
d_4c = Drift(l=0.17395, eid='D_4')
d_5b = Drift(l=0.18395, eid='D_5')
d_6c = Drift(l=1.04372, eid='D_6')
d_7c = Drift(l=0.13628, eid='D_7')
d_10b = Drift(l=0.98395, eid='D_10')
d_11b = Drift(l=0.43628, eid='D_11')

# Quadrupoles
qln_23_i1 = Quadrupole(l=0.05, eid='QLN.23.I1')
qls_23_i1 = Quadrupole(l=0.05, tilt=0.785398163, eid='QLS.23.I1')
q_37_i1 = Quadrupole(l=0.2136, k1=-1.458023, eid='Q.37.I1')
q_38_i1 = Quadrupole(l=0.2136, k1=1.440045, eid='Q.38.I1')
qi_46_i1 = Quadrupole(l=0.2377, k1=0.2388532, eid='QI.46.I1')
qi_47_i1 = Quadrupole(l=0.2377, k1=0.1854469, eid='QI.47.I1')
qi_50_i1 = Quadrupole(l=0.2377, k1=-0.6861892, eid='QI.50.I1')
qi_52_i1 = Quadrupole(l=0.2377, k1=-0.3522076140008414, eid='QI.52.I1')
qi_53_i1 = Quadrupole(l=0.2377, k1=2.104794185999159, eid='QI.53.I1')
qi_54_i1 = Quadrupole(l=0.2377, k1=0.7943661063020614, eid='QI.54.I1')
qi_55_i1 = Quadrupole(l=0.2377, k1=-2.6383360780016827, eid='QI.55.I1')
qi_57_i1 = Quadrupole(l=0.2377, k1=3.2780620240008416, eid='QI.57.I1')
qi_59_i1 = Quadrupole(l=0.2377, k1=-2.6383360780016827, eid='QI.59.I1')
qi_60_i1 = Quadrupole(l=0.2377, k1=1.9778194619983174, eid='QI.60.I1')
qi_61_i1 = Quadrupole(l=0.2377, k1=0.8708619870004207, eid='QI.61.I1')
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
qd_387_b2 = Quadrupole(l=0.2367, k1=0.2720532319391635, eid='QD.387.B2')
qd_388_b2 = Quadrupole(l=0.2367, k1=0.52, eid='QD.388.B2')
qd_391_b2 = Quadrupole(l=0.2367, k1=-0.7685044359949303, eid='QD.391.B2')
qd_392_b2 = Quadrupole(l=0.2367, k1=0.1332995352767216, eid='QD.392.B2')
qd_415_b2 = Quadrupole(l=0.2367, k1=0.07743979721166033, eid='QD.415.B2')
qd_417_b2 = Quadrupole(l=0.2367, k1=-0.7945923109421208, eid='QD.417.B2')
qd_418_b2 = Quadrupole(l=0.2367, k1=0.6150739332488382, eid='QD.418.B2')
qd_425_b2 = Quadrupole(l=0.2367, k1=-1.2299831009716942, eid='QD.425.B2')
qd_427_b2 = Quadrupole(l=0.2367, k1=0.9042923531896916, eid='QD.427.B2')
qd_431_b2 = Quadrupole(l=0.2367, k1=0.6878918462188425, eid='QD.431.B2')
qd_434_b2 = Quadrupole(l=0.2367, k1=-0.9532108153781158, eid='QD.434.B2')
qd_437_b2 = Quadrupole(l=0.2367, k1=0.20036332910857627, eid='QD.437.B2')
qd_440_b2 = Quadrupole(l=0.2367, k1=-0.578403041825095, eid='QD.440.B2')
qd_444_b2 = Quadrupole(l=0.2367, k1=-0.8139121250528094, eid='QD.444.B2')
qd_448_b2 = Quadrupole(l=0.2367, k1=0.8960963244613435, eid='QD.448.B2')
qd_452_b2 = Quadrupole(l=0.2367, k1=-1.2632826362484157, eid='QD.452.B2')
qd_456_b2 = Quadrupole(l=0.2367, k1=0.8960963244613435, eid='QD.456.B2')
qd_459_b2 = Quadrupole(l=0.2367, k1=-0.601, eid='QD.459.B2')
qd_463_b2 = Quadrupole(l=0.2367, k1=1.3346, eid='QD.463.B2')
qd_464_b2 = Quadrupole(l=0.2367, k1=0.7416, eid='QD.464.B2')
qd_465_b2 = Quadrupole(l=0.2367, k1=-1.7783, eid='QD.465.B2')
qf_469_b2d = Quadrupole(l=0.5321, eid='QF.469.B2D')
qe_471_b2d = Quadrupole(l=0.24, k1=2.05, eid='QE.471.B2D')
qf_472_b2d = Quadrupole(l=0.5321, k1=-0.096, eid='QF.472.B2D')

# SBends
bl_48i_i1 = SBend(l=0.2, angle=-0.099484, e2=-0.099484, eid='BL.48I.I1')
bl_48ii_i1 = SBend(l=0.2, angle=0.099484, e1=0.099484, eid='BL.48II.I1')
bl_50i_i1 = SBend(l=0.2, angle=0.099484, e2=0.099484, eid='BL.50I.I1')
bl_50ii_i1 = SBend(l=0.2, angle=-0.099484, e1=-0.099484, eid='BL.50II.I1')
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
bb_393_b2 = SBend(l=0.5, angle=0.04163879892, e2=0.041638799, tilt=1.570796327, eid='BB.393.B2')
bb_402_b2 = SBend(l=0.5, angle=-0.04163879892, e1=-0.041638799, tilt=1.570796327, eid='BB.402.B2')
bb_404_b2 = SBend(l=0.5, angle=-0.04163879892, e2=-0.041638799, tilt=1.570796327, eid='BB.404.B2')
bb_413_b2 = SBend(l=0.5, angle=0.04163879892, e1=0.041638799, tilt=1.570796327, eid='BB.413.B2')
bg_467_b2d = SBend(l=1.5971, angle=0.2094395102, tilt=1.570796327, eid='BG.467.B2D')

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
ckx_23_i1 = Hcor(l=0.025, eid='CKX.23.I1')
ckx_24_i1 = Hcor(l=0.025, eid='CKX.24.I1')
ckx_25_i1 = Hcor(l=0.025, eid='CKX.25.I1')
cx_37_i1 = Hcor(eid='CX.37.I1')
cx_39_i1 = Hcor(eid='CX.39.I1')
cwx_47_i1 = Hcor(eid='CWX.47.I1')
cix_51_i1 = Hcor(l=0.1, eid='CIX.51.I1')
cix_57_i1 = Hcor(l=0.1, eid='CIX.57.I1')
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
cfx_470_b2d = Hcor(l=0.1, eid='CFX.470.B2D')

# Vcors
cky_23_i1 = Vcor(l=0.025, eid='CKY.23.I1')
cky_24_i1 = Vcor(l=0.025, eid='CKY.24.I1')
cky_25_i1 = Vcor(l=0.025, eid='CKY.25.I1')
cy_37_i1 = Vcor(eid='CY.37.I1')
cy_39_i1 = Vcor(eid='CY.39.I1')
cwy_47_i1 = Vcor(eid='CWY.47.I1')
ciy_51_i1 = Vcor(l=0.1, eid='CIY.51.I1')
ciy_55_i1 = Vcor(l=0.1, eid='CIY.55.I1')
ciy_58_i1 = Vcor(l=0.1, eid='CIY.58.I1')
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
cfy_468_b2d = Vcor(l=0.1, eid='CFY.468.B2D')
cfy_471_b2d = Vcor(l=0.1, eid='CFY.471.B2D')

# Undulators
u74_49_i1 = Undulator(lperiod=0.074, nperiods=12.405405405405407, Kx=1.294, eid='U74.49.I1')

# Cavitys
c_a1_1_1_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.1.I1')
c_a1_1_2_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.2.I1')
c_a1_1_3_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.3.I1')
c_a1_1_4_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.4.I1')
c_a1_1_5_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.5.I1')
c_a1_1_6_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.6.I1')
c_a1_1_7_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.7.I1')
c_a1_1_8_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.8.I1')
c3_ah1_1_1_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.1.I1')
c3_ah1_1_2_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.2.I1')
c3_ah1_1_3_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.3.I1')
c3_ah1_1_4_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.4.I1')
c3_ah1_1_5_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.5.I1')
c3_ah1_1_6_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.6.I1')
c3_ah1_1_7_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.7.I1')
c3_ah1_1_8_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.8.I1')
tdsa_52_i1 = TDCavity(l=0.7, freq=3000000000.0, eid='TDSA.52.I1')
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
tdsb_208_b1 = TDCavity(l=1.5, freq=3000000000.0, eid='TDSB.208.B1')
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

# TDCavitys
tdsb_428_b2 = TDCavity(l=1.5, freq=3000000000.0, eid='TDSB.428.B2')
tdsb_430_b2 = TDCavity(l=1.5, freq=3000000000.0, eid='TDSB.430.B2')

# Solenoids
solb_23_i1 = Solenoid(eid='SOLB.23.I1')

# Monitors
bpmg_24_i1 = Monitor(eid='BPMG.24.I1')
bpmg_25i_i1 = Monitor(eid='BPMG.25I.I1')
bpmc_38i_i1 = Monitor(eid='BPMC.38I.I1')
bpmr_38ii_i1 = Monitor(eid='BPMR.38II.I1')
bpmf_47_i1 = Monitor(eid='BPMF.47.I1')
bpmf_48_i1 = Monitor(eid='BPMF.48.I1')
bpmf_52_i1 = Monitor(eid='BPMF.52.I1')
bpma_55_i1 = Monitor(eid='BPMA.55.I1')
bpma_57_i1 = Monitor(eid='BPMA.57.I1')
bpma_59_i1 = Monitor(eid='BPMA.59.I1')
bpma_60_i1 = Monitor(eid='BPMA.60.I1')
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
bpma_469_b2d = Monitor(eid='BPMA.469.B2D')
bpma_471_b2d = Monitor(eid='BPMA.471.B2D')

# Markers
stsec_23_i1 = Marker(eid='STSEC.23.I1')
start_sim = Marker(eid='START_SIM')
id_30058415_ = Marker(eid='ID_30058415_')
id_9649943_ = Marker(eid='ID_9649943_')
match_37_i1 = Marker(eid='MATCH.37.I1')
stlat_47_i1 = Marker(eid='STLAT.47.I1')
id_28650742_ = Marker(eid='ID_28650742_')
id_97588526_ = Marker(eid='ID_97588526_')
match_52_i1 = Marker(eid='MATCH.52.I1')
id_82967176_ = Marker(eid='ID_82967176_')
id_48693585_ = Marker(eid='ID_48693585_')
match_55_i1 = Marker(eid='MATCH.55.I1')
otrc_55_i1 = Marker(eid='OTRC.55.I1')
otrc_56_i1 = Marker(eid='OTRC.56.I1')
otrc_58_i1 = Marker(eid='OTRC.58.I1')
otrc_59_i1 = Marker(eid='OTRC.59.I1')
stsub_62_i1 = Marker(eid='STSUB.62.I1')
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
stsub_229_b1 = Marker(eid='STSUB.229.B1')
stgrd_231_b1 = Marker(eid='STGRD.231.B1')
enblock_233_b1 = Marker(eid='ENBLOCK.233.B1')
engrd_233_b1 = Marker(eid='ENGRD.233.B1')
ensub_235_b1 = Marker(eid='ENSUB.235.B1')
ensec_235_b1 = Marker(eid='ENSEC.235.B1')
stsec_235_l2 = Marker(eid='STSEC.235.L2')
stac_238_l2 = Marker(eid='STAC.238.L2')
enac_250_l2 = Marker(eid='ENAC.250.L2')
stac_250_l2 = Marker(eid='STAC.250.L2')
enac_262_l2 = Marker(eid='ENAC.262.L2')
stac_262_l2 = Marker(eid='STAC.262.L2')
enac_274_l2 = Marker(eid='ENAC.274.L2')
stac_274_l2 = Marker(eid='STAC.274.L2')
enac_286_l2 = Marker(eid='ENAC.286.L2')
stac_286_l2 = Marker(eid='STAC.286.L2')
enac_298_l2 = Marker(eid='ENAC.298.L2')
stac_298_l2 = Marker(eid='STAC.298.L2')
enac_310_l2 = Marker(eid='ENAC.310.L2')
mid_310_l2 = Marker(eid='MID.310.L2')
stac_310_l2 = Marker(eid='STAC.310.L2')
enac_322_l2 = Marker(eid='ENAC.322.L2')
stac_322_l2 = Marker(eid='STAC.322.L2')
enac_334_l2 = Marker(eid='ENAC.334.L2')
stac_334_l2 = Marker(eid='STAC.334.L2')
enac_346_l2 = Marker(eid='ENAC.346.L2')
stac_346_l2 = Marker(eid='STAC.346.L2')
enac_358_l2 = Marker(eid='ENAC.358.L2')
stac_358_l2 = Marker(eid='STAC.358.L2')
enac_370_l2 = Marker(eid='ENAC.370.L2')
stac_370_l2 = Marker(eid='STAC.370.L2')
enac_382_l2 = Marker(eid='ENAC.382.L2')
ensec_385_l2 = Marker(eid='ENSEC.385.L2')
stsec_385_b2 = Marker(eid='STSEC.385.B2')
stsub_385_b2 = Marker(eid='STSUB.385.B2')
match_385_b2 = Marker(eid='MATCH.385.B2')
stgrd_386_b2 = Marker(eid='STGRD.386.B2')
dcm_388_b2 = Marker(eid='DCM.388.B2')
engrd_390_b2 = Marker(eid='ENGRD.390.B2')
stgrd_390_b2 = Marker(eid='STGRD.390.B2')
eod_390_b2 = Marker(eid='EOD.390.B2')
bcm_391_b2 = Marker(eid='BCM.391.B2')
otra_392_b2 = Marker(eid='OTRA.392.B2')
bam_392_b2 = Marker(eid='BAM.392.B2')
midbpmf_393_b2 = Marker(eid='MIDBPMF.393.B2')
engrd_393_b2 = Marker(eid='ENGRD.393.B2')
stlat_393_b2 = Marker(eid='STLAT.393.B2')
otrs_404_b2 = Marker(eid='OTRS.404.B2')
srm_406_b2 = Marker(eid='SRM.406.B2')
match_414_b2 = Marker(eid='MATCH.414.B2')
enlat_414_b2 = Marker(eid='ENLAT.414.B2')
stlat_414_b2 = Marker(eid='STLAT.414.B2')
stgrd_414_b2 = Marker(eid='STGRD.414.B2')
bam_414_b2 = Marker(eid='BAM.414.B2')
midbpmf_414_b2 = Marker(eid='MIDBPMF.414.B2')
tora_415_b2 = Marker(eid='TORA.415.B2')
bcm_416_b2 = Marker(eid='BCM.416.B2')
engrd_419_b2 = Marker(eid='ENGRD.419.B2')
stgrd_423_b2 = Marker(eid='STGRD.423.B2')
otra_426_b2 = Marker(eid='OTRA.426.B2')
engrd_427_b2 = Marker(eid='ENGRD.427.B2')
stgrd_427_b2 = Marker(eid='STGRD.427.B2')
stblock_428_b2 = Marker(eid='STBLOCK.428.B2')
match_428_b2 = Marker(eid='MATCH.428.B2')
marker_tds_b2 = Marker(eid='MARKER.TDS.B2')
engrd_432_b2 = Marker(eid='ENGRD.432.B2')
stgrd_432_b2 = Marker(eid='STGRD.432.B2')
engrd_437_b2 = Marker(eid='ENGRD.437.B2')
stgrd_437_b2 = Marker(eid='STGRD.437.B2')
otra_438_b2 = Marker(eid='OTRA.438.B2')
engrd_442_b2 = Marker(eid='ENGRD.442.B2')
stgrd_442_b2 = Marker(eid='STGRD.442.B2')
match_446_b2 = Marker(eid='MATCH.446.B2')
otra_446_b2 = Marker(eid='OTRA.446.B2')
engrd_446_b2 = Marker(eid='ENGRD.446.B2')
stgrd_447_b2 = Marker(eid='STGRD.447.B2')
otrb_450_b2 = Marker(eid='OTRB.450.B2')
engrd_451_b2 = Marker(eid='ENGRD.451.B2')
stgrd_451_b2 = Marker(eid='STGRD.451.B2')
otrb_454_b2 = Marker(eid='OTRB.454.B2')
engrd_456_b2 = Marker(eid='ENGRD.456.B2')
stgrd_456_b2 = Marker(eid='STGRD.456.B2')
otrb_457_b2 = Marker(eid='OTRB.457.B2')
engrd_461_b2 = Marker(eid='ENGRD.461.B2')
stgrd_461_b2 = Marker(eid='STGRD.461.B2')
otrb_461_b2 = Marker(eid='OTRB.461.B2')
crd_463_b2 = Marker(eid='CRD.463.B2')
engrd_466_b2 = Marker(eid='ENGRD.466.B2')
enlat_466_b2 = Marker(eid='ENLAT.466.B2')
ensub_466_b2 = Marker(eid='ENSUB.466.B2')
otra_473_b2d = Marker(eid='OTRA.473.B2D')

# Lattice 
cell = (stsec_23_i1, id_97509745_, solb_23_i1, qln_23_i1, qls_23_i1, d_2a, ckx_23_i1, cky_23_i1, d_3a, 
ckx_24_i1, cky_24_i1, d_4a, bpmg_24_i1, id_70110258_, bpmg_25i_i1, id_41101705_, ckx_25_i1, cky_25_i1, d_12a, 
start_sim, id_35969356_, c_a1_1_1_i1, id_30058415_, d_13a, c_a1_1_2_i1, d_13a, c_a1_1_3_i1, d_13a, c_a1_1_4_i1, 
d_16a, c_a1_1_5_i1, d_13a, c_a1_1_6_i1, d_13a, c_a1_1_7_i1, d_13a, c_a1_1_8_i1, id_9649943_, d_20, 
match_37_i1, d_21a, q_37_i1, d_21a, cx_37_i1, cy_37_i1, d_23a, bpmc_38i_i1, id_32151375_, bpmr_38ii_i1, 
d_26a, q_38_i1, d_21a, cx_39_i1, cy_39_i1, d_28, c3_ah1_1_1_i1, d_29, c3_ah1_1_2_i1, d_29, 
c3_ah1_1_3_i1, d_29, c3_ah1_1_4_i1, d_29, c3_ah1_1_5_i1, d_29, c3_ah1_1_6_i1, d_29, c3_ah1_1_7_i1, d_29, 
c3_ah1_1_8_i1, id_95966272_, qi_46_i1, id_18462951_, bpmf_47_i1, id_94338373_, cwx_47_i1, cwy_47_i1, id_7308930_, qi_47_i1, 
d_43, stlat_47_i1, d_44a, bl_48i_i1, d_45, bl_48ii_i1, id_71696616_, bpmf_48_i1, id_19200616_, id_28650742_, 
u74_49_i1, id_97588526_, id_36806288_, bl_50i_i1, d_52a, bl_50ii_i1, id_32378225_, qi_50_i1, id_27968780_, ciy_51_i1, 
d_57, cix_51_i1, d_58, bpmf_52_i1, id_73735098_, match_52_i1, qi_52_i1, d_61, id_82967176_, tdsa_52_i1, 
id_48693585_, d_61, qi_53_i1, d_63, qi_54_i1, id_61843027_, match_55_i1, otrc_55_i1, d_66, ciy_55_i1, 
d_67, bpma_55_i1, d_68, qi_55_i1, id_61843027_, otrc_56_i1, d_66, cix_57_i1, d_67, bpma_57_i1, 
d_68, qi_57_i1, id_61843027_, otrc_58_i1, d_74, ciy_58_i1, d_75, qi_59_i1, d_76a, bpma_59_i1, 
d_77a, otrc_59_i1, d_78, qi_60_i1, d_79, bpma_60_i1, id_46725788_, qi_61_i1, id_62624181_, stsub_62_i1, 
d_2b, cbb_62_i1d, d_3b, ciy_63_i1, d_43, qi_63_i1, d_68, bpma_63_i1, d_6a, cix_65_i1, 
d_7a, qi_66_i1, d_8, qi_69_i1, d_9a, qi_71_i1, d_10a, bpma_72_i1, d_75, qi_72_i1, 
d_75, ciy_72_i1, d_13b, cix_73i_i1, d_43, stlat_73_i1, match_73_i1, qi_73_i1, d_15, bl_73_i1, 
d_16b, cbl_73_i1, d_17, cix_73ii_i1, d_18, sc_74i_i1, d_19, qi_74_i1, d_19, sc_74ii_i1, 
d_21b, bl_75_i1, d_22, bpma_75_i1, d_23b, ciy_75_i1, d_24a, qi_75_i1, d_25, cix_76_i1, 
d_26b, bl_76_i1, d_21b, sc_76_i1, d_19, qi_77_i1, d_19, sc_77_i1, d_30, bpma_77_i1, 
d_31, bl_77_i1, d_15, qi_78_i1, d_33, bl_78_i1, d_16b, cbl_78_i1, d_17, cix_78_i1, 
d_18, sc_79i_i1, d_19, qi_79_i1, d_19, sc_79ii_i1, d_39, bl_80_i1, d_22, bpma_80_i1, 
d_23b, ciy_80_i1, d_24a, qi_80_i1, d_25, cix_81_i1, d_44b, bl_81_i1, d_21b, sc_81_i1, 
d_19, qi_82_i1, d_19, sc_82_i1, d_48, bpma_82_i1, d_49, bl_82_i1, d_15, qi_83_i1, 
d_15, bl_83_i1, d_52b, cbl_83_i1, d_17, cix_83_i1, d_54, sc_84i_i1, d_19, qi_84_i1, 
d_19, sc_84ii_i1, d_21b, bl_85_i1, d_22, bpma_85_i1, d_23b, ciy_85_i1, d_24a, qi_85_i1, 
d_25, cix_86_i1, d_44b, bl_86_i1, d_39, sc_86_i1, d_19, qi_86_i1, d_19, sc_87_i1, 
d_30, bpma_87_i1, d_49, bl_87_i1, d_15, qi_88_i1, d_15, bl_88_i1, d_16b, cbl_88_i1, 
d_17, cix_88_i1, d_18, sc_89i_i1, d_19, qi_89_i1, d_19, sc_89ii_i1, d_39, bl_90_i1, 
d_76b, cbl_90_i1, d_77b, bpma_90_i1, d_23b, cix_90_i1, d_24a, qi_90_i1, d_80, bl_91_i1, 
d_21b, sc_91_i1, d_19, qi_92_i1, d_19, sc_92_i1, d_84, ciy_92_i1, d_23b, bpma_92_i1, 
d_31, bl_92_i1, d_15, qi_93_i1, id_30609505_, ciy_94_i1, d_90, qi_94_i1, id_7554339_, bpmf_95_i1, 
d_93, cix_95_i1, d_90, qi_95_i1, d_95, stlat_96_i1, d_96, bb_96_i1, d_97, bb_98_i1, 
d_98, cbb_98_i1, d_99, bpms_99_i1, id_79103439_, bb_100_i1, d_98, cbb_100_i1, d_103, bb_101_i1, 
d_104, cbb_101_i1, d_105, enlat_101_i1, d_106, qi_102_i1, d_90, cix_102_i1, id_14888141_, bpmf_103_i1, 
d_110, ciy_103_i1, d_90, qi_103_i1, d_75, bpma_103_i1, d_113, cix_104_i1, d_90, qi_104_i1, 
stlat_104_i1, match_104_i1, d_75, bpma_105_i1, d_116, ciy_107_i1, d_90, qi_107_i1, d_75, bpma_107_i1, 
d_116, cix_109_i1, d_90, qi_109_i1, d_75, bpma_110_i1, d_116, ciy_112_i1, d_90, qi_112_i1, 
d_75, bpma_112_i1, id_34013725_, cix_114_i1, d_90, qi_114_i1, d_75, bpma_115_i1, id_28166788_, ciy_116_i1, 
d_90, qi_116_i1, d_131, bpma_117_i1, id_50015017_, cix_118_i1, d_90, qi_118_i1, d_136, bpma_119_i1, 
id_70254102_, c_a2_1_1_l1, d_140, c_a2_1_2_l1, d_13a, c_a2_1_3_l1, d_13a, c_a2_1_4_l1, d_143, c_a2_1_5_l1, 
d_13a, c_a2_1_6_l1, d_13a, c_a2_1_7_l1, d_146, c_a2_1_8_l1, d_147, q_134_l1, d_148, cx_134_l1, 
cy_134_l1, d_149, bpmc_134_l1, id_82567243_, c_a2_2_1_l1, d_13a, c_a2_2_2_l1, d_13a, c_a2_2_3_l1, d_13a, 
c_a2_2_4_l1, d_155, c_a2_2_5_l1, d_140, c_a2_2_6_l1, d_13a, c_a2_2_7_l1, d_13a, c_a2_2_8_l1, d_159a, 
q_146_l1, d_21a, cx_146_l1, cy_146_l1, d_161, bpmr_146_l1, id_85517094_, c_a2_3_1_l1, d_13a, c_a2_3_2_l1, 
d_13a, c_a2_3_3_l1, d_146, c_a2_3_4_l1, d_167a, c_a2_3_5_l1, d_13a, c_a2_3_6_l1, d_13a, c_a2_3_7_l1, 
d_13a, c_a2_3_8_l1, d_159a, q_158_l1, d_172a, cx_158_l1, cy_158_l1, d_23a, bpmc_158_l1, id_36296974_, 
c_a2_4_1_l1, d_13a, c_a2_4_2_l1, d_13a, c_a2_4_3_l1, d_13a, c_a2_4_4_l1, d_167a, c_a2_4_5_l1, d_13a, 
c_a2_4_6_l1, d_13a, c_a2_4_7_l1, d_13a, c_a2_4_8_l1, d_147, q_170_l1, d_21a, cx_170_l1, cy_170_l1, 
d_161, bpmr_170_l1, id_70317273_, bpma_175_b1, d_191a, qi_176_b1, d_192a, ciy_176_b1, id_78014327_, cix_177_b1, 
id_45736562_, bpma_179_b1, d_199a, qd_179_b1, d_200a, ccx_179_b1, id_33800950_, qd_181_b1, d_204, ccy_181_b1, 
id_17795282_, bpmf_181_b1, id_98284636_, stlat_182_b1, d_210a, bb_182_b1, d_211a, bb_191_b1, d_212a, cbb_191_b1, 
d_99, bpms_192_b1, id_83151514_, bb_193_b1, d_212a, cbb_193_b1, id_13055336_, bb_202_b1, d_212a, cbb_202_b1, 
d_105, match_202_b1, id_54429047_, bpmf_203_b1, id_1463922_, tora_203_b1, d_226a, ciy_204_b1, d_227a, qi_204_b1, 
id_36362924_, cix_205_b1, d_227a, qi_205_b1, id_76253336_, bpma_206_b1, d_236, qi_206_b1, d_43, match_207_b1, 
d_105, tdsb_208_b1, d_75, qi_209_b1, id_62624181_, cix_209_b1, d_243, bpma_210_b1, d_199a, qd_210_b1, 
d_245a, ccy_210_b1, d_246a, qi_211_b1, d_247a, cix_213_b1, d_248a, bpma_213_b1, d_191a, qi_213_b1, 
d_43, ciy_214_b1, id_30815182_, bpma_215_b1, d_191a, qi_215_b1, d_227a, cix_216_b1, d_256, ccy_217_b1, 
d_257a, bpma_217_b1, d_191a, qi_217_b1, d_259a, match_218_b1, id_53584452_, bpma_219_b1, d_263a, qd_219_b1, 
id_53716454_, bpma_221_b1, d_199a, qd_221_b1, d_267, ccy_221_b1, id_4929001_, bpma_223_b1, d_199a, qd_223_b1, 
d_272, cfx_223_b1, id_32207144_, qi_224_b1, d_277, bpma_226_b1, d_278, qi_226_b1, d_279, ciy_226_b1, 
d_67, cfx_226_b1, d_248a, bpma_227_b1, d_278, qi_227_b1, id_65131257_, ensub_229_b1, stsub_229_b1, d_2c, 
cbb_229_b1d, d_3c, stgrd_231_b1, d_4b, qd_231_b1, d_5a, ccx_232_b1, d_6b, qd_232_b1, d_7b, 
ccy_232_b1, d_67, bpma_233_b1, d_9b, qd_233_b1, d_245a, enblock_233_b1, engrd_233_b1, d_11a, ensub_235_b1, 
ensec_235_b1, stsec_235_l2, d_12b, stac_238_l2, d_13c, c_a3_1_1_l2, d_13a, c_a3_1_2_l2, d_13a, c_a3_1_3_l2, 
d_13a, c_a3_1_4_l2, d_167a, c_a3_1_5_l2, d_13a, c_a3_1_6_l2, d_13a, c_a3_1_7_l2, d_13a, c_a3_1_8_l2, 
d_159a, q_249_l2, d_21a, cx_249_l2, d_23a, bpmc_249_l2, d_24b, enac_250_l2, stac_250_l2, d_13c, 
c_a3_2_1_l2, d_13a, c_a3_2_2_l2, d_13a, c_a3_2_3_l2, d_13a, c_a3_2_4_l2, d_167a, c_a3_2_5_l2, d_13a, 
c_a3_2_6_l2, d_13a, c_a3_2_7_l2, d_13a, c_a3_2_8_l2, d_159a, q_261_l2, d_21a, cy_261_l2, d_23a, 
bpmc_261_l2, d_24b, enac_262_l2, stac_262_l2, d_13c, c_a3_3_1_l2, d_13a, c_a3_3_2_l2, d_13a, c_a3_3_3_l2, 
d_13a, c_a3_3_4_l2, d_167a, c_a3_3_5_l2, d_13a, c_a3_3_6_l2, d_13a, c_a3_3_7_l2, d_13a, c_a3_3_8_l2, 
d_159a, q_273_l2, d_21a, cx_273_l2, d_23a, bpmr_273_l2, d_24b, enac_274_l2, stac_274_l2, d_13c, 
c_a3_4_1_l2, d_13a, c_a3_4_2_l2, d_13a, c_a3_4_3_l2, d_13a, c_a3_4_4_l2, d_167a, c_a3_4_5_l2, d_13a, 
c_a3_4_6_l2, d_13a, c_a3_4_7_l2, d_13a, c_a3_4_8_l2, d_159a, q_285_l2, d_21a, cy_285_l2, d_23a, 
bpmr_285_l2, d_24b, enac_286_l2, stac_286_l2, d_13c, c_a4_1_1_l2, d_13a, c_a4_1_2_l2, d_13a, c_a4_1_3_l2, 
d_13a, c_a4_1_4_l2, d_167a, c_a4_1_5_l2, d_13a, c_a4_1_6_l2, d_13a, c_a4_1_7_l2, d_13a, c_a4_1_8_l2, 
d_159a, q_297_l2, d_21a, cx_297_l2, d_23a, bpmc_297_l2, d_24b, enac_298_l2, stac_298_l2, d_13c, 
c_a4_2_1_l2, d_13a, c_a4_2_2_l2, d_13a, c_a4_2_3_l2, d_13a, c_a4_2_4_l2, d_167a, c_a4_2_5_l2, d_13a, 
c_a4_2_6_l2, d_13a, c_a4_2_7_l2, d_13a, c_a4_2_8_l2, d_159a, q_309_l2, d_21a, cy_309_l2, d_23a, 
bpmr_309_l2, d_24b, enac_310_l2, mid_310_l2, stac_310_l2, d_13c, c_a4_3_1_l2, d_13a, c_a4_3_2_l2, d_13a, 
c_a4_3_3_l2, d_13a, c_a4_3_4_l2, d_167a, c_a4_3_5_l2, d_13a, c_a4_3_6_l2, d_13a, c_a4_3_7_l2, d_13a, 
c_a4_3_8_l2, d_159a, q_321_l2, d_21a, cx_321_l2, d_23a, bpmc_321_l2, d_24b, enac_322_l2, stac_322_l2, 
d_13c, c_a4_4_1_l2, d_13a, c_a4_4_2_l2, d_13a, c_a4_4_3_l2, d_13a, c_a4_4_4_l2, d_167a, c_a4_4_5_l2, 
d_13a, c_a4_4_6_l2, d_13a, c_a4_4_7_l2, d_13a, c_a4_4_8_l2, d_159a, q_333_l2, d_21a, cy_333_l2, 
d_23a, bpmr_333_l2, d_24b, enac_334_l2, stac_334_l2, d_13c, c_a5_1_1_l2, d_13a, c_a5_1_2_l2, d_13a, 
c_a5_1_3_l2, d_13a, c_a5_1_4_l2, d_167a, c_a5_1_5_l2, d_13a, c_a5_1_6_l2, d_13a, c_a5_1_7_l2, d_13a, 
c_a5_1_8_l2, d_159a, q_345_l2, d_21a, cx_345_l2, d_23a, bpmc_345_l2, d_24b, enac_346_l2, stac_346_l2, 
d_13c, c_a5_2_1_l2, d_13a, c_a5_2_2_l2, d_13a, c_a5_2_3_l2, d_13a, c_a5_2_4_l2, d_167a, c_a5_2_5_l2, 
d_13a, c_a5_2_6_l2, d_13a, c_a5_2_7_l2, d_13a, c_a5_2_8_l2, d_159a, q_357_l2, d_21a, cy_357_l2, 
d_23a, bpmc_357_l2, d_24b, enac_358_l2, stac_358_l2, d_13c, c_a5_3_1_l2, d_13a, c_a5_3_2_l2, d_13a, 
c_a5_3_3_l2, d_13a, c_a5_3_4_l2, d_167a, c_a5_3_5_l2, d_13a, c_a5_3_6_l2, d_13a, c_a5_3_7_l2, d_13a, 
c_a5_3_8_l2, d_159a, q_369_l2, d_21a, cx_369_l2, d_23a, bpmr_369_l2, d_24b, enac_370_l2, stac_370_l2, 
d_13c, c_a5_4_1_l2, d_13a, c_a5_4_2_l2, d_13a, c_a5_4_3_l2, d_13a, c_a5_4_4_l2, d_167a, c_a5_4_5_l2, 
d_13a, c_a5_4_6_l2, d_13a, c_a5_4_7_l2, d_13a, c_a5_4_8_l2, d_159a, q_381_l2, d_21a, cy_381_l2, 
d_23a, bpmr_381_l2, d_24b, enac_382_l2, d_157, ensec_385_l2, stsec_385_b2, stsub_385_b2, match_385_b2, d_11a, 
stgrd_386_b2, d_159b, bpma_387_b2, d_160, qd_387_b2, d_245a, ccy_387_b2, d_162, dcm_388_b2, d_163, 
qd_388_b2, d_164, ccx_388_b2, d_165, engrd_390_b2, d_105, stgrd_390_b2, d_167b, eod_390_b2, d_168, 
bpma_390_b2, d_160, qd_391_b2, d_170, ccy_391_b2, d_171, bcm_391_b2, d_172b, qd_392_b2, d_173, 
ccx_392_b2, d_174, otra_392_b2, d_175, bam_392_b2, d_176, bpmf_393_b2, id_94338373_, midbpmf_393_b2, d_178, 
engrd_393_b2, d_179, stlat_393_b2, d_180, bb_393_b2, d_181, bb_402_b2, d_182, cbb_403_b2, d_99, 
bpms_404_b2, d_184, otrs_404_b2, d_185, bb_404_b2, d_182, cbb_405_b2, d_187, srm_406_b2, d_188, 
bb_413_b2, d_182, cbb_414_b2, d_105, match_414_b2, enlat_414_b2, stlat_414_b2, d_191b, stgrd_414_b2, d_192b, 
bam_414_b2, d_176, bpmf_414_b2, id_94338373_, midbpmf_414_b2, tora_415_b2, d_195, qd_415_b2, d_196, ccx_415_b2, d_197, 
ccy_416_b2, d_198, bcm_416_b2, d_199b, qd_417_b2, d_200b, ccx_418_b2, d_67, ccy_418_b2, d_202, 
bpma_418_b2, d_160, qd_418_b2, d_245a, engrd_419_b2, d_205, stgrd_423_b2, d_206, ccx_425_b2, d_207, 
qd_425_b2, d_208, ccy_426_b2, d_209, otra_426_b2, d_210b, bpma_426_b2, d_211b, qd_427_b2, d_212b, 
engrd_427_b2, d_13b, stgrd_427_b2, d_214, stblock_428_b2, match_428_b2, tdsb_428_b2, d_13b, marker_tds_b2, d_13b, 
tdsb_430_b2, d_216, qd_431_b2, d_217, ccx_431_b2, d_218, bpma_432_b2, d_219, engrd_432_b2, d_13b, 
stgrd_432_b2, d_221, qd_434_b2, d_245a, ccy_434_b2, d_223, qd_437_b2, d_245a, engrd_437_b2, d_13b, 
stgrd_437_b2, d_226b, otra_438_b2, d_227b, bpma_440_b2, d_160, qd_440_b2, d_245a, ccx_441_b2, d_230, 
engrd_442_b2, d_13b, stgrd_442_b2, d_232, bpma_444_b2, d_160, qd_444_b2, d_234, match_446_b2, otra_446_b2, 
d_235, engrd_446_b2, d_13b, stgrd_447_b2, d_237, ccx_447_b2, d_238, bpma_448_b2, d_160, qd_448_b2, 
d_245a, ccy_448_b2, d_241, otrb_450_b2, d_242, engrd_451_b2, d_13b, stgrd_451_b2, d_244, bpma_452_b2, 
d_245b, qd_452_b2, d_246b, otrb_454_b2, d_247b, ccx_454_b2, d_248b, bpma_455_b2, d_160, qd_456_b2, 
d_245a, ccx_456_b2, d_105, engrd_456_b2, d_13b, stgrd_456_b2, d_253, otrb_457_b2, d_227b, bpma_459_b2, 
d_160, qd_459_b2, d_245a, ccy_460_b2, d_257b, engrd_461_b2, d_13b, stgrd_461_b2, d_259b, otrb_461_b2, 
d_260, bpma_462_b2, d_261, qd_463_b2, d_262, crd_463_b2, d_263b, ccx_464_b2, d_264, qd_464_b2, 
d_245a, ccy_464_b2, d_237, ccx_465_b2, d_202, bpma_465_b2, d_160, qd_465_b2, d_245a, engrd_466_b2, 
d_215, enlat_466_b2, ensub_466_b2, d_2d, bg_467_b2d, d_3d, cfy_468_b2d, d_4c, qf_469_b2d, d_5b, 
bpma_469_b2d, d_6c, cfx_470_b2d, d_7c, qe_471_b2d, d_248a, bpma_471_b2d, d_13b, cfy_471_b2d, d_10b, 
qf_472_b2d, d_11b, otra_473_b2d)

# power supplies 

#  
qln_23_i1.ps_id = 'QLN.23.I1'
qls_23_i1.ps_id = 'QLS.23.I1'
q_37_i1.ps_id = 'Q.A1.1.I1'
q_38_i1.ps_id = 'Q.AH1.1.I1'
qi_46_i1.ps_id = 'QI.1.I1'
qi_47_i1.ps_id = 'QI.2.I1'
qi_50_i1.ps_id = 'QI.3.I1'
qi_52_i1.ps_id = 'QI.4.I1'
qi_53_i1.ps_id = 'QI.5.I1'
qi_54_i1.ps_id = 'QI.6.I1'
qi_55_i1.ps_id = 'QI.7.I1'
qi_57_i1.ps_id = 'QI.8.I1'
qi_59_i1.ps_id = 'QI.9.I1'
qi_60_i1.ps_id = 'QI.11.I1'
qi_61_i1.ps_id = 'QI.12.I1'
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
qf_469_b2d.ps_id = 'QF.31.B2D'
qe_471_b2d.ps_id = 'QE.32.B2D'
qf_472_b2d.ps_id = 'QF.33.B2D'

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
c_a1_1_1_i1.ps_id = 'C.A1.I1'
c_a1_1_2_i1.ps_id = 'C.A1.I1'
c_a1_1_3_i1.ps_id = 'C.A1.I1'
c_a1_1_4_i1.ps_id = 'C.A1.I1'
c_a1_1_5_i1.ps_id = 'C.A1.I1'
c_a1_1_6_i1.ps_id = 'C.A1.I1'
c_a1_1_7_i1.ps_id = 'C.A1.I1'
c_a1_1_8_i1.ps_id = 'C.A1.I1'
c3_ah1_1_1_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_2_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_3_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_4_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_5_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_6_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_7_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_8_i1.ps_id = 'C3.AH1.I1'
tdsa_52_i1.ps_id = 'TDSA.I1'
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

#  
bl_48i_i1.ps_id = 'BL.1.I1'
bl_48ii_i1.ps_id = 'BL.1.I1'
bl_50i_i1.ps_id = 'BL.3.I1'
bl_50ii_i1.ps_id = 'BL.4.I1'
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
bb_393_b2.ps_id = 'BB.1.B2'
bb_402_b2.ps_id = 'BB.1.B2'
bb_404_b2.ps_id = 'BB.1.B2'
bb_413_b2.ps_id = 'BB.1.B2'
bg_467_b2d.ps_id = 'BG.1.B2D'
