from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 29.41686175122868
tws0.beta_y = 5.144745537053657
tws0.alpha_x = 2.626251558631553
tws0.alpha_y = -1.253808202141189
tws0.E = 2.399999999680003
tws0.s = 466.8192259999962

# Drifts
d_2 = Drift(l=0.00145, eid='D_2')
d_3 = Drift(l=0.58145, eid='D_3')
d_4 = Drift(l=0.17395, eid='D_4')
d_5 = Drift(l=0.18395, eid='D_5')
d_6 = Drift(l=1.04372, eid='D_6')
d_7 = Drift(l=0.13628, eid='D_7')
d_8 = Drift(l=0.18, eid='D_8')
d_9 = Drift(l=0.2, eid='D_9')
d_10 = Drift(l=0.98395, eid='D_10')
d_11 = Drift(l=0.43628, eid='D_11')
d_12 = Drift(l=0.41912, eid='D_12')
d_13 = Drift(l=0.516377, eid='D_13')
d_14 = Drift(l=0.16902, eid='D_14')
d_15 = Drift(l=0.25898, eid='D_15')
d_16 = Drift(l=0.2249, eid='D_16')
d_17 = Drift(l=0.23402, eid='D_17')
d_18 = Drift(l=0.66368, eid='D_18')
d_19 = Drift(l=0.35, eid='D_19')
d_20 = Drift(l=1.01327, eid='D_20')


# Quadrupoles
# special optics in B2/B2D for energy spread measurements 
qf_469_b2d = Quadrupole(l=0.5321, k1=0.0, eid='QF.469.B2D')
qe_471_b2d = Quadrupole(l=0.24, k1=2.05, eid='QE.471.B2D')
qf_472_b2d = Quadrupole(l=0.5321, k1=-0.096, eid='QF.472.B2D')

qf_476_b2d = Quadrupole(l=0.5321, k1=3.1309789299999995, eid='QF.476.B2D')
qf_477_b2d = Quadrupole(l=0.5321, k1=0.7703645572993798, eid='QF.477.B2D')

# SBends
bg_467_b2d = SBend(l=1.5971, angle=0.2094395102, tilt=1.570796327, eid='BG.467.B2D')
bg_474_b2d = SBend(l=1.5971, angle=-0.2094395102, tilt=1.570796327, eid='BG.474.B2D')

# Hcors
cfx_470_b2d = Hcor(l=0.1, eid='CFX.470.B2D')
cfx_477_b2d = Hcor(l=0.1, eid='CFX.477.B2D')

# Vcors
cfy_468_b2d = Vcor(l=0.1, eid='CFY.468.B2D')
cfy_471_b2d = Vcor(l=0.1, eid='CFY.471.B2D')
cfy_476_b2d = Vcor(l=0.1, eid='CFY.476.B2D')

# Monitors
bpma_469_b2d = Monitor(eid='BPMA.469.B2D')
bpma_471_b2d = Monitor(eid='BPMA.471.B2D')
bpma_477_b2d = Monitor(eid='BPMA.477.B2D')
bpmd_479_b2d = Monitor(eid='BPMD.479.B2D')

# Markers
otra_473_b2d = Marker(eid='OTRA.473.B2D')
otrd_478_b2d = Marker(eid='OTRD.478.B2D')
ensec_480_b2d = Marker(eid='ENSEC.480.B2D')

# Lattice 
cell = (d_2, bg_467_b2d, d_3, cfy_468_b2d, d_4, qf_469_b2d, d_5, bpma_469_b2d, d_6, 
cfx_470_b2d, d_7, qe_471_b2d, d_8, bpma_471_b2d, d_9, cfy_471_b2d, d_10, qf_472_b2d, d_11, 
otra_473_b2d, d_12, bg_474_b2d, d_13, cfy_476_b2d, d_14, qf_476_b2d, d_15, bpma_477_b2d, d_16, 
cfx_477_b2d, d_17, qf_477_b2d, d_18, otrd_478_b2d, d_19, bpmd_479_b2d, d_20, ensec_480_b2d)

# power supplies 

#  
qf_469_b2d.ps_id = 'QF.31.B2D'
qe_471_b2d.ps_id = 'QE.32.B2D'
qf_472_b2d.ps_id = 'QF.33.B2D'
qf_476_b2d.ps_id = 'QF.34.B2D'
qf_477_b2d.ps_id = 'QF.35.B2D'

#  

#  

#  

#  
bg_467_b2d.ps_id = 'BG.1.B2D'
bg_474_b2d.ps_id = 'BG.1.B2D'

