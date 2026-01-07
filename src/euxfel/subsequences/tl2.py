from ocelot import *

twiss0 = Twiss()
twiss0._E = 14.0
twiss0._beta_x = 0.5606
twiss0._beta_y = 2.9599
twiss0._alpha_x = -1.3652
twiss0._alpha_y = 0.1497

# Drifts:
d_0 = Drift(l=0.1539500000001226, eid="D_0")
d_1 = Drift(l=0.6899999999999636, eid="D_1")
d_2 = Drift(l=0.15544999999979153, eid="D_2")
d_3 = Drift(l=0.2209000000000001, eid="D_3")
d_4 = Drift(l=0.5709000000001365, eid="D_4")
d_5 = Drift(l=0.2209000000000001, eid="D_5")
d_6 = Drift(l=0.4129500000001085, eid="D_6")
d_7 = Drift(l=0.09600000000000364, eid="D_7")
d_8 = Drift(l=0.30150000000003274, eid="D_8")
d_9 = Drift(l=2.0864999999999325, eid="D_9")
d_10 = Drift(l=0.09600000000000364, eid="D_10")
d_11 = Drift(l=0.33645000000001346, eid="D_11")
d_12 = Drift(l=0.1539500000000229, eid="D_12")
d_13 = Drift(l=0.9299999999999727, eid="D_13")
d_14 = Drift(l=0.09999999999990905, eid="D_14")
d_15 = Drift(l=2.3250000000000455, eid="D_15")
d_16 = Drift(l=0.20895000000018626, eid="D_16")
d_17 = Drift(l=0.15394999999979553, eid="D_17")
d_18 = Drift(l=3.8550000000001545, eid="D_18")
d_19 = Drift(l=0.2089499999999589, eid="D_19")
d_20 = Drift(l=0.1539500000000229, eid="D_20")
d_21 = Drift(l=4.852499999999873, eid="D_21")
d_22 = Drift(l=0.09600000000000364, eid="D_22")
d_23 = Drift(l=2.61545000000001, eid="D_23")
d_24 = Drift(l=0.23394999999995014, eid="D_24")
d_25 = Drift(l=0.2700000000002092, eid="D_25")
d_26 = Drift(l=4.352499999999873, eid="D_26")
d_27 = Drift(l=0.09600000000000364, eid="D_27")
d_28 = Drift(l=2.61545000000001, eid="D_28")
d_29 = Drift(l=0.23394999999995014, eid="D_29")
d_30 = Drift(l=0.3000000000001819, eid="D_30")
d_31 = Drift(l=4.0999999999998185, eid="D_31")
d_32 = Drift(l=7.73395000000005, eid="D_32")
d_33 = Drift(l=0.23394999999995014, eid="D_33")
d_34 = Drift(l=0.4774999999999636, eid="D_34")
d_35 = Drift(l=0.09600000000000364, eid="D_35")
d_36 = Drift(l=0.30150000000003274, eid="D_36")
d_37 = Drift(l=3.525, eid="D_37")
d_38 = Drift(l=7.73395000000005, eid="D_38")
d_39 = Drift(l=0.23394999999995014, eid="D_39")
d_40 = Drift(l=0.4774999999999636, eid="D_40")
d_41 = Drift(l=0.09600000000000364, eid="D_41")
d_42 = Drift(l=0.30150000000003274, eid="D_42")
d_43 = Drift(l=3.525, eid="D_43")
d_44 = Drift(l=1.2774999999999181, eid="D_44")
d_45 = Drift(l=0.09600000000000364, eid="D_45")
d_46 = Drift(l=1.0715000000000146, eid="D_46")
d_47 = Drift(l=0.3000000000001819, eid="D_47")
d_48 = Drift(l=2.677500000000009, eid="D_48")
d_49 = Drift(l=2.3114499999999225, eid="D_49")
d_50 = Drift(l=0.1539500000000229, eid="D_50")
d_51 = Drift(l=0.29000000000010007, eid="D_51")
d_52 = Drift(l=0.2825000000000236, eid="D_52")
d_53 = Drift(l=0.09600000000000364, eid="D_53")
d_54 = Drift(l=0.4815000000000964, eid="D_54")
d_55 = Drift(l=0.2699999999997999, eid="D_55")
d_56 = Drift(l=0.10000000000013642, eid="D_56")
d_57 = Drift(l=0.31999999999993634, eid="D_57")
d_58 = Drift(l=0.31999999999993634, eid="D_58")
d_59 = Drift(l=0.3200000000001637, eid="D_59")
d_60 = Drift(l=0.31999999999993634, eid="D_60")
d_61 = Drift(l=0.2839510000001155, eid="D_61")
d_62 = Drift(l=0.28395099999978846, eid="D_62")
d_63 = Drift(l=0.3200000000001637, eid="D_63")
d_64 = Drift(l=0.31999999999993634, eid="D_64")
d_65 = Drift(l=0.31999999999993634, eid="D_65")
d_66 = Drift(l=0.31999999999993634, eid="D_66")
d_67 = Drift(l=0.37000000000011823, eid="D_67")
d_68 = Drift(l=0.4100000000001273, eid="D_68")
d_69 = Drift(l=0.22499999999995451, eid="D_69")
d_70 = Drift(l=0.36000000000012367, eid="D_70")
d_71 = Drift(l=0.20895100000007005, eid="D_71")
d_72 = Drift(l=0.1539509999999067, eid="D_72")
d_73 = Drift(l=0.20000000000009094, eid="D_73")
d_74 = Drift(l=9.069199999999729, eid="D_74")
d_75 = Drift(l=0.10000000000009096, eid="D_75")
d_76 = Drift(l=0.15000000000004549, eid="D_76")
d_77 = Drift(l=0.20000000000004547, eid="D_77")
d_78 = Drift(l=1.860740000000078, eid="D_78")

# Quadrupoles:
qh_1855_tl = Quadrupole(l=1.0291, k1=0.3716633416004276, eid="QH.1855.TL")
qh_1857_tl = Quadrupole(l=1.0291, k1=0.34605581209989317, eid="QH.1857.TL")
qh_1858_tl = Quadrupole(l=1.0291, k1=-0.3787301584996599, eid="QH.1858.TL")
qh_1859_tl = Quadrupole(l=1.0291, k1=-0.05277408413953941, eid="QH.1859.TL")
qf_1864_tl = Quadrupole(l=0.5321, k1=0.1858986038996429, eid="QF.1864.TL")
qf_1868_tl = Quadrupole(l=0.5321, k1=-0.05512587120090209, eid="QF.1868.TL")
qf_1873_tl = Quadrupole(l=0.5321, k1=0.1199289291993986, eid="QF.1873.TL")
qf_1881_tl = Quadrupole(l=0.5321, k1=-0.20093471310092087, eid="QF.1881.TL")
qf_1892_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid="QF.1892.TL")
qf_1907_tl = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid="QF.1907.TL")
qf_1922_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid="QF.1922.TL")
qf_1937_tl = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid="QF.1937.TL")
qf_1952_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid="QF.1952.TL")
qf_1967_tl = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid="QF.1967.TL")

# RBends:
kmx_1938_tl = RBend(l=0.651, e1=0.0, e2=0.0, eid="KMX.1938.TL")
kny_1938_tl = RBend(l=0.279, e1=0.0, e2=0.0, tilt=1.570796327, eid="KNY.1938.TL")
kspos_1941_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSPOS.1941.TL")
ksneg_1941_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSNEG.1941.TL")
kspos_1943_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSPOS.1943.TL")
ksneg_1943_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSNEG.1943.TL")
kspos_1945_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSPOS.1945.TL")
ksneg_1945_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSNEG.1945.TL")
kspos_1948_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSPOS.1948.TL")
ksneg_1948_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSNEG.1948.TL")
kspos_1950_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSPOS.1950.TL")
ksneg_1950_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSNEG.1950.TL")
kspos_1953_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSPOS.1953.TL")
ksneg_1953_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSNEG.1953.TL")
kspos_1955_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSPOS.1955.TL")
ksneg_1955_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSNEG.1955.TL")
kspos_1958_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSPOS.1958.TL")
ksneg_1958_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSNEG.1958.TL")
kspos_1960_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSPOS.1960.TL")
ksneg_1960_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSNEG.1960.TL")
kspos_1962_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSPOS.1962.TL")
ksneg_1962_tl = RBend(l=1.0, e1=0.0, e2=0.0, eid="KSNEG.1962.TL")
kmx_1965_tl = RBend(l=0.651, e1=0.0, e2=0.0, eid="KMX.1965.TL")
kny_1966_tl = RBend(l=0.279, e1=0.0, e2=0.0, tilt=1.570796327, eid="KNY.1966.TL")

# Hcors:
chx_1855_tl = Hcor(l=0.2, eid="CHX.1855.TL")
cfx_1864_tl = Hcor(l=0.1, eid="CFX.1864.TL")
cfx_1873_tl = Hcor(l=0.1, eid="CFX.1873.TL")
kfbx_1893_tl = Hcor(l=2.0, eid="KFBX.1893.TL")
cfx_1894_tl = Hcor(l=0.1, eid="CFX.1894.TL")
kfbx_1923_tl = Hcor(l=2.0, eid="KFBX.1923.TL")
cfx_1925_tl = Hcor(l=0.1, eid="CFX.1925.TL")
bl_1939_tl = Hcor(l=0.2, eid="BL.1939.TL")
bl_1964_tl = Hcor(l=0.2, eid="BL.1964.TL")
chx_1965_tl = Hcor(l=0.2, eid="CHX.1965.TL")
chx_1967_tl = Hcor(l=0.2, eid="CHX.1967.TL")
cnx_1977_tl = Hcor(l=0.3, eid="CNX.1977.TL")

# Vcors:
cfy_1854_tl = Vcor(l=0.1, eid="CFY.1854.TL")
chy_1861_tl = Vcor(l=0.2, eid="CHY.1861.TL")
cfy_1869_tl = Vcor(l=0.1, eid="CFY.1869.TL")
kfby_1883_tl = Vcor(l=2.0, eid="KFBY.1883.TL")
cfy_1884_tl = Vcor(l=0.1, eid="CFY.1884.TL")
kfby_1908_tl = Vcor(l=2.0, eid="KFBY.1908.TL")
cfy_1910_tl = Vcor(l=0.1, eid="CFY.1910.TL")
cfy_1937_tl = Vcor(l=0.1, eid="CFY.1937.TL")
chy_1967_tl = Vcor(l=0.2, eid="CHY.1967.TL")
cny_1977_tl = Vcor(l=0.3, eid="CNY.1977.TL")

# Monitors:
bpmi_1860_tl = Monitor(eid="BPMI.1860.TL")
bpmi_1863_tl = Monitor(eid="BPMI.1863.TL")
bpma_1868_tl = Monitor(eid="BPMA.1868.TL")
bpma_1873_tl = Monitor(eid="BPMA.1873.TL")
bpmi_1878_tl = Monitor(eid="BPMI.1878.TL")
bpmi_1889_tl = Monitor(eid="BPMI.1889.TL")
bpmi_1910_tl = Monitor(eid="BPMI.1910.TL")
bpmi_1925_tl = Monitor(eid="BPMI.1925.TL")
bpmi_1930_tl = Monitor(eid="BPMI.1930.TL")
bpmi_1939_tl = Monitor(eid="BPMI.1939.TL")
bpma_1966_tl = Monitor(eid="BPMA.1966.TL")
bpmd_1977_tl = Monitor(eid="BPMD.1977.TL")

# Markers:
stsec_1854_tl = Marker(eid="STSEC.1854.TL")
stsub_1854_tl = Marker(eid="STSUB.1854.TL")
midbpmi_1860_tl = Marker(eid="MIDBPMI.1860.TL")
midbpmi_1863_tl = Marker(eid="MIDBPMI.1863.TL")
tora_1865_tl = Marker(eid="TORA.1865.TL")
dcm_1865_tl = Marker(eid="DCM.1865.TL")
midbpmi_1878_tl = Marker(eid="MIDBPMI.1878.TL")
midbpmi_1889_tl = Marker(eid="MIDBPMI.1889.TL")
enblock_1891_cl = Marker(eid="ENBLOCK.1891.CL")
otrbw_1899_tl = Marker(eid="OTRBW.1899.TL")
midbpmi_1910_tl = Marker(eid="MIDBPMI.1910.TL")
otrbw_1914_tl = Marker(eid="OTRBW.1914.TL")
midbpmi_1925_tl = Marker(eid="MIDBPMI.1925.TL")
otrbw_1929_tl = Marker(eid="OTRBW.1929.TL")
midbpmi_1930_tl = Marker(eid="MIDBPMI.1930.TL")
bam_1931_tl = Marker(eid="BAM.1931.TL")
bam_1932_tl = Marker(eid="BAM.1932.TL")
crd_1934_tl = Marker(eid="CRD.1934.TL")
midbpmi_1939_tl = Marker(eid="MIDBPMI.1939.TL")
ensub_1940_tl = Marker(eid="ENSUB.1940.TL")
stsub_1940_tl = Marker(eid="STSUB.1940.TL")
ks_1941_tl = Marker(eid="KS.1941.TL")
ks_1943_tl = Marker(eid="KS.1943.TL")
ks_1945_tl = Marker(eid="KS.1945.TL")
ks_1948_tl = Marker(eid="KS.1948.TL")
ks_1950_tl = Marker(eid="KS.1950.TL")
ks_1953_tl = Marker(eid="KS.1953.TL")
ks_1955_tl = Marker(eid="KS.1955.TL")
ks_1958_tl = Marker(eid="KS.1958.TL")
ks_1960_tl = Marker(eid="KS.1960.TL")
ks_1962_tl = Marker(eid="KS.1962.TL")
otre_1978_tl = Marker(eid="OTRE.1978.TL")
ensub_1980_tl = Marker(eid="ENSUB.1980.TL")

# Sequence:
cell = (stsec_1854_tl,
        stsub_1854_tl,
        d_0,
        cfy_1854_tl,
        d_1,
        chx_1855_tl,
        d_2,
        qh_1855_tl,
        d_3,
        qh_1857_tl,
        d_4,
        qh_1858_tl,
        d_5,
        qh_1859_tl,
        d_6,
        midbpmi_1860_tl,
        d_7,
        bpmi_1860_tl,
        d_8,
        chy_1861_tl,
        d_9,
        bpmi_1863_tl,
        d_10,
        midbpmi_1863_tl,
        d_11,
        qf_1864_tl,
        d_12,
        cfx_1864_tl,
        d_13,
        tora_1865_tl,
        d_14,
        dcm_1865_tl,
        d_15,
        bpma_1868_tl,
        d_16,
        qf_1868_tl,
        d_17,
        cfy_1869_tl,
        d_18,
        bpma_1873_tl,
        d_19,
        qf_1873_tl,
        d_20,
        cfx_1873_tl,
        d_21,
        midbpmi_1878_tl,
        d_22,
        bpmi_1878_tl,
        d_23,
        qf_1881_tl,
        d_24,
        kfby_1883_tl,
        d_25,
        cfy_1884_tl,
        d_26,
        midbpmi_1889_tl,
        d_27,
        bpmi_1889_tl,
        d_28,
        enblock_1891_cl,
        qf_1892_tl,
        d_29,
        kfbx_1893_tl,
        d_30,
        cfx_1894_tl,
        d_31,
        otrbw_1899_tl,
        d_32,
        qf_1907_tl,
        d_33,
        kfby_1908_tl,
        d_34,
        midbpmi_1910_tl,
        d_35,
        bpmi_1910_tl,
        d_36,
        cfy_1910_tl,
        d_37,
        otrbw_1914_tl,
        d_38,
        qf_1922_tl,
        d_39,
        kfbx_1923_tl,
        d_40,
        midbpmi_1925_tl,
        d_41,
        bpmi_1925_tl,
        d_42,
        cfx_1925_tl,
        d_43,
        otrbw_1929_tl,
        d_44,
        midbpmi_1930_tl,
        d_45,
        bpmi_1930_tl,
        d_46,
        bam_1931_tl,
        d_47,
        bam_1932_tl,
        d_48,
        crd_1934_tl,
        d_49,
        qf_1937_tl,
        d_50,
        cfy_1937_tl,
        d_51,
        kmx_1938_tl,
        kny_1938_tl,
        d_52,
        midbpmi_1939_tl,
        d_53,
        bpmi_1939_tl,
        d_54,
        bl_1939_tl,
        d_55,
        ensub_1940_tl,
        stsub_1940_tl,
        d_56,
        kspos_1941_tl,
        ks_1941_tl,
        ksneg_1941_tl,
        d_57,
        kspos_1943_tl,
        ks_1943_tl,
        ksneg_1943_tl,
        d_58,
        kspos_1945_tl,
        ks_1945_tl,
        ksneg_1945_tl,
        d_59,
        kspos_1948_tl,
        ks_1948_tl,
        ksneg_1948_tl,
        d_60,
        kspos_1950_tl,
        ks_1950_tl,
        ksneg_1950_tl,
        d_61,
        qf_1952_tl,
        d_62,
        kspos_1953_tl,
        ks_1953_tl,
        ksneg_1953_tl,
        d_63,
        kspos_1955_tl,
        ks_1955_tl,
        ksneg_1955_tl,
        d_64,
        kspos_1958_tl,
        ks_1958_tl,
        ksneg_1958_tl,
        d_65,
        kspos_1960_tl,
        ks_1960_tl,
        ksneg_1960_tl,
        d_66,
        kspos_1962_tl,
        ks_1962_tl,
        ksneg_1962_tl,
        d_67,
        bl_1964_tl,
        d_68,
        chx_1965_tl,
        d_69,
        kmx_1965_tl,
        kny_1966_tl,
        d_70,
        bpma_1966_tl,
        d_71,
        qf_1967_tl,
        d_72,
        chx_1967_tl,
        d_73,
        chy_1967_tl,
        d_74,
        cnx_1977_tl,
        d_75,
        cny_1977_tl,
        d_76,
        bpmd_1977_tl,
        d_77,
        otre_1978_tl,
        d_78,
        ensub_1980_tl)

# Power Supply IDs:
