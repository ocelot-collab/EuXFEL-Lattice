# Converted from component_list_2026.02.13.xls

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import (
    Drift,
    Hcor,
    Marker,
    Monitor,
    Quadrupole,
    RBend,
    Solenoid,
    Vcor,
)

twiss0 = Twiss()
twiss0.E = 0.005
twiss0.alpha_x = 18.1886
twiss0.alpha_y = 18.1886
twiss0.beta_x = 55.7981
twiss0.beta_y = 55.7981


# fmt: off
# Drifts:
d_0 = Drift(l=0.276, eid="D_0")
d_1 = Drift(l=0.043999999999999984, eid="D_1")
d_2 = Drift(l=0.43, eid="D_2")
d_3 = Drift(l=0.003000000000000086, eid="D_3")
d_4 = Drift(l=0.04699999999999995, eid="D_4")
d_5 = Drift(l=0.1499999999999999, eid="D_5")
d_6 = Drift(l=0.19878200000000001, eid="D_6")

# Quadrupoles:
qln_23_i1 = Quadrupole(eid="QLN.23.I1")
qls_23_i1 = Quadrupole(tilt=0.785398163, eid="QLS.23.I1")

# RBends:
kix_24_i1 = RBend(l=0.1, e1=0.0, e2=0.0, eid="KIX.24.I1")
kiy_24_i1 = RBend(l=0.1, e1=0.0, e2=0.0, eid="KIY.24.I1")

# Hcors:
clx_23_i1 = Hcor(eid="CLX.23.I1")
ckx_24_i1 = Hcor(l=0.025, eid="CKX.24.I1")

# Vcors:
cly_23_i1 = Vcor(eid="CLY.23.I1")
cky_24_i1 = Vcor(l=0.025, eid="CKY.24.I1")

# Solenoids:
solb_23_i1 = Solenoid(eid="SOLB.23.I1")

# Monitors:
bpmg_24_i1 = Monitor(eid="BPMG.24.I1")

# Markers:
stsec_23_i1 = Marker(eid="STSEC.23.I1")
stsub_23_i1 = Marker(eid="STSUB.23.I1")
gun_23_i1 = Marker(eid="GUN.23.I1")
scrn_24_i1 = Marker(eid="SCRN.24.I1")
fcup_24_i1 = Marker(eid="FCUP.24.I1")
ensub_24_i1 = Marker(eid="ENSUB.24.I1")
# fmt: on

# Sequence:
cell = (
    stsec_23_i1,
    stsub_23_i1,
    gun_23_i1,
    d_0,
    solb_23_i1,
    d_1,
    qln_23_i1,
    qls_23_i1,
    clx_23_i1,
    cly_23_i1,
    d_2,
    kix_24_i1,
    kiy_24_i1,
    d_3,
    ckx_24_i1,
    cky_24_i1,
    d_4,
    bpmg_24_i1,
    d_5,
    scrn_24_i1,
    fcup_24_i1,
    d_6,
    ensub_24_i1,
)

# Power Supply IDs:
# RBend power supplies:
kix_24_i1.ps_id = "KIX.24.I1"
kiy_24_i1.ps_id = "KIY.24.I1"
