from ocelot import *

twiss0 = Twiss()
twiss0._E = 14.0
twiss0._beta_x = 42.895
twiss0._beta_y = 57.1921
twiss0._alpha_x = -1.0021
twiss0._alpha_y = 2.1351

# Drifts:
d_0 = Drift(l=6.388699999999972, eid="D_0")
d_1 = Drift(l=0.10000000000013642, eid="D_1")
d_2 = Drift(l=0.7000000000000455, eid="D_2")
d_3 = Drift(l=0.2089499999999589, eid="D_3")
d_4 = Drift(l=0.1539500000000229, eid="D_4")
d_5 = Drift(l=6.209999999999946, eid="D_5")
d_6 = Drift(l=0.15544999999979153, eid="D_6")
d_7 = Drift(l=0.2209000000000001, eid="D_7")
d_8 = Drift(l=0.21045000000023584, eid="D_8")
d_9 = Drift(l=0.3604499999999007, eid="D_9")
d_10 = Drift(l=0.2209000000000001, eid="D_10")
d_11 = Drift(l=0.15545000000017217, eid="D_11")
d_12 = Drift(l=0.7439499999998589, eid="D_12")
d_13 = Drift(l=0.1539500000000229, eid="D_13")
d_14 = Drift(l=0.17179999999998471, eid="D_14")
d_15 = Drift(l=0.441799999999988, eid="D_15")
d_16 = Drift(l=0.09600000000000364, eid="D_16")
d_17 = Drift(l=1.9540019999999458, eid="D_17")
d_18 = Drift(l=2.733952000000045, eid="D_18")
d_19 = Drift(l=0.1539500000000229, eid="D_19")
d_20 = Drift(l=0.17179999999998471, eid="D_20")
d_21 = Drift(l=0.441799999999988, eid="D_21")
d_22 = Drift(l=4.2000000000000455, eid="D_22")
d_23 = Drift(l=0.45000000000009094, eid="D_23")
d_24 = Drift(l=1.69179999999983, eid="D_24")
d_25 = Drift(l=0.4257500000000378, eid="D_25")
d_26 = Drift(l=0.1539500000000229, eid="D_26")
d_27 = Drift(l=0.17179999999998471, eid="D_27")
d_28 = Drift(l=0.441799999999988, eid="D_28")
d_29 = Drift(l=0.09600000000000364, eid="D_29")
d_30 = Drift(l=1.6040000000000418, eid="D_30")
d_31 = Drift(l=4.641799999999921, eid="D_31")
d_32 = Drift(l=0.4257500000000378, eid="D_32")
d_33 = Drift(l=0.1539500000000229, eid="D_33")
d_34 = Drift(l=0.9299999999999727, eid="D_34")
d_35 = Drift(l=1.5500019999999495, eid="D_35")
d_36 = Drift(l=2.491802000000007, eid="D_36")
d_37 = Drift(l=0.4257500000000378, eid="D_37")
d_38 = Drift(l=0.1539500000000229, eid="D_38")
d_39 = Drift(l=0.17179999999998471, eid="D_39")
d_40 = Drift(l=0.441799999999988, eid="D_40")
d_41 = Drift(l=2.0500019999999495, eid="D_41")
d_42 = Drift(l=2.733952000000045, eid="D_42")
d_43 = Drift(l=0.1539500000000229, eid="D_43")
d_44 = Drift(l=0.17179999999998471, eid="D_44")
d_45 = Drift(l=0.441799999999988, eid="D_45")
d_46 = Drift(l=4.2000000000000455, eid="D_46")
d_47 = Drift(l=0.45000000000009094, eid="D_47")
d_48 = Drift(l=1.69179999999983, eid="D_48")
d_49 = Drift(l=0.4257500000000378, eid="D_49")
d_50 = Drift(l=0.1539500000000229, eid="D_50")
d_51 = Drift(l=0.17179999999998471, eid="D_51")
d_52 = Drift(l=0.441799999999988, eid="D_52")
d_53 = Drift(l=0.09600000000000364, eid="D_53")
d_54 = Drift(l=1.6040000000000418, eid="D_54")
d_55 = Drift(l=4.641799999999921, eid="D_55")
d_56 = Drift(l=0.4257500000000378, eid="D_56")
d_57 = Drift(l=0.1539500000000229, eid="D_57")
d_58 = Drift(l=0.9299999999999727, eid="D_58")
d_59 = Drift(l=1.5500019999999495, eid="D_59")
d_60 = Drift(l=2.491802000000007, eid="D_60")
d_61 = Drift(l=0.4257500000002652, eid="D_61")
d_62 = Drift(l=0.15394999999979553, eid="D_62")
d_63 = Drift(l=0.3800000000000182, eid="D_63")
d_64 = Drift(l=0.6750000000001819, eid="D_64")
d_65 = Drift(l=0.15544999999979153, eid="D_65")
d_66 = Drift(l=0.2209000000000001, eid="D_66")
d_67 = Drift(l=0.21045000000000846, eid="D_67")
d_68 = Drift(l=0.3604499999999007, eid="D_68")
d_69 = Drift(l=0.2209000000000001, eid="D_69")
d_70 = Drift(l=0.15545000000017217, eid="D_70")
d_71 = Drift(l=1.3189500000001317, eid="D_71")
d_72 = Drift(l=0.15394999999979553, eid="D_72")
d_73 = Drift(l=0.9299999999999727, eid="D_73")
d_74 = Drift(l=3.2839500000002317, eid="D_74")
d_75 = Drift(l=0.15394999999979553, eid="D_75")
d_76 = Drift(l=0.9299999999999727, eid="D_76")
d_77 = Drift(l=2.2839500000002317, eid="D_77")
d_78 = Drift(l=0.15394999999979553, eid="D_78")
d_79 = Drift(l=0.9299999999999727, eid="D_79")
d_80 = Drift(l=0.43430000000012114, eid="D_80")
d_81 = Drift(l=1.8496470000000045, eid="D_81")
d_82 = Drift(l=0.1539500000000229, eid="D_82")
d_83 = Drift(l=0.9299999999999727, eid="D_83")
d_84 = Drift(l=3.2839500000000044, eid="D_84")
d_85 = Drift(l=0.1539500000000229, eid="D_85")
d_86 = Drift(l=0.3800000000000182, eid="D_86")
d_87 = Drift(l=0.6849999999999454, eid="D_87")
d_88 = Drift(l=0.15544999999979153, eid="D_88")
d_89 = Drift(l=0.2209000000000001, eid="D_89")
d_90 = Drift(l=0.21045000000023584, eid="D_90")
d_91 = Drift(l=0.3604499999999007, eid="D_91")
d_92 = Drift(l=0.2209000000000001, eid="D_92")
d_93 = Drift(l=0.15545000000017217, eid="D_93")
d_94 = Drift(l=1.3089499999999135, eid="D_94")
d_95 = Drift(l=0.1539500000000229, eid="D_95")
d_96 = Drift(l=0.17179999999975734, eid="D_96")
d_97 = Drift(l=0.44180000000021535, eid="D_97")
d_98 = Drift(l=2.0500019999999495, eid="D_98")
d_99 = Drift(l=2.733952000000045, eid="D_99")
d_100 = Drift(l=0.1539500000000229, eid="D_100")
d_101 = Drift(l=0.17179999999975734, eid="D_101")
d_102 = Drift(l=0.44180000000021535, eid="D_102")
d_103 = Drift(l=4.2000000000000455, eid="D_103")
d_104 = Drift(l=0.44999999999986356, eid="D_104")
d_105 = Drift(l=1.6918000000000575, eid="D_105")
d_106 = Drift(l=0.4257500000000378, eid="D_106")
d_107 = Drift(l=0.1539500000000229, eid="D_107")
d_108 = Drift(l=0.17179999999975734, eid="D_108")
d_109 = Drift(l=0.44180000000021535, eid="D_109")
d_110 = Drift(l=1.7000000000000455, eid="D_110")
d_111 = Drift(l=4.641799999999921, eid="D_111")
d_112 = Drift(l=0.4257500000000378, eid="D_112")
d_113 = Drift(l=0.1539500000000229, eid="D_113")
d_114 = Drift(l=0.9299999999999727, eid="D_114")
d_115 = Drift(l=1.5500019999999495, eid="D_115")
d_116 = Drift(l=2.491802000000007, eid="D_116")
d_117 = Drift(l=0.4257500000000378, eid="D_117")
d_118 = Drift(l=0.1539500000000229, eid="D_118")
d_119 = Drift(l=0.17179999999975734, eid="D_119")
d_120 = Drift(l=0.44180000000021535, eid="D_120")
d_121 = Drift(l=2.0500019999999495, eid="D_121")
d_122 = Drift(l=2.733952000000045, eid="D_122")
d_123 = Drift(l=0.1539500000000229, eid="D_123")
d_124 = Drift(l=0.17179999999998471, eid="D_124")
d_125 = Drift(l=0.441799999999988, eid="D_125")
d_126 = Drift(l=4.2000000000000455, eid="D_126")
d_127 = Drift(l=0.44999999999986356, eid="D_127")
d_128 = Drift(l=1.6918000000000575, eid="D_128")
d_129 = Drift(l=0.4257500000000378, eid="D_129")
d_130 = Drift(l=0.1539500000000229, eid="D_130")
d_131 = Drift(l=0.17179999999998471, eid="D_131")
d_132 = Drift(l=0.441799999999988, eid="D_132")
d_133 = Drift(l=0.09600000000000364, eid="D_133")
d_134 = Drift(l=1.6040000000000418, eid="D_134")
d_135 = Drift(l=4.641799999999921, eid="D_135")
d_136 = Drift(l=0.4257500000000378, eid="D_136")
d_137 = Drift(l=0.1539500000000229, eid="D_137")
d_138 = Drift(l=0.9299999999999727, eid="D_138")
d_139 = Drift(l=1.5500019999999495, eid="D_139")
d_140 = Drift(l=2.491802000000007, eid="D_140")
d_141 = Drift(l=0.21680000000007893, eid="D_141")
d_142 = Drift(l=0.2089499999999589, eid="D_142")

# Quadrupoles:
qf_1660_cl = Quadrupole(l=0.5321, k1=0.178404564899455, eid="QF.1660.CL")
qh_1667_cl = Quadrupole(l=1.0291, k1=-0.17334982549995143, eid="QH.1667.CL")
qh_1669_cl = Quadrupole(l=1.0291, k1=-0.17334982549995143, eid="QH.1669.CL")
qh_1670_cl = Quadrupole(l=1.0291, k1=0.33939498329997086, eid="QH.1670.CL")
qh_1671_cl = Quadrupole(l=1.0291, k1=0.33939498329997086, eid="QH.1671.CL")
qf_1673_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid="QF.1673.CL")
qf_1682_cl = Quadrupole(l=0.5321, k1=0.30130361030069536, eid="QF.1682.CL")
qf_1691_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid="QF.1691.CL")
qf_1700_cl = Quadrupole(l=0.5321, k1=0.30130361030069536, eid="QF.1700.CL")
qf_1709_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid="QF.1709.CL")
qf_1718_cl = Quadrupole(l=0.5321, k1=0.30130361030069536, eid="QF.1718.CL")
qf_1727_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid="QF.1727.CL")
qf_1736_cl = Quadrupole(l=0.5321, k1=0.30130361030069536, eid="QF.1736.CL")
qf_1745_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid="QF.1745.CL")
qh_1748_cl = Quadrupole(l=1.0291, k1=0.3239105018997182, eid="QH.1748.CL")
qh_1749_cl = Quadrupole(l=1.0291, k1=0.3239105018997182, eid="QH.1749.CL")
qh_1751_cl = Quadrupole(l=1.0291, k1=-0.22571745480031097, eid="QH.1751.CL")
qh_1752_cl = Quadrupole(l=1.0291, k1=-0.22571745480031097, eid="QH.1752.CL")
qf_1754_cl = Quadrupole(l=0.5321, k1=0.1420399287990979, eid="QF.1754.CL")
qf_1759_cl = Quadrupole(l=0.5321, k1=0.16258806439954893, eid="QF.1759.CL")
qf_1763_cl = Quadrupole(l=0.5321, k1=-0.2212328695996993, eid="QF.1763.CL")
qf_1767_cl = Quadrupole(l=0.5321, k1=0.16258806439954893, eid="QF.1767.CL")
qf_1772_cl = Quadrupole(l=0.5321, k1=0.1420399287990979, eid="QF.1772.CL")
qh_1775_cl = Quadrupole(l=1.0291, k1=-0.22571745480031097, eid="QH.1775.CL")
qh_1776_cl = Quadrupole(l=1.0291, k1=-0.22571745480031097, eid="QH.1776.CL")
qh_1778_cl = Quadrupole(l=1.0291, k1=0.3239105018997182, eid="QH.1778.CL")
qh_1779_cl = Quadrupole(l=1.0291, k1=0.3239105018997182, eid="QH.1779.CL")
qf_1781_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid="QF.1781.CL")
qf_1790_cl = Quadrupole(l=0.5321, k1=0.30130361030069536, eid="QF.1790.CL")
qf_1799_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid="QF.1799.CL")
qf_1808_cl = Quadrupole(l=0.5321, k1=0.30130361030069536, eid="QF.1808.CL")
qf_1817_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid="QF.1817.CL")
qf_1826_cl = Quadrupole(l=0.5321, k1=0.30130361030069536, eid="QF.1826.CL")
qf_1835_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid="QF.1835.CL")
qf_1844_cl = Quadrupole(l=0.5321, k1=0.30130361030069536, eid="QF.1844.CL")
qf_1853_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid="QF.1853.CL")

# SBends:
be_1678_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid="BE.1678.CL")
bl_1688_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid="BL.1688.CL")
bl_1695_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid="BL.1695.CL")
be_1705_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid="BE.1705.CL")
be_1714_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid="BE.1714.CL")
bl_1724_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid="BL.1724.CL")
bl_1731_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid="BL.1731.CL")
be_1741_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid="BE.1741.CL")
be_1786_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid="BE.1786.CL")
bl_1796_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid="BL.1796.CL")
bl_1803_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid="BL.1803.CL")
be_1813_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid="BE.1813.CL")
be_1822_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid="BE.1822.CL")
bl_1832_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid="BL.1832.CL")
bl_1839_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid="BL.1839.CL")
be_1849_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid="BE.1849.CL")

# Sextupoles:
sa_1674_cl = Sextupole(l=0.3164, k2=17.62661441, tilt=1.570796327, eid="SA.1674.CL")
sa_1683_cl = Sextupole(l=0.3164, k2=-14.82028066, tilt=1.570796327, eid="SA.1683.CL")
sa_1691_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid="SA.1691.CL")
sa_1692_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid="SA.1692.CL")
sa_1700_cl = Sextupole(l=0.3164, k2=-14.82028066, tilt=1.570796327, eid="SA.1700.CL")
sa_1708_cl = Sextupole(l=0.3164, k2=17.62661441, tilt=1.570796327, eid="SA.1708.CL")
sa_1710_cl = Sextupole(l=0.3164, k2=17.62661441, tilt=1.570796327, eid="SA.1710.CL")
sa_1719_cl = Sextupole(l=0.3164, k2=-14.82028066, tilt=1.570796327, eid="SA.1719.CL")
sa_1726_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid="SA.1726.CL")
sa_1728_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid="SA.1728.CL")
sa_1736_cl = Sextupole(l=0.3164, k2=-14.82028066, tilt=1.570796327, eid="SA.1736.CL")
sa_1744_cl = Sextupole(l=0.3164, k2=17.62661441, tilt=1.570796327, eid="SA.1744.CL")
sa_1782_cl = Sextupole(l=0.3164, k2=-17.62661441, tilt=1.570796327, eid="SA.1782.CL")
sa_1791_cl = Sextupole(l=0.3164, k2=14.82028066, tilt=1.570796327, eid="SA.1791.CL")
sa_1798_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid="SA.1798.CL")
sa_1800_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid="SA.1800.CL")
sa_1808_cl = Sextupole(l=0.3164, k2=14.82028066, tilt=1.570796327, eid="SA.1808.CL")
sa_1816_cl = Sextupole(l=0.3164, k2=-17.62661441, tilt=1.570796327, eid="SA.1816.CL")
sa_1818_cl = Sextupole(l=0.3164, k2=-17.62661441, tilt=1.570796327, eid="SA.1818.CL")
sa_1827_cl = Sextupole(l=0.3164, k2=14.82028066, tilt=1.570796327, eid="SA.1827.CL")
sa_1834_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid="SA.1834.CL")
sa_1836_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid="SA.1836.CL")
sa_1844_cl = Sextupole(l=0.3164, k2=14.82028066, tilt=1.570796327, eid="SA.1844.CL")
sa_1852_cl = Sextupole(l=0.3164, k2=-17.62661441, tilt=1.570796327, eid="SA.1852.CL")

# Hcors:
cfx_1660_cl = Hcor(l=0.1, eid="CFX.1660.CL")
chx_1672_cl = Hcor(l=0.2, eid="CHX.1672.CL")
cfx_1683_cl = Hcor(l=0.1, eid="CFX.1683.CL")
cfx_1701_cl = Hcor(l=0.1, eid="CFX.1701.CL")
cfx_1719_cl = Hcor(l=0.1, eid="CFX.1719.CL")
cfx_1737_cl = Hcor(l=0.1, eid="CFX.1737.CL")
chx_1747_cl = Hcor(l=0.2, eid="CHX.1747.CL")
cfx_1755_cl = Hcor(l=0.1, eid="CFX.1755.CL")
cfx_1764_cl = Hcor(l=0.1, eid="CFX.1764.CL")
cfx_1773_cl = Hcor(l=0.1, eid="CFX.1773.CL")
chx_1780_cl = Hcor(l=0.2, eid="CHX.1780.CL")
cfx_1791_cl = Hcor(l=0.1, eid="CFX.1791.CL")
cfx_1809_cl = Hcor(l=0.1, eid="CFX.1809.CL")
cfx_1827_cl = Hcor(l=0.1, eid="CFX.1827.CL")
cfx_1845_cl = Hcor(l=0.1, eid="CFX.1845.CL")

# Vcors:
chy_1667_cl = Vcor(l=0.2, eid="CHY.1667.CL")
cfy_1674_cl = Vcor(l=0.1, eid="CFY.1674.CL")
cfy_1692_cl = Vcor(l=0.1, eid="CFY.1692.CL")
cfy_1710_cl = Vcor(l=0.1, eid="CFY.1710.CL")
cfy_1728_cl = Vcor(l=0.1, eid="CFY.1728.CL")
cfy_1746_cl = Vcor(l=0.1, eid="CFY.1746.CL")
chy_1753_cl = Vcor(l=0.2, eid="CHY.1753.CL")
cfy_1760_cl = Vcor(l=0.1, eid="CFY.1760.CL")
cfy_1768_cl = Vcor(l=0.1, eid="CFY.1768.CL")
chy_1774_cl = Vcor(l=0.2, eid="CHY.1774.CL")
cfy_1782_cl = Vcor(l=0.1, eid="CFY.1782.CL")
cfy_1800_cl = Vcor(l=0.1, eid="CFY.1800.CL")
cfy_1818_cl = Vcor(l=0.1, eid="CFY.1818.CL")
cfy_1836_cl = Vcor(l=0.1, eid="CFY.1836.CL")

# Monitors:
bpma_1659_cl = Monitor(eid="BPMA.1659.CL")
bpma_1669_cl = Monitor(eid="BPMA.1669.CL")
bpmi_1675_cl = Monitor(eid="BPMI.1675.CL")
bpma_1684_cl = Monitor(eid="BPMA.1684.CL")
bpmi_1693_cl = Monitor(eid="BPMI.1693.CL")
bpma_1702_cl = Monitor(eid="BPMA.1702.CL")
bpma_1711_cl = Monitor(eid="BPMA.1711.CL")
bpma_1720_cl = Monitor(eid="BPMA.1720.CL")
bpmi_1729_cl = Monitor(eid="BPMI.1729.CL")
bpma_1738_cl = Monitor(eid="BPMA.1738.CL")
bpma_1746_cl = Monitor(eid="BPMA.1746.CL")
bpma_1750_cl = Monitor(eid="BPMA.1750.CL")
bpma_1756_cl = Monitor(eid="BPMA.1756.CL")
bpma_1761_cl = Monitor(eid="BPMA.1761.CL")
bpma_1765_cl = Monitor(eid="BPMA.1765.CL")
bpma_1769_cl = Monitor(eid="BPMA.1769.CL")
bpma_1773_cl = Monitor(eid="BPMA.1773.CL")
bpma_1777_cl = Monitor(eid="BPMA.1777.CL")
bpma_1783_cl = Monitor(eid="BPMA.1783.CL")
bpma_1792_cl = Monitor(eid="BPMA.1792.CL")
bpma_1801_cl = Monitor(eid="BPMA.1801.CL")
bpma_1810_cl = Monitor(eid="BPMA.1810.CL")
bpma_1819_cl = Monitor(eid="BPMA.1819.CL")
bpma_1828_cl = Monitor(eid="BPMA.1828.CL")
bpmi_1837_cl = Monitor(eid="BPMI.1837.CL")
bpma_1846_cl = Monitor(eid="BPMA.1846.CL")
bpma_1853_cl = Monitor(eid="BPMA.1853.CL")

