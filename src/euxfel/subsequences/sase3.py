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
twiss0.alpha_x = 1.5486674815641706
twiss0.alpha_y = -0.6638030609802946
twiss0.beta_x = 22.72948117061306
twiss0.beta_y = 9.639530885538143
twiss0.Dx = 9.396345380381856e-06
twiss0.s = 2777.8147670000008


# Drifts:
d_0 = Drift(l=0.29272000000037224, eid="D_0")
d_1 = Drift(l=5.2444799999998395, eid="D_1")
absp_2806_sa3 = Drift(l=0.05, eid="ABSP.2806.SA3")
d_2 = Drift(l=0.1722999999999047, eid="D_2")
d_3 = Drift(l=0.18665000000009968, eid="D_3")
d_4 = Drift(l=0.33287000000006517, eid="D_4")
d_5 = Drift(l=0.02500000000009095, eid="D_5")
d_6 = Drift(l=0.0727799999999661, eid="D_6")
d_7 = Drift(l=0.07169999999996346, eid="D_7")
d_8 = Drift(l=0.0749999999998181, eid="D_8")
absp_2812_sa3 = Drift(l=0.05, eid="ABSP.2812.SA3")
d_9 = Drift(l=0.1722999999999047, eid="D_9")
d_10 = Drift(l=0.18665000000009968, eid="D_10")
d_11 = Drift(l=0.09815000000014043, eid="D_11")
bps_2813_sa3 = Drift(l=0.23, eid="BPS.2813.SA3")
d_12 = Drift(l=0.004719999999924757, eid="D_12")
d_13 = Drift(l=0.02500000000009095, eid="D_13")
d_14 = Drift(l=0.0727799999999661, eid="D_14")
d_15 = Drift(l=0.07169999999996346, eid="D_15")
d_16 = Drift(l=0.0749999999998181, eid="D_16")
absp_2818_sa3 = Drift(l=0.05, eid="ABSP.2818.SA3")
d_17 = Drift(l=0.1722999999999047, eid="D_17")
d_18 = Drift(l=0.18665000000009968, eid="D_18")
d_19 = Drift(l=0.09815000000014043, eid="D_19")
bps_2819_sa3 = Drift(l=0.23, eid="BPS.2819.SA3")
d_20 = Drift(l=0.004719999999924757, eid="D_20")
d_21 = Drift(l=0.02500000000009095, eid="D_21")
d_22 = Drift(l=0.0727799999999661, eid="D_22")
d_23 = Drift(l=0.07169999999996346, eid="D_23")
d_24 = Drift(l=0.0749999999998181, eid="D_24")
absp_2824_sa3 = Drift(l=0.05, eid="ABSP.2824.SA3")
d_25 = Drift(l=0.17230000000035944, eid="D_25")
d_26 = Drift(l=0.18665000000009968, eid="D_26")
d_27 = Drift(l=0.09815000000014043, eid="D_27")
bps_2825_sa3 = Drift(l=0.23, eid="BPS.2825.SA3")
d_28 = Drift(l=0.004719999999470009, eid="D_28")
d_29 = Drift(l=0.02500000000009095, eid="D_29")
d_30 = Drift(l=0.0727799999999661, eid="D_30")
d_31 = Drift(l=0.07169999999996346, eid="D_31")
d_32 = Drift(l=0.0749999999998181, eid="D_32")
absp_2830_sa3 = Drift(l=0.05, eid="ABSP.2830.SA3")
d_33 = Drift(l=0.17230000000035944, eid="D_33")
d_34 = Drift(l=0.18665000000009968, eid="D_34")
d_35 = Drift(l=0.09815000000014043, eid="D_35")
bps_2831_sa3 = Drift(l=0.23, eid="BPS.2831.SA3")
d_36 = Drift(l=0.004719999999924757, eid="D_36")
d_37 = Drift(l=0.024999999999636202, eid="D_37")
d_38 = Drift(l=0.0727799999999661, eid="D_38")
d_39 = Drift(l=0.07169999999996346, eid="D_39")
d_40 = Drift(l=0.07500000000027285, eid="D_40")
absp_2836_sa3 = Drift(l=0.05, eid="ABSP.2836.SA3")
d_41 = Drift(l=0.1722999999999047, eid="D_41")
d_42 = Drift(l=0.18665000000009968, eid="D_42")
d_43 = Drift(l=0.09815000000014043, eid="D_43")
bps_2837_sa3 = Drift(l=0.23, eid="BPS.2837.SA3")
d_44 = Drift(l=0.004719999999924757, eid="D_44")
d_45 = Drift(l=0.02500000000009095, eid="D_45")
d_46 = Drift(l=0.0727799999999661, eid="D_46")
d_47 = Drift(l=0.07169999999996346, eid="D_47")
d_48 = Drift(l=0.0749999999998181, eid="D_48")
absp_2842_sa3 = Drift(l=0.05, eid="ABSP.2842.SA3")
d_49 = Drift(l=0.1722999999999047, eid="D_49")
d_50 = Drift(l=0.18665000000009968, eid="D_50")
d_51 = Drift(l=0.09815000000014043, eid="D_51")
bps_2843_sa3 = Drift(l=0.23, eid="BPS.2843.SA3")
d_52 = Drift(l=0.004719999999924757, eid="D_52")
d_53 = Drift(l=0.02500000000009095, eid="D_53")
d_54 = Drift(l=0.0727799999999661, eid="D_54")
d_55 = Drift(l=0.07169999999996346, eid="D_55")
d_56 = Drift(l=0.0749999999998181, eid="D_56")
absp_2848_sa3 = Drift(l=0.05, eid="ABSP.2848.SA3")
d_57 = Drift(l=0.1722999999999047, eid="D_57")
d_58 = Drift(l=0.18665000000009968, eid="D_58")
d_59 = Drift(l=0.09815000000014043, eid="D_59")
bps_2849_sa3 = Drift(l=0.23, eid="BPS.2849.SA3")
d_60 = Drift(l=0.004719999999924757, eid="D_60")
d_61 = Drift(l=0.02500000000009095, eid="D_61")
d_62 = Drift(l=0.0727799999999661, eid="D_62")
d_63 = Drift(l=0.07169999999996346, eid="D_63")
d_64 = Drift(l=0.0749999999998181, eid="D_64")
absp_2854_sa3 = Drift(l=0.05, eid="ABSP.2854.SA3")
d_65 = Drift(l=0.17230000000035944, eid="D_65")
d_66 = Drift(l=0.18665000000009968, eid="D_66")
d_67 = Drift(l=0.09815000000014043, eid="D_67")
bps_2855_sa3 = Drift(l=0.23, eid="BPS.2855.SA3")
d_68 = Drift(l=0.004719999999470009, eid="D_68")
d_69 = Drift(l=0.02500000000009095, eid="D_69")
d_70 = Drift(l=0.0727799999999661, eid="D_70")
d_71 = Drift(l=0.07169999999996346, eid="D_71")
d_72 = Drift(l=0.0749999999998181, eid="D_72")
absp_2861_sa3 = Drift(l=0.05, eid="ABSP.2861.SA3")
d_73 = Drift(l=0.17230000000035944, eid="D_73")
d_74 = Drift(l=0.18665000000009968, eid="D_74")
d_75 = Drift(l=0.09815000000014043, eid="D_75")
bps_2861_sa3 = Drift(l=0.23, eid="BPS.2861.SA3")
d_76 = Drift(l=0.004719999999924757, eid="D_76")
d_77 = Drift(l=0.024999999999636202, eid="D_77")
d_78 = Drift(l=0.0727799999999661, eid="D_78")
d_79 = Drift(l=0.07169999999996346, eid="D_79")
d_80 = Drift(l=0.07500000000027285, eid="D_80")
absp_2867_sa3 = Drift(l=0.05, eid="ABSP.2867.SA3")
d_81 = Drift(l=0.1722999999999047, eid="D_81")
d_82 = Drift(l=0.18665000000009968, eid="D_82")
d_83 = Drift(l=0.09815000000014043, eid="D_83")
bps_2867_sa3 = Drift(l=0.23, eid="BPS.2867.SA3")
d_84 = Drift(l=0.004719999999924757, eid="D_84")
d_85 = Drift(l=0.02500000000009095, eid="D_85")
d_86 = Drift(l=0.0727799999999661, eid="D_86")
d_87 = Drift(l=0.07169999999996346, eid="D_87")
d_88 = Drift(l=0.0749999999998181, eid="D_88")
absp_2873_sa3 = Drift(l=0.05, eid="ABSP.2873.SA3")
d_89 = Drift(l=0.1722999999999047, eid="D_89")
d_90 = Drift(l=0.18665000000009968, eid="D_90")
d_91 = Drift(l=0.33287000000006517, eid="D_91")
d_92 = Drift(l=0.21277999999983876, eid="D_92")
d_93 = Drift(l=0.4679999999997563, eid="D_93")
d_94 = Drift(l=1.4339999999997417, eid="D_94")
d_95 = Drift(l=0.4679999999998472, eid="D_95")
d_96 = Drift(l=0.261699999999928, eid="D_96")
absp_2879_sa3 = Drift(l=0.05, eid="ABSP.2879.SA3")
d_97 = Drift(l=0.1722999999999047, eid="D_97")
d_98 = Drift(l=0.18665000000009968, eid="D_98")
d_99 = Drift(l=0.09815000000014043, eid="D_99")
bps_2880_sa3 = Drift(l=0.23, eid="BPS.2880.SA3")
d_100 = Drift(l=0.004719999999924757, eid="D_100")
d_101 = Drift(l=0.02500000000009095, eid="D_101")
d_102 = Drift(l=0.0727799999999661, eid="D_102")
d_103 = Drift(l=0.07169999999996346, eid="D_103")
d_104 = Drift(l=0.0749999999998181, eid="D_104")
absp_2885_sa3 = Drift(l=0.05, eid="ABSP.2885.SA3")
d_105 = Drift(l=0.17230000000035944, eid="D_105")
d_106 = Drift(l=0.18665000000009968, eid="D_106")
d_107 = Drift(l=0.09815000000014043, eid="D_107")
bps_2886_sa3 = Drift(l=0.23, eid="BPS.2886.SA3")
d_108 = Drift(l=0.004719999999470009, eid="D_108")
d_109 = Drift(l=0.02500000000009095, eid="D_109")
d_110 = Drift(l=0.0727799999999661, eid="D_110")
d_111 = Drift(l=0.07169999999996346, eid="D_111")
d_112 = Drift(l=0.0749999999998181, eid="D_112")
absp_2891_sa3 = Drift(l=0.05, eid="ABSP.2891.SA3")
d_113 = Drift(l=0.17230000000035944, eid="D_113")
d_114 = Drift(l=0.18665000000009968, eid="D_114")
d_115 = Drift(l=0.09815000000014043, eid="D_115")
bps_2892_sa3 = Drift(l=0.23, eid="BPS.2892.SA3")
d_116 = Drift(l=0.004719999999924757, eid="D_116")
d_117 = Drift(l=0.024999999999636202, eid="D_117")
d_118 = Drift(l=0.0727799999999661, eid="D_118")
d_119 = Drift(l=0.07169999999996346, eid="D_119")
d_120 = Drift(l=0.07500000000027285, eid="D_120")
absp_2897_sa3 = Drift(l=0.05, eid="ABSP.2897.SA3")
d_121 = Drift(l=0.1722999999999047, eid="D_121")
d_122 = Drift(l=0.18665000000009968, eid="D_122")
d_123 = Drift(l=0.09815000000014043, eid="D_123")
bps_2898_sa3 = Drift(l=0.23, eid="BPS.2898.SA3")
d_124 = Drift(l=0.004719999999924757, eid="D_124")
d_125 = Drift(l=0.02500000000009095, eid="D_125")
d_126 = Drift(l=0.0727799999999661, eid="D_126")
d_127 = Drift(l=0.07169999999996346, eid="D_127")
d_128 = Drift(l=0.0749999999998181, eid="D_128")
absp_2903_sa3 = Drift(l=0.05, eid="ABSP.2903.SA3")
d_129 = Drift(l=0.1722999999999047, eid="D_129")
d_130 = Drift(l=0.18665000000009968, eid="D_130")
d_131 = Drift(l=0.09815000000014043, eid="D_131")
bps_2904_sa3 = Drift(l=0.23, eid="BPS.2904.SA3")
d_132 = Drift(l=0.004719999999924757, eid="D_132")
d_133 = Drift(l=0.02500000000009095, eid="D_133")
d_134 = Drift(l=0.0727799999999661, eid="D_134")
d_135 = Drift(l=0.07169999999996346, eid="D_135")
d_136 = Drift(l=0.0749999999998181, eid="D_136")
absp_2909_sa3 = Drift(l=0.05, eid="ABSP.2909.SA3")
d_137 = Drift(l=0.1722999999999047, eid="D_137")
d_138 = Drift(l=0.18665000000009968, eid="D_138")
d_139 = Drift(l=0.09815000000014043, eid="D_139")
bps_2910_sa3 = Drift(l=0.23, eid="BPS.2910.SA3")
d_140 = Drift(l=0.004719999999924757, eid="D_140")
d_141 = Drift(l=0.02500000000009095, eid="D_141")
d_142 = Drift(l=0.0727799999999661, eid="D_142")
d_143 = Drift(l=0.07169999999996346, eid="D_143")
d_144 = Drift(l=0.0749999999998181, eid="D_144")
absp_2915_sa3 = Drift(l=0.05, eid="ABSP.2915.SA3")
d_145 = Drift(l=0.17230000000035944, eid="D_145")
d_146 = Drift(l=0.18665000000009968, eid="D_146")
d_147 = Drift(l=0.09815000000014043, eid="D_147")
bps_2916_sa3 = Drift(l=0.23, eid="BPS.2916.SA3")
d_148 = Drift(l=0.004719999999470009, eid="D_148")
d_149 = Drift(l=0.02500000000009095, eid="D_149")
d_150 = Drift(l=0.0727799999999661, eid="D_150")
d_151 = Drift(l=0.07169999999996346, eid="D_151")
d_152 = Drift(l=0.0749999999998181, eid="D_152")
absp_2922_sa3 = Drift(l=0.05, eid="ABSP.2922.SA3")
d_153 = Drift(l=0.17230000000035944, eid="D_153")
d_154 = Drift(l=0.18665000000009968, eid="D_154")
d_155 = Drift(l=0.09815000000014043, eid="D_155")
bps_2922_sa3 = Drift(l=0.23, eid="BPS.2922.SA3")
d_156 = Drift(l=0.004719999999924757, eid="D_156")
d_157 = Drift(l=0.024999999999636202, eid="D_157")
d_158 = Drift(l=0.0727799999999661, eid="D_158")
d_159 = Drift(l=0.07169999999996346, eid="D_159")
d_160 = Drift(l=0.07500000000027285, eid="D_160")
absp_2928_sa3 = Drift(l=0.05, eid="ABSP.2928.SA3")
d_161 = Drift(l=0.1722999999999047, eid="D_161")
d_162 = Drift(l=0.18665000000009968, eid="D_162")
d_163 = Drift(l=0.09815000000014043, eid="D_163")
bps_2928_sa3 = Drift(l=0.23, eid="BPS.2928.SA3")
d_164 = Drift(l=0.004719999999924757, eid="D_164")
d_165 = Drift(l=0.02500000000009095, eid="D_165")
d_166 = Drift(l=0.0727799999999661, eid="D_166")
d_167 = Drift(l=0.07169999999996346, eid="D_167")
d_168 = Drift(l=0.0749999999998181, eid="D_168")
absp6_2934_sa3 = Drift(l=0.05, eid="ABSP6.2934.SA3")
d_169 = Drift(l=0.1722999999999047, eid="D_169")
d_170 = Drift(l=0.18665000000009968, eid="D_170")
d_171 = Drift(l=0.09815000000014043, eid="D_171")
bps_2934_sa3 = Drift(l=0.23, eid="BPS.2934.SA3")
d_172 = Drift(l=0.004719999999924757, eid="D_172")
d_173 = Drift(l=0.02500000000009095, eid="D_173")
d_174 = Drift(l=0.0727799999999661, eid="D_174")
d_175 = Drift(l=0.07169999999996346, eid="D_175")
d_176 = Drift(l=0.0749999999998181, eid="D_176")
absp6_2940_sa3 = Drift(l=0.05, eid="ABSP6.2940.SA3")
d_177 = Drift(l=0.1722999999999047, eid="D_177")
d_178 = Drift(l=0.18665000000009968, eid="D_178")
d_179 = Drift(l=0.09815000000014043, eid="D_179")
bps_2941_sa3 = Drift(l=0.23, eid="BPS.2941.SA3")
d_180 = Drift(l=0.004719999999924757, eid="D_180")
d_181 = Drift(l=0.02500000000009095, eid="D_181")
d_182 = Drift(l=0.2687799999998788, eid="D_182")
d_183 = Drift(l=0.032500000000163703, eid="D_183")
d_184 = Drift(l=0.03249999999981812, eid="D_184")
d_185 = Drift(l=0.2306999999999789, eid="D_185")
d_186 = Drift(l=0.0749999999998181, eid="D_186")
absp_2944_sa3 = Drift(l=0.05, eid="ABSP.2944.SA3")
d_187 = Drift(l=0.17230000000035944, eid="D_187")
d_188 = Drift(l=0.3985000000002401, eid="D_188")
bps_2944_sa3 = Drift(l=0.23, eid="BPS.2944.SA3")
d_189 = Drift(l=0.004719999999924757, eid="D_189")
d_190 = Drift(l=0.024999999999636202, eid="D_190")
d_191 = Drift(l=0.2687799999998788, eid="D_191")
d_192 = Drift(l=0.03250000000061845, eid="D_192")
d_193 = Drift(l=0.03249999999936337, eid="D_193")
d_194 = Drift(l=0.23070000000043364, eid="D_194")
d_195 = Drift(l=0.0749999999998181, eid="D_195")
absp6_2947_sa3 = Drift(l=0.05, eid="ABSP6.2947.SA3")
d_196 = Drift(l=0.1722999999999047, eid="D_196")
d_197 = Drift(l=0.18665000000009968, eid="D_197")
d_198 = Drift(l=0.09815000000014043, eid="D_198")
bps_2948_sa3 = Drift(l=0.23, eid="BPS.2948.SA3")
d_199 = Drift(l=0.004719999999924757, eid="D_199")
d_200 = Drift(l=0.02500000000009095, eid="D_200")
d_201 = Drift(l=0.2687799999998788, eid="D_201")
d_202 = Drift(l=0.032500000000163703, eid="D_202")
d_203 = Drift(l=0.03249999999981812, eid="D_203")
d_204 = Drift(l=0.2306999999999789, eid="D_204")
d_205 = Drift(l=0.0749999999998181, eid="D_205")
absp_2951_sa3 = Drift(l=0.05, eid="ABSP.2951.SA3")
d_206 = Drift(l=0.17230000000035944, eid="D_206")
d_207 = Drift(l=0.3985000000002401, eid="D_207")
bps_2952_sa3 = Drift(l=0.23, eid="BPS.2952.SA3")
d_208 = Drift(l=0.004719999999470009, eid="D_208")
d_209 = Drift(l=0.02500000000009095, eid="D_209")
d_210 = Drift(l=0.2687799999998788, eid="D_210")
d_211 = Drift(l=0.03250000000061845, eid="D_211")
d_212 = Drift(l=0.03249999999936337, eid="D_212")
d_213 = Drift(l=0.2306999999999789, eid="D_213")
d_214 = Drift(l=0.07500000000027285, eid="D_214")
absp_2955_sa3 = Drift(l=0.05, eid="ABSP.2955.SA3")
d_215 = Drift(l=0.1722999999999047, eid="D_215")
d_216 = Drift(l=0.18665000000009968, eid="D_216")
d_217 = Drift(l=0.040150000000147706, eid="D_217")

# Quadrupoles:
qa_2806_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2806.SA3")
qa_2812_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2812.SA3")
qa_2818_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2818.SA3")
qa_2824_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2824.SA3")
qa_2831_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2831.SA3")
qa_2837_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2837.SA3")
qa_2843_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2843.SA3")
qa_2849_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2849.SA3")
qa_2855_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2855.SA3")
qa_2861_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2861.SA3")
qa_2867_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2867.SA3")
qa_2873_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2873.SA3")
qa_2879_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2879.SA3")
qa_2885_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2885.SA3")
qa_2892_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2892.SA3")
qa_2898_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2898.SA3")
qa_2904_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2904.SA3")
qa_2910_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2910.SA3")
qa_2916_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2916.SA3")
qa_2922_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2922.SA3")
qa_2928_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2928.SA3")
qa_2934_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2934.SA3")
qa_2940_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2940.SA3")
qp_2941_sa3 = Quadrupole(l=0.1, eid="QP.2941.SA3")
qp_2943_sa3 = Quadrupole(l=0.1, eid="QP.2943.SA3")
qp_2945_sa3 = Quadrupole(l=0.1, eid="QP.2945.SA3")
qp_2947_sa3 = Quadrupole(l=0.1, eid="QP.2947.SA3")
qa_2948_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991207, eid="QA.2948.SA3")
qp_2948_sa3 = Quadrupole(l=0.1, eid="QP.2948.SA3")
qp_2951_sa3 = Quadrupole(l=0.1, eid="QP.2951.SA3")
qp_2952_sa3 = Quadrupole(l=0.1, eid="QP.2952.SA3")
qp_2954_sa3 = Quadrupole(l=0.1, eid="QP.2954.SA3")
qa_2955_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991207, eid="QA.2955.SA3")

# SBends:
bsl_2874_sa3 = SBend(l=0.6, eid="BSL.2874.SA3")
bsl_2875_sa3 = SBend(l=0.6, eid="BSL.2875.SA3")
bsl_2877_sa3 = SBend(l=0.6, eid="BSL.2877.SA3")
bsl_2878_sa3 = SBend(l=0.6, eid="BSL.2878.SA3")

# Hcors:
cax_2807_sa3 = Hcor(eid="CAX.2807.SA3")
cbx_2812_sa3 = Hcor(eid="CBX.2812.SA3")
cax_2813_sa3 = Hcor(eid="CAX.2813.SA3")
cbx_2818_sa3 = Hcor(eid="CBX.2818.SA3")
cax_2819_sa3 = Hcor(eid="CAX.2819.SA3")
cbx_2824_sa3 = Hcor(eid="CBX.2824.SA3")
cax_2825_sa3 = Hcor(eid="CAX.2825.SA3")
cbx_2830_sa3 = Hcor(eid="CBX.2830.SA3")
cax_2831_sa3 = Hcor(eid="CAX.2831.SA3")
cbx_2836_sa3 = Hcor(eid="CBX.2836.SA3")
cax_2838_sa3 = Hcor(eid="CAX.2838.SA3")
cbx_2842_sa3 = Hcor(eid="CBX.2842.SA3")
cax_2844_sa3 = Hcor(eid="CAX.2844.SA3")
cbx_2848_sa3 = Hcor(eid="CBX.2848.SA3")
cax_2850_sa3 = Hcor(eid="CAX.2850.SA3")
cbx_2854_sa3 = Hcor(eid="CBX.2854.SA3")
cax_2856_sa3 = Hcor(eid="CAX.2856.SA3")
cbx_2860_sa3 = Hcor(eid="CBX.2860.SA3")
cax_2862_sa3 = Hcor(eid="CAX.2862.SA3")
cbx_2867_sa3 = Hcor(eid="CBX.2867.SA3")
cax_2868_sa3 = Hcor(eid="CAX.2868.SA3")
cbx_2873_sa3 = Hcor(eid="CBX.2873.SA3")
cbsl_2875_sa3 = Hcor(eid="CBSL.2875.SA3")
cbsl_2877_sa3 = Hcor(eid="CBSL.2877.SA3")
cax_2880_sa3 = Hcor(eid="CAX.2880.SA3")
cbx_2885_sa3 = Hcor(eid="CBX.2885.SA3")
cax_2886_sa3 = Hcor(eid="CAX.2886.SA3")
cbx_2891_sa3 = Hcor(eid="CBX.2891.SA3")
cax_2892_sa3 = Hcor(eid="CAX.2892.SA3")
cbx_2897_sa3 = Hcor(eid="CBX.2897.SA3")
cax_2899_sa3 = Hcor(eid="CAX.2899.SA3")
cbx_2903_sa3 = Hcor(eid="CBX.2903.SA3")
cax_2905_sa3 = Hcor(eid="CAX.2905.SA3")
cbx_2909_sa3 = Hcor(eid="CBX.2909.SA3")
cax_2911_sa3 = Hcor(eid="CAX.2911.SA3")
cbx_2915_sa3 = Hcor(eid="CBX.2915.SA3")
cax_2917_sa3 = Hcor(eid="CAX.2917.SA3")
cbx_2921_sa3 = Hcor(eid="CBX.2921.SA3")
cax_2923_sa3 = Hcor(eid="CAX.2923.SA3")
cbx_2928_sa3 = Hcor(eid="CBX.2928.SA3")
cax_2929_sa3 = Hcor(eid="CAX.2929.SA3")
cbx_2934_sa3 = Hcor(eid="CBX.2934.SA3")
cax_2935_sa3 = Hcor(eid="CAX.2935.SA3")
cbx_2940_sa3 = Hcor(eid="CBX.2940.SA3")
cax_2941_sa3 = Hcor(eid="CAX.2941.SA3")
cbx_2943_sa3 = Hcor(eid="CBX.2943.SA3")
cax_2945_sa3 = Hcor(eid="CAX.2945.SA3")
cbx_2947_sa3 = Hcor(eid="CBX.2947.SA3")
cax_2949_sa3 = Hcor(eid="CAX.2949.SA3")
cbx_2951_sa3 = Hcor(eid="CBX.2951.SA3")
cax_2952_sa3 = Hcor(eid="CAX.2952.SA3")
cbx_2955_sa3 = Hcor(eid="CBX.2955.SA3")

# Vcors:
cay_2807_sa3 = Vcor(eid="CAY.2807.SA3")
cby_2812_sa3 = Vcor(eid="CBY.2812.SA3")
cay_2813_sa3 = Vcor(eid="CAY.2813.SA3")
cby_2818_sa3 = Vcor(eid="CBY.2818.SA3")
cay_2819_sa3 = Vcor(eid="CAY.2819.SA3")
cby_2824_sa3 = Vcor(eid="CBY.2824.SA3")
cay_2825_sa3 = Vcor(eid="CAY.2825.SA3")
cby_2830_sa3 = Vcor(eid="CBY.2830.SA3")
cay_2831_sa3 = Vcor(eid="CAY.2831.SA3")
cby_2836_sa3 = Vcor(eid="CBY.2836.SA3")
cay_2838_sa3 = Vcor(eid="CAY.2838.SA3")
cby_2842_sa3 = Vcor(eid="CBY.2842.SA3")
cay_2844_sa3 = Vcor(eid="CAY.2844.SA3")
cby_2848_sa3 = Vcor(eid="CBY.2848.SA3")
cay_2850_sa3 = Vcor(eid="CAY.2850.SA3")
cby_2854_sa3 = Vcor(eid="CBY.2854.SA3")
cay_2856_sa3 = Vcor(eid="CAY.2856.SA3")
cby_2860_sa3 = Vcor(eid="CBY.2860.SA3")
cay_2862_sa3 = Vcor(eid="CAY.2862.SA3")
cby_2867_sa3 = Vcor(eid="CBY.2867.SA3")
cay_2868_sa3 = Vcor(eid="CAY.2868.SA3")
cby_2873_sa3 = Vcor(eid="CBY.2873.SA3")
cay_2880_sa3 = Vcor(eid="CAY.2880.SA3")
cby_2885_sa3 = Vcor(eid="CBY.2885.SA3")
cay_2886_sa3 = Vcor(eid="CAY.2886.SA3")
cby_2891_sa3 = Vcor(eid="CBY.2891.SA3")
cay_2892_sa3 = Vcor(eid="CAY.2892.SA3")
cby_2897_sa3 = Vcor(eid="CBY.2897.SA3")
cay_2899_sa3 = Vcor(eid="CAY.2899.SA3")
cby_2903_sa3 = Vcor(eid="CBY.2903.SA3")
cay_2905_sa3 = Vcor(eid="CAY.2905.SA3")
cby_2909_sa3 = Vcor(eid="CBY.2909.SA3")
cay_2911_sa3 = Vcor(eid="CAY.2911.SA3")
cby_2915_sa3 = Vcor(eid="CBY.2915.SA3")
cay_2917_sa3 = Vcor(eid="CAY.2917.SA3")
cby_2921_sa3 = Vcor(eid="CBY.2921.SA3")
cay_2923_sa3 = Vcor(eid="CAY.2923.SA3")
cby_2928_sa3 = Vcor(eid="CBY.2928.SA3")
cay_2929_sa3 = Vcor(eid="CAY.2929.SA3")
cby_2934_sa3 = Vcor(eid="CBY.2934.SA3")
cay_2935_sa3 = Vcor(eid="CAY.2935.SA3")
cby_2940_sa3 = Vcor(eid="CBY.2940.SA3")
cay_2941_sa3 = Vcor(eid="CAY.2941.SA3")
cby_2943_sa3 = Vcor(eid="CBY.2943.SA3")
cay_2945_sa3 = Vcor(eid="CAY.2945.SA3")
cby_2947_sa3 = Vcor(eid="CBY.2947.SA3")
cay_2949_sa3 = Vcor(eid="CAY.2949.SA3")
cby_2951_sa3 = Vcor(eid="CBY.2951.SA3")
cay_2952_sa3 = Vcor(eid="CAY.2952.SA3")
cby_2955_sa3 = Vcor(eid="CBY.2955.SA3")

# Undulators:
u68_2809_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2809.SA3")
u68_2815_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2815.SA3")
u68_2821_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2821.SA3")
u68_2827_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2827.SA3")
u68_2834_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2834.SA3")
u68_2840_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2840.SA3")
u68_2846_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2846.SA3")
u68_2852_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2852.SA3")
u68_2858_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2858.SA3")
u68_2864_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2864.SA3")
u68_2870_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2870.SA3")
u68_2882_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2882.SA3")
u68_2888_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2888.SA3")
u68_2894_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2894.SA3")
u68_2901_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2901.SA3")
u68_2907_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2907.SA3")
u68_2913_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2913.SA3")
u68_2919_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2919.SA3")
u68_2925_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2925.SA3")
u68_2931_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2931.SA3")
u68_2937_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid="U68.2937.SA3")
ue90_2942_sa3 = Undulator(lperiod=0.09, nperiods=22.0, eid="UE90.2942.SA3")
ue90_2946_sa3 = Undulator(lperiod=0.09, nperiods=22.0, eid="UE90.2946.SA3")
ue90_2950_sa3 = Undulator(lperiod=0.09, nperiods=22.0, eid="UE90.2950.SA3")
ue90_2953_sa3 = Undulator(lperiod=0.09, nperiods=22.0, eid="UE90.2953.SA3")

# Monitors:
bpme_2806_sa3 = Monitor(eid="BPME.2806.SA3")
bpme_2812_sa3 = Monitor(eid="BPME.2812.SA3")
bpme_2818_sa3 = Monitor(eid="BPME.2818.SA3")
bpme_2824_sa3 = Monitor(eid="BPME.2824.SA3")
bpme_2830_sa3 = Monitor(eid="BPME.2830.SA3")
bpme_2836_sa3 = Monitor(eid="BPME.2836.SA3")
bpme_2842_sa3 = Monitor(eid="BPME.2842.SA3")
bpme_2849_sa3 = Monitor(eid="BPME.2849.SA3")
bpme_2855_sa3 = Monitor(eid="BPME.2855.SA3")
bpme_2861_sa3 = Monitor(eid="BPME.2861.SA3")
bpme_2867_sa3 = Monitor(eid="BPME.2867.SA3")
bpme_2873_sa3 = Monitor(eid="BPME.2873.SA3")
bpme_2879_sa3 = Monitor(eid="BPME.2879.SA3")
bpme_2885_sa3 = Monitor(eid="BPME.2885.SA3")
bpme_2891_sa3 = Monitor(eid="BPME.2891.SA3")
bpme_2897_sa3 = Monitor(eid="BPME.2897.SA3")
bpme_2903_sa3 = Monitor(eid="BPME.2903.SA3")
bpme_2910_sa3 = Monitor(eid="BPME.2910.SA3")
bpme_2916_sa3 = Monitor(eid="BPME.2916.SA3")
bpme_2922_sa3 = Monitor(eid="BPME.2922.SA3")
bpme_2928_sa3 = Monitor(eid="BPME.2928.SA3")
bpme_2934_sa3 = Monitor(eid="BPME.2934.SA3")
bpme_2940_sa3 = Monitor(eid="BPME.2940.SA3")
bpme_2944_sa3 = Monitor(eid="BPME.2944.SA3")
bpme_2947_sa3 = Monitor(eid="BPME.2947.SA3")
bpme_2951_sa3 = Monitor(eid="BPME.2951.SA3")
bpme_2955_sa3 = Monitor(eid="BPME.2955.SA3")

# Markers:
stsec_2800_sa3 = Marker(eid="STSEC.2800.SA3")
stucell_2800_sa3 = Marker(eid="STUCELL.2800.SA3")
enucell_2807_sa3 = Marker(eid="ENUCELL.2807.SA3")
stucell_2807_sa3 = Marker(eid="STUCELL.2807.SA3")
enucell_2813_sa3 = Marker(eid="ENUCELL.2813.SA3")
match_2813_sa3 = Marker(eid="MATCH.2813.SA3")
stucell_2813_sa3 = Marker(eid="STUCELL.2813.SA3")
enucell_2819_sa3 = Marker(eid="ENUCELL.2819.SA3")
stucell_2819_sa3 = Marker(eid="STUCELL.2819.SA3")
enucell_2825_sa3 = Marker(eid="ENUCELL.2825.SA3")
stucell_2825_sa3 = Marker(eid="STUCELL.2825.SA3")
enucell_2831_sa3 = Marker(eid="ENUCELL.2831.SA3")
stucell_2831_sa3 = Marker(eid="STUCELL.2831.SA3")
enucell_2837_sa3 = Marker(eid="ENUCELL.2837.SA3")
stucell_2837_sa3 = Marker(eid="STUCELL.2837.SA3")
enucell_2843_sa3 = Marker(eid="ENUCELL.2843.SA3")
stucell_2843_sa3 = Marker(eid="STUCELL.2843.SA3")
enucell_2849_sa3 = Marker(eid="ENUCELL.2849.SA3")
stucell_2849_sa3 = Marker(eid="STUCELL.2849.SA3")
enucell_2855_sa3 = Marker(eid="ENUCELL.2855.SA3")
stucell_2855_sa3 = Marker(eid="STUCELL.2855.SA3")
enucell_2861_sa3 = Marker(eid="ENUCELL.2861.SA3")
stucell_2861_sa3 = Marker(eid="STUCELL.2861.SA3")
enucell_2868_sa3 = Marker(eid="ENUCELL.2868.SA3")
stucell_2868_sa3 = Marker(eid="STUCELL.2868.SA3")
enucell_2874_sa3 = Marker(eid="ENUCELL.2874.SA3")
stucell_2874_sa3 = Marker(eid="STUCELL.2874.SA3")
enucell_2880_sa3 = Marker(eid="ENUCELL.2880.SA3")
stucell_2880_sa3 = Marker(eid="STUCELL.2880.SA3")
enucell_2886_sa3 = Marker(eid="ENUCELL.2886.SA3")
stucell_2886_sa3 = Marker(eid="STUCELL.2886.SA3")
enucell_2892_sa3 = Marker(eid="ENUCELL.2892.SA3")
stucell_2892_sa3 = Marker(eid="STUCELL.2892.SA3")
enucell_2898_sa3 = Marker(eid="ENUCELL.2898.SA3")
stucell_2898_sa3 = Marker(eid="STUCELL.2898.SA3")
enucell_2904_sa3 = Marker(eid="ENUCELL.2904.SA3")
stucell_2904_sa3 = Marker(eid="STUCELL.2904.SA3")
enucell_2910_sa3 = Marker(eid="ENUCELL.2910.SA3")
stucell_2910_sa3 = Marker(eid="STUCELL.2910.SA3")
enucell_2916_sa3 = Marker(eid="ENUCELL.2916.SA3")
stucell_2916_sa3 = Marker(eid="STUCELL.2916.SA3")
enucell_2922_sa3 = Marker(eid="ENUCELL.2922.SA3")
stucell_2922_sa3 = Marker(eid="STUCELL.2922.SA3")
enucell_2928_sa3 = Marker(eid="ENUCELL.2928.SA3")
stucell_2928_sa3 = Marker(eid="STUCELL.2928.SA3")
enucell_2935_sa3 = Marker(eid="ENUCELL.2935.SA3")
stucell_2935_sa3 = Marker(eid="STUCELL.2935.SA3")
enucell_2941_sa3 = Marker(eid="ENUCELL.2941.SA3")
stsub_2941_sa3 = Marker(eid="STSUB.2941.SA3")
stucell_2941_sa3 = Marker(eid="STUCELL.2941.SA3")
enucell_2944_sa3 = Marker(eid="ENUCELL.2944.SA3")
stucell_2944_sa3 = Marker(eid="STUCELL.2944.SA3")
enucell_2948_sa3 = Marker(eid="ENUCELL.2948.SA3")
stucell_2948_sa3 = Marker(eid="STUCELL.2948.SA3")
enucell_2952_sa3 = Marker(eid="ENUCELL.2952.SA3")
stucell_2952_sa3 = Marker(eid="STUCELL.2952.SA3")
enucell_2955_sa3 = Marker(eid="ENUCELL.2955.SA3")
ensub_2955_sa3 = Marker(eid="ENSUB.2955.SA3")
ensec_2955_sa3 = Marker(eid="ENSEC.2955.SA3")

# Sequence:
cell = (
    stsec_2800_sa3,
    d_0,
    stucell_2800_sa3,
    d_1,
    absp_2806_sa3,
    d_2,
    bpme_2806_sa3,
    d_3,
    qa_2806_sa3,
    d_4,
    enucell_2807_sa3,
    stucell_2807_sa3,
    d_5,
    cax_2807_sa3,
    cay_2807_sa3,
    d_6,
    u68_2809_sa3,
    d_7,
    cbx_2812_sa3,
    cby_2812_sa3,
    d_8,
    absp_2812_sa3,
    d_9,
    bpme_2812_sa3,
    d_10,
    qa_2812_sa3,
    d_11,
    bps_2813_sa3,
    d_12,
    enucell_2813_sa3,
    match_2813_sa3,
    stucell_2813_sa3,
    d_13,
    cax_2813_sa3,
    cay_2813_sa3,
    d_14,
    u68_2815_sa3,
    d_15,
    cbx_2818_sa3,
    cby_2818_sa3,
    d_16,
    absp_2818_sa3,
    d_17,
    bpme_2818_sa3,
    d_18,
    qa_2818_sa3,
    d_19,
    bps_2819_sa3,
    d_20,
    enucell_2819_sa3,
    stucell_2819_sa3,
    d_21,
    cax_2819_sa3,
    cay_2819_sa3,
    d_22,
    u68_2821_sa3,
    d_23,
    cbx_2824_sa3,
    cby_2824_sa3,
    d_24,
    absp_2824_sa3,
    d_25,
    bpme_2824_sa3,
    d_26,
    qa_2824_sa3,
    d_27,
    bps_2825_sa3,
    d_28,
    enucell_2825_sa3,
    stucell_2825_sa3,
    d_29,
    cax_2825_sa3,
    cay_2825_sa3,
    d_30,
    u68_2827_sa3,
    d_31,
    cbx_2830_sa3,
    cby_2830_sa3,
    d_32,
    absp_2830_sa3,
    d_33,
    bpme_2830_sa3,
    d_34,
    qa_2831_sa3,
    d_35,
    bps_2831_sa3,
    d_36,
    enucell_2831_sa3,
    stucell_2831_sa3,
    d_37,
    cax_2831_sa3,
    cay_2831_sa3,
    d_38,
    u68_2834_sa3,
    d_39,
    cbx_2836_sa3,
    cby_2836_sa3,
    d_40,
    absp_2836_sa3,
    d_41,
    bpme_2836_sa3,
    d_42,
    qa_2837_sa3,
    d_43,
    bps_2837_sa3,
    d_44,
    enucell_2837_sa3,
    stucell_2837_sa3,
    d_45,
    cax_2838_sa3,
    cay_2838_sa3,
    d_46,
    u68_2840_sa3,
    d_47,
    cbx_2842_sa3,
    cby_2842_sa3,
    d_48,
    absp_2842_sa3,
    d_49,
    bpme_2842_sa3,
    d_50,
    qa_2843_sa3,
    d_51,
    bps_2843_sa3,
    d_52,
    enucell_2843_sa3,
    stucell_2843_sa3,
    d_53,
    cax_2844_sa3,
    cay_2844_sa3,
    d_54,
    u68_2846_sa3,
    d_55,
    cbx_2848_sa3,
    cby_2848_sa3,
    d_56,
    absp_2848_sa3,
    d_57,
    bpme_2849_sa3,
    d_58,
    qa_2849_sa3,
    d_59,
    bps_2849_sa3,
    d_60,
    enucell_2849_sa3,
    stucell_2849_sa3,
    d_61,
    cax_2850_sa3,
    cay_2850_sa3,
    d_62,
    u68_2852_sa3,
    d_63,
    cbx_2854_sa3,
    cby_2854_sa3,
    d_64,
    absp_2854_sa3,
    d_65,
    bpme_2855_sa3,
    d_66,
    qa_2855_sa3,
    d_67,
    bps_2855_sa3,
    d_68,
    enucell_2855_sa3,
    stucell_2855_sa3,
    d_69,
    cax_2856_sa3,
    cay_2856_sa3,
    d_70,
    u68_2858_sa3,
    d_71,
    cbx_2860_sa3,
    cby_2860_sa3,
    d_72,
    absp_2861_sa3,
    d_73,
    bpme_2861_sa3,
    d_74,
    qa_2861_sa3,
    d_75,
    bps_2861_sa3,
    d_76,
    enucell_2861_sa3,
    stucell_2861_sa3,
    d_77,
    cax_2862_sa3,
    cay_2862_sa3,
    d_78,
    u68_2864_sa3,
    d_79,
    cbx_2867_sa3,
    cby_2867_sa3,
    d_80,
    absp_2867_sa3,
    d_81,
    bpme_2867_sa3,
    d_82,
    qa_2867_sa3,
    d_83,
    bps_2867_sa3,
    d_84,
    enucell_2868_sa3,
    stucell_2868_sa3,
    d_85,
    cax_2868_sa3,
    cay_2868_sa3,
    d_86,
    u68_2870_sa3,
    d_87,
    cbx_2873_sa3,
    cby_2873_sa3,
    d_88,
    absp_2873_sa3,
    d_89,
    bpme_2873_sa3,
    d_90,
    qa_2873_sa3,
    d_91,
    enucell_2874_sa3,
    stucell_2874_sa3,
    d_92,
    bsl_2874_sa3,
    d_93,
    bsl_2875_sa3,
    cbsl_2875_sa3,
    d_94,
    bsl_2877_sa3,
    cbsl_2877_sa3,
    d_95,
    bsl_2878_sa3,
    d_96,
    absp_2879_sa3,
    d_97,
    bpme_2879_sa3,
    d_98,
    qa_2879_sa3,
    d_99,
    bps_2880_sa3,
    d_100,
    enucell_2880_sa3,
    stucell_2880_sa3,
    d_101,
    cax_2880_sa3,
    cay_2880_sa3,
    d_102,
    u68_2882_sa3,
    d_103,
    cbx_2885_sa3,
    cby_2885_sa3,
    d_104,
    absp_2885_sa3,
    d_105,
    bpme_2885_sa3,
    d_106,
    qa_2885_sa3,
    d_107,
    bps_2886_sa3,
    d_108,
    enucell_2886_sa3,
    stucell_2886_sa3,
    d_109,
    cax_2886_sa3,
    cay_2886_sa3,
    d_110,
    u68_2888_sa3,
    d_111,
    cbx_2891_sa3,
    cby_2891_sa3,
    d_112,
    absp_2891_sa3,
    d_113,
    bpme_2891_sa3,
    d_114,
    qa_2892_sa3,
    d_115,
    bps_2892_sa3,
    d_116,
    enucell_2892_sa3,
    stucell_2892_sa3,
    d_117,
    cax_2892_sa3,
    cay_2892_sa3,
    d_118,
    u68_2894_sa3,
    d_119,
    cbx_2897_sa3,
    cby_2897_sa3,
    d_120,
    absp_2897_sa3,
    d_121,
    bpme_2897_sa3,
    d_122,
    qa_2898_sa3,
    d_123,
    bps_2898_sa3,
    d_124,
    enucell_2898_sa3,
    stucell_2898_sa3,
    d_125,
    cax_2899_sa3,
    cay_2899_sa3,
    d_126,
    u68_2901_sa3,
    d_127,
    cbx_2903_sa3,
    cby_2903_sa3,
    d_128,
    absp_2903_sa3,
    d_129,
    bpme_2903_sa3,
    d_130,
    qa_2904_sa3,
    d_131,
    bps_2904_sa3,
    d_132,
    enucell_2904_sa3,
    stucell_2904_sa3,
    d_133,
    cax_2905_sa3,
    cay_2905_sa3,
    d_134,
    u68_2907_sa3,
    d_135,
    cbx_2909_sa3,
    cby_2909_sa3,
    d_136,
    absp_2909_sa3,
    d_137,
    bpme_2910_sa3,
    d_138,
    qa_2910_sa3,
    d_139,
    bps_2910_sa3,
    d_140,
    enucell_2910_sa3,
    stucell_2910_sa3,
    d_141,
    cax_2911_sa3,
    cay_2911_sa3,
    d_142,
    u68_2913_sa3,
    d_143,
    cbx_2915_sa3,
    cby_2915_sa3,
    d_144,
    absp_2915_sa3,
    d_145,
    bpme_2916_sa3,
    d_146,
    qa_2916_sa3,
    d_147,
    bps_2916_sa3,
    d_148,
    enucell_2916_sa3,
    stucell_2916_sa3,
    d_149,
    cax_2917_sa3,
    cay_2917_sa3,
    d_150,
    u68_2919_sa3,
    d_151,
    cbx_2921_sa3,
    cby_2921_sa3,
    d_152,
    absp_2922_sa3,
    d_153,
    bpme_2922_sa3,
    d_154,
    qa_2922_sa3,
    d_155,
    bps_2922_sa3,
    d_156,
    enucell_2922_sa3,
    stucell_2922_sa3,
    d_157,
    cax_2923_sa3,
    cay_2923_sa3,
    d_158,
    u68_2925_sa3,
    d_159,
    cbx_2928_sa3,
    cby_2928_sa3,
    d_160,
    absp_2928_sa3,
    d_161,
    bpme_2928_sa3,
    d_162,
    qa_2928_sa3,
    d_163,
    bps_2928_sa3,
    d_164,
    enucell_2928_sa3,
    stucell_2928_sa3,
    d_165,
    cax_2929_sa3,
    cay_2929_sa3,
    d_166,
    u68_2931_sa3,
    d_167,
    cbx_2934_sa3,
    cby_2934_sa3,
    d_168,
    absp6_2934_sa3,
    d_169,
    bpme_2934_sa3,
    d_170,
    qa_2934_sa3,
    d_171,
    bps_2934_sa3,
    d_172,
    enucell_2935_sa3,
    stucell_2935_sa3,
    d_173,
    cax_2935_sa3,
    cay_2935_sa3,
    d_174,
    u68_2937_sa3,
    d_175,
    cbx_2940_sa3,
    cby_2940_sa3,
    d_176,
    absp6_2940_sa3,
    d_177,
    bpme_2940_sa3,
    d_178,
    qa_2940_sa3,
    d_179,
    bps_2941_sa3,
    d_180,
    enucell_2941_sa3,
    stsub_2941_sa3,
    stucell_2941_sa3,
    d_181,
    cax_2941_sa3,
    cay_2941_sa3,
    d_182,
    qp_2941_sa3,
    d_183,
    ue90_2942_sa3,
    d_184,
    qp_2943_sa3,
    d_185,
    cbx_2943_sa3,
    cby_2943_sa3,
    d_186,
    absp_2944_sa3,
    d_187,
    bpme_2944_sa3,
    d_188,
    bps_2944_sa3,
    d_189,
    enucell_2944_sa3,
    stucell_2944_sa3,
    d_190,
    cax_2945_sa3,
    cay_2945_sa3,
    d_191,
    qp_2945_sa3,
    d_192,
    ue90_2946_sa3,
    d_193,
    qp_2947_sa3,
    d_194,
    cbx_2947_sa3,
    cby_2947_sa3,
    d_195,
    absp6_2947_sa3,
    d_196,
    bpme_2947_sa3,
    d_197,
    qa_2948_sa3,
    d_198,
    bps_2948_sa3,
    d_199,
    enucell_2948_sa3,
    stucell_2948_sa3,
    d_200,
    cax_2949_sa3,
    cay_2949_sa3,
    d_201,
    qp_2948_sa3,
    d_202,
    ue90_2950_sa3,
    d_203,
    qp_2951_sa3,
    d_204,
    cbx_2951_sa3,
    cby_2951_sa3,
    d_205,
    absp_2951_sa3,
    d_206,
    bpme_2951_sa3,
    d_207,
    bps_2952_sa3,
    d_208,
    enucell_2952_sa3,
    stucell_2952_sa3,
    d_209,
    cax_2952_sa3,
    cay_2952_sa3,
    d_210,
    qp_2952_sa3,
    d_211,
    ue90_2953_sa3,
    d_212,
    qp_2954_sa3,
    d_213,
    cbx_2955_sa3,
    cby_2955_sa3,
    d_214,
    absp_2955_sa3,
    d_215,
    bpme_2955_sa3,
    d_216,
    qa_2955_sa3,
    d_217,
    enucell_2955_sa3,
    ensub_2955_sa3,
    ensec_2955_sa3,
)

# Power Supply IDs:
# Quadrupole power supplies:
qa_2806_sa3.ps_id = "QA.1.SA3"
qa_2812_sa3.ps_id = "QA.2.SA3"
qa_2818_sa3.ps_id = "QA.1.SA3"
qa_2824_sa3.ps_id = "QA.2.SA3"
qa_2831_sa3.ps_id = "QA.1.SA3"
qa_2837_sa3.ps_id = "QA.2.SA3"
qa_2843_sa3.ps_id = "QA.1.SA3"
qa_2849_sa3.ps_id = "QA.2.SA3"
qa_2855_sa3.ps_id = "QA.1.SA3"
qa_2861_sa3.ps_id = "QA.2.SA3"
qa_2867_sa3.ps_id = "QA.1.SA3"
qa_2873_sa3.ps_id = "QA.2.SA3"
qa_2879_sa3.ps_id = "QA.1.SA3"
qa_2885_sa3.ps_id = "QA.2.SA3"
qa_2892_sa3.ps_id = "QA.1.SA3"
qa_2898_sa3.ps_id = "QA.2.SA3"
qa_2904_sa3.ps_id = "QA.1.SA3"
qa_2910_sa3.ps_id = "QA.2.SA3"
qa_2916_sa3.ps_id = "QA.1.SA3"
qa_2922_sa3.ps_id = "QA.2.SA3"
qa_2928_sa3.ps_id = "QA.1.SA3"
qa_2934_sa3.ps_id = "QA.2.SA3"
qa_2940_sa3.ps_id = "QA.1.SA3"
qp_2941_sa3.ps_id = "QP.CELL24.SA3"
qp_2943_sa3.ps_id = "QP.CELL24.SA3"
qp_2945_sa3.ps_id = "QP.CELL25.SA3"
qp_2947_sa3.ps_id = "QP.CELL25.SA3"
qa_2948_sa3.ps_id = "QA.2.SA3"
qp_2948_sa3.ps_id = "QP.CELL26.SA3"
qp_2951_sa3.ps_id = "QP.CELL26.SA3"
qp_2952_sa3.ps_id = "QP.CELL27.SA3"
qp_2954_sa3.ps_id = "QP.CELL27.SA3"
qa_2955_sa3.ps_id = "QA.1.SA3"

# SBend power supplies:
bsl_2874_sa3.ps_id = "BSL.1.SA3"
bsl_2875_sa3.ps_id = "BSL.1.SA3"
bsl_2877_sa3.ps_id = "BSL.1.SA3"
bsl_2878_sa3.ps_id = "BSL.1.SA3"
