# Converted from component_list_2024.07.04.xls

from ocelot.cpbd.elements import *
from ocelot.cpbd.beam import Twiss

twiss0 = Twiss()
twiss0._E = 0.7
twiss0._beta_x = 7.4846
twiss0._beta_y = 8.6992
twiss0._alpha_x = -0.6959
twiss0._alpha_y = -1.2903



# Drifts:
d_0 = Drift(l=0.254587000000015, eid="D_0")
d_1 = Drift(l=1.3195570000000032, eid="D_1")
d_2 = Drift(l=0.15064999999998463, eid="D_2")
d_3 = Drift(l=0.1316499999999924, eid="D_3")
d_4 = Drift(l=1.2316500000000246, eid="D_4")
d_5 = Drift(l=0.6896499999999851, eid="D_5")
d_6 = Drift(l=0.18099999999998317, eid="D_6")
d_7 = Drift(l=2.584000000000026, eid="D_7")
d_8 = Drift(l=0.14829999999997767, eid="D_8")
d_9 = Drift(l=0.15430000000000632, eid="D_9")
d_10 = Drift(l=1.1493000000000109, eid="D_10")

# Quadrupoles:
qd_231_b1d = Quadrupole(l=0.2367, k1=-3.0, eid="QD.231.B1D")
qd_232_b1d = Quadrupole(l=0.2367, eid="QD.232.B1D")

# SBends:
bb_229_b1d = SBend(l=0.5, angle=0.2094395102, e2=0.20943951, tilt=1.570796327, eid="BB.229.B1D")

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
otrc_236_b1d = Marker(eid="OTRC.236.B1D")
tora_236_b1d = Marker(eid="TORA.236.B1D")
ensec_237_b1d = Marker(eid="ENSEC.237.B1D")

# Sequence:
cell = (stsec_229_b1d,
        d_0,
        bb_229_b1d,
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
        ensec_237_b1d)

# Power Supply IDs:
# Quadrupole power supplies:
qd_231_b1d.ps_id = "QD.25.B1D"
qd_232_b1d.ps_id = "QD.26.B1D"

# SBend power supplies:
bb_229_b1d.ps_id = "BB.1.B1D"