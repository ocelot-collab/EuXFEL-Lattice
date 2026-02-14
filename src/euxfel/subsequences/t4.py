# Converted from component_list_2026.01.21.xls @ 2026-02-14T21:25:01.867407

from ocelot.cpbd.elements import (
    Drift,
    Hcor,
    Marker,
    Monitor,
    Quadrupole,
    SBend,
    Sextupole,
    Undulator,
    Vcor,
)
from ocelot.cpbd.beam import Twiss

twiss0 = Twiss()
twiss0.E = 14.0
twiss0.alpha_x = -0.8336
twiss0.alpha_y = 1.2176
twiss0.beta_x = 26.0188
twiss0.beta_y = 38.1166


# Drifts:
vcst10t22_2461_t4 = Drift(eid="VCST10T22.2461.T4")
d_0 = Drift(l=0.2580000000002656, eid="D_0")
d_1 = Drift(l=0.041999999999916326, eid="D_1")
vcst22t40_2461_t4 = Drift(eid="VCST22T40.2461.T4")
d_2 = Drift(l=1.080500000000029, eid="D_2")
d_3 = Drift(l=5.677999999999884, eid="D_3")
d_4 = Drift(l=0.205000000000382, eid="D_4")
d_5 = Drift(l=0.1399999999996544, eid="D_5")
d_6 = Drift(l=11.925000000000091, eid="D_6")
d_7 = Drift(l=0.20499999999992724, eid="D_7")
d_8 = Drift(l=0.1399999999996544, eid="D_8")
d_9 = Drift(l=11.925000000000546, eid="D_9")
d_10 = Drift(l=0.20499999999992724, eid="D_10")
d_11 = Drift(l=0.1399999999996544, eid="D_11")
d_12 = Drift(l=0.6160000000003493, eid="D_12")
d_13 = Drift(l=11.308999999999742, eid="D_13")
d_14 = Drift(l=0.205000000000382, eid="D_14")
d_15 = Drift(l=0.1399999999996544, eid="D_15")
d_16 = Drift(l=11.074999999999728, eid="D_16")
d_17 = Drift(l=1.0145000000001345, eid="D_17")
d_18 = Drift(l=0.3410000000002583, eid="D_18")
d_19 = Drift(l=1.0144999999996798, eid="D_19")
d_20 = Drift(l=3.1649999999999636, eid="D_20")
d_21 = Drift(l=0.20499999999992724, eid="D_21")
d_22 = Drift(l=0.1399999999996544, eid="D_22")
d_23 = Drift(l=21.065000000000417, eid="D_23")
d_24 = Drift(l=0.20499999999992724, eid="D_24")
d_25 = Drift(l=0.1399999999996544, eid="D_25")
d_26 = Drift(l=18.720000000000617, eid="D_26")
d_27 = Drift(l=0.2104500000000371, eid="D_27")
d_28 = Drift(l=0.1554499999999448, eid="D_28")
d_29 = Drift(l=1.544999999999891, eid="D_29")
d_30 = Drift(l=0.2104500000000371, eid="D_30")
d_31 = Drift(l=0.1554499999999448, eid="D_31")
d_32 = Drift(l=9.060000000000219, eid="D_32")
d_33 = Drift(l=0.18499999999976352, eid="D_33")
d_34 = Drift(l=0.18999999999987266, eid="D_34")
d_35 = Drift(l=0.2104500000000371, eid="D_35")
d_36 = Drift(l=0.135449999999963, eid="D_36")
vcst40t93x_2583_t4 = Drift(eid="VCST40T93X.2583.T4")
d_37 = Drift(l=0.25, eid="D_37")
d_38 = Drift(l=7.000000096013537e-06, eid="D_38")
d_39 = Drift(l=7.000000096013537e-06, eid="D_39")
vcst93xt40_2585_t4 = Drift(eid="VCST93XT40.2585.T4")
d_40 = Drift(l=1.0701500000000124, eid="D_40")
d_41 = Drift(l=3.5951499999998964, eid="D_41")
d_42 = Drift(l=0.3451500000001033, eid="D_42")
d_43 = Drift(l=0.2901500000000603, eid="D_43")
d_44 = Drift(l=0.6717999999998938, eid="D_44")
d_45 = Drift(l=2.1167999999999427, eid="D_45")
d_46 = Drift(l=0.3451500000001033, eid="D_46")
d_47 = Drift(l=0.2901500000000603, eid="D_47")
d_48 = Drift(l=1.3217999999999848, eid="D_48")
d_49 = Drift(l=1.0767999999999789, eid="D_49")
d_50 = Drift(l=0.18999999999987266, eid="D_50")
d_51 = Drift(l=0.3451500000001033, eid="D_51")
d_52 = Drift(l=0.3698979999997143, eid="D_52")
d_53 = Drift(l=0.0002660000000105356, eid="D_53")
d_54 = Drift(l=0.875, eid="D_54")
d_55 = Drift(l=0.2104500000000371, eid="D_55")
d_56 = Drift(l=0.15545000000039955, eid="D_56")
d_57 = Drift(l=9.834999999999855, eid="D_57")
d_58 = Drift(l=0.2104500000000371, eid="D_58")
d_59 = Drift(l=0.1554499999999448, eid="D_59")
d_60 = Drift(l=1.544999999999891, eid="D_60")
d_61 = Drift(l=0.2104500000000371, eid="D_61")
d_62 = Drift(l=0.1554499999999448, eid="D_62")
d_63 = Drift(l=18.609999999999946, eid="D_63")
d_64 = Drift(l=0.20499999999992724, eid="D_64")
d_65 = Drift(l=0.14000000000010915, eid="D_65")
d_66 = Drift(l=21.064999999999962, eid="D_66")
d_67 = Drift(l=0.20499999999992724, eid="D_67")
d_68 = Drift(l=0.14000000000010915, eid="D_68")
d_69 = Drift(l=21.064999999999962, eid="D_69")
d_70 = Drift(l=0.20499999999992724, eid="D_70")
d_71 = Drift(l=0.14000000000010915, eid="D_71")
d_72 = Drift(l=21.064999999999962, eid="D_72")
d_73 = Drift(l=0.20499999999992724, eid="D_73")
d_74 = Drift(l=0.14000000000010915, eid="D_74")
d_75 = Drift(l=10.789999999999873, eid="D_75")
d_76 = Drift(l=10.275000000000091, eid="D_76")
d_77 = Drift(l=0.20499999999992724, eid="D_77")
d_78 = Drift(l=0.14000000000010915, eid="D_78")
d_79 = Drift(l=20.16499999999987, eid="D_79")
d_80 = Drift(l=0.20894999999973152, eid="D_80")
d_81 = Drift(l=0.15395000000025028, eid="D_81")
d_82 = Drift(l=5.479999999999928, eid="D_82")
d_83 = Drift(l=5.525000000000091, eid="D_83")
d_84 = Drift(l=0.20894999999973152, eid="D_84")
d_85 = Drift(l=0.15395000000025028, eid="D_85")
d_86 = Drift(l=11.005000000000019, eid="D_86")
d_87 = Drift(l=0.20894999999973152, eid="D_87")
d_88 = Drift(l=0.15395000000025028, eid="D_88")
d_89 = Drift(l=5.479999999999928, eid="D_89")
d_90 = Drift(l=5.525000000000091, eid="D_90")
d_91 = Drift(l=0.20894999999973152, eid="D_91")
d_92 = Drift(l=0.15395000000025028, eid="D_92")
d_93 = Drift(l=0.4850000000000364, eid="D_93")
d_94 = Drift(l=1.7549870000002556, eid="D_94")
d_95 = Drift(l=0.6149999999997817, eid="D_95")
vcbshut_2791_t4 = Drift(l=0.3, eid="VCBSHUT.2791.T4")
d_96 = Drift(l=1.9357130000000324, eid="D_96")
d_97 = Drift(l=0.60674999999992, eid="D_97")
vcst40t10_2793_t4 = Drift(eid="VCST40T10.2793.T4")
d_98 = Drift(l=0.19975000000022192, eid="D_98")
d_99 = Drift(l=0.2181500000001506, eid="D_99")
d_100 = Drift(l=0.17814999999961292, eid="D_100")
d_101 = Drift(l=0.1250000000001819, eid="D_101")
d_102 = Drift(l=2.167499999999927, eid="D_102")
d_103 = Drift(l=1.8266999999999642, eid="D_103")
d_104 = Drift(l=0.1499999999998181, eid="D_104")
d_105 = Drift(l=0.20999999999994542, eid="D_105")
absp_2800_t4 = Drift(l=0.05, eid="ABSP.2800.T4")
d_106 = Drift(l=0.17230000000035944, eid="D_106")
d_107 = Drift(l=0.18665000000009968, eid="D_107")
d_108 = Drift(l=0.04014999999969296, eid="D_108")

# Quadrupoles:
qe_2468_t4 = Quadrupole(l=0.24, k1=0.2237922517, eid="QE.2468.T4")
qe_2481_t4 = Quadrupole(l=0.24, k1=-0.2040914524, eid="QE.2481.T4")
qe_2493_t4 = Quadrupole(l=0.24, k1=0.24059635850000002, eid="QE.2493.T4")
qe_2506_t4 = Quadrupole(l=0.24, k1=-0.2306597606, eid="QE.2506.T4")
qe_2526_t4 = Quadrupole(l=0.24, k1=0.19227955160000001, eid="QE.2526.T4")
qe_2548_t4 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid="QE.2548.T4")
qh_2567_t4 = Quadrupole(l=1.0291, k1=0.1965315531998834, eid="QH.2567.T4")
qh_2570_t4 = Quadrupole(l=1.0291, k1=-0.19652613830045673, eid="QH.2570.T4")
qh_2582_t4 = Quadrupole(l=1.0291, k1=0.2948896440996988, eid="QH.2582.T4")
qm_2587_t4 = Quadrupole(l=1.0597, k1=-0.2884660775002359, eid="QM.2587.T4")
qm_2592_t4 = Quadrupole(l=1.0597, k1=0.2882291453996414, eid="QM.2592.T4")
qm_2597_t4 = Quadrupole(l=1.0597, k1=-0.2884660775002359, eid="QM.2597.T4")
qm_2602_t4 = Quadrupole(l=1.0597, k1=0.2882291453996414, eid="QM.2602.T4")
qh_2607_t4 = Quadrupole(l=1.0291, k1=-0.29482679030026243, eid="QH.2607.T4")
qh_2618_t4 = Quadrupole(l=1.0291, k1=0.1965315531998834, eid="QH.2618.T4")
qh_2621_t4 = Quadrupole(l=1.0291, k1=-0.19652613830045673, eid="QH.2621.T4")
qe_2641_t4 = Quadrupole(l=0.24, k1=0.19227955160000001, eid="QE.2641.T4")
qe_2663_t4 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid="QE.2663.T4")
qe_2685_t4 = Quadrupole(l=0.24, k1=0.19227955160000001, eid="QE.2685.T4")
qe_2707_t4 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid="QE.2707.T4")
qe_2728_t4 = Quadrupole(l=0.24, k1=0.19227955160000001, eid="QE.2728.T4")
qf_2749_t4 = Quadrupole(l=0.5321, k1=-0.1156016655008457, eid="QF.2749.T4")
qf_2761_t4 = Quadrupole(l=0.5321, k1=0.14754132349934224, eid="QF.2761.T4")
qf_2773_t4 = Quadrupole(l=0.5321, k1=-0.15051305829919187, eid="QF.2773.T4")
qf_2785_t4 = Quadrupole(l=0.5321, k1=0.183637635399361, eid="QF.2785.T4")
qa_2794_t4 = Quadrupole(l=0.1137, k1=-1.1165159440017591, eid="QA.2794.T4")
qa_2800_t4 = Quadrupole(l=0.1137, k1=1.2439009670008796, eid="QA.2800.T4")

