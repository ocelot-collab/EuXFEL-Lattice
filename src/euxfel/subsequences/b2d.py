# Converted from component_list_2026.01.21.xls

from ocelot.cpbd.elements import *
from ocelot.cpbd.beam import Twiss

twiss0 = Twiss()
twiss0._E = 2.4
twiss0._beta_x = 28.6148
twiss0._beta_y = 5.0704
twiss0._alpha_x = 2.5552
twiss0._alpha_y = -1.1692



# Drifts:
d_0 = Drift(l=0.0014499999999770807, eid="D_0")
d_1 = Drift(l=0.5814499999999729, eid="D_1")
d_2 = Drift(l=0.17395000000001345, eid="D_2")
d_3 = Drift(l=0.18394999999999562, eid="D_3")
d_4 = Drift(l=1.0437200000000075, eid="D_4")
d_5 = Drift(l=0.13628000000002202, eid="D_5")
d_6 = Drift(l=0.17999999999995908, eid="D_6")
d_7 = Drift(l=0.19999999999998863, eid="D_7")
d_8 = Drift(l=0.9839500000000158, eid="D_8")
d_9 = Drift(l=0.43628000000002465, eid="D_9")
d_10 = Drift(l=0.4191200000000208, eid="D_10")
d_11 = Drift(l=0.516376999999989, eid="D_11")
d_12 = Drift(l=0.16901999999995496, eid="D_12")
d_13 = Drift(l=0.2589800000000222, eid="D_13")
d_14 = Drift(l=0.224899999999991, eid="D_14")
d_15 = Drift(l=0.23402000000000953, eid="D_15")
d_16 = Drift(l=0.6636800000000134, eid="D_16")
d_17 = Drift(l=0.22500000000002274, eid="D_17")
d_18 = Drift(l=0.125, eid="D_18")
d_19 = Drift(l=1.0132699999999772, eid="D_19")

# Quadrupoles:
qf_469_b2d = Quadrupole(l=0.5321, k1=-2.19942871499906, eid="QF.469.B2D")
qe_471_b2d = Quadrupole(l=0.24, k1=1.335539651, eid="QE.471.B2D")
qf_472_b2d = Quadrupole(l=0.5321, k1=-2.19942871499906, eid="QF.472.B2D")
qf_476_b2d = Quadrupole(l=0.5321, k1=3.13097893, eid="QF.476.B2D")
qf_477_b2d = Quadrupole(l=0.5321, k1=0.7703645572993798, eid="QF.477.B2D")

# SBends:
bg_467_b2d = SBend(l=1.5971, angle=0.2094395102, tilt=1.570796327, eid="BG.467.B2D")
bg_474_b2d = SBend(l=1.5971, angle=-0.2094395102, tilt=1.570796327, eid="BG.474.B2D")

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
otra_473_b2d = Marker(eid="OTRA.473.B2D")
otrd_478_b2d = Marker(eid="OTRD.478.B2D")
torc_479_b2d = Marker(eid="TORC.479.B2D")
ensec_480_b2d = Marker(eid="ENSEC.480.B2D")

# Sequence:
cell = (stsec_466_b2d,
        d_0,
        bg_467_b2d,
        d_1,
        cfy_468_b2d,
        d_2,
        qf_469_b2d,
        d_3,
        bpma_469_b2d,
        d_4,
        cfx_470_b2d,
        d_5,
        qe_471_b2d,
        d_6,
        bpma_471_b2d,
        d_7,
        cfy_471_b2d,
        d_8,
        qf_472_b2d,
        d_9,
        otra_473_b2d,
        d_10,
        bg_474_b2d,
        d_11,
        cfy_476_b2d,
        d_12,
        qf_476_b2d,
        d_13,
        bpma_477_b2d,
        d_14,
        cfx_477_b2d,
        d_15,
        qf_477_b2d,
        d_16,
        otrd_478_b2d,
        d_17,
        torc_479_b2d,
        d_18,
        bpmd_479_b2d,
        d_19,
        ensec_480_b2d)

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