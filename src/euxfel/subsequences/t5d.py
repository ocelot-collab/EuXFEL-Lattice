# Converted from component_list_2026.02.13.xls

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import (
    Drift,
    Hcor,
    Marker,
    Monitor,
    Quadrupole,
    RBend,
    SBend,
    Sextupole,
    Vcor,
)

twiss0 = Twiss()
twiss0.E = 14.0000000004506
twiss0.alpha_x = -1.0629556476430717
twiss0.alpha_y = 1.240105329279162
twiss0.beta_x = 41.20144102651318
twiss0.beta_y = 47.75834353766889
twiss0.Dx = 1.2652400562403778e-05
twiss0.Dy = 6.627506550612603e-06
twiss0.s = 3016.8813410000203


# fmt: off
# Drifts:
d_0 = Drift(l=1.0, eid="D_0")
d_1 = Drift(l=12.471400000000358, eid="D_1")
d_2 = Drift(l=15.514999999999654, eid="D_2")
d_3 = Drift(l=0.20895000000018626, eid="D_3")
d_4 = Drift(l=0.15394999999979553, eid="D_4")
d_5 = Drift(l=11.205000000000291, eid="D_5")
d_6 = Drift(l=0.20894999999973152, eid="D_6")
d_7 = Drift(l=0.15394999999979553, eid="D_7")
d_8 = Drift(l=60.20500000000029, eid="D_8")
d_9 = Drift(l=0.20894999999973152, eid="D_9")
d_10 = Drift(l=0.15395000000025028, eid="D_10")
d_11 = Drift(l=5.360000000000037, eid="D_11")
d_12 = Drift(l=0.15394999999980427, eid="D_12")
d_13 = Drift(l=0.2639500000003776, eid="D_13")
d_14 = Drift(l=0.09600000000000364, eid="D_14")
d_15 = Drift(l=0.11079999999992651, eid="D_15")
d_16 = Drift(l=0.2828220000001238, eid="D_16")
d_17 = Drift(l=0.23299999999971988, eid="D_17")
d_18 = Drift(l=0.5, eid="D_18")
d_19 = Drift(l=0.5919000000003507, eid="D_19")
d_20 = Drift(l=1.3380999999999403, eid="D_20")
d_21 = Drift(l=0.14239999999990688, eid="D_21")
d_22 = Drift(l=0.19739999999980218, eid="D_22")
d_23 = Drift(l=0.5535000000004402, eid="D_23")
d_24 = Drift(l=0.9034999999997417, eid="D_24")
d_25 = Drift(l=0.8535000000001673, eid="D_25")
d_26 = Drift(l=0.5534999999998327, eid="D_26")
d_27 = Drift(l=0.197400000000016, eid="D_27")
d_28 = Drift(l=0.1423999999999659, eid="D_28")
d_29 = Drift(l=1.7219999999999345, eid="D_29")
d_30 = Drift(l=0.20800000000008367, eid="D_30")
d_31 = Drift(l=0.5, eid="D_31")
d_32 = Drift(l=0.20799999999962893, eid="D_32")
d_33 = Drift(l=0.40370000000029904, eid="D_33")
d_34 = Drift(l=0.16069999999990614, eid="D_34")
d_35 = Drift(l=0.34480000000009103, eid="D_35")
d_36 = Drift(l=0.34480000000009103, eid="D_36")
d_37 = Drift(l=0.34480000000009103, eid="D_37")
d_38 = Drift(l=0.21439999999962756, eid="D_38")
d_39 = Drift(l=0.5579999999999927, eid="D_39")
d_40 = Drift(l=0.49999999999987266, eid="D_40")
d_41 = Drift(l=0.8219999999999891, eid="D_41")
d_42 = Drift(l=0.20000000000027285, eid="D_42")
d_43 = Drift(l=0.4499999999998181, eid="D_43")
d_44 = Drift(l=0.31300000000010186, eid="D_44")
d_45 = Drift(l=0.6430000000000291, eid="D_45")
d_46 = Drift(l=3.2269999999998618, eid="D_46")
d_47 = Drift(l=0.3223000000002685, eid="D_47")
d_48 = Drift(l=0.8577999999997701, eid="D_48")
d_49 = Drift(l=1.073240000000169, eid="D_49")
d_50 = Drift(l=2.0144000000000233, eid="D_50")

# Quadrupoles:
qe_3052_t5d = Quadrupole(l=0.24, k1=0.1781107015, eid="QE.3052.T5D")
qf_3068_t5d = Quadrupole(l=0.5321, k1=-0.17408057190001877, eid="QF.3068.T5D")
qf_3081_t5d = Quadrupole(l=0.5321, k1=0.041949297430934035, eid="QF.3081.T5D")
qf_3142_t5d = Quadrupole(l=0.5321, k1=0.1523450185002819, eid="QF.3142.T5D")
qf_3148_t5d = Quadrupole(l=0.5321, k1=-0.08121677321931968, eid="QF.3148.T5D")
qk_3158_t5d = Quadrupole(l=1.0552, k1=-0.172994430300417, eid="QK.3158.T5D")
qk_3163_t5d = Quadrupole(l=1.0552, k1=-0.172994430300417, eid="QK.3163.T5D")
qk_3172_t5d = Quadrupole(l=1.0552, k1=-0.18514803489954512, eid="QK.3172.T5D")
qk_3174_t5d = Quadrupole(l=1.0552, k1=-0.18514803489954512, eid="QK.3174.T5D")
qk_3175_t5d = Quadrupole(l=1.0552, k1=-0.18514803489954512, eid="QK.3175.T5D")
qk_3177_t5d = Quadrupole(l=1.0552, k1=-0.18514803489954512, eid="QK.3177.T5D")

# SBends:
bv_3151_t5d = SBend(l=2.500198000000182, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3151.T5D")
bv_3154_t5d = SBend(l=2.5001979999997275, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3154.T5D")
bv_3167_t5d = SBend(l=2.500199000000066, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3167.T5D")
bv_3170_t5d = SBend(l=2.500198000000182, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3170.T5D")

# RBends:
sweep_3178_t5d = RBend(l=0.64, e1=0.0, e2=0.0, tilt=-1.570796327, eid="SWEEP.3178.T5D")
sweep_3179_t5d = RBend(l=0.64, e1=0.0, e2=0.0, eid="SWEEP.3179.T5D")

# Sextupoles:
sk_3159_t5d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid="SK.3159.T5D")
sk_3161_t5d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid="SK.3161.T5D")

# Hcors:
cfx_3081_t5d = Hcor(l=0.1, eid="CFX.3081.T5D")
cfx_3142_t5d = Hcor(l=0.1, eid="CFX.3142.T5D")
cnx_3157_t5d = Hcor(l=0.3, eid="CNX.3157.T5D")

# Vcors:
cfy_3069_t5d = Vcor(l=0.1, eid="CFY.3069.T5D")
cfy_3148_t5d = Vcor(l=0.1, eid="CFY.3148.T5D")
cny_3164_t5d = Vcor(l=0.3, eid="CNY.3164.T5D")

# Monitors:
bpma_3068_t5d = Monitor(eid="BPMA.3068.T5D")
bpma_3080_t5d = Monitor(eid="BPMA.3080.T5D")
bpma_3141_t5d = Monitor(eid="BPMA.3141.T5D")
bpmf_3149_t5d = Monitor(eid="BPMF.3149.T5D")
bpmd_3159_t5d = Monitor(eid="BPMD.3159.T5D")
bpmd_3162_t5d = Monitor(eid="BPMD.3162.T5D")
bpmd_3172_t5d = Monitor(eid="BPMD.3172.T5D")
bpmd_3177_t5d = Monitor(eid="BPMD.3177.T5D")
bpmd_3180_t5d = Monitor(eid="BPMD.3180.T5D")
bpmw_3185_t5d = Monitor(eid="BPMW.3185.T5D")

# Markers:
stsec_3039_t5d = Marker(eid="STSEC.3039.T5D")
stsub_3039_t5d = Marker(eid="STSUB.3039.T5D")
tora_3040_t5d = Marker(eid="TORA.3040.T5D")
midbpmf_3149_t5d = Marker(eid="MIDBPMF.3149.T5D")
tora_3149_t5d = Marker(eid="TORA.3149.T5D")
vcst40t93y_3149_t5d = Marker(eid="VCST40T93Y.3149.T5D")
ensub_3149_t5d = Marker(eid="ENSUB.3149.T5D")
stsub_3149_t5d = Marker(eid="STSUB.3149.T5D")
mbv_3151a_t5d = Marker(eid="MBV.3151a.T5D")
mbv_3151d_t5d = Marker(eid="MBV.3151d.T5D")
vcst93yt40_3152_t5d = Marker(eid="VCST93YT40.3152.T5D")
mbv_3154a_t5d = Marker(eid="MBV.3154a.T5D")
mbv_3154d_t5d = Marker(eid="MBV.3154d.T5D")
vcst40t98_3156_t5d = Marker(eid="VCST40T98.3156.T5D")
otrd_3160_t5d = Marker(eid="OTRD.3160.T5D")
vcst98t98y_3166_t5d = Marker(eid="VCST98T98Y.3166.T5D")
mbv_3167a_t5d = Marker(eid="MBV.3167a.T5D")
mbv_3167d_t5d = Marker(eid="MBV.3167d.T5D")
mbv_3170a_t5d = Marker(eid="MBV.3170a.T5D")
mbv_3170d_t5d = Marker(eid="MBV.3170d.T5D")
vcst98yt98_3171_t5d = Marker(eid="VCST98YT98.3171.T5D")
otrd_3181_t5d = Marker(eid="OTRD.3181.T5D")
torc_3181_t5d = Marker(eid="TORC.3181.T5D")
bhm_3181_t5d = Marker(eid="BHM.3181.T5D")
vcst98t200_3182_t5d = Marker(eid="VCST98T200.3182.T5D")
scrw_3186_t5d = Marker(eid="SCRW.3186.T5D")
duwindow_3186_t5d = Marker(eid="DUWINDOW.3186.T5D")
duflange_3186_t5d = Marker(eid="DUFLANGE.3186.T5D")
duconcrete_3187_t5d = Marker(eid="DUCONCRETE.3187.T5D")
duabsorb_3189_t5d = Marker(eid="DUABSORB.3189.T5D")
ensub_3189_t5d = Marker(eid="ENSUB.3189.T5D")
ensec_3189_t5d = Marker(eid="ENSEC.3189.T5D")
# fmt: on

# Sequence:
cell = (
    stsec_3039_t5d,
    stsub_3039_t5d,
    d_0,
    tora_3040_t5d,
    d_1,
    qe_3052_t5d,
    d_2,
    bpma_3068_t5d,
    d_3,
    qf_3068_t5d,
    d_4,
    cfy_3069_t5d,
    d_5,
    bpma_3080_t5d,
    d_6,
    qf_3081_t5d,
    d_7,
    cfx_3081_t5d,
    d_8,
    bpma_3141_t5d,
    d_9,
    qf_3142_t5d,
    d_10,
    cfx_3142_t5d,
    d_11,
    cfy_3148_t5d,
    d_12,
    qf_3148_t5d,
    d_13,
    midbpmf_3149_t5d,
    d_14,
    bpmf_3149_t5d,
    d_15,
    tora_3149_t5d,
    d_16,
    vcst40t93y_3149_t5d,
    d_17,
    ensub_3149_t5d,
    stsub_3149_t5d,
    mbv_3151a_t5d,
    bv_3151_t5d,
    mbv_3151d_t5d,
    vcst93yt40_3152_t5d,
    d_18,
    mbv_3154a_t5d,
    bv_3154_t5d,
    mbv_3154d_t5d,
    d_19,
    vcst40t98_3156_t5d,
    d_20,
    cnx_3157_t5d,
    d_21,
    qk_3158_t5d,
    d_22,
    bpmd_3159_t5d,
    d_23,
    sk_3159_t5d,
    d_24,
    otrd_3160_t5d,
    d_25,
    sk_3161_t5d,
    d_26,
    bpmd_3162_t5d,
    d_27,
    qk_3163_t5d,
    d_28,
    cny_3164_t5d,
    d_29,
    vcst98t98y_3166_t5d,
    d_30,
    mbv_3167a_t5d,
    bv_3167_t5d,
    mbv_3167d_t5d,
    d_31,
    mbv_3170a_t5d,
    bv_3170_t5d,
    mbv_3170d_t5d,
    d_32,
    vcst98yt98_3171_t5d,
    d_33,
    bpmd_3172_t5d,
    d_34,
    qk_3172_t5d,
    d_35,
    qk_3174_t5d,
    d_36,
    qk_3175_t5d,
    d_37,
    qk_3177_t5d,
    d_38,
    bpmd_3177_t5d,
    d_39,
    sweep_3178_t5d,
    d_40,
    sweep_3179_t5d,
    d_41,
    bpmd_3180_t5d,
    d_42,
    otrd_3181_t5d,
    d_43,
    torc_3181_t5d,
    d_44,
    bhm_3181_t5d,
    d_45,
    vcst98t200_3182_t5d,
    d_46,
    bpmw_3185_t5d,
    d_47,
    scrw_3186_t5d,
    duwindow_3186_t5d,
    d_48,
    duflange_3186_t5d,
    d_49,
    duconcrete_3187_t5d,
    d_50,
    duabsorb_3189_t5d,
    ensub_3189_t5d,
    ensec_3189_t5d,
)

# Power Supply IDs:
# Quadrupole power supplies:
qe_3052_t5d.ps_id = "QE.1.T5D"
qf_3068_t5d.ps_id = "QF.1.T5D"
qf_3081_t5d.ps_id = "QF.2.T5D"
qf_3142_t5d.ps_id = "QF.3.T5D"
qf_3148_t5d.ps_id = "QF.4.T5D"
qk_3158_t5d.ps_id = "QK.1.T5D"
qk_3163_t5d.ps_id = "QK.1.T5D"
qk_3172_t5d.ps_id = "QK.6.T5D"
qk_3174_t5d.ps_id = "QK.6.T5D"
qk_3175_t5d.ps_id = "QK.6.T5D"
qk_3177_t5d.ps_id = "QK.6.T5D"

# SBend power supplies:
bv_3151_t5d.ps_id = "BV.1.T5D"
bv_3154_t5d.ps_id = "BV.1.T5D"
bv_3167_t5d.ps_id = "BV.1.T5D"
bv_3170_t5d.ps_id = "BV.1.T5D"

# RBend power supplies:
sweep_3178_t5d.ps_id = "SWEEP.1.T5D"
sweep_3179_t5d.ps_id = "SWEEP.1.T5D"

# Sextupole power supplies:
sk_3159_t5d.ps_id = "SK.1.T5D"
sk_3161_t5d.ps_id = "SK.1.T5D"

# Hcor power supplies:
cfx_3081_t5d.ps_id = "CFX.1.T5D"
cfx_3142_t5d.ps_id = "CFX.2.T5D"
cnx_3157_t5d.ps_id = "CNX.3.T5D"

# Vcor power supplies:
cfy_3069_t5d.ps_id = "CFY.1.T5D"
cfy_3148_t5d.ps_id = "CFY.2.T5D"
cny_3164_t5d.ps_id = "CNY.3.T5D"

# Monitor power supplies:
bpma_3068_t5d.ps_id = "BPMA.T5D"
bpma_3080_t5d.ps_id = "BPMA.T5D"
bpma_3141_t5d.ps_id = "BPMA.T5D"
bpmf_3149_t5d.ps_id = "BPMF.T5D"
bpmd_3159_t5d.ps_id = "BPMD.T5D"
bpmd_3162_t5d.ps_id = "BPMD.T5D"
bpmd_3172_t5d.ps_id = "BPMD.T5D"
bpmd_3177_t5d.ps_id = "BPMD.T5D"
bpmd_3180_t5d.ps_id = "BPMD.T5D"
bpmw_3185_t5d.ps_id = "BPMW.T5D"

# Marker power supplies:
stsec_3039_t5d.ps_id = "STSEC.T5D.T5D"
stsub_3039_t5d.ps_id = "STSUB.T5DU.T5D"
tora_3040_t5d.ps_id = "TORA.T5D"
midbpmf_3149_t5d.ps_id = "MIDBPMF.T5D"
tora_3149_t5d.ps_id = "TORA.T5D"
vcst40t93y_3149_t5d.ps_id = "VCST40T93Y.T5D"
ensub_3149_t5d.ps_id = "ENSUB.T5DU.T5D"
stsub_3149_t5d.ps_id = "STSUB.T5DT.T5D"
mbv_3151a_t5d.ps_id = "MBV.1.T5D"
mbv_3151d_t5d.ps_id = "MBV.1.T5D"
vcst93yt40_3152_t5d.ps_id = "VCST93YT40.T5D"
mbv_3154a_t5d.ps_id = "MBV.1.T5D"
mbv_3154d_t5d.ps_id = "MBV.1.T5D"
vcst40t98_3156_t5d.ps_id = "VCST40T98.T5D"
otrd_3160_t5d.ps_id = "OTRD.T5D"
vcst98t98y_3166_t5d.ps_id = "VCST98T98Y.T5D"
mbv_3167a_t5d.ps_id = "MBV.1.T5D"
mbv_3167d_t5d.ps_id = "MBV.1.T5D"
mbv_3170a_t5d.ps_id = "MBV.1.T5D"
mbv_3170d_t5d.ps_id = "MBV.1.T5D"
vcst98yt98_3171_t5d.ps_id = "VCST98YT98.T5D"
otrd_3181_t5d.ps_id = "OTRD.T5D"
torc_3181_t5d.ps_id = "TORC.T5D"
bhm_3181_t5d.ps_id = "BHM.T5D"
vcst98t200_3182_t5d.ps_id = "VCST98T200.T5D"
scrw_3186_t5d.ps_id = "SCRW.T5D"
duwindow_3186_t5d.ps_id = "DUWINDOW.T5D"
duflange_3186_t5d.ps_id = "DUFLANGE.T5D"
duconcrete_3187_t5d.ps_id = "DUCONCRETE.T5D"
duabsorb_3189_t5d.ps_id = "DUABSORB.T5D"
ensub_3189_t5d.ps_id = "ENSUB.T5DT.T5D"
ensec_3189_t5d.ps_id = "ENSEC.T5D.T5D"

# Component list metadata:
# fmt: off
# Quadrupole metadata:
qe_3052_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_002', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QE', 'xaper': 0.04, 'yaper': 0.04}
qf_3068_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_002', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_3081_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_003', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_3142_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_005', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qf_3148_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_005', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QF', 'xaper': 0.04, 'yaper': 0.04}
qk_3158_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QK', 'xaper': 0.098, 'yaper': 0.098}
qk_3163_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QK', 'xaper': 0.098, 'yaper': 0.098}
qk_3172_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QK', 'xaper': 0.098, 'yaper': 0.098}
qk_3174_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QK', 'xaper': 0.098, 'yaper': 0.098}
qk_3175_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QK', 'xaper': 0.098, 'yaper': 0.098}
qk_3177_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'MAGNET', 'class': 'QUAD', 'type': 'QK', 'xaper': 0.098, 'yaper': 0.098}

# SBend metadata:
bv_3151_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_005', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BV', 'xaper': 0.04, 'yaper': 0.093}
bv_3154_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BV', 'xaper': 0.04, 'yaper': 0.04}
bv_3167_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BV', 'xaper': 0.04, 'yaper': 0.098}
bv_3170_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MAGNET', 'class': 'SBEN', 'type': 'BV', 'xaper': 0.04, 'yaper': 0.098}

# RBend metadata:
sweep_3178_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'MAGNET', 'class': 'RBEN', 'type': 'SWEEP', 'xaper': 0.098, 'yaper': 0.098}
sweep_3179_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'MAGNET', 'class': 'RBEN', 'type': 'SWEEP', 'xaper': 0.098, 'yaper': 0.098}

# Sextupole metadata:
sk_3159_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SK', 'xaper': 0.098, 'yaper': 0.098}
sk_3161_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MAGNET', 'class': 'SEXT', 'type': 'SK', 'xaper': 0.098, 'yaper': 0.098}

# Hcor metadata:
cfx_3081_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_003', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cfx_3142_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_005', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CFX', 'xaper': 0.04, 'yaper': 0.04}
cnx_3157_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MAGNET', 'class': 'HKIC', 'type': 'CNX', 'xaper': 0.098, 'yaper': 0.098}

# Vcor metadata:
cfy_3069_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_002', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cfy_3148_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_005', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CFY', 'xaper': 0.04, 'yaper': 0.04}
cny_3164_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MAGNET', 'class': 'VKIC', 'type': 'CNY', 'xaper': 0.098, 'yaper': 0.098}

# Monitor metadata:
bpma_3068_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_002', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_3080_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_003', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpma_3141_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_005', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMA', 'xaper': 0.04, 'yaper': 0.04}
bpmf_3149_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_005', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMF', 'xaper': 0.04, 'yaper': 0.04}
bpmd_3159_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMD', 'xaper': 0.098, 'yaper': 0.098}
bpmd_3162_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMD', 'xaper': 0.098, 'yaper': 0.098}
bpmd_3172_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMD', 'xaper': 0.098, 'yaper': 0.098}
bpmd_3177_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMD', 'xaper': 0.098, 'yaper': 0.098}
bpmd_3180_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMD', 'xaper': 0.098, 'yaper': 0.098}
bpmw_3185_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'DIAG', 'class': 'MONI', 'type': 'BPMW', 'xaper': 0.2, 'yaper': 0.2}

# Marker metadata:
stsec_3039_t5d.metadata = {'section': 'T5D', 'subsection': 'T5D', 'cad_room': 'XTD5_002', 'group': 'MARK', 'class': 'MARK', 'type': 'STSEC', 'xaper': 0.04, 'yaper': 0.04}
stsub_3039_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_002', 'group': 'MARK', 'class': 'MARK', 'type': 'STSUB', 'xaper': 0.04, 'yaper': 0.04}
tora_3040_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_002', 'group': 'DIAG', 'class': 'CM', 'type': 'TORA', 'xaper': 0.04, 'yaper': 0.04}
midbpmf_3149_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_005', 'group': 'MARK', 'class': 'MARK', 'type': 'MIDBPMF', 'xaper': 0.04, 'yaper': 0.04}
tora_3149_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_005', 'group': 'DIAG', 'class': 'CM', 'type': 'TORA', 'xaper': 0.04, 'yaper': 0.04}
vcst40t93y_3149_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_005', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST40T93Y', 'xaper': 0.04, 'yaper': 0.093}
ensub_3149_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DU', 'cad_room': 'XTD5_005', 'group': 'MARK', 'class': 'MARK', 'type': 'ENSUB', 'xaper': 0.04, 'yaper': 0.093}
stsub_3149_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_005', 'group': 'MARK', 'class': 'MARK', 'type': 'STSUB', 'xaper': 0.04, 'yaper': 0.093}
mbv_3151a_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_005', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.093}
mbv_3151d_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.093}
vcst93yt40_3152_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST93YT40', 'xaper': 0.04, 'yaper': 0.04}
mbv_3154a_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
mbv_3154d_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.04}
vcst40t98_3156_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST40T98', 'xaper': 0.098, 'yaper': 0.098}
otrd_3160_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRD', 'xaper': 0.098, 'yaper': 0.098}
vcst98t98y_3166_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST98T98Y', 'xaper': 0.04, 'yaper': 0.098}
mbv_3167a_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.098}
mbv_3167d_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.098}
mbv_3170a_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MARK', 'class': 'BENDIN', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.098}
mbv_3170d_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'MARK', 'class': 'BENDOUT', 'type': 'BENDMARK', 'xaper': 0.04, 'yaper': 0.098}
vcst98yt98_3171_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XTD5_006', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST98YT98', 'xaper': 0.098, 'yaper': 0.098}
otrd_3181_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'DIAG', 'class': 'INSTR', 'type': 'OTRD', 'xaper': 0.098, 'yaper': 0.098}
torc_3181_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'DIAG', 'class': 'CM', 'type': 'TORC', 'xaper': 0.098, 'yaper': 0.098}
bhm_3181_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'DIAG', 'class': 'INSTR', 'type': 'BHM', 'xaper': 0.098, 'yaper': 0.098}
vcst98t200_3182_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'VACUUM', 'class': 'VACSTEP', 'type': 'VCST98T200', 'xaper': 0.2, 'yaper': 0.2}
scrw_3186_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'DIAG', 'class': 'INSTR', 'type': 'SCRW', 'xaper': 0.2, 'yaper': 0.2}
duwindow_3186_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'DUMP', 'class': 'DUMP', 'type': 'DUWINDOW', 'xaper': 0.2, 'yaper': 0.2}
duflange_3186_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'DUMP', 'class': 'DUMP', 'type': 'DUFLANGE', 'xaper': 0.2, 'yaper': 0.2}
duconcrete_3187_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'DUMP', 'class': 'DUMP', 'type': 'DUCONCRETE', 'xaper': 0.2, 'yaper': 0.2}
duabsorb_3189_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'DUMP', 'class': 'DUMP', 'type': 'DUABSORB', 'xaper': 0.2, 'yaper': 0.2}
ensub_3189_t5d.metadata = {'section': 'T5D', 'subsection': 'T5DT', 'cad_room': 'XSDU1_000', 'group': 'MARK', 'class': 'MARK', 'type': 'ENSUB', 'xaper': 0.2, 'yaper': 0.2}
# fmt: on
