# Converted from component_list_2026.01.21.xls

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
twiss0.alpha_x = 0.23963274967383724
twiss0.alpha_y = -2.1841621855227062
twiss0.beta_x = 3.0206082389378044
twiss0.beta_y = 7.034952481825338
twiss0.s = 38.889005


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
d_16 = Drift(l=5.099999999913507e-05, eid="D_16")
d_17 = Drift(l=5.100000000196614e-05, eid="D_17")
d_18 = Drift(l=0.13500000000000512, eid="D_18")
d_19 = Drift(l=0.23943199999999507, eid="D_19")
d_20 = Drift(l=0.07509999999999714, eid="D_20")
d_21 = Drift(l=0.07510000000000286, eid="D_21")
d_22 = Drift(l=0.13493199999999725, eid="D_22")
d_23 = Drift(l=8.000000001118224e-06, eid="D_23")
d_24 = Drift(l=6.999999999368622e-06, eid="D_24")
d_25 = Drift(l=0.15860899999999845, eid="D_25")
d_26 = Drift(l=0.1325000000000074, eid="D_26")
d_27 = Drift(l=0.09864999999999355, eid="D_27")
d_28 = Drift(l=0.11615000000000844, eid="D_28")
d_29 = Drift(l=0.2736079999999902, eid="D_29")
d_30 = Drift(l=7.000000003642981e-06, eid="D_30")
d_31 = Drift(l=7.999999996843865e-06, eid="D_31")
d_32 = Drift(l=0.13493200000000627, eid="D_32")
d_33 = Drift(l=0.07509999999999714, eid="D_33")
d_34 = Drift(l=0.07510000000000286, eid="D_34")
d_35 = Drift(l=0.3244319999999997, eid="D_35")
d_36 = Drift(l=0.14999999999999858, eid="D_36")
d_37 = Drift(l=5.099999999913507e-05, eid="D_37")
d_38 = Drift(l=5.199999999944138e-05, eid="D_38")
d_39 = Drift(l=0.18237599999999787, eid="D_39")
d_40 = Drift(l=0.18237699999999915, eid="D_40")
d_41 = Drift(l=5.200000000371574e-05, eid="D_41")
d_42 = Drift(l=5.100000000196614e-05, eid="D_42")
d_43 = Drift(l=0.134999999999998, eid="D_43")
d_44 = Drift(l=0.23943200000000217, eid="D_44")
d_45 = Drift(l=0.07509999999999714, eid="D_45")
d_46 = Drift(l=0.07510000000000286, eid="D_46")
d_47 = Drift(l=0.13493199999999725, eid="D_47")
d_48 = Drift(l=6.999999996537554e-06, eid="D_48")
d_49 = Drift(l=8.000000003949292e-06, eid="D_49")
d_50 = Drift(l=0.15860800000000097, eid="D_50")
d_51 = Drift(l=0.13250000000000028, eid="D_51")
d_52 = Drift(l=0.09864999999999355, eid="D_52")
d_53 = Drift(l=0.11615000000000844, eid="D_53")
d_54 = Drift(l=0.2736089999999948, eid="D_54")
d_55 = Drift(l=6.999999996537554e-06, eid="D_55")
d_56 = Drift(l=8.000000003949292e-06, eid="D_56")
d_57 = Drift(l=0.13493199999999916, eid="D_57")
d_58 = Drift(l=0.07509999999999714, eid="D_58")
d_59 = Drift(l=0.07510000000000286, eid="D_59")
d_60 = Drift(l=0.32443100000000225, eid="D_60")
d_61 = Drift(l=0.14999999999999858, eid="D_61")
d_62 = Drift(l=5.199999999661031e-05, eid="D_62")
d_63 = Drift(l=5.100000000196614e-05, eid="D_63")
d_64 = Drift(l=0.18237700000000245, eid="D_64")
d_65 = Drift(l=0.18237699999999915, eid="D_65")
d_66 = Drift(l=5.099999999913507e-05, eid="D_66")
d_67 = Drift(l=5.199999999944138e-05, eid="D_67")
d_68 = Drift(l=0.13500000000000512, eid="D_68")
d_69 = Drift(l=0.2394309999999976, eid="D_69")
d_70 = Drift(l=0.07509999999999714, eid="D_70")
d_71 = Drift(l=0.07510000000000286, eid="D_71")
d_72 = Drift(l=0.13493199999999725, eid="D_72")
d_73 = Drift(l=8.000000001118224e-06, eid="D_73")
d_74 = Drift(l=6.999999999368622e-06, eid="D_74")
d_75 = Drift(l=0.15860899999999845, eid="D_75")
d_76 = Drift(l=0.1325000000000074, eid="D_76")
d_77 = Drift(l=0.09864999999999355, eid="D_77")
d_78 = Drift(l=0.11615000000000844, eid="D_78")
d_79 = Drift(l=0.2736079999999902, eid="D_79")
d_80 = Drift(l=8.000000001118224e-06, eid="D_80")
d_81 = Drift(l=6.999999999368622e-06, eid="D_81")
d_82 = Drift(l=0.13493200000000627, eid="D_82")
d_83 = Drift(l=0.07509999999999714, eid="D_83")
d_84 = Drift(l=0.07509999999999575, eid="D_84")
d_85 = Drift(l=0.3244319999999997, eid="D_85")
d_86 = Drift(l=0.15000000000000568, eid="D_86")
d_87 = Drift(l=5.200000001082117e-05, eid="D_87")
d_88 = Drift(l=5.0999999987755285e-05, eid="D_88")
d_89 = Drift(l=0.18237700000000245, eid="D_89")
d_90 = Drift(l=0.18237599999999457, eid="D_90")
d_91 = Drift(l=5.200000001082117e-05, eid="D_91")
d_92 = Drift(l=5.0999999987755285e-05, eid="D_92")
d_93 = Drift(l=0.13500000000000512, eid="D_93")
d_94 = Drift(l=0.23943200000000217, eid="D_94")
d_95 = Drift(l=0.07510000000000425, eid="D_95")
d_96 = Drift(l=0.07509999999999575, eid="D_96")
d_97 = Drift(l=0.13493199999999014, eid="D_97")
d_98 = Drift(l=7.000000010748408e-06, eid="D_98")
d_99 = Drift(l=7.999999996843865e-06, eid="D_99")
d_100 = Drift(l=0.15860800000000097, eid="D_100")
d_101 = Drift(l=0.1325000000000074, eid="D_101")
d_102 = Drift(l=0.09865000000000065, eid="D_102")
d_103 = Drift(l=0.48975899999999606, eid="D_103")
d_104 = Drift(l=6.999999996537554e-06, eid="D_104")
d_105 = Drift(l=7.999999996843865e-06, eid="D_105")
d_106 = Drift(l=0.13493200000000627, eid="D_106")
d_107 = Drift(l=0.07510000000000425, eid="D_107")
d_108 = Drift(l=0.07509999999999575, eid="D_108")
d_109 = Drift(l=0.09193199999999799, eid="D_109")
d_110 = Drift(l=0.1325000000000017, eid="D_110")
d_111 = Drift(l=0.14999999999999147, eid="D_111")
d_112 = Drift(l=5.1000000013345925e-05, eid="D_112")
d_113 = Drift(l=5.0999999987755285e-05, eid="D_113")
d_114 = Drift(l=0.18237700000000245, eid="D_114")
d_115 = Drift(l=0.8812799999999896, eid="D_115")
d_116 = Drift(l=0.20000000000000284, eid="D_116")
d_117 = Drift(l=0.09115000000000748, eid="D_117")
d_118 = Drift(l=0.28115000000000046, eid="D_118")
d_119 = Drift(l=0.09599999999998943, eid="D_119")
d_120 = Drift(l=0.20400000000000773, eid="D_120")
d_121 = Drift(l=0.09115000000000748, eid="D_121")
d_122 = Drift(l=0.38114999999999477, eid="D_122")
d_123 = Drift(l=0.09999999999999432, eid="D_123")
d_124 = Drift(l=0.0005969999999990705, eid="D_124")
d_125 = Drift(l=0.0005960000000015953, eid="D_125")
d_126 = Drift(l=1.0071920000000034, eid="D_126")
d_127 = Drift(l=0.0005960000000015953, eid="D_127")
d_128 = Drift(l=0.0005969999999990705, eid="D_128")
d_129 = Drift(l=0.39749999999999375, eid="D_129")
d_130 = Drift(l=0.08500000000000796, eid="D_130")
d_131 = Drift(l=0.3824999999999932, eid="D_131")
d_132 = Drift(l=0.3100000000000023, eid="D_132")
d_133 = Drift(l=0.32500000000000284, eid="D_133")
d_134 = Drift(l=0.0005969999999990705, eid="D_134")
d_135 = Drift(l=0.0005969999999990705, eid="D_135")
d_136 = Drift(l=1.007191000000006, eid="D_136")
d_137 = Drift(l=0.0005969999999990705, eid="D_137")
d_138 = Drift(l=0.0005959999999873844, eid="D_138")
d_139 = Drift(l=0.10000000000000853, eid="D_139")
d_140 = Drift(l=0.3911499999999961, eid="D_140")
d_141 = Drift(l=0.09115000000000276, eid="D_141")
d_142 = Drift(l=0.2499999999999943, eid="D_142")
d_143 = Drift(l=0.09600000000000364, eid="D_143")
d_144 = Drift(l=0.14400000000000546, eid="D_144")
d_145 = Drift(l=0.09115000000000748, eid="D_145")
d_146 = Drift(l=0.18114999999999196, eid="D_146")
d_147 = Drift(l=0.5600000000000023, eid="D_147")
d_148 = Drift(l=0.09114999999999326, eid="D_148")
d_149 = Drift(l=0.18115000000000236, eid="D_149")
d_150 = Drift(l=1.8900000000000006, eid="D_150")
d_151 = Drift(l=0.09114999999999326, eid="D_151")
d_152 = Drift(l=0.18115000000000617, eid="D_152")
d_153 = Drift(l=1.8900000000000006, eid="D_153")
d_154 = Drift(l=0.09114999999999326, eid="D_154")
d_155 = Drift(l=0.18115000000000617, eid="D_155")
d_156 = Drift(l=1.8900000000000006, eid="D_156")
d_157 = Drift(l=0.09114999999999326, eid="D_157")
d_158 = Drift(l=0.18115000000000617, eid="D_158")
d_159 = Drift(l=0.4999999999999858, eid="D_159")
vcdst_113_i1 = Drift(l=1.215, eid="VCDST.113.I1")
d_160 = Drift(l=0.3250000000000062, eid="D_160")
d_161 = Drift(l=0.09115000000000748, eid="D_161")
d_162 = Drift(l=0.18114999999999196, eid="D_162")
d_163 = Drift(l=1.1242000000000019, eid="D_163")
d_164 = Drift(l=0.1407999999999987, eid="D_164")
d_165 = Drift(l=0.09115000000000748, eid="D_165")
d_166 = Drift(l=0.13964999999999275, eid="D_166")
d_167 = Drift(l=1.091319999999996, eid="D_167")
d_168 = Drift(l=0.3490300000000133, eid="D_168")
d_169 = Drift(l=0.09114999999999895, eid="D_169")
d_170 = Drift(l=0.09114999999999326, eid="D_170")
d_171 = Drift(l=0.1439500000000076, eid="D_171")
d_172 = Drift(l=0.3521999999999963, eid="D_172")
cfb_121_l1 = Drift(l=3.35, eid="CFB.121.L1")
d_173 = Drift(l=0.22160100000000682, eid="D_173")
d_174 = Drift(l=0.3458989999999895, eid="D_174")
d_175 = Drift(l=0.3459000000000012, eid="D_175")
d_176 = Drift(l=0.3459000000000012, eid="D_176")
d_177 = Drift(l=0.3459000000000012, eid="D_177")
d_178 = Drift(l=0.3459000000000012, eid="D_178")
d_179 = Drift(l=0.3459000000000012, eid="D_179")
d_180 = Drift(l=0.3459009999999987, eid="D_180")
d_181 = Drift(l=0.24749899999999148, eid="D_181")
d_182 = Drift(l=0.04320100000001004, eid="D_182")
d_183 = Drift(l=0.08499899999999627, eid="D_183")
d_184 = Drift(l=0.4579010000000068, eid="D_184")
d_185 = Drift(l=0.22159999999999513, eid="D_185")
d_186 = Drift(l=0.3459000000000012, eid="D_186")
d_187 = Drift(l=0.3459000000000012, eid="D_187")
d_188 = Drift(l=0.3459000000000012, eid="D_188")
d_189 = Drift(l=0.3459000000000012, eid="D_189")
d_190 = Drift(l=0.3458989999999895, eid="D_190")
d_191 = Drift(l=0.3459000000000012, eid="D_191")
d_192 = Drift(l=0.3459000000000012, eid="D_192")
d_193 = Drift(l=0.24750000000000316, eid="D_193")
d_194 = Drift(l=0.04319999999999835, eid="D_194")
d_195 = Drift(l=0.08500100000000543, eid="D_195")
d_196 = Drift(l=0.4578989999999976, eid="D_196")
d_197 = Drift(l=0.22159999999999513, eid="D_197")
d_198 = Drift(l=0.3459000000000012, eid="D_198")
d_199 = Drift(l=0.3459000000000012, eid="D_199")
d_200 = Drift(l=0.3459010000000129, eid="D_200")
d_201 = Drift(l=0.3459000000000012, eid="D_201")
d_202 = Drift(l=0.3459000000000012, eid="D_202")
d_203 = Drift(l=0.3459000000000012, eid="D_203")
d_204 = Drift(l=0.3459000000000012, eid="D_204")
d_205 = Drift(l=0.24750000000000316, eid="D_205")
d_206 = Drift(l=0.043198999999972454, eid="D_206")
d_207 = Drift(l=0.08500000000000796, eid="D_207")
d_208 = Drift(l=0.4578999999999951, eid="D_208")
d_209 = Drift(l=0.22160100000002103, eid="D_209")
d_210 = Drift(l=0.3459000000000012, eid="D_210")
d_211 = Drift(l=0.3459000000000012, eid="D_211")
d_212 = Drift(l=0.3459000000000012, eid="D_212")
d_213 = Drift(l=0.3459000000000012, eid="D_213")
d_214 = Drift(l=0.3459000000000012, eid="D_214")
d_215 = Drift(l=0.3459000000000012, eid="D_215")
d_216 = Drift(l=0.3459000000000012, eid="D_216")
d_217 = Drift(l=0.24749899999997726, eid="D_217")
d_218 = Drift(l=0.04319999999999835, eid="D_218")
d_219 = Drift(l=0.08500100000000543, eid="D_219")
d_220 = Drift(l=0.4578999999999951, eid="D_220")
ctb_172_l1 = Drift(l=3.25, eid="CTB.172.L1")
d_221 = Drift(l=0.12573000000000434, eid="D_221")
vcdst_174_b1 = Drift(l=1.215, eid="VCDST.174.B1")
d_222 = Drift(l=0.07426899999999015, eid="D_222")
d_223 = Drift(l=0.13100000000000023, eid="D_223")
d_224 = Drift(l=0.24800100000001635, eid="D_224")
d_225 = Drift(l=0.15214999999997758, eid="D_225")
d_226 = Drift(l=0.08214900000000494, eid="D_226")
d_227 = Drift(l=0.3689999999999941, eid="D_227")
d_228 = Drift(l=0.8460010000000011, eid="D_228")
d_229 = Drift(l=0.8840000000000089, eid="D_229")
d_230 = Drift(l=0.05000000000001137, eid="D_230")
d_231 = Drift(l=0.3299989999999866, eid="D_231")
d_232 = Drift(l=0.34900100000001544, eid="D_232")
d_233 = Drift(l=0.15264999999999418, eid="D_233")
d_234 = Drift(l=0.13164899999999494, eid="D_234")
d_235 = Drift(l=0.15000099999999747, eid="D_235")
d_236 = Drift(l=0.5, eid="D_236")
d_237 = Drift(l=0.23164900000000443, eid="D_237")
d_238 = Drift(l=0.10164999999999128, eid="D_238")
d_239 = Drift(l=0.10300000000000295, eid="D_239")
d_240 = Drift(l=0.2524999999999977, eid="D_240")
d_241 = Drift(l=0.09600000000000364, eid="D_241")
d_242 = Drift(l=0.07849999999999113, eid="D_242")
d_243 = Drift(l=0.25, eid="D_243")
d_244 = Drift(l=0.10000100000002021, eid="D_244")
d_245 = Drift(l=0.00010399999999322063, eid="D_245")
d_246 = Drift(l=0.00010399999999322063, eid="D_246")
d_247 = Drift(l=8.510621000000015, eid="D_247")
d_248 = Drift(l=0.00010399999999322063, eid="D_248")
d_249 = Drift(l=0.00010399999999322063, eid="D_249")
d_250 = Drift(l=0.39750000000000796, eid="D_250")
d_251 = Drift(l=0.08500000000000796, eid="D_251")
d_252 = Drift(l=0.3824999999999932, eid="D_252")
d_253 = Drift(l=0.3100000000000023, eid="D_253")
d_254 = Drift(l=0.32499999999998863, eid="D_254")
d_255 = Drift(l=0.00010399999999322063, eid="D_255")
d_256 = Drift(l=0.00010400000002164234, eid="D_256")
d_257 = Drift(l=1.0547759999999755, eid="D_257")
d_258 = Drift(l=7.455845000000011, eid="D_258")
d_259 = Drift(l=0.00010399999999322063, eid="D_259")
d_260 = Drift(l=0.00010400000002164234, eid="D_260")
d_261 = Drift(l=0.09999999999999432, eid="D_261")
d_262 = Drift(l=0.29999999999998295, eid="D_262")
d_263 = Drift(l=0.12250000000000227, eid="D_263")
d_264 = Drift(l=0.1564999999999941, eid="D_264")
d_265 = Drift(l=0.09600000000000364, eid="D_265")
d_266 = Drift(l=0.35480000000001155, eid="D_266")
d_267 = Drift(l=0.15419999999997458, eid="D_267")
d_268 = Drift(l=0.09715000000002191, eid="D_268")
d_269 = Drift(l=0.4421499999999876, eid="D_269")
d_270 = Drift(l=0.2230000000000132, eid="D_270")
d_271 = Drift(l=0.09714999999999349, eid="D_271")
d_272 = Drift(l=0.15015000000001447, eid="D_272")
d_273 = Drift(l=0.47299999999998477, eid="D_273")
d_274 = Drift(l=0.10800000000000409, eid="D_274")
d_275 = Drift(l=0.05000000000001137, eid="D_275")
d_276 = Drift(l=0.3779999999999859, eid="D_276")
d_277 = Drift(l=0.15315000000001078, eid="D_277")
d_278 = Drift(l=0.08114999999999764, eid="D_278")
d_279 = Drift(l=0.09999999999999432, eid="D_279")
d_280 = Drift(l=0.18115000000000236, eid="D_280")
d_281 = Drift(l=0.28115000000001467, eid="D_281")
d_282 = Drift(l=0.14999999999997726, eid="D_282")
d_283 = Drift(l=0.09999999999999432, eid="D_283")
d_284 = Drift(l=0.37900000000001344, eid="D_284")
d_285 = Drift(l=0.1526500000000226, eid="D_285")
d_286 = Drift(l=0.131649999999964, eid="D_286")
d_287 = Drift(l=1.0311500000000193, eid="D_287")
d_288 = Drift(l=1.23014999999997, eid="D_288")
d_289 = Drift(l=0.18000000000002955, eid="D_289")
d_290 = Drift(l=0.15214999999997758, eid="D_290")
d_291 = Drift(l=0.08114999999999764, eid="D_291")
d_292 = Drift(l=0.0500000000000341, eid="D_292")
d_293 = Drift(l=0.19999999999998863, eid="D_293")
d_294 = Drift(l=0.14999999999997726, eid="D_294")
d_295 = Drift(l=0.5790000000000305, eid="D_295")
d_296 = Drift(l=0.15214999999997758, eid="D_296")
d_297 = Drift(l=0.09714999999998877, eid="D_297")
d_298 = Drift(l=0.21500000000002614, eid="D_298")
d_299 = Drift(l=0.5009999999999991, eid="D_299")
d_300 = Drift(l=0.14699999999998567, eid="D_300")
d_301 = Drift(l=0.152150000000006, eid="D_301")
d_302 = Drift(l=0.12515000000000878, eid="D_302")
d_303 = Drift(l=0.3559999999999889, eid="D_303")
d_304 = Drift(l=0.4000000000000057, eid="D_304")
d_305 = Drift(l=0.20000000000001705, eid="D_305")
d_306 = Drift(l=0.09899999999998954, eid="D_306")
d_307 = Drift(l=0.13265000000001237, eid="D_307")
d_308 = Drift(l=0.12564999999996376, eid="D_308")
d_309 = Drift(l=0.3560000000000173, eid="D_309")
d_310 = Drift(l=0.679000000000002, eid="D_310")
d_311 = Drift(l=0.1526500000000226, eid="D_311")
d_312 = Drift(l=0.10764999999996308, eid="D_312")
d_313 = Drift(l=0.15418000000001938, eid="D_313")
d_314 = Drift(l=0.46981999999999857, eid="D_314")
d_315 = Drift(l=0.679000000000002, eid="D_315")
d_316 = Drift(l=0.15264999999999418, eid="D_316")
d_317 = Drift(l=0.18165000000000378, eid="D_317")
d_318 = Drift(l=0.05000000000000568, eid="D_318")
d_319 = Drift(l=0.19999999999998863, eid="D_319")
d_320 = Drift(l=0.30000000000001137, eid="D_320")
d_321 = Drift(l=0.3461499999999944, eid="D_321")
d_322 = Drift(l=0.12614999999998514, eid="D_322")
d_323 = Drift(l=0.06999999999998752, eid="D_323")
d_324 = Drift(l=0.3320000000000164, eid="D_324")
d_325 = Drift(l=0.15215100000000348, eid="D_325")
d_326 = Drift(l=0.08115099999999512, eid="D_326")
d_327 = Drift(l=0.15, eid="D_327")
d_328 = Drift(l=0.18000000000000113, eid="D_328")
d_329 = Drift(l=0.15215100000000348, eid="D_329")
d_330 = Drift(l=1.0971510000000146, eid="D_330")
d_331 = Drift(l=0.39724999999998545, eid="D_331")

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
bl_73_i1 = SBend(
    l=0.2,
    angle=-0.1109740393,
    e1=-0.05548702,
    e2=-0.05548702,
    tilt=1.570796327,
    eid="BL.73.I1",
)
bl_75_i1 = SBend(
    l=0.2,
    angle=0.0426524581,
    e1=0.021326229,
    e2=0.021326229,
    tilt=1.570796327,
    eid="BL.75.I1",
)
bl_76_i1 = SBend(
    l=0.2,
    angle=0.0426524581,
    e1=0.021326229,
    e2=0.021326229,
    tilt=1.570796327,
    eid="BL.76.I1",
)
bl_77_i1 = SBend(
    l=0.2,
    angle=-0.1109740393,
    e1=-0.05548702,
    e2=-0.05548702,
    tilt=1.570796327,
    eid="BL.77.I1",
)
bl_78_i1 = SBend(
    l=0.2,
    angle=-0.1109740393,
    e1=-0.05548702,
    e2=-0.05548702,
    tilt=1.570796327,
    eid="BL.78.I1",
)
bl_80_i1 = SBend(
    l=0.2,
    angle=0.0426524581,
    e1=0.021326229,
    e2=0.021326229,
    tilt=1.570796327,
    eid="BL.80.I1",
)
bl_81_i1 = SBend(
    l=0.2,
    angle=0.0426524581,
    e1=0.021326229,
    e2=0.021326229,
    tilt=1.570796327,
    eid="BL.81.I1",
)
bl_82_i1 = SBend(
    l=0.2,
    angle=-0.1109740393,
    e1=-0.05548702,
    e2=-0.05548702,
    tilt=1.570796327,
    eid="BL.82.I1",
)
bl_83_i1 = SBend(
    l=0.2,
    angle=0.1109740393,
    e1=0.05548702,
    e2=0.05548702,
    tilt=1.570796327,
    eid="BL.83.I1",
)
bl_85_i1 = SBend(
    l=0.2,
    angle=-0.0426524581,
    e1=-0.021326229,
    e2=-0.021326229,
    tilt=1.570796327,
    eid="BL.85.I1",
)
bl_86_i1 = SBend(
    l=0.2,
    angle=-0.0426524581,
    e1=-0.021326229,
    e2=-0.021326229,
    tilt=1.570796327,
    eid="BL.86.I1",
)
bl_87_i1 = SBend(
    l=0.2,
    angle=0.1109740393,
    e1=0.05548702,
    e2=0.05548702,
    tilt=1.570796327,
    eid="BL.87.I1",
)
bl_88_i1 = SBend(
    l=0.2,
    angle=0.1109740393,
    e1=0.05548702,
    e2=0.05548702,
    tilt=1.570796327,
    eid="BL.88.I1",
)
bl_90_i1 = SBend(
    l=0.2,
    angle=-0.0426524581,
    e1=-0.021326229,
    e2=-0.021326229,
    tilt=1.570796327,
    eid="BL.90.I1",
)
bl_91_i1 = SBend(
    l=0.2,
    angle=-0.0426524581,
    e1=-0.021326229,
    e2=-0.021326229,
    tilt=1.570796327,
    eid="BL.91.I1",
)
bl_92_i1 = SBend(
    l=0.2,
    angle=0.1109740393,
    e1=0.05548702,
    e2=0.05548702,
    tilt=1.570796327,
    eid="BL.92.I1",
)
bb_96_i1 = SBend(
    l=0.5, angle=0.11957038, e2=0.11957038, tilt=1.570796327, eid="BB.96.I1"
)
bb_98_i1 = SBend(
    l=0.5, angle=-0.11957038, e1=-0.11957038, tilt=1.570796327, eid="BB.98.I1"
)
bb_100_i1 = SBend(
    l=0.5, angle=-0.11957038, e2=-0.11957038, tilt=1.570796327, eid="BB.100.I1"
)
bb_101_i1 = SBend(
    l=0.5, angle=0.11957038, e1=0.11957038, tilt=1.570796327, eid="BB.101.I1"
)
bb_182_b1 = SBend(
    l=0.5, angle=0.04996493936, e2=0.049964939, tilt=1.570796327, eid="BB.182.B1"
)
bb_191_b1 = SBend(
    l=0.5, angle=-0.04996493936, e1=-0.049964939, tilt=1.570796327, eid="BB.191.B1"
)
bb_193_b1 = SBend(
    l=0.5, angle=-0.04996493936, e2=-0.049964939, tilt=1.570796327, eid="BB.193.B1"
)
bb_202_b1 = SBend(
    l=0.5, angle=0.04996493936, e1=0.049964939, tilt=1.570796327, eid="BB.202.B1"
)

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
sc_74ii_i1 = Sextupole(
    l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid="SC.74II.I1"
)
sc_76_i1 = Sextupole(l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid="SC.76.I1")
sc_77_i1 = Sextupole(l=0.1121, k2=-87.57825836, tilt=1.570796327, eid="SC.77.I1")
sc_79i_i1 = Sextupole(l=0.1121, k2=-87.57825836, tilt=1.570796327, eid="SC.79I.I1")
sc_79ii_i1 = Sextupole(
    l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid="SC.79II.I1"
)
sc_81_i1 = Sextupole(l=0.1121, k2=-53.061653289999995, tilt=1.570796327, eid="SC.81.I1")
sc_82_i1 = Sextupole(l=0.1121, k2=-87.57825836, tilt=1.570796327, eid="SC.82.I1")
sc_84i_i1 = Sextupole(l=0.1121, k2=87.57825836, tilt=1.570796327, eid="SC.84I.I1")
sc_84ii_i1 = Sextupole(
    l=0.1121, k2=53.061653289999995, tilt=1.570796327, eid="SC.84II.I1"
)
sc_86_i1 = Sextupole(l=0.1121, k2=53.061653289999995, tilt=1.570796327, eid="SC.86.I1")
sc_87_i1 = Sextupole(l=0.1121, k2=87.57825836, tilt=1.570796327, eid="SC.87.I1")
sc_89i_i1 = Sextupole(l=0.1121, k2=87.57825836, tilt=1.570796327, eid="SC.89I.I1")
sc_89ii_i1 = Sextupole(
    l=0.1121, k2=53.061653289999995, tilt=1.570796327, eid="SC.89II.I1"
)
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
c_a2_1_1_l1 = Cavity(
    l=1.0377,
    v=0.0214344953,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.1.1.L1",
)
c_a2_1_2_l1 = Cavity(
    l=1.0377,
    v=0.0214344953,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.1.2.L1",
)
c_a2_1_3_l1 = Cavity(
    l=1.0377,
    v=0.0214344953,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.1.3.L1",
)
c_a2_1_4_l1 = Cavity(
    l=1.0377,
    v=0.0214344953,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.1.4.L1",
)
c_a2_1_5_l1 = Cavity(
    l=1.0377,
    v=0.0214344953,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.1.5.L1",
)
c_a2_1_6_l1 = Cavity(
    l=1.0377,
    v=0.0214344953,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.1.6.L1",
)
c_a2_1_7_l1 = Cavity(
    l=1.0377,
    v=0.0214344953,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.1.7.L1",
)
c_a2_1_8_l1 = Cavity(
    l=1.0377,
    v=0.0214344953,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.1.8.L1",
)
c_a2_2_1_l1 = Cavity(
    l=1.0377,
    v=0.020463522730000003,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.2.1.L1",
)
c_a2_2_2_l1 = Cavity(
    l=1.0377,
    v=0.020463522730000003,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.2.2.L1",
)
c_a2_2_3_l1 = Cavity(
    l=1.0377,
    v=0.020463522730000003,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.2.3.L1",
)
c_a2_2_4_l1 = Cavity(
    l=1.0377,
    v=0.020463522730000003,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.2.4.L1",
)
c_a2_2_5_l1 = Cavity(
    l=1.0377,
    v=0.020463522730000003,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.2.5.L1",
)
c_a2_2_6_l1 = Cavity(
    l=1.0377,
    v=0.020463522730000003,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.2.6.L1",
)
c_a2_2_7_l1 = Cavity(
    l=1.0377,
    v=0.020463522730000003,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.2.7.L1",
)
c_a2_2_8_l1 = Cavity(
    l=1.0377,
    v=0.020463522730000003,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.2.8.L1",
)
c_a2_3_1_l1 = Cavity(
    l=1.0377,
    v=0.01914636534,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.3.1.L1",
)
c_a2_3_2_l1 = Cavity(
    l=1.0377,
    v=0.01914636534,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.3.2.L1",
)
c_a2_3_3_l1 = Cavity(
    l=1.0377,
    v=0.01914636534,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.3.3.L1",
)
c_a2_3_4_l1 = Cavity(
    l=1.0377,
    v=0.01914636534,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.3.4.L1",
)
c_a2_3_5_l1 = Cavity(
    l=1.0377,
    v=0.01914636534,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.3.5.L1",
)
c_a2_3_6_l1 = Cavity(
    l=1.0377,
    v=0.01914636534,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.3.6.L1",
)
c_a2_3_7_l1 = Cavity(
    l=1.0377,
    v=0.01914636534,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.3.7.L1",
)
c_a2_3_8_l1 = Cavity(
    l=1.0377,
    v=0.01914636534,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.3.8.L1",
)
c_a2_4_1_l1 = Cavity(
    l=1.0377,
    v=0.01757129336,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.4.1.L1",
)
c_a2_4_2_l1 = Cavity(
    l=1.0377,
    v=0.01757129336,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.4.2.L1",
)
c_a2_4_3_l1 = Cavity(
    l=1.0377,
    v=0.01757129336,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.4.3.L1",
)
c_a2_4_4_l1 = Cavity(
    l=1.0377,
    v=0.01757129336,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.4.4.L1",
)
c_a2_4_5_l1 = Cavity(
    l=1.0377,
    v=0.01757129336,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.4.5.L1",
)
c_a2_4_6_l1 = Cavity(
    l=1.0377,
    v=0.01757129336,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.4.6.L1",
)
c_a2_4_7_l1 = Cavity(
    l=1.0377,
    v=0.01757129336,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.4.7.L1",
)
c_a2_4_8_l1 = Cavity(
    l=1.0377,
    v=0.01757129336,
    phi=24.999999839999997,
    freq=1300000000.0,
    eid="C.A2.4.8.L1",
)

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
    d_16,
    bl_73_i1,
    d_17,
    mbl_73d_i1,
    cbl_73_i1,
    d_18,
    cix_73ii_i1,
    d_19,
    sc_74i_i1,
    d_20,
    qi_74_i1,
    d_21,
    sc_74ii_i1,
    d_22,
    mbl_75a_i1,
    d_23,
    bl_75_i1,
    d_24,
    mbl_75d_i1,
    d_25,
    bpma_75_i1,
    d_26,
    ciy_75_i1,
    d_27,
    qi_75_i1,
    d_28,
    cix_76_i1,
    d_29,
    mbl_76a_i1,
    d_30,
    bl_76_i1,
    d_31,
    mbl_76d_i1,
    d_32,
    sc_76_i1,
    d_33,
    qi_77_i1,
    d_34,
    sc_77_i1,
    d_35,
    bpma_77_i1,
    d_36,
    mbl_77a_i1,
    d_37,
    bl_77_i1,
    d_38,
    mbl_77d_i1,
    d_39,
    qi_78_i1,
    d_40,
    mbl_78a_i1,
    d_41,
    bl_78_i1,
    d_42,
    mbl_78d_i1,
    cbl_78_i1,
    d_43,
    cix_78_i1,
    d_44,
    sc_79i_i1,
    d_45,
    qi_79_i1,
    d_46,
    sc_79ii_i1,
    d_47,
    mbl_80a_i1,
    d_48,
    bl_80_i1,
    d_49,
    mbl_80d_i1,
    d_50,
    bpma_80_i1,
    d_51,
    ciy_80_i1,
    d_52,
    qi_80_i1,
    d_53,
    cix_81_i1,
    d_54,
    mbl_81a_i1,
    d_55,
    bl_81_i1,
    d_56,
    mbl_81d_i1,
    d_57,
    sc_81_i1,
    d_58,
    qi_82_i1,
    d_59,
    sc_82_i1,
    d_60,
    bpma_82_i1,
    d_61,
    mbl_82a_i1,
    d_62,
    bl_82_i1,
    d_63,
    mbl_82d_i1,
    d_64,
    qi_83_i1,
    d_65,
    mbl_83a_i1,
    d_66,
    bl_83_i1,
    d_67,
    mbl_83d_i1,
    cbl_83_i1,
    d_68,
    cix_83_i1,
    d_69,
    sc_84i_i1,
    d_70,
    qi_84_i1,
    d_71,
    sc_84ii_i1,
    d_72,
    mbl_85a_i1,
    d_73,
    bl_85_i1,
    d_74,
    mbl_85d_i1,
    d_75,
    bpma_85_i1,
    d_76,
    ciy_85_i1,
    d_77,
    qi_85_i1,
    d_78,
    cix_86_i1,
    d_79,
    mbl_86a_i1,
    d_80,
    bl_86_i1,
    d_81,
    mbl_86d_i1,
    d_82,
    sc_86_i1,
    d_83,
    qi_86_i1,
    d_84,
    sc_87_i1,
    d_85,
    bpma_87_i1,
    d_86,
    mbl_87a_i1,
    d_87,
    bl_87_i1,
    d_88,
    mbl_87d_i1,
    d_89,
    qi_88_i1,
    d_90,
    mbl_88a_i1,
    d_91,
    bl_88_i1,
    d_92,
    mbl_88d_i1,
    cbl_88_i1,
    d_93,
    cix_88_i1,
    d_94,
    sc_89i_i1,
    d_95,
    qi_89_i1,
    d_96,
    sc_89ii_i1,
    d_97,
    mbl_90a_i1,
    d_98,
    bl_90_i1,
    d_99,
    mbl_90d_i1,
    cbl_90_i1,
    d_100,
    bpma_90_i1,
    d_101,
    cix_90_i1,
    d_102,
    qi_90_i1,
    d_103,
    mbl_91a_i1,
    d_104,
    bl_91_i1,
    d_105,
    mbl_91d_i1,
    d_106,
    sc_91_i1,
    d_107,
    qi_92_i1,
    d_108,
    sc_92_i1,
    d_109,
    ciy_92_i1,
    d_110,
    bpma_92_i1,
    d_111,
    mbl_92a_i1,
    d_112,
    bl_92_i1,
    d_113,
    mbl_92d_i1,
    d_114,
    qi_93_i1,
    enlat_93_i1,
    ensub_93_i1,
    stsub_93_i1,
    d_115,
    tora_94_i1,
    d_116,
    ciy_94_i1,
    d_117,
    qi_94_i1,
    d_118,
    midbpmf_95_i1,
    d_119,
    bpmf_95_i1,
    d_120,
    cix_95_i1,
    d_121,
    qi_95_i1,
    d_122,
    dogleg_stop_bc0_start,
    stlat_96_i1,
    d_123,
    mbb_96a_i1,
    d_124,
    bb_96_i1,
    d_125,
    mbb_96d_i1,
    vcst40t400y_96_i1,
    d_126,
    vcst400y_97_i1,
    mbb_98a_i1,
    d_127,
    bb_98_i1,
    d_128,
    mbb_98d_i1,
    cbb_98_i1,
    d_129,
    colo_98_i1,
    d_130,
    colu_98_i1,
    d_131,
    bpms_99_i1,
    d_132,
    otrs_99_i1,
    d_133,
    mbb_100a_i1,
    d_134,
    bb_100_i1,
    d_135,
    mbb_100d_i1,
    cbb_100_i1,
    vcst400yt40_100_i1,
    d_136,
    vcst40y_101_i1,
    mbb_101a_i1,
    d_137,
    bb_101_i1,
    d_138,
    mbb_101d_i1,
    cbb_101_i1,
    d_139,
    enlat_101_i1,
    d_140,
    qi_102_i1,
    d_141,
    cix_102_i1,
    d_142,
    midbpmf_103_i1,
    d_143,
    bpmf_103_i1,
    d_144,
    ciy_103_i1,
    d_145,
    bc0_stop_l1_start,
    qi_103_i1,
    d_146,
    bpma_103_i1,
    d_147,
    cix_104_i1,
    d_148,
    qi_104_i1,
    stlat_104_i1,
    match_104_i1,
    d_149,
    bpma_105_i1,
    d_150,
    ciy_107_i1,
    d_151,
    qi_107_i1,
    d_152,
    bpma_107_i1,
    d_153,
    cix_109_i1,
    d_154,
    qi_109_i1,
    d_155,
    bpma_110_i1,
    d_156,
    ciy_112_i1,
    d_157,
    qi_112_i1,
    d_158,
    bpma_112_i1,
    d_159,
    vcdst_113_i1,
    d_160,
    enlat_114_i1,
    cix_114_i1,
    d_161,
    qi_114_i1,
    d_162,
    bpma_115_i1,
    d_163,
    tora_116_i1,
    d_164,
    ciy_116_i1,
    d_165,
    qi_116_i1,
    d_166,
    bpma_117_i1,
    d_167,
    otra_118_i1,
    d_168,
    dcm_118_i1,
    d_169,
    cix_118_i1,
    d_170,
    qi_118_i1,
    d_171,
    bpma_119_i1,
    d_172,
    ensub_119_i1,
    ensec_119_i1,
    stsec_119_l1,
    vcst40t78_119_l1,
    cfb_121_l1,
    stac_122_l1,
    d_173,
    c_a2_1_1_l1,
    d_174,
    c_a2_1_2_l1,
    d_175,
    c_a2_1_3_l1,
    d_176,
    c_a2_1_4_l1,
    d_177,
    c_a2_1_5_l1,
    d_178,
    c_a2_1_6_l1,
    d_179,
    c_a2_1_7_l1,
    d_180,
    c_a2_1_8_l1,
    d_181,
    q_134_l1,
    d_182,
    cx_134_l1,
    cy_134_l1,
    d_183,
    bpmc_134_l1,
    d_184,
    enac_134_l1,
    stac_134_l1,
    d_185,
    c_a2_2_1_l1,
    d_186,
    c_a2_2_2_l1,
    d_187,
    c_a2_2_3_l1,
    d_188,
    c_a2_2_4_l1,
    d_189,
    c_a2_2_5_l1,
    d_190,
    c_a2_2_6_l1,
    d_191,
    c_a2_2_7_l1,
    d_192,
    c_a2_2_8_l1,
    d_193,
    q_146_l1,
    d_194,
    cx_146_l1,
    cy_146_l1,
    d_195,
    bpmr_146_l1,
    d_196,
    enac_146_l1,
    stac_146_l1,
    d_197,
    c_a2_3_1_l1,
    d_198,
    c_a2_3_2_l1,
    d_199,
    c_a2_3_3_l1,
    d_200,
    c_a2_3_4_l1,
    d_201,
    c_a2_3_5_l1,
    d_202,
    c_a2_3_6_l1,
    d_203,
    c_a2_3_7_l1,
    d_204,
    c_a2_3_8_l1,
    d_205,
    q_158_l1,
    d_206,
    cx_158_l1,
    cy_158_l1,
    d_207,
    bpmc_158_l1,
    d_208,
    enac_158_l1,
    stac_158_l1,
    d_209,
    c_a2_4_1_l1,
    d_210,
    c_a2_4_2_l1,
    d_211,
    c_a2_4_3_l1,
    d_212,
    c_a2_4_4_l1,
    d_213,
    c_a2_4_5_l1,
    d_214,
    c_a2_4_6_l1,
    d_215,
    c_a2_4_7_l1,
    d_216,
    c_a2_4_8_l1,
    d_217,
    q_170_l1,
    d_218,
    cx_170_l1,
    cy_170_l1,
    d_219,
    bpmr_170_l1,
    d_220,
    enac_170_l1,
    ctb_172_l1,
    vcst78t40_174_l1,
    ensec_174_l1,
    stsec_174_b1,
    stsub_174_b1,
    match_174_b1,
    d_221,
    vcdst_174_b1,
    d_222,
    stgrd_175_b1,
    d_223,
    tora_175_b1,
    d_224,
    bpma_175_b1,
    d_225,
    qi_176_b1,
    d_226,
    ciy_176_b1,
    d_227,
    dcm_176_b1,
    d_228,
    cix_177_b1,
    d_229,
    engrd_178_b1,
    d_230,
    stgrd_178_b1,
    d_231,
    eod_179_b1,
    d_232,
    bpma_179_b1,
    d_233,
    qd_179_b1,
    d_234,
    ccx_179_b1,
    d_235,
    bcm_180_b1,
    d_236,
    otra_180_b1,
    d_237,
    qd_181_b1,
    d_238,
    ccy_181_b1,
    d_239,
    bam_181_b1,
    d_240,
    midbpmf_181_b1,
    d_241,
    bpmf_181_b1,
    d_242,
    engrd_181_b1,
    d_243,
    l1_stop_bc1_start,
    stlat_182_b1,
    d_244,
    mbb_182a_b1,
    d_245,
    bb_182_b1,
    d_246,
    mbb_182d_b1,
    vcst40t400y_182_b1,
    d_247,
    vcst400y_191_b1,
    mbb_191a_b1,
    d_248,
    bb_191_b1,
    d_249,
    mbb_191d_b1,
    cbb_191_b1,
    d_250,
    colo_192_b1,
    d_251,
    colu_192_b1,
    d_252,
    bpms_192_b1,
    d_253,
    otrs_192_b1,
    d_254,
    mbb_193a_b1,
    d_255,
    bb_193_b1,
    d_256,
    mbb_193d_b1,
    cbb_193_b1,
    vcst400yt40_193_b1,
    d_257,
    srm_194_b1,
    d_258,
    vcst40y_202_b1,
    mbb_202a_b1,
    d_259,
    bb_202_b1,
    d_260,
    mbb_202d_b1,
    cbb_202_b1,
    d_261,
    enlat_202_b1,
    match_202_b1,
    stlat_202_b1,
    d_262,
    stgrd_203_b1,
    d_263,
    bam_203_b1,
    d_264,
    bpmf_203_b1,
    d_265,
    midbpmf_203_b1,
    d_266,
    tora_203_b1,
    bc1_stop_l2_start,
    d_267,
    ciy_204_b1,
    d_268,
    qi_204_b1,
    d_269,
    eod_204_b1,
    d_270,
    cix_205_b1,
    d_271,
    qi_205_b1,
    d_272,
    bcm_205_b1,
    d_273,
    otra_206_b1,
    d_274,
    engrd_206_b1,
    d_275,
    stgrd_206_b1,
    d_276,
    bpma_206_b1,
    d_277,
    qi_206_b1,
    d_278,
    match_207_b1,
    stblock_207_b1,
    d_279,
    tdsb_208_b1,
    d_280,
    qi_209_b1,
    d_281,
    engrd_209_b1,
    d_282,
    stgrd_209_b1,
    d_283,
    cix_209_b1,
    d_284,
    bpma_210_b1,
    d_285,
    qd_210_b1,
    d_286,
    ccy_210_b1,
    d_287,
    qi_211_b1,
    d_288,
    cix_213_b1,
    d_289,
    bpma_213_b1,
    d_290,
    qi_213_b1,
    d_291,
    ciy_214_b1,
    d_292,
    engrd_214_b1,
    d_293,
    stgrd_214_b1,
    d_294,
    kay_214_b1,
    d_295,
    bpma_215_b1,
    d_296,
    qi_215_b1,
    d_297,
    cix_216_b1,
    d_298,
    kay_216_b1,
    d_299,
    ccy_217_b1,
    d_300,
    bpma_217_b1,
    d_301,
    qi_217_b1,
    d_302,
    kay_218_b1,
    d_303,
    match_218_b1,
    otrb_218_b1,
    d_304,
    engrd_219_b1,
    d_305,
    stgrd_219_b1,
    d_306,
    bpma_219_b1,
    d_307,
    qd_219_b1,
    d_308,
    kay_219_b1,
    d_309,
    otrb_220_b1,
    d_310,
    bpma_221_b1,
    d_311,
    qd_221_b1,
    d_312,
    ccy_221_b1,
    d_313,
    dcm_221_b1,
    d_314,
    otrb_222_b1,
    d_315,
    bpma_223_b1,
    d_316,
    qd_223_b1,
    d_317,
    cfx_223_b1,
    d_318,
    engrd_223_b1,
    d_319,
    stgrd_224_b1,
    d_320,
    otrb_224_b1,
    d_321,
    qi_224_b1,
    d_322,
    kax_225_b1,
    d_323,
    kax_226_b1,
    d_324,
    bpma_226_b1,
    d_325,
    qi_226_b1,
    d_326,
    ciy_226_b1,
    d_327,
    cfx_226_b1,
    d_328,
    bpma_227_b1,
    d_329,
    qi_227_b1,
    d_330,
    engrd_228_b1,
    d_331,
    enlat_229_b1,
    ensub_229_b1,
)

# Power Supply IDs:
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
