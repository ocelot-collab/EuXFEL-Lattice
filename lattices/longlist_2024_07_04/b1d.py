from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 7.865550253394325
tws0.beta_y = 8.698292442670796
tws0.alpha_x = -1.0418290882386196
tws0.alpha_y = -1.2234476587083056
tws0.E = 0.7000000007706801
tws0.s = 229.3007540000002

# Drifts
d_2 = Drift(l=0.254587, eid='D_2')
d_3 = Drift(l=1.319557, eid='D_3')
d_4 = Drift(l=0.15065, eid='D_4')
d_5 = Drift(l=0.13165, eid='D_5')
d_6 = Drift(l=1.23165, eid='D_6')
d_7 = Drift(l=0.68965, eid='D_7')
d_8 = Drift(l=0.181, eid='D_8')
id_54786280_ = Drift(l=2.8866, eid='ID_54786280_')
d_11 = Drift(l=1.1493, eid='D_11')

# Quadrupoles
qd_231_b1d = Quadrupole(l=0.2367, k1=-3.0, eid='QD.231.B1D')
qd_232_b1d = Quadrupole(l=0.2367, eid='QD.232.B1D')

# SBends
bb_229_b1d = SBend(l=0.5, angle=0.2094395102, e2=0.20943951, tilt=1.570796327, eid='BB.229.B1D')

# Hcors
ccx_233_b1d = Hcor(l=0.1, eid='CCX.233.B1D')

# Vcors
ccy_231_b1d = Vcor(l=0.1, eid='CCY.231.B1D')

# Monitors
bpma_231_b1d = Monitor(eid='BPMA.231.B1D')
bpma_233_b1d = Monitor(eid='BPMA.233.B1D')
bpma_236_b1d = Monitor(eid='BPMA.236.B1D')

# Markers
ensec_237_b1d = Marker(eid='ENSEC.237.B1D')

# Lattice 
cell = (d_2, bb_229_b1d, d_3, bpma_231_b1d, d_4, qd_231_b1d, d_5, ccy_231_b1d, d_6, 
qd_232_b1d, d_7, bpma_233_b1d, d_8, ccx_233_b1d, id_54786280_, bpma_236_b1d, d_11, ensec_237_b1d)

# power supplies 

#  
qd_231_b1d.ps_id = 'QD.25.B1D'
qd_232_b1d.ps_id = 'QD.26.B1D'

#  

#  

#  

#  
bb_229_b1d.ps_id = 'BB.1.B1D'
