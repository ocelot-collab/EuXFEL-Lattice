from ocelot import *

twiss0 = Twiss()
twiss0._E = 14.0
twiss0._beta_x = 49.3586
twiss0._beta_y = 40.0818
twiss0._alpha_x = 1.2634
twiss0._alpha_y = -1.0757

# Drifts:
d_0 = Drift(l=1.0, eid="D_0")
d_1 = Drift(l=11.390000000000327, eid="D_1")
d_2 = Drift(l=0.20499999999992724, eid="D_2")
d_3 = Drift(l=0.1399999999996544, eid="D_3")
d_4 = Drift(l=9.315000000000419, eid="D_4")
d_5 = Drift(l=0.20499999999992724, eid="D_5")
d_6 = Drift(l=0.1399999999996544, eid="D_6")
d_7 = Drift(l=9.315000000000419, eid="D_7")
d_8 = Drift(l=0.20499999999992724, eid="D_8")
d_9 = Drift(l=0.1399999999996544, eid="D_9")
d_10 = Drift(l=9.315000000000419, eid="D_10")
d_11 = Drift(l=0.20499999999992724, eid="D_11")
d_12 = Drift(l=0.1399999999996544, eid="D_12")
d_13 = Drift(l=17.095000000000162, eid="D_13")
d_14 = Drift(l=0.2104500000000371, eid="D_14")
d_15 = Drift(l=0.1554499999999448, eid="D_15")
d_16 = Drift(l=1.5450000000003457, eid="D_16")
d_17 = Drift(l=0.2104500000000371, eid="D_17")
d_18 = Drift(l=0.1554499999999448, eid="D_18")
d_19 = Drift(l=9.059999999999764, eid="D_19")
d_20 = Drift(l=0.18500000000021827, eid="D_20")
d_21 = Drift(l=0.1819999999996071, eid="D_21")
d_22 = Drift(l=0.21845000000030268, eid="D_22")
d_23 = Drift(l=0.385449999999963, eid="D_23")
d_24 = Drift(l=1.5000000075815478e-05, eid="D_24")
d_25 = Drift(l=1.0701650000000882, eid="D_25")
d_26 = Drift(l=3.5951499999998964, eid="D_26")
d_27 = Drift(l=0.3451500000001033, eid="D_27")
d_28 = Drift(l=0.2901500000000603, eid="D_28")
d_29 = Drift(l=0.6717999999998938, eid="D_29")
d_30 = Drift(l=2.1167999999999427, eid="D_30")
d_31 = Drift(l=0.3451500000001033, eid="D_31")
d_32 = Drift(l=0.2901500000000603, eid="D_32")
d_33 = Drift(l=1.3217999999999848, eid="D_33")
d_34 = Drift(l=1.0767999999999789, eid="D_34")
d_35 = Drift(l=0.18999999999987266, eid="D_35")
d_36 = Drift(l=0.3451500000001033, eid="D_36")
d_37 = Drift(l=0.3701649999996086, eid="D_37")
d_38 = Drift(l=0.8750150000000758, eid="D_38")
d_39 = Drift(l=0.2104500000000371, eid="D_39")
d_40 = Drift(l=0.1554499999999448, eid="D_40")
d_41 = Drift(l=9.83500000000031, eid="D_41")
d_42 = Drift(l=0.2104500000000371, eid="D_42")
d_43 = Drift(l=0.1554499999999448, eid="D_43")
d_44 = Drift(l=1.544999999999891, eid="D_44")
d_45 = Drift(l=0.2104500000000371, eid="D_45")
d_46 = Drift(l=0.1554499999999448, eid="D_46")
d_47 = Drift(l=18.609999999999946, eid="D_47")
d_48 = Drift(l=0.20499999999992724, eid="D_48")
d_49 = Drift(l=0.14000000000010915, eid="D_49")
d_50 = Drift(l=21.064999999999962, eid="D_50")
d_51 = Drift(l=0.20499999999992724, eid="D_51")
d_52 = Drift(l=0.14000000000010915, eid="D_52")
d_53 = Drift(l=21.064999999999962, eid="D_53")
d_54 = Drift(l=0.20499999999992724, eid="D_54")
d_55 = Drift(l=0.14000000000010915, eid="D_55")
d_56 = Drift(l=21.60000000000009, eid="D_56")
d_57 = Drift(l=0.1539499999996224, eid="D_57")
d_58 = Drift(l=0.20895000000008657, eid="D_58")
d_59 = Drift(l=1.3250000000002728, eid="D_59")
d_60 = Drift(l=0.1499999999998181, eid="D_60")
d_61 = Drift(l=0.21894999999973153, eid="D_61")
d_62 = Drift(l=0.2089500000005413, eid="D_62")
d_63 = Drift(l=1.4399999999995998, eid="D_63")
d_64 = Drift(l=0.15395000000007714, eid="D_64")
d_65 = Drift(l=0.20895000000008657, eid="D_65")
d_66 = Drift(l=0.8364999999998872, eid="D_66")
d_67 = Drift(l=0.44050000000015643, eid="D_67")
d_68 = Drift(l=2.286000000000058, eid="D_68")
d_69 = Drift(l=1.0529999999998836, eid="D_69")
d_70 = Drift(l=0.20894999999973152, eid="D_70")
d_71 = Drift(l=0.15395000000025028, eid="D_71")
d_72 = Drift(l=1.4400000000002364, eid="D_72")
d_73 = Drift(l=0.20894999999973152, eid="D_73")
d_74 = Drift(l=0.21895000000030485, eid="D_74")
d_75 = Drift(l=0.14999999999987268, eid="D_75")
d_76 = Drift(l=1.325, eid="D_76")
d_77 = Drift(l=0.20894999999973152, eid="D_77")
d_78 = Drift(l=0.15395000000025028, eid="D_78")
d_79 = Drift(l=12.953999999999905, eid="D_79")
d_80 = Drift(l=0.20894999999973152, eid="D_80")
d_81 = Drift(l=0.15395000000025028, eid="D_81")
d_82 = Drift(l=0.8399999999998726, eid="D_82")
d_83 = Drift(l=0.7332599999999729, eid="D_83")
d_84 = Drift(l=7.139000000000124, eid="D_84")
d_85 = Drift(l=0.205000000000382, eid="D_85")
d_86 = Drift(l=0.1399999999996544, eid="D_86")
d_87 = Drift(l=1.103149999999823, eid="D_87")
d_88 = Drift(l=19.96185000000014, eid="D_88")
d_89 = Drift(l=0.205000000000382, eid="D_89")
d_90 = Drift(l=0.1399999999996544, eid="D_90")
d_91 = Drift(l=21.064999999999962, eid="D_91")
d_92 = Drift(l=0.205000000000382, eid="D_92")
d_93 = Drift(l=0.1399999999996544, eid="D_93")
d_94 = Drift(l=9.67599999999984, eid="D_94")

# Quadrupoles:
qe_2756_t5 = Quadrupole(l=0.24, k1=-0.2155167819, eid="QE.2756.T5")
qe_2766_t5 = Quadrupole(l=0.24, k1=0.1255484698, eid="QE.2766.T5")
qe_2776_t5 = Quadrupole(l=0.24, k1=0.133219012, eid="QE.2776.T5")
qe_2786_t5 = Quadrupole(l=0.24, k1=-0.21171532269999999, eid="QE.2786.T5")
qh_2804_t5 = Quadrupole(l=1.0291, k1=0.19652570639976683, eid="QH.2804.T5")
qh_2807_t5 = Quadrupole(l=1.0291, k1=-0.1965228316995433, eid="QH.2807.T5")
qh_2819_t5 = Quadrupole(l=1.0291, k1=0.2948796721999806, eid="QH.2819.T5")
qm_2824_t5 = Quadrupole(l=1.0597, k1=-0.2866762791997735, eid="QM.2824.T5")
qm_2829_t5 = Quadrupole(l=1.0597, k1=0.2878854605001415, eid="QM.2829.T5")
qm_2834_t5 = Quadrupole(l=1.0597, k1=-0.2866762791997735, eid="QM.2834.T5")
qm_2839_t5 = Quadrupole(l=1.0597, k1=0.2878854605001415, eid="QM.2839.T5")
qh_2844_t5 = Quadrupole(l=1.0291, k1=-0.294760129400447, eid="QH.2844.T5")
qh_2855_t5 = Quadrupole(l=1.0291, k1=0.19652570639976683, eid="QH.2855.T5")
qh_2858_t5 = Quadrupole(l=1.0291, k1=-0.1965228316995433, eid="QH.2858.T5")
qe_2878_t5 = Quadrupole(l=0.24, k1=0.19227955160000001, eid="QE.2878.T5")
qe_2900_t5 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid="QE.2900.T5")
qe_2922_t5 = Quadrupole(l=0.24, k1=0.19515670000000002, eid="QE.2922.T5")
qf_2945_t5 = Quadrupole(l=0.5321, k1=-0.44567809999999997, eid="QF.2945.T5")
qe_2947_t5 = Quadrupole(l=0.24, k1=0.49325050000000004, eid="QE.2947.T5")
qf_2948_t5 = Quadrupole(l=0.5321, k1=0.49325050000000004, eid="QF.2948.T5")
qf_2950_t5 = Quadrupole(l=0.5321, k1=-0.448114, eid="QF.2950.T5")
qf_2956_t5 = Quadrupole(l=0.5321, k1=-0.4210365, eid="QF.2956.T5")
qf_2958_t5 = Quadrupole(l=0.5321, k1=0.49188450000000006, eid="QF.2958.T5")
qe_2959_t5 = Quadrupole(l=0.24, k1=0.4918845, eid="QE.2959.T5")
qf_2961_t5 = Quadrupole(l=0.5321, k1=-0.4469194, eid="QF.2961.T5")
qf_2976_t5 = Quadrupole(l=0.5321, k1=0.1004532, eid="QF.2976.T5")
qe_2985_un2 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid="QE.2985.UN2")
qe_3007_un2 = Quadrupole(l=0.24, k1=0.19227955160000001, eid="QE.3007.UN2")
qe_3029_un2 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid="QE.3029.UN2")

