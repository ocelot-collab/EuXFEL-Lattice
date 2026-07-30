# Converted from component_list_2026.02.13.xls

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import Drift, Marker, Monitor, Quadrupole, SBend

twiss0 = Twiss()
twiss0.E = 0.12999999999999998
twiss0.alpha_x = 0.23964062933824398
twiss0.alpha_y = -2.1841640590702722
twiss0.beta_x = 3.020592602704924
twiss0.beta_y = 7.034982640199846
twiss0.s = 38.889005


# fmt: off
# Drifts:
d_0 = Drift(l=0.966149999999999, eid="D_0")
d_1 = Drift(l=0.15615000000000048, eid="D_1")
d_2 = Drift(l=0.4060000000000059, eid="D_2")
d_3 = Drift(l=0.15014999999999645, eid="D_3")
d_4 = Drift(l=0.09914999999999832, eid="D_4")
d_5 = Drift(l=0.1500600000000034, eid="D_5")
d_6 = Drift(l=0.22500000000000142, eid="D_6")
d_7 = Drift(l=0.125, eid="D_7")
d_8 = Drift(l=0.04999999999999716, eid="D_8")
d_9 = Drift(l=0.23523000000000138, eid="D_9")
d_10 = Drift(l=0.25200000000000244, eid="D_10")
d_11 = Drift(l=1.695999999999998, eid="D_11")
d_12 = Drift(l=0.09799999999999898, eid="D_12")

# Quadrupoles:
qi_63_i1d = Quadrupole(l=0.2377, k1=4.401795, eid="QI.63.I1D")
qi_64_i1d = Quadrupole(l=0.2377, eid="QI.64.I1D")

# SBends:
bb_62_i1d = SBend(l=0.5057580000000002, angle=0.5235987756, e1=0.261799388, e2=0.261799388, eid="BB.62.I1D")

# Monitors:
bpma_63_i1d = Monitor(eid="BPMA.63.I1D")
bpmd_64_i1d = Monitor(eid="BPMD.64.I1D")

# Markers:
stsec_62_i1d = Marker(eid="STSEC.62.I1D")
mbb_62a_i1d = Marker(eid="MBB.62a.I1D")
mbb_62d_i1d = Marker(eid="MBB.62d.I1D")
otrc_64_i1d = Marker(eid="OTRC.64.I1D")
vcst40t98_64_i1d = Marker(eid="VCST40T98.64.I1D")
otrd_64_i1d = Marker(eid="OTRD.64.I1D")
torc_64_i1d = Marker(eid="TORC.64.I1D")
vcst98t60_64_i1d = Marker(eid="VCST98T60.64.I1D")
duflange_65_i1d = Marker(eid="DUFLANGE.65.I1D")
duconcrete_65_i1d = Marker(eid="DUCONCRETE.65.I1D")
bhm_66_i1d = Marker(eid="BHM.66.I1D")
duabsorb_66_i1d = Marker(eid="DUABSORB.66.I1D")
ensec_66_i1d = Marker(eid="ENSEC.66.I1D")
# fmt: on

# Sequence:
cell = (
    stsec_62_i1d,
    mbb_62a_i1d,
    bb_62_i1d,
    mbb_62d_i1d,
    d_0,
    qi_63_i1d,
    d_1,
    bpma_63_i1d,
    d_2,
    otrc_64_i1d,
    d_3,
    qi_64_i1d,
    d_4,
    vcst40t98_64_i1d,
    d_5,
    otrd_64_i1d,
    d_6,
    torc_64_i1d,
    d_7,
    bpmd_64_i1d,
    d_8,
    vcst98t60_64_i1d,
    d_9,
    duflange_65_i1d,
    d_10,
    duconcrete_65_i1d,
    d_11,
    bhm_66_i1d,
    d_12,
    duabsorb_66_i1d,
    ensec_66_i1d,
)

# Power Supply IDs:
# Quadrupole power supplies:
qi_63_i1d.ps_id = "QI.41.I1D"
qi_64_i1d.ps_id = "QI.42.I1D"

# SBend power supplies:
bb_62_i1d.ps_id = "BB.5.I1D"

# Monitor power supplies:
bpma_63_i1d.ps_id = "BPMA.I1D"
bpmd_64_i1d.ps_id = "BPMD.I1D"

# Marker power supplies:
stsec_62_i1d.ps_id = "STSEC.I1D.I1D"
mbb_62a_i1d.ps_id = "MBB.5.I1D"
mbb_62d_i1d.ps_id = "MBB.5.I1D"
otrc_64_i1d.ps_id = "OTRC.I1D"
vcst40t98_64_i1d.ps_id = "VCST40T98.I1D"
otrd_64_i1d.ps_id = "OTRD.I1D"
torc_64_i1d.ps_id = "TORC.I1D"
vcst98t60_64_i1d.ps_id = "VCST98T60.I1D"
duflange_65_i1d.ps_id = "DUFLANGE.I1D"
duconcrete_65_i1d.ps_id = "DUCONCRETE.I1D"
bhm_66_i1d.ps_id = "BHM.I1D"
duabsorb_66_i1d.ps_id = "DUABSORB.I1D"
ensec_66_i1d.ps_id = "ENSEC.I1D.I1D"

# Component list metadata:
# fmt: off
# Quadrupole metadata:
qi_63_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}
qi_64_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QI', 'xaper': 0.04, 'yaper': 0.04}

# SBend metadata:
bb_62_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BB', 'xaper': 0.04, 'yaper': 0.04}

# Monitor metadata:
bpma_63_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpmd_64_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMD', 'xaper': 0.098, 'yaper': 0.098}

# Marker metadata:
stsec_62_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'MARK', 'class': 'MARK', 'type': 'STSEC', 'xaper': 0.04, 'yaper': 0.04}
mbb_62a_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbb_62d_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
otrc_64_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRC', 'xaper': 0.04, 'yaper': 0.04}
vcst40t98_64_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST40T98', 'xaper': 0.098, 'yaper': 0.098}
otrd_64_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRD', 'xaper': 0.098, 'yaper': 0.098}
torc_64_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'DIAG', 'class': 'CM', 'type': 'TORC', 'xaper': 0.098, 'yaper': 0.098}
vcst98t60_64_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST98T60', 'xaper': 0.098, 'yaper': 0.098}
duflange_65_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'DUMP', 'class': 'DUMP', 'type': 'DUFLANGE', 'xaper': 0.098, 'yaper': 0.098}
duconcrete_65_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'DUMP', 'class': 'DUMP', 'type': 'DUCONCRETE', 'xaper': 0.098, 'yaper': 0.098}
bhm_66_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'DIAG', 'class': 'INSTR', 'type': 'BHM', 'xaper': 0.098, 'yaper': 0.098}
duabsorb_66_i1d.metadata = {'section': 'I1D', 'subsection': 'I1D', 'cad_room': 'XTIN_000', 'group': 'DUMP', 'class': 'DUMP', 'type': 'DUABSORB', 'xaper': 0.098, 'yaper': 0.098}
# fmt: on
