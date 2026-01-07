from ocelot import *

twiss0 = Twiss()
twiss0._E = 14.0
twiss0._beta_x = 8.1459
twiss0._beta_y = 26.9484
twiss0._alpha_x = -0.4663
twiss0._alpha_y = 1.7423

# Drifts:
d_0 = Drift(l=0.2579999999998108, eid="D_0")
d_1 = Drift(l=6.570000000000164, eid="D_1")
d_2 = Drift(l=0.20894999999973152, eid="D_2")
d_3 = Drift(l=0.15394999999979553, eid="D_3")
d_4 = Drift(l=3.929500000000098, eid="D_4")
d_5 = Drift(l=2.475500000000011, eid="D_5")
d_6 = Drift(l=0.20895000000018626, eid="D_6")
d_7 = Drift(l=0.15394999999979553, eid="D_7")
d_8 = Drift(l=6.4050000000001095, eid="D_8")
d_9 = Drift(l=0.20894999999973152, eid="D_9")
d_10 = Drift(l=0.15395000000025028, eid="D_10")
d_11 = Drift(l=4.630000000000291, eid="D_11")
d_12 = Drift(l=0.20894999999973152, eid="D_12")
d_13 = Drift(l=0.15394999999979553, eid="D_13")
d_14 = Drift(l=2.3900000000000547, eid="D_14")
d_15 = Drift(l=0.148949999999968, eid="D_15")
d_16 = Drift(l=0.2139500000001957, eid="D_16")
d_17 = Drift(l=17.950000000000273, eid="D_17")
d_18 = Drift(l=0.20894999999973152, eid="D_18")
d_19 = Drift(l=0.15394999999979553, eid="D_19")
d_20 = Drift(l=2.630000000000291, eid="D_20")
d_21 = Drift(l=0.20894999999973152, eid="D_21")
d_22 = Drift(l=0.15395000000025028, eid="D_22")
d_23 = Drift(l=4.6299999999998365, eid="D_23")
d_24 = Drift(l=0.20895000000018626, eid="D_24")
d_25 = Drift(l=0.15394999999979553, eid="D_25")
d_26 = Drift(l=6.205000000000109, eid="D_26")
d_27 = Drift(l=0.20894999999973152, eid="D_27")
d_28 = Drift(l=0.15395000000025028, eid="D_28")
d_29 = Drift(l=34.250600000000034, eid="D_29")
d_30 = Drift(l=0.20894999999973152, eid="D_30")
d_31 = Drift(l=0.15395000000025028, eid="D_31")
d_32 = Drift(l=5.360000000000037, eid="D_32")
d_33 = Drift(l=0.15394999999980427, eid="D_33")
d_34 = Drift(l=0.2639500000003776, eid="D_34")
d_35 = Drift(l=0.09600000000000364, eid="D_35")
d_36 = Drift(l=0.11079999999992651, eid="D_36")
d_37 = Drift(l=0.5389399999999114, eid="D_37")
d_38 = Drift(l=9.899999986373587e-05, eid="D_38")
d_39 = Drift(l=0.5001980000001822, eid="D_39")
d_40 = Drift(l=1.9300989999997, eid="D_40")
d_41 = Drift(l=0.14240000000036163, eid="D_41")
d_42 = Drift(l=0.19739999999980218, eid="D_42")
d_43 = Drift(l=0.5534999999999854, eid="D_43")
d_44 = Drift(l=0.9035000000001965, eid="D_44")
d_45 = Drift(l=0.8535000000001673, eid="D_45")
d_46 = Drift(l=0.5534999999998327, eid="D_46")
d_47 = Drift(l=0.197400000000016, eid="D_47")
d_48 = Drift(l=0.1423999999999659, eid="D_48")
d_49 = Drift(l=1.9300989999998819, eid="D_49")
d_50 = Drift(l=0.500199000000066, eid="D_50")
d_51 = Drift(l=0.6117989999997917, eid="D_51")
d_52 = Drift(l=0.1607000000003609, eid="D_52")
d_53 = Drift(l=0.34480000000009103, eid="D_53")
d_54 = Drift(l=0.3447999999996363, eid="D_54")
d_55 = Drift(l=0.34480000000009103, eid="D_55")
d_56 = Drift(l=0.2144000000000823, eid="D_56")
d_57 = Drift(l=0.5579999999999927, eid="D_57")
d_58 = Drift(l=0.49999999999987266, eid="D_58")
d_59 = Drift(l=0.8219999999999891, eid="D_59")
d_60 = Drift(l=0.20000000000027285, eid="D_60")
d_61 = Drift(l=0.4499999999998181, eid="D_61")
d_62 = Drift(l=0.31300000000010186, eid="D_62")
d_63 = Drift(l=3.869999999999891, eid="D_63")
d_64 = Drift(l=0.32229999999981374, eid="D_64")
d_65 = Drift(l=3.9454399999999623, eid="D_65")

# Quadrupoles:
qf_2962_t4d = Quadrupole(l=0.5321, k1=0.1712989174008645, eid="QF.2962.T4D")
qf_2970_t4d = Quadrupole(l=0.5321, k1=-0.11021564689907912, eid="QF.2970.T4D")
qf_2977_t4d = Quadrupole(l=0.5321, k1=0.0953482920597632, eid="QF.2977.T4D")
qf_2983_t4d = Quadrupole(l=0.5321, eid="QF.2983.T4D")
qf_2987_t4d = Quadrupole(l=0.5321, eid="QF.2987.T4D")
qf_3006_t4d = Quadrupole(l=0.5321, eid="QF.3006.T4D")
qf_3010_t4d = Quadrupole(l=0.5321, eid="QF.3010.T4D")
qf_3015_t4d = Quadrupole(l=0.5321, eid="QF.3015.T4D")
qf_3023_t4d = Quadrupole(l=0.5321, eid="QF.3023.T4D")
qf_3058_t4d = Quadrupole(l=0.5321, k1=0.1356646570005638, eid="QF.3058.T4D")
qf_3065_t4d = Quadrupole(l=0.5321, k1=-0.080864647870701, eid="QF.3065.T4D")
qk_3074_t4d = Quadrupole(l=1.0552, k1=-0.172994430300417, eid="QK.3074.T4D")
qk_3079_t4d = Quadrupole(l=1.0552, k1=-0.172994430300417, eid="QK.3079.T4D")
qk_3089_t4d = Quadrupole(l=1.0552, k1=-0.1699949051999621, eid="QK.3089.T4D")
qk_3090_t4d = Quadrupole(l=1.0552, k1=-0.1699949051999621, eid="QK.3090.T4D")
qk_3092_t4d = Quadrupole(l=1.0552, k1=-0.1699949051999621, eid="QK.3092.T4D")
qk_3093_t4d = Quadrupole(l=1.0552, k1=-0.1699949051999621, eid="QK.3093.T4D")

# SBends:
bv_3067_t4d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3067.T4D")
bv_3070_t4d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3070.T4D")
bv_3083_t4d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3083.T4D")
bv_3086_t4d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid="BV.3086.T4D")

# RBends:
sweep_3095_t4d = RBend(l=0.64, e1=0.0, e2=0.0, tilt=-1.570796327, eid="SWEEP.3095.T4D")
sweep_3096_t4d = RBend(l=0.64, e1=0.0, e2=0.0, eid="SWEEP.3096.T4D")

# Sextupoles:
sk_3076_t4d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid="SK.3076.T4D")
sk_3078_t4d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid="SK.3078.T4D")

# Hcors:
cfx_2963_t4d = Hcor(l=0.1, eid="CFX.2963.T4D")
cmx_2978_t4d = Hcor(l=0.3, eid="CMX.2978.T4D")
cmx_2986_t4d = Hcor(l=0.3, eid="CMX.2986.T4D")
cmx_3006_t4d = Hcor(l=0.3, eid="CMX.3006.T4D")
cmx_3016_t4d = Hcor(l=0.3, eid="CMX.3016.T4D")
cfx_3059_t4d = Hcor(l=0.1, eid="CFX.3059.T4D")
cnx_3074_t4d = Hcor(l=0.3, eid="CNX.3074.T4D")

# Vcors:
cfy_2970_t4d = Vcor(l=0.1, eid="CFY.2970.T4D")
cmy_2984_t4d = Vcor(l=0.3, eid="CMY.2984.T4D")
cmy_3010_t4d = Vcor(l=0.3, eid="CMY.3010.T4D")
cmy_3023_t4d = Vcor(l=0.3, eid="CMY.3023.T4D")
cfy_3064_t4d = Vcor(l=0.1, eid="CFY.3064.T4D")
cny_3080_t4d = Vcor(l=0.3, eid="CNY.3080.T4D")

# Monitors:
bpma_2962_t4d = Monitor(eid="BPMA.2962.T4D")
bpma_2969_t4d = Monitor(eid="BPMA.2969.T4D")
bpma_2977_t4d = Monitor(eid="BPMA.2977.T4D")
bpma_2983_t4d = Monitor(eid="BPMA.2983.T4D")
bpma_2987_t4d = Monitor(eid="BPMA.2987.T4D")
bpma_3005_t4d = Monitor(eid="BPMA.3005.T4D")
bpma_3009_t4d = Monitor(eid="BPMA.3009.T4D")
bpma_3015_t4d = Monitor(eid="BPMA.3015.T4D")
bpma_3022_t4d = Monitor(eid="BPMA.3022.T4D")
bpma_3058_t4d = Monitor(eid="BPMA.3058.T4D")
bpmf_3065_t4d = Monitor(eid="BPMF.3065.T4D")
bpmd_3075_t4d = Monitor(eid="BPMD.3075.T4D")
bpmd_3079_t4d = Monitor(eid="BPMD.3079.T4D")
bpmd_3088_t4d = Monitor(eid="BPMD.3088.T4D")
bpmd_3094_t4d = Monitor(eid="BPMD.3094.T4D")
bpmd_3097_t4d = Monitor(eid="BPMD.3097.T4D")
bpmw_3102_t4d = Monitor(eid="BPMW.3102.T4D")

# Markers:
stsec_2955_t4d = Marker(eid="STSEC.2955.T4D")
stsub_2955_t4d = Marker(eid="STSUB.2955.T4D")
bamc_2955_t4d = Marker(eid="BAMC.2955.T4D")
tora_2967_t4d = Marker(eid="TORA.2967.T4D")
midbpmf_3065_t4d = Marker(eid="MIDBPMF.3065.T4D")
tora_3065_t4d = Marker(eid="TORA.3065.T4D")
ensub_3066_t4d = Marker(eid="ENSUB.3066.T4D")
stsub_3066_t4d = Marker(eid="STSUB.3066.T4D")
otrcr_3077_t4d = Marker(eid="OTRCR.3077.T4D")
otrd_3097_t4d = Marker(eid="OTRD.3097.T4D")
torc_3098_t4d = Marker(eid="TORC.3098.T4D")
bhm_3098_t4d = Marker(eid="BHM.3098.T4D")
scrw_3102_t4d = Marker(eid="SCRW.3102.T4D")
ensub_3106_t4d = Marker(eid="ENSUB.3106.T4D")
ensec_3106_t4d = Marker(eid="ENSEC.3106.T4D")

# Sequence:
cell = (stsec_2955_t4d,
        stsub_2955_t4d,
        d_0,
        bamc_2955_t4d,
        d_1,
        bpma_2962_t4d,
        d_2,
        qf_2962_t4d,
        d_3,
        cfx_2963_t4d,
        d_4,
        tora_2967_t4d,
        d_5,
        bpma_2969_t4d,
        d_6,
        qf_2970_t4d,
        d_7,
        cfy_2970_t4d,
        d_8,
        bpma_2977_t4d,
        d_9,
        qf_2977_t4d,
        d_10,
        cmx_2978_t4d,
        d_11,
        bpma_2983_t4d,
        d_12,
        qf_2983_t4d,
        d_13,
        cmy_2984_t4d,
        d_14,
        cmx_2986_t4d,
        d_15,
        qf_2987_t4d,
        d_16,
        bpma_2987_t4d,
        d_17,
        bpma_3005_t4d,
        d_18,
        qf_3006_t4d,
        d_19,
        cmx_3006_t4d,
        d_20,
        bpma_3009_t4d,
        d_21,
        qf_3010_t4d,
        d_22,
        cmy_3010_t4d,
        d_23,
        bpma_3015_t4d,
        d_24,
        qf_3015_t4d,
        d_25,
        cmx_3016_t4d,
        d_26,
        bpma_3022_t4d,
        d_27,
        qf_3023_t4d,
        d_28,
        cmy_3023_t4d,
        d_29,
        bpma_3058_t4d,
        d_30,
        qf_3058_t4d,
        d_31,
        cfx_3059_t4d,
        d_32,
        cfy_3064_t4d,
        d_33,
        qf_3065_t4d,
        d_34,
        midbpmf_3065_t4d,
        d_35,
        bpmf_3065_t4d,
        d_36,
        tora_3065_t4d,
        d_37,
        ensub_3066_t4d,
        stsub_3066_t4d,
        d_38,
        bv_3067_t4d,
        d_39,
        bv_3070_t4d,
        d_40,
        cnx_3074_t4d,
        d_41,
        qk_3074_t4d,
        d_42,
        bpmd_3075_t4d,
        d_43,
        sk_3076_t4d,
        d_44,
        otrcr_3077_t4d,
        d_45,
        sk_3078_t4d,
        d_46,
        bpmd_3079_t4d,
        d_47,
        qk_3079_t4d,
        d_48,
        cny_3080_t4d,
        d_49,
        bv_3083_t4d,
        d_50,
        bv_3086_t4d,
        d_51,
        bpmd_3088_t4d,
        d_52,
        qk_3089_t4d,
        d_53,
        qk_3090_t4d,
        d_54,
        qk_3092_t4d,
        d_55,
        qk_3093_t4d,
        d_56,
        bpmd_3094_t4d,
        d_57,
        sweep_3095_t4d,
        d_58,
        sweep_3096_t4d,
        d_59,
        bpmd_3097_t4d,
        d_60,
        otrd_3097_t4d,
        d_61,
        torc_3098_t4d,
        d_62,
        bhm_3098_t4d,
        d_63,
        bpmw_3102_t4d,
        d_64,
        scrw_3102_t4d,
        d_65,
        ensub_3106_t4d,
        ensec_3106_t4d)

# Power Supply IDs:
