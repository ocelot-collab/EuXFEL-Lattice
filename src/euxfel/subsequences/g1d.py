# Converted from component_list_2026.02.13.xls

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import Drift, Marker, Monitor, SBend

twiss0 = Twiss()
twiss0.E = 0.005
twiss0.alpha_x = 9.870197135261082
twiss0.alpha_y = 9.870197135261082
twiss0.beta_x = 16.549959625545227
twiss0.beta_y = 16.549959625545227
twiss0.s = 1.398782


# fmt: off
# Drifts:
d_0 = Drift(l=0.23351999999999995, eid="D_0")
d_1 = Drift(l=0.08800000000000008, eid="D_1")
d_2 = Drift(l=0.10000000000000009, eid="D_2")

# SBends:
bk_24_i1 = SBend(l=0.30000000000000004, angle=1.047197551, eid="BK.24.I1")

# Monitors:
bpmg_25ii_i1 = Monitor(eid="BPMG.25II.I1")

# Markers:
stsub_24ii_i1 = Marker(eid="STSUB.24II.I1")
mbk_24a_i1 = Marker(eid="MBK.24a.I1")
mbk_24d_i1 = Marker(eid="MBK.24d.I1")
fcup_25ii_i1 = Marker(eid="FCUP.25II.I1")
scrn_25ii_i1 = Marker(eid="SCRN.25II.I1")
fcup_25iii_i1 = Marker(eid="FCUP.25III.I1")
ensub_25_i1 = Marker(eid="ENSUB.25.I1")
# fmt: on

# Sequence:
cell = (
    stsub_24ii_i1,
    mbk_24a_i1,
    bk_24_i1,
    mbk_24d_i1,
    d_0,
    fcup_25ii_i1,
    scrn_25ii_i1,
    d_1,
    bpmg_25ii_i1,
    d_2,
    fcup_25iii_i1,
    ensub_25_i1,
)

# Power Supply IDs:
# SBend power supplies:
bk_24_i1.ps_id = "BK.1.I1"
