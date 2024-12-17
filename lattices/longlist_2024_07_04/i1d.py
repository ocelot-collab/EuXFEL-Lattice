from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 3.020685835329106
tws0.beta_y = 7.0413164056761035
tws0.alpha_x = 0.23961060835472217
tws0.alpha_y = -2.1828482259048667
tws0.E = 0.12999999999999998
tws0.s = 62.08900499999993

# Drifts
d_2 = Drift(l=0.002879, eid='D_2')
d_3 = Drift(l=0.969029, eid='D_3')
d_4 = Drift(l=0.15615, eid='D_4')
id_42915600_ = Drift(l=0.55615, eid='ID_42915600_')
id_58116680_ = Drift(l=0.59921, eid='ID_58116680_')
id_42845338_ = Drift(l=2.3312299999999997, eid='ID_42845338_')

# Quadrupoles
qi_63_i1d = Quadrupole(l=0.2377, k1=4.401795, eid='QI.63.I1D')
qi_64_i1d = Quadrupole(l=0.2377, eid='QI.64.I1D')

# SBends
bb_62_i1d = SBend(l=0.5, angle=0.5235987756, e1=0.261799388, e2=0.261799388, eid='BB.62.I1D')

# Monitors
bpma_63_i1d = Monitor(eid='BPMA.63.I1D')
bpmd_64_i1d = Monitor(eid='BPMD.64.I1D')

# Markers
stsec_62_i1d = Marker(eid='STSEC.62.I1D')
ensec_66_i1d = Marker(eid='ENSEC.66.I1D')

# Lattice 
cell = (stsec_62_i1d, d_2, bb_62_i1d, d_3, qi_63_i1d, d_4, bpma_63_i1d, id_42915600_, qi_64_i1d, 
id_58116680_, bpmd_64_i1d, id_42845338_, ensec_66_i1d)

# power supplies 

#  
qi_63_i1d.ps_id = 'QI.41.I1D'
qi_64_i1d.ps_id = 'QI.42.I1D'

#  

#  

#  

#  
bb_62_i1d.ps_id = 'BB.5.I1D'
