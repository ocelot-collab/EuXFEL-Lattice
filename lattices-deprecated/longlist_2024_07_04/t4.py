from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 25.263665891080947
tws0.beta_y = 40.54159948158437
tws0.alpha_x = -0.7944632639752688
tws0.alpha_y = 1.26958806877402
tws0.E = 14
tws0.s = 2461.7178630000176

# Drifts
id_62297124_ = Drift(l=7.0585, eid='ID_62297124_')
d_4 = Drift(l=0.205, eid='D_4')
d_5 = Drift(l=0.14, eid='D_5')
d_6 = Drift(l=11.925, eid='D_6')
id_47145858_ = Drift(l=11.924999999999999, eid='ID_47145858_')
d_16 = Drift(l=19.01, eid='D_16')
d_19 = Drift(l=21.065, eid='D_19')
d_22 = Drift(l=18.72, eid='D_22')
d_23 = Drift(l=0.21045, eid='D_23')
d_24 = Drift(l=0.15545, eid='D_24')
d_25 = Drift(l=1.545, eid='D_25')
d_28 = Drift(l=9.06, eid='D_28')
d_29 = Drift(l=0.185, eid='D_29')
d_30 = Drift(l=0.19, eid='D_30')
id_19088442_ = Drift(l=0.38545, eid='ID_19088442_')
d_33 = Drift(l=7e-06, eid='D_33')
d_34 = Drift(l=1.070157, eid='D_34')
d_35 = Drift(l=3.59515, eid='D_35')
d_36 = Drift(l=0.34515, eid='D_36')
d_37 = Drift(l=0.29015, eid='D_37')
d_38 = Drift(l=0.6718, eid='D_38')
d_39 = Drift(l=2.1168, eid='D_39')
d_42 = Drift(l=1.3218, eid='D_42')
d_43 = Drift(l=1.0768, eid='D_43')
d_46 = Drift(l=0.369898, eid='D_46')
d_47 = Drift(l=0.875266, eid='D_47')
d_50 = Drift(l=9.835, eid='D_50')
d_56 = Drift(l=18.61, eid='D_56')
id_36419442_ = Drift(l=21.064999999999998, eid='ID_36419442_')
d_72 = Drift(l=20.165, eid='D_72')
d_73 = Drift(l=0.20895, eid='D_73')
d_74 = Drift(l=0.15395, eid='D_74')
id_24319000_ = Drift(l=11.005, eid='ID_24319000_')
id_28148742_ = Drift(l=4.239987, eid='ID_28148742_')
d_88 = Drift(l=3.657213, eid='D_88')
d_89 = Drift(l=0.21815, eid='D_89')
d_90 = Drift(l=0.17815, eid='D_90')
d_91 = Drift(l=0.125, eid='D_91')
d_92 = Drift(l=2.1675, eid='D_92')
d_93 = Drift(l=1.8267, eid='D_93')
d_94 = Drift(l=0.15, eid='D_94')
d_95 = Drift(l=0.4323, eid='D_95')
d_96 = Drift(l=0.18665, eid='D_96')
id_24575046_ = Drift(l=0.04015, eid='ID_24575046_')

# Quadrupoles
qe_2468_t4 = Quadrupole(l=0.24, k1=0.2237922517, eid='QE.2468.T4')
qe_2481_t4 = Quadrupole(l=0.24, k1=-0.2040914524, eid='QE.2481.T4')
qe_2493_t4 = Quadrupole(l=0.24, k1=0.24059635850000002, eid='QE.2493.T4')
qe_2506_t4 = Quadrupole(l=0.24, k1=-0.23065976060000004, eid='QE.2506.T4')
qe_2526_t4 = Quadrupole(l=0.24, k1=0.19227955160000001, eid='QE.2526.T4')
qe_2548_t4 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid='QE.2548.T4')
qh_2567_t4 = Quadrupole(l=1.0291, k1=0.1965315531998834, eid='QH.2567.T4')
qh_2570_t4 = Quadrupole(l=1.0291, k1=-0.19652613830045673, eid='QH.2570.T4')
qh_2582_t4 = Quadrupole(l=1.0291, k1=0.2948896440996988, eid='QH.2582.T4')
qm_2587_t4 = Quadrupole(l=1.0597, k1=-0.2884660775002359, eid='QM.2587.T4')
qm_2592_t4 = Quadrupole(l=1.0597, k1=0.28822914539964134, eid='QM.2592.T4')
qm_2597_t4 = Quadrupole(l=1.0597, k1=-0.2884660775002359, eid='QM.2597.T4')
qm_2602_t4 = Quadrupole(l=1.0597, k1=0.28822914539964134, eid='QM.2602.T4')
qh_2607_t4 = Quadrupole(l=1.0291, k1=-0.29482679030026243, eid='QH.2607.T4')
qh_2618_t4 = Quadrupole(l=1.0291, k1=0.1965315531998834, eid='QH.2618.T4')
qh_2621_t4 = Quadrupole(l=1.0291, k1=-0.19652613830045673, eid='QH.2621.T4')
qe_2641_t4 = Quadrupole(l=0.24, k1=0.19227955160000001, eid='QE.2641.T4')
qe_2663_t4 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid='QE.2663.T4')
qe_2685_t4 = Quadrupole(l=0.24, k1=0.19227955160000001, eid='QE.2685.T4')
qe_2707_t4 = Quadrupole(l=0.24, k1=-0.19227955160000001, eid='QE.2707.T4')
qe_2728_t4 = Quadrupole(l=0.24, k1=0.19227955160000001, eid='QE.2728.T4')
qf_2749_t4 = Quadrupole(l=0.5321, k1=-0.1156016655008457, eid='QF.2749.T4')
qf_2761_t4 = Quadrupole(l=0.5321, k1=0.14754132349934224, eid='QF.2761.T4')
qf_2773_t4 = Quadrupole(l=0.5321, k1=-0.15051305829919187, eid='QF.2773.T4')
qf_2785_t4 = Quadrupole(l=0.5321, k1=0.18363763539936098, eid='QF.2785.T4')
qa_2794_t4 = Quadrupole(l=0.1137, k1=-1.116515944001759, eid='QA.2794.T4')
qa_2800_t4 = Quadrupole(l=0.1137, k1=1.2439009670008796, eid='QA.2800.T4')

# SBends
be_2584_t4 = SBend(l=2.5, angle=0.0115035, e1=0.00575175, e2=0.00575175, eid='BE.2584.T4')
be_2604_t4 = SBend(l=2.5, angle=0.0115035, e1=0.00575175, e2=0.00575175, eid='BE.2604.T4')

# Sextupoles
saox_2594_t4 = Sextupole(l=0.3164, k2=23.92225032, eid='SAOX.2594.T4')
saox_2599_t4 = Sextupole(l=0.3164, k2=8.44816687700063, eid='SAOX.2599.T4')

# Hcors
cex_2469_t4 = Hcor(l=0.1, eid='CEX.2469.T4')
cex_2494_t4 = Hcor(l=0.1, eid='CEX.2494.T4')
cex_2526_t4 = Hcor(l=0.1, eid='CEX.2526.T4')
chx_2568_t4 = Hcor(l=0.2, eid='CHX.2568.T4')
chx_2581_t4 = Hcor(l=0.2, eid='CHX.2581.T4')
chx_2593_t4 = Hcor(l=0.2, eid='CHX.2593.T4')
chx_2601_t4 = Hcor(l=0.2, eid='CHX.2601.T4')
chx_2619_t4 = Hcor(l=0.2, eid='CHX.2619.T4')
cex_2642_t4 = Hcor(l=0.1, eid='CEX.2642.T4')
cex_2685_t4 = Hcor(l=0.1, eid='CEX.2685.T4')
cex_2729_t4 = Hcor(l=0.1, eid='CEX.2729.T4')
cfx_2762_t4 = Hcor(l=0.1, eid='CFX.2762.T4')
cfx_2786_t4 = Hcor(l=0.1, eid='CFX.2786.T4')
cex_2795_t4 = Hcor(l=0.1, eid='CEX.2795.T4')
cex_2799_t4 = Hcor(l=0.1, eid='CEX.2799.T4')

# Vcors
cey_2481_t4 = Vcor(l=0.1, eid='CEY.2481.T4')
cey_2506_t4 = Vcor(l=0.1, eid='CEY.2506.T4')
cey_2548_t4 = Vcor(l=0.1, eid='CEY.2548.T4')
chy_2571_t4 = Vcor(l=0.2, eid='CHY.2571.T4')
chy_2581_t4 = Vcor(l=0.2, eid='CHY.2581.T4')
chy_2598_t4 = Vcor(l=0.2, eid='CHY.2598.T4')
chy_2608_t4 = Vcor(l=0.2, eid='CHY.2608.T4')
chy_2622_t4 = Vcor(l=0.2, eid='CHY.2622.T4')
cey_2663_t4 = Vcor(l=0.1, eid='CEY.2663.T4')
cey_2707_t4 = Vcor(l=0.1, eid='CEY.2707.T4')
cfy_2750_t4 = Vcor(l=0.1, eid='CFY.2750.T4')
cfy_2774_t4 = Vcor(l=0.1, eid='CFY.2774.T4')
cny_2794_t4 = Vcor(l=0.3, eid='CNY.2794.T4')
cny_2799_t4 = Vcor(l=0.3, eid='CNY.2799.T4')

# Undulators
u40s_2797_t4 = Undulator(lperiod=0.04, nperiods=3.0, eid='U40S.2797.T4')

# Monitors
bpma_2468_t4 = Monitor(eid='BPMA.2468.T4')
bpma_2481_t4 = Monitor(eid='BPMA.2481.T4')
bpma_2493_t4 = Monitor(eid='BPMA.2493.T4')
bpma_2506_t4 = Monitor(eid='BPMA.2506.T4')
bpma_2525_t4 = Monitor(eid='BPMA.2525.T4')
bpma_2547_t4 = Monitor(eid='BPMA.2547.T4')
bpma_2567_t4 = Monitor(eid='BPMA.2567.T4')
bpma_2570_t4 = Monitor(eid='BPMA.2570.T4')
bpma_2581_t4 = Monitor(eid='BPMA.2581.T4')
bpma_2591_t4 = Monitor(eid='BPMA.2591.T4')
bpma_2596_t4 = Monitor(eid='BPMA.2596.T4')
bpma_2601_t4 = Monitor(eid='BPMA.2601.T4')
bpma_2606_t4 = Monitor(eid='BPMA.2606.T4')
bpma_2618_t4 = Monitor(eid='BPMA.2618.T4')
bpma_2621_t4 = Monitor(eid='BPMA.2621.T4')
bpma_2641_t4 = Monitor(eid='BPMA.2641.T4')
bpma_2663_t4 = Monitor(eid='BPMA.2663.T4')
bpma_2684_t4 = Monitor(eid='BPMA.2684.T4')
bpma_2706_t4 = Monitor(eid='BPMA.2706.T4')
bpma_2728_t4 = Monitor(eid='BPMA.2728.T4')
bpma_2749_t4 = Monitor(eid='BPMA.2749.T4')
bpma_2761_t4 = Monitor(eid='BPMA.2761.T4')
bpma_2773_t4 = Monitor(eid='BPMA.2773.T4')
bpma_2785_t4 = Monitor(eid='BPMA.2785.T4')
bpma_2790_t4 = Monitor(eid='BPMA.2790.T4')
bpme_2794_t4 = Monitor(eid='BPME.2794.T4')
bpme_2800_t4 = Monitor(eid='BPME.2800.T4')

# Markers
stsub_2583_t4 = Marker(eid='STSUB.2583.T4')
ensec_2800_t4 = Marker(eid='ENSEC.2800.T4')

# Lattice 
cell = (id_62297124_, bpma_2468_t4, d_4, qe_2468_t4, d_5, cex_2469_t4, d_6, bpma_2481_t4, d_4, 
qe_2481_t4, d_5, cey_2481_t4, d_6, bpma_2493_t4, d_4, qe_2493_t4, d_5, cex_2494_t4, id_47145858_, 
bpma_2506_t4, d_4, qe_2506_t4, d_5, cey_2506_t4, d_16, bpma_2525_t4, d_4, qe_2526_t4, d_5, 
cex_2526_t4, d_19, bpma_2547_t4, d_4, qe_2548_t4, d_5, cey_2548_t4, d_22, bpma_2567_t4, d_23, 
qh_2567_t4, d_24, chx_2568_t4, d_25, bpma_2570_t4, d_23, qh_2570_t4, d_24, chy_2571_t4, d_28, 
chx_2581_t4, d_29, chy_2581_t4, d_30, bpma_2581_t4, d_23, qh_2582_t4, id_19088442_, stsub_2583_t4, d_33, 
be_2584_t4, d_34, qm_2587_t4, d_35, bpma_2591_t4, d_36, qm_2592_t4, d_37, chx_2593_t4, d_38, 
saox_2594_t4, d_39, bpma_2596_t4, d_36, qm_2597_t4, d_37, chy_2598_t4, d_42, saox_2599_t4, d_43, 
chx_2601_t4, d_30, bpma_2601_t4, d_36, qm_2602_t4, d_46, be_2604_t4, d_47, bpma_2606_t4, d_23, 
qh_2607_t4, d_24, chy_2608_t4, d_50, bpma_2618_t4, d_23, qh_2618_t4, d_24, chx_2619_t4, d_25, 
bpma_2621_t4, d_23, qh_2621_t4, d_24, chy_2622_t4, d_56, bpma_2641_t4, d_4, qe_2641_t4, d_5, 
cex_2642_t4, d_19, bpma_2663_t4, d_4, qe_2663_t4, d_5, cey_2663_t4, d_19, bpma_2684_t4, d_4, 
qe_2685_t4, d_5, cex_2685_t4, d_19, bpma_2706_t4, d_4, qe_2707_t4, d_5, cey_2707_t4, id_36419442_, 
bpma_2728_t4, d_4, qe_2728_t4, d_5, cex_2729_t4, d_72, bpma_2749_t4, d_73, qf_2749_t4, d_74, 
cfy_2750_t4, id_24319000_, bpma_2761_t4, d_73, qf_2761_t4, d_74, cfx_2762_t4, id_24319000_, bpma_2773_t4, d_73, 
qf_2773_t4, d_74, cfy_2774_t4, id_24319000_, bpma_2785_t4, d_73, qf_2785_t4, d_74, cfx_2786_t4, id_28148742_, 
bpma_2790_t4, d_88, bpme_2794_t4, d_89, qa_2794_t4, d_90, cny_2794_t4, d_91, cex_2795_t4, d_92, 
u40s_2797_t4, d_93, cny_2799_t4, d_94, cex_2799_t4, d_95, bpme_2800_t4, d_96, qa_2800_t4, id_24575046_, 
ensec_2800_t4)

# power supplies 

#  
qe_2468_t4.ps_id = 'QE.3.T4'
qe_2481_t4.ps_id = 'QE.4.T4'
qe_2493_t4.ps_id = 'QE.5.T4'
qe_2506_t4.ps_id = 'QE.6.T4'
qe_2526_t4.ps_id = 'QE.2.T4'
qe_2548_t4.ps_id = 'QE.1.T4'
qh_2567_t4.ps_id = 'QH.4.T4'
qh_2570_t4.ps_id = 'QH.3.T4'
qh_2582_t4.ps_id = 'QH.1.T4'
qm_2587_t4.ps_id = 'QM.2.T4'
qm_2592_t4.ps_id = 'QM.1.T4'
qm_2597_t4.ps_id = 'QM.2.T4'
qm_2602_t4.ps_id = 'QM.1.T4'
qh_2607_t4.ps_id = 'QH.2.T4'
qh_2618_t4.ps_id = 'QH.4.T4'
qh_2621_t4.ps_id = 'QH.3.T4'
qe_2641_t4.ps_id = 'QE.2.T4'
qe_2663_t4.ps_id = 'QE.1.T4'
qe_2685_t4.ps_id = 'QE.2.T4'
qe_2707_t4.ps_id = 'QE.1.T4'
qe_2728_t4.ps_id = 'QE.2.T4'
qf_2749_t4.ps_id = 'QF.7.T4'
qf_2761_t4.ps_id = 'QF.8.T4'
qf_2773_t4.ps_id = 'QF.9.T4'
qf_2785_t4.ps_id = 'QF.10.T4'
qa_2794_t4.ps_id = 'QA.3.T4'
qa_2800_t4.ps_id = 'QA.4.T4'

#  
saox_2594_t4.ps_id = 'SAOX.1.T4'
saox_2599_t4.ps_id = 'SAOX.2.T4'

#  

#  

#  
be_2584_t4.ps_id = 'BE.1.T4'
be_2604_t4.ps_id = 'BE.1.T4'
