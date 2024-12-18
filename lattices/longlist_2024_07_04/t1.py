from ocelot import * 
from ocelot.cpbd.elements import *
#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 10.776023018690426
tws0.beta_y = 39.48730762141566
tws0.alpha_x = 0.6698245190372976
tws0.alpha_y = -2.0320682898456615
tws0.E = 14
tws0.s = 2025.3865970000204

# Drifts
d_2 = Drift(l=3.500022, eid='D_2')
d_3 = Drift(l=0.5, eid='D_3')
id_78732084_ = Drift(l=7.025005999999999, eid='ID_78732084_')
d_7 = Drift(l=0.20895, eid='D_7')
d_8 = Drift(l=0.15395, eid='D_8')
d_9 = Drift(l=1.22435, eid='D_9')
d_10 = Drift(l=1.710028, eid='D_10')
d_13 = Drift(l=4.379405, eid='D_13')
d_14 = Drift(l=0.8568, eid='D_14')
d_15 = Drift(l=2.976816, eid='D_15')
d_18 = Drift(l=0.22435, eid='D_18')
d_19 = Drift(l=5.029084, eid='D_19')
d_20 = Drift(l=0.275, eid='D_20')
d_23 = Drift(l=3.3318, eid='D_23')
d_24 = Drift(l=1.277982, eid='D_24')
d_27 = Drift(l=7.218425, eid='D_27')
d_28 = Drift(l=0.500002, eid='D_28')
d_29 = Drift(l=0.500001, eid='D_29')
d_31 = Drift(l=0.275002, eid='D_31')
d_34 = Drift(l=0.23, eid='D_34')
d_35 = Drift(l=3.62, eid='D_35')
d_36 = Drift(l=0.27, eid='D_36')
d_37 = Drift(l=3.42, eid='D_37')
d_39 = Drift(l=3.72, eid='D_39')
d_43 = Drift(l=11.005, eid='D_43')
id_39225354_ = Drift(l=13.505, eid='ID_39225354_')
id_37674827_ = Drift(l=10.905, eid='ID_37674827_')
d_65 = Drift(l=4.02, eid='D_65')
d_66 = Drift(l=6.401125, eid='D_66')
d_67 = Drift(l=0.21815, eid='D_67')
d_68 = Drift(l=0.17815, eid='D_68')
d_69 = Drift(l=0.125, eid='D_69')
d_70 = Drift(l=2.1675, eid='D_70')
d_71 = Drift(l=1.8267, eid='D_71')
d_72 = Drift(l=0.15, eid='D_72')
d_73 = Drift(l=0.4323, eid='D_73')
d_74 = Drift(l=0.18665, eid='D_74')
id_95602070_ = Drift(l=0.04015, eid='ID_95602070_')

# Quadrupoles
qf_2041_t1 = Quadrupole(l=0.5321, k1=0.3152129371001691, eid='QF.2041.T1')
qf_2045_t1 = Quadrupole(l=0.5321, k1=-0.32369191230031946, eid='QF.2045.T1')
qf_2055_t1 = Quadrupole(l=0.5321, k1=0.15454609750046983, eid='QF.2055.T1')
qf_2063_t1 = Quadrupole(l=0.5321, k1=-0.3389276572993798, eid='QF.2063.T1')
qf_2069_t1 = Quadrupole(l=0.5321, k1=0.282283084600639, eid='QF.2069.T1')
qf_2083_t1 = Quadrupole(l=0.5321, k1=-0.19486095489945496, eid='QF.2083.T1')
qf_2098_t1 = Quadrupole(l=0.5321, k1=0.1711531861999624, eid='QF.2098.T1')
qf_2110_t1 = Quadrupole(l=0.5321, k1=-0.16747232019921066, eid='QF.2110.T1')
qf_2124_t1 = Quadrupole(l=0.5321, k1=0.12999663750046983, eid='QF.2124.T1')
qf_2139_t1 = Quadrupole(l=0.5321, k1=-0.1257752891993986, eid='QF.2139.T1')
qf_2153_t1 = Quadrupole(l=0.5321, k1=0.11681319299943618, eid='QF.2153.T1')
qf_2168_t1 = Quadrupole(l=0.5321, k1=-0.1272886595996993, eid='QF.2168.T1')
qf_2180_t1 = Quadrupole(l=0.5321, k1=0.12020166719977447, eid='QF.2180.T1')
qa_2191_t1 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2191.T1')
qa_2197_t1 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2197.T1')

# SBends
bz_2025_t1 = SBend(l=1.0, angle=-0.00550002773, e2=-0.005500028, tilt=0.21321543, eid='BZ.2025.T1')
bz_2030_t1 = SBend(l=1.0, angle=-0.00550002773, e1=-0.002750014, e2=-0.002750014, eid='BZ.2030.T1')
bz_2031_t1 = SBend(l=1.0, angle=-0.00550002773, e1=-0.002750014, e2=-0.002750014, eid='BZ.2031.T1')
bz_2033_t1 = SBend(l=1.0, angle=-0.00550002773, e1=-0.002750014, e2=-0.002750014, eid='BZ.2033.T1')
bd_2050_t1 = SBend(l=1.0, angle=0.00303654925, e1=0.001518275, e2=0.001518275, eid='BD.2050.T1')
bd_2062_t1 = SBend(l=1.0, angle=0.00303654925, e1=0.001518275, e2=0.001518275, eid='BD.2062.T1')
bd_2077_t1 = SBend(l=1.0, angle=-0.005827964456, e1=-0.002913982, e2=-0.002913982, eid='BD.2077.T1')
bd_2079_t1 = SBend(l=1.0, angle=-0.005827964456, e1=-0.002913982, e2=-0.002913982, eid='BD.2079.T1')
bd_2080_t1 = SBend(l=1.0, angle=-0.005827964456, e1=-0.002913982, e2=-0.002913982, eid='BD.2080.T1')
bd_2082_t1 = SBend(l=1.0, angle=-0.005827964456, e1=-0.002913982, e2=-0.002913982, eid='BD.2082.T1')
bd_2084_t1 = SBend(l=1.0, angle=0.001913314532, e1=0.000956657, e2=0.000956657, tilt=1.570796327, eid='BD.2084.T1')
bd_2097_t1 = SBend(l=1.0, angle=-0.001913314532, e1=-0.000956657, e2=-0.000956657, tilt=1.570796327, eid='BD.2097.T1')

# Sextupoles
sa_2052_t1 = Sextupole(l=0.3164, k2=-5.974177089001264, tilt=-0.095993109, eid='SA.2052.T1')
sa_2067_t1 = Sextupole(l=0.3164, k2=-1.7090884390012642, tilt=-0.322885912, eid='SA.2067.T1')

# Octupoles
oa_2042_t1 = Octupole(l=0.2113, k3=-132.8835386, tilt=-0.13962634, eid='OA.2042.T1')
oa_2056_t1 = Octupole(l=0.2113, k3=-186.9089832, tilt=-0.270526034, eid='OA.2056.T1')

# Hcors
cfx_2041_t1 = Hcor(l=0.1, eid='CFX.2041.T1')
cfx_2056_t1 = Hcor(l=0.1, eid='CFX.2056.T1')
cfx_2069_t1 = Hcor(l=0.1, eid='CFX.2069.T1')
cfx_2089_t1 = Hcor(l=0.1, eid='CFX.2089.T1')
cfx_2098_t1 = Hcor(l=0.1, eid='CFX.2098.T1')
cfx_2125_t1 = Hcor(l=0.1, eid='CFX.2125.T1')
cfx_2154_t1 = Hcor(l=0.1, eid='CFX.2154.T1')
cfx_2180_t1 = Hcor(l=0.1, eid='CFX.2180.T1')
cex_2192_t1 = Hcor(l=0.1, eid='CEX.2192.T1')
cex_2196_t1 = Hcor(l=0.1, eid='CEX.2196.T1')

# Vcors
cfy_2045_t1 = Vcor(l=0.1, eid='CFY.2045.T1')
cfy_2063_t1 = Vcor(l=0.1, eid='CFY.2063.T1')
cfy_2083_t1 = Vcor(l=0.1, eid='CFY.2083.T1')
cfy_2092_t1 = Vcor(l=0.1, eid='CFY.2092.T1')
cfy_2110_t1 = Vcor(l=0.1, eid='CFY.2110.T1')
cfy_2139_t1 = Vcor(l=0.1, eid='CFY.2139.T1')
cfy_2168_t1 = Vcor(l=0.1, eid='CFY.2168.T1')
cny_2191_t1 = Vcor(l=0.3, eid='CNY.2191.T1')
cny_2196_t1 = Vcor(l=0.3, eid='CNY.2196.T1')

# Undulators
u40s_2194_t1 = Undulator(lperiod=0.04, nperiods=3.0, eid='U40S.2194.T1')

# Monitors
bpma_2040_t1 = Monitor(eid='BPMA.2040.T1')
bpma_2044_t1 = Monitor(eid='BPMA.2044.T1')
bpma_2055_t1 = Monitor(eid='BPMA.2055.T1')
bpma_2062_t1 = Monitor(eid='BPMA.2062.T1')
bpma_2068_t1 = Monitor(eid='BPMA.2068.T1')
bpma_2082_t1 = Monitor(eid='BPMA.2082.T1')
bpma_2088_t1 = Monitor(eid='BPMA.2088.T1')
bpma_2092_t1 = Monitor(eid='BPMA.2092.T1')
bpma_2097_t1 = Monitor(eid='BPMA.2097.T1')
bpma_2109_t1 = Monitor(eid='BPMA.2109.T1')
bpma_2124_t1 = Monitor(eid='BPMA.2124.T1')
bpma_2138_t1 = Monitor(eid='BPMA.2138.T1')
bpma_2153_t1 = Monitor(eid='BPMA.2153.T1')
bpma_2167_t1 = Monitor(eid='BPMA.2167.T1')
bpma_2179_t1 = Monitor(eid='BPMA.2179.T1')
bpma_2184_t1 = Monitor(eid='BPMA.2184.T1')
bpme_2191_t1 = Monitor(eid='BPME.2191.T1')
bpme_2197_t1 = Monitor(eid='BPME.2197.T1')

# Markers
stsub_2025_t1 = Marker(eid='STSUB.2025.T1')
ensec_2197_t1 = Marker(eid='ENSEC.2197.T1')


# XYQuadrupoles
#qk_2027_tl = XYQuadrupole(l=1.0552, x_offs=0.0081538, y_offs=0.02356075, k1=-0.09035541, eid='QK.2027.TL')
xBend = Bend(l=0.005276, angle= -7.791933105545399e-05, k1=-0.090359600075815)
yBend = Bend(l=0.005276, angle= 1.181521439452105e-05, k1=0.090359600075815, tilt=np.pi/2)
qk_2027_tl = ([yBend]*19 + [xBend]) * 10
# Drifts
d_1_1 = Drift(l=0.472401, eid='D_1_1')
d_2_1 = Drift(l=1.972421, eid='D_2_1')

