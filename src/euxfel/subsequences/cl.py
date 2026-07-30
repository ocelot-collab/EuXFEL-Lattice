# Converted from component_list_2026.02.13.xls

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import (
    Drift,
    Hcor,
    Marker,
    Monitor,
    Quadrupole,
    SBend,
    Sextupole,
    Vcor,
)

twiss0 = Twiss()
twiss0.E = 14.0000000004506
twiss0.alpha_x = -1.0022055913827863
twiss0.alpha_y = 2.134937911362842
twiss0.beta_x = 42.897735593786805
twiss0.beta_y = 57.18695611464805
twiss0.Dy = -1.2083209439381936e-06
twiss0.s = 1629.702026


# fmt: off
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
d_17 = Drift(l=1.9539999999999509, eid="D_17")
d_18 = Drift(l=2.73395000000005, eid="D_18")
d_19 = Drift(l=0.1539500000000229, eid="D_19")
d_20 = Drift(l=0.17179999999998471, eid="D_20")
d_21 = Drift(l=0.441799999999988, eid="D_21")
d_22 = Drift(l=1.0499999999999545, eid="D_22")
cols_1685_cl = Drift(l=1.0, eid="COLS.1685.CL")
d_23 = Drift(l=2.150000000000091, eid="D_23")
d_24 = Drift(l=0.4500000000000455, eid="D_24")
d_25 = Drift(l=0.75, eid="D_25")
colm_1690_cl = Drift(l=0.5, eid="COLM.1690.CL")
d_26 = Drift(l=0.4417999999998301, eid="D_26")
d_27 = Drift(l=0.4257500000000378, eid="D_27")
d_28 = Drift(l=0.1539500000000229, eid="D_28")
d_29 = Drift(l=0.17179999999998471, eid="D_29")
d_30 = Drift(l=0.441799999999988, eid="D_30")
d_31 = Drift(l=0.09600000000000364, eid="D_31")
d_32 = Drift(l=1.6040000000000418, eid="D_32")
d_33 = Drift(l=4.641799999999876, eid="D_33")
d_34 = Drift(l=0.4257500000000378, eid="D_34")
d_35 = Drift(l=0.1539500000000229, eid="D_35")
d_36 = Drift(l=0.9299999999999727, eid="D_36")
d_37 = Drift(l=1.5499999999999545, eid="D_37")
d_38 = Drift(l=2.491800000000012, eid="D_38")
d_39 = Drift(l=0.4257500000000378, eid="D_39")
d_40 = Drift(l=0.1539500000000229, eid="D_40")
d_41 = Drift(l=0.17179999999998471, eid="D_41")
d_42 = Drift(l=0.441799999999988, eid="D_42")
d_43 = Drift(l=2.0499999999999545, eid="D_43")
d_44 = Drift(l=2.73395000000005, eid="D_44")
d_45 = Drift(l=0.1539500000000229, eid="D_45")
d_46 = Drift(l=0.17179999999998471, eid="D_46")
d_47 = Drift(l=0.441799999999988, eid="D_47")
d_48 = Drift(l=1.0499999999999545, eid="D_48")
cols_1721_cl = Drift(l=1.0, eid="COLS.1721.CL")
d_49 = Drift(l=2.150000000000091, eid="D_49")
d_50 = Drift(l=0.4500000000000455, eid="D_50")
d_51 = Drift(l=0.75, eid="D_51")
colm_1726_cl = Drift(l=0.5, eid="COLM.1726.CL")
d_52 = Drift(l=0.4417999999998301, eid="D_52")
d_53 = Drift(l=0.4257500000000378, eid="D_53")
d_54 = Drift(l=0.1539500000000229, eid="D_54")
d_55 = Drift(l=0.17179999999998471, eid="D_55")
d_56 = Drift(l=0.441799999999988, eid="D_56")
d_57 = Drift(l=0.09600000000000364, eid="D_57")
d_58 = Drift(l=1.6040000000000418, eid="D_58")
d_59 = Drift(l=4.641799999999876, eid="D_59")
d_60 = Drift(l=0.4257500000000378, eid="D_60")
d_61 = Drift(l=0.1539500000000229, eid="D_61")
d_62 = Drift(l=0.9299999999999727, eid="D_62")
d_63 = Drift(l=1.5499999999999545, eid="D_63")
d_64 = Drift(l=2.4917999999997846, eid="D_64")
d_65 = Drift(l=0.4257500000002652, eid="D_65")
d_66 = Drift(l=0.15394999999979553, eid="D_66")
d_67 = Drift(l=0.3800000000000182, eid="D_67")
d_68 = Drift(l=0.6750000000001819, eid="D_68")
d_69 = Drift(l=0.15544999999979153, eid="D_69")
d_70 = Drift(l=0.2209000000000001, eid="D_70")
d_71 = Drift(l=0.21045000000000846, eid="D_71")
d_72 = Drift(l=0.3604499999999007, eid="D_72")
d_73 = Drift(l=0.2209000000000001, eid="D_73")
d_74 = Drift(l=0.15545000000017217, eid="D_74")
d_75 = Drift(l=1.3189500000001317, eid="D_75")
d_76 = Drift(l=0.15394999999979553, eid="D_76")
d_77 = Drift(l=0.9299999999999727, eid="D_77")
d_78 = Drift(l=3.2839500000002317, eid="D_78")
d_79 = Drift(l=0.15394999999979553, eid="D_79")
d_80 = Drift(l=0.9299999999999727, eid="D_80")
d_81 = Drift(l=2.2839500000002317, eid="D_81")
d_82 = Drift(l=0.15394999999979553, eid="D_82")
d_83 = Drift(l=0.9299999999999727, eid="D_83")
d_84 = Drift(l=0.43430000000012114, eid="D_84")
d_85 = Drift(l=1.8496470000000045, eid="D_85")
d_86 = Drift(l=0.1539500000000229, eid="D_86")
d_87 = Drift(l=0.9299999999999727, eid="D_87")
d_88 = Drift(l=3.2839500000000044, eid="D_88")
d_89 = Drift(l=0.1539500000000229, eid="D_89")
d_90 = Drift(l=0.3800000000000182, eid="D_90")
d_91 = Drift(l=0.6849999999999454, eid="D_91")
d_92 = Drift(l=0.15544999999979153, eid="D_92")
d_93 = Drift(l=0.2209000000000001, eid="D_93")
d_94 = Drift(l=0.21045000000023584, eid="D_94")
d_95 = Drift(l=0.3604499999999007, eid="D_95")
d_96 = Drift(l=0.2209000000000001, eid="D_96")
d_97 = Drift(l=0.15545000000017217, eid="D_97")
d_98 = Drift(l=1.3089499999999135, eid="D_98")
d_99 = Drift(l=0.1539500000000229, eid="D_99")
d_100 = Drift(l=0.17179999999975734, eid="D_100")
d_101 = Drift(l=0.44180000000021535, eid="D_101")
d_102 = Drift(l=2.0499999999999545, eid="D_102")
d_103 = Drift(l=2.73395000000005, eid="D_103")
d_104 = Drift(l=0.1539500000000229, eid="D_104")
d_105 = Drift(l=0.17179999999975734, eid="D_105")
d_106 = Drift(l=0.44180000000021535, eid="D_106")
d_107 = Drift(l=1.0499999999999545, eid="D_107")
cols_1793_cl = Drift(l=1.0, eid="COLS.1793.CL")
d_108 = Drift(l=2.150000000000091, eid="D_108")
d_109 = Drift(l=0.4500000000000455, eid="D_109")
d_110 = Drift(l=0.75, eid="D_110")
colm_1798_cl = Drift(l=0.5, eid="COLM.1798.CL")
d_111 = Drift(l=0.4418000000000575, eid="D_111")
d_112 = Drift(l=0.4257500000000378, eid="D_112")
d_113 = Drift(l=0.1539500000000229, eid="D_113")
d_114 = Drift(l=0.17179999999975734, eid="D_114")
d_115 = Drift(l=0.44180000000021535, eid="D_115")
d_116 = Drift(l=1.7000000000000455, eid="D_116")
d_117 = Drift(l=4.641800000000103, eid="D_117")
d_118 = Drift(l=0.4257500000000378, eid="D_118")
d_119 = Drift(l=0.1539500000000229, eid="D_119")
d_120 = Drift(l=0.9299999999999727, eid="D_120")
d_121 = Drift(l=1.5499999999999545, eid="D_121")
d_122 = Drift(l=2.491800000000012, eid="D_122")
d_123 = Drift(l=0.4257500000000378, eid="D_123")
d_124 = Drift(l=0.1539500000000229, eid="D_124")
d_125 = Drift(l=0.17179999999975734, eid="D_125")
d_126 = Drift(l=0.44180000000021535, eid="D_126")
d_127 = Drift(l=2.0499999999999545, eid="D_127")
d_128 = Drift(l=2.73395000000005, eid="D_128")
d_129 = Drift(l=0.1539500000000229, eid="D_129")
d_130 = Drift(l=0.17179999999998471, eid="D_130")
d_131 = Drift(l=0.441799999999988, eid="D_131")
d_132 = Drift(l=4.2000000000000455, eid="D_132")
d_133 = Drift(l=0.4499999999998181, eid="D_133")
d_134 = Drift(l=0.75, eid="D_134")
colm_1834_cl = Drift(l=0.5, eid="COLM.1834.CL")
d_135 = Drift(l=0.4418000000000575, eid="D_135")
d_136 = Drift(l=0.4257500000000378, eid="D_136")
d_137 = Drift(l=0.1539500000000229, eid="D_137")
d_138 = Drift(l=0.17179999999998471, eid="D_138")
d_139 = Drift(l=0.441799999999988, eid="D_139")
d_140 = Drift(l=0.09600000000000364, eid="D_140")
d_141 = Drift(l=1.6040000000000418, eid="D_141")
d_142 = Drift(l=4.641799999999876, eid="D_142")
d_143 = Drift(l=0.4257500000000378, eid="D_143")
d_144 = Drift(l=0.1539500000000229, eid="D_144")
d_145 = Drift(l=0.9299999999999727, eid="D_145")
d_146 = Drift(l=1.5499999999999545, eid="D_146")
d_147 = Drift(l=2.491800000000012, eid="D_147")
d_148 = Drift(l=0.21680000000007893, eid="D_148")
d_149 = Drift(l=0.2089499999999589, eid="D_149")

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
be_1678_cl = SBend(l=2.50000399999999, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid="BE.1678.CL")
bl_1688_cl = SBend(l=0.20000000000004547, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid="BL.1688.CL")
bl_1695_cl = SBend(l=0.20000000000004547, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid="BL.1695.CL")
be_1705_cl = SBend(l=2.50000399999999, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid="BE.1705.CL")
be_1714_cl = SBend(l=2.50000399999999, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid="BE.1714.CL")
bl_1724_cl = SBend(l=0.20000000000004547, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid="BL.1724.CL")
bl_1731_cl = SBend(l=0.20000000000004547, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid="BL.1731.CL")
be_1741_cl = SBend(l=2.5000040000002173, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid="BE.1741.CL")
be_1786_cl = SBend(l=2.50000399999999, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid="BE.1786.CL")
bl_1796_cl = SBend(l=0.1999999999998181, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid="BL.1796.CL")
bl_1803_cl = SBend(l=0.1999999999998181, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid="BL.1803.CL")
be_1813_cl = SBend(l=2.50000399999999, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid="BE.1813.CL")
be_1822_cl = SBend(l=2.50000399999999, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid="BE.1822.CL")
bl_1832_cl = SBend(l=0.20000000000004547, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid="BL.1832.CL")
bl_1839_cl = SBend(l=0.20000000000004547, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid="BL.1839.CL")
be_1849_cl = SBend(l=2.50000399999999, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid="BE.1849.CL")

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
mbe_1678a_cl = Marker(eid="MBE.1678a.CL")
mbe_1678d_cl = Marker(eid="MBE.1678d.CL")
mbl_1688a_cl = Marker(eid="MBL.1688a.CL")
mbl_1688d_cl = Marker(eid="MBL.1688d.CL")
otrb_1689_cl = Marker(eid="OTRB.1689.CL")
midbpmi_1693_cl = Marker(eid="MIDBPMI.1693.CL")
mbl_1695a_cl = Marker(eid="MBL.1695a.CL")
mbl_1695d_cl = Marker(eid="MBL.1695d.CL")
mbe_1705a_cl = Marker(eid="MBE.1705a.CL")
mbe_1705d_cl = Marker(eid="MBE.1705d.CL")
mbe_1714a_cl = Marker(eid="MBE.1714a.CL")
mbe_1714d_cl = Marker(eid="MBE.1714d.CL")
mbl_1724a_cl = Marker(eid="MBL.1724a.CL")
mbl_1724d_cl = Marker(eid="MBL.1724d.CL")
otrb_1725_cl = Marker(eid="OTRB.1725.CL")
midbpmi_1729_cl = Marker(eid="MIDBPMI.1729.CL")
mbl_1731a_cl = Marker(eid="MBL.1731a.CL")
mbl_1731d_cl = Marker(eid="MBL.1731d.CL")
mbe_1741a_cl = Marker(eid="MBE.1741a.CL")
mbe_1741d_cl = Marker(eid="MBE.1741d.CL")
tora_1765_cl = Marker(eid="TORA.1765.CL")
mbe_1786a_cl = Marker(eid="MBE.1786a.CL")
mbe_1786d_cl = Marker(eid="MBE.1786d.CL")
mbl_1796a_cl = Marker(eid="MBL.1796a.CL")
mbl_1796d_cl = Marker(eid="MBL.1796d.CL")
otrb_1797_cl = Marker(eid="OTRB.1797.CL")
mbl_1803a_cl = Marker(eid="MBL.1803a.CL")
mbl_1803d_cl = Marker(eid="MBL.1803d.CL")
mbe_1813a_cl = Marker(eid="MBE.1813a.CL")
mbe_1813d_cl = Marker(eid="MBE.1813d.CL")
mbe_1822a_cl = Marker(eid="MBE.1822a.CL")
mbe_1822d_cl = Marker(eid="MBE.1822d.CL")
mbl_1832a_cl = Marker(eid="MBL.1832a.CL")
mbl_1832d_cl = Marker(eid="MBL.1832d.CL")
otrb_1833_cl = Marker(eid="OTRB.1833.CL")
midbpmi_1837_cl = Marker(eid="MIDBPMI.1837.CL")
mbl_1839a_cl = Marker(eid="MBL.1839a.CL")
mbl_1839d_cl = Marker(eid="MBL.1839d.CL")
mbe_1849a_cl = Marker(eid="MBE.1849a.CL")
mbe_1849d_cl = Marker(eid="MBE.1849d.CL")
ensec_1854_cl = Marker(eid="ENSEC.1854.CL")
# fmt: on

# Sequence:
cell = (
    stsec_1652_cl,
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
    mbe_1678a_cl,
    be_1678_cl,
    mbe_1678d_cl,
    d_18,
    qf_1682_cl,
    d_19,
    cfx_1683_cl,
    d_20,
    sa_1683_cl,
    d_21,
    bpma_1684_cl,
    d_22,
    cols_1685_cl,
    d_23,
    mbl_1688a_cl,
    bl_1688_cl,
    mbl_1688d_cl,
    d_24,
    otrb_1689_cl,
    d_25,
    colm_1690_cl,
    d_26,
    sa_1691_cl,
    d_27,
    qf_1691_cl,
    d_28,
    cfy_1692_cl,
    d_29,
    sa_1692_cl,
    d_30,
    midbpmi_1693_cl,
    d_31,
    bpmi_1693_cl,
    d_32,
    mbl_1695a_cl,
    bl_1695_cl,
    mbl_1695d_cl,
    d_33,
    sa_1700_cl,
    d_34,
    qf_1700_cl,
    d_35,
    cfx_1701_cl,
    d_36,
    bpma_1702_cl,
    d_37,
    mbe_1705a_cl,
    be_1705_cl,
    mbe_1705d_cl,
    d_38,
    sa_1708_cl,
    d_39,
    qf_1709_cl,
    d_40,
    cfy_1710_cl,
    d_41,
    sa_1710_cl,
    d_42,
    bpma_1711_cl,
    d_43,
    mbe_1714a_cl,
    be_1714_cl,
    mbe_1714d_cl,
    d_44,
    qf_1718_cl,
    d_45,
    cfx_1719_cl,
    d_46,
    sa_1719_cl,
    d_47,
    bpma_1720_cl,
    d_48,
    cols_1721_cl,
    d_49,
    mbl_1724a_cl,
    bl_1724_cl,
    mbl_1724d_cl,
    d_50,
    otrb_1725_cl,
    d_51,
    colm_1726_cl,
    d_52,
    sa_1726_cl,
    d_53,
    qf_1727_cl,
    d_54,
    cfy_1728_cl,
    d_55,
    sa_1728_cl,
    d_56,
    midbpmi_1729_cl,
    d_57,
    bpmi_1729_cl,
    d_58,
    mbl_1731a_cl,
    bl_1731_cl,
    mbl_1731d_cl,
    d_59,
    sa_1736_cl,
    d_60,
    qf_1736_cl,
    d_61,
    cfx_1737_cl,
    d_62,
    bpma_1738_cl,
    d_63,
    mbe_1741a_cl,
    be_1741_cl,
    mbe_1741d_cl,
    d_64,
    sa_1744_cl,
    d_65,
    qf_1745_cl,
    d_66,
    cfy_1746_cl,
    d_67,
    bpma_1746_cl,
    d_68,
    chx_1747_cl,
    d_69,
    qh_1748_cl,
    d_70,
    qh_1749_cl,
    d_71,
    bpma_1750_cl,
    d_72,
    qh_1751_cl,
    d_73,
    qh_1752_cl,
    d_74,
    chy_1753_cl,
    d_75,
    qf_1754_cl,
    d_76,
    cfx_1755_cl,
    d_77,
    bpma_1756_cl,
    d_78,
    qf_1759_cl,
    d_79,
    cfy_1760_cl,
    d_80,
    bpma_1761_cl,
    d_81,
    qf_1763_cl,
    d_82,
    cfx_1764_cl,
    d_83,
    bpma_1765_cl,
    d_84,
    tora_1765_cl,
    d_85,
    qf_1767_cl,
    d_86,
    cfy_1768_cl,
    d_87,
    bpma_1769_cl,
    d_88,
    qf_1772_cl,
    d_89,
    cfx_1773_cl,
    d_90,
    bpma_1773_cl,
    d_91,
    chy_1774_cl,
    d_92,
    qh_1775_cl,
    d_93,
    qh_1776_cl,
    d_94,
    bpma_1777_cl,
    d_95,
    qh_1778_cl,
    d_96,
    qh_1779_cl,
    d_97,
    chx_1780_cl,
    d_98,
    qf_1781_cl,
    d_99,
    cfy_1782_cl,
    d_100,
    sa_1782_cl,
    d_101,
    bpma_1783_cl,
    d_102,
    mbe_1786a_cl,
    be_1786_cl,
    mbe_1786d_cl,
    d_103,
    qf_1790_cl,
    d_104,
    cfx_1791_cl,
    d_105,
    sa_1791_cl,
    d_106,
    bpma_1792_cl,
    d_107,
    cols_1793_cl,
    d_108,
    mbl_1796a_cl,
    bl_1796_cl,
    mbl_1796d_cl,
    d_109,
    otrb_1797_cl,
    d_110,
    colm_1798_cl,
    d_111,
    sa_1798_cl,
    d_112,
    qf_1799_cl,
    d_113,
    cfy_1800_cl,
    d_114,
    sa_1800_cl,
    d_115,
    bpma_1801_cl,
    d_116,
    mbl_1803a_cl,
    bl_1803_cl,
    mbl_1803d_cl,
    d_117,
    sa_1808_cl,
    d_118,
    qf_1808_cl,
    d_119,
    cfx_1809_cl,
    d_120,
    bpma_1810_cl,
    d_121,
    mbe_1813a_cl,
    be_1813_cl,
    mbe_1813d_cl,
    d_122,
    sa_1816_cl,
    d_123,
    qf_1817_cl,
    d_124,
    cfy_1818_cl,
    d_125,
    sa_1818_cl,
    d_126,
    bpma_1819_cl,
    d_127,
    mbe_1822a_cl,
    be_1822_cl,
    mbe_1822d_cl,
    d_128,
    qf_1826_cl,
    d_129,
    cfx_1827_cl,
    d_130,
    sa_1827_cl,
    d_131,
    bpma_1828_cl,
    d_132,
    mbl_1832a_cl,
    bl_1832_cl,
    mbl_1832d_cl,
    d_133,
    otrb_1833_cl,
    d_134,
    colm_1834_cl,
    d_135,
    sa_1834_cl,
    d_136,
    qf_1835_cl,
    d_137,
    cfy_1836_cl,
    d_138,
    sa_1836_cl,
    d_139,
    midbpmi_1837_cl,
    d_140,
    bpmi_1837_cl,
    d_141,
    mbl_1839a_cl,
    bl_1839_cl,
    mbl_1839d_cl,
    d_142,
    sa_1844_cl,
    d_143,
    qf_1844_cl,
    d_144,
    cfx_1845_cl,
    d_145,
    bpma_1846_cl,
    d_146,
    mbe_1849a_cl,
    be_1849_cl,
    mbe_1849d_cl,
    d_147,
    sa_1852_cl,
    d_148,
    bpma_1853_cl,
    d_149,
    qf_1853_cl,
    ensec_1854_cl,
)

# Power Supply IDs:
# Drift power supplies:
cols_1685_cl.ps_id = "COLS.CL"
colm_1690_cl.ps_id = "COLM.CL"
cols_1721_cl.ps_id = "COLS.CL"
colm_1726_cl.ps_id = "COLM.CL"
cols_1793_cl.ps_id = "COLS.CL"
colm_1798_cl.ps_id = "COLM.CL"
colm_1834_cl.ps_id = "COLM.CL"

# Quadrupole power supplies:
qf_1660_cl.ps_id = "QF.3.CL"
qh_1667_cl.ps_id = "QH.1.CL"
qh_1669_cl.ps_id = "QH.1.CL"
qh_1670_cl.ps_id = "QH.2.CL"
qh_1671_cl.ps_id = "QH.2.CL"
qf_1673_cl.ps_id = "QF.4.CL"
qf_1682_cl.ps_id = "QF.4.CL"
qf_1691_cl.ps_id = "QF.4.CL"
qf_1700_cl.ps_id = "QF.4.CL"
qf_1709_cl.ps_id = "QF.4.CL"
qf_1718_cl.ps_id = "QF.4.CL"
qf_1727_cl.ps_id = "QF.4.CL"
qf_1736_cl.ps_id = "QF.4.CL"
qf_1745_cl.ps_id = "QF.4.CL"
qh_1748_cl.ps_id = "QH.3.CL"
qh_1749_cl.ps_id = "QH.3.CL"
qh_1751_cl.ps_id = "QH.4.CL"
qh_1752_cl.ps_id = "QH.4.CL"
qf_1754_cl.ps_id = "QF.5.CL"
qf_1759_cl.ps_id = "QF.6.CL"
qf_1763_cl.ps_id = "QF.7.CL"
qf_1767_cl.ps_id = "QF.6.CL"
qf_1772_cl.ps_id = "QF.5.CL"
qh_1775_cl.ps_id = "QH.4.CL"
qh_1776_cl.ps_id = "QH.4.CL"
qh_1778_cl.ps_id = "QH.3.CL"
qh_1779_cl.ps_id = "QH.3.CL"
qf_1781_cl.ps_id = "QF.4.CL"
qf_1790_cl.ps_id = "QF.4.CL"
qf_1799_cl.ps_id = "QF.4.CL"
qf_1808_cl.ps_id = "QF.4.CL"
qf_1817_cl.ps_id = "QF.4.CL"
qf_1826_cl.ps_id = "QF.4.CL"
qf_1835_cl.ps_id = "QF.4.CL"
qf_1844_cl.ps_id = "QF.4.CL"
qf_1853_cl.ps_id = "QF.4.CL"