# SBends:
bt_2518_t4 = SBend(l=0.6, eid="BT.2518.T4")
bt_2519_t4 = SBend(l=0.6, eid="BT.2519.T4")
bt_2520_t4 = SBend(l=0.6, eid="BT.2520.T4")
bt_2522_t4 = SBend(l=0.6, eid="BT.2522.T4")
be_2584_t4 = SBend(
    l=2.5, angle=0.0115035, e1=0.00575175, e2=0.00575175, eid="BE.2584.T4"
)
be_2604_t4 = SBend(
    l=2.5, angle=0.0115035, e1=0.00575175, e2=0.00575175, eid="BE.2604.T4"
)

# Sextupoles:
saox_2594_t4 = Sextupole(l=0.3164, k2=23.92225032, eid="SAOX.2594.T4")
saox_2599_t4 = Sextupole(l=0.3164, k2=8.44816687700063, eid="SAOX.2599.T4")

# Hcors:
cex_2469_t4 = Hcor(l=0.1, eid="CEX.2469.T4")
cex_2494_t4 = Hcor(l=0.1, eid="CEX.2494.T4")
cbt_2522_t4 = Hcor(eid="CBT.2522.T4")
cex_2526_t4 = Hcor(l=0.1, eid="CEX.2526.T4")
chx_2568_t4 = Hcor(l=0.2, eid="CHX.2568.T4")
chx_2581_t4 = Hcor(l=0.2, eid="CHX.2581.T4")
chx_2593_t4 = Hcor(l=0.2, eid="CHX.2593.T4")
chx_2601_t4 = Hcor(l=0.2, eid="CHX.2601.T4")
chx_2619_t4 = Hcor(l=0.2, eid="CHX.2619.T4")
cex_2642_t4 = Hcor(l=0.1, eid="CEX.2642.T4")
cex_2685_t4 = Hcor(l=0.1, eid="CEX.2685.T4")
cex_2729_t4 = Hcor(l=0.1, eid="CEX.2729.T4")
cfx_2762_t4 = Hcor(l=0.1, eid="CFX.2762.T4")
cfx_2786_t4 = Hcor(l=0.1, eid="CFX.2786.T4")
kspos_2787_t4 = Hcor(l=1.0, eid="KSPOS.2787.T4")
ksneg_2787_t4 = Hcor(l=1.0, eid="KSNEG.2787.T4")
cex_2795_t4 = Hcor(l=0.1, eid="CEX.2795.T4")
cex_2799_t4 = Hcor(l=0.1, eid="CEX.2799.T4")

# Vcors:
cey_2481_t4 = Vcor(l=0.1, eid="CEY.2481.T4")
cey_2506_t4 = Vcor(l=0.1, eid="CEY.2506.T4")
cey_2548_t4 = Vcor(l=0.1, eid="CEY.2548.T4")
chy_2571_t4 = Vcor(l=0.2, eid="CHY.2571.T4")
chy_2581_t4 = Vcor(l=0.2, eid="CHY.2581.T4")
chy_2598_t4 = Vcor(l=0.2, eid="CHY.2598.T4")
chy_2608_t4 = Vcor(l=0.2, eid="CHY.2608.T4")
chy_2622_t4 = Vcor(l=0.2, eid="CHY.2622.T4")
cey_2663_t4 = Vcor(l=0.1, eid="CEY.2663.T4")
cey_2707_t4 = Vcor(l=0.1, eid="CEY.2707.T4")
cfy_2750_t4 = Vcor(l=0.1, eid="CFY.2750.T4")
cfy_2774_t4 = Vcor(l=0.1, eid="CFY.2774.T4")
cny_2794_t4 = Vcor(l=0.3, eid="CNY.2794.T4")
cny_2799_t4 = Vcor(l=0.3, eid="CNY.2799.T4")

# Undulators:
u40s_2797_t4 = Undulator(lperiod=0.04, nperiods=3.0, eid="U40S.2797.T4")

# Monitors:
bpma_2468_t4 = Monitor(eid="BPMA.2468.T4")
bpma_2481_t4 = Monitor(eid="BPMA.2481.T4")
bpma_2493_t4 = Monitor(eid="BPMA.2493.T4")
bpma_2506_t4 = Monitor(eid="BPMA.2506.T4")
bpma_2525_t4 = Monitor(eid="BPMA.2525.T4")
bpma_2547_t4 = Monitor(eid="BPMA.2547.T4")
bpma_2567_t4 = Monitor(eid="BPMA.2567.T4")
bpma_2570_t4 = Monitor(eid="BPMA.2570.T4")
bpma_2581_t4 = Monitor(eid="BPMA.2581.T4")
bpma_2591_t4 = Monitor(eid="BPMA.2591.T4")
bpma_2596_t4 = Monitor(eid="BPMA.2596.T4")
bpma_2601_t4 = Monitor(eid="BPMA.2601.T4")
bpma_2606_t4 = Monitor(eid="BPMA.2606.T4")
bpma_2618_t4 = Monitor(eid="BPMA.2618.T4")
bpma_2621_t4 = Monitor(eid="BPMA.2621.T4")
bpma_2641_t4 = Monitor(eid="BPMA.2641.T4")
bpma_2663_t4 = Monitor(eid="BPMA.2663.T4")
bpma_2684_t4 = Monitor(eid="BPMA.2684.T4")
bpma_2706_t4 = Monitor(eid="BPMA.2706.T4")
bpma_2728_t4 = Monitor(eid="BPMA.2728.T4")
bpma_2749_t4 = Monitor(eid="BPMA.2749.T4")
bpma_2761_t4 = Monitor(eid="BPMA.2761.T4")
bpma_2773_t4 = Monitor(eid="BPMA.2773.T4")
bpma_2785_t4 = Monitor(eid="BPMA.2785.T4")
bpma_2790_t4 = Monitor(eid="BPMA.2790.T4")
bpme_2794_t4 = Monitor(eid="BPME.2794.T4")
bpme_2800_t4 = Monitor(eid="BPME.2800.T4")

# Markers:
stsec_2461_t4 = Marker(eid="STSEC.2461.T4")
stsub_2461_t4 = Marker(eid="STSUB.2461.T4")
bamc_2461_t4 = Marker(eid="BAMC.2461.T4")
tora_2462_t4 = Marker(eid="TORA.2462.T4")
otra_2494_t4 = Marker(eid="OTRA.2494.T4")
t4_csr_start = Marker(eid="t4_csr_start")
ensub_2583_t4 = Marker(eid="ENSUB.2583.T4")
stsub_2583_t4 = Marker(eid="STSUB.2583.T4")
mbe_2584a_t4 = Marker(eid="MBE.2584a.T4")
mbe_2584d_t4 = Marker(eid="MBE.2584d.T4")
mbe_2604d_t4 = Marker(eid="MBE.2604d.T4")
t4_csr_stop = Marker(eid="t4_csr_stop")
otrbw_2718_t4 = Marker(eid="OTRBW.2718.T4")
otrbw_2755_t4 = Marker(eid="OTRBW.2755.T4")
otrbw_2779_t4 = Marker(eid="OTRBW.2779.T4")
ks_2787_t4 = Marker(eid="KS.2787.T4")
tora_2793_t4 = Marker(eid="TORA.2793.T4")
ensub_2800_t4 = Marker(eid="ENSUB.2800.T4")
ensec_2800_t4 = Marker(eid="ENSEC.2800.T4")

# Sequence:
cell = (
    stsec_2461_t4,
    stsub_2461_t4,
    vcst10t22_2461_t4,
    d_0,
    bamc_2461_t4,
    d_1,
    vcst22t40_2461_t4,
    d_2,
    tora_2462_t4,
    d_3,
    bpma_2468_t4,
    d_4,
    qe_2468_t4,
    d_5,
    cex_2469_t4,
    d_6,
    bpma_2481_t4,
    d_7,
    qe_2481_t4,
    d_8,
    cey_2481_t4,
    d_9,
    bpma_2493_t4,
    d_10,
    qe_2493_t4,
    d_11,
    cex_2494_t4,
    d_12,
    otra_2494_t4,
    d_13,
    bpma_2506_t4,
    d_14,
    qe_2506_t4,
    d_15,
    cey_2506_t4,
    d_16,
    bt_2518_t4,
    d_17,
    bt_2519_t4,
    d_18,
    bt_2520_t4,
    d_19,
    bt_2522_t4,
    cbt_2522_t4,
    d_20,
    bpma_2525_t4,
    d_21,
    qe_2526_t4,
    d_22,
    cex_2526_t4,
    d_23,
    bpma_2547_t4,
    d_24,
    qe_2548_t4,
    d_25,
    cey_2548_t4,
    d_26,
    bpma_2567_t4,
    d_27,
    qh_2567_t4,
    d_28,
    chx_2568_t4,
    d_29,
    bpma_2570_t4,
    d_30,
    qh_2570_t4,
    d_31,
    chy_2571_t4,
    d_32,
    chx_2581_t4,
    d_33,
    chy_2581_t4,
    d_34,
    bpma_2581_t4,
    d_35,
    qh_2582_t4,
    t4_csr_start,
    d_36,
    vcst40t93x_2583_t4,
    d_37,
    ensub_2583_t4,
    stsub_2583_t4,
    mbe_2584a_t4,
    d_38,
    be_2584_t4,
    d_39,
    mbe_2584d_t4,
    vcst93xt40_2585_t4,
    d_40,
    qm_2587_t4,
    d_41,
    bpma_2591_t4,
    d_42,
    qm_2592_t4,
    d_43,
    chx_2593_t4,
    d_44,
    saox_2594_t4,
    d_45,
    bpma_2596_t4,
    d_46,
    qm_2597_t4,
    d_47,
    chy_2598_t4,
    d_48,
    saox_2599_t4,
    d_49,
    chx_2601_t4,
    d_50,
    bpma_2601_t4,
    d_51,
    qm_2602_t4,
    d_52,
    be_2604_t4,
    d_53,
    mbe_2604d_t4,
    d_54,
    bpma_2606_t4,
    t4_csr_stop,
    d_55,
    qh_2607_t4,
    d_56,
    chy_2608_t4,
    d_57,
    bpma_2618_t4,
    d_58,
    qh_2618_t4,
    d_59,
    chx_2619_t4,
    d_60,
    bpma_2621_t4,
    d_61,
    qh_2621_t4,
    d_62,
    chy_2622_t4,
    d_63,
    bpma_2641_t4,
    d_64,
    qe_2641_t4,
    d_65,
    cex_2642_t4,
    d_66,
    bpma_2663_t4,
    d_67,
    qe_2663_t4,
    d_68,
    cey_2663_t4,
    d_69,
    bpma_2684_t4,
    d_70,
    qe_2685_t4,
    d_71,
    cex_2685_t4,
    d_72,
    bpma_2706_t4,
    d_73,
    qe_2707_t4,
    d_74,
    cey_2707_t4,
    d_75,
    otrbw_2718_t4,
    d_76,
    bpma_2728_t4,
    d_77,
    qe_2728_t4,
    d_78,
    cex_2729_t4,
    d_79,
    bpma_2749_t4,
    d_80,
    qf_2749_t4,
    d_81,
    cfy_2750_t4,
    d_82,
    otrbw_2755_t4,
    d_83,
    bpma_2761_t4,
    d_84,
    qf_2761_t4,
    d_85,
    cfx_2762_t4,
    d_86,
    bpma_2773_t4,
    d_87,
    qf_2773_t4,
    d_88,
    cfy_2774_t4,
    d_89,
    otrbw_2779_t4,
    d_90,
    bpma_2785_t4,
    d_91,
    qf_2785_t4,
    d_92,
    cfx_2786_t4,
    d_93,
    kspos_2787_t4,
    ks_2787_t4,
    ksneg_2787_t4,
    d_94,
    bpma_2790_t4,
    d_95,
    vcbshut_2791_t4,
    d_96,
    tora_2793_t4,
    d_97,
    vcst40t10_2793_t4,
    d_98,
    bpme_2794_t4,
    d_99,
    qa_2794_t4,
    d_100,
    cny_2794_t4,
    d_101,
    cex_2795_t4,
    d_102,
    u40s_2797_t4,
    d_103,
    cny_2799_t4,
    d_104,
    cex_2799_t4,
    d_105,
    absp_2800_t4,
    d_106,
    bpme_2800_t4,
    d_107,
    qa_2800_t4,
    d_108,
    ensub_2800_t4,
    ensec_2800_t4,
)

# Power Supply IDs:
# Quadrupole power supplies:
qe_2468_t4.ps_id = "QE.3.T4"
qe_2481_t4.ps_id = "QE.4.T4"
qe_2493_t4.ps_id = "QE.5.T4"
qe_2506_t4.ps_id = "QE.6.T4"
qe_2526_t4.ps_id = "QE.2.T4"
qe_2548_t4.ps_id = "QE.1.T4"
qh_2567_t4.ps_id = "QH.4.T4"
qh_2570_t4.ps_id = "QH.3.T4"
qh_2582_t4.ps_id = "QH.1.T4"
qm_2587_t4.ps_id = "QM.2.T4"
qm_2592_t4.ps_id = "QM.1.T4"
qm_2597_t4.ps_id = "QM.2.T4"
qm_2602_t4.ps_id = "QM.1.T4"
qh_2607_t4.ps_id = "QH.2.T4"
qh_2618_t4.ps_id = "QH.4.T4"
qh_2621_t4.ps_id = "QH.3.T4"
qe_2641_t4.ps_id = "QE.2.T4"
qe_2663_t4.ps_id = "QE.1.T4"
qe_2685_t4.ps_id = "QE.2.T4"
qe_2707_t4.ps_id = "QE.1.T4"
qe_2728_t4.ps_id = "QE.2.T4"
qf_2749_t4.ps_id = "QF.7.T4"
qf_2761_t4.ps_id = "QF.8.T4"
qf_2773_t4.ps_id = "QF.9.T4"
qf_2785_t4.ps_id = "QF.10.T4"
qa_2794_t4.ps_id = "QA.3.T4"
qa_2800_t4.ps_id = "QA.4.T4"

# SBend power supplies:
bt_2518_t4.ps_id = "BT.1.T4"
bt_2519_t4.ps_id = "BT.1.T4"
bt_2520_t4.ps_id = "BT.1.T4"
bt_2522_t4.ps_id = "BT.1.T4"
be_2584_t4.ps_id = "BE.1.T4"
be_2604_t4.ps_id = "BE.1.T4"

# Sextupole power supplies:
saox_2594_t4.ps_id = "SAOX.1.T4"
saox_2599_t4.ps_id = "SAOX.2.T4"
