# Converted from component_list_2026.01.21.xls

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import (
    Drift,
    Hcor,
    Marker,
    Monitor,
    Quadrupole,
    SBend,
    Undulator,
    Vcor,
)

twiss0 = Twiss()
twiss0.E = 14.0000000004506
twiss0.alpha_x = 1.2509875229615357
twiss0.alpha_y = -0.8261963931928359
twiss0.beta_x = 39.651100517205535
twiss0.beta_y = 25.951946797806908
twiss0.Dx = 4.212204628110794e-06
twiss0.Dy = 4.067259042224402e-06
twiss0.s = 2174.808421000021


# Drifts:
d_0 = Drift(l=0.2927199999999175, eid="D_0")
d_1 = Drift(l=5.2444799999998395, eid="D_1")
absp_2203_sa2 = Drift(l=0.05, eid="ABSP.2203.SA2")
d_2 = Drift(l=0.1722999999999047, eid="D_2")
d_3 = Drift(l=0.18665000000009968, eid="D_3")
d_4 = Drift(l=0.33287000000006517, eid="D_4")
d_5 = Drift(l=5.2444799999998395, eid="D_5")
absp_2209_sa2 = Drift(l=0.05, eid="ABSP.2209.SA2")
d_6 = Drift(l=0.17230000000035944, eid="D_6")
d_7 = Drift(l=0.18664999999964493, eid="D_7")
d_8 = Drift(l=0.33287000000006517, eid="D_8")
d_9 = Drift(l=0.02500000000009095, eid="D_9")
d_10 = Drift(l=0.0727799999999661, eid="D_10")
d_11 = Drift(l=0.07169999999996435, eid="D_11")
d_12 = Drift(l=0.0749999999998181, eid="D_12")
absp_2215_sa2 = Drift(l=0.05, eid="ABSP.2215.SA2")
d_13 = Drift(l=0.17230000000035944, eid="D_13")
d_14 = Drift(l=0.18665000000009968, eid="D_14")
d_15 = Drift(l=0.09815000000014043, eid="D_15")
bps_2216_sa2 = Drift(l=0.23, eid="BPS.2216.SA2")
d_16 = Drift(l=0.004719999999470009, eid="D_16")
d_17 = Drift(l=0.02500000000009095, eid="D_17")
d_18 = Drift(l=0.0727799999999661, eid="D_18")
d_19 = Drift(l=0.07169999999996435, eid="D_19")
d_20 = Drift(l=0.07500000000027285, eid="D_20")
absp_2221_sa2 = Drift(l=0.05, eid="ABSP.2221.SA2")
d_21 = Drift(l=0.1722999999999047, eid="D_21")
d_22 = Drift(l=0.18665000000009968, eid="D_22")
d_23 = Drift(l=0.09815000000014043, eid="D_23")
bps_2222_sa2 = Drift(l=0.23, eid="BPS.2222.SA2")
d_24 = Drift(l=0.004719999999924757, eid="D_24")
d_25 = Drift(l=0.024999999999636202, eid="D_25")
d_26 = Drift(l=0.0727799999999661, eid="D_26")
d_27 = Drift(l=0.0717000000004191, eid="D_27")
d_28 = Drift(l=0.0749999999998181, eid="D_28")
absp_2227_sa2 = Drift(l=0.05, eid="ABSP.2227.SA2")
d_29 = Drift(l=0.1722999999999047, eid="D_29")
d_30 = Drift(l=0.18665000000009968, eid="D_30")
d_31 = Drift(l=0.09815000000014043, eid="D_31")
bps_2228_sa2 = Drift(l=0.23, eid="BPS.2228.SA2")
d_32 = Drift(l=0.004719999999924757, eid="D_32")
d_33 = Drift(l=0.02500000000009095, eid="D_33")
d_34 = Drift(l=0.0727799999999661, eid="D_34")
d_35 = Drift(l=0.07169999999996435, eid="D_35")
d_36 = Drift(l=0.0749999999998181, eid="D_36")
absp_2233_sa2 = Drift(l=0.05, eid="ABSP.2233.SA2")
d_37 = Drift(l=0.1722999999999047, eid="D_37")
d_38 = Drift(l=0.18665000000009968, eid="D_38")
d_39 = Drift(l=0.09815000000014043, eid="D_39")
bps_2234_sa2 = Drift(l=0.23, eid="BPS.2234.SA2")
d_40 = Drift(l=0.004719999999924757, eid="D_40")
d_41 = Drift(l=0.02500000000009095, eid="D_41")
d_42 = Drift(l=0.0727799999999661, eid="D_42")
d_43 = Drift(l=0.07169999999996435, eid="D_43")
d_44 = Drift(l=0.0749999999998181, eid="D_44")
absp_2239_sa2 = Drift(l=0.05, eid="ABSP.2239.SA2")
d_45 = Drift(l=0.17230000000035944, eid="D_45")
d_46 = Drift(l=0.18664999999964493, eid="D_46")
d_47 = Drift(l=0.09815000000014043, eid="D_47")
bps_2240_sa2 = Drift(l=0.23, eid="BPS.2240.SA2")
d_48 = Drift(l=0.004719999999924757, eid="D_48")
d_49 = Drift(l=0.02500000000009095, eid="D_49")
d_50 = Drift(l=0.0727799999999661, eid="D_50")
d_51 = Drift(l=0.07169999999996435, eid="D_51")
d_52 = Drift(l=0.0749999999998181, eid="D_52")
absp_2245_sa2 = Drift(l=0.05, eid="ABSP.2245.SA2")
d_53 = Drift(l=0.17230000000035944, eid="D_53")
d_54 = Drift(l=0.18665000000009968, eid="D_54")
d_55 = Drift(l=0.09815000000014043, eid="D_55")
bps_2246_sa2 = Drift(l=0.23, eid="BPS.2246.SA2")
d_56 = Drift(l=0.004719999999470009, eid="D_56")
d_57 = Drift(l=0.02500000000009095, eid="D_57")
d_58 = Drift(l=0.0727799999999661, eid="D_58")
d_59 = Drift(l=0.07169999999996435, eid="D_59")
d_60 = Drift(l=0.07500000000027285, eid="D_60")
absp_2251_sa2 = Drift(l=0.05, eid="ABSP.2251.SA2")
d_61 = Drift(l=0.1722999999999047, eid="D_61")
d_62 = Drift(l=0.18665000000009968, eid="D_62")
d_63 = Drift(l=0.09815000000014043, eid="D_63")
bps_2252_sa2 = Drift(l=0.23, eid="BPS.2252.SA2")
d_64 = Drift(l=0.004719999999924757, eid="D_64")
d_65 = Drift(l=0.024999999999636202, eid="D_65")
d_66 = Drift(l=0.0727799999999661, eid="D_66")
d_67 = Drift(l=0.0717000000004191, eid="D_67")
d_68 = Drift(l=0.0749999999998181, eid="D_68")
absp_2257_sa2 = Drift(l=0.05, eid="ABSP.2257.SA2")
d_69 = Drift(l=0.1722999999999047, eid="D_69")
d_70 = Drift(l=0.18665000000009968, eid="D_70")
d_71 = Drift(l=0.33287000000006517, eid="D_71")
d_72 = Drift(l=0.2462799999998424, eid="D_72")
d_73 = Drift(l=1.2374999999997272, eid="D_73")
d_74 = Drift(l=0.2899999999999636, eid="D_74")
d_75 = Drift(l=0.7350000000001273, eid="D_75")
d_76 = Drift(l=1.237499999999909, eid="D_76")
d_77 = Drift(l=0.29819999999972424, eid="D_77")
absp_2264_sa2 = Drift(l=0.05, eid="ABSP.2264.SA2")
d_78 = Drift(l=0.1722999999999047, eid="D_78")
d_79 = Drift(l=0.18665000000009968, eid="D_79")
d_80 = Drift(l=0.09815000000014043, eid="D_80")
bps_2264_sa2 = Drift(l=0.23, eid="BPS.2264.SA2")
d_81 = Drift(l=0.004719999999924757, eid="D_81")
d_82 = Drift(l=0.02500000000009095, eid="D_82")
d_83 = Drift(l=0.0727799999999661, eid="D_83")
d_84 = Drift(l=0.07169999999996435, eid="D_84")
d_85 = Drift(l=0.0749999999998181, eid="D_85")
absp_2270_sa2 = Drift(l=0.05, eid="ABSP.2270.SA2")
d_86 = Drift(l=0.17230000000035944, eid="D_86")
d_87 = Drift(l=0.18664999999964493, eid="D_87")
d_88 = Drift(l=0.09815000000014043, eid="D_88")
bps_2270_sa2 = Drift(l=0.23, eid="BPS.2270.SA2")
d_89 = Drift(l=0.004719999999924757, eid="D_89")
d_90 = Drift(l=0.02500000000009095, eid="D_90")
d_91 = Drift(l=0.0727799999999661, eid="D_91")
d_92 = Drift(l=0.07169999999996435, eid="D_92")
d_93 = Drift(l=0.0749999999998181, eid="D_93")
absp_2276_sa2 = Drift(l=0.05, eid="ABSP.2276.SA2")
d_94 = Drift(l=0.17230000000035944, eid="D_94")
d_95 = Drift(l=0.18665000000009968, eid="D_95")
d_96 = Drift(l=0.09815000000014043, eid="D_96")
bps_2276_sa2 = Drift(l=0.23, eid="BPS.2276.SA2")
d_97 = Drift(l=0.004719999999470009, eid="D_97")
d_98 = Drift(l=0.02500000000009095, eid="D_98")
d_99 = Drift(l=0.0727799999999661, eid="D_99")
d_100 = Drift(l=0.07169999999996435, eid="D_100")
d_101 = Drift(l=0.07500000000027285, eid="D_101")
absp_2282_sa2 = Drift(l=0.05, eid="ABSP.2282.SA2")
d_102 = Drift(l=0.1722999999999047, eid="D_102")
d_103 = Drift(l=0.18665000000009968, eid="D_103")
d_104 = Drift(l=0.09815000000014043, eid="D_104")
bps_2283_sa2 = Drift(l=0.23, eid="BPS.2283.SA2")
d_105 = Drift(l=0.004719999999924757, eid="D_105")
d_106 = Drift(l=0.024999999999636202, eid="D_106")
d_107 = Drift(l=0.0727799999999661, eid="D_107")
d_108 = Drift(l=0.0717000000004191, eid="D_108")
d_109 = Drift(l=0.0749999999998181, eid="D_109")
absp_2288_sa2 = Drift(l=0.05, eid="ABSP.2288.SA2")
d_110 = Drift(l=0.1722999999999047, eid="D_110")
d_111 = Drift(l=0.18665000000009968, eid="D_111")
d_112 = Drift(l=0.09815000000014043, eid="D_112")
bps_2289_sa2 = Drift(l=0.23, eid="BPS.2289.SA2")
d_113 = Drift(l=0.004719999999924757, eid="D_113")
d_114 = Drift(l=0.02500000000009095, eid="D_114")
d_115 = Drift(l=0.0727799999999661, eid="D_115")
d_116 = Drift(l=0.07169999999996435, eid="D_116")
d_117 = Drift(l=0.0749999999998181, eid="D_117")
absp_2294_sa2 = Drift(l=0.05, eid="ABSP.2294.SA2")
d_118 = Drift(l=0.1722999999999047, eid="D_118")
d_119 = Drift(l=0.18665000000009968, eid="D_119")
d_120 = Drift(l=0.09815000000014043, eid="D_120")
bps_2295_sa2 = Drift(l=0.23, eid="BPS.2295.SA2")
d_121 = Drift(l=0.004719999999924757, eid="D_121")
d_122 = Drift(l=0.02500000000009095, eid="D_122")
d_123 = Drift(l=0.0727799999999661, eid="D_123")
d_124 = Drift(l=0.07169999999996435, eid="D_124")
d_125 = Drift(l=0.0749999999998181, eid="D_125")
absp_2300_sa2 = Drift(l=0.05, eid="ABSP.2300.SA2")
d_126 = Drift(l=0.17230000000035944, eid="D_126")
d_127 = Drift(l=0.18664999999964493, eid="D_127")
d_128 = Drift(l=0.09815000000014043, eid="D_128")
bps_2301_sa2 = Drift(l=0.23, eid="BPS.2301.SA2")
d_129 = Drift(l=0.004719999999924757, eid="D_129")
d_130 = Drift(l=0.02500000000009095, eid="D_130")
d_131 = Drift(l=0.0727799999999661, eid="D_131")
d_132 = Drift(l=0.07169999999996435, eid="D_132")
d_133 = Drift(l=0.0749999999998181, eid="D_133")
absp_2306_sa2 = Drift(l=0.05, eid="ABSP.2306.SA2")
d_134 = Drift(l=0.17230000000035944, eid="D_134")
d_135 = Drift(l=0.18665000000009968, eid="D_135")
d_136 = Drift(l=0.09815000000014043, eid="D_136")
bps_2307_sa2 = Drift(l=0.23, eid="BPS.2307.SA2")
d_137 = Drift(l=0.004719999999470009, eid="D_137")
d_138 = Drift(l=0.02500000000009095, eid="D_138")
d_139 = Drift(l=0.0727799999999661, eid="D_139")
d_140 = Drift(l=0.07169999999996435, eid="D_140")
d_141 = Drift(l=0.07500000000027285, eid="D_141")
absp_2312_sa2 = Drift(l=0.05, eid="ABSP.2312.SA2")
d_142 = Drift(l=0.1722999999999047, eid="D_142")
d_143 = Drift(l=0.18665000000009968, eid="D_143")
d_144 = Drift(l=0.33287000000006517, eid="D_144")
d_145 = Drift(l=0.2462799999998424, eid="D_145")
d_146 = Drift(l=1.2374999999997272, eid="D_146")
d_147 = Drift(l=0.2899999999999636, eid="D_147")
d_148 = Drift(l=0.7349999999996726, eid="D_148")
d_149 = Drift(l=1.237500000000182, eid="D_149")
d_150 = Drift(l=0.29819999999990615, eid="D_150")
absp_2318_sa2 = Drift(l=0.05, eid="ABSP.2318.SA2")
d_151 = Drift(l=0.1722999999999047, eid="D_151")
d_152 = Drift(l=0.18665000000009968, eid="D_152")
d_153 = Drift(l=0.09815000000014043, eid="D_153")
bps_2319_sa2 = Drift(l=0.23, eid="BPS.2319.SA2")
d_154 = Drift(l=0.004719999999924757, eid="D_154")
d_155 = Drift(l=0.02500000000009095, eid="D_155")
d_156 = Drift(l=0.0727799999999661, eid="D_156")
d_157 = Drift(l=0.07169999999996435, eid="D_157")
d_158 = Drift(l=0.0749999999998181, eid="D_158")
absp_2325_sa2 = Drift(l=0.05, eid="ABSP.2325.SA2")
d_159 = Drift(l=0.1722999999999047, eid="D_159")
d_160 = Drift(l=0.18665000000009968, eid="D_160")
d_161 = Drift(l=0.09815000000014043, eid="D_161")
bps_2325_sa2 = Drift(l=0.23, eid="BPS.2325.SA2")
d_162 = Drift(l=0.004719999999924757, eid="D_162")
d_163 = Drift(l=0.02500000000009095, eid="D_163")
d_164 = Drift(l=0.0727799999999661, eid="D_164")
d_165 = Drift(l=0.07169999999996435, eid="D_165")
d_166 = Drift(l=0.0749999999998181, eid="D_166")
absp_2331_sa2 = Drift(l=0.05, eid="ABSP.2331.SA2")
d_167 = Drift(l=0.17230000000035944, eid="D_167")
d_168 = Drift(l=0.18664999999964493, eid="D_168")
d_169 = Drift(l=0.09815000000014043, eid="D_169")
bps_2331_sa2 = Drift(l=0.23, eid="BPS.2331.SA2")
d_170 = Drift(l=0.004719999999924757, eid="D_170")
d_171 = Drift(l=0.02500000000009095, eid="D_171")
d_172 = Drift(l=0.0727799999999661, eid="D_172")
d_173 = Drift(l=0.07169999999996435, eid="D_173")
d_174 = Drift(l=0.0749999999998181, eid="D_174")
absp_2337_sa2 = Drift(l=0.05, eid="ABSP.2337.SA2")
d_175 = Drift(l=0.17230000000035944, eid="D_175")
d_176 = Drift(l=0.18665000000009968, eid="D_176")
d_177 = Drift(l=0.09815000000014043, eid="D_177")
bps_2337_sa2 = Drift(l=0.23, eid="BPS.2337.SA2")
d_178 = Drift(l=0.004719999999470009, eid="D_178")
d_179 = Drift(l=0.02500000000009095, eid="D_179")
d_180 = Drift(l=0.0727799999999661, eid="D_180")
d_181 = Drift(l=0.07169999999996435, eid="D_181")
d_182 = Drift(l=0.07500000000027285, eid="D_182")
absp_2343_sa2 = Drift(l=0.05, eid="ABSP.2343.SA2")
d_183 = Drift(l=0.1722999999999047, eid="D_183")
d_184 = Drift(l=0.18665000000009968, eid="D_184")
d_185 = Drift(l=0.09815000000014043, eid="D_185")
bps_2344_sa2 = Drift(l=0.23, eid="BPS.2344.SA2")
d_186 = Drift(l=0.004719999999924757, eid="D_186")
d_187 = Drift(l=0.024999999999636202, eid="D_187")
d_188 = Drift(l=0.0727799999999661, eid="D_188")
d_189 = Drift(l=0.0717000000004191, eid="D_189")
d_190 = Drift(l=0.0749999999998181, eid="D_190")
absp_2349_sa2 = Drift(l=0.05, eid="ABSP.2349.SA2")
d_191 = Drift(l=0.1722999999999047, eid="D_191")
d_192 = Drift(l=0.18665000000009968, eid="D_192")
d_193 = Drift(l=0.09815000000014043, eid="D_193")
bps_2350_sa2 = Drift(l=0.23, eid="BPS.2350.SA2")
d_194 = Drift(l=0.004719999999924757, eid="D_194")
d_195 = Drift(l=0.02500000000009095, eid="D_195")
d_196 = Drift(l=0.0727799999999661, eid="D_196")
d_197 = Drift(l=0.07169999999996435, eid="D_197")
d_198 = Drift(l=0.0749999999998181, eid="D_198")
absp_2355_sa2 = Drift(l=0.05, eid="ABSP.2355.SA2")
d_199 = Drift(l=0.1722999999999047, eid="D_199")
d_200 = Drift(l=0.18665000000009968, eid="D_200")
d_201 = Drift(l=0.09815000000014043, eid="D_201")
bps_2356_sa2 = Drift(l=0.23, eid="BPS.2356.SA2")
d_202 = Drift(l=0.004719999999924757, eid="D_202")
d_203 = Drift(l=0.02500000000009095, eid="D_203")
d_204 = Drift(l=0.0727799999999661, eid="D_204")
d_205 = Drift(l=0.07169999999996435, eid="D_205")
d_206 = Drift(l=0.0749999999998181, eid="D_206")
absp_2361_sa2 = Drift(l=0.05, eid="ABSP.2361.SA2")
d_207 = Drift(l=0.17230000000035944, eid="D_207")
d_208 = Drift(l=0.18664999999964493, eid="D_208")
d_209 = Drift(l=0.09815000000014043, eid="D_209")
bps_2362_sa2 = Drift(l=0.23, eid="BPS.2362.SA2")
d_210 = Drift(l=0.004719999999924757, eid="D_210")
d_211 = Drift(l=0.02500000000009095, eid="D_211")
d_212 = Drift(l=0.0727799999999661, eid="D_212")
d_213 = Drift(l=0.07169999999996435, eid="D_213")
d_214 = Drift(l=0.0749999999998181, eid="D_214")
absp_2367_sa2 = Drift(l=0.05, eid="ABSP.2367.SA2")
d_215 = Drift(l=0.17230000000035944, eid="D_215")
d_216 = Drift(l=0.18665000000009968, eid="D_216")
d_217 = Drift(l=0.09815000000014043, eid="D_217")
bps_2368_sa2 = Drift(l=0.23, eid="BPS.2368.SA2")
d_218 = Drift(l=0.004719999999470009, eid="D_218")
d_219 = Drift(l=0.02500000000009095, eid="D_219")
d_220 = Drift(l=0.0727799999999661, eid="D_220")
d_221 = Drift(l=0.07169999999996435, eid="D_221")
d_222 = Drift(l=0.07500000000027285, eid="D_222")
absp_2373_sa2 = Drift(l=0.05, eid="ABSP.2373.SA2")
d_223 = Drift(l=0.1722999999999047, eid="D_223")
d_224 = Drift(l=0.18665000000009968, eid="D_224")
d_225 = Drift(l=0.09815000000014043, eid="D_225")
bps_2374_sa2 = Drift(l=0.23, eid="BPS.2374.SA2")
d_226 = Drift(l=0.004719999999924757, eid="D_226")
d_227 = Drift(l=0.024999999999636202, eid="D_227")
d_228 = Drift(l=0.0727799999999661, eid="D_228")
d_229 = Drift(l=0.0717000000004191, eid="D_229")
d_230 = Drift(l=0.0749999999998181, eid="D_230")
absp_2379_sa2 = Drift(l=0.05, eid="ABSP.2379.SA2")
d_231 = Drift(l=0.1722999999999047, eid="D_231")
d_232 = Drift(l=0.18665000000009968, eid="D_232")
d_233 = Drift(l=0.09815000000014043, eid="D_233")
bps_2380_sa2 = Drift(l=0.23, eid="BPS.2380.SA2")
d_234 = Drift(l=0.004719999999924757, eid="D_234")
d_235 = Drift(l=0.02500000000009095, eid="D_235")
d_236 = Drift(l=0.0727799999999661, eid="D_236")
d_237 = Drift(l=0.07169999999996435, eid="D_237")
d_238 = Drift(l=0.0749999999998181, eid="D_238")
absp_2385_sa2 = Drift(l=0.05, eid="ABSP.2385.SA2")
d_239 = Drift(l=0.1722999999999047, eid="D_239")
d_240 = Drift(l=0.18665000000009968, eid="D_240")
d_241 = Drift(l=0.09815000000014043, eid="D_241")
bps_2386_sa2 = Drift(l=0.23, eid="BPS.2386.SA2")
d_242 = Drift(l=0.004719999999924757, eid="D_242")
d_243 = Drift(l=0.02500000000009095, eid="D_243")
d_244 = Drift(l=0.0727799999999661, eid="D_244")
d_245 = Drift(l=0.07169999999996435, eid="D_245")
d_246 = Drift(l=0.0749999999998181, eid="D_246")
absp_2392_sa2 = Drift(l=0.05, eid="ABSP.2392.SA2")
d_247 = Drift(l=0.17230000000035944, eid="D_247")
d_248 = Drift(l=0.18664999999964493, eid="D_248")
d_249 = Drift(l=0.09815000000014043, eid="D_249")
bps_2392_sa2 = Drift(l=0.23, eid="BPS.2392.SA2")
d_250 = Drift(l=0.004719999999924757, eid="D_250")
d_251 = Drift(l=0.02500000000009095, eid="D_251")
d_252 = Drift(l=0.0727799999999661, eid="D_252")
d_253 = Drift(l=0.07169999999996435, eid="D_253")
d_254 = Drift(l=0.0749999999998181, eid="D_254")
absp_2398_sa2 = Drift(l=0.05, eid="ABSP.2398.SA2")
d_255 = Drift(l=0.17230000000035944, eid="D_255")
d_256 = Drift(l=0.18665000000009968, eid="D_256")
d_257 = Drift(l=0.09815000000014043, eid="D_257")
bps_2398_sa2 = Drift(l=0.23, eid="BPS.2398.SA2")
d_258 = Drift(l=0.004719999999470009, eid="D_258")
d_259 = Drift(l=0.02500000000009095, eid="D_259")
d_260 = Drift(l=0.0727799999999661, eid="D_260")
d_261 = Drift(l=0.07169999999996435, eid="D_261")
d_262 = Drift(l=0.07500000000027285, eid="D_262")
absp_2404_sa2 = Drift(l=0.05, eid="ABSP.2404.SA2")
d_263 = Drift(l=0.1722999999999047, eid="D_263")
d_264 = Drift(l=0.18665000000009968, eid="D_264")
d_265 = Drift(l=0.09815000000014043, eid="D_265")
bps_2404_sa2 = Drift(l=0.23, eid="BPS.2404.SA2")
d_266 = Drift(l=0.004719999999924757, eid="D_266")
d_267 = Drift(l=0.024999999999636202, eid="D_267")
d_268 = Drift(l=0.0727799999999661, eid="D_268")
d_269 = Drift(l=0.0717000000004191, eid="D_269")
d_270 = Drift(l=0.0749999999998181, eid="D_270")
absp_2410_sa2 = Drift(l=0.05, eid="ABSP.2410.SA2")
d_271 = Drift(l=0.1722999999999047, eid="D_271")
d_272 = Drift(l=0.18665000000009968, eid="D_272")
d_273 = Drift(l=0.09815000000014043, eid="D_273")
bps_2411_sa2 = Drift(l=0.23, eid="BPS.2411.SA2")
d_274 = Drift(l=0.004719999999924757, eid="D_274")
d_275 = Drift(l=0.02500000000009095, eid="D_275")
d_276 = Drift(l=0.0727799999999661, eid="D_276")
d_277 = Drift(l=0.07169999999996435, eid="D_277")
d_278 = Drift(l=0.0749999999998181, eid="D_278")
absp_2416_sa2 = Drift(l=0.05, eid="ABSP.2416.SA2")
d_279 = Drift(l=0.1722999999999047, eid="D_279")
d_280 = Drift(l=0.18665000000009968, eid="D_280")
d_281 = Drift(l=0.09815000000014043, eid="D_281")
bps_2417_sa2 = Drift(l=0.23, eid="BPS.2417.SA2")
d_282 = Drift(l=0.004719999999924757, eid="D_282")
d_283 = Drift(l=0.02500000000009095, eid="D_283")
d_284 = Drift(l=0.0727799999999661, eid="D_284")
d_285 = Drift(l=0.07169999999996435, eid="D_285")
d_286 = Drift(l=0.0749999999998181, eid="D_286")
absp_2422_sa2 = Drift(l=0.05, eid="ABSP.2422.SA2")
d_287 = Drift(l=0.17230000000035944, eid="D_287")
d_288 = Drift(l=0.18664999999964493, eid="D_288")
d_289 = Drift(l=0.09815000000014043, eid="D_289")
bps_2423_sa2 = Drift(l=0.23, eid="BPS.2423.SA2")
d_290 = Drift(l=0.004719999999924757, eid="D_290")
d_291 = Drift(l=0.02500000000009095, eid="D_291")
d_292 = Drift(l=0.0727799999999661, eid="D_292")
d_293 = Drift(l=0.07169999999996435, eid="D_293")
d_294 = Drift(l=0.0749999999998181, eid="D_294")
absp_2428_sa2 = Drift(l=0.05, eid="ABSP.2428.SA2")
d_295 = Drift(l=0.17230000000035944, eid="D_295")
d_296 = Drift(l=0.18665000000009968, eid="D_296")
d_297 = Drift(l=0.09815000000014043, eid="D_297")
bps_2429_sa2 = Drift(l=0.23, eid="BPS.2429.SA2")
d_298 = Drift(l=0.004719999999470009, eid="D_298")
d_299 = Drift(l=0.02500000000009095, eid="D_299")
d_300 = Drift(l=0.0727799999999661, eid="D_300")
d_301 = Drift(l=0.07169999999996435, eid="D_301")
d_302 = Drift(l=0.07500000000027285, eid="D_302")
absp4_2434_sa2 = Drift(l=0.05, eid="ABSP4.2434.SA2")
d_303 = Drift(l=0.1722999999999047, eid="D_303")
d_304 = Drift(l=0.18665000000009968, eid="D_304")
d_305 = Drift(l=0.09815000000014043, eid="D_305")
bps_2435_sa2 = Drift(l=0.23, eid="BPS.2435.SA2")
d_306 = Drift(l=0.004719999999924757, eid="D_306")
d_307 = Drift(l=5.524479999999585, eid="D_307")
absp_2441_sa2 = Drift(l=0.05, eid="ABSP.2441.SA2")
d_308 = Drift(l=0.17230000000035944, eid="D_308")
d_309 = Drift(l=0.18665000000009968, eid="D_309")
d_310 = Drift(l=0.21314999999992215, eid="D_310")
d_311 = Drift(l=0.1197199999996883, eid="D_311")
d_312 = Drift(l=5.52448000000004, eid="D_312")
absp_2447_sa2 = Drift(l=0.05, eid="ABSP.2447.SA2")
d_313 = Drift(l=0.1722999999999047, eid="D_313")
d_314 = Drift(l=0.18665000000009968, eid="D_314")
d_315 = Drift(l=0.21314999999992215, eid="D_315")
d_316 = Drift(l=0.11972000000014305, eid="D_316")
d_317 = Drift(l=5.52448000000004, eid="D_317")
absp_2453_sa2 = Drift(l=0.05, eid="ABSP.2453.SA2")
d_318 = Drift(l=0.1722999999999047, eid="D_318")
d_319 = Drift(l=0.18665000000009968, eid="D_319")
d_320 = Drift(l=0.21314999999992215, eid="D_320")
d_321 = Drift(l=0.11972000000014305, eid="D_321")
d_322 = Drift(l=5.52448000000004, eid="D_322")
absp_2460_sa2 = Drift(l=0.05, eid="ABSP.2460.SA2")
d_323 = Drift(l=0.1722999999999047, eid="D_323")
d_324 = Drift(l=0.18665000000009968, eid="D_324")
d_325 = Drift(l=0.21314999999992215, eid="D_325")
d_326 = Drift(l=0.11972000000014305, eid="D_326")
d_327 = Drift(l=5.524479999999585, eid="D_327")
absp_2466_sa2 = Drift(l=0.05, eid="ABSP.2466.SA2")
d_328 = Drift(l=0.17230000000035944, eid="D_328")
d_329 = Drift(l=0.18665000000009968, eid="D_329")
d_330 = Drift(l=0.21314999999992215, eid="D_330")
d_331 = Drift(l=0.1197199999996883, eid="D_331")
d_332 = Drift(l=5.52448000000004, eid="D_332")
absp4_2472_sa2 = Drift(l=0.05, eid="ABSP4.2472.SA2")
d_333 = Drift(l=0.17230000000035944, eid="D_333")
d_334 = Drift(l=0.18664999999964493, eid="D_334")
d_335 = Drift(l=0.040150000000147706, eid="D_335")

# Quadrupoles:
qa_2203_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2203.SA2")
qa_2209_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2209.SA2")
qa_2215_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2215.SA2")
qa_2221_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2221.SA2")
qa_2227_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2227.SA2")
qa_2234_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2234.SA2")
qa_2240_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2240.SA2")
qa_2246_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2246.SA2")
qa_2252_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2252.SA2")
qa_2258_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2258.SA2")
qa_2264_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2264.SA2")
qa_2270_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2270.SA2")
qa_2276_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2276.SA2")
qa_2282_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2282.SA2")
qa_2288_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2288.SA2")
qa_2295_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2295.SA2")
qa_2301_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2301.SA2")
qa_2307_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2307.SA2")
qa_2313_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2313.SA2")
qa_2319_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2319.SA2")
qa_2325_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2325.SA2")
qa_2331_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2331.SA2")
qa_2337_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2337.SA2")
qa_2343_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2343.SA2")
qa_2349_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2349.SA2")
qa_2355_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2355.SA2")
qa_2362_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2362.SA2")
qa_2368_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2368.SA2")
qa_2374_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2374.SA2")
qa_2380_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2380.SA2")
qa_2386_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2386.SA2")
qa_2392_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2392.SA2")
qa_2398_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2398.SA2")
qa_2404_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2404.SA2")
qa_2410_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2410.SA2")
qa_2416_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2416.SA2")
qa_2422_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2422.SA2")
qa_2429_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2429.SA2")
qa_2435_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2435.SA2")
qa_2441_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2441.SA2")
qa_2447_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2447.SA2")
qa_2454_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2454.SA2")
qa_2460_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2460.SA2")
qa_2467_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid="QA.2467.SA2")
qa_2473_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid="QA.2473.SA2")

# SBends:
bs_2259_sa2 = SBend(l=0.3, eid="BS.2259.SA2")
bs_2260_sa2 = SBend(l=0.3, eid="BS.2260.SA2")
bs_2262_sa2 = SBend(l=0.3, eid="BS.2262.SA2")
bs_2263_sa2 = SBend(l=0.3, eid="BS.2263.SA2")
bs_2314_sa2 = SBend(l=0.3, eid="BS.2314.SA2")
bs_2315_sa2 = SBend(l=0.3, eid="BS.2315.SA2")
bs_2316_sa2 = SBend(l=0.3, eid="BS.2316.SA2")
bs_2318_sa2 = SBend(l=0.3, eid="BS.2318.SA2")

# Hcors:
cax_2210_sa2 = Hcor(eid="CAX.2210.SA2")
cbx_2215_sa2 = Hcor(eid="CBX.2215.SA2")
cax_2216_sa2 = Hcor(eid="CAX.2216.SA2")
cbx_2221_sa2 = Hcor(eid="CBX.2221.SA2")
cax_2222_sa2 = Hcor(eid="CAX.2222.SA2")
cbx_2227_sa2 = Hcor(eid="CBX.2227.SA2")
cax_2228_sa2 = Hcor(eid="CAX.2228.SA2")
cbx_2233_sa2 = Hcor(eid="CBX.2233.SA2")
cax_2234_sa2 = Hcor(eid="CAX.2234.SA2")
cbx_2239_sa2 = Hcor(eid="CBX.2239.SA2")
cax_2241_sa2 = Hcor(eid="CAX.2241.SA2")
cbx_2245_sa2 = Hcor(eid="CBX.2245.SA2")
cax_2247_sa2 = Hcor(eid="CAX.2247.SA2")
cbx_2251_sa2 = Hcor(eid="CBX.2251.SA2")
cax_2253_sa2 = Hcor(eid="CAX.2253.SA2")
cbx_2257_sa2 = Hcor(eid="CBX.2257.SA2")
cbs_2260_sa2 = Hcor(eid="CBS.2260.SA2")
cbs_2263_sa2 = Hcor(eid="CBS.2263.SA2")
cax_2265_sa2 = Hcor(eid="CAX.2265.SA2")
cbx_2270_sa2 = Hcor(eid="CBX.2270.SA2")
cax_2271_sa2 = Hcor(eid="CAX.2271.SA2")
cbx_2276_sa2 = Hcor(eid="CBX.2276.SA2")
cax_2277_sa2 = Hcor(eid="CAX.2277.SA2")
cbx_2282_sa2 = Hcor(eid="CBX.2282.SA2")
cax_2283_sa2 = Hcor(eid="CAX.2283.SA2")
cbx_2288_sa2 = Hcor(eid="CBX.2288.SA2")
cax_2289_sa2 = Hcor(eid="CAX.2289.SA2")
cbx_2294_sa2 = Hcor(eid="CBX.2294.SA2")
cax_2295_sa2 = Hcor(eid="CAX.2295.SA2")
cbx_2300_sa2 = Hcor(eid="CBX.2300.SA2")
cax_2302_sa2 = Hcor(eid="CAX.2302.SA2")
cbx_2306_sa2 = Hcor(eid="CBX.2306.SA2")
cax_2308_sa2 = Hcor(eid="CAX.2308.SA2")
cbx_2312_sa2 = Hcor(eid="CBX.2312.SA2")
cbs_2315_sa2 = Hcor(eid="CBS.2315.SA2")
cbs_2317_sa2 = Hcor(eid="CBS.2317.SA2")
cax_2320_sa2 = Hcor(eid="CAX.2320.SA2")
cbx_2324_sa2 = Hcor(eid="CBX.2324.SA2")
cax_2326_sa2 = Hcor(eid="CAX.2326.SA2")
cbx_2331_sa2 = Hcor(eid="CBX.2331.SA2")
cax_2332_sa2 = Hcor(eid="CAX.2332.SA2")
cbx_2337_sa2 = Hcor(eid="CBX.2337.SA2")
cax_2338_sa2 = Hcor(eid="CAX.2338.SA2")
cbx_2343_sa2 = Hcor(eid="CBX.2343.SA2")
cax_2344_sa2 = Hcor(eid="CAX.2344.SA2")
cbx_2349_sa2 = Hcor(eid="CBX.2349.SA2")
cax_2350_sa2 = Hcor(eid="CAX.2350.SA2")
cbx_2355_sa2 = Hcor(eid="CBX.2355.SA2")
cax_2356_sa2 = Hcor(eid="CAX.2356.SA2")
cbx_2361_sa2 = Hcor(eid="CBX.2361.SA2")
cax_2362_sa2 = Hcor(eid="CAX.2362.SA2")
cbx_2367_sa2 = Hcor(eid="CBX.2367.SA2")
cax_2369_sa2 = Hcor(eid="CAX.2369.SA2")
cbx_2373_sa2 = Hcor(eid="CBX.2373.SA2")
cax_2375_sa2 = Hcor(eid="CAX.2375.SA2")
cbx_2379_sa2 = Hcor(eid="CBX.2379.SA2")
cax_2381_sa2 = Hcor(eid="CAX.2381.SA2")
cbx_2385_sa2 = Hcor(eid="CBX.2385.SA2")
cax_2387_sa2 = Hcor(eid="CAX.2387.SA2")
cbx_2391_sa2 = Hcor(eid="CBX.2391.SA2")
cax_2393_sa2 = Hcor(eid="CAX.2393.SA2")
cbx_2398_sa2 = Hcor(eid="CBX.2398.SA2")
cax_2399_sa2 = Hcor(eid="CAX.2399.SA2")
cbx_2404_sa2 = Hcor(eid="CBX.2404.SA2")
cax_2405_sa2 = Hcor(eid="CAX.2405.SA2")
cbx_2410_sa2 = Hcor(eid="CBX.2410.SA2")
cax_2411_sa2 = Hcor(eid="CAX.2411.SA2")
cbx_2416_sa2 = Hcor(eid="CBX.2416.SA2")
cax_2417_sa2 = Hcor(eid="CAX.2417.SA2")
cbx_2422_sa2 = Hcor(eid="CBX.2422.SA2")
cax_2423_sa2 = Hcor(eid="CAX.2423.SA2")
cbx_2428_sa2 = Hcor(eid="CBX.2428.SA2")
cax_2430_sa2 = Hcor(eid="CAX.2430.SA2")
cbx_2434_sa2 = Hcor(eid="CBX.2434.SA2")

# Vcors:
cay_2210_sa2 = Vcor(eid="CAY.2210.SA2")
cby_2215_sa2 = Vcor(eid="CBY.2215.SA2")
cay_2216_sa2 = Vcor(eid="CAY.2216.SA2")
cby_2221_sa2 = Vcor(eid="CBY.2221.SA2")
cay_2222_sa2 = Vcor(eid="CAY.2222.SA2")
cby_2227_sa2 = Vcor(eid="CBY.2227.SA2")
cay_2228_sa2 = Vcor(eid="CAY.2228.SA2")
cby_2233_sa2 = Vcor(eid="CBY.2233.SA2")
cay_2234_sa2 = Vcor(eid="CAY.2234.SA2")
cby_2239_sa2 = Vcor(eid="CBY.2239.SA2")
cay_2241_sa2 = Vcor(eid="CAY.2241.SA2")
cby_2245_sa2 = Vcor(eid="CBY.2245.SA2")
cay_2247_sa2 = Vcor(eid="CAY.2247.SA2")
cby_2251_sa2 = Vcor(eid="CBY.2251.SA2")
cay_2253_sa2 = Vcor(eid="CAY.2253.SA2")
cby_2257_sa2 = Vcor(eid="CBY.2257.SA2")
cay_2265_sa2 = Vcor(eid="CAY.2265.SA2")
cby_2270_sa2 = Vcor(eid="CBY.2270.SA2")
cay_2271_sa2 = Vcor(eid="CAY.2271.SA2")
cby_2276_sa2 = Vcor(eid="CBY.2276.SA2")
cay_2277_sa2 = Vcor(eid="CAY.2277.SA2")
cby_2282_sa2 = Vcor(eid="CBY.2282.SA2")
cay_2283_sa2 = Vcor(eid="CAY.2283.SA2")
cby_2288_sa2 = Vcor(eid="CBY.2288.SA2")
cay_2289_sa2 = Vcor(eid="CAY.2289.SA2")
cby_2294_sa2 = Vcor(eid="CBY.2294.SA2")
cay_2295_sa2 = Vcor(eid="CAY.2295.SA2")
cby_2300_sa2 = Vcor(eid="CBY.2300.SA2")
cay_2302_sa2 = Vcor(eid="CAY.2302.SA2")
cby_2306_sa2 = Vcor(eid="CBY.2306.SA2")
cay_2308_sa2 = Vcor(eid="CAY.2308.SA2")
cby_2312_sa2 = Vcor(eid="CBY.2312.SA2")
cay_2320_sa2 = Vcor(eid="CAY.2320.SA2")
cby_2324_sa2 = Vcor(eid="CBY.2324.SA2")
cay_2326_sa2 = Vcor(eid="CAY.2326.SA2")
cby_2331_sa2 = Vcor(eid="CBY.2331.SA2")
cay_2332_sa2 = Vcor(eid="CAY.2332.SA2")
cby_2337_sa2 = Vcor(eid="CBY.2337.SA2")
cay_2338_sa2 = Vcor(eid="CAY.2338.SA2")
cby_2343_sa2 = Vcor(eid="CBY.2343.SA2")
cay_2344_sa2 = Vcor(eid="CAY.2344.SA2")
cby_2349_sa2 = Vcor(eid="CBY.2349.SA2")
cay_2350_sa2 = Vcor(eid="CAY.2350.SA2")
cby_2355_sa2 = Vcor(eid="CBY.2355.SA2")
cay_2356_sa2 = Vcor(eid="CAY.2356.SA2")
cby_2361_sa2 = Vcor(eid="CBY.2361.SA2")
cay_2362_sa2 = Vcor(eid="CAY.2362.SA2")
cby_2367_sa2 = Vcor(eid="CBY.2367.SA2")
cay_2369_sa2 = Vcor(eid="CAY.2369.SA2")
cby_2373_sa2 = Vcor(eid="CBY.2373.SA2")
cay_2375_sa2 = Vcor(eid="CAY.2375.SA2")
cby_2379_sa2 = Vcor(eid="CBY.2379.SA2")
cay_2381_sa2 = Vcor(eid="CAY.2381.SA2")
cby_2385_sa2 = Vcor(eid="CBY.2385.SA2")
cay_2387_sa2 = Vcor(eid="CAY.2387.SA2")
cby_2391_sa2 = Vcor(eid="CBY.2391.SA2")
cay_2393_sa2 = Vcor(eid="CAY.2393.SA2")
cby_2398_sa2 = Vcor(eid="CBY.2398.SA2")
cay_2399_sa2 = Vcor(eid="CAY.2399.SA2")
cby_2404_sa2 = Vcor(eid="CBY.2404.SA2")
cay_2405_sa2 = Vcor(eid="CAY.2405.SA2")
cby_2410_sa2 = Vcor(eid="CBY.2410.SA2")
cay_2411_sa2 = Vcor(eid="CAY.2411.SA2")
cby_2416_sa2 = Vcor(eid="CBY.2416.SA2")
cay_2417_sa2 = Vcor(eid="CAY.2417.SA2")
cby_2422_sa2 = Vcor(eid="CBY.2422.SA2")
cay_2423_sa2 = Vcor(eid="CAY.2423.SA2")
cby_2428_sa2 = Vcor(eid="CBY.2428.SA2")
cay_2430_sa2 = Vcor(eid="CAY.2430.SA2")
cby_2434_sa2 = Vcor(eid="CBY.2434.SA2")

