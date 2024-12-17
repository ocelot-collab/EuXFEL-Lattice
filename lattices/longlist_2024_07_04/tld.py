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
d_2 = Drift(l=1.472401, eid='D_2')
d_3 = Drift(l=13.047401, eid='D_3')
d_4 = Drift(l=1.15895, eid='D_4')
d_5 = Drift(l=0.15395, eid='D_5')
id_92438011_ = Drift(l=0.16, eid='ID_92438011_')
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
id_4344751_ = Drift(l=3.533121, eid='ID_4344751_')
d_24 = Drift(l=13.997421, eid='D_24')
d_27 = Drift(l=11.37, eid='D_27')
d_28 = Drift(l=0.17, eid='D_28')
d_29 = Drift(l=0.27, eid='D_29')
d_30 = Drift(l=1.742401, eid='D_30')
id_77895590_ = Drift(l=13.997441, eid='ID_77895590_')
d_33 = Drift(l=0.20895, eid='D_33')
d_35 = Drift(l=6.405, eid='D_35')
d_36 = Drift(l=6.6, eid='D_36')
d_39 = Drift(l=14.005, eid='D_39')
d_42 = Drift(l=14.0051, eid='D_42')
d_45 = Drift(l=12.5482, eid='D_45')

# Quadrupoles
qk_1982_tl = Quadrupole(l=1.0552, k1=0.09035960007960576, eid='QK.1982.TL')
qf_1997_tl = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid='QF.1997.TL')
qf_2012_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid='QF.2012.TL')
qk_2027_tl = Quadrupole(l=1.0552, k1=-0.09035960007960576, eid='QK.2027.TL')
qf_2042_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid='QF.2042.TL')
qk_2057_tl = Quadrupole(l=1.0552, k1=-0.09035960007960576, eid='QK.2057.TL')
qf_2072_t2 = Quadrupole(l=0.5321, k1=0.17919084760007517, eid='QF.2072.T2')
qf_2087_t2 = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid='QF.2087.T2')
qf_2102_t2 = Quadrupole(l=0.5321, k1=0.17919084760007517, eid='QF.2102.T2')
qf_2117_t2 = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid='QF.2117.T2')

# RBends
kl_1998_tl = RBend(l=0.93, tilt=1.570796327, eid='KL.1998.TL')
kl_1999_tl = RBend(l=0.93, tilt=1.570796327, eid='KL.1999.TL')
kl_2000_tl = RBend(l=0.93, tilt=1.570796327, eid='KL.2000.TL')
kl_2001_tl = RBend(l=0.93, tilt=1.570796327, eid='KL.2001.TL')
kl_2002_tl = RBend(l=0.93, tilt=1.570796327, eid='KL.2002.TL')
kl_2003_tl = RBend(l=0.93, tilt=1.570796327, eid='KL.2003.TL')
bd_2079_t2 = RBend(l=1.0, eid='BD.2079.T2')

# Hcors
chx_2012_tl = Hcor(l=0.2, eid='CHX.2012.TL')
cnx_2021_tl = Hcor(l=0.3, eid='CNX.2021.TL')
cfx_2042_tl = Hcor(l=0.1, eid='CFX.2042.TL')
chx_2054_tl = Hcor(l=0.2, eid='CHX.2054.TL')
cfx_2072_t2 = Hcor(l=0.1, eid='CFX.2072.T2')
cfx_2102_t2 = Hcor(l=0.1, eid='CFX.2102.T2')

# Vcors
chy_1997_tl = Vcor(l=0.2, eid='CHY.1997.TL')
chy_2004_tl = Vcor(l=0.2, eid='CHY.2004.TL')
cfy_2010_tl = Vcor(l=0.1, eid='CFY.2010.TL')
chy_2012_tl = Vcor(l=0.2, eid='CHY.2012.TL')
cny_2021_tl = Vcor(l=0.3, eid='CNY.2021.TL')
chy_2054_tl = Vcor(l=0.2, eid='CHY.2054.TL')
cfy_2087_t2 = Vcor(l=0.1, eid='CFY.2087.T2')
cfy_2117_t2 = Vcor(l=0.1, eid='CFY.2117.T2')

# Monitors
bpma_1995_tl = Monitor(eid='BPMA.1995.TL')
bpma_2011_tl = Monitor(eid='BPMA.2011.TL')
bpmd_2022_tl = Monitor(eid='BPMD.2022.TL')
bpma_2041_tl = Monitor(eid='BPMA.2041.TL')
bpma_2054_tl = Monitor(eid='BPMA.2054.TL')
bpma_2071_t2 = Monitor(eid='BPMA.2071.T2')
bpma_2086_t2 = Monitor(eid='BPMA.2086.T2')
bpma_2101_t2 = Monitor(eid='BPMA.2101.T2')
bpma_2116_t2 = Monitor(eid='BPMA.2116.T2')

# Markers
stsub_1980_tl = Marker(eid='STSUB.1980.TL')
ensub_2130_t2 = Marker(eid='ENSUB.2130.T2')

# Lattice 
cell = (stsub_1980_tl, d_2, qk_1982_tl, d_3, bpma_1995_tl, d_4, qf_1997_tl, d_5, chy_1997_tl, 
id_92438011_, kl_1998_tl, d_7, kl_1999_tl, d_7, kl_2000_tl, d_9, kl_2001_tl, d_7, kl_2002_tl, 
d_7, kl_2003_tl, d_12, chy_2004_tl, d_13, cfy_2010_tl, d_14, bpma_2011_tl, d_15, qf_2012_tl, 
d_16, chx_2012_tl, d_17, chy_2012_tl, d_18, cnx_2021_tl, d_19, cny_2021_tl, d_20, bpmd_2022_tl, 
id_4344751_, qk_2027_tl, d_24, bpma_2041_tl, d_15, qf_2042_tl, d_16, cfx_2042_tl, d_27, chx_2054_tl, 
d_28, chy_2054_tl, d_29, bpma_2054_tl, d_30, qk_2057_tl, id_77895590_, bpma_2071_t2, d_33, qf_2072_t2, 
d_5, cfx_2072_t2, d_35, bd_2079_t2, d_36, bpma_2086_t2, d_33, qf_2087_t2, d_5, cfy_2087_t2, 
d_39, bpma_2101_t2, d_33, qf_2102_t2, d_5, cfx_2102_t2, d_42, bpma_2116_t2, d_33, qf_2117_t2, 
d_5, cfy_2117_t2, d_45, ensub_2130_t2)

# power supplies 

#  
qk_1982_tl.ps_id = 'QK.1.TL'
qf_1997_tl.ps_id = 'QF.2.TL'
qf_2012_tl.ps_id = 'QF.1.TL'
qk_2027_tl.ps_id = 'QK.2.TL'
qf_2042_tl.ps_id = 'QF.1.TL'
qk_2057_tl.ps_id = 'QK.2.TL'
qf_2072_t2.ps_id = 'QF.1.T2'
qf_2087_t2.ps_id = 'QF.1.T2'
qf_2102_t2.ps_id = 'QF.1.T2'
qf_2117_t2.ps_id = 'QF.7.T2'

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
bd_2079_t2.ps_id = 'BD.10.T2'