# SBends:
be_2821_t5 = SBend(l=2.5, angle=-0.0169497, e1=-0.00847485, e2=-0.00847485, eid="BE.2821.T5")
be_2841_t5 = SBend(l=2.5, angle=-0.0169497, e1=-0.00847485, e2=-0.00847485, eid="BE.2841.T5")

# Sextupoles:
saox_2831_t5 = Sextupole(l=0.3164, k2=-16.23261694, eid="SAOX.2831.T5")
sao_2836_t5 = Sextupole(l=0.3164, k2=-5.755372945998736, eid="SAO.2836.T5")

# Hcors:
cex_2766_t5 = Hcor(l=0.1, eid="CEX.2766.T5")
cex_2776_t5 = Hcor(l=0.1, eid="CEX.2776.T5")
chx_2805_t5 = Hcor(l=0.2, eid="CHX.2805.T5")
chx_2817_t5 = Hcor(l=0.2, eid="CHX.2817.T5")
chx_2830_t5 = Hcor(l=0.2, eid="CHX.2830.T5")
chx_2838_t5 = Hcor(l=0.2, eid="CHX.2838.T5")
chx_2856_t5 = Hcor(l=0.2, eid="CHX.2856.T5")
cex_2879_t5 = Hcor(l=0.1, eid="CEX.2879.T5")
cmx_2922_t5 = Hcor(l=0.3, eid="CMX.2922.T5")
cmx_2947_t5 = Hcor(l=0.3, eid="CMX.2947.T5")
cmx_2959_t5 = Hcor(l=0.3, eid="CMX.2959.T5")
cmx_2976_t5 = Hcor(l=0.3, eid="CMX.2976.T5")
cex_3007_un2 = Hcor(l=0.1, eid="CEX.3007.UN2")

# Vcors:
cey_2756_t5 = Vcor(l=0.1, eid="CEY.2756.T5")
cey_2786_t5 = Vcor(l=0.1, eid="CEY.2786.T5")
chy_2808_t5 = Vcor(l=0.2, eid="CHY.2808.T5")
chy_2818_t5 = Vcor(l=0.2, eid="CHY.2818.T5")
chy_2835_t5 = Vcor(l=0.2, eid="CHY.2835.T5")
chy_2845_t5 = Vcor(l=0.2, eid="CHY.2845.T5")
chy_2859_t5 = Vcor(l=0.2, eid="CHY.2859.T5")
cey_2900_t5 = Vcor(l=0.1, eid="CEY.2900.T5")
cmy_2944_t5 = Vcor(l=0.3, eid="CMY.2944.T5")
cmy_2950_t5 = Vcor(l=0.3, eid="CMY.2950.T5")
cmy_2956_t5 = Vcor(l=0.3, eid="CMY.2956.T5")
cmy_2962_t5 = Vcor(l=0.3, eid="CMY.2962.T5")
cey_2986_un2 = Vcor(l=0.1, eid="CEY.2986.UN2")
cey_3029_un2 = Vcor(l=0.1, eid="CEY.3029.UN2")

# Monitors:
bpma_2756_t5 = Monitor(eid="BPMA.2756.T5")
bpma_2766_t5 = Monitor(eid="BPMA.2766.T5")
bpma_2776_t5 = Monitor(eid="BPMA.2776.T5")
bpma_2786_t5 = Monitor(eid="BPMA.2786.T5")
bpma_2804_t5 = Monitor(eid="BPMA.2804.T5")
bpma_2807_t5 = Monitor(eid="BPMA.2807.T5")
bpma_2818_t5 = Monitor(eid="BPMA.2818.T5")
bpma_2828_t5 = Monitor(eid="BPMA.2828.T5")
bpma_2833_t5 = Monitor(eid="BPMA.2833.T5")
bpma_2838_t5 = Monitor(eid="BPMA.2838.T5")
bpma_2843_t5 = Monitor(eid="BPMA.2843.T5")
bpma_2855_t5 = Monitor(eid="BPMA.2855.T5")
bpma_2858_t5 = Monitor(eid="BPMA.2858.T5")
bpma_2878_t5 = Monitor(eid="BPMA.2878.T5")
bpma_2900_t5 = Monitor(eid="BPMA.2900.T5")
bpma_2921_t5 = Monitor(eid="BPMA.2921.T5")
bpma_2945_t5 = Monitor(eid="BPMA.2945.T5")
bpma_2948_t5 = Monitor(eid="BPMA.2948.T5")
bpma_2951_t5 = Monitor(eid="BPMA.2951.T5")
bpma_2955_t5 = Monitor(eid="BPMA.2955.T5")
bpma_2958_t5 = Monitor(eid="BPMA.2958.T5")
bpma_2961_t5 = Monitor(eid="BPMA.2961.T5")
bpma_2975_t5 = Monitor(eid="BPMA.2975.T5")
bpma_2985_un2 = Monitor(eid="BPMA.2985.UN2")
bpma_3007_un2 = Monitor(eid="BPMA.3007.UN2")
bpma_3028_un2 = Monitor(eid="BPMA.3028.UN2")

# Markers:
stsec_2743_t5 = Marker(eid="STSEC.2743.T5")
stsub_2743_t5 = Marker(eid="STSUB.2743.T5")
tora_2744_t5 = Marker(eid="TORA.2744.T5")
ensub_2820_t5 = Marker(eid="ENSUB.2820.T5")
stsub_2820_t5 = Marker(eid="STSUB.2820.T5")
miral_2952_t5 = Marker(eid="MIRAL.2952.T5")
otrc_2952_t5 = Marker(eid="OTRC.2952.T5")
otrc_2954_t5 = Marker(eid="OTRC.2954.T5")
tora_2977_t5 = Marker(eid="TORA.2977.T5")
ensub_2978_t5 = Marker(eid="ENSUB.2978.T5")
ensec_2978_t5 = Marker(eid="ENSEC.2978.T5")
stsec_2978_un2 = Marker(eid="STSEC.2978.UN2")
otrdp4_2987_un2 = Marker(eid="OTRDP4.2987.UN2")
ensec_3039_un2 = Marker(eid="ENSEC.3039.UN2")

# Sequence:
cell = (stsec_2743_t5,
        stsub_2743_t5,
        d_0,
        tora_2744_t5,
        d_1,
        bpma_2756_t5,
        d_2,
        qe_2756_t5,
        d_3,
        cey_2756_t5,
        d_4,
        bpma_2766_t5,
        d_5,
        qe_2766_t5,
        d_6,
        cex_2766_t5,
        d_7,
        bpma_2776_t5,
        d_8,
        qe_2776_t5,
        d_9,
        cex_2776_t5,
        d_10,
        bpma_2786_t5,
        d_11,
        qe_2786_t5,
        d_12,
        cey_2786_t5,
        d_13,
        bpma_2804_t5,
        d_14,
        qh_2804_t5,
        d_15,
        chx_2805_t5,
        d_16,
        bpma_2807_t5,
        d_17,
        qh_2807_t5,
        d_18,
        chy_2808_t5,
        d_19,
        chx_2817_t5,
        d_20,
        chy_2818_t5,
        d_21,
        bpma_2818_t5,
        d_22,
        qh_2819_t5,
        d_23,
        ensub_2820_t5,
        stsub_2820_t5,
        d_24,
        be_2821_t5,
        d_25,
        qm_2824_t5,
        d_26,
        bpma_2828_t5,
        d_27,
        qm_2829_t5,
        d_28,
        chx_2830_t5,
        d_29,
        saox_2831_t5,
        d_30,
        bpma_2833_t5,
        d_31,
        qm_2834_t5,
        d_32,
        chy_2835_t5,
        d_33,
        sao_2836_t5,
        d_34,
        chx_2838_t5,
        d_35,
        bpma_2838_t5,
        d_36,
        qm_2839_t5,
        d_37,
        be_2841_t5,
        d_38,
        bpma_2843_t5,
        d_39,
        qh_2844_t5,
        d_40,
        chy_2845_t5,
        d_41,
        bpma_2855_t5,
        d_42,
        qh_2855_t5,
        d_43,
        chx_2856_t5,
        d_44,
        bpma_2858_t5,
        d_45,
        qh_2858_t5,
        d_46,
        chy_2859_t5,
        d_47,
        bpma_2878_t5,
        d_48,
        qe_2878_t5,
        d_49,
        cex_2879_t5,
        d_50,
        bpma_2900_t5,
        d_51,
        qe_2900_t5,
        d_52,
        cey_2900_t5,
        d_53,
        bpma_2921_t5,
        d_54,
        qe_2922_t5,
        d_55,
        cmx_2922_t5,
        d_56,
        cmy_2944_t5,
        d_57,
        qf_2945_t5,
        d_58,
        bpma_2945_t5,
        d_59,
        cmx_2947_t5,
        d_60,
        qe_2947_t5,
        d_61,
        qf_2948_t5,
        d_62,
        bpma_2948_t5,
        d_63,
        cmy_2950_t5,
        d_64,
        qf_2950_t5,
        d_65,
        bpma_2951_t5,
        d_66,
        miral_2952_t5,
        d_67,
        otrc_2952_t5,
        d_68,
        otrc_2954_t5,
        d_69,
        bpma_2955_t5,
        d_70,
        qf_2956_t5,
        d_71,
        cmy_2956_t5,
        d_72,
        bpma_2958_t5,
        d_73,
        qf_2958_t5,
        d_74,
        qe_2959_t5,
        d_75,
        cmx_2959_t5,
        d_76,
        bpma_2961_t5,
        d_77,
        qf_2961_t5,
        d_78,
        cmy_2962_t5,
        d_79,
        bpma_2975_t5,
        d_80,
        qf_2976_t5,
        d_81,
        cmx_2976_t5,
        d_82,
        tora_2977_t5,
        d_83,
        ensub_2978_t5,
        ensec_2978_t5,
        stsec_2978_un2,
        d_84,
        bpma_2985_un2,
        d_85,
        qe_2985_un2,
        d_86,
        cey_2986_un2,
        d_87,
        otrdp4_2987_un2,
        d_88,
        bpma_3007_un2,
        d_89,
        qe_3007_un2,
        d_90,
        cex_3007_un2,
        d_91,
        bpma_3028_un2,
        d_92,
        qe_3029_un2,
        d_93,
        cey_3029_un2,
        d_94,
        ensec_3039_un2)

# Power Supply IDs:
