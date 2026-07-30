# Converted from component_list_2026.02.13.xls

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import Drift, Hcor, Marker, Monitor, Quadrupole, SBend, Vcor

twiss0 = Twiss()
twiss0.E = 2.4000000004506834
twiss0.alpha_x = 2.55519355394083
twiss0.alpha_y = -1.16932766668269
twiss0.beta_x = 28.61364619706966
twiss0.beta_y = 5.0705567123194974
twiss0.s = 443.619226


# fmt: off
# Drifts:
d_0 = Drift(l=0.5799999999999841, eid="D_0")
d_1 = Drift(l=0.17395000000001345, eid="D_1")
d_2 = Drift(l=0.18394999999999562, eid="D_2")
d_3 = Drift(l=1.0437200000000075, eid="D_3")
d_4 = Drift(l=0.13628000000002202, eid="D_4")
d_5 = Drift(l=0.17999999999995908, eid="D_5")
d_6 = Drift(l=0.19999999999998863, eid="D_6")
d_7 = Drift(l=0.9839500000000158, eid="D_7")
d_8 = Drift(l=0.43628000000002465, eid="D_8")
d_9 = Drift(l=0.4176699999999869, eid="D_9")
d_10 = Drift(l=0.5149270000000001, eid="D_10")
d_11 = Drift(l=0.16901999999995496, eid="D_11")
d_12 = Drift(l=0.2589800000000222, eid="D_12")
d_13 = Drift(l=0.224899999999991, eid="D_13")
d_14 = Drift(l=0.23402000000000953, eid="D_14")
d_15 = Drift(l=0.5136800000000361, eid="D_15")
d_16 = Drift(l=0.14999999999997726, eid="D_16")
d_17 = Drift(l=0.22500000000002274, eid="D_17")
d_18 = Drift(l=0.125, eid="D_18")
d_19 = Drift(l=0.049999999999954525, eid="D_19")
d_20 = Drift(l=0.23527000000001408, eid="D_20")
d_21 = Drift(l=0.7280000000000086, eid="D_21")

# Quadrupoles:
qf_469_b2d = Quadrupole(l=0.5321, k1=-2.19942871499906, eid="QF.469.B2D")
qe_471_b2d = Quadrupole(l=0.24, k1=1.335539651, eid="QE.471.B2D")
qf_472_b2d = Quadrupole(l=0.5321, k1=-2.19942871499906, eid="QF.472.B2D")
qf_476_b2d = Quadrupole(l=0.5321, k1=3.13097893, eid="QF.476.B2D")
qf_477_b2d = Quadrupole(l=0.5321, k1=0.7703645572993798, eid="QF.477.B2D")

# SBends:
bg_467_b2d = SBend(l=1.599999999999966, angle=0.2094395102, tilt=1.570796327, eid="BG.467.B2D")
bg_474_b2d = SBend(l=1.6000000000000227, angle=-0.2094395102, tilt=1.570796327, eid="BG.474.B2D")

# Hcors:
cfx_470_b2d = Hcor(l=0.1, eid="CFX.470.B2D")
cfx_477_b2d = Hcor(l=0.1, eid="CFX.477.B2D")

# Vcors:
cfy_468_b2d = Vcor(l=0.1, eid="CFY.468.B2D")
cfy_471_b2d = Vcor(l=0.1, eid="CFY.471.B2D")
cfy_476_b2d = Vcor(l=0.1, eid="CFY.476.B2D")

# Monitors:
bpma_469_b2d = Monitor(eid="BPMA.469.B2D")
bpma_471_b2d = Monitor(eid="BPMA.471.B2D")
bpma_477_b2d = Monitor(eid="BPMA.477.B2D")
bpmd_479_b2d = Monitor(eid="BPMD.479.B2D")

# Markers:
stsec_466_b2d = Marker(eid="STSEC.466.B2D")
mbg_467a_b2d = Marker(eid="MBG.467a.B2D")
mbg_467d_b2d = Marker(eid="MBG.467d.B2D")
otra_473_b2d = Marker(eid="OTRA.473.B2D")
mbg_474a_b2d = Marker(eid="MBG.474a.B2D")
mbg_474d_b2d = Marker(eid="MBG.474d.B2D")
vcst40t98_478_b2d = Marker(eid="VCST40T98.478.B2D")
otrd_478_b2d = Marker(eid="OTRD.478.B2D")
torc_479_b2d = Marker(eid="TORC.479.B2D")
vcst98t60_479_b2d = Marker(eid="VCST98T60.479.B2D")
duflange_479_b2d = Marker(eid="DUFLANGE.479.B2D")
duabsorb_480_b2d = Marker(eid="DUABSORB.480.B2D")
ensec_480_b2d = Marker(eid="ENSEC.480.B2D")
# fmt: on

# Sequence:
cell = (
    stsec_466_b2d,
    mbg_467a_b2d,
    bg_467_b2d,
    mbg_467d_b2d,
    d_0,
    cfy_468_b2d,
    d_1,
    qf_469_b2d,
    d_2,
    bpma_469_b2d,
    d_3,
    cfx_470_b2d,
    d_4,
    qe_471_b2d,
    d_5,
    bpma_471_b2d,
    d_6,
    cfy_471_b2d,
    d_7,
    qf_472_b2d,
    d_8,
    otra_473_b2d,
    d_9,
    mbg_474a_b2d,
    bg_474_b2d,
    mbg_474d_b2d,
    d_10,
    cfy_476_b2d,
    d_11,
    qf_476_b2d,
    d_12,
    bpma_477_b2d,
    d_13,
    cfx_477_b2d,
    d_14,
    qf_477_b2d,
    d_15,
    vcst40t98_478_b2d,
    d_16,
    otrd_478_b2d,
    d_17,
    torc_479_b2d,
    d_18,
    bpmd_479_b2d,
    d_19,
    vcst98t60_479_b2d,
    d_20,
    duflange_479_b2d,
    d_21,
    duabsorb_480_b2d,
    ensec_480_b2d,
)

# Power Supply IDs:
# Quadrupole power supplies:
qf_469_b2d.ps_id = "QF.31.B2D"
qe_471_b2d.ps_id = "QE.32.B2D"
qf_472_b2d.ps_id = "QF.33.B2D"
qf_476_b2d.ps_id = "QF.34.B2D"
qf_477_b2d.ps_id = "QF.35.B2D"

# SBend power supplies:
bg_467_b2d.ps_id = "BG.1.B2D"
bg_474_b2d.ps_id = "BG.1.B2D"

# Hcor power supplies:
cfx_470_b2d.ps_id = "CFX.1.B2D"
cfx_477_b2d.ps_id = "CFX.2.B2D"

# Vcor power supplies:
cfy_468_b2d.ps_id = "CFY.1.B2D"
cfy_471_b2d.ps_id = "CFY.2.B2D"
cfy_476_b2d.ps_id = "CFY.3.B2D"

# Monitor power supplies:
bpma_469_b2d.ps_id = "BPMA.B2D"
bpma_471_b2d.ps_id = "BPMA.B2D"
bpma_477_b2d.ps_id = "BPMA.B2D"
bpmd_479_b2d.ps_id = "BPMD.B2D"

# Marker power supplies:
stsec_466_b2d.ps_id = "STSEC.B2D.B2D"
mbg_467a_b2d.ps_id = "MBG.1.1.B2D"
mbg_467d_b2d.ps_id = "MBG.1.1.B2D"
otra_473_b2d.ps_id = "OTRA.B2D"
mbg_474a_b2d.ps_id = "MBG.1.2.B2D"
mbg_474d_b2d.ps_id = "MBG.1.2.B2D"
vcst40t98_478_b2d.ps_id = "VCST40T98.B2D"
otrd_478_b2d.ps_id = "OTRD.B2D"
torc_479_b2d.ps_id = "TORC.B2D"
vcst98t60_479_b2d.ps_id = "VCST98T60.B2D"
duflange_479_b2d.ps_id = "DUFLANGE.B2D"
duabsorb_480_b2d.ps_id = "DUABSORB.B2D"
ensec_480_b2d.ps_id = "ENSEC.B2D.B2D"

# Component list metadata:
# fmt: off
# Quadrupole metadata:
qf_469_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qe_471_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QE', 'xaper': 0.04, 'yaper': 0.04}
qf_472_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_476_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_477_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}

# SBend metadata:
bg_467_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BG', 'xaper': 0.04, 'yaper': 0.04}
bg_474_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BG', 'xaper': 0.04, 'yaper': 0.04}

# Hcor metadata:
cfx_470_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cfx_477_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}

# Vcor metadata:
cfy_468_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cfy_471_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cfy_476_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}

# Monitor metadata:
bpma_469_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_471_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_477_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpmd_479_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMD', 'xaper': 0.098, 'yaper': 0.098}

# Marker metadata:
stsec_466_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MARK', 'class': 'MARK', 'type': 'STSEC', 'xaper': 0.04, 'yaper': 0.04}
mbg_467a_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbg_467d_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
otra_473_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRA', 'xaper': 0.04, 'yaper': 0.04}
mbg_474a_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbg_474d_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
vcst40t98_478_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST40T98', 'xaper': 0.098, 'yaper': 0.098}
otrd_478_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRD', 'xaper': 0.098, 'yaper': 0.098}
torc_479_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'DIAG', 'class': 'CM', 'type': 'TORC', 'xaper': 0.098, 'yaper': 0.098}
vcst98t60_479_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST98T60', 'xaper': 0.098, 'yaper': 0.098}
duflange_479_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'DUMP', 'class': 'DUMP', 'type': 'DUFLANGE', 'xaper': 0.098, 'yaper': 0.098}
duabsorb_480_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'DUMP', 'class': 'DUMP', 'type': 'DUABSORB', 'xaper': 0.098, 'yaper': 0.098}
ensec_480_b2d.metadata = {'section': 'B2D', 'subsection': 'B2D', 'cad_room': 'XTL_008', 'group': 'MARK', 'class': 'MARK', 'type': 'ENSEC', 'xaper': 0.098, 'yaper': 0.098}
# fmt: on
