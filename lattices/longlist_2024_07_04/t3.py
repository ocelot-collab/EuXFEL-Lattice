from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 56.797212917921975
tws0.beta_y = 262.99048996645803
tws0.alpha_x = -1.517388900059324
tws0.alpha_y = -2.4145325077606694
tws0.E = 14
tws0.s = 2423.709195000019

# Drifts
id_1843966_ = Drift(l=7.0585, eid='ID_1843966_')
d_4 = Drift(l=0.205, eid='D_4')
d_5 = Drift(l=0.14, eid='D_5')
d_6 = Drift(l=11.925, eid='D_6')
d_8 = Drift(l=0.1, eid='D_8')
id_7434326_ = Drift(l=11.97, eid='ID_7434326_')
d_12 = Drift(l=0.63, eid='D_12')
d_13 = Drift(l=4.82, eid='D_13')
d_14 = Drift(l=6.175, eid='D_14')
d_17 = Drift(l=19.01, eid='D_17')
d_20 = Drift(l=0.33, eid='D_20')
d_21 = Drift(l=20.435, eid='D_21')
d_24 = Drift(l=18.72, eid='D_24')
d_25 = Drift(l=0.21045, eid='D_25')
d_26 = Drift(l=0.15545, eid='D_26')
d_27 = Drift(l=1.545, eid='D_27')
d_30 = Drift(l=9.06, eid='D_30')
d_31 = Drift(l=0.185, eid='D_31')
d_32 = Drift(l=0.182, eid='D_32')
d_33 = Drift(l=0.21845, eid='D_33')
id_55063665_ = Drift(l=0.385475, eid='ID_55063665_')
d_36 = Drift(l=1.070175, eid='D_36')
d_37 = Drift(l=3.59515, eid='D_37')
d_38 = Drift(l=0.34515, eid='D_38')
d_39 = Drift(l=0.29015, eid='D_39')
d_40 = Drift(l=0.6718, eid='D_40')
d_41 = Drift(l=2.1168, eid='D_41')
id_26776011_ = Drift(l=1.3218, eid='ID_26776011_')
d_46 = Drift(l=1.0768, eid='D_46')
d_47 = Drift(l=0.19, eid='D_47')
d_49 = Drift(l=0.370175, eid='D_49')
d_50 = Drift(l=0.875025, eid='D_50')
d_53 = Drift(l=9.835, eid='D_53')
d_59 = Drift(l=18.61, eid='D_59')
d_62 = Drift(l=21.065, eid='D_62')
id_70607298_ = Drift(l=21.045, eid='ID_70607298_')
d_81 = Drift(l=9.676, eid='D_81')

# Quadrupoles
qe_2430_t3 = Quadrupole(l=0.24, k1=0.2237922517, eid='QE.2430.T3')
qe_2443_t3 = Quadrupole(l=0.24, k1=-0.2040914523, eid='QE.2443.T3')
qe_2455_t3 = Quadrupole(l=0.24, k1=0.24059635850000002, eid='QE.2455.T3')
qe_2468_t3 = Quadrupole(l=0.24, k1=-0.23065976070000002, eid='QE.2468.T3')
qe_2487_t3 = Quadrupole(l=0.24, k1=0.19227955160000001, eid='QE.2487.T3')
qe_2509_t3 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid='QE.2509.T3')
qh_2529_t3 = Quadrupole(l=1.0291, k1=0.19651887780001945, eid='QH.2529.T3')
qh_2532_t3 = Quadrupole(l=1.0291, k1=-0.19651370810028182, eid='QH.2532.T3')
qh_2544_t3 = Quadrupole(l=1.0291, k1=0.29487653610047615, eid='QH.2544.T3')
qm_2549_t3 = Quadrupole(l=1.0597, k1=-0.28678140370010374, eid='QM.2549.T3')
qm_2554_t3 = Quadrupole(l=1.0597, k1=0.2879068968000377, eid='QM.2554.T3')
qm_2559_t3 = Quadrupole(l=1.0597, k1=-0.28678140370010374, eid='QM.2559.T3')
qm_2564_t3 = Quadrupole(l=1.0597, k1=0.2879068968000377, eid='QM.2564.T3')
qh_2569_t3 = Quadrupole(l=1.0291, k1=-0.2946863598999126, eid='QH.2569.T3')
qh_2580_t3 = Quadrupole(l=1.0291, k1=0.19651887780001945, eid='QH.2580.T3')
qh_2583_t3 = Quadrupole(l=1.0291, k1=-0.19651370810028182, eid='QH.2583.T3')
qe_2603_t3 = Quadrupole(l=0.24, k1=0.19227955160000001, eid='QE.2603.T3')
qe_2625_t3 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid='QE.2625.T3')
qe_2646_t3 = Quadrupole(l=0.24, k1=0.19227955160000001, eid='QE.2646.T3')
qe_2668_t3 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid='QE.2668.T3')
qe_2690_un1 = Quadrupole(l=0.24, k1=0.19227955160000001, eid='QE.2690.UN1')
qe_2712_un1 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid='QE.2712.UN1')
qe_2733_un1 = Quadrupole(l=0.24, k1=0.19227955160000001, eid='QE.2733.UN1')

# SBends
be_2546_t3 = SBend(l=2.5, angle=0.0218803, e1=0.01094015, e2=0.01094015, eid='BE.2546.T3')
be_2566_t3 = SBend(l=2.5, angle=0.0218803, e1=0.01094015, e2=0.01094015, eid='BE.2566.T3')

# Sextupoles
saox_2555_t3 = Sextupole(l=0.3164, k2=12.57269279, eid='SAOX.2555.T3')
sao_2561_t3 = Sextupole(l=0.3164, k2=4.465865992000632, eid='SAO.2561.T3')

# Hcors
cex_2430_t3 = Hcor(l=0.1, eid='CEX.2430.T3')
cex_2455_t3 = Hcor(l=0.1, eid='CEX.2455.T3')
cex_2488_t3 = Hcor(l=0.1, eid='CEX.2488.T3')
chx_2530_t3 = Hcor(l=0.2, eid='CHX.2530.T3')
chx_2542_t3 = Hcor(l=0.2, eid='CHX.2542.T3')
chx_2554_t3 = Hcor(l=0.2, eid='CHX.2554.T3')
chx_2562_t3 = Hcor(l=0.2, eid='CHX.2562.T3')
chx_2581_t3 = Hcor(l=0.2, eid='CHX.2581.T3')
cex_2603_t3 = Hcor(l=0.1, eid='CEX.2603.T3')
cex_2647_t3 = Hcor(l=0.1, eid='CEX.2647.T3')
cex_2690_un1 = Hcor(l=0.1, eid='CEX.2690.UN1')
cex_2734_un1 = Hcor(l=0.1, eid='CEX.2734.UN1')

# Vcors
cmy_2443_t3 = Vcor(l=0.3, eid='CMY.2443.T3')
cmy_2456_t3 = Vcor(l=0.3, eid='CMY.2456.T3')
cey_2468_t3 = Vcor(l=0.1, eid='CEY.2468.T3')
cmy_2488_t3 = Vcor(l=0.3, eid='CMY.2488.T3')
cey_2509_t3 = Vcor(l=0.1, eid='CEY.2509.T3')
chy_2533_t3 = Vcor(l=0.2, eid='CHY.2533.T3')
chy_2543_t3 = Vcor(l=0.2, eid='CHY.2543.T3')
chy_2559_t3 = Vcor(l=0.2, eid='CHY.2559.T3')
chy_2569_t3 = Vcor(l=0.2, eid='CHY.2569.T3')
chy_2584_t3 = Vcor(l=0.2, eid='CHY.2584.T3')
cey_2625_t3 = Vcor(l=0.1, eid='CEY.2625.T3')
cey_2668_t3 = Vcor(l=0.1, eid='CEY.2668.T3')
cey_2712_un1 = Vcor(l=0.1, eid='CEY.2712.UN1')

# Monitors
bpma_2430_t3 = Monitor(eid='BPMA.2430.T3')
bpma_2442_t3 = Monitor(eid='BPMA.2442.T3')
bpma_2461_t3 = Monitor(eid='BPMA.2461.T3')
bpma_2467_t3 = Monitor(eid='BPMA.2467.T3')
bpma_2487_t3 = Monitor(eid='BPMA.2487.T3')
bpma_2509_t3 = Monitor(eid='BPMA.2509.T3')
bpma_2528_t3 = Monitor(eid='BPMA.2528.T3')
bpma_2531_t3 = Monitor(eid='BPMA.2531.T3')
bpma_2543_t3 = Monitor(eid='BPMA.2543.T3')
bpma_2553_t3 = Monitor(eid='BPMA.2553.T3')
bpma_2558_t3 = Monitor(eid='BPMA.2558.T3')
bpma_2563_t3 = Monitor(eid='BPMA.2563.T3')
bpma_2568_t3 = Monitor(eid='BPMA.2568.T3')
bpma_2579_t3 = Monitor(eid='BPMA.2579.T3')
bpma_2582_t3 = Monitor(eid='BPMA.2582.T3')
bpma_2603_t3 = Monitor(eid='BPMA.2603.T3')
bpma_2624_t3 = Monitor(eid='BPMA.2624.T3')
bpma_2646_t3 = Monitor(eid='BPMA.2646.T3')
bpma_2668_t3 = Monitor(eid='BPMA.2668.T3')
bpma_2690_un1 = Monitor(eid='BPMA.2690.UN1')
bpma_2711_un1 = Monitor(eid='BPMA.2711.UN1')
bpma_2733_un1 = Monitor(eid='BPMA.2733.UN1')

# Markers
ensec_2743_un1 = Marker(eid='ENSEC.2743.UN1')

# Lattice 
cell = (id_1843966_, bpma_2430_t3, d_4, qe_2430_t3, d_5, cex_2430_t3, d_6, bpma_2442_t3, d_4, 
qe_2443_t3, d_8, cmy_2443_t3, id_7434326_, qe_2455_t3, d_5, cex_2455_t3, d_12, cmy_2456_t3, d_13, 
bpma_2461_t3, d_14, bpma_2467_t3, d_4, qe_2468_t3, d_5, cey_2468_t3, d_17, bpma_2487_t3, d_4, 
qe_2487_t3, d_5, cex_2488_t3, d_20, cmy_2488_t3, d_21, bpma_2509_t3, d_4, qe_2509_t3, d_5, 
cey_2509_t3, d_24, bpma_2528_t3, d_25, qh_2529_t3, d_26, chx_2530_t3, d_27, bpma_2531_t3, d_25, 
qh_2532_t3, d_26, chy_2533_t3, d_30, chx_2542_t3, d_31, chy_2543_t3, d_32, bpma_2543_t3, d_33, 
qh_2544_t3, id_55063665_, be_2546_t3, d_36, qm_2549_t3, d_37, bpma_2553_t3, d_38, qm_2554_t3, d_39, 
chx_2554_t3, d_40, saox_2555_t3, d_41, bpma_2558_t3, d_38, qm_2559_t3, d_39, chy_2559_t3, id_26776011_, 
sao_2561_t3, d_46, chx_2562_t3, d_47, bpma_2563_t3, d_38, qm_2564_t3, d_49, be_2566_t3, d_50, 
bpma_2568_t3, d_25, qh_2569_t3, d_26, chy_2569_t3, d_53, bpma_2579_t3, d_25, qh_2580_t3, d_26, 
chx_2581_t3, d_27, bpma_2582_t3, d_25, qh_2583_t3, d_26, chy_2584_t3, d_59, bpma_2603_t3, d_4, 
qe_2603_t3, d_5, cex_2603_t3, d_62, bpma_2624_t3, d_4, qe_2625_t3, d_5, cey_2625_t3, d_62, 
bpma_2646_t3, d_4, qe_2646_t3, d_5, cex_2647_t3, d_62, bpma_2668_t3, d_4, qe_2668_t3, d_5, 
cey_2668_t3, id_70607298_, bpma_2690_un1, d_4, qe_2690_un1, d_5, cex_2690_un1, d_62, bpma_2711_un1, d_4, 
qe_2712_un1, d_5, cey_2712_un1, d_62, bpma_2733_un1, d_4, qe_2733_un1, d_5, cex_2734_un1, d_81, 
ensec_2743_un1)

# power supplies 

#  
qe_2430_t3.ps_id = 'QE.3.T3'
qe_2443_t3.ps_id = 'QE.4.T3'
qe_2455_t3.ps_id = 'QE.5.T3'
qe_2468_t3.ps_id = 'QE.6.T3'
qe_2487_t3.ps_id = 'QE.1.T3'
qe_2509_t3.ps_id = 'QE.2.T3'
qh_2529_t3.ps_id = 'QH.3.T3'
qh_2532_t3.ps_id = 'QH.4.T3'
qh_2544_t3.ps_id = 'QH.1.T3'
qm_2549_t3.ps_id = 'QM.2.T3'
qm_2554_t3.ps_id = 'QM.1.T3'
qm_2559_t3.ps_id = 'QM.2.T3'
qm_2564_t3.ps_id = 'QM.1.T3'
qh_2569_t3.ps_id = 'QH.2.T3'
qh_2580_t3.ps_id = 'QH.3.T3'
qh_2583_t3.ps_id = 'QH.4.T3'
qe_2603_t3.ps_id = 'QE.1.T3'
qe_2625_t3.ps_id = 'QE.2.T3'
qe_2646_t3.ps_id = 'QE.1.T3'
qe_2668_t3.ps_id = 'QE.2.T3'
qe_2690_un1.ps_id = 'QE.1.UN1'
qe_2712_un1.ps_id = 'QE.2.UN1'
qe_2733_un1.ps_id = 'QE.1.UN1'

#  
saox_2555_t3.ps_id = 'SAOX.1.T3'
sao_2561_t3.ps_id = 'SAO.2.T3'

#  

#  

#  
be_2546_t3.ps_id = 'BE.1.T3'
be_2566_t3.ps_id = 'BE.1.T3'