# Undulators:
u40_2212_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2212.SA2")
u40_2218_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2218.SA2")
u40_2224_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2224.SA2")
u40_2230_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2230.SA2")
u40_2237_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2237.SA2")
u40_2243_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2243.SA2")
u40_2249_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2249.SA2")
u40_2255_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2255.SA2")
u40_2267_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2267.SA2")
u40_2273_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2273.SA2")
u40_2279_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2279.SA2")
u40_2285_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2285.SA2")
u40_2291_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2291.SA2")
u40_2297_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2297.SA2")
u40_2304_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2304.SA2")
u40_2310_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2310.SA2")
u40_2322_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2322.SA2")
u40_2328_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2328.SA2")
u40_2334_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2334.SA2")
u40_2340_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2340.SA2")
u40_2346_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2346.SA2")
u40_2352_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2352.SA2")
u40_2358_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2358.SA2")
u40_2365_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2365.SA2")
u40_2371_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2371.SA2")
u40_2377_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2377.SA2")
u40_2383_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2383.SA2")
u40_2389_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2389.SA2")
u40_2395_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2395.SA2")
u40_2401_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2401.SA2")
u40_2407_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2407.SA2")
u40_2413_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2413.SA2")
u40_2419_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2419.SA2")
u40_2425_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2425.SA2")
u40_2432_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid="U40.2432.SA2")

# Monitors:
bpme_2203_sa2 = Monitor(eid="BPME.2203.SA2")
bpme_2209_sa2 = Monitor(eid="BPME.2209.SA2")
bpme_2215_sa2 = Monitor(eid="BPME.2215.SA2")
bpme_2221_sa2 = Monitor(eid="BPME.2221.SA2")
bpme_2227_sa2 = Monitor(eid="BPME.2227.SA2")
bpme_2233_sa2 = Monitor(eid="BPME.2233.SA2")
bpme_2239_sa2 = Monitor(eid="BPME.2239.SA2")
bpme_2245_sa2 = Monitor(eid="BPME.2245.SA2")
bpme_2252_sa2 = Monitor(eid="BPME.2252.SA2")
bpme_2258_sa2 = Monitor(eid="BPME.2258.SA2")
bpmh_2261_sa2 = Monitor(eid="BPMH.2261.SA2")
bpme_2264_sa2 = Monitor(eid="BPME.2264.SA2")
bpme_2270_sa2 = Monitor(eid="BPME.2270.SA2")
bpme_2276_sa2 = Monitor(eid="BPME.2276.SA2")
bpme_2282_sa2 = Monitor(eid="BPME.2282.SA2")
bpme_2288_sa2 = Monitor(eid="BPME.2288.SA2")
bpme_2294_sa2 = Monitor(eid="BPME.2294.SA2")
bpme_2300_sa2 = Monitor(eid="BPME.2300.SA2")
bpme_2306_sa2 = Monitor(eid="BPME.2306.SA2")
bpme_2313_sa2 = Monitor(eid="BPME.2313.SA2")
bpmh_2316_sa2 = Monitor(eid="BPMH.2316.SA2")
bpme_2319_sa2 = Monitor(eid="BPME.2319.SA2")
bpme_2325_sa2 = Monitor(eid="BPME.2325.SA2")
bpme_2331_sa2 = Monitor(eid="BPME.2331.SA2")
bpme_2337_sa2 = Monitor(eid="BPME.2337.SA2")
bpme_2343_sa2 = Monitor(eid="BPME.2343.SA2")
bpme_2349_sa2 = Monitor(eid="BPME.2349.SA2")
bpme_2355_sa2 = Monitor(eid="BPME.2355.SA2")
bpme_2361_sa2 = Monitor(eid="BPME.2361.SA2")
bpme_2367_sa2 = Monitor(eid="BPME.2367.SA2")
bpme_2373_sa2 = Monitor(eid="BPME.2373.SA2")
bpme_2380_sa2 = Monitor(eid="BPME.2380.SA2")
bpme_2386_sa2 = Monitor(eid="BPME.2386.SA2")
bpme_2392_sa2 = Monitor(eid="BPME.2392.SA2")
bpme_2398_sa2 = Monitor(eid="BPME.2398.SA2")
bpme_2404_sa2 = Monitor(eid="BPME.2404.SA2")
bpme_2410_sa2 = Monitor(eid="BPME.2410.SA2")
bpme_2416_sa2 = Monitor(eid="BPME.2416.SA2")
bpme_2422_sa2 = Monitor(eid="BPME.2422.SA2")
bpme_2428_sa2 = Monitor(eid="BPME.2428.SA2")
bpme_2434_sa2 = Monitor(eid="BPME.2434.SA2")
bpme_2441_sa2 = Monitor(eid="BPME.2441.SA2")
bpme_2447_sa2 = Monitor(eid="BPME.2447.SA2")
bpme_2454_sa2 = Monitor(eid="BPME.2454.SA2")
bpme_2460_sa2 = Monitor(eid="BPME.2460.SA2")
bpme_2466_sa2 = Monitor(eid="BPME.2466.SA2")
bpme_2473_sa2 = Monitor(eid="BPME.2473.SA2")

# Markers:
stsec_2197_sa2 = Marker(eid="STSEC.2197.SA2")
match_2197_sa2 = Marker(eid="MATCH.2197.SA2")
stucell_2197_sa2 = Marker(eid="STUCELL.2197.SA2")
enucell_2203_sa2 = Marker(eid="ENUCELL.2203.SA2")
stucell_2203_sa2 = Marker(eid="STUCELL.2203.SA2")
enucell_2210_sa2 = Marker(eid="ENUCELL.2210.SA2")
stucell_2210_sa2 = Marker(eid="STUCELL.2210.SA2")
enucell_2216_sa2 = Marker(eid="ENUCELL.2216.SA2")
stucell_2216_sa2 = Marker(eid="STUCELL.2216.SA2")
enucell_2222_sa2 = Marker(eid="ENUCELL.2222.SA2")
stucell_2222_sa2 = Marker(eid="STUCELL.2222.SA2")
enucell_2228_sa2 = Marker(eid="ENUCELL.2228.SA2")
stucell_2228_sa2 = Marker(eid="STUCELL.2228.SA2")
enucell_2234_sa2 = Marker(eid="ENUCELL.2234.SA2")
stucell_2234_sa2 = Marker(eid="STUCELL.2234.SA2")
enucell_2240_sa2 = Marker(eid="ENUCELL.2240.SA2")
stucell_2240_sa2 = Marker(eid="STUCELL.2240.SA2")
enucell_2246_sa2 = Marker(eid="ENUCELL.2246.SA2")
stucell_2246_sa2 = Marker(eid="STUCELL.2246.SA2")
enucell_2252_sa2 = Marker(eid="ENUCELL.2252.SA2")
stucell_2252_sa2 = Marker(eid="STUCELL.2252.SA2")
enucell_2258_sa2 = Marker(eid="ENUCELL.2258.SA2")
stucell_2258_sa2 = Marker(eid="STUCELL.2258.SA2")
mcbs_2259_sa2 = Marker(eid="MCBS.2259.SA2")
enucell_2264_sa2 = Marker(eid="ENUCELL.2264.SA2")
stucell_2264_sa2 = Marker(eid="STUCELL.2264.SA2")
enucell_2271_sa2 = Marker(eid="ENUCELL.2271.SA2")
stucell_2271_sa2 = Marker(eid="STUCELL.2271.SA2")
enucell_2277_sa2 = Marker(eid="ENUCELL.2277.SA2")
stucell_2277_sa2 = Marker(eid="STUCELL.2277.SA2")
enucell_2283_sa2 = Marker(eid="ENUCELL.2283.SA2")
stucell_2283_sa2 = Marker(eid="STUCELL.2283.SA2")
enucell_2289_sa2 = Marker(eid="ENUCELL.2289.SA2")
stucell_2289_sa2 = Marker(eid="STUCELL.2289.SA2")
enucell_2295_sa2 = Marker(eid="ENUCELL.2295.SA2")
stucell_2295_sa2 = Marker(eid="STUCELL.2295.SA2")
enucell_2301_sa2 = Marker(eid="ENUCELL.2301.SA2")
stucell_2301_sa2 = Marker(eid="STUCELL.2301.SA2")
enucell_2307_sa2 = Marker(eid="ENUCELL.2307.SA2")
stucell_2307_sa2 = Marker(eid="STUCELL.2307.SA2")
enucell_2313_sa2 = Marker(eid="ENUCELL.2313.SA2")
stucell_2313_sa2 = Marker(eid="STUCELL.2313.SA2")
mcbs_2314_sa2 = Marker(eid="MCBS.2314.SA2")
enucell_2319_sa2 = Marker(eid="ENUCELL.2319.SA2")
stucell_2319_sa2 = Marker(eid="STUCELL.2319.SA2")
enucell_2325_sa2 = Marker(eid="ENUCELL.2325.SA2")
stucell_2325_sa2 = Marker(eid="STUCELL.2325.SA2")
enucell_2331_sa2 = Marker(eid="ENUCELL.2331.SA2")
stucell_2331_sa2 = Marker(eid="STUCELL.2331.SA2")
enucell_2338_sa2 = Marker(eid="ENUCELL.2338.SA2")
stucell_2338_sa2 = Marker(eid="STUCELL.2338.SA2")
enucell_2344_sa2 = Marker(eid="ENUCELL.2344.SA2")
stucell_2344_sa2 = Marker(eid="STUCELL.2344.SA2")
enucell_2350_sa2 = Marker(eid="ENUCELL.2350.SA2")
stucell_2350_sa2 = Marker(eid="STUCELL.2350.SA2")
enucell_2356_sa2 = Marker(eid="ENUCELL.2356.SA2")
stucell_2356_sa2 = Marker(eid="STUCELL.2356.SA2")
enucell_2362_sa2 = Marker(eid="ENUCELL.2362.SA2")
stucell_2362_sa2 = Marker(eid="STUCELL.2362.SA2")
enucell_2368_sa2 = Marker(eid="ENUCELL.2368.SA2")
stucell_2368_sa2 = Marker(eid="STUCELL.2368.SA2")
enucell_2374_sa2 = Marker(eid="ENUCELL.2374.SA2")
stucell_2374_sa2 = Marker(eid="STUCELL.2374.SA2")
enucell_2380_sa2 = Marker(eid="ENUCELL.2380.SA2")
stucell_2380_sa2 = Marker(eid="STUCELL.2380.SA2")
enucell_2386_sa2 = Marker(eid="ENUCELL.2386.SA2")
stucell_2386_sa2 = Marker(eid="STUCELL.2386.SA2")
enucell_2392_sa2 = Marker(eid="ENUCELL.2392.SA2")
stucell_2392_sa2 = Marker(eid="STUCELL.2392.SA2")
enucell_2399_sa2 = Marker(eid="ENUCELL.2399.SA2")
stucell_2399_sa2 = Marker(eid="STUCELL.2399.SA2")
enucell_2405_sa2 = Marker(eid="ENUCELL.2405.SA2")
stucell_2405_sa2 = Marker(eid="STUCELL.2405.SA2")
enucell_2411_sa2 = Marker(eid="ENUCELL.2411.SA2")
stucell_2411_sa2 = Marker(eid="STUCELL.2411.SA2")
enucell_2417_sa2 = Marker(eid="ENUCELL.2417.SA2")
stucell_2417_sa2 = Marker(eid="STUCELL.2417.SA2")
enucell_2423_sa2 = Marker(eid="ENUCELL.2423.SA2")
stucell_2423_sa2 = Marker(eid="STUCELL.2423.SA2")
enucell_2429_sa2 = Marker(eid="ENUCELL.2429.SA2")
stucell_2429_sa2 = Marker(eid="STUCELL.2429.SA2")
enucell_2435_sa2 = Marker(eid="ENUCELL.2435.SA2")
stsub_2435_sa2 = Marker(eid="STSUB.2435.SA2")
stucell_2435_sa2 = Marker(eid="STUCELL.2435.SA2")
mbps_2441_sa2 = Marker(eid="MBPS.2441.SA2")
enucell_2441_sa2 = Marker(eid="ENUCELL.2441.SA2")
stucell_2441_sa2 = Marker(eid="STUCELL.2441.SA2")
mbps_2448_sa2 = Marker(eid="MBPS.2448.SA2")
enucell_2448_sa2 = Marker(eid="ENUCELL.2448.SA2")
stucell_2448_sa2 = Marker(eid="STUCELL.2448.SA2")
mbps_2454_sa2 = Marker(eid="MBPS.2454.SA2")
enucell_2454_sa2 = Marker(eid="ENUCELL.2454.SA2")
stucell_2454_sa2 = Marker(eid="STUCELL.2454.SA2")
mbps_2460_sa2 = Marker(eid="MBPS.2460.SA2")
enucell_2461_sa2 = Marker(eid="ENUCELL.2461.SA2")
stucell_2461_sa2 = Marker(eid="STUCELL.2461.SA2")
mbps_2467_sa2 = Marker(eid="MBPS.2467.SA2")
enucell_2467_sa2 = Marker(eid="ENUCELL.2467.SA2")
stucell_2467_sa2 = Marker(eid="STUCELL.2467.SA2")
enucell_2473_sa2 = Marker(eid="ENUCELL.2473.SA2")
ensub_2473_sa2 = Marker(eid="ENSUB.2473.SA2")
ensec_2473_sa2 = Marker(eid="ENSEC.2473.SA2")

# Sequence:
cell = (
    stsec_2197_sa2,
    d_0,
    match_2197_sa2,
    stucell_2197_sa2,
    d_1,
    absp_2203_sa2,
    d_2,
    bpme_2203_sa2,
    d_3,
    qa_2203_sa2,
    d_4,
    enucell_2203_sa2,
    stucell_2203_sa2,
    d_5,
    absp_2209_sa2,
    d_6,
    bpme_2209_sa2,
    d_7,
    qa_2209_sa2,
    d_8,
    enucell_2210_sa2,
    stucell_2210_sa2,
    d_9,
    cax_2210_sa2,
    cay_2210_sa2,
    d_10,
    u40_2212_sa2,
    d_11,
    cbx_2215_sa2,
    cby_2215_sa2,
    d_12,
    absp_2215_sa2,
    d_13,
    bpme_2215_sa2,
    d_14,
    qa_2215_sa2,
    d_15,
    bps_2216_sa2,
    d_16,
    enucell_2216_sa2,
    stucell_2216_sa2,
    d_17,
    cax_2216_sa2,
    cay_2216_sa2,
    d_18,
    u40_2218_sa2,
    d_19,
    cbx_2221_sa2,
    cby_2221_sa2,
    d_20,
    absp_2221_sa2,
    d_21,
    bpme_2221_sa2,
    d_22,
    qa_2221_sa2,
    d_23,
    bps_2222_sa2,
    d_24,
    enucell_2222_sa2,
    stucell_2222_sa2,
    d_25,
    cax_2222_sa2,
    cay_2222_sa2,
    d_26,
    u40_2224_sa2,
    d_27,
    cbx_2227_sa2,
    cby_2227_sa2,
    d_28,
    absp_2227_sa2,
    d_29,
    bpme_2227_sa2,
    d_30,
    qa_2227_sa2,
    d_31,
    bps_2228_sa2,
    d_32,
    enucell_2228_sa2,
    stucell_2228_sa2,
    d_33,
    cax_2228_sa2,
    cay_2228_sa2,
    d_34,
    u40_2230_sa2,
    d_35,
    cbx_2233_sa2,
    cby_2233_sa2,
    d_36,
    absp_2233_sa2,
    d_37,
    bpme_2233_sa2,
    d_38,
    qa_2234_sa2,
    d_39,
    bps_2234_sa2,
    d_40,
    enucell_2234_sa2,
    stucell_2234_sa2,
    d_41,
    cax_2234_sa2,
    cay_2234_sa2,
    d_42,
    u40_2237_sa2,
    d_43,
    cbx_2239_sa2,
    cby_2239_sa2,
    d_44,
    absp_2239_sa2,
    d_45,
    bpme_2239_sa2,
    d_46,
    qa_2240_sa2,
    d_47,
    bps_2240_sa2,
    d_48,
    enucell_2240_sa2,
    stucell_2240_sa2,
    d_49,
    cax_2241_sa2,
    cay_2241_sa2,
    d_50,
    u40_2243_sa2,
    d_51,
    cbx_2245_sa2,
    cby_2245_sa2,
    d_52,
    absp_2245_sa2,
    d_53,
    bpme_2245_sa2,
    d_54,
    qa_2246_sa2,
    d_55,
    bps_2246_sa2,
    d_56,
    enucell_2246_sa2,
    stucell_2246_sa2,
    d_57,
    cax_2247_sa2,
    cay_2247_sa2,
    d_58,
    u40_2249_sa2,
    d_59,
    cbx_2251_sa2,
    cby_2251_sa2,
    d_60,
    absp_2251_sa2,
    d_61,
    bpme_2252_sa2,
    d_62,
    qa_2252_sa2,
    d_63,
    bps_2252_sa2,
    d_64,
    enucell_2252_sa2,
    stucell_2252_sa2,
    d_65,
    cax_2253_sa2,
    cay_2253_sa2,
    d_66,
    u40_2255_sa2,
    d_67,
    cbx_2257_sa2,
    cby_2257_sa2,
    d_68,
    absp_2257_sa2,
    d_69,
    bpme_2258_sa2,
    d_70,
    qa_2258_sa2,
    d_71,
    enucell_2258_sa2,
    stucell_2258_sa2,
    d_72,
    bs_2259_sa2,
    mcbs_2259_sa2,
    d_73,
    bs_2260_sa2,
    cbs_2260_sa2,
    d_74,
    bpmh_2261_sa2,
    d_75,
    bs_2262_sa2,
    d_76,
    bs_2263_sa2,
    cbs_2263_sa2,
    d_77,
    absp_2264_sa2,
    d_78,
    bpme_2264_sa2,
    d_79,
    qa_2264_sa2,
    d_80,
    bps_2264_sa2,
    d_81,
    enucell_2264_sa2,
    stucell_2264_sa2,
    d_82,
    cax_2265_sa2,
    cay_2265_sa2,
    d_83,
    u40_2267_sa2,
    d_84,
    cbx_2270_sa2,
    cby_2270_sa2,
    d_85,
    absp_2270_sa2,
    d_86,
    bpme_2270_sa2,
    d_87,
    qa_2270_sa2,
    d_88,
    bps_2270_sa2,
    d_89,
    enucell_2271_sa2,
    stucell_2271_sa2,
    d_90,
    cax_2271_sa2,
    cay_2271_sa2,
    d_91,
    u40_2273_sa2,
    d_92,
    cbx_2276_sa2,
    cby_2276_sa2,
    d_93,
    absp_2276_sa2,
    d_94,
    bpme_2276_sa2,
    d_95,
    qa_2276_sa2,
    d_96,
    bps_2276_sa2,
    d_97,
    enucell_2277_sa2,
    stucell_2277_sa2,
    d_98,
    cax_2277_sa2,
    cay_2277_sa2,
    d_99,
    u40_2279_sa2,
    d_100,
    cbx_2282_sa2,
    cby_2282_sa2,
    d_101,
    absp_2282_sa2,
    d_102,
    bpme_2282_sa2,
    d_103,
    qa_2282_sa2,
    d_104,
    bps_2283_sa2,
    d_105,
    enucell_2283_sa2,
    stucell_2283_sa2,
    d_106,
    cax_2283_sa2,
    cay_2283_sa2,
    d_107,
    u40_2285_sa2,
    d_108,
    cbx_2288_sa2,
    cby_2288_sa2,
    d_109,
    absp_2288_sa2,
    d_110,
    bpme_2288_sa2,
    d_111,
    qa_2288_sa2,
    d_112,
    bps_2289_sa2,
    d_113,
    enucell_2289_sa2,
    stucell_2289_sa2,
    d_114,
    cax_2289_sa2,
    cay_2289_sa2,
    d_115,
    u40_2291_sa2,
    d_116,
    cbx_2294_sa2,
    cby_2294_sa2,
    d_117,
    absp_2294_sa2,
    d_118,
    bpme_2294_sa2,
    d_119,
    qa_2295_sa2,
    d_120,
    bps_2295_sa2,
    d_121,
    enucell_2295_sa2,
    stucell_2295_sa2,
    d_122,
    cax_2295_sa2,
    cay_2295_sa2,
    d_123,
    u40_2297_sa2,
    d_124,
    cbx_2300_sa2,
    cby_2300_sa2,
    d_125,
    absp_2300_sa2,
    d_126,
    bpme_2300_sa2,
    d_127,
    qa_2301_sa2,
    d_128,
    bps_2301_sa2,
    d_129,
    enucell_2301_sa2,
    stucell_2301_sa2,
    d_130,
    cax_2302_sa2,
    cay_2302_sa2,
    d_131,
    u40_2304_sa2,
    d_132,
    cbx_2306_sa2,
    cby_2306_sa2,
    d_133,
    absp_2306_sa2,
    d_134,
    bpme_2306_sa2,
    d_135,
    qa_2307_sa2,
    d_136,
    bps_2307_sa2,
    d_137,
    enucell_2307_sa2,
    stucell_2307_sa2,
    d_138,
    cax_2308_sa2,
    cay_2308_sa2,
    d_139,
    u40_2310_sa2,
    d_140,
    cbx_2312_sa2,
    cby_2312_sa2,
    d_141,
    absp_2312_sa2,
    d_142,
    bpme_2313_sa2,
    d_143,
    qa_2313_sa2,
    d_144,
    enucell_2313_sa2,
    stucell_2313_sa2,
    d_145,
    bs_2314_sa2,
    mcbs_2314_sa2,
    d_146,
    bs_2315_sa2,
    cbs_2315_sa2,
    d_147,
    bpmh_2316_sa2,
    d_148,
    bs_2316_sa2,
    cbs_2317_sa2,
    d_149,
    bs_2318_sa2,
    d_150,
    absp_2318_sa2,
    d_151,
    bpme_2319_sa2,
    d_152,
    qa_2319_sa2,
    d_153,
    bps_2319_sa2,
    d_154,
    enucell_2319_sa2,
    stucell_2319_sa2,
    d_155,
    cax_2320_sa2,
    cay_2320_sa2,
    d_156,
    u40_2322_sa2,
    d_157,
    cbx_2324_sa2,
    cby_2324_sa2,
    d_158,
    absp_2325_sa2,
    d_159,
    bpme_2325_sa2,
    d_160,
    qa_2325_sa2,
    d_161,
    bps_2325_sa2,
    d_162,
    enucell_2325_sa2,
    stucell_2325_sa2,
    d_163,
    cax_2326_sa2,
    cay_2326_sa2,
    d_164,
    u40_2328_sa2,
    d_165,
    cbx_2331_sa2,
    cby_2331_sa2,
    d_166,
    absp_2331_sa2,
    d_167,
    bpme_2331_sa2,
    d_168,
    qa_2331_sa2,
    d_169,
    bps_2331_sa2,
    d_170,
    enucell_2331_sa2,
    stucell_2331_sa2,
    d_171,
    cax_2332_sa2,
    cay_2332_sa2,
    d_172,
    u40_2334_sa2,
    d_173,
    cbx_2337_sa2,
    cby_2337_sa2,
    d_174,
    absp_2337_sa2,
    d_175,
    bpme_2337_sa2,
    d_176,
    qa_2337_sa2,
    d_177,
    bps_2337_sa2,
    d_178,
    enucell_2338_sa2,
    stucell_2338_sa2,
    d_179,
    cax_2338_sa2,
    cay_2338_sa2,
    d_180,
    u40_2340_sa2,
    d_181,
    cbx_2343_sa2,
    cby_2343_sa2,
    d_182,
    absp_2343_sa2,
    d_183,
    bpme_2343_sa2,
    d_184,
    qa_2343_sa2,
    d_185,
    bps_2344_sa2,
    d_186,
    enucell_2344_sa2,
    stucell_2344_sa2,
    d_187,
    cax_2344_sa2,
    cay_2344_sa2,
    d_188,
    u40_2346_sa2,
    d_189,
    cbx_2349_sa2,
    cby_2349_sa2,
    d_190,
    absp_2349_sa2,
    d_191,
    bpme_2349_sa2,
    d_192,
    qa_2349_sa2,
    d_193,
    bps_2350_sa2,
    d_194,
    enucell_2350_sa2,
    stucell_2350_sa2,
    d_195,
    cax_2350_sa2,
    cay_2350_sa2,
    d_196,
    u40_2352_sa2,
    d_197,
    cbx_2355_sa2,
    cby_2355_sa2,
    d_198,
    absp_2355_sa2,
    d_199,
    bpme_2355_sa2,
    d_200,
    qa_2355_sa2,
    d_201,
    bps_2356_sa2,
    d_202,
    enucell_2356_sa2,
    stucell_2356_sa2,
    d_203,
    cax_2356_sa2,
    cay_2356_sa2,
    d_204,
    u40_2358_sa2,
    d_205,
    cbx_2361_sa2,
    cby_2361_sa2,
    d_206,
    absp_2361_sa2,
    d_207,
    bpme_2361_sa2,
    d_208,
    qa_2362_sa2,
    d_209,
    bps_2362_sa2,
    d_210,
    enucell_2362_sa2,
    stucell_2362_sa2,
    d_211,
    cax_2362_sa2,
    cay_2362_sa2,
    d_212,
    u40_2365_sa2,
    d_213,
    cbx_2367_sa2,
    cby_2367_sa2,
    d_214,
    absp_2367_sa2,
    d_215,
    bpme_2367_sa2,
    d_216,
    qa_2368_sa2,
    d_217,
    bps_2368_sa2,
    d_218,
    enucell_2368_sa2,
    stucell_2368_sa2,
    d_219,
    cax_2369_sa2,
    cay_2369_sa2,
    d_220,
    u40_2371_sa2,
    d_221,
    cbx_2373_sa2,
    cby_2373_sa2,
    d_222,
    absp_2373_sa2,
    d_223,
    bpme_2373_sa2,
    d_224,
    qa_2374_sa2,
    d_225,
    bps_2374_sa2,
    d_226,
    enucell_2374_sa2,
    stucell_2374_sa2,
    d_227,
    cax_2375_sa2,
    cay_2375_sa2,
    d_228,
    u40_2377_sa2,
    d_229,
    cbx_2379_sa2,
    cby_2379_sa2,
    d_230,
    absp_2379_sa2,
    d_231,
    bpme_2380_sa2,
    d_232,
    qa_2380_sa2,
    d_233,
    bps_2380_sa2,
    d_234,
    enucell_2380_sa2,
    stucell_2380_sa2,
    d_235,
    cax_2381_sa2,
    cay_2381_sa2,
    d_236,
    u40_2383_sa2,
    d_237,
    cbx_2385_sa2,
    cby_2385_sa2,
    d_238,
    absp_2385_sa2,
    d_239,
    bpme_2386_sa2,
    d_240,
    qa_2386_sa2,
    d_241,
    bps_2386_sa2,
    d_242,
    enucell_2386_sa2,
    stucell_2386_sa2,
    d_243,
    cax_2387_sa2,
    cay_2387_sa2,
    d_244,
    u40_2389_sa2,
    d_245,
    cbx_2391_sa2,
    cby_2391_sa2,
    d_246,
    absp_2392_sa2,
    d_247,
    bpme_2392_sa2,
    d_248,
    qa_2392_sa2,
    d_249,
    bps_2392_sa2,
    d_250,
    enucell_2392_sa2,
    stucell_2392_sa2,
    d_251,
    cax_2393_sa2,
    cay_2393_sa2,
    d_252,
    u40_2395_sa2,
    d_253,
    cbx_2398_sa2,
    cby_2398_sa2,
    d_254,
    absp_2398_sa2,
    d_255,
    bpme_2398_sa2,
    d_256,
    qa_2398_sa2,
    d_257,
    bps_2398_sa2,
    d_258,
    enucell_2399_sa2,
    stucell_2399_sa2,
    d_259,
    cax_2399_sa2,
    cay_2399_sa2,
    d_260,
    u40_2401_sa2,
    d_261,
    cbx_2404_sa2,
    cby_2404_sa2,
    d_262,
    absp_2404_sa2,
    d_263,
    bpme_2404_sa2,
    d_264,
    qa_2404_sa2,
    d_265,
    bps_2404_sa2,
    d_266,
    enucell_2405_sa2,
    stucell_2405_sa2,
    d_267,
    cax_2405_sa2,
    cay_2405_sa2,
    d_268,
    u40_2407_sa2,
    d_269,
    cbx_2410_sa2,
    cby_2410_sa2,
    d_270,
    absp_2410_sa2,
    d_271,
    bpme_2410_sa2,
    d_272,
    qa_2410_sa2,
    d_273,
    bps_2411_sa2,
    d_274,
    enucell_2411_sa2,
    stucell_2411_sa2,
    d_275,
    cax_2411_sa2,
    cay_2411_sa2,
    d_276,
    u40_2413_sa2,
    d_277,
    cbx_2416_sa2,
    cby_2416_sa2,
    d_278,
    absp_2416_sa2,
    d_279,
    bpme_2416_sa2,
    d_280,
    qa_2416_sa2,
    d_281,
    bps_2417_sa2,
    d_282,
    enucell_2417_sa2,
    stucell_2417_sa2,
    d_283,
    cax_2417_sa2,
    cay_2417_sa2,
    d_284,
    u40_2419_sa2,
    d_285,
    cbx_2422_sa2,
    cby_2422_sa2,
    d_286,
    absp_2422_sa2,
    d_287,
    bpme_2422_sa2,
    d_288,
    qa_2422_sa2,
    d_289,
    bps_2423_sa2,
    d_290,
    enucell_2423_sa2,
    stucell_2423_sa2,
    d_291,
    cax_2423_sa2,
    cay_2423_sa2,
    d_292,
    u40_2425_sa2,
    d_293,
    cbx_2428_sa2,
    cby_2428_sa2,
    d_294,
    absp_2428_sa2,
    d_295,
    bpme_2428_sa2,
    d_296,
    qa_2429_sa2,
    d_297,
    bps_2429_sa2,
    d_298,
    enucell_2429_sa2,
    stucell_2429_sa2,
    d_299,
    cax_2430_sa2,
    cay_2430_sa2,
    d_300,
    u40_2432_sa2,
    d_301,
    cbx_2434_sa2,
    cby_2434_sa2,
    d_302,
    absp4_2434_sa2,
    d_303,
    bpme_2434_sa2,
    d_304,
    qa_2435_sa2,
    d_305,
    bps_2435_sa2,
    d_306,
    enucell_2435_sa2,
    stsub_2435_sa2,
    stucell_2435_sa2,
    d_307,
    absp_2441_sa2,
    d_308,
    bpme_2441_sa2,
    d_309,
    qa_2441_sa2,
    d_310,
    mbps_2441_sa2,
    d_311,
    enucell_2441_sa2,
    stucell_2441_sa2,
    d_312,
    absp_2447_sa2,
    d_313,
    bpme_2447_sa2,
    d_314,
    qa_2447_sa2,
    d_315,
    mbps_2448_sa2,
    d_316,
    enucell_2448_sa2,
    stucell_2448_sa2,
    d_317,
    absp_2453_sa2,
    d_318,
    bpme_2454_sa2,
    d_319,
    qa_2454_sa2,
    d_320,
    mbps_2454_sa2,
    d_321,
    enucell_2454_sa2,
    stucell_2454_sa2,
    d_322,
    absp_2460_sa2,
    d_323,
    bpme_2460_sa2,
    d_324,
    qa_2460_sa2,
    d_325,
    mbps_2460_sa2,
    d_326,
    enucell_2461_sa2,
    stucell_2461_sa2,
    d_327,
    absp_2466_sa2,
    d_328,
    bpme_2466_sa2,
    d_329,
    qa_2467_sa2,
    d_330,
    mbps_2467_sa2,
    d_331,
    enucell_2467_sa2,
    stucell_2467_sa2,
    d_332,
    absp4_2472_sa2,
    d_333,
    bpme_2473_sa2,
    d_334,
    qa_2473_sa2,
    d_335,
    enucell_2473_sa2,
    ensub_2473_sa2,
    ensec_2473_sa2,
)

# Power Supply IDs:
# Quadrupole power supplies:
qa_2203_sa2.ps_id = "QA.1.SA2"
qa_2209_sa2.ps_id = "QA.2.SA2"
qa_2215_sa2.ps_id = "QA.1.SA2"
qa_2221_sa2.ps_id = "QA.2.SA2"
qa_2227_sa2.ps_id = "QA.1.SA2"
qa_2234_sa2.ps_id = "QA.2.SA2"
qa_2240_sa2.ps_id = "QA.1.SA2"
qa_2246_sa2.ps_id = "QA.2.SA2"
qa_2252_sa2.ps_id = "QA.1.SA2"
qa_2258_sa2.ps_id = "QA.2.SA2"
qa_2264_sa2.ps_id = "QA.1.SA2"
qa_2270_sa2.ps_id = "QA.2.SA2"
qa_2276_sa2.ps_id = "QA.1.SA2"
qa_2282_sa2.ps_id = "QA.2.SA2"
qa_2288_sa2.ps_id = "QA.1.SA2"
qa_2295_sa2.ps_id = "QA.2.SA2"
qa_2301_sa2.ps_id = "QA.1.SA2"
qa_2307_sa2.ps_id = "QA.2.SA2"
qa_2313_sa2.ps_id = "QA.1.SA2"
qa_2319_sa2.ps_id = "QA.2.SA2"
qa_2325_sa2.ps_id = "QA.1.SA2"
qa_2331_sa2.ps_id = "QA.2.SA2"
qa_2337_sa2.ps_id = "QA.1.SA2"
qa_2343_sa2.ps_id = "QA.2.SA2"
qa_2349_sa2.ps_id = "QA.1.SA2"
qa_2355_sa2.ps_id = "QA.2.SA2"
qa_2362_sa2.ps_id = "QA.1.SA2"
qa_2368_sa2.ps_id = "QA.2.SA2"
qa_2374_sa2.ps_id = "QA.1.SA2"
qa_2380_sa2.ps_id = "QA.2.SA2"
qa_2386_sa2.ps_id = "QA.1.SA2"
qa_2392_sa2.ps_id = "QA.2.SA2"
qa_2398_sa2.ps_id = "QA.1.SA2"
qa_2404_sa2.ps_id = "QA.2.SA2"
qa_2410_sa2.ps_id = "QA.1.SA2"
qa_2416_sa2.ps_id = "QA.2.SA2"
qa_2422_sa2.ps_id = "QA.1.SA2"
qa_2429_sa2.ps_id = "QA.2.SA2"
qa_2435_sa2.ps_id = "QA.1.SA2"
qa_2441_sa2.ps_id = "QA.2.SA2"
qa_2447_sa2.ps_id = "QA.1.SA2"
qa_2454_sa2.ps_id = "QA.2.SA2"
qa_2460_sa2.ps_id = "QA.1.SA2"
qa_2467_sa2.ps_id = "QA.2.SA2"
qa_2473_sa2.ps_id = "QA.1.SA2"

# SBend power supplies:
bs_2259_sa2.ps_id = "BS.1.SA2"
bs_2260_sa2.ps_id = "BS.1.SA2"
bs_2262_sa2.ps_id = "BS.1.SA2"
bs_2263_sa2.ps_id = "BS.1.SA2"
bs_2314_sa2.ps_id = "BS.2.SA2"
bs_2315_sa2.ps_id = "BS.2.SA2"
bs_2316_sa2.ps_id = "BS.2.SA2"
bs_2318_sa2.ps_id = "BS.2.SA2"
