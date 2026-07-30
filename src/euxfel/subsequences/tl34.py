# Converted from component_list_2026.02.13.xls

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import Drift, Hcor, Marker, Monitor, Quadrupole, RBend, Vcor

twiss0 = Twiss()
twiss0.E = 14.0000000004506
twiss0.alpha_x = -2.1712558193719076
twiss0.alpha_y = 0.6889692560430991
twiss0.beta_x = 42.40098969962086
twiss0.beta_y = 10.94378883028304
twiss0.s = 1957.1856990000008


# fmt: off
# Drifts:
d_0 = Drift(l=1.4724009999999907, eid="D_0")
d_1 = Drift(l=13.047400999999823, eid="D_1")
d_2 = Drift(l=1.1589500000002317, eid="D_2")
d_3 = Drift(l=0.1539500000000229, eid="D_3")
d_4 = Drift(l=0.16000000000008185, eid="D_4")
d_5 = Drift(l=0.06999999999999995, eid="D_5")
d_6 = Drift(l=0.06999999999999995, eid="D_6")
d_7 = Drift(l=0.28000000000003633, eid="D_7")
d_8 = Drift(l=0.06999999999999995, eid="D_8")
d_9 = Drift(l=0.06999999999999995, eid="D_9")
d_10 = Drift(l=0.20499999999999086, eid="D_10")
d_11 = Drift(l=0.18999999999987266, eid="D_11")
d_12 = Drift(l=0.5200000000000454, eid="D_12")
d_13 = Drift(l=3.930000000000127, eid="D_13")
d_14 = Drift(l=0.44569999999989707, eid="D_14")
d_15 = Drift(l=0.15429999999992106, eid="D_15")
d_16 = Drift(l=0.20895100000007005, eid="D_16")
d_17 = Drift(l=0.15395100000013406, eid="D_17")
d_18 = Drift(l=0.19999999999986356, eid="D_18")
d_19 = Drift(l=1.4800000000000637, eid="D_19")
d_20 = Drift(l=6.304699999999912, eid="D_20")
d_21 = Drift(l=0.09999999999986359, eid="D_21")
d_22 = Drift(l=1.4347000000002026, eid="D_22")
d_23 = Drift(l=0.1999999999998181, eid="D_23")
d_24 = Drift(l=0.15000000000009095, eid="D_24")
vcv100_2023_tl = Drift(l=0.085, eid="VCV100.2023.TL")
d_25 = Drift(l=0.5857000000001245, eid="D_25")
vcb100_2024_tl = Drift(l=0.18, eid="VCB100.2024.TL")
vcabsa_2024_tl = Drift(l=0.61, eid="VCABSA.2024.TL")
d_26 = Drift(l=0.25002000000007685, eid="D_26")

# Quadrupoles:
qk_1982_tl = Quadrupole(l=1.0552, k1=0.09035960007960576, eid="QK.1982.TL")
qf_1997_tl = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid="QF.1997.TL")
qf_2012_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid="QF.2012.TL")

# RBends:
kl_1998_tl = RBend(l=0.93, e1=0.0, e2=0.0, tilt=1.570796327, eid="KL.1998.TL")
kl_1999_tl = RBend(l=0.93, e1=0.0, e2=0.0, tilt=1.570796327, eid="KL.1999.TL")
kl_2000_tl = RBend(l=0.93, e1=0.0, e2=0.0, tilt=1.570796327, eid="KL.2000.TL")
kl_2001_tl = RBend(l=0.93, e1=0.0, e2=0.0, tilt=1.570796327, eid="KL.2001.TL")
kl_2002_tl = RBend(l=0.93, e1=0.0, e2=0.0, tilt=1.570796327, eid="KL.2002.TL")
kl_2003_tl = RBend(l=0.93, e1=0.0, e2=0.0, tilt=1.570796327, eid="KL.2003.TL")
kl_2005_tl = RBend(l=0.93, e1=0.0, e2=0.0, eid="KL.2005.TL")
kl_2006_tl = RBend(l=0.93, e1=0.0, e2=0.0, eid="KL.2006.TL")

# Hcors:
chx_2012_tl = Hcor(l=0.2, eid="CHX.2012.TL")
cnx_2021_tl = Hcor(l=0.3, eid="CNX.2021.TL")

# Vcors:
chy_1997_tl = Vcor(l=0.2, eid="CHY.1997.TL")
chy_2004_tl = Vcor(l=0.2, eid="CHY.2004.TL")
cfy_2010_tl = Vcor(l=0.1, eid="CFY.2010.TL")
chy_2012_tl = Vcor(l=0.2, eid="CHY.2012.TL")
cny_2021_tl = Vcor(l=0.3, eid="CNY.2021.TL")

# Monitors:
bpma_1995_tl = Monitor(eid="BPMA.1995.TL")
bpma_2011_tl = Monitor(eid="BPMA.2011.TL")
bpmd_2022_tl = Monitor(eid="BPMD.2022.TL")

# Markers:
stsub_1980_tl = Marker(eid="STSUB.1980.TL")
vcst98t40_1980_tl = Marker(eid="VCST98T40.1980.TL")
ensub_1997_tl = Marker(eid="ENSUB.1997.TL")
stsub_1997_tl = Marker(eid="STSUB.1997.TL")
tora_2011_tl = Marker(eid="TORA.2011.TL")
vcst40t98_2014_tl = Marker(eid="VCST40T98.2014.TL")
otre_2023_tl = Marker(eid="OTRE.2023.TL")
ensub_2025_tl = Marker(eid="ENSUB.2025.TL")
# fmt: on

# Sequence:
cell = (
    stsub_1980_tl,
    vcst98t40_1980_tl,
    d_0,
    qk_1982_tl,
    d_1,
    bpma_1995_tl,
    d_2,
    qf_1997_tl,
    d_3,
    chy_1997_tl,
    ensub_1997_tl,
    stsub_1997_tl,
    d_4,
    kl_1998_tl,
    d_5,
    kl_1999_tl,
    d_6,
    kl_2000_tl,
    d_7,
    kl_2001_tl,
    d_8,
    kl_2002_tl,
    d_9,
    kl_2003_tl,
    d_10,
    chy_2004_tl,
    d_11,
    kl_2005_tl,
    d_12,
    kl_2006_tl,
    d_13,
    cfy_2010_tl,
    d_14,
    tora_2011_tl,
    d_15,
    bpma_2011_tl,
    d_16,
    qf_2012_tl,
    d_17,
    chx_2012_tl,
    d_18,
    chy_2012_tl,
    d_19,
    vcst40t98_2014_tl,
    d_20,
    cnx_2021_tl,
    d_21,
    cny_2021_tl,
    d_22,
    bpmd_2022_tl,
    d_23,
    otre_2023_tl,
    d_24,
    vcv100_2023_tl,
    d_25,
    vcb100_2024_tl,
    vcabsa_2024_tl,
    d_26,
    ensub_2025_tl,
)

# Power Supply IDs:
# Drift power supplies:
vcv100_2023_tl.ps_id = "VCV100.TL"
vcb100_2024_tl.ps_id = "VCB100.TL"
vcabsa_2024_tl.ps_id = "VCABSA.TL"

# Quadrupole power supplies:
qk_1982_tl.ps_id = "QK.1.TL"
qf_1997_tl.ps_id = "QF.2.TL"
qf_2012_tl.ps_id = "QF.1.TL"

# RBend power supplies:
kl_1998_tl.ps_id = "KL.1998.TL"
kl_1999_tl.ps_id = "KL.1999.TL"
kl_2000_tl.ps_id = "KL.2000.TL"
kl_2001_tl.ps_id = "KL.2001.TL"
kl_2002_tl.ps_id = "KL.2002.TL"
kl_2003_tl.ps_id = "KL.2003.TL"
kl_2005_tl.ps_id = "KL.2005.TL"
kl_2006_tl.ps_id = "KL.2006.TL"

# Hcor power supplies:
chx_2012_tl.ps_id = "CHX.8.TL"
cnx_2021_tl.ps_id = "CNX.2.TL"

# Vcor power supplies:
chy_1997_tl.ps_id = "CHY.11.TL"
chy_2004_tl.ps_id = "CHY.12.TL"
cfy_2010_tl.ps_id = "CFY.7.TL"
chy_2012_tl.ps_id = "CHY.13.TL"
cny_2021_tl.ps_id = "CNY.3.TL"

# Monitor power supplies:
bpma_1995_tl.ps_id = "BPMA.TL"
bpma_2011_tl.ps_id = "BPMA.TL"
bpmd_2022_tl.ps_id = "BPMD.TL"

# Marker power supplies:
stsub_1980_tl.ps_id = "STSUB.TL3.TL"
vcst98t40_1980_tl.ps_id = "VCST98T40.TL"
ensub_1997_tl.ps_id = "ENSUB.TL3.TL"
stsub_1997_tl.ps_id = "STSUB.TL4.TL"
tora_2011_tl.ps_id = "TORA.TL"
vcst40t98_2014_tl.ps_id = "VCST40T98.TL"
otre_2023_tl.ps_id = "OTRE.TL"
ensub_2025_tl.ps_id = "ENSUB.TL4.TL"

# Component list metadata:
# fmt: off
# Drift metadata:
vcv100_2023_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'VACUUM', 'class': 'VAC', 'type': 'VCV100', 'xaper': 0.098, 'yaper': 0.098}
vcb100_2024_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'VACUUM', 'class': 'VAC', 'type': 'VCB100', 'xaper': 0.098, 'yaper': 0.098}
vcabsa_2024_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'VACUUM', 'class': 'VAC', 'type': 'VCABSA', 'xaper': 0.098, 'yaper': 0.098}

# Quadrupole metadata:
qk_1982_tl.metadata = {'section': 'TL', 'subsection': 'TL3', 'cad_room': 'XTL_037', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QK', 'xaper': 0.04, 'yaper': 0.04}
qf_1997_tl.metadata = {'section': 'TL', 'subsection': 'TL3', 'cad_room': 'XTL_037', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_2012_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}

# RBend metadata:
kl_1998_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_037', 'group': 'FASTKICK', 'class': 'RBEN', 'type': 'KL', 'xaper': 0.04, 'yaper': 0.04}
kl_1999_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_037', 'group': 'FASTKICK', 'class': 'RBEN', 'type': 'KL', 'xaper': 0.04, 'yaper': 0.04}
kl_2000_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_037', 'group': 'FASTKICK', 'class': 'RBEN', 'type': 'KL', 'xaper': 0.04, 'yaper': 0.04}
kl_2001_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_037', 'group': 'FASTKICK', 'class': 'RBEN', 'type': 'KL', 'xaper': 0.04, 'yaper': 0.04}
kl_2002_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_037', 'group': 'FASTKICK', 'class': 'RBEN', 'type': 'KL', 'xaper': 0.04, 'yaper': 0.04}
kl_2003_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_037', 'group': 'FASTKICK', 'class': 'RBEN', 'type': 'KL', 'xaper': 0.04, 'yaper': 0.04}
kl_2005_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_037', 'group': 'RAMPKICK', 'class': 'RBEN', 'type': 'KL', 'xaper': 0.04, 'yaper': 0.04}
kl_2006_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'FASTKICK', 'class': 'RBEN', 'type': 'KL', 'xaper': 0.04, 'yaper': 0.04}

# Hcor metadata:
chx_2012_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CHX', 'xaper': 0.04, 'yaper': 0.04}
cnx_2021_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CNX', 'xaper': 0.098, 'yaper': 0.098}

# Vcor metadata:
chy_1997_tl.metadata = {'section': 'TL', 'subsection': 'TL3', 'cad_room': 'XTL_037', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CHY', 'xaper': 0.04, 'yaper': 0.04}
chy_2004_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_037', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CHY', 'xaper': 0.04, 'yaper': 0.04}
cfy_2010_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
chy_2012_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CHY', 'xaper': 0.04, 'yaper': 0.04}
cny_2021_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CNY', 'xaper': 0.098, 'yaper': 0.098}

# Monitor metadata:
bpma_1995_tl.metadata = {'section': 'TL', 'subsection': 'TL3', 'cad_room': 'XTL_037', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_2011_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpmd_2022_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMD', 'xaper': 0.098, 'yaper': 0.098}

# Marker metadata:
stsub_1980_tl.metadata = {'section': 'TL', 'subsection': 'TL3', 'cad_room': 'XTL_037', 'group': 'MARK', 'class': 'MARK', 'type': 'STSUB', 'xaper': 0.098, 'yaper': 0.098}
vcst98t40_1980_tl.metadata = {'section': 'TL', 'subsection': 'TL3', 'cad_room': 'XTL_037', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST98T40', 'xaper': 0.04, 'yaper': 0.04}
ensub_1997_tl.metadata = {'section': 'TL', 'subsection': 'TL3', 'cad_room': 'XTL_037', 'group': 'MARK', 'class': 'MARK', 'type': 'ENSUB', 'xaper': 0.04, 'yaper': 0.04}
stsub_1997_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_037', 'group': 'MARK', 'class': 'MARK', 'type': 'STSUB', 'xaper': 0.04, 'yaper': 0.04}
tora_2011_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'DIAG', 'class': 'CM', 'type': 'TORA', 'xaper': 0.04, 'yaper': 0.04}
vcst40t98_2014_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST40T98', 'xaper': 0.098, 'yaper': 0.098}
otre_2023_tl.metadata = {'section': 'TL', 'subsection': 'TL4', 'cad_room': 'XTL_038', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRE', 'xaper': 0.098, 'yaper': 0.098}
# fmt: on
