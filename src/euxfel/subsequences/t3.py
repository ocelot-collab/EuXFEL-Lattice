from ocelot import *

twiss0 = Twiss()
twiss0._E = 14.0
twiss0._beta_x = 25.586
twiss0._beta_y = 38.9113
twiss0._alpha_x = -0.854
twiss0._alpha_y = 1.242



# Drifts:
d_0 = Drift(l=0.2579999999998108, eid="D_0")
d_1 = Drift(l=1.4725000000003092, eid="D_1")
d_2 = Drift(l=1.3099999999999454, eid="D_2")
d_3 = Drift(l=0.22999999999974535, eid="D_3")
d_4 = Drift(l=2.920000000000255, eid="D_4")
d_5 = Drift(l=0.20499999999992724, eid="D_5")
d_6 = Drift(l=0.1399999999996544, eid="D_6")
d_7 = Drift(l=5.0300000000001095, eid="D_7")
d_8 = Drift(l=0.9415000000000873, eid="D_8")
d_9 = Drift(l=6.0, eid="D_9")
d_10 = Drift(l=2.5465000000003783, eid="D_10")
d_11 = Drift(l=0.09999999999969078, eid="D_11")
d_12 = Drift(l=10.22500000000009, eid="D_12")
d_13 = Drift(l=0.20499999999992724, eid="D_13")
d_14 = Drift(l=0.1399999999996544, eid="D_14")
d_15 = Drift(l=0.33000000000029106, eid="D_15")
d_16 = Drift(l=9.759999999999945, eid="D_16")
d_17 = Drift(l=0.205000000000382, eid="D_17")
d_18 = Drift(l=0.1399999999996544, eid="D_18")
d_19 = Drift(l=10.340000000000055, eid="D_19")
d_20 = Drift(l=0.2104500000000371, eid="D_20")
d_21 = Drift(l=0.1554499999999448, eid="D_21")
d_22 = Drift(l=1.544999999999891, eid="D_22")
d_23 = Drift(l=0.21045000000049185, eid="D_23")
d_24 = Drift(l=0.1554499999999448, eid="D_24")
d_25 = Drift(l=9.059999999999764, eid="D_25")
d_26 = Drift(l=0.18500000000021827, eid="D_26")
d_27 = Drift(l=0.1819999999996071, eid="D_27")
d_28 = Drift(l=0.21845000000030268, eid="D_28")
d_29 = Drift(l=0.385449999999963, eid="D_29")
d_30 = Drift(l=2.499999982319423e-05, eid="D_30")
d_31 = Drift(l=1.0701750000002903, eid="D_31")
d_32 = Drift(l=3.5951499999998964, eid="D_32")
d_33 = Drift(l=0.3451500000001033, eid="D_33")
d_34 = Drift(l=0.2901500000000603, eid="D_34")
d_35 = Drift(l=0.6717999999998938, eid="D_35")
d_36 = Drift(l=2.1167999999999427, eid="D_36")
d_37 = Drift(l=0.3451500000001033, eid="D_37")
d_38 = Drift(l=0.2901500000000603, eid="D_38")
d_39 = Drift(l=0.8899999999996908, eid="D_39")
d_40 = Drift(l=0.43180000000029395, eid="D_40")
d_41 = Drift(l=1.0767999999999789, eid="D_41")
d_42 = Drift(l=0.18999999999987266, eid="D_42")
d_43 = Drift(l=0.3451500000001033, eid="D_43")
d_44 = Drift(l=0.37017499999981074, eid="D_44")
d_45 = Drift(l=0.8750249999998232, eid="D_45")
d_46 = Drift(l=0.21045000000049185, eid="D_46")
d_47 = Drift(l=0.1554499999999448, eid="D_47")
d_48 = Drift(l=9.834999999999855, eid="D_48")
d_49 = Drift(l=0.2104500000000371, eid="D_49")
d_50 = Drift(l=0.1554499999999448, eid="D_50")
d_51 = Drift(l=1.544999999999891, eid="D_51")
d_52 = Drift(l=0.2104500000000371, eid="D_52")
d_53 = Drift(l=0.1554499999999448, eid="D_53")
d_54 = Drift(l=18.609999999999946, eid="D_54")
d_55 = Drift(l=0.205000000000382, eid="D_55")
d_56 = Drift(l=0.1399999999996544, eid="D_56")
d_57 = Drift(l=21.064999999999962, eid="D_57")
d_58 = Drift(l=0.205000000000382, eid="D_58")
d_59 = Drift(l=0.1399999999996544, eid="D_59")
d_60 = Drift(l=21.064999999999962, eid="D_60")
d_61 = Drift(l=0.205000000000382, eid="D_61")
d_62 = Drift(l=0.1399999999996544, eid="D_62")
d_63 = Drift(l=21.064999999999962, eid="D_63")
d_64 = Drift(l=0.205000000000382, eid="D_64")
d_65 = Drift(l=0.1399999999996544, eid="D_65")
d_66 = Drift(l=13.515000000000237, eid="D_66")
d_67 = Drift(l=0.39099999999962165, eid="D_67")
d_68 = Drift(l=7.139000000000124, eid="D_68")
d_69 = Drift(l=0.205000000000382, eid="D_69")
d_70 = Drift(l=0.1399999999996544, eid="D_70")
d_71 = Drift(l=21.064999999999962, eid="D_71")
d_72 = Drift(l=0.205000000000382, eid="D_72")
d_73 = Drift(l=0.1399999999996544, eid="D_73")
d_74 = Drift(l=21.064999999999962, eid="D_74")
d_75 = Drift(l=0.205000000000382, eid="D_75")
d_76 = Drift(l=0.1399999999996544, eid="D_76")
d_77 = Drift(l=9.67599999999984, eid="D_77")

# Quadrupoles:
qe_2480_t3 = Quadrupole(l=0.24, k1=0.2169588756, eid="QE.2480.T3")
qe_2495_t3 = Quadrupole(l=0.24, k1=-0.201978927, eid="QE.2495.T3")
qe_2506_t3 = Quadrupole(l=0.24, k1=0.2470554674, eid="QE.2506.T3")
qe_2518_t3 = Quadrupole(l=0.24, k1=-0.25202719170000004, eid="QE.2518.T3")
qh_2529_t3 = Quadrupole(l=1.0291, k1=0.20047962199980568, eid="QH.2529.T3")
qh_2532_t3 = Quadrupole(l=1.0291, k1=-0.19285370480031097, eid="QH.2532.T3")
qh_2544_t3 = Quadrupole(l=1.0291, k1=0.29487653610047615, eid="QH.2544.T3")
qm_2549_t3 = Quadrupole(l=1.0597, k1=-0.28678140370010374, eid="QM.2549.T3")
qm_2554_t3 = Quadrupole(l=1.0597, k1=0.2879068968000377, eid="QM.2554.T3")
qm_2559_t3 = Quadrupole(l=1.0597, k1=-0.28678140370010374, eid="QM.2559.T3")
qm_2564_t3 = Quadrupole(l=1.0597, k1=0.2879068968000377, eid="QM.2564.T3")
qh_2569_t3 = Quadrupole(l=1.0291, k1=-0.2946863598999126, eid="QH.2569.T3")
qh_2580_t3 = Quadrupole(l=1.0291, k1=0.19651887780001945, eid="QH.2580.T3")
qh_2583_t3 = Quadrupole(l=1.0291, k1=-0.19651370810028182, eid="QH.2583.T3")
qe_2603_t3 = Quadrupole(l=0.24, k1=0.19227955160000001, eid="QE.2603.T3")
qe_2625_t3 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid="QE.2625.T3")
qe_2646_t3 = Quadrupole(l=0.24, k1=0.19227955160000001, eid="QE.2646.T3")
qe_2668_t3 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid="QE.2668.T3")
qe_2690_un1 = Quadrupole(l=0.24, k1=0.19227955160000001, eid="QE.2690.UN1")
qe_2712_un1 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid="QE.2712.UN1")
qe_2733_un1 = Quadrupole(l=0.24, k1=0.19227955160000001, eid="QE.2733.UN1")

# SBends:
be_2546_t3 = SBend(l=2.5, angle=0.0218803, e1=0.01094015, e2=0.01094015, eid="BE.2546.T3")
be_2566_t3 = SBend(l=2.5, angle=0.0218803, e1=0.01094015, e2=0.01094015, eid="BE.2566.T3")

# Sextupoles:
saox_2555_t3 = Sextupole(l=0.3164, k2=12.57269279, eid="SAOX.2555.T3")
sao_2561_t3 = Sextupole(l=0.3164, k2=4.465865992000632, eid="SAO.2561.T3")

# Hcors:
cmx_2477_t3 = Hcor(l=0.3, eid="CMX.2477.T3")
cex_2480_t3 = Hcor(l=0.1, eid="CEX.2480.T3")
cex_2507_t3 = Hcor(l=0.1, eid="CEX.2507.T3")
chx_2530_t3 = Hcor(l=0.2, eid="CHX.2530.T3")
chx_2542_t3 = Hcor(l=0.2, eid="CHX.2542.T3")
chx_2554_t3 = Hcor(l=0.2, eid="CHX.2554.T3")
chx_2562_t3 = Hcor(l=0.2, eid="CHX.2562.T3")
chx_2581_t3 = Hcor(l=0.2, eid="CHX.2581.T3")
cex_2603_t3 = Hcor(l=0.1, eid="CEX.2603.T3")
cex_2647_t3 = Hcor(l=0.1, eid="CEX.2647.T3")
cex_2690_un1 = Hcor(l=0.1, eid="CEX.2690.UN1")
cex_2734_un1 = Hcor(l=0.1, eid="CEX.2734.UN1")

# Vcors:
cmy_2476_t3 = Vcor(l=0.3, eid="CMY.2476.T3")
cmy_2486_t3 = Vcor(l=0.3, eid="CMY.2486.T3")
cmy_2496_t3 = Vcor(l=0.3, eid="CMY.2496.T3")
cmy_2507_t3 = Vcor(l=0.3, eid="CMY.2507.T3")
cey_2518_t3 = Vcor(l=0.1, eid="CEY.2518.T3")
chy_2533_t3 = Vcor(l=0.2, eid="CHY.2533.T3")
chy_2543_t3 = Vcor(l=0.2, eid="CHY.2543.T3")
chy_2559_t3 = Vcor(l=0.2, eid="CHY.2559.T3")
chy_2569_t3 = Vcor(l=0.2, eid="CHY.2569.T3")
chy_2584_t3 = Vcor(l=0.2, eid="CHY.2584.T3")
cey_2625_t3 = Vcor(l=0.1, eid="CEY.2625.T3")
cey_2668_t3 = Vcor(l=0.1, eid="CEY.2668.T3")
cey_2712_un1 = Vcor(l=0.1, eid="CEY.2712.UN1")

# Monitors:
bpma_2480_t3 = Monitor(eid="BPMA.2480.T3")
bpma_2487_t3 = Monitor(eid="BPMA.2487.T3")
bpma_2493_t3 = Monitor(eid="BPMA.2493.T3")
bpma_2506_t3 = Monitor(eid="BPMA.2506.T3")
bpma_2517_t3 = Monitor(eid="BPMA.2517.T3")
bpma_2528_t3 = Monitor(eid="BPMA.2528.T3")
bpma_2531_t3 = Monitor(eid="BPMA.2531.T3")
bpma_2543_t3 = Monitor(eid="BPMA.2543.T3")
bpma_2553_t3 = Monitor(eid="BPMA.2553.T3")
bpma_2558_t3 = Monitor(eid="BPMA.2558.T3")
bpma_2563_t3 = Monitor(eid="BPMA.2563.T3")
bpma_2568_t3 = Monitor(eid="BPMA.2568.T3")
bpma_2579_t3 = Monitor(eid="BPMA.2579.T3")
bpma_2582_t3 = Monitor(eid="BPMA.2582.T3")
bpma_2603_t3 = Monitor(eid="BPMA.2603.T3")
bpma_2624_t3 = Monitor(eid="BPMA.2624.T3")
bpma_2646_t3 = Monitor(eid="BPMA.2646.T3")
bpma_2668_t3 = Monitor(eid="BPMA.2668.T3")
bpma_2690_un1 = Monitor(eid="BPMA.2690.UN1")
bpma_2711_un1 = Monitor(eid="BPMA.2711.UN1")
bpma_2733_un1 = Monitor(eid="BPMA.2733.UN1")

# Markers:
stsec_2473_t3 = Marker(eid="STSEC.2473.T3")
stsub_2473_t3 = Marker(eid="STSUB.2473.T3")
bamc_2473_t3 = Marker(eid="BAMC.2473.T3")
tora_2475_t3 = Marker(eid="TORA.2475.T3")
ensub_2544_t3 = Marker(eid="ENSUB.2544.T3")
stsub_2544_t3 = Marker(eid="STSUB.2544.T3")
otrc_2560_t3 = Marker(eid="OTRC.2560.T3")
tora_2682_t3 = Marker(eid="TORA.2682.T3")
ensub_2682_t3 = Marker(eid="ENSUB.2682.T3")
ensec_2682_t3 = Marker(eid="ENSEC.2682.T3")
stsec_2682_un1 = Marker(eid="STSEC.2682.UN1")
ensec_2743_un1 = Marker(eid="ENSEC.2743.UN1")

# Sequence:
cell = (stsec_2473_t3,
        stsub_2473_t3,
        d_0,
        bamc_2473_t3,
        d_1,
        tora_2475_t3,
        d_2,
        cmy_2476_t3,
        d_3,
        cmx_2477_t3,
        d_4,
        bpma_2480_t3,
        d_5,
        qe_2480_t3,
        d_6,
        cex_2480_t3,
        d_7,
        cmy_2486_t3,
        d_8,
        bpma_2487_t3,
        d_9,
        bpma_2493_t3,
        d_10,
        qe_2495_t3,
        d_11,
        cmy_2496_t3,
        d_12,
        bpma_2506_t3,
        d_13,
        qe_2506_t3,
        d_14,
        cex_2507_t3,
        d_15,
        cmy_2507_t3,
        d_16,
        bpma_2517_t3,
        d_17,
        qe_2518_t3,
        d_18,
        cey_2518_t3,
        d_19,
        bpma_2528_t3,
        d_20,
        qh_2529_t3,
        d_21,
        chx_2530_t3,
        d_22,
        bpma_2531_t3,
        d_23,
        qh_2532_t3,
        d_24,
        chy_2533_t3,
        d_25,
        chx_2542_t3,
        d_26,
        chy_2543_t3,
        d_27,
        bpma_2543_t3,
        d_28,
        qh_2544_t3,
        d_29,
        ensub_2544_t3,
        stsub_2544_t3,
        d_30,
        be_2546_t3,
        d_31,
        qm_2549_t3,
        d_32,
        bpma_2553_t3,
        d_33,
        qm_2554_t3,
        d_34,
        chx_2554_t3,
        d_35,
        saox_2555_t3,
        d_36,
        bpma_2558_t3,
        d_37,
        qm_2559_t3,
        d_38,
        chy_2559_t3,
        d_39,
        otrc_2560_t3,
        d_40,
        sao_2561_t3,
        d_41,
        chx_2562_t3,
        d_42,
        bpma_2563_t3,
        d_43,
        qm_2564_t3,
        d_44,
        be_2566_t3,
        d_45,
        bpma_2568_t3,
        d_46,
        qh_2569_t3,
        d_47,
        chy_2569_t3,
        d_48,
        bpma_2579_t3,
        d_49,
        qh_2580_t3,
        d_50,
        chx_2581_t3,
        d_51,
        bpma_2582_t3,
        d_52,
        qh_2583_t3,
        d_53,
        chy_2584_t3,
        d_54,
        bpma_2603_t3,
        d_55,
        qe_2603_t3,
        d_56,
        cex_2603_t3,
        d_57,
        bpma_2624_t3,
        d_58,
        qe_2625_t3,
        d_59,
        cey_2625_t3,
        d_60,
        bpma_2646_t3,
        d_61,
        qe_2646_t3,
        d_62,
        cex_2647_t3,
        d_63,
        bpma_2668_t3,
        d_64,
        qe_2668_t3,
        d_65,
        cey_2668_t3,
        d_66,
        tora_2682_t3,
        d_67,
        ensub_2682_t3,
        ensec_2682_t3,
        stsec_2682_un1,
        d_68,
        bpma_2690_un1,
        d_69,
        qe_2690_un1,
        d_70,
        cex_2690_un1,
        d_71,
        bpma_2711_un1,
        d_72,
        qe_2712_un1,
        d_73,
        cey_2712_un1,
        d_74,
        bpma_2733_un1,
        d_75,
        qe_2733_un1,
        d_76,
        cex_2734_un1,
        d_77,
        ensec_2743_un1)

# Power Supply IDs:
# Quadrupole power supplies:
qe_2480_t3.ps_id = "QE.3.T3"
qe_2495_t3.ps_id = "QE.4.T3"
qe_2506_t3.ps_id = "QE.5.T3"
qe_2518_t3.ps_id = "QE.6.T3"
qh_2529_t3.ps_id = "QH.5.T3"
qh_2532_t3.ps_id = "QH.6.T3"
qh_2544_t3.ps_id = "QH.1.T3"
qm_2549_t3.ps_id = "QM.2.T3"
qm_2554_t3.ps_id = "QM.1.T3"
qm_2559_t3.ps_id = "QM.2.T3"
qm_2564_t3.ps_id = "QM.1.T3"
qh_2569_t3.ps_id = "QH.2.T3"
qh_2580_t3.ps_id = "QH.3.T3"
qh_2583_t3.ps_id = "QH.4.T3"
qe_2603_t3.ps_id = "QE.1.T3"
qe_2625_t3.ps_id = "QE.2.T3"
qe_2646_t3.ps_id = "QE.1.T3"
qe_2668_t3.ps_id = "QE.2.T3"
qe_2690_un1.ps_id = "QE.1.UN1"
qe_2712_un1.ps_id = "QE.2.UN1"
qe_2733_un1.ps_id = "QE.1.UN1"

# SBend power supplies:
be_2546_t3.ps_id = "BE.1.T3"
be_2566_t3.ps_id = "BE.1.T3"

# Sextupole power supplies:
saox_2555_t3.ps_id = "SAOX.1.T3"
sao_2561_t3.ps_id = "SAO.2.T3"