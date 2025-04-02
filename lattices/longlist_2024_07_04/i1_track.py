from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 55.7981
tws0.beta_y = 55.7981
tws0.alpha_x = 18.1886
tws0.alpha_y = 18.1886
tws0.E = 0.005
tws0.s = 23.2

# Drifts
id_97509745_ = Drift(l=0.276, eid='ID_97509745_')
d_2 = Drift(l=0.216, eid='D_2')
d_3 = Drift(l=0.311, eid='D_3')
d_4 = Drift(l=0.047, eid='D_4')
id_70110258_ = Drift(l=1.101, eid='ID_70110258_')
id_41101705_ = Drift(l=0.421, eid='ID_41101705_')
id_79148922_ = Drift(l=0.8992, eid='ID_79148922_')
d_13 = Drift(l=0.3459, eid='D_13')
d_16 = Drift(l=0.3458999999999992, eid='D_16')
d_20 = Drift(l=0.2043, eid='D_20')
d_21 = Drift(l=0.0432, eid='D_21')
d_23 = Drift(l=0.085, eid='D_23')
id_32151375_ = Drift(l=0.6789999999999999, eid='ID_32151375_')
d_26 = Drift(l=0.1282, eid='D_26')
d_28 = Drift(l=0.202, eid='D_28')
d_29 = Drift(l=0.262, eid='D_29')
id_95966272_ = Drift(l=2.8244499999999997, eid='ID_95966272_')
id_18462951_ = Drift(l=0.20765, eid='ID_18462951_')
id_94338373_ = Drift(l=0.096, eid='ID_94338373_')
id_7308930_ = Drift(l=0.33715, eid='ID_7308930_')
d_43 = Drift(l=0.08115, eid='D_43')
d_44 = Drift(l=0.051165, eid='D_44')
d_45 = Drift(l=0.100827, eid='D_45')
id_71696616_ = Drift(l=0.284415, eid='ID_71696616_')
id_19200616_ = Drift(l=0.28075, eid='ID_19200616_')
id_36806288_ = Drift(l=0.225165, eid='ID_36806288_')
d_52 = Drift(l=0.100828, eid='D_52')
id_32378225_ = Drift(l=0.13231500000000002, eid='ID_32378225_')
id_27968780_ = Drift(l=0.38964, eid='ID_27968780_')
d_57 = Drift(l=0.303, eid='D_57')
d_58 = Drift(l=0.1015, eid='D_58')
id_73735098_ = Drift(l=0.27965, eid='ID_73735098_')
d_61 = Drift(l=0.05115, eid='D_61')
d_63 = Drift(l=0.7143, eid='D_63')
id_61843027_ = Drift(l=0.75615, eid='ID_61843027_')
d_66 = Drift(l=0.175, eid='D_66')
d_67 = Drift(l=0.15, eid='D_67')
d_68 = Drift(l=0.13115, eid='D_68')
d_74 = Drift(l=0.275, eid='D_74')
d_75 = Drift(l=0.18115, eid='D_75')
d_76 = Drift(l=0.20115, eid='D_76')
d_77 = Drift(l=0.38, eid='D_77')
d_78 = Drift(l=0.28115, eid='D_78')
d_79 = Drift(l=0.62715, eid='D_79')
id_46725788_ = Drift(l=0.38515, eid='ID_46725788_')
id_62624181_ = Drift(l=0.53115, eid='ID_62624181_')

# Quadrupoles
qln_23_i1 = Quadrupole(l=0.05, eid='QLN.23.I1')
qls_23_i1 = Quadrupole(l=0.05, tilt=0.785398163, eid='QLS.23.I1')
q_37_i1 =  Quadrupole(l=0.21360, k1=-1.458023e+00, eid="Q.37.I1")
q_38_i1 =  Quadrupole(l=0.21360, k1=1.440045e+00, eid="Q.38.I1")
qi_46_i1 = Quadrupole(l=0.23770, k1=2.388532e-01, eid="QI.46.I1")
qi_47_i1 = Quadrupole(l=0.23770, k1=1.854469e-01, eid="QI.47.I1")
qi_50_i1 = Quadrupole(l=0.23770, k1=-6.861892e-01, eid="QI.50.I1")
qi_52_i1 = Quadrupole(l=0.2377, k1=-0.3522076140008414, eid='QI.52.I1')
qi_53_i1 = Quadrupole(l=0.2377, k1=2.104794185999159, eid='QI.53.I1')
qi_54_i1 = Quadrupole(l=0.2377, k1=0.7943661063020614, eid='QI.54.I1')
qi_55_i1 = Quadrupole(l=0.2377, k1=-2.6383360780016827, eid='QI.55.I1')
qi_57_i1 = Quadrupole(l=0.2377, k1=3.2780620240008416, eid='QI.57.I1')
qi_59_i1 = Quadrupole(l=0.2377, k1=-2.6383360780016827, eid='QI.59.I1')
qi_60_i1 = Quadrupole(l=0.2377, k1=1.9778194619983174, eid='QI.60.I1')
qi_61_i1 = Quadrupole(l=0.2377, k1=0.8708619870004207, eid='QI.61.I1')

# SBends
bl_48i_i1 = SBend(l=0.2, angle=-0.099484, e2=-0.099484, eid='BL.48I.I1')
bl_48ii_i1 = SBend(l=0.2, angle=0.099484, e1=0.099484, eid='BL.48II.I1')
bl_50i_i1 = SBend(l=0.2, angle=0.099484, e2=0.099484, eid='BL.50I.I1')
bl_50ii_i1 = SBend(l=0.2, angle=-0.099484, e1=-0.099484, eid='BL.50II.I1')

# Hcors
ckx_23_i1 = Hcor(l=0.025, eid='CKX.23.I1')
ckx_24_i1 = Hcor(l=0.025, eid='CKX.24.I1')
ckx_25_i1 = Hcor(l=0.025, eid='CKX.25.I1')
cx_37_i1 = Hcor(eid='CX.37.I1')
cx_39_i1 = Hcor(eid='CX.39.I1')
cwx_47_i1 = Hcor(eid='CWX.47.I1')
cix_51_i1 = Hcor(l=0.1, eid='CIX.51.I1')
cix_57_i1 = Hcor(l=0.1, eid='CIX.57.I1')

# Vcors
cky_23_i1 = Vcor(l=0.025, eid='CKY.23.I1')
cky_24_i1 = Vcor(l=0.025, eid='CKY.24.I1')
cky_25_i1 = Vcor(l=0.025, eid='CKY.25.I1')
cy_37_i1 = Vcor(eid='CY.37.I1')
cy_39_i1 = Vcor(eid='CY.39.I1')
cwy_47_i1 = Vcor(eid='CWY.47.I1')
ciy_51_i1 = Vcor(l=0.1, eid='CIY.51.I1')
ciy_55_i1 = Vcor(l=0.1, eid='CIY.55.I1')
ciy_58_i1 = Vcor(l=0.1, eid='CIY.58.I1')

# Undulators
u74_49_i1 = Undulator(lperiod=0.074, nperiods=12.405405405405407, Kx=1.294, Ky=0.0, eid='U74.49.I1')
#u74_49_i1 = Undulator(lperiod=0.074, nperiods=10, Kx=1.294, Ky=0.0,eid='U74.49.I1')
# Cavitys
c_a1_1_1_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.1.I1')
c_a1_1_2_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.2.I1')
c_a1_1_3_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.3.I1')
c_a1_1_4_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.4.I1')
c_a1_1_5_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.5.I1')
c_a1_1_6_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.6.I1')
c_a1_1_7_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.7.I1')
c_a1_1_8_i1 = Cavity(l=1.0377, v=0.018125, freq=1300000000.0, eid='C.A1.1.8.I1')
c3_ah1_1_1_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.1.I1')
c3_ah1_1_2_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.2.I1')
c3_ah1_1_3_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.3.I1')
c3_ah1_1_4_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.4.I1')
c3_ah1_1_5_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.5.I1')
c3_ah1_1_6_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.6.I1')
c3_ah1_1_7_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.7.I1')
c3_ah1_1_8_i1 = Cavity(l=0.346, v=0.0025, phi=180.0, freq=3900000000.0, eid='C3.AH1.1.8.I1')
tdsa_52_i1 = TDCavity(l=0.7, freq=3_000_000_000.0, eid='TDSA.52.I1')

# Solenoids
solb_23_i1 = Solenoid(eid='SOLB.23.I1')

# Monitors
bpmg_24_i1 = Monitor(eid='BPMG.24.I1')
bpmg_25i_i1 = Monitor(eid='BPMG.25I.I1')
bpmc_38i_i1 = Monitor(eid='BPMC.38I.I1')
bpmr_38ii_i1 = Monitor(eid='BPMR.38II.I1')
bpmf_47_i1 = Monitor(eid='BPMF.47.I1')
bpmf_48_i1 = Monitor(eid='BPMF.48.I1')
bpmf_52_i1 = Monitor(eid='BPMF.52.I1')
bpma_55_i1 = Monitor(eid='BPMA.55.I1')
bpma_57_i1 = Monitor(eid='BPMA.57.I1')
bpma_59_i1 = Monitor(eid='BPMA.59.I1')
bpma_60_i1 = Monitor(eid='BPMA.60.I1')

# Markers
stsec_23_i1 = Marker(eid='STSEC.23.I1')
match_37_i1 = Marker(eid='MATCH.37.I1')
stlat_47_i1 = Marker(eid='STLAT.47.I1')
match_52_i1 = Marker(eid='MATCH.52.I1')
match_55_i1 = Marker(eid='MATCH.55.I1')
otrc_55_i1 = Marker(eid='OTRC.55.I1')
otrc_56_i1 = Marker(eid='OTRC.56.I1')
otrc_58_i1 = Marker(eid='OTRC.58.I1')
otrc_59_i1 = Marker(eid='OTRC.59.I1')
stsub_62_i1 = Marker(eid='STSUB.62.I1')

# Markers added manually
d_8_1 = Drift(l=0.5776, eid='D_12')
start_sim = Marker(eid="START_SIM")
d_8_2 = Drift(l=id_79148922_.l - d_8_1.l)
d_8_n = (d_8_1, start_sim, d_8_2)

a1_sim_stop = Marker()
a1_1_stop = Marker()
ah_stop = Marker()

tds_start = Marker()
tds_stop = Marker()

lh_start = Marker()
lh_stop = Marker()

# Lattice 
cell = (stsec_23_i1, id_97509745_, solb_23_i1, qln_23_i1, qls_23_i1, d_2, ckx_23_i1, cky_23_i1, d_3, 
ckx_24_i1, cky_24_i1, d_4, bpmg_24_i1, id_70110258_, bpmg_25i_i1, id_41101705_, ckx_25_i1, cky_25_i1, d_8_n,
c_a1_1_1_i1, a1_1_stop, d_13, c_a1_1_2_i1, d_13, c_a1_1_3_i1, d_13, c_a1_1_4_i1, d_16, c_a1_1_5_i1, d_13,
c_a1_1_6_i1, d_13, c_a1_1_7_i1, d_13, c_a1_1_8_i1, a1_sim_stop, d_20, match_37_i1, d_21, q_37_i1, d_21,
cx_37_i1, cy_37_i1, d_23, bpmc_38i_i1, id_32151375_, bpmr_38ii_i1, d_26, q_38_i1, d_21, cx_39_i1, 
cy_39_i1, d_28, c3_ah1_1_1_i1, d_29, c3_ah1_1_2_i1, d_29, c3_ah1_1_3_i1, d_29, c3_ah1_1_4_i1, d_29, 
c3_ah1_1_5_i1, d_29, c3_ah1_1_6_i1, d_29, c3_ah1_1_7_i1, d_29, c3_ah1_1_8_i1, ah_stop, id_95966272_, qi_46_i1, id_18462951_,
bpmf_47_i1, id_94338373_, cwx_47_i1, cwy_47_i1, id_7308930_, qi_47_i1, d_43, stlat_47_i1, d_44, bl_48i_i1, 
d_45, bl_48ii_i1, id_71696616_, bpmf_48_i1, id_19200616_, lh_start, u74_49_i1, lh_stop, id_36806288_, bl_50i_i1, d_52, bl_50ii_i1,
id_32378225_, qi_50_i1, id_27968780_, ciy_51_i1, d_57, cix_51_i1, d_58, bpmf_52_i1, id_73735098_, match_52_i1, 
qi_52_i1, d_61, tds_start, tdsa_52_i1, tds_stop, d_61, qi_53_i1, d_63, qi_54_i1, id_61843027_, match_55_i1, otrc_55_i1,
d_66, ciy_55_i1, d_67, bpma_55_i1, d_68, qi_55_i1, id_61843027_, otrc_56_i1, d_66, cix_57_i1, 
d_67, bpma_57_i1, d_68, qi_57_i1, id_61843027_, otrc_58_i1, d_74, ciy_58_i1, d_75, qi_59_i1, 
d_76, bpma_59_i1, d_77, otrc_59_i1, d_78, qi_60_i1, d_79, bpma_60_i1, id_46725788_, qi_61_i1, 
id_62624181_, stsub_62_i1)

# power supplies 

#  
qln_23_i1.ps_id = 'QLN.23.I1'
qls_23_i1.ps_id = 'QLS.23.I1'
q_37_i1.ps_id = 'Q.A1.1.I1'
q_38_i1.ps_id = 'Q.AH1.1.I1'
qi_46_i1.ps_id = 'QI.1.I1'
qi_47_i1.ps_id = 'QI.2.I1'
qi_50_i1.ps_id = 'QI.3.I1'
qi_52_i1.ps_id = 'QI.4.I1'
qi_53_i1.ps_id = 'QI.5.I1'
qi_54_i1.ps_id = 'QI.6.I1'
qi_55_i1.ps_id = 'QI.7.I1'
qi_57_i1.ps_id = 'QI.8.I1'
qi_59_i1.ps_id = 'QI.9.I1'
qi_60_i1.ps_id = 'QI.11.I1'
qi_61_i1.ps_id = 'QI.12.I1'

#  

#  

#  
c_a1_1_1_i1.ps_id = 'C.A1.I1'
c_a1_1_2_i1.ps_id = 'C.A1.I1'
c_a1_1_3_i1.ps_id = 'C.A1.I1'
c_a1_1_4_i1.ps_id = 'C.A1.I1'
c_a1_1_5_i1.ps_id = 'C.A1.I1'
c_a1_1_6_i1.ps_id = 'C.A1.I1'
c_a1_1_7_i1.ps_id = 'C.A1.I1'
c_a1_1_8_i1.ps_id = 'C.A1.I1'
c3_ah1_1_1_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_2_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_3_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_4_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_5_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_6_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_7_i1.ps_id = 'C3.AH1.I1'
c3_ah1_1_8_i1.ps_id = 'C3.AH1.I1'
tdsa_52_i1.ps_id = 'TDSA.I1'

#  
bl_48i_i1.ps_id = 'BL.1.I1'
bl_48ii_i1.ps_id = 'BL.1.I1'
bl_50i_i1.ps_id = 'BL.3.I1'
bl_50ii_i1.ps_id = 'BL.4.I1'