# SBend power supplies:
be_1678_cl.ps_id = "BE.1.CL"
bl_1688_cl.ps_id = "BL.1.CL"
bl_1695_cl.ps_id = "BL.1.CL"
be_1705_cl.ps_id = "BE.1.CL"
be_1714_cl.ps_id = "BE.1.CL"
bl_1724_cl.ps_id = "BL.1.CL"
bl_1731_cl.ps_id = "BL.1.CL"
be_1741_cl.ps_id = "BE.1.CL"
be_1786_cl.ps_id = "BE.2.CL"
bl_1796_cl.ps_id = "BL.2.CL"
bl_1803_cl.ps_id = "BL.2.CL"
be_1813_cl.ps_id = "BE.2.CL"
be_1822_cl.ps_id = "BE.2.CL"
bl_1832_cl.ps_id = "BL.2.CL"
bl_1839_cl.ps_id = "BL.2.CL"
be_1849_cl.ps_id = "BE.2.CL"

# Sextupole power supplies:
sa_1674_cl.ps_id = "SA.1.CL"
sa_1683_cl.ps_id = "SA.2.CL"
sa_1691_cl.ps_id = "SA.3.CL"
sa_1692_cl.ps_id = "SA.3.CL"
sa_1700_cl.ps_id = "SA.2.CL"
sa_1708_cl.ps_id = "SA.1.CL"
sa_1710_cl.ps_id = "SA.1.CL"
sa_1719_cl.ps_id = "SA.2.CL"
sa_1726_cl.ps_id = "SA.3.CL"
sa_1728_cl.ps_id = "SA.3.CL"
sa_1736_cl.ps_id = "SA.2.CL"
sa_1744_cl.ps_id = "SA.1.CL"
sa_1782_cl.ps_id = "SA.4.CL"
sa_1791_cl.ps_id = "SA.5.CL"
sa_1798_cl.ps_id = "SA.6.CL"
sa_1800_cl.ps_id = "SA.6.CL"
sa_1808_cl.ps_id = "SA.5.CL"
sa_1816_cl.ps_id = "SA.4.CL"
sa_1818_cl.ps_id = "SA.4.CL"
sa_1827_cl.ps_id = "SA.5.CL"
sa_1834_cl.ps_id = "SA.6.CL"
sa_1836_cl.ps_id = "SA.6.CL"
sa_1844_cl.ps_id = "SA.5.CL"
sa_1852_cl.ps_id = "SA.4.CL"

# Hcor power supplies:
cfx_1660_cl.ps_id = "CFX.1.CL"
chx_1672_cl.ps_id = "CHX.2.CL"
cfx_1683_cl.ps_id = "CFX.3.CL"
cfx_1701_cl.ps_id = "CFX.4.CL"
cfx_1719_cl.ps_id = "CFX.5.CL"
cfx_1737_cl.ps_id = "CFX.6.CL"
chx_1747_cl.ps_id = "CHX.7.CL"
cfx_1755_cl.ps_id = "CFX.8.CL"
cfx_1764_cl.ps_id = "CFX.9.CL"
cfx_1773_cl.ps_id = "CFX.10.CL"
chx_1780_cl.ps_id = "CHX.11.CL"
cfx_1791_cl.ps_id = "CFX.12.CL"
cfx_1809_cl.ps_id = "CFX.13.CL"
cfx_1827_cl.ps_id = "CFX.14.CL"
cfx_1845_cl.ps_id = "CFX.15.CL"

# Vcor power supplies:
chy_1667_cl.ps_id = "CHY.1.CL"
cfy_1674_cl.ps_id = "CFY.2.CL"
cfy_1692_cl.ps_id = "CFY.3.CL"
cfy_1710_cl.ps_id = "CFY.4.CL"
cfy_1728_cl.ps_id = "CFY.5.CL"
cfy_1746_cl.ps_id = "CFY.6.CL"
chy_1753_cl.ps_id = "CHY.7.CL"
cfy_1760_cl.ps_id = "CFY.8.CL"
cfy_1768_cl.ps_id = "CFY.9.CL"
chy_1774_cl.ps_id = "CHY.10.CL"
cfy_1782_cl.ps_id = "CFY.11.CL"
cfy_1800_cl.ps_id = "CFY.12.CL"
cfy_1818_cl.ps_id = "CFY.13.CL"
cfy_1836_cl.ps_id = "CFY.14.CL"

# Monitor power supplies:
bpma_1659_cl.ps_id = "BPMA.CL"
bpma_1669_cl.ps_id = "BPMA.CL"
bpmi_1675_cl.ps_id = "BPMI.E.CL"
bpma_1684_cl.ps_id = "BPMA.CL"
bpmi_1693_cl.ps_id = "BPMI.E.CL"
bpma_1702_cl.ps_id = "BPMA.CL"
bpma_1711_cl.ps_id = "BPMA.CL"
bpma_1720_cl.ps_id = "BPMA.CL"
bpmi_1729_cl.ps_id = "BPMI.E.CL"
bpma_1738_cl.ps_id = "BPMA.CL"
bpma_1746_cl.ps_id = "BPMA.CL"
bpma_1750_cl.ps_id = "BPMA.CL"
bpma_1756_cl.ps_id = "BPMA.CL"
bpma_1761_cl.ps_id = "BPMA.CL"
bpma_1765_cl.ps_id = "BPMA.CL"
bpma_1769_cl.ps_id = "BPMA.CL"
bpma_1773_cl.ps_id = "BPMA.CL"
bpma_1777_cl.ps_id = "BPMA.CL"
bpma_1783_cl.ps_id = "BPMA.CL"
bpma_1792_cl.ps_id = "BPMA.CL"
bpma_1801_cl.ps_id = "BPMA.CL"
bpma_1810_cl.ps_id = "BPMA.CL"
bpma_1819_cl.ps_id = "BPMA.CL"
bpma_1828_cl.ps_id = "BPMA.CL"
bpmi_1837_cl.ps_id = "BPMI.E.CL"
bpma_1846_cl.ps_id = "BPMA.CL"
bpma_1853_cl.ps_id = "BPMA.CL"

# Marker power supplies:
stsec_1652_cl.ps_id = "STSEC.CL.CL"
stblock_1652_cl.ps_id = "STBLOCK.FODO.CL"
tora_1658_cl.ps_id = "TORA.CL"
dcm_1659_cl.ps_id = "DCM.CL"
match_1673_cl.ps_id = "MATCH.ARC.CL"
midbpmi_1675_cl.ps_id = "MIDBPMI.E.CL"
mbe_1678a_cl.ps_id = "MBE.1.CL"
mbe_1678d_cl.ps_id = "MBE.1.CL"
mbl_1688a_cl.ps_id = "MBL.1.CL"
mbl_1688d_cl.ps_id = "MBL.1.CL"
otrb_1689_cl.ps_id = "OTRB.CL"
midbpmi_1693_cl.ps_id = "MIDBPMI.E.CL"
mbl_1695a_cl.ps_id = "MBL.1.CL"
mbl_1695d_cl.ps_id = "MBL.1.CL"
mbe_1705a_cl.ps_id = "MBE.1.CL"
mbe_1705d_cl.ps_id = "MBE.1.CL"
mbe_1714a_cl.ps_id = "MBE.1.CL"
mbe_1714d_cl.ps_id = "MBE.1.CL"
mbl_1724a_cl.ps_id = "MBL.1.CL"
mbl_1724d_cl.ps_id = "MBL.1.CL"
otrb_1725_cl.ps_id = "OTRB.CL"
midbpmi_1729_cl.ps_id = "MIDBPMI.E.CL"
mbl_1731a_cl.ps_id = "MBL.1.CL"
mbl_1731d_cl.ps_id = "MBL.1.CL"
mbe_1741a_cl.ps_id = "MBE.1.CL"
mbe_1741d_cl.ps_id = "MBE.1.CL"
tora_1765_cl.ps_id = "TORA.CL"
mbe_1786a_cl.ps_id = "MBE.2.CL"
mbe_1786d_cl.ps_id = "MBE.2.CL"
mbl_1796a_cl.ps_id = "MBL.2.CL"
mbl_1796d_cl.ps_id = "MBL.2.CL"
otrb_1797_cl.ps_id = "OTRB.CL"
mbl_1803a_cl.ps_id = "MBL.2.CL"
mbl_1803d_cl.ps_id = "MBL.2.CL"
mbe_1813a_cl.ps_id = "MBE.2.CL"
mbe_1813d_cl.ps_id = "MBE.2.CL"
mbe_1822a_cl.ps_id = "MBE.2.CL"
mbe_1822d_cl.ps_id = "MBE.2.CL"
mbl_1832a_cl.ps_id = "MBL.2.CL"
mbl_1832d_cl.ps_id = "MBL.2.CL"
otrb_1833_cl.ps_id = "OTRB.CL"
midbpmi_1837_cl.ps_id = "MIDBPMI.E.CL"
mbl_1839a_cl.ps_id = "MBL.2.CL"
mbl_1839d_cl.ps_id = "MBL.2.CL"
mbe_1849a_cl.ps_id = "MBE.2.CL"
mbe_1849d_cl.ps_id = "MBE.2.CL"
ensec_1854_cl.ps_id = "ENSEC.CL.CL"

# Component list metadata:
# fmt: off
# Drift metadata:
cols_1685_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'VACUUM', 'class': 'ECOL', 'type': 'COLS', 'xaper': 0.02, 'yaper': 0.02}
colm_1690_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'VACUUM', 'class': 'ECOL', 'type': 'COLM', 'xaper': 0.006, 'yaper': 0.006}
cols_1721_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'VACUUM', 'class': 'ECOL', 'type': 'COLS', 'xaper': 0.02, 'yaper': 0.02}
colm_1726_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'VACUUM', 'class': 'ECOL', 'type': 'COLM', 'xaper': 0.006, 'yaper': 0.006}
cols_1793_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'VACUUM', 'class': 'ECOL', 'type': 'COLS', 'xaper': 0.02, 'yaper': 0.02}
colm_1798_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'VACUUM', 'class': 'ECOL', 'type': 'COLM', 'xaper': 0.006, 'yaper': 0.006}
colm_1834_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'VACUUM', 'class': 'ECOL', 'type': 'COLM', 'xaper': 0.006, 'yaper': 0.006}

# Quadrupole metadata:
qf_1660_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qh_1667_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qh_1669_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qh_1670_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qh_1671_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qf_1673_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1682_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1691_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1700_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1709_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1718_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1727_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1736_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1745_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qh_1748_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qh_1749_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qh_1751_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qh_1752_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qf_1754_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1759_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1763_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1767_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1772_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qh_1775_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qh_1776_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qh_1778_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qh_1779_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QH', 'xaper': 0.04, 'yaper': 0.04}
qf_1781_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1790_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1799_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1808_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1817_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1826_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1835_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1844_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_1853_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_035', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}

# SBend metadata:
be_1678_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BE', 'xaper': 0.04, 'yaper': 0.04}
bl_1688_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_1695_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
be_1705_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BE', 'xaper': 0.04, 'yaper': 0.04}
be_1714_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BE', 'xaper': 0.04, 'yaper': 0.04}
bl_1724_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_1731_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
be_1741_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BE', 'xaper': 0.04, 'yaper': 0.04}
be_1786_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BE', 'xaper': 0.04, 'yaper': 0.04}
bl_1796_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_1803_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
be_1813_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BE', 'xaper': 0.04, 'yaper': 0.04}
be_1822_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BE', 'xaper': 0.04, 'yaper': 0.04}
bl_1832_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
bl_1839_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BL', 'xaper': 0.04, 'yaper': 0.04}
be_1849_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BE', 'xaper': 0.04, 'yaper': 0.04}

# Sextupole metadata:
sa_1674_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1683_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1691_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1692_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1700_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1708_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1710_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1719_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1726_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1728_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1736_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1744_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1782_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1791_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1798_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1800_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1808_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1816_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1818_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1827_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1834_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1836_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1844_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}
sa_1852_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_035', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SA', 'xaper': 0.04, 'yaper': 0.04}

# Hcor metadata:
cfx_1660_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
chx_1672_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CHX', 'xaper': 0.04, 'yaper': 0.04}
cfx_1683_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cfx_1701_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cfx_1719_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cfx_1737_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
chx_1747_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CHX', 'xaper': 0.04, 'yaper': 0.04}
cfx_1755_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cfx_1764_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cfx_1773_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
chx_1780_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CHX', 'xaper': 0.04, 'yaper': 0.04}
cfx_1791_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cfx_1809_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cfx_1827_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cfx_1845_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}

# Vcor metadata:
chy_1667_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CHY', 'xaper': 0.04, 'yaper': 0.04}
cfy_1674_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cfy_1692_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cfy_1710_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cfy_1728_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cfy_1746_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
chy_1753_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CHY', 'xaper': 0.04, 'yaper': 0.04}
cfy_1760_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cfy_1768_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
chy_1774_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CHY', 'xaper': 0.04, 'yaper': 0.04}
cfy_1782_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cfy_1800_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cfy_1818_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cfy_1836_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}

# Monitor metadata:
bpma_1659_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1669_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpmi_1675_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMI', 'xaper': 0.04, 'yaper': 0.04}
bpma_1684_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpmi_1693_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMI', 'xaper': 0.04, 'yaper': 0.04}
bpma_1702_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1711_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1720_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpmi_1729_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMI', 'xaper': 0.04, 'yaper': 0.04}
bpma_1738_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1746_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1750_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1756_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1761_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1765_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1769_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1773_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1777_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1783_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1792_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1801_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1810_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1819_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1828_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpmi_1837_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMI', 'xaper': 0.04, 'yaper': 0.04}
bpma_1846_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_1853_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_035', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}

# Marker metadata:
stsec_1652_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MARK', 'class': 'MARK', 'type': 'STSEC', 'xaper': 0.04, 'yaper': 0.04}
stblock_1652_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MARK', 'class': 'MARK', 'type': 'STBLOCK', 'xaper': 0.04, 'yaper': 0.04}
tora_1658_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'DIAG', 'class': 'CM', 'type': 'TORA', 'xaper': 0.04, 'yaper': 0.04}
dcm_1659_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'DIAG', 'class': 'INSTR', 'type': 'DCM', 'xaper': 0.04, 'yaper': 0.04}
match_1673_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MARK', 'class': 'MARK', 'type': 'MATCH', 'xaper': 0.04, 'yaper': 0.04}
midbpmi_1675_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MARK', 'class': 'MARK', 'type': 'MIDBPMI', 'xaper': 0.04, 'yaper': 0.04}
mbe_1678a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_031', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1678d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1688a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1688d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
otrb_1689_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRB', 'xaper': 0.04, 'yaper': 0.04}
midbpmi_1693_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'MARK', 'type': 'MIDBPMI', 'xaper': 0.04, 'yaper': 0.04}
mbl_1695a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1695d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1705a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1705d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1714a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1714d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1724a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1724d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
otrb_1725_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRB', 'xaper': 0.04, 'yaper': 0.04}
midbpmi_1729_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'MARK', 'type': 'MIDBPMI', 'xaper': 0.04, 'yaper': 0.04}
mbl_1731a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1731d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1741a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_032', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1741d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
tora_1765_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'DIAG', 'class': 'CM', 'type': 'TORA', 'xaper': 0.04, 'yaper': 0.04}
mbe_1786a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_033', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1786d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1796a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1796d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
otrb_1797_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRB', 'xaper': 0.04, 'yaper': 0.04}
mbl_1803a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1803d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1813a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1813d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1822a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1822d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1832a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1832d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
otrb_1833_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRB', 'xaper': 0.04, 'yaper': 0.04}
midbpmi_1837_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'MARK', 'type': 'MIDBPMI', 'xaper': 0.04, 'yaper': 0.04}
mbl_1839a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbl_1839d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1849a_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_034', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbe_1849d_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_035', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
ensec_1854_cl.metadata = {'section': 'CL', 'subsection': 'CL', 'cad_room': 'XTL_035', 'group': 'MARK', 'class': 'MARK', 'type': 'ENSEC', 'xaper': 0.04, 'yaper': 0.04}
# fmt: on
