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
#d_2 = Drift(l=2.000002, eid='D_2')
d_3 = Drift(l=0.5, eid='D_3')
d_5 = Drift(l=8.050009, eid='D_5')
d_6 = Drift(l=0.3026, eid='D_6')
d_7 = Drift(l=0.38135, eid='D_7')
d_8 = Drift(l=4.23795, eid='D_8')
d_9 = Drift(l=0.2, eid='D_9')
d_10 = Drift(l=3.546001, eid='D_10')
d_11 = Drift(l=0.500002, eid='D_11')
d_13 = Drift(l=0.31235, eid='D_13')
d_14 = Drift(l=0.20895, eid='D_14')
d_15 = Drift(l=0.15395, eid='D_15')
d_16 = Drift(l=6.0218, eid='D_16')
d_17 = Drift(l=0.260793, eid='D_17')
d_20 = Drift(l=3.88, eid='D_20')
d_22 = Drift(l=0.1418, eid='D_22')
d_23 = Drift(l=1.962924, eid='D_23')
d_24 = Drift(l=9.801347, eid='D_24')
d_27 = Drift(l=2.1218, eid='D_27')
d_28 = Drift(l=1.500337, eid='D_28')
d_29 = Drift(l=5.525001, eid='D_29')
d_32 = Drift(l=11.57414, eid='D_32')
d_35 = Drift(l=6.313742, eid='D_35')
d_36 = Drift(l=1.225001, eid='D_36')
d_39 = Drift(l=6.493894, eid='D_39')
d_42 = Drift(l=9.764269, eid='D_42')
d_43 = Drift(l=0.500173, eid='D_43')
d_45 = Drift(l=0.622486, eid='D_45')
d_46 = Drift(l=0.2509, eid='D_46')
d_47 = Drift(l=0.1935, eid='D_47')
d_48 = Drift(l=0.835, eid='D_48')
d_49 = Drift(l=0.15, eid='D_49')
d_50 = Drift(l=3.1577, eid='D_50')
d_53 = Drift(l=0.622487, eid='D_53')
d_54 = Drift(l=0.500172, eid='D_54')
d_56 = Drift(l=0.611786, eid='D_56')
d_57 = Drift(l=0.1607, eid='D_57')
d_58 = Drift(l=0.3448, eid='D_58')
d_61 = Drift(l=0.2144, eid='D_61')
d_62 = Drift(l=0.558, eid='D_62')
d_64 = Drift(l=0.822, eid='D_64')
id_65092054_ = Drift(l=4.833, eid='ID_65092054_')
id_52324373_ = Drift(l=4.26774, eid='ID_52324373_')

# Quadrupoles
qf_1996_tld = Quadrupole(l=0.5321, k1=-0.17071419800037585, eid='QF.1996.TLD')
qf_2009_tld = Quadrupole(l=0.5321, k1=0.3253644447998496, eid='QF.2009.TLD')
qf_2016_tld = Quadrupole(l=0.5321, k1=-0.33304205750046983, eid='QF.2016.TLD')
qf_2024_tld = Quadrupole(l=0.5321, k1=0.3373289400996053, eid='QF.2024.TLD')
qf_2034_tld = Quadrupole(l=0.5321, k1=-0.30482150999999996, eid='QF.2034.TLD')
qf_2046_tld = Quadrupole(l=0.5321, k1=0.17452716339973687, eid='QF.2046.TLD')
qf_2058_tld = Quadrupole(l=0.5321, k1=-0.09725015276075925, eid='QF.2058.TLD')
qf_2068_tld = Quadrupole(l=0.5321, k1=0.01622291716030821, eid='QF.2068.TLD')
qf_2075_tld = Quadrupole(l=0.5321, k1=-0.016449723520015034, eid='QF.2075.TLD')
qk_2095_tld = Quadrupole(l=1.0552, k1=-0.18126525409969674, eid='QK.2095.TLD')
qk_2103_tld = Quadrupole(l=1.0552, k1=-0.18126525409969674, eid='QK.2103.TLD')
qk_2113_tld = Quadrupole(l=1.0552, k1=0.19471760659969675, eid='QK.2113.TLD')
qk_2115_tld = Quadrupole(l=1.0552, k1=0.19471760659969675, eid='QK.2115.TLD')
qk_2116_tld = Quadrupole(l=1.0552, k1=0.19471760659969675, eid='QK.2116.TLD')
qk_2117_tld = Quadrupole(l=1.0552, k1=0.19471760659969675, eid='QK.2117.TLD')

# SBends
bz_1980_tld = SBend(l=1.0, angle=-0.00550002773, e2=-0.005500028, tilt=1.351193237, eid='BZ.1980.TLD')
bz_1983_tld = SBend(l=1.0, angle=-0.005499885903, e1=-0.002749943, e2=-0.002749943, tilt=1.570796327, eid='BZ.1983.TLD')
bz_1985_tld = SBend(l=1.0, angle=-0.005499885903, e1=-0.002749943, e2=-0.002749943, tilt=1.570796327, eid='BZ.1985.TLD')
bz_1986_tld = SBend(l=1.0, angle=-0.005499885903, e1=-0.002749943, e2=-0.002749943, tilt=1.570796327, eid='BZ.1986.TLD')
bd_2005_tld = SBend(l=1.0, angle=0.007145035231, e1=0.003572518, e2=0.003572518, tilt=1.570796327, eid='BD.2005.TLD')
bd_2006_tld = SBend(l=1.0, angle=0.007145035231, e1=0.003572518, e2=0.003572518, tilt=1.570796327, eid='BD.2006.TLD')
bd_2008_tld = SBend(l=1.0, angle=-0.006696413191, e1=-0.003348207, e2=-0.003348207, eid='BD.2008.TLD')
bd_2039_tld = SBend(l=1.0, angle=-0.006696413191, e1=-0.003348207, e2=-0.003348207, eid='BD.2039.TLD')
bd_2066_tld = SBend(l=1.0, angle=0.008354779726, e1=0.00417739, e2=0.00417739, tilt=1.570796327, eid='BD.2066.TLD')
bv_2087_tld = SBend(l=2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, tilt=1.570796327, eid='BV.2087.TLD')
bv_2090_tld = SBend(l=2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, tilt=1.570796327, eid='BV.2090.TLD')
bv_2093_tld = SBend(l=2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, tilt=1.570796327, eid='BV.2093.TLD')
bv_2105_tld = SBend(l=2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, tilt=1.570796327, eid='BV.2105.TLD')
bv_2108_tld = SBend(l=2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, tilt=1.570796327, eid='BV.2108.TLD')
bv_2111_tld = SBend(l=2.5, angle=0.04072434921, e1=0.020362175, e2=0.020362175, tilt=1.570796327, eid='BV.2111.TLD')

# RBends
sweep_2119_tld = RBend(l=0.64, tilt=-1.570796327, eid='SWEEP.2119.TLD')
sweep_2120_tld = RBend(l=0.64, eid='SWEEP.2120.TLD')

# Sextupoles
sa_2016_tld = Sextupole(l=0.3164, k2=3.222550959001264, tilt=0.401425728, eid='SA.2016.TLD')
sa_2021_tld = Sextupole(l=0.3164, k2=-6.12795586, tilt=0.322885912, eid='SA.2021.TLD')
sa_2037_tld = Sextupole(l=0.3164, k2=-7.494478072999368, tilt=0.628318531, eid='SA.2037.TLD')
sk_2096_tld = Sextupole(l=0.343, k2=1.576496626, tilt=1.570796327, eid='SK.2096.TLD')
sk_2102_tld = Sextupole(l=0.343, k2=1.576496626, tilt=1.570796327, eid='SK.2102.TLD')

# Hcors
cfx_2000_tld = Hcor(l=0.1, eid='CFX.2000.TLD')
cfx_2009_tld = Hcor(l=0.1, eid='CFX.2009.TLD')
cfx_2021_tld = Hcor(l=0.1, eid='CFX.2021.TLD')
cfx_2046_tld = Hcor(l=0.1, eid='CFX.2046.TLD')
cfx_2068_tld = Hcor(l=0.1, eid='CFX.2068.TLD')
cnx_2098_tld = Hcor(l=0.3, eid='CNX.2098.TLD')

# Vcors
cfy_2000_tld = Vcor(l=0.1, eid='CFY.2000.TLD')
cfy_2017_tld = Vcor(l=0.1, eid='CFY.2017.TLD')
cfy_2035_tld = Vcor(l=0.1, eid='CFY.2035.TLD')
cfy_2059_tld = Vcor(l=0.1, eid='CFY.2059.TLD')
cfy_2076_tld = Vcor(l=0.1, eid='CFY.2076.TLD')
cny_2098_tld = Vcor(l=0.3, eid='CNY.2098.TLD')

# Monitors
bpma_1995_tld = Monitor(eid='BPMA.1995.TLD')
bpma_2008_tld = Monitor(eid='BPMA.2008.TLD')
bpma_2016_tld = Monitor(eid='BPMA.2016.TLD')
bpma_2021_tld = Monitor(eid='BPMA.2021.TLD')
bpma_2034_tld = Monitor(eid='BPMA.2034.TLD')
bpma_2045_tld = Monitor(eid='BPMA.2045.TLD')
bpma_2058_tld = Monitor(eid='BPMA.2058.TLD')
bpma_2067_tld = Monitor(eid='BPMA.2067.TLD')
bpma_2075_tld = Monitor(eid='BPMA.2075.TLD')
bpmd_2097_tld = Monitor(eid='BPMD.2097.TLD')
bpmd_2101_tld = Monitor(eid='BPMD.2101.TLD')
bpmd_2113_tld = Monitor(eid='BPMD.2113.TLD')
bpmd_2118_tld = Monitor(eid='BPMD.2118.TLD')
bpmd_2121_tld = Monitor(eid='BPMD.2121.TLD')
bpmw_2126_tld = Monitor(eid='BPMW.2126.TLD')

# Markers
otrc_1995_tld = Marker(eid='OTRC.1995.TLD')
ensec_2130_tld = Marker(eid='ENSEC.2130.TLD')

qk_1982_tl = Quadrupole(l=1.0552, k1=0.09035960007960576, eid='QK.1982.TL')
x_bend = Bend(l=0.005276, angle = +1.180477777265855e-05, k1 = +0.090359600075815)
y_bend = Bend(l=0.005276, angle = -7.780804909999998e-05, k1 = -0.090359600075815, tilt=np.pi/2)
QK = ([x_bend] * 19 + [y_bend])*10

qk_drift = (Drift(l=0.4724), QK, Drift(l=2.000002 - 0.4724 - 1.0552))
# Lattice 
cell = (bz_1980_tld, qk_drift, bz_1983_tld, d_3, bz_1985_tld, d_3, bz_1986_tld, d_5, otrc_1995_tld,
d_6, bpma_1995_tld, d_7, qf_1996_tld, d_8, cfy_2000_tld, d_9, cfx_2000_tld, d_10, bd_2005_tld, 
d_11, bd_2006_tld, d_11, bd_2008_tld, d_13, bpma_2008_tld, d_14, qf_2009_tld, d_15, cfx_2009_tld, 
d_16, sa_2016_tld, d_17, bpma_2016_tld, d_14, qf_2016_tld, d_15, cfy_2017_tld, d_20, bpma_2021_tld, 
d_9, cfx_2021_tld, d_22, sa_2021_tld, d_23, qf_2024_tld, d_24, bpma_2034_tld, d_14, qf_2034_tld, 
d_15, cfy_2035_tld, d_27, sa_2037_tld, d_28, bd_2039_tld, d_29, bpma_2045_tld, d_14, qf_2046_tld, 
d_15, cfx_2046_tld, d_32, bpma_2058_tld, d_14, qf_2058_tld, d_15, cfy_2059_tld, d_35, bd_2066_tld, 
d_36, bpma_2067_tld, d_14, qf_2068_tld, d_15, cfx_2068_tld, d_39, bpma_2075_tld, d_14, qf_2075_tld, 
d_15, cfy_2076_tld, d_42, bv_2087_tld, d_43, bv_2090_tld, d_43, bv_2093_tld, d_45, qk_2095_tld, 
d_46, sk_2096_tld, d_47, bpmd_2097_tld, d_48, cnx_2098_tld, d_49, cny_2098_tld, d_50, bpmd_2101_tld, 
d_47, sk_2102_tld, d_46, qk_2103_tld, d_53, bv_2105_tld, d_54, bv_2108_tld, d_43, bv_2111_tld, 
d_56, bpmd_2113_tld, d_57, qk_2113_tld, d_58, qk_2115_tld, d_58, qk_2116_tld, d_58, qk_2117_tld, 
d_61, bpmd_2118_tld, d_62, sweep_2119_tld, d_3, sweep_2120_tld, d_64, bpmd_2121_tld, id_65092054_, bpmw_2126_tld, 
id_52324373_, ensec_2130_tld)

# power supplies 

#  
qf_1996_tld.ps_id = 'QF.1.TLD'
qf_2009_tld.ps_id = 'QF.2.TLD'
qf_2016_tld.ps_id = 'QF.3.TLD'
qf_2024_tld.ps_id = 'QF.4.TLD'
qf_2034_tld.ps_id = 'QF.5.TLD'
qf_2046_tld.ps_id = 'QF.6.TLD'
qf_2058_tld.ps_id = 'QF.7.TLD'
qf_2068_tld.ps_id = 'QF.8.TLD'
qf_2075_tld.ps_id = 'QF.9.TLD'
qk_2095_tld.ps_id = 'QK.1.TLD'
qk_2103_tld.ps_id = 'QK.1.TLD'
qk_2113_tld.ps_id = 'QK.2.TLD'
qk_2115_tld.ps_id = 'QK.2.TLD'
qk_2116_tld.ps_id = 'QK.3.TLD'
qk_2117_tld.ps_id = 'QK.3.TLD'

#  
sa_2016_tld.ps_id = 'SA.1.TLD'
sa_2021_tld.ps_id = 'SA.2.TLD'
sa_2037_tld.ps_id = 'SA.3.TLD'
sk_2096_tld.ps_id = 'SK.1.TLD'
sk_2102_tld.ps_id = 'SK.1.TLD'

#  

#  

#  
bz_1980_tld.ps_id = 'BZ.1.TLD'
bz_1983_tld.ps_id = 'BZ.2.TLD'
bz_1985_tld.ps_id = 'BZ.2.TLD'
bz_1986_tld.ps_id = 'BZ.2.TLD'
bd_2005_tld.ps_id = 'BD.3.TLD'
bd_2006_tld.ps_id = 'BD.3.TLD'
bd_2008_tld.ps_id = 'BD.5.TLD'
bd_2039_tld.ps_id = 'BD.5.TLD'
bd_2066_tld.ps_id = 'BD.4.TLD'
bv_2087_tld.ps_id = 'BV.1.TLD'
bv_2090_tld.ps_id = 'BV.1.TLD'
bv_2093_tld.ps_id = 'BV.1.TLD'
bv_2105_tld.ps_id = 'BV.1.TLD'
bv_2108_tld.ps_id = 'BV.1.TLD'
bv_2111_tld.ps_id = 'BV.1.TLD'
sweep_2119_tld.ps_id = 'SWEEP.1.TLD'
sweep_2120_tld.ps_id = 'SWEEP.1.TLD'