# Lattice 
cell = (stsub_2025_t1, bz_2025_t1, d_1_1, qk_2027_tl, d_2_1, bz_2030_t1, d_3, bz_2031_t1, d_3, bz_2033_t1, id_78732084_,
bpma_2040_t1, d_7, qf_2041_t1, d_8, cfx_2041_t1, d_9, oa_2042_t1, d_10, bpma_2044_t1, d_7, 
qf_2045_t1, d_8, cfy_2045_t1, d_13, bd_2050_t1, d_14, sa_2052_t1, d_15, bpma_2055_t1, d_7, 
qf_2055_t1, d_8, cfx_2056_t1, d_18, oa_2056_t1, d_19, bd_2062_t1, d_20, bpma_2062_t1, d_7, 
qf_2063_t1, d_8, cfy_2063_t1, d_23, sa_2067_t1, d_24, bpma_2068_t1, d_7, qf_2069_t1, d_8, 
cfx_2069_t1, d_27, bd_2077_t1, d_28, bd_2079_t1, d_29, bd_2080_t1, d_3, bd_2082_t1, d_31, 
bpma_2082_t1, d_7, qf_2083_t1, d_8, cfy_2083_t1, d_34, bd_2084_t1, d_35, bpma_2088_t1, d_36, 
cfx_2089_t1, d_37, bpma_2092_t1, d_36, cfy_2092_t1, d_39, bd_2097_t1, d_20, bpma_2097_t1, d_7, 
qf_2098_t1, d_8, cfx_2098_t1, d_43, bpma_2109_t1, d_7, qf_2110_t1, d_8, cfy_2110_t1, id_39225354_, 
bpma_2124_t1, d_7, qf_2124_t1, d_8, cfx_2125_t1, id_39225354_, bpma_2138_t1, d_7, qf_2139_t1, d_8, 
cfy_2139_t1, id_39225354_, bpma_2153_t1, d_7, qf_2153_t1, d_8, cfx_2154_t1, id_39225354_, bpma_2167_t1, d_7, 
qf_2168_t1, d_8, cfy_2168_t1, id_37674827_, bpma_2179_t1, d_7, qf_2180_t1, d_8, cfx_2180_t1, d_65, 
bpma_2184_t1, d_66, bpme_2191_t1, d_67, qa_2191_t1, d_68, cny_2191_t1, d_69, cex_2192_t1, d_70, 
u40s_2194_t1, d_71, cny_2196_t1, d_72, cex_2196_t1, d_73, bpme_2197_t1, d_74, qa_2197_t1, id_95602070_, 
ensec_2197_t1)

# power supplies 

#  
qf_2041_t1.ps_id = 'QF.1.T1'
qf_2045_t1.ps_id = 'QF.2.T1'
qf_2055_t1.ps_id = 'QF.3.T1'
qf_2063_t1.ps_id = 'QF.4.T1'
qf_2069_t1.ps_id = 'QF.5.T1'
qf_2083_t1.ps_id = 'QF.6.T1'
qf_2098_t1.ps_id = 'QF.7.T1'
qf_2110_t1.ps_id = 'QF.8.T1'
qf_2124_t1.ps_id = 'QF.9.T1'
qf_2139_t1.ps_id = 'QF.10.T1'
qf_2153_t1.ps_id = 'QF.11.T1'
qf_2168_t1.ps_id = 'QF.12.T1'
qf_2180_t1.ps_id = 'QF.13.T1'
qa_2191_t1.ps_id = 'QA.1.T1'
qa_2197_t1.ps_id = 'QA.2.T1'

#  
sa_2052_t1.ps_id = 'SA.1.T1'
sa_2067_t1.ps_id = 'SA.2.T1'

#  
oa_2042_t1.ps_id = 'OA.1.T1'
oa_2056_t1.ps_id = 'OA.2.T1'

#  

#  
bz_2025_t1.ps_id = 'BZ.1.T1'
bz_2030_t1.ps_id = 'BZ.2.T1'
bz_2031_t1.ps_id = 'BZ.2.T1'
bz_2033_t1.ps_id = 'BZ.2.T1'
bd_2050_t1.ps_id = 'BD.2.T1'
bd_2062_t1.ps_id = 'BD.2.T1'
bd_2077_t1.ps_id = 'BD.1.T1'
bd_2079_t1.ps_id = 'BD.1.T1'
bd_2080_t1.ps_id = 'BD.1.T1'
bd_2082_t1.ps_id = 'BD.1.T1'
bd_2084_t1.ps_id = 'BD.3.T1'
bd_2097_t1.ps_id = 'BD.4.T1'
