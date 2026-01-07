from ocelot import *

twiss0 = Twiss()
twiss0._E = 14.0
twiss0._beta_x = 0.5606
twiss0._beta_y = 2.9601
twiss0._alpha_x = -1.3653
twiss0._alpha_y = 0.1496

# Drifts:
d_1846 = Drift(l=0.1539500000001226, eid="D_1846")
d_1847 = Drift(l=0.6899999999999636, eid="D_1847")
d_1848 = Drift(l=0.15544999999979153, eid="D_1848")
d_1849 = Drift(l=0.2209000000000001, eid="D_1849")
d_1850 = Drift(l=0.5709000000001365, eid="D_1850")
d_1851 = Drift(l=0.2209000000000001, eid="D_1851")
d_1852 = Drift(l=0.4129500000001085, eid="D_1852")
d_1853 = Drift(l=0.09600000000000364, eid="D_1853")
d_1854 = Drift(l=0.30150000000003274, eid="D_1854")
d_1855 = Drift(l=2.0864999999999325, eid="D_1855")
d_1856 = Drift(l=0.09600000000000364, eid="D_1856")
d_1857 = Drift(l=0.33645000000001346, eid="D_1857")
d_1858 = Drift(l=0.1539500000000229, eid="D_1858")
d_1859 = Drift(l=0.9299999999999727, eid="D_1859")
d_1860 = Drift(l=0.09999999999990905, eid="D_1860")
d_1861 = Drift(l=2.3250000000000455, eid="D_1861")
d_1862 = Drift(l=0.20895000000018626, eid="D_1862")
d_1863 = Drift(l=0.15394999999979553, eid="D_1863")
d_1864 = Drift(l=3.8550000000001545, eid="D_1864")
d_1865 = Drift(l=0.2089499999999589, eid="D_1865")
d_1866 = Drift(l=0.1539500000000229, eid="D_1866")
d_1867 = Drift(l=4.852499999999873, eid="D_1867")
d_1868 = Drift(l=0.09600000000000364, eid="D_1868")
d_1869 = Drift(l=0.38149999999996, eid="D_1869")
kfb0_1880_tl = Drift(l=2.0, eid="KFB0.1880.TL")
d_1870 = Drift(l=0.23395000000004984, eid="D_1870")
d_1871 = Drift(l=0.23394999999995014, eid="D_1871")
d_1872 = Drift(l=0.2700000000002092, eid="D_1872")
d_1873 = Drift(l=4.352499999999873, eid="D_1873")
d_1874 = Drift(l=0.09600000000000364, eid="D_1874")
d_1875 = Drift(l=0.38149999999996, eid="D_1875")
kfb0_1890_tl = Drift(l=2.0, eid="KFB0.1890.TL")
d_1876 = Drift(l=0.23395000000004984, eid="D_1876")
d_1877 = Drift(l=0.23394999999995014, eid="D_1877")
d_1878 = Drift(l=0.3000000000001819, eid="D_1878")
d_1879 = Drift(l=4.0999999999998185, eid="D_1879")
d_1880 = Drift(l=5.5, eid="D_1880")
kfb0_1905_tl = Drift(l=2.0, eid="KFB0.1905.TL")
d_1881 = Drift(l=0.23395000000004984, eid="D_1881")
d_1882 = Drift(l=0.23394999999995014, eid="D_1882")
d_1883 = Drift(l=0.4774999999999636, eid="D_1883")
d_1884 = Drift(l=0.09600000000000364, eid="D_1884")
d_1885 = Drift(l=0.30150000000003274, eid="D_1885")
d_1886 = Drift(l=3.525, eid="D_1886")
d_1887 = Drift(l=5.5, eid="D_1887")
kfb0_1920_tl = Drift(l=2.0, eid="KFB0.1920.TL")
d_1888 = Drift(l=0.23395000000004984, eid="D_1888")
d_1889 = Drift(l=0.23394999999995014, eid="D_1889")
d_1890 = Drift(l=0.4774999999999636, eid="D_1890")
d_1891 = Drift(l=0.09600000000000364, eid="D_1891")
d_1892 = Drift(l=0.30150000000003274, eid="D_1892")
d_1893 = Drift(l=3.525, eid="D_1893")
d_1894 = Drift(l=1.2774999999999181, eid="D_1894")
d_1895 = Drift(l=0.09600000000000364, eid="D_1895")
d_1896 = Drift(l=1.0715000000000146, eid="D_1896")
d_1897 = Drift(l=0.3000000000001819, eid="D_1897")
d_1898 = Drift(l=2.677500000000009, eid="D_1898")
d_1899 = Drift(l=2.3114499999999225, eid="D_1899")
d_1900 = Drift(l=0.1539500000000229, eid="D_1900")
d_1901 = Drift(l=0.29000000000010007, eid="D_1901")
d_1902 = Drift(l=0.2825000000000236, eid="D_1902")
d_1903 = Drift(l=0.09600000000000364, eid="D_1903")
d_1904 = Drift(l=0.4815000000000964, eid="D_1904")
d_1905 = Drift(l=0.2699999999997999, eid="D_1905")

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

# RBends:
kmx_1938_tl = RBend(l=0.651, e1=0.0, e2=0.0, eid="KMX.1938.TL")
kny_1938_tl = RBend(l=0.279, e1=0.0, e2=0.0, tilt=1.570796327, eid="KNY.1938.TL")

# Hcors:
chx_1855_tl = Hcor(l=0.2, eid="CHX.1855.TL")
cfx_1864_tl = Hcor(l=0.1, eid="CFX.1864.TL")
cfx_1873_tl = Hcor(l=0.1, eid="CFX.1873.TL")
kfbx_1893_tl = Hcor(l=2.0, eid="KFBX.1893.TL")
cfx_1894_tl = Hcor(l=0.1, eid="CFX.1894.TL")
kfbx_1923_tl = Hcor(l=2.0, eid="KFBX.1923.TL")
cfx_1925_tl = Hcor(l=0.1, eid="CFX.1925.TL")
bl_1939_tl = Hcor(l=0.2, eid="BL.1939.TL")

# Vcors:
cfy_1854_tl = Vcor(l=0.1, eid="CFY.1854.TL")
chy_1861_tl = Vcor(l=0.2, eid="CHY.1861.TL")
cfy_1869_tl = Vcor(l=0.1, eid="CFY.1869.TL")
kfby_1883_tl = Vcor(l=2.0, eid="KFBY.1883.TL")
cfy_1884_tl = Vcor(l=0.1, eid="CFY.1884.TL")
kfby_1908_tl = Vcor(l=2.0, eid="KFBY.1908.TL")
cfy_1910_tl = Vcor(l=0.1, eid="CFY.1910.TL")
cfy_1937_tl = Vcor(l=0.1, eid="CFY.1937.TL")

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

# Sequence:
cell = (stsec_1854_tl,
        stsub_1854_tl,
        d_1846,
        cfy_1854_tl,
        d_1847,
        chx_1855_tl,
        d_1848,
        qh_1855_tl,
        d_1849,
        qh_1857_tl,
        d_1850,
        qh_1858_tl,
        d_1851,
        qh_1859_tl,
        d_1852,
        midbpmi_1860_tl,
        d_1853,
        bpmi_1860_tl,
        d_1854,
        chy_1861_tl,
        d_1855,
        bpmi_1863_tl,
        d_1856,
        midbpmi_1863_tl,
        d_1857,
        qf_1864_tl,
        d_1858,
        cfx_1864_tl,
        d_1859,
        tora_1865_tl,
        d_1860,
        dcm_1865_tl,
        d_1861,
        bpma_1868_tl,
        d_1862,
        qf_1868_tl,
        d_1863,
        cfy_1869_tl,
        d_1864,
        bpma_1873_tl,
        d_1865,
        qf_1873_tl,
        d_1866,
        cfx_1873_tl,
        d_1867,
        midbpmi_1878_tl,
        d_1868,
        bpmi_1878_tl,
        d_1869,
        kfb0_1880_tl,
        d_1870,
        qf_1881_tl,
        d_1871,
        kfby_1883_tl,
        d_1872,
        cfy_1884_tl,
        d_1873,
        midbpmi_1889_tl,
        d_1874,
        bpmi_1889_tl,
        d_1875,
        kfb0_1890_tl,
        d_1876,
        enblock_1891_cl,
        qf_1892_tl,
        d_1877,
        kfbx_1893_tl,
        d_1878,
        cfx_1894_tl,
        d_1879,
        otrbw_1899_tl,
        d_1880,
        kfb0_1905_tl,
        d_1881,
        qf_1907_tl,
        d_1882,
        kfby_1908_tl,
        d_1883,
        midbpmi_1910_tl,
        d_1884,
        bpmi_1910_tl,
        d_1885,
        cfy_1910_tl,
        d_1886,
        otrbw_1914_tl,
        d_1887,
        kfb0_1920_tl,
        d_1888,
        qf_1922_tl,
        d_1889,
        kfbx_1923_tl,
        d_1890,
        midbpmi_1925_tl,
        d_1891,
        bpmi_1925_tl,
        d_1892,
        cfx_1925_tl,
        d_1893,
        otrbw_1929_tl,
        d_1894,
        midbpmi_1930_tl,
        d_1895,
        bpmi_1930_tl,
        d_1896,
        bam_1931_tl,
        d_1897,
        bam_1932_tl,
        d_1898,
        crd_1934_tl,
        d_1899,
        qf_1937_tl,
        d_1900,
        cfy_1937_tl,
        d_1901,
        kmx_1938_tl,
        kny_1938_tl,
        d_1902,
        midbpmi_1939_tl,
        d_1903,
        bpmi_1939_tl,
        d_1904,
        bl_1939_tl,
        d_1905)

# Power Supply IDs:
