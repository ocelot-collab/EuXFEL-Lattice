from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 41.66496631816343
tws0.beta_y = 53.55111570484648
tws0.alpha_x = -0.9889897612957868
tws0.alpha_y = 2.004822139010063
tws0.E = 14
tws0.s = 1652.902800000028

# Drifts
id_15388144_ = Drift(l=7.1887, eid='ID_15388144_')
d_4 = Drift(l=0.20895, eid='D_4')
d_5 = Drift(l=0.15395, eid='D_5')
d_6 = Drift(l=6.21, eid='D_6')
d_7 = Drift(l=0.15545, eid='D_7')
d_8 = Drift(l=0.2209, eid='D_8')
d_9 = Drift(l=0.21045, eid='D_9')
d_10 = Drift(l=0.36045, eid='D_10')
d_13 = Drift(l=0.74395, eid='D_13')
d_15 = Drift(l=0.1718, eid='D_15')
id_389319_ = Drift(l=0.5378000000000001, eid='ID_389319_')
d_18 = Drift(l=1.954002, eid='D_18')
d_19 = Drift(l=2.733952, eid='D_19')
d_22 = Drift(l=0.4418, eid='D_22')
d_23 = Drift(l=4.2, eid='D_23')
id_50656927_ = Drift(l=2.1418, eid='ID_50656927_')
d_26 = Drift(l=0.42575, eid='D_26')
d_31 = Drift(l=1.604, eid='D_31')
d_32 = Drift(l=4.6418, eid='D_32')
d_35 = Drift(l=0.93, eid='D_35')
d_36 = Drift(l=1.550002, eid='D_36')
d_37 = Drift(l=2.491802, eid='D_37')
d_42 = Drift(l=2.050002, eid='D_42')
d_64 = Drift(l=0.38, eid='D_64')
d_65 = Drift(l=0.675, eid='D_65')
d_72 = Drift(l=1.31895, eid='D_72')
d_75 = Drift(l=3.28395, eid='D_75')
d_78 = Drift(l=2.28395, eid='D_78')
d_81 = Drift(l=2.283947, eid='D_81')
d_87 = Drift(l=0.685, eid='D_87')
d_94 = Drift(l=1.30895, eid='D_94')
d_110 = Drift(l=1.7, eid='D_110')
d_141 = Drift(l=0.2168, eid='D_141')
d_144 = Drift(l=0.69, eid='D_144')
d_147 = Drift(l=0.5709, eid='D_147')
id_22692917_ = Drift(l=0.50895, eid='ID_22692917_')
d_151 = Drift(l=0.3015, eid='D_151')
d_152 = Drift(l=2.0865, eid='D_152')
id_75563590_ = Drift(l=0.43245, eid='ID_75563590_')
id_11766094_ = Drift(l=3.3550000000000004, eid='ID_11766094_')
d_160 = Drift(l=3.855, eid='D_160')
id_94527400_ = Drift(l=4.9485, eid='ID_94527400_')
d_165 = Drift(l=2.61545, eid='D_165')
d_166 = Drift(l=2.50395, eid='D_166')
id_61704230_ = Drift(l=4.4485, eid='ID_61704230_')
d_170 = Drift(l=2.53395, eid='D_170')
id_21941902_ = Drift(l=11.83395, eid='ID_21941902_')
id_54090033_ = Drift(l=2.8074500000000002, eid='ID_54090033_')
id_25778097_ = Drift(l=11.25895, eid='ID_25778097_')
id_78367389_ = Drift(l=4.8985, eid='ID_78367389_')
id_69348953_ = Drift(l=6.36045, eid='ID_69348953_')
id_7559873_ = Drift(l=1.5985, eid='ID_7559873_')
d_191 = Drift(l=0.4815, eid='D_191')
id_5581078_ = Drift(l=0.37, eid='ID_5581078_')
d_194 = Drift(l=0.32, eid='D_194')
d_198 = Drift(l=0.283951, eid='D_198')
d_205 = Drift(l=0.41, eid='D_205')
d_206 = Drift(l=1.515, eid='D_206')
d_207 = Drift(l=0.208951, eid='D_207')
d_208 = Drift(l=0.153951, eid='D_208')
d_209 = Drift(l=0.2, eid='D_209')
d_210 = Drift(l=9.0692, eid='D_210')
d_211 = Drift(l=0.1, eid='D_211')
d_212 = Drift(l=0.15, eid='D_212')
id_63971798_ = Drift(l=2.06074, eid='ID_63971798_')

# Quadrupoles
qf_1660_cl = Quadrupole(l=0.5321, k1=0.178404564899455, eid='QF.1660.CL')
qh_1667_cl = Quadrupole(l=1.0291, k1=-0.17334982549995143, eid='QH.1667.CL')
qh_1669_cl = Quadrupole(l=1.0291, k1=-0.17334982549995143, eid='QH.1669.CL')
qh_1670_cl = Quadrupole(l=1.0291, k1=0.33939498329997086, eid='QH.1670.CL')
qh_1671_cl = Quadrupole(l=1.0291, k1=0.33939498329997086, eid='QH.1671.CL')
qf_1673_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid='QF.1673.CL')
qf_1682_cl = Quadrupole(l=0.5321, k1=0.3013036103006953, eid='QF.1682.CL')
qf_1691_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid='QF.1691.CL')
qf_1700_cl = Quadrupole(l=0.5321, k1=0.3013036103006953, eid='QF.1700.CL')
qf_1709_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid='QF.1709.CL')
qf_1718_cl = Quadrupole(l=0.5321, k1=0.3013036103006953, eid='QF.1718.CL')
qf_1727_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid='QF.1727.CL')
qf_1736_cl = Quadrupole(l=0.5321, k1=0.3013036103006953, eid='QF.1736.CL')
qf_1745_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid='QF.1745.CL')
qh_1748_cl = Quadrupole(l=1.0291, k1=0.3239105018997182, eid='QH.1748.CL')
qh_1749_cl = Quadrupole(l=1.0291, k1=0.3239105018997182, eid='QH.1749.CL')
qh_1751_cl = Quadrupole(l=1.0291, k1=-0.22571745480031097, eid='QH.1751.CL')
qh_1752_cl = Quadrupole(l=1.0291, k1=-0.22571745480031097, eid='QH.1752.CL')
qf_1754_cl = Quadrupole(l=0.5321, k1=0.1420399287990979, eid='QF.1754.CL')
qf_1759_cl = Quadrupole(l=0.5321, k1=0.16258806439954893, eid='QF.1759.CL')
qf_1763_cl = Quadrupole(l=0.5321, k1=-0.2212328695996993, eid='QF.1763.CL')
qf_1767_cl = Quadrupole(l=0.5321, k1=0.16258806439954893, eid='QF.1767.CL')
qf_1772_cl = Quadrupole(l=0.5321, k1=0.1420399287990979, eid='QF.1772.CL')
qh_1775_cl = Quadrupole(l=1.0291, k1=-0.22571745480031097, eid='QH.1775.CL')
qh_1776_cl = Quadrupole(l=1.0291, k1=-0.22571745480031097, eid='QH.1776.CL')
qh_1778_cl = Quadrupole(l=1.0291, k1=0.3239105018997182, eid='QH.1778.CL')
qh_1779_cl = Quadrupole(l=1.0291, k1=0.3239105018997182, eid='QH.1779.CL')
qf_1781_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid='QF.1781.CL')
qf_1790_cl = Quadrupole(l=0.5321, k1=0.3013036103006953, eid='QF.1790.CL')
qf_1799_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid='QF.1799.CL')
qf_1808_cl = Quadrupole(l=0.5321, k1=0.3013036103006953, eid='QF.1808.CL')
qf_1817_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid='QF.1817.CL')
qf_1826_cl = Quadrupole(l=0.5321, k1=0.3013036103006953, eid='QF.1826.CL')
qf_1835_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid='QF.1835.CL')
qf_1844_cl = Quadrupole(l=0.5321, k1=0.3013036103006953, eid='QF.1844.CL')
qf_1853_cl = Quadrupole(l=0.5321, k1=-0.30131733840067654, eid='QF.1853.CL')
qh_1855_tl = Quadrupole(l=1.0291, k1=0.3716633416004276, eid='QH.1855.TL')
qh_1857_tl = Quadrupole(l=1.0291, k1=0.34605581209989317, eid='QH.1857.TL')
qh_1858_tl = Quadrupole(l=1.0291, k1=-0.3787301584996599, eid='QH.1858.TL')
qh_1859_tl = Quadrupole(l=1.0291, k1=-0.05277408413953941, eid='QH.1859.TL')
qf_1864_tl = Quadrupole(l=0.5321, k1=0.18589860389964288, eid='QF.1864.TL')
qf_1868_tl = Quadrupole(l=0.5321, k1=-0.05512587120090208, eid='QF.1868.TL')
qf_1873_tl = Quadrupole(l=0.5321, k1=0.1199289291993986, eid='QF.1873.TL')
qf_1881_tl = Quadrupole(l=0.5321, k1=-0.20093471310092084, eid='QF.1881.TL')
qf_1892_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid='QF.1892.TL')
qf_1907_tl = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid='QF.1907.TL')
qf_1922_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid='QF.1922.TL')
qf_1937_tl = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid='QF.1937.TL')
qf_1952_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid='QF.1952.TL')
qf_1967_tl = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid='QF.1967.TL')

# SBends
be_1678_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid='BE.1678.CL')
bl_1688_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid='BL.1688.CL')
bl_1695_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid='BL.1695.CL')
be_1705_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid='BE.1705.CL')
be_1714_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid='BE.1714.CL')
bl_1724_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid='BL.1724.CL')
bl_1731_cl = SBend(l=0.2, angle=-0.000737152538, e1=-0.000368576, e2=-0.000368576, tilt=1.570796327, eid='BL.1731.CL')
be_1741_cl = SBend(l=2.5, angle=0.006233024763, e1=0.003116512, e2=0.003116512, tilt=1.570796327, eid='BE.1741.CL')
be_1786_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid='BE.1786.CL')
bl_1796_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid='BL.1796.CL')
bl_1803_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid='BL.1803.CL')
be_1813_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid='BE.1813.CL')
be_1822_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid='BE.1822.CL')
bl_1832_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid='BL.1832.CL')
bl_1839_cl = SBend(l=0.2, angle=0.000724902792, e1=0.000362451, e2=0.000362451, tilt=1.570796327, eid='BL.1839.CL')
be_1849_cl = SBend(l=2.5, angle=-0.006129494209, e1=-0.003064747, e2=-0.003064747, tilt=1.570796327, eid='BE.1849.CL')

# RBends
kspos_1941_tl = RBend(l=1.0, eid='KSPOS.1941.TL')
ksneg_1941_tl = RBend(l=1.0, eid='KSNEG.1941.TL')
kspos_1943_tl = RBend(l=1.0, eid='KSPOS.1943.TL')
ksneg_1943_tl = RBend(l=1.0, eid='KSNEG.1943.TL')
kspos_1945_tl = RBend(l=1.0, eid='KSPOS.1945.TL')
ksneg_1945_tl = RBend(l=1.0, eid='KSNEG.1945.TL')
kspos_1948_tl = RBend(l=1.0, eid='KSPOS.1948.TL')
ksneg_1948_tl = RBend(l=1.0, eid='KSNEG.1948.TL')
kspos_1950_tl = RBend(l=1.0, eid='KSPOS.1950.TL')
ksneg_1950_tl = RBend(l=1.0, eid='KSNEG.1950.TL')
kspos_1953_tl = RBend(l=1.0, eid='KSPOS.1953.TL')
ksneg_1953_tl = RBend(l=1.0, eid='KSNEG.1953.TL')
kspos_1955_tl = RBend(l=1.0, eid='KSPOS.1955.TL')
ksneg_1955_tl = RBend(l=1.0, eid='KSNEG.1955.TL')
kspos_1958_tl = RBend(l=1.0, eid='KSPOS.1958.TL')
ksneg_1958_tl = RBend(l=1.0, eid='KSNEG.1958.TL')
kspos_1960_tl = RBend(l=1.0, eid='KSPOS.1960.TL')
ksneg_1960_tl = RBend(l=1.0, eid='KSNEG.1960.TL')
kspos_1962_tl = RBend(l=1.0, eid='KSPOS.1962.TL')
ksneg_1962_tl = RBend(l=1.0, eid='KSNEG.1962.TL')

# Sextupoles
sa_1674_cl = Sextupole(l=0.3164, k2=17.626614410000002, tilt=1.570796327, eid='SA.1674.CL')
sa_1683_cl = Sextupole(l=0.3164, k2=-14.820280660000002, tilt=1.570796327, eid='SA.1683.CL')
sa_1691_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid='SA.1691.CL')
sa_1692_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid='SA.1692.CL')
sa_1700_cl = Sextupole(l=0.3164, k2=-14.820280660000002, tilt=1.570796327, eid='SA.1700.CL')
sa_1708_cl = Sextupole(l=0.3164, k2=17.626614410000002, tilt=1.570796327, eid='SA.1708.CL')
sa_1710_cl = Sextupole(l=0.3164, k2=17.626614410000002, tilt=1.570796327, eid='SA.1710.CL')
sa_1719_cl = Sextupole(l=0.3164, k2=-14.820280660000002, tilt=1.570796327, eid='SA.1719.CL')
sa_1726_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid='SA.1726.CL')
sa_1728_cl = Sextupole(l=0.3164, k2=2.8569510959987356, tilt=1.570796327, eid='SA.1728.CL')
sa_1736_cl = Sextupole(l=0.3164, k2=-14.820280660000002, tilt=1.570796327, eid='SA.1736.CL')
sa_1744_cl = Sextupole(l=0.3164, k2=17.626614410000002, tilt=1.570796327, eid='SA.1744.CL')
sa_1782_cl = Sextupole(l=0.3164, k2=-17.626614410000002, tilt=1.570796327, eid='SA.1782.CL')
sa_1791_cl = Sextupole(l=0.3164, k2=14.820280660000002, tilt=1.570796327, eid='SA.1791.CL')
sa_1798_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid='SA.1798.CL')
sa_1800_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid='SA.1800.CL')
sa_1808_cl = Sextupole(l=0.3164, k2=14.820280660000002, tilt=1.570796327, eid='SA.1808.CL')
sa_1816_cl = Sextupole(l=0.3164, k2=-17.626614410000002, tilt=1.570796327, eid='SA.1816.CL')
sa_1818_cl = Sextupole(l=0.3164, k2=-17.626614410000002, tilt=1.570796327, eid='SA.1818.CL')
sa_1827_cl = Sextupole(l=0.3164, k2=14.820280660000002, tilt=1.570796327, eid='SA.1827.CL')
sa_1834_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid='SA.1834.CL')
sa_1836_cl = Sextupole(l=0.3164, k2=-2.8569510959987356, tilt=1.570796327, eid='SA.1836.CL')
sa_1844_cl = Sextupole(l=0.3164, k2=14.820280660000002, tilt=1.570796327, eid='SA.1844.CL')
sa_1852_cl = Sextupole(l=0.3164, k2=-17.626614410000002, tilt=1.570796327, eid='SA.1852.CL')

# Hcors
cfx_1660_cl = Hcor(l=0.1, eid='CFX.1660.CL')
chx_1672_cl = Hcor(l=0.2, eid='CHX.1672.CL')
cfx_1683_cl = Hcor(l=0.1, eid='CFX.1683.CL')
cfx_1701_cl = Hcor(l=0.1, eid='CFX.1701.CL')
cfx_1719_cl = Hcor(l=0.1, eid='CFX.1719.CL')
cfx_1737_cl = Hcor(l=0.1, eid='CFX.1737.CL')
chx_1747_cl = Hcor(l=0.2, eid='CHX.1747.CL')
cfx_1755_cl = Hcor(l=0.1, eid='CFX.1755.CL')
cfx_1764_cl = Hcor(l=0.1, eid='CFX.1764.CL')
cfx_1773_cl = Hcor(l=0.1, eid='CFX.1773.CL')
chx_1780_cl = Hcor(l=0.2, eid='CHX.1780.CL')
cfx_1791_cl = Hcor(l=0.1, eid='CFX.1791.CL')
cfx_1809_cl = Hcor(l=0.1, eid='CFX.1809.CL')
cfx_1827_cl = Hcor(l=0.1, eid='CFX.1827.CL')
cfx_1845_cl = Hcor(l=0.1, eid='CFX.1845.CL')
chx_1855_tl = Hcor(l=0.2, eid='CHX.1855.TL')
cfx_1864_tl = Hcor(l=0.1, eid='CFX.1864.TL')
cfx_1873_tl = Hcor(l=0.1, eid='CFX.1873.TL')
cfx_1894_tl = Hcor(l=0.1, eid='CFX.1894.TL')
cfx_1925_tl = Hcor(l=0.1, eid='CFX.1925.TL')
bl_1939_tl = Hcor(l=0.2, eid='BL.1939.TL')
bl_1964_tl = Hcor(l=0.2, eid='BL.1964.TL')
chx_1965_tl = Hcor(l=0.2, eid='CHX.1965.TL')
chx_1967_tl = Hcor(l=0.2, eid='CHX.1967.TL')
cnx_1977_tl = Hcor(l=0.3, eid='CNX.1977.TL')

# Vcors
chy_1667_cl = Vcor(l=0.2, eid='CHY.1667.CL')
cfy_1674_cl = Vcor(l=0.1, eid='CFY.1674.CL')
cfy_1692_cl = Vcor(l=0.1, eid='CFY.1692.CL')
cfy_1710_cl = Vcor(l=0.1, eid='CFY.1710.CL')
cfy_1728_cl = Vcor(l=0.1, eid='CFY.1728.CL')
cfy_1746_cl = Vcor(l=0.1, eid='CFY.1746.CL')
chy_1753_cl = Vcor(l=0.2, eid='CHY.1753.CL')
cfy_1760_cl = Vcor(l=0.1, eid='CFY.1760.CL')
cfy_1768_cl = Vcor(l=0.1, eid='CFY.1768.CL')
chy_1774_cl = Vcor(l=0.2, eid='CHY.1774.CL')
cfy_1782_cl = Vcor(l=0.1, eid='CFY.1782.CL')
cfy_1800_cl = Vcor(l=0.1, eid='CFY.1800.CL')
cfy_1818_cl = Vcor(l=0.1, eid='CFY.1818.CL')
cfy_1836_cl = Vcor(l=0.1, eid='CFY.1836.CL')
cfy_1854_tl = Vcor(l=0.1, eid='CFY.1854.TL')
chy_1861_tl = Vcor(l=0.2, eid='CHY.1861.TL')
cfy_1869_tl = Vcor(l=0.1, eid='CFY.1869.TL')
cfy_1884_tl = Vcor(l=0.1, eid='CFY.1884.TL')
cfy_1910_tl = Vcor(l=0.1, eid='CFY.1910.TL')
cfy_1937_tl = Vcor(l=0.1, eid='CFY.1937.TL')
chy_1967_tl = Vcor(l=0.2, eid='CHY.1967.TL')
cny_1977_tl = Vcor(l=0.3, eid='CNY.1977.TL')