# Markers:
stsec_1652_cl = Marker(eid="STSEC.1652.CL")
stblock_1652_cl = Marker(eid="STBLOCK.1652.CL")
tora_1658_cl = Marker(eid="TORA.1658.CL")
dcm_1659_cl = Marker(eid="DCM.1659.CL")
match_1673_cl = Marker(eid="MATCH.1673.CL")
midbpmi_1675_cl = Marker(eid="MIDBPMI.1675.CL")
otrb_1689_cl = Marker(eid="OTRB.1689.CL")
midbpmi_1693_cl = Marker(eid="MIDBPMI.1693.CL")
otrb_1725_cl = Marker(eid="OTRB.1725.CL")
midbpmi_1729_cl = Marker(eid="MIDBPMI.1729.CL")
tora_1765_cl = Marker(eid="TORA.1765.CL")
otrb_1797_cl = Marker(eid="OTRB.1797.CL")
otrb_1833_cl = Marker(eid="OTRB.1833.CL")
midbpmi_1837_cl = Marker(eid="MIDBPMI.1837.CL")
ensec_1854_cl = Marker(eid="ENSEC.1854.CL")

# Sequence:
cell = (stsec_1652_cl,
        stblock_1652_cl,
        d_0,
        tora_1658_cl,
        d_1,
        dcm_1659_cl,
        d_2,
        bpma_1659_cl,
        d_3,
        qf_1660_cl,
        d_4,
        cfx_1660_cl,
        d_5,
        chy_1667_cl,
        d_6,
        qh_1667_cl,
        d_7,
        qh_1669_cl,
        d_8,
        bpma_1669_cl,
        d_9,
        qh_1670_cl,
        d_10,
        qh_1671_cl,
        d_11,
        chx_1672_cl,
        d_12,
        match_1673_cl,
        qf_1673_cl,
        d_13,
        cfy_1674_cl,
        d_14,
        sa_1674_cl,
        d_15,
        midbpmi_1675_cl,
        d_16,
        bpmi_1675_cl,
        d_17,
        be_1678_cl,
        d_18,
        qf_1682_cl,
        d_19,
        cfx_1683_cl,
        d_20,
        sa_1683_cl,
        d_21,
        bpma_1684_cl,
        d_22,
        bl_1688_cl,
        d_23,
        otrb_1689_cl,
        d_24,
        sa_1691_cl,
        d_25,
        qf_1691_cl,
        d_26,
        cfy_1692_cl,
        d_27,
        sa_1692_cl,
        d_28,
        midbpmi_1693_cl,
        d_29,
        bpmi_1693_cl,
        d_30,
        bl_1695_cl,
        d_31,
        sa_1700_cl,
        d_32,
        qf_1700_cl,
        d_33,
        cfx_1701_cl,
        d_34,
        bpma_1702_cl,
        d_35,
        be_1705_cl,
        d_36,
        sa_1708_cl,
        d_37,
        qf_1709_cl,
        d_38,
        cfy_1710_cl,
        d_39,
        sa_1710_cl,
        d_40,
        bpma_1711_cl,
        d_41,
        be_1714_cl,
        d_42,
        qf_1718_cl,
        d_43,
        cfx_1719_cl,
        d_44,
        sa_1719_cl,
        d_45,
        bpma_1720_cl,
        d_46,
        bl_1724_cl,
        d_47,
        otrb_1725_cl,
        d_48,
        sa_1726_cl,
        d_49,
        qf_1727_cl,
        d_50,
        cfy_1728_cl,
        d_51,
        sa_1728_cl,
        d_52,
        midbpmi_1729_cl,
        d_53,
        bpmi_1729_cl,
        d_54,
        bl_1731_cl,
        d_55,
        sa_1736_cl,
        d_56,
        qf_1736_cl,
        d_57,
        cfx_1737_cl,
        d_58,
        bpma_1738_cl,
        d_59,
        be_1741_cl,
        d_60,
        sa_1744_cl,
        d_61,
        qf_1745_cl,
        d_62,
        cfy_1746_cl,
        d_63,
        bpma_1746_cl,
        d_64,
        chx_1747_cl,
        d_65,
        qh_1748_cl,
        d_66,
        qh_1749_cl,
        d_67,
        bpma_1750_cl,
        d_68,
        qh_1751_cl,
        d_69,
        qh_1752_cl,
        d_70,
        chy_1753_cl,
        d_71,
        qf_1754_cl,
        d_72,
        cfx_1755_cl,
        d_73,
        bpma_1756_cl,
        d_74,
        qf_1759_cl,
        d_75,
        cfy_1760_cl,
        d_76,
        bpma_1761_cl,
        d_77,
        qf_1763_cl,
        d_78,
        cfx_1764_cl,
        d_79,
        bpma_1765_cl,
        d_80,
        tora_1765_cl,
        d_81,
        qf_1767_cl,
        d_82,
        cfy_1768_cl,
        d_83,
        bpma_1769_cl,
        d_84,
        qf_1772_cl,
        d_85,
        cfx_1773_cl,
        d_86,
        bpma_1773_cl,
        d_87,
        chy_1774_cl,
        d_88,
        qh_1775_cl,
        d_89,
        qh_1776_cl,
        d_90,
        bpma_1777_cl,
        d_91,
        qh_1778_cl,
        d_92,
        qh_1779_cl,
        d_93,
        chx_1780_cl,
        d_94,
        qf_1781_cl,
        d_95,
        cfy_1782_cl,
        d_96,
        sa_1782_cl,
        d_97,
        bpma_1783_cl,
        d_98,
        be_1786_cl,
        d_99,
        qf_1790_cl,
        d_100,
        cfx_1791_cl,
        d_101,
        sa_1791_cl,
        d_102,
        bpma_1792_cl,
        d_103,
        bl_1796_cl,
        d_104,
        otrb_1797_cl,
        d_105,
        sa_1798_cl,
        d_106,
        qf_1799_cl,
        d_107,
        cfy_1800_cl,
        d_108,
        sa_1800_cl,
        d_109,
        bpma_1801_cl,
        d_110,
        bl_1803_cl,
        d_111,
        sa_1808_cl,
        d_112,
        qf_1808_cl,
        d_113,
        cfx_1809_cl,
        d_114,
        bpma_1810_cl,
        d_115,
        be_1813_cl,
        d_116,
        sa_1816_cl,
        d_117,
        qf_1817_cl,
        d_118,
        cfy_1818_cl,
        d_119,
        sa_1818_cl,
        d_120,
        bpma_1819_cl,
        d_121,
        be_1822_cl,
        d_122,
        qf_1826_cl,
        d_123,
        cfx_1827_cl,
        d_124,
        sa_1827_cl,
        d_125,
        bpma_1828_cl,
        d_126,
        bl_1832_cl,
        d_127,
        otrb_1833_cl,
        d_128,
        sa_1834_cl,
        d_129,
        qf_1835_cl,
        d_130,
        cfy_1836_cl,
        d_131,
        sa_1836_cl,
        d_132,
        midbpmi_1837_cl,
        d_133,
        bpmi_1837_cl,
        d_134,
        bl_1839_cl,
        d_135,
        sa_1844_cl,
        d_136,
        qf_1844_cl,
        d_137,
        cfx_1845_cl,
        d_138,
        bpma_1846_cl,
        d_139,
        be_1849_cl,
        d_140,
        sa_1852_cl,
        d_141,
        bpma_1853_cl,
        d_142,
        qf_1853_cl,
        ensec_1854_cl)

# Power Supply IDs:
