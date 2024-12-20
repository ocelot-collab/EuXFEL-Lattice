from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 0.5790415663071324
tws0.beta_y = 2.787247754647999
tws0.alpha_x = -1.4029863567200784
tws0.alpha_y = 0.16729234667447596
tws0.E = 14
tws0.s = 1854.412579000024

# Drifts
id_63873174_ = Drift(l=0.15395, eid='ID_63873174_')
d_3 = Drift(l=0.69, eid='D_3')
d_4 = Drift(l=0.15545, eid='D_4')
d_5 = Drift(l=0.2209, eid='D_5')
d_6 = Drift(l=0.5709, eid='D_6')
id_43590782_ = Drift(l=0.50895, eid='ID_43590782_')
d_10 = Drift(l=0.3015, eid='D_10')
d_11 = Drift(l=2.0865, eid='D_11')
id_28104852_ = Drift(l=0.43245, eid='ID_28104852_')
id_10150471_ = Drift(l=3.3550000000000004, eid='ID_10150471_')
d_17 = Drift(l=0.20895, eid='D_17')
d_19 = Drift(l=3.855, eid='D_19')
id_10626481_ = Drift(l=4.9485, eid='ID_10626481_')
d_24 = Drift(l=2.61545, eid='D_24')
d_25 = Drift(l=2.50395, eid='D_25')
id_70249577_ = Drift(l=4.4485, eid='ID_70249577_')
d_29 = Drift(l=2.53395, eid='D_29')
id_51460630_ = Drift(l=11.83395, eid='ID_51460630_')
id_62113810_ = Drift(l=2.8074500000000002, eid='ID_62113810_')
id_81477652_ = Drift(l=11.25895, eid='ID_81477652_')
id_83218926_ = Drift(l=4.8985, eid='ID_83218926_')
id_54955776_ = Drift(l=6.36045, eid='ID_54955776_')
id_47037829_ = Drift(l=1.5985, eid='ID_47037829_')
d_50 = Drift(l=0.4815, eid='D_50')
id_61581222_ = Drift(l=0.37, eid='ID_61581222_')
d_53 = Drift(l=0.32, eid='D_53')
d_57 = Drift(l=0.283951, eid='D_57')
d_64 = Drift(l=0.41, eid='D_64')
d_65 = Drift(l=1.515, eid='D_65')
d_66 = Drift(l=0.208951, eid='D_66')
d_67 = Drift(l=0.153951, eid='D_67')
d_68 = Drift(l=0.2, eid='D_68')
d_69 = Drift(l=9.0692, eid='D_69')
d_70 = Drift(l=0.1, eid='D_70')
d_71 = Drift(l=0.15, eid='D_71')
id_92907356_ = Drift(l=2.06074, eid='ID_92907356_')

# Quadrupoles
qh_1855_tl = Quadrupole(l=1.0291, k1=0.3716633416004276, eid='QH.1855.TL')
qh_1857_tl = Quadrupole(l=1.0291, k1=0.34605581209989317, eid='QH.1857.TL')
qh_1858_tl = Quadrupole(l=1.0291, k1=-0.3787301584996599, eid='QH.1858.TL')
qh_1859_tl = Quadrupole(l=1.0291, k1=-0.05277408413953941, eid='QH.1859.TL')
qf_1864_tl = Quadrupole(l=0.5321, k1=0.18589860389964288, eid='QF.1864.TL')
qf_1868_tl = Quadrupole(l=0.5321, k1=-0.05512587120090208, eid='QF.1868.TL')
qf_1873_tl = Quadrupole(l=0.5321, k1=0.1199289291993986, eid='QF.1873.TL')
qf_1881_tl = Quadrupole(l=0.5321, k1=-0.20093471310092084, eid='QF.1881.TL')
qf_1892_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid='QF.1892.TL')
qf_1907_tl = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid='QF.1907.TL')
qf_1922_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid='QF.1922.TL')
qf_1937_tl = Quadrupole(l=0.5321, k1=-0.17919084760007517, eid='QF.1937.TL')


# Quads QF.1952.TL and QF.1967.TL replace with combine function SBEND 
qf_1952_tl = SBend(l=0.5321, angle=1.771753973e-04, k1=0.17919084758504, e1=3.025448949E-04,  e2=1.253694976E-04, eid='QF.1952.TL')
qf_1967_tl = SBend(l=0.5321, angle=-6.168830834999999e-04, k1=-0.17919084758504, e1=4.279143925E-04, e2=1.044797476E-03, eid='QF.1967.TL')

# RBends
kspos_1941_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1941.TL')
ksneg_1941_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1941.TL')
kspos_1943_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1943.TL')
ksneg_1943_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1943.TL')
kspos_1945_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1945.TL')
ksneg_1945_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1945.TL')
kspos_1948_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1948.TL')
ksneg_1948_tl = RBend(l=1.0, angle=-3.025448745461549e-05,eid='KSNEG.1948.TL')
kspos_1950_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1950.TL')
ksneg_1950_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1950.TL')
kspos_1953_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1953.TL')
ksneg_1953_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1953.TL')
kspos_1955_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1955.TL')
ksneg_1955_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1955.TL')
kspos_1958_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1958.TL')
ksneg_1958_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1958.TL')
kspos_1960_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1960.TL')
ksneg_1960_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1960.TL')
kspos_1962_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1962.TL')
ksneg_1962_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1962.TL')


# Hcors
chx_1855_tl = Hcor(l=0.2, eid='CHX.1855.TL')
cfx_1864_tl = Hcor(l=0.1, eid='CFX.1864.TL')
cfx_1873_tl = Hcor(l=0.1, eid='CFX.1873.TL')
cfx_1894_tl = Hcor(l=0.1, eid='CFX.1894.TL')
cfx_1925_tl = Hcor(l=0.1, eid='CFX.1925.TL')
bl_1939_tl = Hcor(l=0.2, eid='BL.1939.TL')
bl_1964_tl = Hcor(l=0.2, eid='BL.1964.TL')
chx_1965_tl = Hcor(l=0.2, eid='CHX.1965.TL')
chx_1967_tl = Hcor(l=0.2, eid='CHX.1967.TL')
cnx_1977_tl = Hcor(l=0.3, eid='CNX.1977.TL')

# Vcors
cfy_1854_tl = Vcor(l=0.1, eid='CFY.1854.TL')
chy_1861_tl = Vcor(l=0.2, eid='CHY.1861.TL')
cfy_1869_tl = Vcor(l=0.1, eid='CFY.1869.TL')
cfy_1884_tl = Vcor(l=0.1, eid='CFY.1884.TL')
cfy_1910_tl = Vcor(l=0.1, eid='CFY.1910.TL')
cfy_1937_tl = Vcor(l=0.1, eid='CFY.1937.TL')
chy_1967_tl = Vcor(l=0.2, eid='CHY.1967.TL')
cny_1977_tl = Vcor(l=0.3, eid='CNY.1977.TL')

# Monitors
bpmi_1860_tl = Monitor(eid='BPMI.1860.TL')
bpmi_1863_tl = Monitor(eid='BPMI.1863.TL')
bpma_1868_tl = Monitor(eid='BPMA.1868.TL')
bpma_1873_tl = Monitor(eid='BPMA.1873.TL')
bpmi_1878_tl = Monitor(eid='BPMI.1878.TL')
bpmi_1889_tl = Monitor(eid='BPMI.1889.TL')
bpmi_1910_tl = Monitor(eid='BPMI.1910.TL')
bpmi_1925_tl = Monitor(eid='BPMI.1925.TL')
bpmi_1930_tl = Monitor(eid='BPMI.1930.TL')
bpmi_1939_tl = Monitor(eid='BPMI.1939.TL')
bpma_1966_tl = Monitor(eid='BPMA.1966.TL')
bpmd_1977_tl = Monitor(eid='BPMD.1977.TL')

# Markers
ks_1941_tl = Marker(eid='KS.1941.TL')
ks_1943_tl = Marker(eid='KS.1943.TL')
ks_1945_tl = Marker(eid='KS.1945.TL')
ks_1948_tl = Marker(eid='KS.1948.TL')
ks_1950_tl = Marker(eid='KS.1950.TL')
ks_1953_tl = Marker(eid='KS.1953.TL')
ks_1955_tl = Marker(eid='KS.1955.TL')
ks_1958_tl = Marker(eid='KS.1958.TL')
ks_1960_tl = Marker(eid='KS.1960.TL')
ks_1962_tl = Marker(eid='KS.1962.TL')
ensub_1980_tl = Marker(eid='ENSUB.1980.TL')

# Lattice 
cell = (id_63873174_, cfy_1854_tl, d_3, chx_1855_tl, d_4, qh_1855_tl, d_5, qh_1857_tl, d_6, 
qh_1858_tl, d_5, qh_1859_tl, id_43590782_, bpmi_1860_tl, d_10, chy_1861_tl, d_11, bpmi_1863_tl, id_28104852_, 
qf_1864_tl, id_63873174_, cfx_1864_tl, id_10150471_, bpma_1868_tl, d_17, qf_1868_tl, id_63873174_, cfy_1869_tl, d_19, 
bpma_1873_tl, d_17, qf_1873_tl, id_63873174_, cfx_1873_tl, id_10626481_, bpmi_1878_tl, d_24, qf_1881_tl, d_25, 
cfy_1884_tl, id_70249577_, bpmi_1889_tl, d_24, qf_1892_tl, d_29, cfx_1894_tl, id_51460630_, qf_1907_tl, id_62113810_, 
bpmi_1910_tl, d_10, cfy_1910_tl, id_81477652_, qf_1922_tl, id_62113810_, bpmi_1925_tl, d_10, cfx_1925_tl, id_83218926_, 
bpmi_1930_tl, id_54955776_, qf_1937_tl, id_63873174_, cfy_1937_tl, id_47037829_, bpmi_1939_tl, d_50, bl_1939_tl, id_61581222_, 
kspos_1941_tl, ks_1941_tl, ksneg_1941_tl, d_53, kspos_1943_tl, ks_1943_tl, ksneg_1943_tl, d_53, kspos_1945_tl, ks_1945_tl, 
ksneg_1945_tl, d_53, kspos_1948_tl, ks_1948_tl, ksneg_1948_tl, d_53, kspos_1950_tl, ks_1950_tl, ksneg_1950_tl, d_57, 
qf_1952_tl, d_57, kspos_1953_tl, ks_1953_tl, ksneg_1953_tl, d_53, kspos_1955_tl, ks_1955_tl, ksneg_1955_tl, d_53, 
kspos_1958_tl, ks_1958_tl, ksneg_1958_tl, d_53, kspos_1960_tl, ks_1960_tl, ksneg_1960_tl, d_53, kspos_1962_tl, ks_1962_tl, 
ksneg_1962_tl, id_61581222_, bl_1964_tl, d_64, chx_1965_tl, d_65, bpma_1966_tl, d_66, qf_1967_tl, d_67, 
chx_1967_tl, d_68, chy_1967_tl, d_69, cnx_1977_tl, d_70, cny_1977_tl, d_71, bpmd_1977_tl, id_92907356_, 
ensub_1980_tl)

# power supplies 

#  
qh_1855_tl.ps_id = 'QH.5.TL'
qh_1857_tl.ps_id = 'QH.6.TL'
qh_1858_tl.ps_id = 'QH.7.TL'
qh_1859_tl.ps_id = 'QH.8.TL'
qf_1864_tl.ps_id = 'QF.8.TL'
qf_1868_tl.ps_id = 'QF.9.TL'
qf_1873_tl.ps_id = 'QF.10.TL'
qf_1881_tl.ps_id = 'QF.11.TL'
qf_1892_tl.ps_id = 'QF.1.TL'
qf_1907_tl.ps_id = 'QF.2.TL'
qf_1922_tl.ps_id = 'QF.1.TL'
qf_1937_tl.ps_id = 'QF.2.TL'
qf_1952_tl.ps_id = 'QF.1.TL'
qf_1967_tl.ps_id = 'QF.2.TL'

#  

#  

#  

#  
kspos_1941_tl.ps_id = 'KSPOS.1941.TL'
ksneg_1941_tl.ps_id = 'KSNEG.1941.TL'
kspos_1943_tl.ps_id = 'KSPOS.1943.TL'
ksneg_1943_tl.ps_id = 'KSNEG.1943.TL'
kspos_1945_tl.ps_id = 'KSPOS.1945.TL'
ksneg_1945_tl.ps_id = 'KSNEG.1945.TL'
kspos_1948_tl.ps_id = 'KSPOS.1948.TL'
ksneg_1948_tl.ps_id = 'KSNEG.1948.TL'
kspos_1950_tl.ps_id = 'KSPOS.1950.TL'
ksneg_1950_tl.ps_id = 'KSNEG.1950.TL'
kspos_1953_tl.ps_id = 'KSPOS.1953.TL'
ksneg_1953_tl.ps_id = 'KSNEG.1953.TL'
kspos_1955_tl.ps_id = 'KSPOS.1955.TL'
ksneg_1955_tl.ps_id = 'KSNEG.1955.TL'
kspos_1958_tl.ps_id = 'KSPOS.1958.TL'
ksneg_1958_tl.ps_id = 'KSNEG.1958.TL'
kspos_1960_tl.ps_id = 'KSPOS.1960.TL'
ksneg_1960_tl.ps_id = 'KSNEG.1960.TL'
kspos_1962_tl.ps_id = 'KSPOS.1962.TL'
ksneg_1962_tl.ps_id = 'KSNEG.1962.TL'