# Monitors
bpma_1659_cl = Monitor(eid='BPMA.1659.CL')
bpma_1669_cl = Monitor(eid='BPMA.1669.CL')
bpmi_1675_cl = Monitor(eid='BPMI.1675.CL')
bpma_1684_cl = Monitor(eid='BPMA.1684.CL')
bpmi_1693_cl = Monitor(eid='BPMI.1693.CL')
bpma_1702_cl = Monitor(eid='BPMA.1702.CL')
bpma_1711_cl = Monitor(eid='BPMA.1711.CL')
bpma_1720_cl = Monitor(eid='BPMA.1720.CL')
bpmi_1729_cl = Monitor(eid='BPMI.1729.CL')
bpma_1738_cl = Monitor(eid='BPMA.1738.CL')
bpma_1746_cl = Monitor(eid='BPMA.1746.CL')
bpma_1750_cl = Monitor(eid='BPMA.1750.CL')
bpma_1756_cl = Monitor(eid='BPMA.1756.CL')
bpma_1761_cl = Monitor(eid='BPMA.1761.CL')
bpma_1765_cl = Monitor(eid='BPMA.1765.CL')
bpma_1769_cl = Monitor(eid='BPMA.1769.CL')
bpma_1773_cl = Monitor(eid='BPMA.1773.CL')
bpma_1777_cl = Monitor(eid='BPMA.1777.CL')
bpma_1783_cl = Monitor(eid='BPMA.1783.CL')
bpma_1792_cl = Monitor(eid='BPMA.1792.CL')
bpma_1801_cl = Monitor(eid='BPMA.1801.CL')
bpma_1810_cl = Monitor(eid='BPMA.1810.CL')
bpma_1819_cl = Monitor(eid='BPMA.1819.CL')
bpma_1828_cl = Monitor(eid='BPMA.1828.CL')
bpmi_1837_cl = Monitor(eid='BPMI.1837.CL')
bpma_1846_cl = Monitor(eid='BPMA.1846.CL')
bpma_1853_cl = Monitor(eid='BPMA.1853.CL')
bpmi_1860_tl = Monitor(eid='BPMI.1860.TL')
bpmi_1863_tl = Monitor(eid='BPMI.1863.TL')
bpma_1868_tl = Monitor(eid='BPMA.1868.TL')
bpma_1873_tl = Monitor(eid='BPMA.1873.TL')
bpmi_1878_tl = Monitor(eid='BPMI.1878.TL')
bpmi_1889_tl = Monitor(eid='BPMI.1889.TL')
bpmi_1910_tl = Monitor(eid='BPMI.1910.TL')
bpmi_1925_tl = Monitor(eid='BPMI.1925.TL')
bpmi_1930_tl = Monitor(eid='BPMI.1930.TL')
bpmi_1939_tl = Monitor(eid='BPMI.1939.TL')
bpma_1966_tl = Monitor(eid='BPMA.1966.TL')
bpmd_1977_tl = Monitor(eid='BPMD.1977.TL')

# Markers
match_1673_cl = Marker(eid='MATCH.1673.CL')
ks_1941_tl = Marker(eid='KS.1941.TL')
ks_1943_tl = Marker(eid='KS.1943.TL')
ks_1945_tl = Marker(eid='KS.1945.TL')
ks_1948_tl = Marker(eid='KS.1948.TL')
ks_1950_tl = Marker(eid='KS.1950.TL')
ks_1953_tl = Marker(eid='KS.1953.TL')
ks_1955_tl = Marker(eid='KS.1955.TL')
ks_1958_tl = Marker(eid='KS.1958.TL')
ks_1960_tl = Marker(eid='KS.1960.TL')
ks_1962_tl = Marker(eid='KS.1962.TL')
ensub_1980_tl = Marker(eid='ENSUB.1980.TL')

# Lattice 
cell = (id_15388144_, bpma_1659_cl, d_4, qf_1660_cl, d_5, cfx_1660_cl, d_6, chy_1667_cl, d_7, 
qh_1667_cl, d_8, qh_1669_cl, d_9, bpma_1669_cl, d_10, qh_1670_cl, d_8, qh_1671_cl, d_7, 
chx_1672_cl, d_13, match_1673_cl, qf_1673_cl, d_5, cfy_1674_cl, d_15, sa_1674_cl, id_389319_, bpmi_1675_cl, 
d_18, be_1678_cl, d_19, qf_1682_cl, d_5, cfx_1683_cl, d_15, sa_1683_cl, d_22, bpma_1684_cl, 
d_23, bl_1688_cl, id_50656927_, sa_1691_cl, d_26, qf_1691_cl, d_5, cfy_1692_cl, d_15, sa_1692_cl, 
id_389319_, bpmi_1693_cl, d_31, bl_1695_cl, d_32, sa_1700_cl, d_26, qf_1700_cl, d_5, cfx_1701_cl, 
d_35, bpma_1702_cl, d_36, be_1705_cl, d_37, sa_1708_cl, d_26, qf_1709_cl, d_5, cfy_1710_cl, 
d_15, sa_1710_cl, d_22, bpma_1711_cl, d_42, be_1714_cl, d_19, qf_1718_cl, d_5, cfx_1719_cl, 
d_15, sa_1719_cl, d_22, bpma_1720_cl, d_23, bl_1724_cl, id_50656927_, sa_1726_cl, d_26, qf_1727_cl, 
d_5, cfy_1728_cl, d_15, sa_1728_cl, id_389319_, bpmi_1729_cl, d_31, bl_1731_cl, d_32, sa_1736_cl, 
d_26, qf_1736_cl, d_5, cfx_1737_cl, d_35, bpma_1738_cl, d_36, be_1741_cl, d_37, sa_1744_cl, 
d_26, qf_1745_cl, d_5, cfy_1746_cl, d_64, bpma_1746_cl, d_65, chx_1747_cl, d_7, qh_1748_cl, 
d_8, qh_1749_cl, d_9, bpma_1750_cl, d_10, qh_1751_cl, d_8, qh_1752_cl, d_7, chy_1753_cl, 
d_72, qf_1754_cl, d_5, cfx_1755_cl, d_35, bpma_1756_cl, d_75, qf_1759_cl, d_5, cfy_1760_cl, 
d_35, bpma_1761_cl, d_78, qf_1763_cl, d_5, cfx_1764_cl, d_35, bpma_1765_cl, d_81, qf_1767_cl, 
d_5, cfy_1768_cl, d_35, bpma_1769_cl, d_75, qf_1772_cl, d_5, cfx_1773_cl, d_64, bpma_1773_cl, 
d_87, chy_1774_cl, d_7, qh_1775_cl, d_8, qh_1776_cl, d_9, bpma_1777_cl, d_10, qh_1778_cl, 
d_8, qh_1779_cl, d_7, chx_1780_cl, d_94, qf_1781_cl, d_5, cfy_1782_cl, d_15, sa_1782_cl, 
d_22, bpma_1783_cl, d_42, be_1786_cl, d_19, qf_1790_cl, d_5, cfx_1791_cl, d_15, sa_1791_cl, 
d_22, bpma_1792_cl, d_23, bl_1796_cl, id_50656927_, sa_1798_cl, d_26, qf_1799_cl, d_5, cfy_1800_cl, 
d_15, sa_1800_cl, d_22, bpma_1801_cl, d_110, bl_1803_cl, d_32, sa_1808_cl, d_26, qf_1808_cl, 
d_5, cfx_1809_cl, d_35, bpma_1810_cl, d_36, be_1813_cl, d_37, sa_1816_cl, d_26, qf_1817_cl, 
d_5, cfy_1818_cl, d_15, sa_1818_cl, d_22, bpma_1819_cl, d_42, be_1822_cl, d_19, qf_1826_cl, 
d_5, cfx_1827_cl, d_15, sa_1827_cl, d_22, bpma_1828_cl, d_23, bl_1832_cl, id_50656927_, sa_1834_cl, 
d_26, qf_1835_cl, d_5, cfy_1836_cl, d_15, sa_1836_cl, id_389319_, bpmi_1837_cl, d_31, bl_1839_cl, 
d_32, sa_1844_cl, d_26, qf_1844_cl, d_5, cfx_1845_cl, d_35, bpma_1846_cl, d_36, be_1849_cl, 
d_37, sa_1852_cl, d_141, bpma_1853_cl, d_4, qf_1853_cl, d_5, cfy_1854_tl, d_144, chx_1855_tl, 
d_7, qh_1855_tl, d_8, qh_1857_tl, d_147, qh_1858_tl, d_8, qh_1859_tl, id_22692917_, bpmi_1860_tl, 
d_151, chy_1861_tl, d_152, bpmi_1863_tl, id_75563590_, qf_1864_tl, d_5, cfx_1864_tl, id_11766094_, bpma_1868_tl, 
d_4, qf_1868_tl, d_5, cfy_1869_tl, d_160, bpma_1873_tl, d_4, qf_1873_tl, d_5, cfx_1873_tl, 
id_94527400_, bpmi_1878_tl, d_165, qf_1881_tl, d_166, cfy_1884_tl, id_61704230_, bpmi_1889_tl, d_165, qf_1892_tl, 
d_170, cfx_1894_tl, id_21941902_, qf_1907_tl, id_54090033_, bpmi_1910_tl, d_151, cfy_1910_tl, id_25778097_, qf_1922_tl, 
id_54090033_, bpmi_1925_tl, d_151, cfx_1925_tl, id_78367389_, bpmi_1930_tl, id_69348953_, qf_1937_tl, d_5, cfy_1937_tl, 
id_7559873_, bpmi_1939_tl, d_191, bl_1939_tl, id_5581078_, kspos_1941_tl, ks_1941_tl, ksneg_1941_tl, d_194, kspos_1943_tl, 
ks_1943_tl, ksneg_1943_tl, d_194, kspos_1945_tl, ks_1945_tl, ksneg_1945_tl, d_194, kspos_1948_tl, ks_1948_tl, ksneg_1948_tl, 
d_194, kspos_1950_tl, ks_1950_tl, ksneg_1950_tl, d_198, qf_1952_tl, d_198, kspos_1953_tl, ks_1953_tl, ksneg_1953_tl, 
d_194, kspos_1955_tl, ks_1955_tl, ksneg_1955_tl, d_194, kspos_1958_tl, ks_1958_tl, ksneg_1958_tl, d_194, kspos_1960_tl, 
ks_1960_tl, ksneg_1960_tl, d_194, kspos_1962_tl, ks_1962_tl, ksneg_1962_tl, id_5581078_, bl_1964_tl, d_205, chx_1965_tl, 
d_206, bpma_1966_tl, d_207, qf_1967_tl, d_208, chx_1967_tl, d_209, chy_1967_tl, d_210, cnx_1977_tl, 
d_211, cny_1977_tl, d_212, bpmd_1977_tl, id_63971798_, ensub_1980_tl)

# power supplies 

#  
qf_1660_cl.ps_id = 'QF.3.CL'
qh_1667_cl.ps_id = 'QH.1.CL'
qh_1669_cl.ps_id = 'QH.1.CL'
qh_1670_cl.ps_id = 'QH.2.CL'
qh_1671_cl.ps_id = 'QH.2.CL'
qf_1673_cl.ps_id = 'QF.4.CL'
qf_1682_cl.ps_id = 'QF.4.CL'
qf_1691_cl.ps_id = 'QF.4.CL'
qf_1700_cl.ps_id = 'QF.4.CL'
qf_1709_cl.ps_id = 'QF.4.CL'
qf_1718_cl.ps_id = 'QF.4.CL'
qf_1727_cl.ps_id = 'QF.4.CL'
qf_1736_cl.ps_id = 'QF.4.CL'
qf_1745_cl.ps_id = 'QF.4.CL'
qh_1748_cl.ps_id = 'QH.3.CL'
qh_1749_cl.ps_id = 'QH.3.CL'
qh_1751_cl.ps_id = 'QH.4.CL'
qh_1752_cl.ps_id = 'QH.4.CL'
qf_1754_cl.ps_id = 'QF.5.CL'
qf_1759_cl.ps_id = 'QF.6.CL'
qf_1763_cl.ps_id = 'QF.7.CL'
qf_1767_cl.ps_id = 'QF.6.CL'
qf_1772_cl.ps_id = 'QF.5.CL'
qh_1775_cl.ps_id = 'QH.4.CL'
qh_1776_cl.ps_id = 'QH.4.CL'
qh_1778_cl.ps_id = 'QH.3.CL'
qh_1779_cl.ps_id = 'QH.3.CL'
qf_1781_cl.ps_id = 'QF.4.CL'
qf_1790_cl.ps_id = 'QF.4.CL'
qf_1799_cl.ps_id = 'QF.4.CL'
qf_1808_cl.ps_id = 'QF.4.CL'
qf_1817_cl.ps_id = 'QF.4.CL'
qf_1826_cl.ps_id = 'QF.4.CL'
qf_1835_cl.ps_id = 'QF.4.CL'
qf_1844_cl.ps_id = 'QF.4.CL'
qf_1853_cl.ps_id = 'QF.4.CL'
qh_1855_tl.ps_id = 'QH.5.TL'
qh_1857_tl.ps_id = 'QH.6.TL'
qh_1858_tl.ps_id = 'QH.7.TL'
qh_1859_tl.ps_id = 'QH.8.TL'
qf_1864_tl.ps_id = 'QF.8.TL'
qf_1868_tl.ps_id = 'QF.9.TL'
qf_1873_tl.ps_id = 'QF.10.TL'
qf_1881_tl.ps_id = 'QF.11.TL'
qf_1892_tl.ps_id = 'QF.1.TL'
qf_1907_tl.ps_id = 'QF.2.TL'
qf_1922_tl.ps_id = 'QF.1.TL'
qf_1937_tl.ps_id = 'QF.2.TL'
qf_1952_tl.ps_id = 'QF.1.TL'
qf_1967_tl.ps_id = 'QF.2.TL'

#  
sa_1674_cl.ps_id = 'SA.1.CL'
sa_1683_cl.ps_id = 'SA.2.CL'
sa_1691_cl.ps_id = 'SA.3.CL'
sa_1692_cl.ps_id = 'SA.3.CL'
sa_1700_cl.ps_id = 'SA.2.CL'
sa_1708_cl.ps_id = 'SA.1.CL'
sa_1710_cl.ps_id = 'SA.1.CL'
sa_1719_cl.ps_id = 'SA.2.CL'
sa_1726_cl.ps_id = 'SA.3.CL'
sa_1728_cl.ps_id = 'SA.3.CL'
sa_1736_cl.ps_id = 'SA.2.CL'
sa_1744_cl.ps_id = 'SA.1.CL'
sa_1782_cl.ps_id = 'SA.4.CL'
sa_1791_cl.ps_id = 'SA.5.CL'
sa_1798_cl.ps_id = 'SA.6.CL'
sa_1800_cl.ps_id = 'SA.6.CL'
sa_1808_cl.ps_id = 'SA.5.CL'
sa_1816_cl.ps_id = 'SA.4.CL'
sa_1818_cl.ps_id = 'SA.4.CL'
sa_1827_cl.ps_id = 'SA.5.CL'
sa_1834_cl.ps_id = 'SA.6.CL'
sa_1836_cl.ps_id = 'SA.6.CL'
sa_1844_cl.ps_id = 'SA.5.CL'
sa_1852_cl.ps_id = 'SA.4.CL'

#  

#  

#  
be_1678_cl.ps_id = 'BE.1.CL'
bl_1688_cl.ps_id = 'BL.1.CL'
bl_1695_cl.ps_id = 'BL.1.CL'
be_1705_cl.ps_id = 'BE.1.CL'
be_1714_cl.ps_id = 'BE.1.CL'
bl_1724_cl.ps_id = 'BL.1.CL'
bl_1731_cl.ps_id = 'BL.1.CL'
be_1741_cl.ps_id = 'BE.1.CL'
be_1786_cl.ps_id = 'BE.2.CL'
bl_1796_cl.ps_id = 'BL.2.CL'
bl_1803_cl.ps_id = 'BL.2.CL'
be_1813_cl.ps_id = 'BE.2.CL'
be_1822_cl.ps_id = 'BE.2.CL'
bl_1832_cl.ps_id = 'BL.2.CL'
bl_1839_cl.ps_id = 'BL.2.CL'
be_1849_cl.ps_id = 'BE.2.CL'
kspos_1941_tl.ps_id = 'KSPOS.1941.TL'
ksneg_1941_tl.ps_id = 'KSNEG.1941.TL'
kspos_1943_tl.ps_id = 'KSPOS.1943.TL'
ksneg_1943_tl.ps_id = 'KSNEG.1943.TL'
kspos_1945_tl.ps_id = 'KSPOS.1945.TL'
ksneg_1945_tl.ps_id = 'KSNEG.1945.TL'
kspos_1948_tl.ps_id = 'KSPOS.1948.TL'
ksneg_1948_tl.ps_id = 'KSNEG.1948.TL'
kspos_1950_tl.ps_id = 'KSPOS.1950.TL'
ksneg_1950_tl.ps_id = 'KSNEG.1950.TL'
kspos_1953_tl.ps_id = 'KSPOS.1953.TL'
ksneg_1953_tl.ps_id = 'KSNEG.1953.TL'
kspos_1955_tl.ps_id = 'KSPOS.1955.TL'
ksneg_1955_tl.ps_id = 'KSNEG.1955.TL'
kspos_1958_tl.ps_id = 'KSPOS.1958.TL'
ksneg_1958_tl.ps_id = 'KSNEG.1958.TL'
kspos_1960_tl.ps_id = 'KSPOS.1960.TL'
ksneg_1960_tl.ps_id = 'KSNEG.1960.TL'
kspos_1962_tl.ps_id = 'KSPOS.1962.TL'
ksneg_1962_tl.ps_id = 'KSNEG.1962.TL'