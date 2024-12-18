from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 9.429026330526568
tws0.beta_y = 22.189275259818615
tws0.alpha_x = -0.6621363588705478
tws0.alpha_y = 1.509023055887539
tws0.E = 14
tws0.s = 2956

# Drifts
id_50681361_ = Drift(l=6.1786, eid='ID_50681361_')
d_4 = Drift(l=0.20895, eid='D_4')
d_5 = Drift(l=0.15395, eid='D_5')
d_6 = Drift(l=11.205, eid='D_6')
d_9 = Drift(l=9.83, eid='D_9')
d_12 = Drift(l=72.48, eid='D_12')
d_15 = Drift(l=5.36, eid='D_15')
id_87871054_ = Drift(l=0.35995, eid='ID_87871054_')
id_61769444_ = Drift(l=0.6498389999999999, eid='ID_61769444_')
d_21 = Drift(l=0.500198, eid='D_21')
d_22 = Drift(l=1.930099, eid='D_22')
d_23 = Drift(l=0.1424, eid='D_23')
d_24 = Drift(l=0.1974, eid='D_24')
d_25 = Drift(l=0.5535, eid='D_25')
id_63596323_ = Drift(l=1.7570000000000001, eid='ID_63596323_')
d_32 = Drift(l=0.500199, eid='D_32')
d_33 = Drift(l=0.611799, eid='D_33')
d_34 = Drift(l=0.1607, eid='D_34')
d_35 = Drift(l=0.3448, eid='D_35')
d_38 = Drift(l=0.2144, eid='D_38')
d_39 = Drift(l=0.558, eid='D_39')
d_40 = Drift(l=0.5, eid='D_40')
d_41 = Drift(l=0.822, eid='D_41')
id_95198724_ = Drift(l=4.833, eid='ID_95198724_')
id_4236296_ = Drift(l=4.26774, eid='ID_4236296_')

# Quadrupoles
qf_2962_t4d = Quadrupole(l=0.5321, k1=0.17384421159932342, eid='QF.2962.T4D')
qf_2974_t4d = Quadrupole(l=0.5321, k1=-0.10382021230031947, eid='QF.2974.T4D')
qf_2985_t4d = Quadrupole(l=0.5321, k1=0.10948822700056379, eid='QF.2985.T4D')
qf_3058_t4d = Quadrupole(l=0.5321, k1=0.144940185399361, eid='QF.3058.T4D')
qf_3065_t4d = Quadrupole(l=0.5321, k1=-0.08471032545010336, eid='QF.3065.T4D')
qk_3074_t4d = Quadrupole(l=1.0552, k1=-0.172994430300417, eid='QK.3074.T4D')
qk_3079_t4d = Quadrupole(l=1.0552, k1=-0.172994430300417, eid='QK.3079.T4D')
qk_3089_t4d = Quadrupole(l=1.0552, k1=-0.1699949051999621, eid='QK.3089.T4D')
qk_3090_t4d = Quadrupole(l=1.0552, k1=-0.1699949051999621, eid='QK.3090.T4D')
qk_3092_t4d = Quadrupole(l=1.0552, k1=-0.1699949051999621, eid='QK.3092.T4D')
qk_3093_t4d = Quadrupole(l=1.0552, k1=-0.1699949051999621, eid='QK.3093.T4D')

# SBends
bv_3067_t4d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3067.T4D')
bv_3070_t4d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3070.T4D')
bv_3083_t4d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3083.T4D')
bv_3086_t4d = SBend(l=2.5, angle=0.043633231, e1=0.021816616, e2=0.021816616, tilt=1.570796327, eid='BV.3086.T4D')

# RBends
sweep_3095_t4d = RBend(l=0.64, tilt=-1.570796327, eid='SWEEP.3095.T4D')
sweep_3096_t4d = RBend(l=0.64, eid='SWEEP.3096.T4D')

# Sextupoles
sk_3076_t4d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid='SK.3076.T4D')
sk_3078_t4d = Sextupole(l=0.343, k2=2.020228531, tilt=1.570796327, eid='SK.3078.T4D')

# Hcors
cfx_2962_t4d = Hcor(l=0.1, eid='CFX.2962.T4D')
cfx_2985_t4d = Hcor(l=0.1, eid='CFX.2985.T4D')
cfx_3059_t4d = Hcor(l=0.1, eid='CFX.3059.T4D')
cnx_3074_t4d = Hcor(l=0.3, eid='CNX.3074.T4D')

# Vcors
cfy_2975_t4d = Vcor(l=0.1, eid='CFY.2975.T4D')
cfy_3064_t4d = Vcor(l=0.1, eid='CFY.3064.T4D')
cny_3080_t4d = Vcor(l=0.3, eid='CNY.3080.T4D')

# Monitors
bpma_2961_t4d = Monitor(eid='BPMA.2961.T4D')
bpma_2974_t4d = Monitor(eid='BPMA.2974.T4D')
bpma_2984_t4d = Monitor(eid='BPMA.2984.T4D')
bpma_3058_t4d = Monitor(eid='BPMA.3058.T4D')
bpmf_3065_t4d = Monitor(eid='BPMF.3065.T4D')
bpmd_3075_t4d = Monitor(eid='BPMD.3075.T4D')
bpmd_3079_t4d = Monitor(eid='BPMD.3079.T4D')
bpmd_3088_t4d = Monitor(eid='BPMD.3088.T4D')
bpmd_3094_t4d = Monitor(eid='BPMD.3094.T4D')
bpmd_3097_t4d = Monitor(eid='BPMD.3097.T4D')
bpmw_3102_t4d = Monitor(eid='BPMW.3102.T4D')

# Markers
ensec_3106_t4d = Marker(eid='ENSEC.3106.T4D')

# Lattice 
cell = (id_50681361_, bpma_2961_t4d, d_4, qf_2962_t4d, d_5, cfx_2962_t4d, d_6, bpma_2974_t4d, d_4, 
qf_2974_t4d, d_5, cfy_2975_t4d, d_9, bpma_2984_t4d, d_4, qf_2985_t4d, d_5, cfx_2985_t4d, d_12, 
bpma_3058_t4d, d_4, qf_3058_t4d, d_5, cfx_3059_t4d, d_15, cfy_3064_t4d, d_5, qf_3065_t4d, id_87871054_, 
bpmf_3065_t4d, id_61769444_, bv_3067_t4d, d_21, bv_3070_t4d, d_22, cnx_3074_t4d, d_23, qk_3074_t4d, d_24, 
bpmd_3075_t4d, d_25, sk_3076_t4d, id_63596323_, sk_3078_t4d, d_25, bpmd_3079_t4d, d_24, qk_3079_t4d, d_23, 
cny_3080_t4d, d_22, bv_3083_t4d, d_32, bv_3086_t4d, d_33, bpmd_3088_t4d, d_34, qk_3089_t4d, d_35, 
qk_3090_t4d, d_35, qk_3092_t4d, d_35, qk_3093_t4d, d_38, bpmd_3094_t4d, d_39, sweep_3095_t4d, d_40, 
sweep_3096_t4d, d_41, bpmd_3097_t4d, id_95198724_, bpmw_3102_t4d, id_4236296_, ensec_3106_t4d)

# power supplies 

#  
qf_2962_t4d.ps_id = 'QF.2.T4D'
qf_2974_t4d.ps_id = 'QF.3.T4D'
qf_2985_t4d.ps_id = 'QF.1.T4D'
qf_3058_t4d.ps_id = 'QF.4.T4D'
qf_3065_t4d.ps_id = 'QF.5.T4D'
qk_3074_t4d.ps_id = 'QK.1.T4D'
qk_3079_t4d.ps_id = 'QK.1.T4D'
qk_3089_t4d.ps_id = 'QK.6.T4D'
qk_3090_t4d.ps_id = 'QK.6.T4D'
qk_3092_t4d.ps_id = 'QK.6.T4D'
qk_3093_t4d.ps_id = 'QK.6.T4D'

#  
sk_3076_t4d.ps_id = 'SK.1.T4D'
sk_3078_t4d.ps_id = 'SK.1.T4D'

#  

#  

#  
bv_3067_t4d.ps_id = 'BV.1.T4D'
bv_3070_t4d.ps_id = 'BV.1.T4D'
bv_3083_t4d.ps_id = 'BV.1.T4D'
bv_3086_t4d.ps_id = 'BV.1.T4D'
sweep_3095_t4d.ps_id = 'SWEEP.1.T4D'
sweep_3096_t4d.ps_id = 'SWEEP.1.T4D'
