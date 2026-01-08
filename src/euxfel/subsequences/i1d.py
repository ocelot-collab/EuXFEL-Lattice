from ocelot import *

twiss0 = Twiss()
twiss0._E = 0.13
twiss0._beta_x = 3.0207
twiss0._beta_y = 7.035
twiss0._alpha_x = 0.2396
twiss0._alpha_y = -2.1842



# Drifts:
d_0 = Drift(l=0.002879000000000076, eid="D_0")
d_1 = Drift(l=0.969028999999999, eid="D_1")
d_2 = Drift(l=0.15615000000000048, eid="D_2")
d_3 = Drift(l=0.4060000000000059, eid="D_3")
d_4 = Drift(l=0.15014999999999645, eid="D_4")
d_5 = Drift(l=0.24921000000000174, eid="D_5")
d_6 = Drift(l=0.22500000000000142, eid="D_6")
d_7 = Drift(l=0.125, eid="D_7")
d_8 = Drift(l=2.233229999999999, eid="D_8")
d_9 = Drift(l=0.09799999999999898, eid="D_9")

# Quadrupoles:
qi_63_i1d = Quadrupole(l=0.2377, k1=4.401795, eid="QI.63.I1D")
qi_64_i1d = Quadrupole(l=0.2377, eid="QI.64.I1D")

# SBends:
bb_62_i1d = SBend(l=0.5, angle=0.5235987756, e1=0.261799388, e2=0.261799388, eid="BB.62.I1D")

# Monitors:
bpma_63_i1d = Monitor(eid="BPMA.63.I1D")
bpmd_64_i1d = Monitor(eid="BPMD.64.I1D")

# Markers:
stsec_62_i1d = Marker(eid="STSEC.62.I1D")
otrc_64_i1d = Marker(eid="OTRC.64.I1D")
otrd_64_i1d = Marker(eid="OTRD.64.I1D")
torc_64_i1d = Marker(eid="TORC.64.I1D")
bhm_66_i1d = Marker(eid="BHM.66.I1D")
ensec_66_i1d = Marker(eid="ENSEC.66.I1D")

# Sequence:
cell = (stsec_62_i1d,
        d_0,
        bb_62_i1d,
        d_1,
        qi_63_i1d,
        d_2,
        bpma_63_i1d,
        d_3,
        otrc_64_i1d,
        d_4,
        qi_64_i1d,
        d_5,
        otrd_64_i1d,
        d_6,
        torc_64_i1d,
        d_7,
        bpmd_64_i1d,
        d_8,
        bhm_66_i1d,
        d_9,
        ensec_66_i1d)

# Power Supply IDs:
# Quadrupole power supplies:
qi_63_i1d.ps_id = "QI.41.I1D"
qi_64_i1d.ps_id = "QI.42.I1D"

# SBend power supplies:
bb_62_i1d.ps_id = "BB.5.I1D"