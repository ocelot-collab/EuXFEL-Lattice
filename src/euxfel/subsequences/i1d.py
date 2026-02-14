# Converted from component_list_2026.01.21.xls

from ocelot.cpbd.elements import Drift, Marker, Monitor, Quadrupole, SBend
from ocelot.cpbd.beam import Twiss

twiss0 = Twiss()
twiss0.E = 0.13
twiss0.alpha_x = 0.2396
twiss0.alpha_y = -2.1842
twiss0.beta_x = 3.0207
twiss0.beta_y = 7.035


# Drifts:
d_0 = Drift(l=0.002879000000000076, eid="D_0")
d_1 = Drift(l=0.002879000000000076, eid="D_1")
d_2 = Drift(l=0.966149999999999, eid="D_2")
d_3 = Drift(l=0.15615000000000048, eid="D_3")
d_4 = Drift(l=0.4060000000000059, eid="D_4")
d_5 = Drift(l=0.15014999999999645, eid="D_5")
d_6 = Drift(l=0.09914999999999832, eid="D_6")
d_7 = Drift(l=0.1500600000000034, eid="D_7")
d_8 = Drift(l=0.22500000000000142, eid="D_8")
d_9 = Drift(l=0.125, eid="D_9")
d_10 = Drift(l=0.04999999999999716, eid="D_10")
d_11 = Drift(l=2.183230000000002, eid="D_11")
d_12 = Drift(l=0.09799999999999898, eid="D_12")

# Quadrupoles:
qi_63_i1d = Quadrupole(l=0.2377, k1=4.401795, eid="QI.63.I1D")
qi_64_i1d = Quadrupole(l=0.2377, eid="QI.64.I1D")

# SBends:
bb_62_i1d = SBend(
    l=0.5, angle=0.5235987756, e1=0.261799388, e2=0.261799388, eid="BB.62.I1D"
)

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
bhm_66_i1d = Marker(eid="BHM.66.I1D")
ensec_66_i1d = Marker(eid="ENSEC.66.I1D")

# Sequence:
cell = (
    stsec_62_i1d,
    mbb_62a_i1d,
    d_0,
    bb_62_i1d,
    d_1,
    mbb_62d_i1d,
    d_2,
    qi_63_i1d,
    d_3,
    bpma_63_i1d,
    d_4,
    otrc_64_i1d,
    d_5,
    qi_64_i1d,
    d_6,
    vcst40t98_64_i1d,
    d_7,
    otrd_64_i1d,
    d_8,
    torc_64_i1d,
    d_9,
    bpmd_64_i1d,
    d_10,
    vcst98t60_64_i1d,
    d_11,
    bhm_66_i1d,
    d_12,
    ensec_66_i1d,
)

# Power Supply IDs:
# Quadrupole power supplies:
qi_63_i1d.ps_id = "QI.41.I1D"
qi_64_i1d.ps_id = "QI.42.I1D"

# SBend power supplies:
bb_62_i1d.ps_id = "BB.5.I1D"
