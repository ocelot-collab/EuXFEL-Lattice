from ocelot import * 

# Drifts
d_1960 = Drift(l=1.4724009999999907, eid='D_1960')
d_1961 = Drift(l=13.997421000000259, eid='D_1961')
d_1962 = Drift(l=0.20895100000007005, eid='D_1962')
d_1963 = Drift(l=0.1539510000000064, eid='D_1963')
d_1964 = Drift(l=11.370000000000118, eid='D_1964')
d_1965 = Drift(l=0.17000000000030013, eid='D_1965')
d_1966 = Drift(l=0.2699999999999818, eid='D_1966')
d_1967 = Drift(l=1.7424010000002, eid='D_1967')
d_1968 = Drift(l=0.47244100000011713, eid='D_1968')

# Quadrupoles
qk_2027_tl = Quadrupole(l=1.0552, k1=-0.09035960007960576, eid='QK.2027.TL')
qf_2042_tl = Quadrupole(l=0.5321, k1=0.17919084760007517, eid='QF.2042.TL')
qk_2057_tl = Quadrupole(l=1.0552, k1=-0.09035960007960576, eid='QK.2057.TL')

# Hcors
cfx_2042_tl = Hcor(l=0.1, eid='CFX.2042.TL')
chx_2054_tl = Hcor(l=0.2, eid='CHX.2054.TL')

# Vcors
chy_2054_tl = Vcor(l=0.2, eid='CHY.2054.TL')

# Monitors
bpma_2041_tl = Monitor(eid='BPMA.2041.TL')
bpma_2054_tl = Monitor(eid='BPMA.2054.TL')

# Markers
stsub_2025_tl = Marker(eid='STSUB.2025.TL')
ensub_2058_tl = Marker(eid='ENSUB.2058.TL')
ensec_2058_tl = Marker(eid='ENSEC.2058.TL')

# Lattice 
cell = (stsub_2025_tl, d_1960, qk_2027_tl, d_1961, bpma_2041_tl, d_1962, qf_2042_tl, d_1963, cfx_2042_tl, 
d_1964, chx_2054_tl, d_1965, chy_2054_tl, d_1966, bpma_2054_tl, d_1967, qk_2057_tl, d_1968, ensub_2058_tl, 
ensec_2058_tl)
