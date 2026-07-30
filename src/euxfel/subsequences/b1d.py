# Converted from component_list_2026.02.13.xls

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import Drift, Hcor, Marker, Monitor, Quadrupole, SBend, Vcor

twiss0 = Twiss()
twiss0.E = 0.7000000007706801
twiss0.alpha_x = -0.6958914582198614
twiss0.alpha_y = -1.2901388217363727
twiss0.beta_x = 7.485110494209615
twiss0.beta_y = 8.698761588502316
twiss0.s = 206.100754


# fmt: off
# Drifts:
d_0 = Drift(l=0.2527499999999918, eid="D_0")
d_1 = Drift(l=1.3177200000000084, eid="D_1")
d_2 = Drift(l=0.15064999999998463, eid="D_2")
d_3 = Drift(l=0.1316499999999924, eid="D_3")
d_4 = Drift(l=1.2316500000000246, eid="D_4")
d_5 = Drift(l=0.6896499999999851, eid="D_5")
d_6 = Drift(l=0.18099999999998317, eid="D_6")
d_7 = Drift(l=2.584000000000026, eid="D_7")
d_8 = Drift(l=0.14829999999997767, eid="D_8")
d_9 = Drift(l=0.15430000000000632, eid="D_9")
d_10 = Drift(l=0.265199999999993, eid="D_10")
d_11 = Drift(l=0.1600999999999999, eid="D_11")
d_12 = Drift(l=0.724000000000018, eid="D_12")

# Quadrupoles:
qd_231_b1d = Quadrupole(l=0.2367, k1=-3.0, eid="QD.231.B1D")
qd_232_b1d = Quadrupole(l=0.2367, eid="QD.232.B1D")

# SBends:
bb_229_b1d = SBend(l=0.5036740000000179, angle=0.2094395102, e2=0.20943951, tilt=1.570796327, eid="BB.229.B1D")

# Hcors:
ccx_233_b1d = Hcor(l=0.1, eid="CCX.233.B1D")

# Vcors:
ccy_231_b1d = Vcor(l=0.1, eid="CCY.231.B1D")

# Monitors:
bpma_231_b1d = Monitor(eid="BPMA.231.B1D")
bpma_233_b1d = Monitor(eid="BPMA.233.B1D")
bpma_236_b1d = Monitor(eid="BPMA.236.B1D")

# Markers:
stsec_229_b1d = Marker(eid="STSEC.229.B1D")
mbb_229a_b1d = Marker(eid="MBB.229a.B1D")
mbb_229d_b1d = Marker(eid="MBB.229d.B1D")
otrc_236_b1d = Marker(eid="OTRC.236.B1D")
tora_236_b1d = Marker(eid="TORA.236.B1D")
vcst40t60_237_b1d = Marker(eid="VCST40T60.237.B1D")
duflange_237_b1d = Marker(eid="DUFLANGE.237.B1D")
duabsorb_237_b1d = Marker(eid="DUABSORB.237.B1D")
ensec_237_b1d = Marker(eid="ENSEC.237.B1D")
# fmt: on

# Sequence:
cell = (
    stsec_229_b1d,
    d_0,
    mbb_229a_b1d,
    bb_229_b1d,
    mbb_229d_b1d,
    d_1,
    bpma_231_b1d,
    d_2,
    qd_231_b1d,
    d_3,
    ccy_231_b1d,
    d_4,
    qd_232_b1d,
    d_5,
    bpma_233_b1d,
    d_6,
    ccx_233_b1d,
    d_7,
    otrc_236_b1d,
    d_8,
    tora_236_b1d,
    d_9,
    bpma_236_b1d,
    d_10,
    vcst40t60_237_b1d,
    d_11,
    duflange_237_b1d,
    d_12,
    duabsorb_237_b1d,
    ensec_237_b1d,
)

# Power Supply IDs:
# Quadrupole power supplies:
qd_231_b1d.ps_id = "QD.25.B1D"
qd_232_b1d.ps_id = "QD.26.B1D"

# SBend power supplies:
bb_229_b1d.ps_id = "BB.1.B1D"

# Hcor power supplies:
ccx_233_b1d.ps_id = "CCX.1.B1D"

# Vcor power supplies:
ccy_231_b1d.ps_id = "CCY.1.B1D"

# Monitor power supplies:
bpma_231_b1d.ps_id = "BPMA.B1D"
bpma_233_b1d.ps_id = "BPMA.B1D"
bpma_236_b1d.ps_id = "BPMA.B1D"

# Marker power supplies:
stsec_229_b1d.ps_id = "STSEC.B1D.B1D"
mbb_229a_b1d.ps_id = "MBB.1.B1D"
mbb_229d_b1d.ps_id = "MBB.1.B1D"
otrc_236_b1d.ps_id = "OTRC.B1D"
tora_236_b1d.ps_id = "TORA.B1D"
vcst40t60_237_b1d.ps_id = "VCST40T60.B1D"
duflange_237_b1d.ps_id = "DUFLANGE.B1D"
duabsorb_237_b1d.ps_id = "DUABSORB.B1D"
ensec_237_b1d.ps_id = "ENSEC.B1D.B1D"

# Component list metadata:
# fmt: off
# Quadrupole metadata:
qd_231_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QD', 'xaper': 0.04, 'yaper': 0.04}
qd_232_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QD', 'xaper': 0.04, 'yaper': 0.04}

# SBend metadata:
bb_229_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BB', 'xaper': 0.04, 'yaper': 0.04}

# Hcor metadata:
ccx_233_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CCX', 'xaper': 0.04, 'yaper': 0.04}

# Vcor metadata:
ccy_231_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CCY', 'xaper': 0.04, 'yaper': 0.04}

# Monitor metadata:
bpma_231_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_233_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_236_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}

# Marker metadata:
stsec_229_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'STSEC', 'xaper': 0.04, 'yaper': 0.04}
mbb_229a_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbb_229d_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
otrc_236_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRC', 'xaper': 0.04, 'yaper': 0.04}
tora_236_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'DIAG', 'class': 'CM', 'type': 'TORA', 'xaper': 0.04, 'yaper': 0.04}
vcst40t60_237_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST40T60', 'xaper': 0.06, 'yaper': 0.06}
duflange_237_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'DUMP', 'class': 'DUMP', 'type': 'DUFLANGE', 'xaper': 0.06, 'yaper': 0.06}
duabsorb_237_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'DUMP', 'class': 'DUMP', 'type': 'DUABSORB', 'xaper': 0.06, 'yaper': 0.06}
ensec_237_b1d.metadata = {'section': 'B1D', 'subsection': 'B1D', 'cad_room': 'XTL_003', 'group': 'MARK', 'class': 'MARK', 'type': 'ENSEC', 'xaper': 0.06, 'yaper': 0.06}
# fmt: on
