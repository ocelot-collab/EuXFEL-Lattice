from ocelot import *

twiss0 = Twiss()
twiss0._E = 14.0
twiss0._beta_x = 41.2014
twiss0._beta_y = 47.773
twiss0._alpha_x = -1.063
twiss0._alpha_y = 1.2411

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
d_16 = Drift(l=0.5158219999998437, eid="D_16")
d_17 = Drift(l=9.900000031848322e-05, eid="D_17")
d_18 = Drift(l=0.5001979999997275, eid="D_18")
d_19 = Drift(l=1.9300990000001548, eid="D_19")
d_20 = Drift(l=0.14239999999990688, eid="D_20")
d_21 = Drift(l=0.19739999999980218, eid="D_21")
d_22 = Drift(l=0.5535000000004402, eid="D_22")
d_23 = Drift(l=0.9034999999997417, eid="D_23")
d_24 = Drift(l=0.8535000000001673, eid="D_24")
d_25 = Drift(l=0.5534999999998327, eid="D_25")
d_26 = Drift(l=0.197400000000016, eid="D_26")
d_27 = Drift(l=0.1423999999999659, eid="D_27")
d_28 = Drift(l=1.9300989999998819, eid="D_28")
d_29 = Drift(l=0.500199000000066, eid="D_29")
d_30 = Drift(l=0.6117990000002465, eid="D_30")
d_31 = Drift(l=0.16069999999990614, eid="D_31")
d_32 = Drift(l=0.34480000000009103, eid="D_32")
d_33 = Drift(l=0.34480000000009103, eid="D_33")
d_34 = Drift(l=0.34480000000009103, eid="D_34")
d_35 = Drift(l=0.21439999999962756, eid="D_35")
d_36 = Drift(l=0.5579999999999927, eid="D_36")
d_37 = Drift(l=0.49999999999987266, eid="D_37")
d_38 = Drift(l=0.8219999999999891, eid="D_38")
d_39 = Drift(l=0.20000000000027285, eid="D_39")
d_40 = Drift(l=0.4499999999998181, eid="D_40")
d_41 = Drift(l=0.31300000000010186, eid="D_41")
d_42 = Drift(l=3.869999999999891, eid="D_42")
d_43 = Drift(l=0.3223000000002685, eid="D_43")
d_44 = Drift(l=3.9454399999999623, eid="D_44")

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
bv_3151_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3151.T5D")
bv_3154_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3154.T5D")
bv_3167_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3167.T5D")
bv_3170_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3170.T5D")

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
ensub_3149_t5d = Marker(eid="ENSUB.3149.T5D")
stsub_3149_t5d = Marker(eid="STSUB.3149.T5D")
otrd_3160_t5d = Marker(eid="OTRD.3160.T5D")
otrd_3181_t5d = Marker(eid="OTRD.3181.T5D")
torc_3181_t5d = Marker(eid="TORC.3181.T5D")
bhm_3181_t5d = Marker(eid="BHM.3181.T5D")
scrw_3186_t5d = Marker(eid="SCRW.3186.T5D")
ensub_3189_t5d = Marker(eid="ENSUB.3189.T5D")
ensec_3189_t5d = Marker(eid="ENSEC.3189.T5D")

# Sequence:
cell = (stsec_3039_t5d,
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
        ensub_3149_t5d,
        stsub_3149_t5d,
        d_17,
        bv_3151_t5d,
        d_18,
        bv_3154_t5d,
        d_19,
        cnx_3157_t5d,
        d_20,
        qk_3158_t5d,
        d_21,
        bpmd_3159_t5d,
        d_22,
        sk_3159_t5d,
        d_23,
        otrd_3160_t5d,
        d_24,
        sk_3161_t5d,
        d_25,
        bpmd_3162_t5d,
        d_26,
        qk_3163_t5d,
        d_27,
        cny_3164_t5d,
        d_28,
        bv_3167_t5d,
        d_29,
        bv_3170_t5d,
        d_30,
        bpmd_3172_t5d,
        d_31,
        qk_3172_t5d,
        d_32,
        qk_3174_t5d,
        d_33,
        qk_3175_t5d,
        d_34,
        qk_3177_t5d,
        d_35,
        bpmd_3177_t5d,
        d_36,
        sweep_3178_t5d,
        d_37,
        sweep_3179_t5d,
        d_38,
        bpmd_3180_t5d,
        d_39,
        otrd_3181_t5d,
        d_40,
        torc_3181_t5d,
        d_41,
        bhm_3181_t5d,
        d_42,
        bpmw_3185_t5d,
        d_43,
        scrw_3186_t5d,
        d_44,
        ensub_3189_t5d,
        ensec_3189_t5d)

# Power Supply IDs:
