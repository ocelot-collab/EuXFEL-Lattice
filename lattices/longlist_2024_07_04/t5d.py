from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 38.45542292280062
tws0.beta_y = 49.754948691305444
tws0.alpha_x = -1.0273576528473884
tws0.alpha_y = 1.3083708330446713
tws0.E = 14
tws0.s = 3039.372919999988

# Drifts
id_85098369_ = Drift(l=13.4714, eid='ID_85098369_')
d_3 = Drift(l=15.515, eid='D_3')
d_4 = Drift(l=0.20895, eid='D_4')
d_5 = Drift(l=0.15395, eid='D_5')
d_6 = Drift(l=11.205, eid='D_6')
d_9 = Drift(l=60.205, eid='D_9')
d_12 = Drift(l=5.36, eid='D_12')
id_73386990_ = Drift(l=0.35995, eid='ID_73386990_')
id_98070484_ = Drift(l=0.626721, eid='ID_98070484_')
d_18 = Drift(l=0.500198, eid='D_18')
d_19 = Drift(l=1.930099, eid='D_19')
d_20 = Drift(l=0.1424, eid='D_20')
d_21 = Drift(l=0.1974, eid='D_21')
d_22 = Drift(l=0.5535, eid='D_22')
id_74499753_ = Drift(l=1.7570000000000001, eid='ID_74499753_')
d_29 = Drift(l=0.500199, eid='D_29')
d_30 = Drift(l=0.611799, eid='D_30')
d_31 = Drift(l=0.1607, eid='D_31')
d_32 = Drift(l=0.3448, eid='D_32')
d_35 = Drift(l=0.2144, eid='D_35')
d_36 = Drift(l=0.558, eid='D_36')
d_37 = Drift(l=0.5, eid='D_37')
d_38 = Drift(l=0.822, eid='D_38')
id_89569167_ = Drift(l=4.833, eid='ID_89569167_')
id_19340264_ = Drift(l=4.26774, eid='ID_19340264_')

# Quadrupoles
qe_3052_t5d = Quadrupole(l=0.24, k1=0.17811070150000002, eid='QE.3052.T5D')
qf_3068_t5d = Quadrupole(l=0.5321, k1=-0.17408057190001877, eid='QF.3068.T5D')
qf_3081_t5d = Quadrupole(l=0.5321, k1=0.041949297430934035, eid='QF.3081.T5D')
qf_3142_t5d = Quadrupole(l=0.5321, k1=0.15234501850028187, eid='QF.3142.T5D')
qf_3148_t5d = Quadrupole(l=0.5321, k1=-0.08121677321931967, eid='QF.3148.T5D')
qk_3158_t5d = Quadrupole(l=1.0552, k1=-0.172994430300417, eid='QK.3158.T5D')
qk_3163_t5d = Quadrupole(l=1.0552, k1=-0.172994430300417, eid='QK.3163.T5D')
qk_3172_t5d = Quadrupole(l=1.0552, k1=-0.18514803489954512, eid='QK.3172.T5D')
qk_3174_t5d = Quadrupole(l=1.0552, k1=-0.18514803489954512, eid='QK.3174.T5D')
qk_3175_t5d = Quadrupole(l=1.0552, k1=-0.18514803489954512, eid='QK.3175.T5D')
qk_3177_t5d = Quadrupole(l=1.0552, k1=-0.18514803489954512, eid='QK.3177.T5D')

# SBends
bv_3151_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3151.T5D')
bv_3154_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3154.T5D')
bv_3167_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3167.T5D')
bv_3170_t5d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3170.T5D')

# RBends
sweep_3178_t5d = RBend(l=0.64, tilt=-1.570796327, eid='SWEEP.3178.T5D')
sweep_3179_t5d = RBend(l=0.64, eid='SWEEP.3179.T5D')

# Sextupoles
sk_3159_t5d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid='SK.3159.T5D')
sk_3161_t5d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid='SK.3161.T5D')

# Hcors
cfx_3081_t5d = Hcor(l=0.1, eid='CFX.3081.T5D')
cfx_3142_t5d = Hcor(l=0.1, eid='CFX.3142.T5D')
cnx_3157_t5d = Hcor(l=0.3, eid='CNX.3157.T5D')

# Vcors
cfy_3069_t5d = Vcor(l=0.1, eid='CFY.3069.T5D')
cfy_3148_t5d = Vcor(l=0.1, eid='CFY.3148.T5D')
cny_3164_t5d = Vcor(l=0.3, eid='CNY.3164.T5D')

# Monitors
bpma_3068_t5d = Monitor(eid='BPMA.3068.T5D')
bpma_3080_t5d = Monitor(eid='BPMA.3080.T5D')
bpma_3141_t5d = Monitor(eid='BPMA.3141.T5D')
bpmf_3149_t5d = Monitor(eid='BPMF.3149.T5D')
bpmd_3159_t5d = Monitor(eid='BPMD.3159.T5D')
bpmd_3162_t5d = Monitor(eid='BPMD.3162.T5D')
bpmd_3172_t5d = Monitor(eid='BPMD.3172.T5D')
bpmd_3177_t5d = Monitor(eid='BPMD.3177.T5D')
bpmd_3180_t5d = Monitor(eid='BPMD.3180.T5D')
bpmw_3185_t5d = Monitor(eid='BPMW.3185.T5D')

# Markers
ensec_3039_un2 = Marker(eid='ENSEC.3039.UN2')
ensec_3189_t5d = Marker(eid='ENSEC.3189.T5D')

# Lattice 
cell = (ensec_3039_un2, id_85098369_, qe_3052_t5d, d_3, bpma_3068_t5d, d_4, qf_3068_t5d, d_5, cfy_3069_t5d, 
d_6, bpma_3080_t5d, d_4, qf_3081_t5d, d_5, cfx_3081_t5d, d_9, bpma_3141_t5d, d_4, qf_3142_t5d, 
d_5, cfx_3142_t5d, d_12, cfy_3148_t5d, d_5, qf_3148_t5d, id_73386990_, bpmf_3149_t5d, id_98070484_, bv_3151_t5d, 
d_18, bv_3154_t5d, d_19, cnx_3157_t5d, d_20, qk_3158_t5d, d_21, bpmd_3159_t5d, d_22, sk_3159_t5d, 
id_74499753_, sk_3161_t5d, d_22, bpmd_3162_t5d, d_21, qk_3163_t5d, d_20, cny_3164_t5d, d_19, bv_3167_t5d, 
d_29, bv_3170_t5d, d_30, bpmd_3172_t5d, d_31, qk_3172_t5d, d_32, qk_3174_t5d, d_32, qk_3175_t5d, 
d_32, qk_3177_t5d, d_35, bpmd_3177_t5d, d_36, sweep_3178_t5d, d_37, sweep_3179_t5d, d_38, bpmd_3180_t5d, 
id_89569167_, bpmw_3185_t5d, id_19340264_, ensec_3189_t5d)

# power supplies 

#  
qe_3052_t5d.ps_id = 'QE.1.T5D'
qf_3068_t5d.ps_id = 'QF.1.T5D'
qf_3081_t5d.ps_id = 'QF.2.T5D'
qf_3142_t5d.ps_id = 'QF.3.T5D'
qf_3148_t5d.ps_id = 'QF.4.T5D'
qk_3158_t5d.ps_id = 'QK.1.T5D'
qk_3163_t5d.ps_id = 'QK.1.T5D'
qk_3172_t5d.ps_id = 'QK.6.T5D'
qk_3174_t5d.ps_id = 'QK.6.T5D'
qk_3175_t5d.ps_id = 'QK.6.T5D'
qk_3177_t5d.ps_id = 'QK.6.T5D'

#  
sk_3159_t5d.ps_id = 'SK.1.T5D'
sk_3161_t5d.ps_id = 'SK.1.T5D'

#  

#  

#  
bv_3151_t5d.ps_id = 'BV.1.T5D'
bv_3154_t5d.ps_id = 'BV.1.T5D'
bv_3167_t5d.ps_id = 'BV.1.T5D'
bv_3170_t5d.ps_id = 'BV.1.T5D'
sweep_3178_t5d.ps_id = 'SWEEP.1.T5D'
sweep_3179_t5d.ps_id = 'SWEEP.1.T5D'
