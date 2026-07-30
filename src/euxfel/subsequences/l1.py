# Converted from component_list_2026.02.13.xls

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import (
    Cavity,
    Drift,
    Hcor,
    Marker,
    Monitor,
    Quadrupole,
    RBend,
    SBend,
    Sextupole,
    TDCavity,
    Vcor,
)

twiss0 = Twiss()
twiss0.E = 0.12999999999999998
twiss0.alpha_x = 0.23964062933824398
twiss0.alpha_y = -2.1841640590702722
twiss0.beta_x = 3.020592602704924
twiss0.beta_y = 7.034982640199846
twiss0.s = 38.889005


# fmt: off
# Drifts:
d_0 = Drift(l=0.5, eid="D_0")
d_1 = Drift(l=0.740000000000002, eid="D_1")
d_2 = Drift(l=0.08114999999999525, eid="D_2")
d_3 = Drift(l=0.1311500000000019, eid="D_3")
d_4 = Drift(l=0.5499999999999972, eid="D_4")
d_5 = Drift(l=0.5000000000000057, eid="D_5")
d_6 = Drift(l=0.15, eid="D_6")
vcbshut_65_i1 = Drift(l=0.3, eid="VCBSHUT.65.I1")
d_7 = Drift(l=0.18114999999999953, eid="D_7")
d_8 = Drift(l=2.8623000000000016, eid="D_8")
d_9 = Drift(l=1.7623, eid="D_9")
d_10 = Drift(l=0.681149999999999, eid="D_10")
d_11 = Drift(l=0.18114999999999526, eid="D_11")
d_12 = Drift(l=0.18115000000000617, eid="D_12")
d_13 = Drift(l=0.20000000000000426, eid="D_13")
d_14 = Drift(l=0.08114999999999525, eid="D_14")
d_15 = Drift(l=0.18237699999999915, eid="D_15")
d_16 = Drift(l=0.13500000000000512, eid="D_16")
d_17 = Drift(l=0.23943199999999507, eid="D_17")
d_18 = Drift(l=0.07509999999999714, eid="D_18")
d_19 = Drift(l=0.07510000000000286, eid="D_19")
d_20 = Drift(l=0.13493199999999725, eid="D_20")
d_21 = Drift(l=0.15860899999999845, eid="D_21")
d_22 = Drift(l=0.1325000000000074, eid="D_22")
d_23 = Drift(l=0.09864999999999355, eid="D_23")
d_24 = Drift(l=0.11615000000000844, eid="D_24")
d_25 = Drift(l=0.2736079999999902, eid="D_25")
d_26 = Drift(l=0.13493200000000627, eid="D_26")
d_27 = Drift(l=0.07509999999999714, eid="D_27")
d_28 = Drift(l=0.07510000000000286, eid="D_28")
d_29 = Drift(l=0.3244319999999997, eid="D_29")
d_30 = Drift(l=0.14999999999999858, eid="D_30")
d_31 = Drift(l=0.18237599999999787, eid="D_31")
d_32 = Drift(l=0.18237699999999915, eid="D_32")
d_33 = Drift(l=0.134999999999998, eid="D_33")
d_34 = Drift(l=0.23943200000000217, eid="D_34")
d_35 = Drift(l=0.07509999999999714, eid="D_35")
d_36 = Drift(l=0.07510000000000286, eid="D_36")
d_37 = Drift(l=0.13493199999999725, eid="D_37")
d_38 = Drift(l=0.15860800000000097, eid="D_38")
d_39 = Drift(l=0.13250000000000028, eid="D_39")
d_40 = Drift(l=0.09864999999999355, eid="D_40")
d_41 = Drift(l=0.11615000000000844, eid="D_41")
d_42 = Drift(l=0.2736089999999948, eid="D_42")
d_43 = Drift(l=0.13493199999999916, eid="D_43")
d_44 = Drift(l=0.07509999999999714, eid="D_44")
d_45 = Drift(l=0.07510000000000286, eid="D_45")
d_46 = Drift(l=0.32443100000000225, eid="D_46")
d_47 = Drift(l=0.14999999999999858, eid="D_47")
d_48 = Drift(l=0.18237700000000245, eid="D_48")
d_49 = Drift(l=0.18237699999999915, eid="D_49")
d_50 = Drift(l=0.13500000000000512, eid="D_50")
d_51 = Drift(l=0.2394309999999976, eid="D_51")
d_52 = Drift(l=0.07509999999999714, eid="D_52")
d_53 = Drift(l=0.07510000000000286, eid="D_53")
d_54 = Drift(l=0.13493199999999725, eid="D_54")
d_55 = Drift(l=0.15860899999999845, eid="D_55")
d_56 = Drift(l=0.1325000000000074, eid="D_56")
d_57 = Drift(l=0.09864999999999355, eid="D_57")
d_58 = Drift(l=0.11615000000000844, eid="D_58")
d_59 = Drift(l=0.2736079999999902, eid="D_59")
d_60 = Drift(l=0.13493200000000627, eid="D_60")
d_61 = Drift(l=0.07509999999999714, eid="D_61")
d_62 = Drift(l=0.07509999999999575, eid="D_62")
d_63 = Drift(l=0.3244319999999997, eid="D_63")
d_64 = Drift(l=0.15000000000000568, eid="D_64")
d_65 = Drift(l=0.18237700000000245, eid="D_65")
d_66 = Drift(l=0.18237599999999457, eid="D_66")
d_67 = Drift(l=0.13500000000000512, eid="D_67")
d_68 = Drift(l=0.23943200000000217, eid="D_68")
d_69 = Drift(l=0.07510000000000425, eid="D_69")
d_70 = Drift(l=0.07509999999999575, eid="D_70")
d_71 = Drift(l=0.13493199999999014, eid="D_71")
d_72 = Drift(l=0.15860800000000097, eid="D_72")
d_73 = Drift(l=0.1325000000000074, eid="D_73")
d_74 = Drift(l=0.09865000000000065, eid="D_74")
d_75 = Drift(l=0.48975899999999606, eid="D_75")
d_76 = Drift(l=0.13493200000000627, eid="D_76")
d_77 = Drift(l=0.07510000000000425, eid="D_77")
d_78 = Drift(l=0.07509999999999575, eid="D_78")
d_79 = Drift(l=0.09193199999999799, eid="D_79")
d_80 = Drift(l=0.1325000000000017, eid="D_80")
d_81 = Drift(l=0.14999999999999147, eid="D_81")
d_82 = Drift(l=0.18237700000000245, eid="D_82")
d_83 = Drift(l=0.8812799999999896, eid="D_83")
d_84 = Drift(l=0.20000000000000284, eid="D_84")
d_85 = Drift(l=0.09115000000000748, eid="D_85")
d_86 = Drift(l=0.28115000000000046, eid="D_86")
d_87 = Drift(l=0.09599999999998943, eid="D_87")
d_88 = Drift(l=0.20400000000000773, eid="D_88")
d_89 = Drift(l=0.09115000000000748, eid="D_89")
d_90 = Drift(l=0.38114999999999477, eid="D_90")
d_91 = Drift(l=0.09999999999999432, eid="D_91")
d_92 = Drift(l=1.0071920000000034, eid="D_92")
d_93 = Drift(l=0.39749999999999375, eid="D_93")
d_94 = Drift(l=0.08500000000000796, eid="D_94")
d_95 = Drift(l=0.3824999999999932, eid="D_95")
d_96 = Drift(l=0.3100000000000023, eid="D_96")
d_97 = Drift(l=0.32500000000000284, eid="D_97")
d_98 = Drift(l=1.007191000000006, eid="D_98")
d_99 = Drift(l=0.10000000000000853, eid="D_99")
d_100 = Drift(l=0.3911499999999961, eid="D_100")
d_101 = Drift(l=0.09115000000000276, eid="D_101")
d_102 = Drift(l=0.2499999999999943, eid="D_102")
d_103 = Drift(l=0.09600000000000364, eid="D_103")
d_104 = Drift(l=0.14400000000000546, eid="D_104")
d_105 = Drift(l=0.09115000000000748, eid="D_105")
d_106 = Drift(l=0.18114999999999196, eid="D_106")
d_107 = Drift(l=0.5600000000000023, eid="D_107")
d_108 = Drift(l=0.09114999999999326, eid="D_108")
d_109 = Drift(l=0.18115000000000236, eid="D_109")
d_110 = Drift(l=1.8900000000000006, eid="D_110")
d_111 = Drift(l=0.09114999999999326, eid="D_111")
d_112 = Drift(l=0.18115000000000617, eid="D_112")
d_113 = Drift(l=1.8900000000000006, eid="D_113")
d_114 = Drift(l=0.09114999999999326, eid="D_114")
d_115 = Drift(l=0.18115000000000617, eid="D_115")
d_116 = Drift(l=1.8900000000000006, eid="D_116")
d_117 = Drift(l=0.09114999999999326, eid="D_117")
d_118 = Drift(l=0.18115000000000617, eid="D_118")
d_119 = Drift(l=0.4999999999999858, eid="D_119")
vcdst_113_i1 = Drift(l=1.215, eid="VCDST.113.I1")
d_120 = Drift(l=0.3250000000000062, eid="D_120")
d_121 = Drift(l=0.09115000000000748, eid="D_121")
d_122 = Drift(l=0.18114999999999196, eid="D_122")
d_123 = Drift(l=1.1242000000000019, eid="D_123")
d_124 = Drift(l=0.1407999999999987, eid="D_124")
d_125 = Drift(l=0.09115000000000748, eid="D_125")
d_126 = Drift(l=0.13964999999999275, eid="D_126")
d_127 = Drift(l=1.091319999999996, eid="D_127")
d_128 = Drift(l=0.3490300000000133, eid="D_128")
d_129 = Drift(l=0.09114999999999895, eid="D_129")
d_130 = Drift(l=0.09114999999999326, eid="D_130")
d_131 = Drift(l=0.1439500000000076, eid="D_131")
d_132 = Drift(l=0.3521999999999963, eid="D_132")
cfb_121_l1 = Drift(l=3.35, eid="CFB.121.L1")
d_133 = Drift(l=0.22160100000000682, eid="D_133")
d_134 = Drift(l=0.3458989999999895, eid="D_134")
d_135 = Drift(l=0.3459000000000012, eid="D_135")
d_136 = Drift(l=0.3459000000000012, eid="D_136")
d_137 = Drift(l=0.3459000000000012, eid="D_137")
d_138 = Drift(l=0.3459000000000012, eid="D_138")
d_139 = Drift(l=0.3459000000000012, eid="D_139")
d_140 = Drift(l=0.3459009999999987, eid="D_140")
d_141 = Drift(l=0.24749899999999148, eid="D_141")
d_142 = Drift(l=0.04320100000001004, eid="D_142")
d_143 = Drift(l=0.08499899999999627, eid="D_143")
d_144 = Drift(l=0.4579010000000068, eid="D_144")
d_145 = Drift(l=0.22159999999999513, eid="D_145")
d_146 = Drift(l=0.3459000000000012, eid="D_146")
d_147 = Drift(l=0.3459000000000012, eid="D_147")
d_148 = Drift(l=0.3459000000000012, eid="D_148")
d_149 = Drift(l=0.3459000000000012, eid="D_149")
d_150 = Drift(l=0.3458989999999895, eid="D_150")
d_151 = Drift(l=0.3459000000000012, eid="D_151")
d_152 = Drift(l=0.3459000000000012, eid="D_152")
d_153 = Drift(l=0.24750000000000316, eid="D_153")
d_154 = Drift(l=0.04319999999999835, eid="D_154")
d_155 = Drift(l=0.08500100000000543, eid="D_155")
d_156 = Drift(l=0.4578989999999976, eid="D_156")
d_157 = Drift(l=0.22159999999999513, eid="D_157")
d_158 = Drift(l=0.3459000000000012, eid="D_158")
d_159 = Drift(l=0.3459000000000012, eid="D_159")
d_160 = Drift(l=0.3459010000000129, eid="D_160")
d_161 = Drift(l=0.3459000000000012, eid="D_161")
d_162 = Drift(l=0.3459000000000012, eid="D_162")
d_163 = Drift(l=0.3459000000000012, eid="D_163")
d_164 = Drift(l=0.3459000000000012, eid="D_164")
d_165 = Drift(l=0.24750000000000316, eid="D_165")
d_166 = Drift(l=0.043198999999972454, eid="D_166")
d_167 = Drift(l=0.08500000000000796, eid="D_167")
d_168 = Drift(l=0.4578999999999951, eid="D_168")
d_169 = Drift(l=0.22160100000002103, eid="D_169")
d_170 = Drift(l=0.3459000000000012, eid="D_170")
d_171 = Drift(l=0.3459000000000012, eid="D_171")
d_172 = Drift(l=0.3459000000000012, eid="D_172")
d_173 = Drift(l=0.3459000000000012, eid="D_173")
d_174 = Drift(l=0.3459000000000012, eid="D_174")
d_175 = Drift(l=0.3459000000000012, eid="D_175")
d_176 = Drift(l=0.3459000000000012, eid="D_176")
d_177 = Drift(l=0.24749899999997726, eid="D_177")
d_178 = Drift(l=0.04319999999999835, eid="D_178")
d_179 = Drift(l=0.08500100000000543, eid="D_179")
d_180 = Drift(l=0.4578999999999951, eid="D_180")
ctb_172_l1 = Drift(l=3.25, eid="CTB.172.L1")
d_181 = Drift(l=0.12573000000000434, eid="D_181")
vcdst_174_b1 = Drift(l=1.215, eid="VCDST.174.B1")
d_182 = Drift(l=0.07426899999999015, eid="D_182")
d_183 = Drift(l=0.13100000000000023, eid="D_183")
d_184 = Drift(l=0.24800100000001635, eid="D_184")
d_185 = Drift(l=0.15214999999997758, eid="D_185")
d_186 = Drift(l=0.08214900000000494, eid="D_186")
d_187 = Drift(l=0.3689999999999941, eid="D_187")
d_188 = Drift(l=0.8460010000000011, eid="D_188")
d_189 = Drift(l=0.8840000000000089, eid="D_189")
d_190 = Drift(l=0.05000000000001137, eid="D_190")
d_191 = Drift(l=0.3299989999999866, eid="D_191")
d_192 = Drift(l=0.34900100000001544, eid="D_192")
d_193 = Drift(l=0.15264999999999418, eid="D_193")
d_194 = Drift(l=0.13164899999999494, eid="D_194")
d_195 = Drift(l=0.15000099999999747, eid="D_195")
d_196 = Drift(l=0.5, eid="D_196")
d_197 = Drift(l=0.23164900000000443, eid="D_197")
d_198 = Drift(l=0.10164999999999128, eid="D_198")
d_199 = Drift(l=0.10300000000000295, eid="D_199")
d_200 = Drift(l=0.2524999999999977, eid="D_200")
d_201 = Drift(l=0.09600000000000364, eid="D_201")
d_202 = Drift(l=0.07849999999999113, eid="D_202")
d_203 = Drift(l=0.25, eid="D_203")
d_204 = Drift(l=0.10000100000002021, eid="D_204")
d_205 = Drift(l=8.510621000000015, eid="D_205")
d_206 = Drift(l=0.39750000000000796, eid="D_206")
d_207 = Drift(l=0.08500000000000796, eid="D_207")
d_208 = Drift(l=0.3824999999999932, eid="D_208")
d_209 = Drift(l=0.3100000000000023, eid="D_209")
d_210 = Drift(l=0.32499999999998863, eid="D_210")
d_211 = Drift(l=1.0547759999999755, eid="D_211")
d_212 = Drift(l=7.455845000000011, eid="D_212")
d_213 = Drift(l=0.09999999999999432, eid="D_213")
d_214 = Drift(l=0.29999999999998295, eid="D_214")
d_215 = Drift(l=0.12250000000000227, eid="D_215")
d_216 = Drift(l=0.1564999999999941, eid="D_216")
d_217 = Drift(l=0.09600000000000364, eid="D_217")
d_218 = Drift(l=0.35480000000001155, eid="D_218")
d_219 = Drift(l=0.15419999999997458, eid="D_219")
d_220 = Drift(l=0.09715000000002191, eid="D_220")
d_221 = Drift(l=0.4421499999999876, eid="D_221")
d_222 = Drift(l=0.2230000000000132, eid="D_222")
d_223 = Drift(l=0.09714999999999349, eid="D_223")
d_224 = Drift(l=0.15015000000001447, eid="D_224")
d_225 = Drift(l=0.47299999999998477, eid="D_225")
d_226 = Drift(l=0.10800000000000409, eid="D_226")
d_227 = Drift(l=0.05000000000001137, eid="D_227")
d_228 = Drift(l=0.3779999999999859, eid="D_228")
d_229 = Drift(l=0.15315000000001078, eid="D_229")
d_230 = Drift(l=0.08114999999999764, eid="D_230")
d_231 = Drift(l=0.09999999999999432, eid="D_231")
d_232 = Drift(l=0.18115000000000236, eid="D_232")
d_233 = Drift(l=0.28115000000001467, eid="D_233")
d_234 = Drift(l=0.14999999999997726, eid="D_234")
d_235 = Drift(l=0.09999999999999432, eid="D_235")
d_236 = Drift(l=0.37900000000001344, eid="D_236")
d_237 = Drift(l=0.1526500000000226, eid="D_237")
d_238 = Drift(l=0.131649999999964, eid="D_238")
d_239 = Drift(l=1.0311500000000193, eid="D_239")
d_240 = Drift(l=1.23014999999997, eid="D_240")
d_241 = Drift(l=0.18000000000002955, eid="D_241")
d_242 = Drift(l=0.15214999999997758, eid="D_242")
d_243 = Drift(l=0.08114999999999764, eid="D_243")
d_244 = Drift(l=0.0500000000000341, eid="D_244")
d_245 = Drift(l=0.19999999999998863, eid="D_245")
d_246 = Drift(l=0.14999999999997726, eid="D_246")
d_247 = Drift(l=0.5790000000000305, eid="D_247")
d_248 = Drift(l=0.15214999999997758, eid="D_248")
d_249 = Drift(l=0.09714999999998877, eid="D_249")
d_250 = Drift(l=0.21500000000002614, eid="D_250")
d_251 = Drift(l=0.5009999999999991, eid="D_251")
d_252 = Drift(l=0.14699999999998567, eid="D_252")
d_253 = Drift(l=0.152150000000006, eid="D_253")
d_254 = Drift(l=0.12515000000000878, eid="D_254")
d_255 = Drift(l=0.3559999999999889, eid="D_255")
d_256 = Drift(l=0.4000000000000057, eid="D_256")
d_257 = Drift(l=0.20000000000001705, eid="D_257")
d_258 = Drift(l=0.09899999999998954, eid="D_258")
d_259 = Drift(l=0.13265000000001237, eid="D_259")
d_260 = Drift(l=0.12564999999996376, eid="D_260")
d_261 = Drift(l=0.3560000000000173, eid="D_261")
d_262 = Drift(l=0.679000000000002, eid="D_262")
d_263 = Drift(l=0.1526500000000226, eid="D_263")
d_264 = Drift(l=0.10764999999996308, eid="D_264")
d_265 = Drift(l=0.15418000000001938, eid="D_265")
d_266 = Drift(l=0.46981999999999857, eid="D_266")
d_267 = Drift(l=0.679000000000002, eid="D_267")
d_268 = Drift(l=0.15264999999999418, eid="D_268")
d_269 = Drift(l=0.18165000000000378, eid="D_269")
d_270 = Drift(l=0.05000000000000568, eid="D_270")
d_271 = Drift(l=0.19999999999998863, eid="D_271")
d_272 = Drift(l=0.30000000000001137, eid="D_272")
d_273 = Drift(l=0.3461499999999944, eid="D_273")
d_274 = Drift(l=0.12614999999998514, eid="D_274")
d_275 = Drift(l=0.06999999999998752, eid="D_275")
d_276 = Drift(l=0.3320000000000164, eid="D_276")
d_277 = Drift(l=0.15215100000000348, eid="D_277")
d_278 = Drift(l=0.08115099999999512, eid="D_278")
d_279 = Drift(l=0.15, eid="D_279")
d_280 = Drift(l=0.18000000000000113, eid="D_280")
d_281 = Drift(l=0.15215100000000348, eid="D_281")
d_282 = Drift(l=1.0971510000000146, eid="D_282")
d_283 = Drift(l=0.39724999999998545, eid="D_283")

# Quadrupoles:
qi_63_i1 = Quadrupole(l=0.2377, k1=-1.824087238998738, eid="QI.63.I1")
qi_66_i1 = Quadrupole(l=0.2377, k1=2.142575757000421, eid="QI.66.I1")
qi_69_i1 = Quadrupole(l=0.2377, k1=-2.1265116389987377, eid="QI.69.I1")
qi_71_i1 = Quadrupole(l=0.2377, k1=3.4033787980016825, eid="QI.71.I1")
qi_72_i1 = Quadrupole(l=0.2377, k1=-4.43452895, eid="QI.72.I1")
qi_73_i1 = Quadrupole(l=0.2377, k1=4.632555991998317, eid="QI.73.I1")
qi_74_i1 = Quadrupole(l=0.2377, k1=-4.99137522, eid="QI.74.I1")
qi_75_i1 = Quadrupole(l=0.2377, k1=5.027338701001262, eid="QI.75.I1")
qi_77_i1 = Quadrupole(l=0.2377, k1=-4.99137522, eid="QI.77.I1")
qi_78_i1 = Quadrupole(l=0.2377, k1=4.632555991998317, eid="QI.78.I1")
qi_79_i1 = Quadrupole(l=0.2377, k1=-4.99137522, eid="QI.79.I1")
qi_80_i1 = Quadrupole(l=0.2377, k1=5.027338701001262, eid="QI.80.I1")
qi_82_i1 = Quadrupole(l=0.2377, k1=-4.99137522, eid="QI.82.I1")
qi_83_i1 = Quadrupole(l=0.2377, k1=4.632555991998317, eid="QI.83.I1")
qi_84_i1 = Quadrupole(l=0.2377, k1=-4.99137522, eid="QI.84.I1")
qi_85_i1 = Quadrupole(l=0.2377, k1=5.027338701001262, eid="QI.85.I1")
qi_86_i1 = Quadrupole(l=0.2377, k1=-4.99137522, eid="QI.86.I1")
qi_88_i1 = Quadrupole(l=0.2377, k1=4.632555991998317, eid="QI.88.I1")
qi_89_i1 = Quadrupole(l=0.2377, k1=-4.99137522, eid="QI.89.I1")
qi_90_i1 = Quadrupole(l=0.2377, k1=5.027338701001262, eid="QI.90.I1")
qi_92_i1 = Quadrupole(l=0.2377, k1=-4.99137522, eid="QI.92.I1")
qi_93_i1 = Quadrupole(l=0.2377, k1=-0.7125210101009677, eid="QI.93.I1")
qi_94_i1 = Quadrupole(l=0.2377, k1=3.3764224510012624, eid="QI.94.I1")
qi_95_i1 = Quadrupole(l=0.2377, k1=-3.0503922929995793, eid="QI.95.I1")
qi_102_i1 = Quadrupole(l=0.2377, k1=0.6879609419983171, eid="QI.102.I1")
qi_103_i1 = Quadrupole(l=0.2377, k1=-1.3591500629995792, eid="QI.103.I1")
qi_104_i1 = Quadrupole(l=0.2377, k1=1.4975012119983173, eid="QI.104.I1")
qi_107_i1 = Quadrupole(l=0.2377, k1=-1.5226412540008414, eid="QI.107.I1")
qi_109_i1 = Quadrupole(l=0.2377, k1=1.5226410680016829, eid="QI.109.I1")
qi_112_i1 = Quadrupole(l=0.2377, k1=-1.5226412540008414, eid="QI.112.I1")
qi_114_i1 = Quadrupole(l=0.2377, k1=0.9967996614009255, eid="QI.114.I1")
qi_116_i1 = Quadrupole(l=0.2377, k1=0.5375414028986117, eid="QI.116.I1")
qi_118_i1 = Quadrupole(l=0.2377, k1=-0.94121992, eid="QI.118.I1")
q_134_l1 = Quadrupole(l=0.2136, k1=0.2857947439981273, eid="Q.134.L1")
q_146_l1 = Quadrupole(l=0.2136, k1=-0.29239645940074904, eid="Q.146.L1")
q_158_l1 = Quadrupole(l=0.2136, k1=0.21577324690074906, eid="Q.158.L1")
q_170_l1 = Quadrupole(l=0.2136, k1=-0.22084659039794008, eid="Q.170.L1")
qi_176_b1 = Quadrupole(l=0.2377, eid="QI.176.B1")
qd_179_b1 = Quadrupole(l=0.2367, k1=0.7960126531009717, eid="QD.179.B1")
qd_181_b1 = Quadrupole(l=0.2367, k1=-0.7285956364005071, eid="QD.181.B1")
qi_204_b1 = Quadrupole(l=0.2377, k1=-0.9137399601009676, eid="QI.204.B1")
qi_205_b1 = Quadrupole(l=0.2377, k1=0.0415357294110223, eid="QI.205.B1")
qi_206_b1 = Quadrupole(l=0.2377, k1=0.6755384867017249, eid="QI.206.B1")
qi_209_b1 = Quadrupole(l=0.2377, k1=1.0443862489987379, eid="QI.209.B1")
qd_210_b1 = Quadrupole(l=0.2367, k1=-2.1831505249978878, eid="QD.210.B1")
qi_211_b1 = Quadrupole(l=0.2377, k1=0.6386118848001683, eid="QI.211.B1")
qi_213_b1 = Quadrupole(l=0.2377, k1=1.186969648998738, eid="QI.213.B1")
qi_215_b1 = Quadrupole(l=0.2377, k1=-1.1237338750021033, eid="QI.215.B1")
qi_217_b1 = Quadrupole(l=0.2377, k1=-1.43507582, eid="QI.217.B1")
qd_219_b1 = Quadrupole(l=0.2367, k1=2.859590704000845, eid="QD.219.B1")
qd_221_b1 = Quadrupole(l=0.2367, k1=-2.8595909289987325, eid="QD.221.B1")
qd_223_b1 = Quadrupole(l=0.2367, k1=2.859590704000845, eid="QD.223.B1")
qi_224_b1 = Quadrupole(l=0.2377, k1=-0.8565833407993269, eid="QI.224.B1")
qi_226_b1 = Quadrupole(l=0.2377, k1=-1.5618567640008414, eid="QI.226.B1")
qi_227_b1 = Quadrupole(l=0.2377, k1=1.5235329029995792, eid="QI.227.B1")

# SBends:
bl_73_i1 = SBend(l=0.2001020000000011, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, tilt=1.570796327, eid="BL.73.I1")
bl_75_i1 = SBend(l=0.2000150000000005, angle=0.0426524581, e1=0.021326229, e2=0.021326229, tilt=1.570796327, eid="BL.75.I1")
bl_76_i1 = SBend(l=0.2000150000000005, angle=0.0426524581, e1=0.021326229, e2=0.021326229, tilt=1.570796327, eid="BL.76.I1")
bl_77_i1 = SBend(l=0.2001029999999986, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, tilt=1.570796327, eid="BL.77.I1")
bl_78_i1 = SBend(l=0.2001030000000057, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, tilt=1.570796327, eid="BL.78.I1")
bl_80_i1 = SBend(l=0.2000150000000005, angle=0.0426524581, e1=0.021326229, e2=0.021326229, tilt=1.570796327, eid="BL.80.I1")
bl_81_i1 = SBend(l=0.2000150000000005, angle=0.0426524581, e1=0.021326229, e2=0.021326229, tilt=1.570796327, eid="BL.81.I1")
bl_82_i1 = SBend(l=0.2001029999999986, angle=-0.1109740393, e1=-0.05548702, e2=-0.05548702, tilt=1.570796327, eid="BL.82.I1")
bl_83_i1 = SBend(l=0.2001029999999986, angle=0.1109740393, e1=0.05548702, e2=0.05548702, tilt=1.570796327, eid="BL.83.I1")
bl_85_i1 = SBend(l=0.2000150000000005, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, tilt=1.570796327, eid="BL.85.I1")
bl_86_i1 = SBend(l=0.2000150000000005, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, tilt=1.570796327, eid="BL.86.I1")
bl_87_i1 = SBend(l=0.2001029999999986, angle=0.1109740393, e1=0.05548702, e2=0.05548702, tilt=1.570796327, eid="BL.87.I1")
bl_88_i1 = SBend(l=0.2001029999999986, angle=0.1109740393, e1=0.05548702, e2=0.05548702, tilt=1.570796327, eid="BL.88.I1")
bl_90_i1 = SBend(l=0.2000150000000076, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, tilt=1.570796327, eid="BL.90.I1")
bl_91_i1 = SBend(l=0.2000149999999934, angle=-0.0426524581, e1=-0.021326229, e2=-0.021326229, tilt=1.570796327, eid="BL.91.I1")
bl_92_i1 = SBend(l=0.2001020000000011, angle=0.1109740393, e1=0.05548702, e2=0.05548702, tilt=1.570796327, eid="BL.92.I1")
bb_96_i1 = SBend(l=0.5011930000000007, angle=0.11957038, e2=0.11957038, tilt=1.570796327, eid="BB.96.I1")
bb_98_i1 = SBend(l=0.5011930000000007, angle=-0.11957038, e1=-0.11957038, tilt=1.570796327, eid="BB.98.I1")
bb_100_i1 = SBend(l=0.5011939999999981, angle=-0.11957038, e2=-0.11957038, tilt=1.570796327, eid="BB.100.I1")
bb_101_i1 = SBend(l=0.5011929999999865, angle=0.11957038, e1=0.11957038, tilt=1.570796327, eid="BB.101.I1")
bb_182_b1 = SBend(l=0.5002079999999864, angle=0.04996493936, e2=0.049964939, tilt=1.570796327, eid="BB.182.B1")
bb_191_b1 = SBend(l=0.5002079999999864, angle=-0.04996493936, e1=-0.049964939, tilt=1.570796327, eid="BB.191.B1")
bb_193_b1 = SBend(l=0.5002080000000149, angle=-0.04996493936, e2=-0.049964939, tilt=1.570796327, eid="BB.193.B1")
bb_202_b1 = SBend(l=0.5002080000000149, angle=0.04996493936, e1=0.049964939, tilt=1.570796327, eid="BB.202.B1")

# RBends:
bseci_64_i1 = RBend(l=0.4, e1=0.0, e2=0.0, eid="BSECI.64.I1")
kay_214_b1 = RBend(l=0.35, e1=0.0, e2=0.0, eid="KAY.214.B1")
kay_216_b1 = RBend(l=0.35, e1=0.0, e2=0.0, eid="KAY.216.B1")
kay_218_b1 = RBend(l=0.35, e1=0.0, e2=0.0, eid="KAY.218.B1")
kay_219_b1 = RBend(l=0.35, e1=0.0, e2=0.0, eid="KAY.219.B1")
kax_225_b1 = RBend(l=0.35, e1=0.0, e2=0.0, eid="KAX.225.B1")
kax_226_b1 = RBend(l=0.35, e1=0.0, e2=0.0, eid="KAX.226.B1")

# Sextupoles:
sc_74i_i1 = Sextupole(l=0.1121, k2=-87.57825836, tilt=1.570796327, eid="SC.74I.I1")
sc_74ii_i1 = Sextupole(l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid="SC.74II.I1")
sc_76_i1 = Sextupole(l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid="SC.76.I1")
sc_77_i1 = Sextupole(l=0.1121, k2=-87.57825836, tilt=1.570796327, eid="SC.77.I1")
sc_79i_i1 = Sextupole(l=0.1121, k2=-87.57825836, tilt=1.570796327, eid="SC.79I.I1")
sc_79ii_i1 = Sextupole(l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid="SC.79II.I1")
sc_81_i1 = Sextupole(l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid="SC.81.I1")
sc_82_i1 = Sextupole(l=0.1121, k2=-87.57825836, tilt=1.570796327, eid="SC.82.I1")
sc_84i_i1 = Sextupole(l=0.1121, k2=87.57825836, tilt=1.570796327, eid="SC.84I.I1")
sc_84ii_i1 = Sextupole(l=0.1121, k2=53.061653289999995, tilt=1.570796327, eid="SC.84II.I1")
sc_86_i1 = Sextupole(l=0.1121, k2=53.061653289999995, tilt=1.570796327, eid="SC.86.I1")
sc_87_i1 = Sextupole(l=0.1121, k2=87.57825836, tilt=1.570796327, eid="SC.87.I1")
sc_89i_i1 = Sextupole(l=0.1121, k2=87.57825836, tilt=1.570796327, eid="SC.89I.I1")
sc_89ii_i1 = Sextupole(l=0.1121, k2=53.061653289999995, tilt=1.570796327, eid="SC.89II.I1")
sc_91_i1 = Sextupole(l=0.1121, k2=53.061653289999995, tilt=1.570796327, eid="SC.91.I1")
sc_92_i1 = Sextupole(l=0.1121, k2=87.57825836, tilt=1.570796327, eid="SC.92.I1")

# Hcors:
cbb_62_i1d = Hcor(eid="CBB.62.I1D")
cix_65_i1 = Hcor(l=0.1, eid="CIX.65.I1")
cix_73i_i1 = Hcor(l=0.1, eid="CIX.73I.I1")
cix_73ii_i1 = Hcor(l=0.1, eid="CIX.73II.I1")
cix_76_i1 = Hcor(l=0.1, eid="CIX.76.I1")
cix_78_i1 = Hcor(l=0.1, eid="CIX.78.I1")
cix_81_i1 = Hcor(l=0.1, eid="CIX.81.I1")
cix_83_i1 = Hcor(l=0.1, eid="CIX.83.I1")
cix_86_i1 = Hcor(l=0.1, eid="CIX.86.I1")
cix_88_i1 = Hcor(l=0.1, eid="CIX.88.I1")
cix_90_i1 = Hcor(l=0.1, eid="CIX.90.I1")
cix_95_i1 = Hcor(l=0.1, eid="CIX.95.I1")
cix_102_i1 = Hcor(l=0.1, eid="CIX.102.I1")
cix_104_i1 = Hcor(l=0.1, eid="CIX.104.I1")
cix_109_i1 = Hcor(l=0.1, eid="CIX.109.I1")
cix_114_i1 = Hcor(l=0.1, eid="CIX.114.I1")
cix_118_i1 = Hcor(l=0.1, eid="CIX.118.I1")
cx_134_l1 = Hcor(eid="CX.134.L1")
cx_146_l1 = Hcor(eid="CX.146.L1")
cx_158_l1 = Hcor(eid="CX.158.L1")
cx_170_l1 = Hcor(eid="CX.170.L1")
cix_177_b1 = Hcor(l=0.1, eid="CIX.177.B1")
ccx_179_b1 = Hcor(l=0.1, eid="CCX.179.B1")
cix_205_b1 = Hcor(l=0.1, eid="CIX.205.B1")
cix_209_b1 = Hcor(l=0.1, eid="CIX.209.B1")
cix_213_b1 = Hcor(l=0.1, eid="CIX.213.B1")
cix_216_b1 = Hcor(l=0.1, eid="CIX.216.B1")
cfx_223_b1 = Hcor(l=0.1, eid="CFX.223.B1")
cfx_226_b1 = Hcor(l=0.1, eid="CFX.226.B1")

# Vcors:
ciy_63_i1 = Vcor(l=0.1, eid="CIY.63.I1")
ciy_72_i1 = Vcor(l=0.1, eid="CIY.72.I1")
cbl_73_i1 = Vcor(eid="CBL.73.I1")
ciy_75_i1 = Vcor(l=0.1, eid="CIY.75.I1")
cbl_78_i1 = Vcor(eid="CBL.78.I1")
ciy_80_i1 = Vcor(l=0.1, eid="CIY.80.I1")
cbl_83_i1 = Vcor(eid="CBL.83.I1")
ciy_85_i1 = Vcor(l=0.1, eid="CIY.85.I1")
cbl_88_i1 = Vcor(eid="CBL.88.I1")
cbl_90_i1 = Vcor(eid="CBL.90.I1")
ciy_92_i1 = Vcor(l=0.1, eid="CIY.92.I1")
ciy_94_i1 = Vcor(l=0.1, eid="CIY.94.I1")
cbb_98_i1 = Vcor(eid="CBB.98.I1")
cbb_100_i1 = Vcor(eid="CBB.100.I1")
cbb_101_i1 = Vcor(eid="CBB.101.I1")
ciy_103_i1 = Vcor(l=0.1, eid="CIY.103.I1")
ciy_107_i1 = Vcor(l=0.1, eid="CIY.107.I1")
ciy_112_i1 = Vcor(l=0.1, eid="CIY.112.I1")
ciy_116_i1 = Vcor(l=0.1, eid="CIY.116.I1")
cy_134_l1 = Vcor(eid="CY.134.L1")
cy_146_l1 = Vcor(eid="CY.146.L1")
cy_158_l1 = Vcor(eid="CY.158.L1")
cy_170_l1 = Vcor(eid="CY.170.L1")
ciy_176_b1 = Vcor(l=0.1, eid="CIY.176.B1")
ccy_181_b1 = Vcor(l=0.1, eid="CCY.181.B1")
cbb_191_b1 = Vcor(eid="CBB.191.B1")
cbb_193_b1 = Vcor(eid="CBB.193.B1")
cbb_202_b1 = Vcor(eid="CBB.202.B1")
ciy_204_b1 = Vcor(l=0.1, eid="CIY.204.B1")
ccy_210_b1 = Vcor(l=0.1, eid="CCY.210.B1")
ciy_214_b1 = Vcor(l=0.1, eid="CIY.214.B1")
ccy_217_b1 = Vcor(l=0.1, eid="CCY.217.B1")
ccy_221_b1 = Vcor(l=0.1, eid="CCY.221.B1")
ciy_226_b1 = Vcor(l=0.1, eid="CIY.226.B1")

# Cavitys:
c_a2_1_1_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.1.1.L1")
c_a2_1_2_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.1.2.L1")
c_a2_1_3_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.1.3.L1")
c_a2_1_4_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.1.4.L1")
c_a2_1_5_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.1.5.L1")
c_a2_1_6_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.1.6.L1")
c_a2_1_7_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.1.7.L1")
c_a2_1_8_l1 = Cavity(l=1.0377, v=0.0214344953, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.1.8.L1")
c_a2_2_1_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.2.1.L1")
c_a2_2_2_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.2.2.L1")
c_a2_2_3_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.2.3.L1")
c_a2_2_4_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.2.4.L1")
c_a2_2_5_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.2.5.L1")
c_a2_2_6_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.2.6.L1")
c_a2_2_7_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.2.7.L1")
c_a2_2_8_l1 = Cavity(l=1.0377, v=0.020463522730000003, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.2.8.L1")
c_a2_3_1_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.3.1.L1")
c_a2_3_2_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.3.2.L1")
c_a2_3_3_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.3.3.L1")
c_a2_3_4_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.3.4.L1")
c_a2_3_5_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.3.5.L1")
c_a2_3_6_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.3.6.L1")
c_a2_3_7_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.3.7.L1")
c_a2_3_8_l1 = Cavity(l=1.0377, v=0.01914636534, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.3.8.L1")
c_a2_4_1_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.4.1.L1")
c_a2_4_2_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.4.2.L1")
c_a2_4_3_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.4.3.L1")
c_a2_4_4_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.4.4.L1")
c_a2_4_5_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.4.5.L1")
c_a2_4_6_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.4.6.L1")
c_a2_4_7_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.4.7.L1")
c_a2_4_8_l1 = Cavity(l=1.0377, v=0.01757129336, phi=24.999999839999997, freq=1300000000.0, eid="C.A2.4.8.L1")

# TDCavitys:
tdsb_208_b1 = TDCavity(l=1.5, freq=2800000000.0, eid="TDSB.208.B1")

# Monitors:
bpma_63_i1 = Monitor(eid="BPMA.63.I1")
bpma_72_i1 = Monitor(eid="BPMA.72.I1")
bpma_75_i1 = Monitor(eid="BPMA.75.I1")
bpma_77_i1 = Monitor(eid="BPMA.77.I1")
bpma_80_i1 = Monitor(eid="BPMA.80.I1")
bpma_82_i1 = Monitor(eid="BPMA.82.I1")
bpma_85_i1 = Monitor(eid="BPMA.85.I1")
bpma_87_i1 = Monitor(eid="BPMA.87.I1")
bpma_90_i1 = Monitor(eid="BPMA.90.I1")
bpma_92_i1 = Monitor(eid="BPMA.92.I1")
bpmf_95_i1 = Monitor(eid="BPMF.95.I1")
bpms_99_i1 = Monitor(eid="BPMS.99.I1")
bpmf_103_i1 = Monitor(eid="BPMF.103.I1")
bpma_103_i1 = Monitor(eid="BPMA.103.I1")
bpma_105_i1 = Monitor(eid="BPMA.105.I1")
bpma_107_i1 = Monitor(eid="BPMA.107.I1")
bpma_110_i1 = Monitor(eid="BPMA.110.I1")
bpma_112_i1 = Monitor(eid="BPMA.112.I1")
bpma_115_i1 = Monitor(eid="BPMA.115.I1")
bpma_117_i1 = Monitor(eid="BPMA.117.I1")
bpma_119_i1 = Monitor(eid="BPMA.119.I1")
bpmc_134_l1 = Monitor(eid="BPMC.134.L1")
bpmr_146_l1 = Monitor(eid="BPMR.146.L1")
bpmc_158_l1 = Monitor(eid="BPMC.158.L1")
bpmr_170_l1 = Monitor(eid="BPMR.170.L1")
bpma_175_b1 = Monitor(eid="BPMA.175.B1")
bpma_179_b1 = Monitor(eid="BPMA.179.B1")
bpmf_181_b1 = Monitor(eid="BPMF.181.B1")
bpms_192_b1 = Monitor(eid="BPMS.192.B1")
bpmf_203_b1 = Monitor(eid="BPMF.203.B1")
bpma_206_b1 = Monitor(eid="BPMA.206.B1")
bpma_210_b1 = Monitor(eid="BPMA.210.B1")
bpma_213_b1 = Monitor(eid="BPMA.213.B1")
bpma_215_b1 = Monitor(eid="BPMA.215.B1")
bpma_217_b1 = Monitor(eid="BPMA.217.B1")
bpma_219_b1 = Monitor(eid="BPMA.219.B1")
bpma_221_b1 = Monitor(eid="BPMA.221.B1")
bpma_223_b1 = Monitor(eid="BPMA.223.B1")
bpma_226_b1 = Monitor(eid="BPMA.226.B1")
bpma_227_b1 = Monitor(eid="BPMA.227.B1")

# Markers:
stsub_62_i1 = Marker(eid="STSUB.62.I1")
dogleg_start = Marker(eid="dogleg_start")
stlat_73_i1 = Marker(eid="STLAT.73.I1")
match_73_i1 = Marker(eid="MATCH.73.I1")
mbl_73a_i1 = Marker(eid="MBL.73a.I1")
mbl_73d_i1 = Marker(eid="MBL.73d.I1")
mbl_75a_i1 = Marker(eid="MBL.75a.I1")
mbl_75d_i1 = Marker(eid="MBL.75d.I1")
mbl_76a_i1 = Marker(eid="MBL.76a.I1")
mbl_76d_i1 = Marker(eid="MBL.76d.I1")
mbl_77a_i1 = Marker(eid="MBL.77a.I1")
mbl_77d_i1 = Marker(eid="MBL.77d.I1")
mbl_78a_i1 = Marker(eid="MBL.78a.I1")
mbl_78d_i1 = Marker(eid="MBL.78d.I1")
mbl_80a_i1 = Marker(eid="MBL.80a.I1")
mbl_80d_i1 = Marker(eid="MBL.80d.I1")
mbl_81a_i1 = Marker(eid="MBL.81a.I1")
mbl_81d_i1 = Marker(eid="MBL.81d.I1")
mbl_82a_i1 = Marker(eid="MBL.82a.I1")
mbl_82d_i1 = Marker(eid="MBL.82d.I1")
mbl_83a_i1 = Marker(eid="MBL.83a.I1")
mbl_83d_i1 = Marker(eid="MBL.83d.I1")
mbl_85a_i1 = Marker(eid="MBL.85a.I1")
mbl_85d_i1 = Marker(eid="MBL.85d.I1")
mbl_86a_i1 = Marker(eid="MBL.86a.I1")
mbl_86d_i1 = Marker(eid="MBL.86d.I1")
mbl_87a_i1 = Marker(eid="MBL.87a.I1")
mbl_87d_i1 = Marker(eid="MBL.87d.I1")
mbl_88a_i1 = Marker(eid="MBL.88a.I1")
mbl_88d_i1 = Marker(eid="MBL.88d.I1")
mbl_90a_i1 = Marker(eid="MBL.90a.I1")
mbl_90d_i1 = Marker(eid="MBL.90d.I1")
mbl_91a_i1 = Marker(eid="MBL.91a.I1")
mbl_91d_i1 = Marker(eid="MBL.91d.I1")
mbl_92a_i1 = Marker(eid="MBL.92a.I1")
mbl_92d_i1 = Marker(eid="MBL.92d.I1")
enlat_93_i1 = Marker(eid="ENLAT.93.I1")
ensub_93_i1 = Marker(eid="ENSUB.93.I1")
stsub_93_i1 = Marker(eid="STSUB.93.I1")
tora_94_i1 = Marker(eid="TORA.94.I1")
midbpmf_95_i1 = Marker(eid="MIDBPMF.95.I1")
dogleg_stop_bc0_start = Marker(eid="dogleg_stop_bc0_start")
stlat_96_i1 = Marker(eid="STLAT.96.I1")
mbb_96a_i1 = Marker(eid="MBB.96a.I1")
mbb_96d_i1 = Marker(eid="MBB.96d.I1")
vcst40t400y_96_i1 = Marker(eid="VCST40T400Y.96.I1")
vcst400y_97_i1 = Marker(eid="VCST400Y.97.I1")
mbb_98a_i1 = Marker(eid="MBB.98a.I1")
mbb_98d_i1 = Marker(eid="MBB.98d.I1")
colo_98_i1 = Marker(eid="COLO.98.I1")
colu_98_i1 = Marker(eid="COLU.98.I1")
otrs_99_i1 = Marker(eid="OTRS.99.I1")
mbb_100a_i1 = Marker(eid="MBB.100a.I1")
mbb_100d_i1 = Marker(eid="MBB.100d.I1")
vcst400yt40_100_i1 = Marker(eid="VCST400YT40.100.I1")
vcst40y_101_i1 = Marker(eid="VCST40Y.101.I1")
mbb_101a_i1 = Marker(eid="MBB.101a.I1")
mbb_101d_i1 = Marker(eid="MBB.101d.I1")
enlat_101_i1 = Marker(eid="ENLAT.101.I1")
midbpmf_103_i1 = Marker(eid="MIDBPMF.103.I1")
bc0_stop_l1_start = Marker(eid="bc0_stop_l1_start")
stlat_104_i1 = Marker(eid="STLAT.104.I1")
match_104_i1 = Marker(eid="MATCH.104.I1")
enlat_114_i1 = Marker(eid="ENLAT.114.I1")
tora_116_i1 = Marker(eid="TORA.116.I1")
otra_118_i1 = Marker(eid="OTRA.118.I1")
dcm_118_i1 = Marker(eid="DCM.118.I1")
ensub_119_i1 = Marker(eid="ENSUB.119.I1")
ensec_119_i1 = Marker(eid="ENSEC.119.I1")
stsec_119_l1 = Marker(eid="STSEC.119.L1")
vcst40t78_119_l1 = Marker(eid="VCST40T78.119.L1")
stac_122_l1 = Marker(eid="STAC.122.L1")
enac_134_l1 = Marker(eid="ENAC.134.L1")
stac_134_l1 = Marker(eid="STAC.134.L1")
enac_146_l1 = Marker(eid="ENAC.146.L1")
stac_146_l1 = Marker(eid="STAC.146.L1")
enac_158_l1 = Marker(eid="ENAC.158.L1")
stac_158_l1 = Marker(eid="STAC.158.L1")
enac_170_l1 = Marker(eid="ENAC.170.L1")
vcst78t40_174_l1 = Marker(eid="VCST78T40.174.L1")
ensec_174_l1 = Marker(eid="ENSEC.174.L1")
stsec_174_b1 = Marker(eid="STSEC.174.B1")
stsub_174_b1 = Marker(eid="STSUB.174.B1")
match_174_b1 = Marker(eid="MATCH.174.B1")
stgrd_175_b1 = Marker(eid="STGRD.175.B1")
tora_175_b1 = Marker(eid="TORA.175.B1")
dcm_176_b1 = Marker(eid="DCM.176.B1")
engrd_178_b1 = Marker(eid="ENGRD.178.B1")
stgrd_178_b1 = Marker(eid="STGRD.178.B1")
eod_179_b1 = Marker(eid="EOD.179.B1")
bcm_180_b1 = Marker(eid="BCM.180.B1")
otra_180_b1 = Marker(eid="OTRA.180.B1")
bam_181_b1 = Marker(eid="BAM.181.B1")
midbpmf_181_b1 = Marker(eid="MIDBPMF.181.B1")
engrd_181_b1 = Marker(eid="ENGRD.181.B1")
l1_stop_bc1_start = Marker(eid="l1_stop_bc1_start")
stlat_182_b1 = Marker(eid="STLAT.182.B1")
mbb_182a_b1 = Marker(eid="MBB.182a.B1")
mbb_182d_b1 = Marker(eid="MBB.182d.B1")
vcst40t400y_182_b1 = Marker(eid="VCST40T400Y.182.B1")
vcst400y_191_b1 = Marker(eid="VCST400Y.191.B1")
mbb_191a_b1 = Marker(eid="MBB.191a.B1")
mbb_191d_b1 = Marker(eid="MBB.191d.B1")
colo_192_b1 = Marker(eid="COLO.192.B1")
colu_192_b1 = Marker(eid="COLU.192.B1")
otrs_192_b1 = Marker(eid="OTRS.192.B1")
mbb_193a_b1 = Marker(eid="MBB.193a.B1")
mbb_193d_b1 = Marker(eid="MBB.193d.B1")
vcst400yt40_193_b1 = Marker(eid="VCST400YT40.193.B1")
srm_194_b1 = Marker(eid="SRM.194.B1")
vcst40y_202_b1 = Marker(eid="VCST40Y.202.B1")
mbb_202a_b1 = Marker(eid="MBB.202a.B1")
mbb_202d_b1 = Marker(eid="MBB.202d.B1")
enlat_202_b1 = Marker(eid="ENLAT.202.B1")
match_202_b1 = Marker(eid="MATCH.202.B1")
stlat_202_b1 = Marker(eid="STLAT.202.B1")
stgrd_203_b1 = Marker(eid="STGRD.203.B1")
bam_203_b1 = Marker(eid="BAM.203.B1")
midbpmf_203_b1 = Marker(eid="MIDBPMF.203.B1")
tora_203_b1 = Marker(eid="TORA.203.B1")
bc1_stop_l2_start = Marker(eid="bc1_stop_l2_start")
eod_204_b1 = Marker(eid="EOD.204.B1")
bcm_205_b1 = Marker(eid="BCM.205.B1")
otra_206_b1 = Marker(eid="OTRA.206.B1")
engrd_206_b1 = Marker(eid="ENGRD.206.B1")
stgrd_206_b1 = Marker(eid="STGRD.206.B1")
match_207_b1 = Marker(eid="MATCH.207.B1")
stblock_207_b1 = Marker(eid="STBLOCK.207.B1")
engrd_209_b1 = Marker(eid="ENGRD.209.B1")
stgrd_209_b1 = Marker(eid="STGRD.209.B1")
engrd_214_b1 = Marker(eid="ENGRD.214.B1")
stgrd_214_b1 = Marker(eid="STGRD.214.B1")
match_218_b1 = Marker(eid="MATCH.218.B1")
otrb_218_b1 = Marker(eid="OTRB.218.B1")
engrd_219_b1 = Marker(eid="ENGRD.219.B1")
stgrd_219_b1 = Marker(eid="STGRD.219.B1")
otrb_220_b1 = Marker(eid="OTRB.220.B1")
dcm_221_b1 = Marker(eid="DCM.221.B1")
otrb_222_b1 = Marker(eid="OTRB.222.B1")
engrd_223_b1 = Marker(eid="ENGRD.223.B1")
stgrd_224_b1 = Marker(eid="STGRD.224.B1")
otrb_224_b1 = Marker(eid="OTRB.224.B1")
engrd_228_b1 = Marker(eid="ENGRD.228.B1")
enlat_229_b1 = Marker(eid="ENLAT.229.B1")
ensub_229_b1 = Marker(eid="ENSUB.229.B1")
# fmt: on

# Sequence:
cell = (
    stsub_62_i1,
    d_0,
    cbb_62_i1d,
    d_1,
    ciy_63_i1,
    d_2,
    qi_63_i1,
    d_3,
    bpma_63_i1,
    d_4,
    bseci_64_i1,
    d_5,
    dogleg_start,
    cix_65_i1,
    d_6,
    vcbshut_65_i1,
    d_7,
    qi_66_i1,
    d_8,
    qi_69_i1,
    d_9,
    qi_71_i1,
    d_10,
    bpma_72_i1,
    d_11,
    qi_72_i1,
    d_12,
    ciy_72_i1,
    d_13,
    cix_73i_i1,
    d_14,
    stlat_73_i1,
    match_73_i1,
    qi_73_i1,
    d_15,
    mbl_73a_i1,
    bl_73_i1,
    mbl_73d_i1,
    cbl_73_i1,
    d_16,
    cix_73ii_i1,
    d_17,
    sc_74i_i1,
    d_18,
    qi_74_i1,
    d_19,
    sc_74ii_i1,
    d_20,
    mbl_75a_i1,
    bl_75_i1,
    mbl_75d_i1,
    d_21,
    bpma_75_i1,
    d_22,
    ciy_75_i1,
    d_23,
    qi_75_i1,
    d_24,
    cix_76_i1,
    d_25,
    mbl_76a_i1,
    bl_76_i1,
    mbl_76d_i1,
    d_26,
    sc_76_i1,
    d_27,
    qi_77_i1,
    d_28,
    sc_77_i1,
    d_29,
    bpma_77_i1,
    d_30,
    mbl_77a_i1,
    bl_77_i1,
    mbl_77d_i1,
    d_31,
    qi_78_i1,
    d_32,
    mbl_78a_i1,
    bl_78_i1,
    mbl_78d_i1,
    cbl_78_i1,
    d_33,
    cix_78_i1,
    d_34,
    sc_79i_i1,
    d_35,
    qi_79_i1,
    d_36,
    sc_79ii_i1,
    d_37,
    mbl_80a_i1,
    bl_80_i1,
    mbl_80d_i1,
    d_38,
    bpma_80_i1,
    d_39,
    ciy_80_i1,
    d_40,
    qi_80_i1,
    d_41,
    cix_81_i1,
    d_42,
    mbl_81a_i1,
    bl_81_i1,
    mbl_81d_i1,
    d_43,
    sc_81_i1,
    d_44,
    qi_82_i1,
    d_45,
    sc_82_i1,
    d_46,
    bpma_82_i1,
    d_47,
    mbl_82a_i1,
    bl_82_i1,
    mbl_82d_i1,
    d_48,
    qi_83_i1,
    d_49,
    mbl_83a_i1,
    bl_83_i1,
    mbl_83d_i1,
    cbl_83_i1,
    d_50,
    cix_83_i1,
    d_51,
    sc_84i_i1,
    d_52,
    qi_84_i1,
    d_53,
    sc_84ii_i1,
    d_54,
    mbl_85a_i1,
    bl_85_i1,
    mbl_85d_i1,
    d_55,
    bpma_85_i1,
    d_56,
    ciy_85_i1,
    d_57,
    qi_85_i1,
    d_58,
    cix_86_i1,
    d_59,
    mbl_86a_i1,
    bl_86_i1,
    mbl_86d_i1,
    d_60,
    sc_86_i1,
    d_61,
    qi_86_i1,
    d_62,
    sc_87_i1,
    d_63,
    bpma_87_i1,
    d_64,
    mbl_87a_i1,
    bl_87_i1,
    mbl_87d_i1,
    d_65,
    qi_88_i1,
    d_66,
    mbl_88a_i1,
    bl_88_i1,
    mbl_88d_i1,
    cbl_88_i1,
    d_67,
    cix_88_i1,
    d_68,
    sc_89i_i1,
    d_69,
    qi_89_i1,
    d_70,
    sc_89ii_i1,
    d_71,
    mbl_90a_i1,
    bl_90_i1,
    mbl_90d_i1,
    cbl_90_i1,
    d_72,
    bpma_90_i1,
    d_73,
    cix_90_i1,
    d_74,
    qi_90_i1,
    d_75,
    mbl_91a_i1,
    bl_91_i1,
    mbl_91d_i1,
    d_76,
    sc_91_i1,
    d_77,
    qi_92_i1,
    d_78,
    sc_92_i1,
    d_79,
    ciy_92_i1,
    d_80,
    bpma_92_i1,
    d_81,
    mbl_92a_i1,
    bl_92_i1,
    mbl_92d_i1,
    d_82,
    qi_93_i1,
    enlat_93_i1,
    ensub_93_i1,
    stsub_93_i1,
    d_83,
    tora_94_i1,
    d_84,
    ciy_94_i1,
    d_85,
    qi_94_i1,
    d_86,
    midbpmf_95_i1,
    d_87,
    bpmf_95_i1,
    d_88,
    cix_95_i1,
    d_89,
    qi_95_i1,
    d_90,
    dogleg_stop_bc0_start,
    stlat_96_i1,
    d_91,
    mbb_96a_i1,
    bb_96_i1,
    mbb_96d_i1,
    vcst40t400y_96_i1,
    d_92,
    vcst400y_97_i1,
    mbb_98a_i1,
    bb_98_i1,
    mbb_98d_i1,
    cbb_98_i1,
    d_93,
    colo_98_i1,
    d_94,
    colu_98_i1,
    d_95,
    bpms_99_i1,
    d_96,
    otrs_99_i1,
    d_97,
    mbb_100a_i1,
    bb_100_i1,
    mbb_100d_i1,
    cbb_100_i1,
    vcst400yt40_100_i1,
    d_98,
    vcst40y_101_i1,
    mbb_101a_i1,
    bb_101_i1,
    mbb_101d_i1,
    cbb_101_i1,
    d_99,
    enlat_101_i1,
    d_100,
    qi_102_i1,
    d_101,
    cix_102_i1,
    d_102,
    midbpmf_103_i1,
    d_103,
    bpmf_103_i1,
    d_104,
    ciy_103_i1,
    d_105,
    bc0_stop_l1_start,
    qi_103_i1,
    d_106,
    bpma_103_i1,
    d_107,
    cix_104_i1,
    d_108,
    qi_104_i1,
    stlat_104_i1,
    match_104_i1,
    d_109,
    bpma_105_i1,
    d_110,
    ciy_107_i1,
    d_111,
    qi_107_i1,
    d_112,
    bpma_107_i1,
    d_113,
    cix_109_i1,
    d_114,
    qi_109_i1,
    d_115,
    bpma_110_i1,
    d_116,
    ciy_112_i1,
    d_117,
    qi_112_i1,
    d_118,
    bpma_112_i1,
    d_119,
    vcdst_113_i1,
    d_120,
    enlat_114_i1,
    cix_114_i1,
    d_121,
    qi_114_i1,
    d_122,
    bpma_115_i1,
    d_123,
    tora_116_i1,
    d_124,
    ciy_116_i1,
    d_125,
    qi_116_i1,
    d_126,
    bpma_117_i1,
    d_127,
    otra_118_i1,
    d_128,
    dcm_118_i1,
    d_129,
    cix_118_i1,
    d_130,
    qi_118_i1,
    d_131,
    bpma_119_i1,
    d_132,
    ensub_119_i1,
    ensec_119_i1,
    stsec_119_l1,
    vcst40t78_119_l1,
    cfb_121_l1,
    stac_122_l1,
    d_133,
    c_a2_1_1_l1,
    d_134,
    c_a2_1_2_l1,
    d_135,
    c_a2_1_3_l1,
    d_136,
    c_a2_1_4_l1,
    d_137,
    c_a2_1_5_l1,
    d_138,
    c_a2_1_6_l1,
    d_139,
    c_a2_1_7_l1,
    d_140,
    c_a2_1_8_l1,
    d_141,
    q_134_l1,
    d_142,
    cx_134_l1,
    cy_134_l1,
    d_143,
    bpmc_134_l1,
    d_144,
    enac_134_l1,
    stac_134_l1,
    d_145,
    c_a2_2_1_l1,
    d_146,
    c_a2_2_2_l1,
    d_147,
    c_a2_2_3_l1,
    d_148,
    c_a2_2_4_l1,
    d_149,
    c_a2_2_5_l1,
    d_150,
    c_a2_2_6_l1,
    d_151,
    c_a2_2_7_l1,
    d_152,
    c_a2_2_8_l1,
    d_153,
    q_146_l1,
    d_154,
    cx_146_l1,
    cy_146_l1,
    d_155,
    bpmr_146_l1,
    d_156,
    enac_146_l1,
    stac_146_l1,
    d_157,
    c_a2_3_1_l1,
    d_158,
    c_a2_3_2_l1,
    d_159,
    c_a2_3_3_l1,
    d_160,
    c_a2_3_4_l1,
    d_161,
    c_a2_3_5_l1,
    d_162,
    c_a2_3_6_l1,
    d_163,
    c_a2_3_7_l1,
    d_164,
    c_a2_3_8_l1,
    d_165,
    q_158_l1,
    d_166,
    cx_158_l1,
    cy_158_l1,
    d_167,
    bpmc_158_l1,
    d_168,
    enac_158_l1,
    stac_158_l1,
    d_169,
    c_a2_4_1_l1,
    d_170,
    c_a2_4_2_l1,
    d_171,
    c_a2_4_3_l1,
    d_172,
    c_a2_4_4_l1,
    d_173,
    c_a2_4_5_l1,
    d_174,
    c_a2_4_6_l1,
    d_175,
    c_a2_4_7_l1,
    d_176,
    c_a2_4_8_l1,
    d_177,
    q_170_l1,
    d_178,
    cx_170_l1,
    cy_170_l1,
    d_179,
    bpmr_170_l1,
    d_180,
    enac_170_l1,
    ctb_172_l1,
    vcst78t40_174_l1,
    ensec_174_l1,
    stsec_174_b1,
    stsub_174_b1,
    match_174_b1,
    d_181,
    vcdst_174_b1,
    d_182,
    stgrd_175_b1,
    d_183,
    tora_175_b1,
    d_184,
    bpma_175_b1,
    d_185,
    qi_176_b1,
    d_186,
    ciy_176_b1,
    d_187,
    dcm_176_b1,
    d_188,
    cix_177_b1,
    d_189,
    engrd_178_b1,
    d_190,
    stgrd_178_b1,
    d_191,
    eod_179_b1,
    d_192,
    bpma_179_b1,
    d_193,
    qd_179_b1,
    d_194,
    ccx_179_b1,
    d_195,
    bcm_180_b1,
    d_196,
    otra_180_b1,
    d_197,
    qd_181_b1,
    d_198,
    ccy_181_b1,
    d_199,
    bam_181_b1,
    d_200,
    midbpmf_181_b1,
    d_201,
    bpmf_181_b1,
    d_202,
    engrd_181_b1,
    d_203,
    l1_stop_bc1_start,
    stlat_182_b1,
    d_204,
    mbb_182a_b1,
    bb_182_b1,
    mbb_182d_b1,
    vcst40t400y_182_b1,
    d_205,
    vcst400y_191_b1,
    mbb_191a_b1,
    bb_191_b1,
    mbb_191d_b1,
    cbb_191_b1,
    d_206,
    colo_192_b1,
    d_207,
    colu_192_b1,
    d_208,
    bpms_192_b1,
    d_209,
    otrs_192_b1,
    d_210,
    mbb_193a_b1,
    bb_193_b1,
    mbb_193d_b1,
    cbb_193_b1,
    vcst400yt40_193_b1,
    d_211,
    srm_194_b1,
    d_212,
    vcst40y_202_b1,
    mbb_202a_b1,
    bb_202_b1,
    mbb_202d_b1,
    cbb_202_b1,
    d_213,
    enlat_202_b1,
    match_202_b1,
    stlat_202_b1,
    d_214,
    stgrd_203_b1,
    d_215,
    bam_203_b1,
    d_216,
    bpmf_203_b1,
    d_217,
    midbpmf_203_b1,
    d_218,
    tora_203_b1,
    bc1_stop_l2_start,
    d_219,
    ciy_204_b1,
    d_220,
    qi_204_b1,
    d_221,
    eod_204_b1,
    d_222,
    cix_205_b1,
    d_223,
    qi_205_b1,
    d_224,
    bcm_205_b1,
    d_225,
    otra_206_b1,
    d_226,
    engrd_206_b1,
    d_227,
    stgrd_206_b1,
    d_228,
    bpma_206_b1,
    d_229,
    qi_206_b1,
    d_230,
    match_207_b1,
    stblock_207_b1,
    d_231,
    tdsb_208_b1,
    d_232,
    qi_209_b1,
    d_233,
    engrd_209_b1,
    d_234,
    stgrd_209_b1,
    d_235,
    cix_209_b1,
    d_236,
    bpma_210_b1,
    d_237,
    qd_210_b1,
    d_238,
    ccy_210_b1,
    d_239,
    qi_211_b1,
    d_240,
    cix_213_b1,
    d_241,
    bpma_213_b1,
    d_242,
    qi_213_b1,
    d_243,
    ciy_214_b1,
    d_244,
    engrd_214_b1,
    d_245,
    stgrd_214_b1,
    d_246,
    kay_214_b1,
    d_247,
    bpma_215_b1,
    d_248,
    qi_215_b1,
    d_249,
    cix_216_b1,
    d_250,
    kay_216_b1,
    d_251,
    ccy_217_b1,
    d_252,
    bpma_217_b1,
    d_253,
    qi_217_b1,
    d_254,
    kay_218_b1,
    d_255,
    match_218_b1,
    otrb_218_b1,
    d_256,
    engrd_219_b1,
    d_257,
    stgrd_219_b1,
    d_258,
    bpma_219_b1,
    d_259,
    qd_219_b1,
    d_260,
    kay_219_b1,
    d_261,
    otrb_220_b1,
    d_262,
    bpma_221_b1,
    d_263,
    qd_221_b1,
    d_264,
    ccy_221_b1,
    d_265,
    dcm_221_b1,
    d_266,
    otrb_222_b1,
    d_267,
    bpma_223_b1,
    d_268,
    qd_223_b1,
    d_269,
    cfx_223_b1,
    d_270,
    engrd_223_b1,
    d_271,
    stgrd_224_b1,
    d_272,
    otrb_224_b1,
    d_273,
    qi_224_b1,
    d_274,
    kax_225_b1,
    d_275,
    kax_226_b1,
    d_276,
    bpma_226_b1,
    d_277,
    qi_226_b1,
    d_278,
    ciy_226_b1,
    d_279,
    cfx_226_b1,
    d_280,
    bpma_227_b1,
    d_281,
    qi_227_b1,
    d_282,
    engrd_228_b1,
    d_283,
    enlat_229_b1,
    ensub_229_b1,
)

# Power Supply IDs:
# Drift power supplies:
vcbshut_65_i1.ps_id = "VCBSHUT.I1"
vcdst_113_i1.ps_id = "VCDST.I1"
cfb_121_l1.ps_id = "CFB.L1"
ctb_172_l1.ps_id = "CTB.L1"
vcdst_174_b1.ps_id = "VCDST.B1"

# Quadrupole power supplies:
qi_63_i1.ps_id = "QI.13.I1"
qi_66_i1.ps_id = "QI.14.I1"
qi_69_i1.ps_id = "QI.15.I1"
qi_71_i1.ps_id = "QI.16.I1"
qi_72_i1.ps_id = "QI.17.I1"
qi_73_i1.ps_id = "QI.18.I1"
qi_74_i1.ps_id = "QI.19.I1"
qi_75_i1.ps_id = "QI.20.I1"
qi_77_i1.ps_id = "QI.19.I1"
qi_78_i1.ps_id = "QI.18.I1"
qi_79_i1.ps_id = "QI.19.I1"
qi_80_i1.ps_id = "QI.20.I1"
qi_82_i1.ps_id = "QI.21.I1"
qi_83_i1.ps_id = "QI.22.I1"
qi_84_i1.ps_id = "QI.21.I1"
qi_85_i1.ps_id = "QI.24.I1"
qi_86_i1.ps_id = "QI.23.I1"
qi_88_i1.ps_id = "QI.22.I1"
qi_89_i1.ps_id = "QI.23.I1"
qi_90_i1.ps_id = "QI.24.I1"
qi_92_i1.ps_id = "QI.23.I1"
qi_93_i1.ps_id = "QI.25.I1"
qi_94_i1.ps_id = "QI.26.I1"
qi_95_i1.ps_id = "QI.27.I1"
qi_102_i1.ps_id = "QI.28.I1"
qi_103_i1.ps_id = "QI.29.I1"
qi_104_i1.ps_id = "QI.30.I1"
qi_107_i1.ps_id = "QI.31.I1"
qi_109_i1.ps_id = "QI.32.I1"
qi_112_i1.ps_id = "QI.31.I1"
qi_114_i1.ps_id = "QI.33.I1"
qi_116_i1.ps_id = "QI.34.I1"
qi_118_i1.ps_id = "QI.35.I1"
q_134_l1.ps_id = "Q.A2.1.L1"
q_146_l1.ps_id = "Q.A2.2.L1"
q_158_l1.ps_id = "Q.A2.3.L1"
q_170_l1.ps_id = "Q.A2.4.L1"
qi_176_b1.ps_id = "QI.1.B1"
qd_179_b1.ps_id = "QD.3.B1"
qd_181_b1.ps_id = "QD.4.B1"
qi_204_b1.ps_id = "QI.5.B1"
qi_205_b1.ps_id = "QI.6.B1"
qi_206_b1.ps_id = "QI.7.B1"
qi_209_b1.ps_id = "QI.8.B1"
qd_210_b1.ps_id = "QD.9.B1"
qi_211_b1.ps_id = "QI.10.B1"
qi_213_b1.ps_id = "QI.11.B1"
qi_215_b1.ps_id = "QI.12.B1"
qi_217_b1.ps_id = "QI.13.B1"
qd_219_b1.ps_id = "QD.14.B1"
qd_221_b1.ps_id = "QD.15.B1"
qd_223_b1.ps_id = "QD.16.B1"
qi_224_b1.ps_id = "QI.17.B1"
qi_226_b1.ps_id = "QI.18.B1"
qi_227_b1.ps_id = "QI.19.B1"

# SBend power supplies:
bl_73_i1.ps_id = "BL.6.I1"
bl_75_i1.ps_id = "BL.7.I1"
bl_76_i1.ps_id = "BL.7.I1"
bl_77_i1.ps_id = "BL.6.I1"
bl_78_i1.ps_id = "BL.6.I1"
bl_80_i1.ps_id = "BL.7.I1"
bl_81_i1.ps_id = "BL.7.I1"
bl_82_i1.ps_id = "BL.6.I1"
bl_83_i1.ps_id = "BL.8.I1"
bl_85_i1.ps_id = "BL.7.I1"
bl_86_i1.ps_id = "BL.7.I1"
bl_87_i1.ps_id = "BL.8.I1"
bl_88_i1.ps_id = "BL.8.I1"
bl_90_i1.ps_id = "BL.7.I1"
bl_91_i1.ps_id = "BL.7.I1"
bl_92_i1.ps_id = "BL.8.I1"
bb_96_i1.ps_id = "BB.1.I1"
bb_98_i1.ps_id = "BB.1.I1"
bb_100_i1.ps_id = "BB.1.I1"
bb_101_i1.ps_id = "BB.1.I1"
bb_182_b1.ps_id = "BB.1.B1"
bb_191_b1.ps_id = "BB.1.B1"
bb_193_b1.ps_id = "BB.1.B1"
bb_202_b1.ps_id = "BB.1.B1"

# RBend power supplies:
bseci_64_i1.ps_id = "BSECI.I1"
kay_214_b1.ps_id = "KAY.214.B1"
kay_216_b1.ps_id = "KAY.216.B1"
kay_218_b1.ps_id = "KAY.218.B1"
kay_219_b1.ps_id = "KAY.219.B1"
kax_225_b1.ps_id = "KAX.225.B1"
kax_226_b1.ps_id = "KAX.226.B1"

# Sextupole power supplies:
sc_74i_i1.ps_id = "SC.1.I1"
sc_74ii_i1.ps_id = "SC.2.I1"
sc_76_i1.ps_id = "SC.2.I1"
sc_77_i1.ps_id = "SC.1.I1"
sc_79i_i1.ps_id = "SC.1.I1"
sc_79ii_i1.ps_id = "SC.2.I1"
sc_81_i1.ps_id = "SC.2.I1"
sc_82_i1.ps_id = "SC.1.I1"
sc_84i_i1.ps_id = "SC.1.I1"
sc_84ii_i1.ps_id = "SC.2.I1"
sc_86_i1.ps_id = "SC.2.I1"
sc_87_i1.ps_id = "SC.1.I1"
sc_89i_i1.ps_id = "SC.1.I1"
sc_89ii_i1.ps_id = "SC.2.I1"
sc_91_i1.ps_id = "SC.2.I1"
sc_92_i1.ps_id = "SC.1.I1"

# Hcor power supplies:
cbb_62_i1d.ps_id = "CBB.5.I1D"
cix_65_i1.ps_id = "CIX.6.I1"
cix_73i_i1.ps_id = "CIX.7.I1"
cix_73ii_i1.ps_id = "CIX.8.I1"
cix_76_i1.ps_id = "CIX.9.I1"
cix_78_i1.ps_id = "CIX.10.I1"
cix_81_i1.ps_id = "CIX.11.I1"
cix_83_i1.ps_id = "CIX.12.I1"
cix_86_i1.ps_id = "CIX.13.I1"
cix_88_i1.ps_id = "CIX.14.I1"
cix_90_i1.ps_id = "CIX.15.I1"
cix_95_i1.ps_id = "CIX.16.I1"
cix_102_i1.ps_id = "CIX.17.I1"
cix_104_i1.ps_id = "CIX.18.I1"
cix_109_i1.ps_id = "CIX.19.I1"
cix_114_i1.ps_id = "CIX.20.I1"
cix_118_i1.ps_id = "CIX.21.I1"
cx_134_l1.ps_id = "CX.A2.1.L1"
cx_146_l1.ps_id = "CX.A2.2.L1"
cx_158_l1.ps_id = "CX.A2.3.L1"
cx_170_l1.ps_id = "CX.A2.4.L1"
cix_177_b1.ps_id = "CIX.1.B1"
ccx_179_b1.ps_id = "CCX.2.B1"
cix_205_b1.ps_id = "CIX.3.B1"
cix_209_b1.ps_id = "CIX.4.B1"
cix_213_b1.ps_id = "CIX.5.B1"
cix_216_b1.ps_id = "CIX.6.B1"
cfx_223_b1.ps_id = "CFX.7.B1"
cfx_226_b1.ps_id = "CFX.8.B1"

# Vcor power supplies:
ciy_63_i1.ps_id = "CIY.7.I1"
ciy_72_i1.ps_id = "CIY.8.I1"
cbl_73_i1.ps_id = "CBL.9.I1"
ciy_75_i1.ps_id = "CIY.10.I1"
cbl_78_i1.ps_id = "CBL.11.I1"
ciy_80_i1.ps_id = "CIY.12.I1"
cbl_83_i1.ps_id = "CBL.13.I1"
ciy_85_i1.ps_id = "CIY.14.I1"
cbl_88_i1.ps_id = "CBL.15.I1"
cbl_90_i1.ps_id = "CBL.16.I1"
ciy_92_i1.ps_id = "CIY.17.I1"
ciy_94_i1.ps_id = "CIY.18.I1"
cbb_98_i1.ps_id = "CBB.2.I1"
cbb_100_i1.ps_id = "CBB.3.I1"
cbb_101_i1.ps_id = "CBB.4.I1"
ciy_103_i1.ps_id = "CIY.19.I1"
ciy_107_i1.ps_id = "CIY.20.I1"
ciy_112_i1.ps_id = "CIY.21.I1"
ciy_116_i1.ps_id = "CIY.22.I1"
cy_134_l1.ps_id = "CY.A2.1.L1"
cy_146_l1.ps_id = "CY.A2.2.L1"
cy_158_l1.ps_id = "CY.A2.3.L1"
cy_170_l1.ps_id = "CY.A2.4.L1"
ciy_176_b1.ps_id = "CIY.1.B1"
ccy_181_b1.ps_id = "CCY.2.B1"
cbb_191_b1.ps_id = "CBB.2.B1"
cbb_193_b1.ps_id = "CBB.3.B1"
cbb_202_b1.ps_id = "CBB.4.B1"
ciy_204_b1.ps_id = "CIY.3.B1"
ccy_210_b1.ps_id = "CCY.4.B1"
ciy_214_b1.ps_id = "CIY.5.B1"
ccy_217_b1.ps_id = "CCY.6.B1"
ccy_221_b1.ps_id = "CCY.7.B1"
ciy_226_b1.ps_id = "CIY.8.B1"

# Cavity power supplies:
c_a2_1_1_l1.ps_id = "C.A2.L1"
c_a2_1_2_l1.ps_id = "C.A2.L1"
c_a2_1_3_l1.ps_id = "C.A2.L1"
c_a2_1_4_l1.ps_id = "C.A2.L1"
c_a2_1_5_l1.ps_id = "C.A2.L1"
c_a2_1_6_l1.ps_id = "C.A2.L1"
c_a2_1_7_l1.ps_id = "C.A2.L1"
c_a2_1_8_l1.ps_id = "C.A2.L1"
c_a2_2_1_l1.ps_id = "C.A2.L1"
c_a2_2_2_l1.ps_id = "C.A2.L1"
c_a2_2_3_l1.ps_id = "C.A2.L1"
c_a2_2_4_l1.ps_id = "C.A2.L1"
c_a2_2_5_l1.ps_id = "C.A2.L1"
c_a2_2_6_l1.ps_id = "C.A2.L1"
c_a2_2_7_l1.ps_id = "C.A2.L1"
c_a2_2_8_l1.ps_id = "C.A2.L1"
c_a2_3_1_l1.ps_id = "C.A2.L1"
c_a2_3_2_l1.ps_id = "C.A2.L1"
c_a2_3_3_l1.ps_id = "C.A2.L1"
c_a2_3_4_l1.ps_id = "C.A2.L1"
c_a2_3_5_l1.ps_id = "C.A2.L1"
c_a2_3_6_l1.ps_id = "C.A2.L1"
c_a2_3_7_l1.ps_id = "C.A2.L1"
c_a2_3_8_l1.ps_id = "C.A2.L1"
c_a2_4_1_l1.ps_id = "C.A2.L1"
c_a2_4_2_l1.ps_id = "C.A2.L1"
c_a2_4_3_l1.ps_id = "C.A2.L1"
c_a2_4_4_l1.ps_id = "C.A2.L1"
c_a2_4_5_l1.ps_id = "C.A2.L1"
c_a2_4_6_l1.ps_id = "C.A2.L1"
c_a2_4_7_l1.ps_id = "C.A2.L1"
c_a2_4_8_l1.ps_id = "C.A2.L1"

# TDCavity power supplies:
tdsb_208_b1.ps_id = "TDSB.B1"

# Monitor power supplies:
bpma_63_i1.ps_id = "BPMA.I1"
bpma_72_i1.ps_id = "BPMA.I1"
bpma_75_i1.ps_id = "BPMA.I1"
bpma_77_i1.ps_id = "BPMA.I1"
bpma_80_i1.ps_id = "BPMA.I1"
bpma_82_i1.ps_id = "BPMA.I1"
bpma_85_i1.ps_id = "BPMA.I1"
bpma_87_i1.ps_id = "BPMA.I1"
bpma_90_i1.ps_id = "BPMA.I1"
bpma_92_i1.ps_id = "BPMA.I1"
bpmf_95_i1.ps_id = "BPMF.I1"
bpms_99_i1.ps_id = "BPMS.I1"
bpmf_103_i1.ps_id = "BPMF.I1"
bpma_103_i1.ps_id = "BPMA.I1"
bpma_105_i1.ps_id = "BPMA.I1"
bpma_107_i1.ps_id = "BPMA.I1"
bpma_110_i1.ps_id = "BPMA.I1"
bpma_112_i1.ps_id = "BPMA.I1"
bpma_115_i1.ps_id = "BPMA.I1"
bpma_117_i1.ps_id = "BPMA.I1"
bpma_119_i1.ps_id = "BPMA.I1"
bpmc_134_l1.ps_id = "BPMC.A2.1.L1"
bpmr_146_l1.ps_id = "BPMR.A2.2.L1"
bpmc_158_l1.ps_id = "BPMC.A2.3.L1"
bpmr_170_l1.ps_id = "BPMR.A2.4.L1"
bpma_175_b1.ps_id = "BPMA.B1"
bpma_179_b1.ps_id = "BPMA.B1"
bpmf_181_b1.ps_id = "BPMF.B1"
bpms_192_b1.ps_id = "BPMS.B1"
bpmf_203_b1.ps_id = "BPMF.B1"
bpma_206_b1.ps_id = "BPMA.B1"
bpma_210_b1.ps_id = "BPMA.B1"
bpma_213_b1.ps_id = "BPMA.B1"
bpma_215_b1.ps_id = "BPMA.B1"
bpma_217_b1.ps_id = "BPMA.B1"
bpma_219_b1.ps_id = "BPMA.B1"
bpma_221_b1.ps_id = "BPMA.B1"
bpma_223_b1.ps_id = "BPMA.B1"
bpma_226_b1.ps_id = "BPMA.B1"
bpma_227_b1.ps_id = "BPMA.B1"

# Marker power supplies:
stsub_62_i1.ps_id = "STSUB.I1T.I1"
stlat_73_i1.ps_id = "STLAT.DOG.I1"
match_73_i1.ps_id = "MATCH.DLG.I1"
mbl_73a_i1.ps_id = "MBL.6.I1"
mbl_73d_i1.ps_id = "MBL.6.I1"
mbl_75a_i1.ps_id = "MBL.7.1.I1"
mbl_75d_i1.ps_id = "MBL.7.1.I1"
mbl_76a_i1.ps_id = "MBL.7.1.I1"
mbl_76d_i1.ps_id = "MBL.7.1.I1"
mbl_77a_i1.ps_id = "MBL.6.I1"
mbl_77d_i1.ps_id = "MBL.6.I1"
mbl_78a_i1.ps_id = "MBL.6.I1"
mbl_78d_i1.ps_id = "MBL.6.I1"
mbl_80a_i1.ps_id = "MBL.7.1.I1"
mbl_80d_i1.ps_id = "MBL.7.1.I1"
mbl_81a_i1.ps_id = "MBL.7.1.I1"
mbl_81d_i1.ps_id = "MBL.7.1.I1"
mbl_82a_i1.ps_id = "MBL.6.I1"
mbl_82d_i1.ps_id = "MBL.6.I1"
mbl_83a_i1.ps_id = "MBL.8.I1"
mbl_83d_i1.ps_id = "MBL.8.I1"
mbl_85a_i1.ps_id = "MBL.7.2.I1"
mbl_85d_i1.ps_id = "MBL.7.2.I1"
mbl_86a_i1.ps_id = "MBL.7.2.I1"
mbl_86d_i1.ps_id = "MBL.7.2.I1"
mbl_87a_i1.ps_id = "MBL.8.I1"
mbl_87d_i1.ps_id = "MBL.8.I1"
mbl_88a_i1.ps_id = "MBL.8.I1"
mbl_88d_i1.ps_id = "MBL.8.I1"
mbl_90a_i1.ps_id = "MBL.7.2.I1"
mbl_90d_i1.ps_id = "MBL.7.2.I1"
mbl_91a_i1.ps_id = "MBL.7.2.I1"
mbl_91d_i1.ps_id = "MBL.7.2.I1"
mbl_92a_i1.ps_id = "MBL.8.I1"
mbl_92d_i1.ps_id = "MBL.8.I1"
enlat_93_i1.ps_id = "ENLAT.DOG.I1"
ensub_93_i1.ps_id = "ENSUB.I1T.I1"
stsub_93_i1.ps_id = "STSUB.B0.I1"
tora_94_i1.ps_id = "TORA.I1"
midbpmf_95_i1.ps_id = "MIDBPMF.I1"
stlat_96_i1.ps_id = "STLAT.B0M.I1"
mbb_96a_i1.ps_id = "MBB.1.1.I1"
mbb_96d_i1.ps_id = "MBB.1.1.I1"
vcst40t400y_96_i1.ps_id = "VCST40T400Y.I1"
vcst400y_97_i1.ps_id = "VCST400Y.I1"
mbb_98a_i1.ps_id = "MBB.1.2.I1"
mbb_98d_i1.ps_id = "MBB.1.2.I1"
colo_98_i1.ps_id = "COLO.I1"
colu_98_i1.ps_id = "COLU.I1"
otrs_99_i1.ps_id = "OTRS.I1"
mbb_100a_i1.ps_id = "MBB.1.3.I1"
mbb_100d_i1.ps_id = "MBB.1.3.I1"
vcst400yt40_100_i1.ps_id = "VCST400YT40.I1"
vcst40y_101_i1.ps_id = "VCST40Y.I1"
mbb_101a_i1.ps_id = "MBB.1.4.I1"
mbb_101d_i1.ps_id = "MBB.1.4.I1"
enlat_101_i1.ps_id = "ENLAT.B0M.I1"
midbpmf_103_i1.ps_id = "MIDBPMF.I1"
stlat_104_i1.ps_id = "STLAT.PS.I1"
match_104_i1.ps_id = "MATCH.PS.I1"
enlat_114_i1.ps_id = "ENLAT.PS.I1"
tora_116_i1.ps_id = "TORA.I1"
otra_118_i1.ps_id = "OTRA.I1"
dcm_118_i1.ps_id = "DCM.I1"
ensub_119_i1.ps_id = "ENSUB.B0.I1"
ensec_119_i1.ps_id = "ENSEC.I1.I1"
stsec_119_l1.ps_id = "STSEC.L1.L1"
vcst40t78_119_l1.ps_id = "VCST40T78.L1"
stac_122_l1.ps_id = "STAC.A2.1.L1"
enac_134_l1.ps_id = "ENAC.A2.1.L1"
stac_134_l1.ps_id = "STAC.A2.2.L1"
enac_146_l1.ps_id = "ENAC.A2.2.L1"
stac_146_l1.ps_id = "STAC.A2.3.L1"
enac_158_l1.ps_id = "ENAC.A2.3.L1"
stac_158_l1.ps_id = "STAC.A2.4.L1"
enac_170_l1.ps_id = "ENAC.A2.4.L1"
vcst78t40_174_l1.ps_id = "VCST78T40.L1"
ensec_174_l1.ps_id = "ENSEC.L1.L1"
stsec_174_b1.ps_id = "STSEC.B1.B1"
stsub_174_b1.ps_id = "STSUB.B1M.B1"
match_174_b1.ps_id = "MATCH.B1.B1"
stgrd_175_b1.ps_id = "STGRD.G1.B1"
tora_175_b1.ps_id = "TORA.B1"
dcm_176_b1.ps_id = "DCM.B1"
engrd_178_b1.ps_id = "ENGRD.G1.B1"
stgrd_178_b1.ps_id = "STGRD.G2.B1"
eod_179_b1.ps_id = "EOD.B1"
bcm_180_b1.ps_id = "BCM.B1"
otra_180_b1.ps_id = "OTRA.B1"
bam_181_b1.ps_id = "BAM.B1"
midbpmf_181_b1.ps_id = "MIDBPMF.B1"
engrd_181_b1.ps_id = "ENGRD.G2.B1"
stlat_182_b1.ps_id = "STLAT.B1M.B1"
mbb_182a_b1.ps_id = "MBB.1.1.B1"
mbb_182d_b1.ps_id = "MBB.1.1.B1"
vcst40t400y_182_b1.ps_id = "VCST40T400Y.B1"
vcst400y_191_b1.ps_id = "VCST400Y.B1"
mbb_191a_b1.ps_id = "MBB.1.2.B1"
mbb_191d_b1.ps_id = "MBB.1.2.B1"
colo_192_b1.ps_id = "COLO.B1"
colu_192_b1.ps_id = "COLU.B1"
otrs_192_b1.ps_id = "OTRS.B1"
mbb_193a_b1.ps_id = "MBB.1.3.B1"
mbb_193d_b1.ps_id = "MBB.1.3.B1"
vcst400yt40_193_b1.ps_id = "VCST400YT40.B1"
srm_194_b1.ps_id = "SRM.B1"
vcst40y_202_b1.ps_id = "VCST40Y.B1"
mbb_202a_b1.ps_id = "MBB.1.4.B1"
mbb_202d_b1.ps_id = "MBB.1.4.B1"
enlat_202_b1.ps_id = "ENLAT.B1M.B1"
match_202_b1.ps_id = "MATCH.B1M.B1"
stlat_202_b1.ps_id = "STLAT.DIA.B1"
stgrd_203_b1.ps_id = "STGRD.G3.B1"
bam_203_b1.ps_id = "BAM.B1"
midbpmf_203_b1.ps_id = "MIDBPMF.B1"
tora_203_b1.ps_id = "TORA.B1"
eod_204_b1.ps_id = "EOD.B1"
bcm_205_b1.ps_id = "BCM.B1"
otra_206_b1.ps_id = "OTRA.B1"
engrd_206_b1.ps_id = "ENGRD.G3.B1"
stgrd_206_b1.ps_id = "STGRD.G4.B1"
match_207_b1.ps_id = "MATCH.TDS.B1"
stblock_207_b1.ps_id = "STBLOCK.DIA.B1"
engrd_209_b1.ps_id = "ENGRD.G4.B1"
stgrd_209_b1.ps_id = "STGRD.G5.B1"
engrd_214_b1.ps_id = "ENGRD.G5.B1"
stgrd_214_b1.ps_id = "STGRD.G6.B1"
match_218_b1.ps_id = "MATCH.DIA.B1"
otrb_218_b1.ps_id = "OTRB.B1"
engrd_219_b1.ps_id = "ENGRD.G6.B1"
stgrd_219_b1.ps_id = "STGRD.G7.B1"
otrb_220_b1.ps_id = "OTRB.B1"
dcm_221_b1.ps_id = "DCM.B1"
otrb_222_b1.ps_id = "OTRB.B1"
engrd_223_b1.ps_id = "ENGRD.G7.B1"
stgrd_224_b1.ps_id = "STGRD.G8.B1"
otrb_224_b1.ps_id = "OTRB.B1"
engrd_228_b1.ps_id = "ENGRD.G8.B1"
enlat_229_b1.ps_id = "ENLAT.DIA.B1"
ensub_229_b1.ps_id = "ENSUB.B1M.B1"

# Component list metadata:
# fmt: off
# Drift metadata:
vcbshut_65_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTIN_000', 'group': 'VACUUM', 'class': 'VAC', 'type': 'VCBSHUT', 'xaper': 0.04, 'yaper': 0.04}
vcdst_113_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'VACUUM', 'class': 'VAC', 'type': 'VCDST', 'xaper': 0.04, 'yaper': 0.04}
cfb_121_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CRYO', 'class': 'CRYO', 'type': 'CFB', 'xaper': 0.078, 'yaper': 0.078}
ctb_172_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CRYO', 'class': 'CRYO', 'type': 'CTB', 'xaper': 0.078, 'yaper': 0.078}
vcdst_174_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'VACUUM', 'class': 'VAC', 'type': 'VCDST', 'xaper': 0.04, 'yaper': 0.04}

# Quadrupole metadata:
qi_63_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTIN_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_66_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTIN_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_69_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_71_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_72_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_73_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_74_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_75_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_77_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_78_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_79_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_80_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_82_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_83_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_84_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_85_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_86_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_88_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_89_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_90_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_92_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_93_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_94_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_95_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_102_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_103_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_104_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_107_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_109_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_112_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_114_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_116_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_118_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
q_134_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'Q', 'xaper': 0.078, 'yaper': 0.078}
q_146_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'Q', 'xaper': 0.078, 'yaper': 0.078}
q_158_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'Q', 'xaper': 0.078, 'yaper': 0.078}
q_170_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'Q', 'xaper': 0.078, 'yaper': 0.078}
qi_176_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qd_179_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QD', 'xaper': 0.04, 'yaper': 0.04}
qd_181_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QD', 'xaper': 0.04, 'yaper': 0.04}
qi_204_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_205_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_206_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_209_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qd_210_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QD', 'xaper': 0.04, 'yaper': 0.04}
qi_211_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_213_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_215_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_217_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qd_219_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QD', 'xaper': 0.04, 'yaper': 0.04}
qd_221_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QD', 'xaper': 0.04, 'yaper': 0.04}
qd_223_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QD', 'xaper': 0.04, 'yaper': 0.04}
qi_224_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_226_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_227_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}

# SBend metadata:
bl_73_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_75_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_76_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_77_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_78_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_80_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_81_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_82_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_83_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_85_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_86_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_87_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_88_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_90_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_91_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_92_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bb_96_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BB', 'xaper': 0.04, 'yaper': 0.04}
bb_98_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BB', 'xaper': 0.04, 'yaper': 0.4}
bb_100_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BB', 'xaper': 0.04, 'yaper': 0.4}
bb_101_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BB', 'xaper': 0.04, 'yaper': 0.04}
bb_182_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BB', 'xaper': 0.04, 'yaper': 0.04}
bb_191_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BB', 'xaper': 0.04, 'yaper': 0.4}
bb_193_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BB', 'xaper': 0.04, 'yaper': 0.4}
bb_202_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BB', 'xaper': 0.04, 'yaper': 0.04}

# RBend metadata:
bseci_64_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTIN_000', 'group': 'PMAGNET', 'class': 'RBEN', 'type': 'BSECI', 'xaper': 0.04, 'yaper': 0.04}
kay_214_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'FASTKICK', 'class': 'VKIC', 'type': 'KAY', 'xaper': 0.04, 'yaper': 0.04}
kay_216_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'FASTKICK', 'class': 'VKIC', 'type': 'KAY', 'xaper': 0.04, 'yaper': 0.04}
kay_218_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'FASTKICK', 'class': 'VKIC', 'type': 'KAY', 'xaper': 0.04, 'yaper': 0.04}
kay_219_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'FASTKICK', 'class': 'VKIC', 'type': 'KAY', 'xaper': 0.04, 'yaper': 0.04}
kax_225_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'FASTKICK', 'class': 'HKIC', 'type': 'KAX', 'xaper': 0.04, 'yaper': 0.04}
kax_226_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'FASTKICK', 'class': 'HKIC', 'type': 'KAX', 'xaper': 0.04, 'yaper': 0.04}

