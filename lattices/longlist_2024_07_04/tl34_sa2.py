from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 43.11647525647555
tws0.beta_y = 10.860573729512675
tws0.alpha_x = -2.1790120506947406
tws0.alpha_y = 0.6184659724795544
tws0.E = 14
tws0.s = 1980.3864730000207

# Drifts
id_60730788_ = Drift(l=1.472401, eid='ID_60730788_')
d_3 = Drift(l=13.047401, eid='D_3')
d_4 = Drift(l=1.15895, eid='D_4')
d_5 = Drift(l=0.15395, eid='D_5')
id_71590683_ = Drift(l=0.16, eid='ID_71590683_')
d_7 = Drift(l=0.07, eid='D_7')
d_9 = Drift(l=0.28, eid='D_9')
d_12 = Drift(l=0.205, eid='D_12')
d_13 = Drift(l=6.5, eid='D_13')
d_14 = Drift(l=0.6, eid='D_14')
d_15 = Drift(l=0.208951, eid='D_15')
d_16 = Drift(l=0.153951, eid='D_16')
d_17 = Drift(l=0.2, eid='D_17')
d_18 = Drift(l=7.7847, eid='D_18')
d_19 = Drift(l=0.1, eid='D_19')
d_20 = Drift(l=1.4347, eid='D_20')
id_79622812_ = Drift(l=2.06072, eid='ID_79622812_')

# Quadrupoles
qk_1982_tl = Quadrupole(l=1.0552, k1=0.09035960007960576, eid='QK.1982.TL')
qf_1997_tl = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid='QF.1997.TL')
# Quad QF.2012.TL replace with combine function SBEND since beam has displacement 0.00581165 m
angle_n = -5.715204879e-04
qf_2012_tl = SBend(l=0.5321, angle=angle_n, k1=-0.1791908476, e1=+1.444493782E-04, e2=+7.159698661E-04, tilt=1.570796, eid='QF.2012.TL')

# bending magnets: KL kickers have to be ON to transport beam to SA2 branch
alpha=-0.0001019145217
kl_1998_tl = SBend(l=0.93, angle=alpha, e1=0,        e2=alpha, tilt=1.570796, eid="KL.1998.TL")
kl_1999_tl = SBend(l=0.93, angle=alpha, e1=-alpha,   e2=2*alpha,  tilt=1.570796, eid="KL.1999.TL")
kl_2000_tl = SBend(l=0.93, angle=alpha, e1=-2*alpha, e2=3*alpha,  tilt=1.570796, eid="KL.2000.TL")
kl_2001_tl = SBend(l=0.93, angle=alpha, e1=-3*alpha, e2=4*alpha,  tilt=1.570796, eid="KL.2001.TL")
kl_2002_tl = SBend(l=0.93, angle=alpha, e1=-4*alpha, e2=5*alpha,  tilt=1.570796, eid="KL.2002.TL")
kl_2003_tl = SBend(l=0.93, angle=0, tilt=1.570796, eid="KL.2003.TL")


# Hcors
chx_2012_tl = Hcor(l=0.2, eid='CHX.2012.TL')
cnx_2021_tl = Hcor(l=0.3, eid='CNX.2021.TL')

# Vcors
chy_1997_tl = Vcor(l=0.2, eid='CHY.1997.TL')
chy_2004_tl = Vcor(l=0.2, eid='CHY.2004.TL')
cfy_2010_tl = Vcor(l=0.1, eid='CFY.2010.TL')
chy_2012_tl = Vcor(l=0.2, eid='CHY.2012.TL')
cny_2021_tl = Vcor(l=0.3, eid='CNY.2021.TL')

# Monitors
bpma_1995_tl = Monitor(eid='BPMA.1995.TL')
bpma_2011_tl = Monitor(eid='BPMA.2011.TL')
bpmd_2022_tl = Monitor(eid='BPMD.2022.TL')

# Markers
ensub_2025_tl = Marker(eid='ENSUB.2025.TL')

# Lattice 
cell = (id_60730788_, qk_1982_tl, d_3, bpma_1995_tl, d_4, qf_1997_tl, d_5, chy_1997_tl, id_71590683_, 
kl_1998_tl, d_7, kl_1999_tl, d_7, kl_2000_tl, d_9, kl_2001_tl, d_7, kl_2002_tl, d_7, 
kl_2003_tl, d_12, chy_2004_tl, d_13, cfy_2010_tl, d_14, bpma_2011_tl, d_15, qf_2012_tl, d_16, 
chx_2012_tl, d_17, chy_2012_tl, d_18, cnx_2021_tl, d_19, cny_2021_tl, d_20, bpmd_2022_tl, id_79622812_, 
ensub_2025_tl)

# power supplies 

#  
qk_1982_tl.ps_id = 'QK.1.TL'
qf_1997_tl.ps_id = 'QF.2.TL'
qf_2012_tl.ps_id = 'QF.1.TL'

#  

#  

#  

#  
kl_1998_tl.ps_id = 'KL.1998.TL'
kl_1999_tl.ps_id = 'KL.1999.TL'
kl_2000_tl.ps_id = 'KL.2000.TL'
kl_2001_tl.ps_id = 'KL.2001.TL'
kl_2002_tl.ps_id = 'KL.2002.TL'
kl_2003_tl.ps_id = 'KL.2003.TL'