# Sextupole metadata:
sc_74i_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_74ii_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_76_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_77_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_79i_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_79ii_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_81_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_82_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_84i_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_84ii_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_86_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_87_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_89i_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_89ii_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_91_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}
sc_92_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SC', 'xaper': 0.04, 'yaper': 0.04}

# Hcor metadata:
cbb_62_i1d.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTIN_000', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CBB', 'xaper': 0.04, 'yaper': 0.04}
cix_65_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTIN_000', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_73i_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_73ii_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_76_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_78_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_81_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_83_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_86_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_88_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_90_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_95_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_102_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_104_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_109_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_114_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_118_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cx_134_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CX', 'xaper': 0.078, 'yaper': 0.078}
cx_146_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CX', 'xaper': 0.078, 'yaper': 0.078}
cx_158_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CX', 'xaper': 0.078, 'yaper': 0.078}
cx_170_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CX', 'xaper': 0.078, 'yaper': 0.078}
cix_177_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
ccx_179_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CCX', 'xaper': 0.04, 'yaper': 0.04}
cix_205_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_209_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_213_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cix_216_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CIX', 'xaper': 0.04, 'yaper': 0.04}
cfx_223_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cfx_226_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}

# Vcor metadata:
ciy_63_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTIN_000', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
ciy_72_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
cbl_73_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CBL', 'xaper': 0.04, 'yaper': 0.04}
ciy_75_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
cbl_78_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CBL', 'xaper': 0.04, 'yaper': 0.04}
ciy_80_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
cbl_83_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CBL', 'xaper': 0.04, 'yaper': 0.04}
ciy_85_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
cbl_88_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CBL', 'xaper': 0.04, 'yaper': 0.04}
cbl_90_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CBL', 'xaper': 0.04, 'yaper': 0.04}
ciy_92_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
ciy_94_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
cbb_98_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CBB', 'xaper': 0.04, 'yaper': 0.4}
cbb_100_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CBB', 'xaper': 0.04, 'yaper': 0.4}
cbb_101_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CBB', 'xaper': 0.04, 'yaper': 0.04}
ciy_103_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
ciy_107_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
ciy_112_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
ciy_116_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
cy_134_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CY', 'xaper': 0.078, 'yaper': 0.078}
cy_146_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CY', 'xaper': 0.078, 'yaper': 0.078}
cy_158_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CY', 'xaper': 0.078, 'yaper': 0.078}
cy_170_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CY', 'xaper': 0.078, 'yaper': 0.078}
ciy_176_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
ccy_181_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CCY', 'xaper': 0.04, 'yaper': 0.04}
cbb_191_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CBB', 'xaper': 0.04, 'yaper': 0.4}
cbb_193_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CBB', 'xaper': 0.04, 'yaper': 0.4}
cbb_202_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CBB', 'xaper': 0.04, 'yaper': 0.04}
ciy_204_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
ccy_210_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CCY', 'xaper': 0.04, 'yaper': 0.04}
ciy_214_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}
ccy_217_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CCY', 'xaper': 0.04, 'yaper': 0.04}
ccy_221_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CCY', 'xaper': 0.04, 'yaper': 0.04}
ciy_226_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CIY', 'xaper': 0.04, 'yaper': 0.04}

# Cavity metadata:
c_a2_1_1_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_1_2_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_1_3_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_1_4_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_1_5_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_1_6_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_1_7_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_1_8_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_2_1_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_2_2_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_2_3_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_2_4_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_2_5_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_2_6_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_2_7_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_2_8_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_3_1_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_3_2_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_3_3_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_3_4_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_3_5_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_3_6_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_3_7_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_3_8_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_4_1_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_4_2_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_4_3_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_4_4_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_4_5_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_4_6_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_4_7_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}
c_a2_4_8_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'C', 'xaper': 0.078, 'yaper': 0.078}

# TDCavity metadata:
tdsb_208_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'CAVITY', 'class': 'LCAV', 'type': 'TDSB', 'xaper': 0.04, 'yaper': 0.04}

# Monitor metadata:
bpma_63_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTIN_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_72_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_75_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_77_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_80_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_82_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_85_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_87_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_90_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_92_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpmf_95_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMF', 'xaper': 0.04, 'yaper': 0.04}
bpms_99_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMS', 'xaper': 0.04, 'yaper': 0.4}
bpmf_103_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMF', 'xaper': 0.04, 'yaper': 0.04}
bpma_103_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_105_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_107_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_110_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_112_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_115_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_117_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_119_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpmc_134_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMC', 'xaper': 0.078, 'yaper': 0.078}
bpmr_146_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMR', 'xaper': 0.078, 'yaper': 0.078}
bpmc_158_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMC', 'xaper': 0.078, 'yaper': 0.078}
bpmr_170_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMR', 'xaper': 0.078, 'yaper': 0.078}
bpma_175_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_179_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpmf_181_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMF', 'xaper': 0.04, 'yaper': 0.04}
bpms_192_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMS', 'xaper': 0.04, 'yaper': 0.4}
bpmf_203_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMF', 'xaper': 0.04, 'yaper': 0.04}
bpma_206_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_210_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_213_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_215_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_217_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_219_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_221_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_223_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_226_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_227_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}

# Marker metadata:
stsub_62_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTIN_000', 'group': 'MARK', 'class': 'MARK', 'type': 'STSUB', 'xaper': 0.04, 'yaper': 0.04}
stlat_73_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'MARK', 'type': 'STLAT', 'xaper': 0.04, 'yaper': 0.04}
match_73_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'MARK', 'type': 'MATCH', 'xaper': 0.04, 'yaper': 0.04}
mbl_73a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_73d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_75a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_75d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_76a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_76d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_77a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_77d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_78a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_78d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_80a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_80d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_81a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_81d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_82a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_82d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_83a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_83d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_85a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_85d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_86a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_86d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_87a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_87d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_88a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_88d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XSE_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_90a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_90d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_91a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_91d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_92a_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_92d_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
enlat_93_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'ENLAT', 'xaper': 0.04, 'yaper': 0.04}
ensub_93_i1.metadata = {'section': 'I1', 'subsection': 'I1T', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'ENSUB', 'xaper': 0.04, 'yaper': 0.04}
stsub_93_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'STSUB', 'xaper': 0.04, 'yaper': 0.04}
tora_94_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'CM', 'type': 'TORA', 'xaper': 0.04, 'yaper': 0.04}
midbpmf_95_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'MIDBPMF', 'xaper': 0.04, 'yaper': 0.04}
stlat_96_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'STLAT', 'xaper': 0.04, 'yaper': 0.04}
mbb_96a_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbb_96d_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
vcst40t400y_96_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST40T400Y', 'xaper': 0.04, 'yaper': 0.04}
vcst400y_97_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST400Y', 'xaper': 0.04, 'yaper': 0.4}
mbb_98a_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.4}
mbb_98d_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.4}
colo_98_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'VACUUM', 'class': 'ECOL', 'type': 'COLO', 'xaper': 0.04, 'yaper': 0.4}
colu_98_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'VACUUM', 'class': 'ECOL', 'type': 'COLU', 'xaper': 0.04, 'yaper': 0.4}
otrs_99_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRS', 'xaper': 0.04, 'yaper': 0.4}
mbb_100a_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.4}
mbb_100d_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.4}
vcst400yt40_100_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST400YT40', 'xaper': 0.04, 'yaper': 0.04}
vcst40y_101_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST40Y', 'xaper': 0.04, 'yaper': 0.04}
mbb_101a_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbb_101d_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
enlat_101_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'ENLAT', 'xaper': 0.04, 'yaper': 0.04}
midbpmf_103_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'MIDBPMF', 'xaper': 0.04, 'yaper': 0.04}
stlat_104_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'STLAT', 'xaper': 0.04, 'yaper': 0.04}
match_104_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'MATCH', 'xaper': 0.04, 'yaper': 0.04}
enlat_114_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'ENLAT', 'xaper': 0.04, 'yaper': 0.04}
tora_116_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'CM', 'type': 'TORA', 'xaper': 0.04, 'yaper': 0.04}
otra_118_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRA', 'xaper': 0.04, 'yaper': 0.04}
dcm_118_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'DIAG', 'class': 'INSTR', 'type': 'DCM', 'xaper': 0.04, 'yaper': 0.04}
ensub_119_i1.metadata = {'section': 'I1', 'subsection': 'B0', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'ENSUB', 'xaper': 0.04, 'yaper': 0.04}
ensec_119_i1.metadata = {'section': 'I1', 'subsection': 'I1', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'ENSEC', 'xaper': 0.04, 'yaper': 0.04}
stsec_119_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'STSEC', 'xaper': 0.04, 'yaper': 0.04}
vcst40t78_119_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST40T78', 'xaper': 0.078, 'yaper': 0.078}
stac_122_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'STAC', 'xaper': 0.078, 'yaper': 0.078}
enac_134_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'ENAC', 'xaper': 0.078, 'yaper': 0.078}
stac_134_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_001', 'group': 'MARK', 'class': 'MARK', 'type': 'STAC', 'xaper': 0.078, 'yaper': 0.078}
enac_146_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'ENAC', 'xaper': 0.078, 'yaper': 0.078}
stac_146_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'STAC', 'xaper': 0.078, 'yaper': 0.078}
enac_158_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'ENAC', 'xaper': 0.078, 'yaper': 0.078}
stac_158_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'STAC', 'xaper': 0.078, 'yaper': 0.078}
enac_170_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'ENAC', 'xaper': 0.078, 'yaper': 0.078}
vcst78t40_174_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST78T40', 'xaper': 0.04, 'yaper': 0.04}
ensec_174_l1.metadata = {'section': 'L1', 'subsection': 'L1', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'ENSEC', 'xaper': 0.04, 'yaper': 0.04}
stsec_174_b1.metadata = {'section': 'B1', 'subsection': 'B1', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'STSEC', 'xaper': 0.04, 'yaper': 0.04}
stsub_174_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'STSUB', 'xaper': 0.04, 'yaper': 0.04}
match_174_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'MATCH', 'xaper': 0.04, 'yaper': 0.04}
stgrd_175_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'STGRD', 'xaper': 0.04, 'yaper': 0.04}
tora_175_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'CM', 'type': 'TORA', 'xaper': 0.04, 'yaper': 0.04}
dcm_176_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'INSTR', 'type': 'DCM', 'xaper': 0.04, 'yaper': 0.04}
engrd_178_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'ENGRD', 'xaper': 0.04, 'yaper': 0.04}
stgrd_178_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'STGRD', 'xaper': 0.04, 'yaper': 0.04}
eod_179_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'INSTR', 'type': 'EOD', 'xaper': 0.04, 'yaper': 0.04}
bcm_180_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'INSTR', 'type': 'BCM', 'xaper': 0.04, 'yaper': 0.04}
otra_180_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRA', 'xaper': 0.04, 'yaper': 0.04}
bam_181_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'INSTR', 'type': 'BAM', 'xaper': 0.04, 'yaper': 0.04}
midbpmf_181_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'MIDBPMF', 'xaper': 0.04, 'yaper': 0.04}
engrd_181_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'ENGRD', 'xaper': 0.04, 'yaper': 0.04}
stlat_182_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'MARK', 'type': 'STLAT', 'xaper': 0.04, 'yaper': 0.04}
mbb_182a_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbb_182d_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
vcst40t400y_182_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST40T400Y', 'xaper': 0.04, 'yaper': 0.04}
vcst400y_191_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST400Y', 'xaper': 0.04, 'yaper': 0.4}
mbb_191a_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.4}
mbb_191d_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.4}
colo_192_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'VACUUM', 'class': 'ECOL', 'type': 'COLO', 'xaper': 0.04, 'yaper': 0.4}
colu_192_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'VACUUM', 'class': 'ECOL', 'type': 'COLU', 'xaper': 0.04, 'yaper': 0.4}
otrs_192_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRS', 'xaper': 0.04, 'yaper': 0.4}
mbb_193a_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_002', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.4}
mbb_193d_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.4}
vcst400yt40_193_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST400YT40', 'xaper': 0.04, 'yaper': 0.04}
srm_194_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'INSTR', 'type': 'SRM', 'xaper': 0.04, 'yaper': 0.04}
vcst40y_202_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST40Y', 'xaper': 0.04, 'yaper': 0.04}
mbb_202a_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbb_202d_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
enlat_202_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'ENLAT', 'xaper': 0.04, 'yaper': 0.04}
match_202_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'MATCH', 'xaper': 0.04, 'yaper': 0.04}
stlat_202_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'STLAT', 'xaper': 0.04, 'yaper': 0.04}
stgrd_203_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'STGRD', 'xaper': 0.04, 'yaper': 0.04}
bam_203_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'INSTR', 'type': 'BAM', 'xaper': 0.04, 'yaper': 0.04}
midbpmf_203_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'MIDBPMF', 'xaper': 0.04, 'yaper': 0.04}
tora_203_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'CM', 'type': 'TORA', 'xaper': 0.04, 'yaper': 0.04}
eod_204_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'INSTR', 'type': 'EOD', 'xaper': 0.04, 'yaper': 0.04}
bcm_205_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'INSTR', 'type': 'BCM', 'xaper': 0.04, 'yaper': 0.04}
otra_206_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRA', 'xaper': 0.04, 'yaper': 0.04}
engrd_206_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'ENGRD', 'xaper': 0.04, 'yaper': 0.04}
stgrd_206_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'STGRD', 'xaper': 0.04, 'yaper': 0.04}
match_207_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'MATCH', 'xaper': 0.04, 'yaper': 0.04}
stblock_207_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'STBLOCK', 'xaper': 0.04, 'yaper': 0.04}
engrd_209_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'ENGRD', 'xaper': 0.04, 'yaper': 0.04}
stgrd_209_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'STGRD', 'xaper': 0.04, 'yaper': 0.04}
engrd_214_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'ENGRD', 'xaper': 0.04, 'yaper': 0.04}
stgrd_214_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'STGRD', 'xaper': 0.04, 'yaper': 0.04}
match_218_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'MATCH', 'xaper': 0.04, 'yaper': 0.04}
otrb_218_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRB', 'xaper': 0.04, 'yaper': 0.04}
engrd_219_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'ENGRD', 'xaper': 0.04, 'yaper': 0.04}
stgrd_219_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'STGRD', 'xaper': 0.04, 'yaper': 0.04}
otrb_220_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRB', 'xaper': 0.04, 'yaper': 0.04}
dcm_221_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'INSTR', 'type': 'DCM', 'xaper': 0.04, 'yaper': 0.04}
otrb_222_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRB', 'xaper': 0.04, 'yaper': 0.04}
engrd_223_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'ENGRD', 'xaper': 0.04, 'yaper': 0.04}
stgrd_224_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'STGRD', 'xaper': 0.04, 'yaper': 0.04}
otrb_224_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRB', 'xaper': 0.04, 'yaper': 0.04}
engrd_228_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'ENGRD', 'xaper': 0.04, 'yaper': 0.04}
enlat_229_b1.metadata = {'section': 'B1', 'subsection': 'B1M', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'ENLAT', 'xaper': 0.04, 'yaper': 0.04}
# fmt: on
