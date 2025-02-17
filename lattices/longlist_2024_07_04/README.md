# Changes in the LongList
## Renamed:
- SECTION CL to TL which affect this marker ENBLOCK.1891.CL
- SUBSECTION TL to TL5 which affect this marker ENSEC.2058.TL
- SUBSECTION TL to TL1: TL	TL1	XTL_035	STSEC.1854.TL	STSEC.TL.TL	MARK
- in SUBSECTION CL: BENDIN or BENDOUT to MARKER 

## Removed
- U90 CUS elements. it is coils for magnetic earth correction
- all QP quads which are used only for alignment

```python
SA3	UE90	XTD4_003	CUSX.2942.SA3	CUSX.CELL24.SA3	MAGNET
SA3	UE90	XTD4_003	CUSY.2942.SA3	CUSY.CELL24.SA3	MAGNET
SA3	UE90	XTD4_003	QP.2941.SA3	QP.CELL24.SA3	PMAGNET	QUAD	QP
SA3	UE90	XTD4_004	CUSX.2946.SA3	CUSX.CELL25.SA3	MAGNET	HKIC	CUSX
SA3	UE90	XTD4_004	CUSY.2946.SA3	CUSY.CELL25.SA3	MAGNET	HKIC	CUSY
SA3	UE90	XTD4_004	QP.2945.SA3	QP.CELL25.SA3	PMAGNET	QUAD	QP
SA3	UE90	XTD4_004	CUSX.2949.SA3	CUSX.CELL26.SA3	MAGNET	HKIC	CUSX
SA3	UE90	XTD4_004	CUSY.2949.SA3	CUSY.CELL26.SA3	MAGNET	HKIC	CUSY
SA3	UE90	XTD4_004	QP.2948.SA3	QP.CELL26.SA3	PMAGNET	QUAD	QP
SA3	UE90	XTD4_004	CUSX.2953.SA3	CUSX.CELL27.SA3	MAGNET	HKIC	CUSX
SA3	UE90	XTD4_004	CUSY.2953.SA3	CUSY.CELL27.SA3	MAGNET	HKIC	CUSY
SA3	UE90	XTD4_004	QP.2952.SA3	QP.CELL27.SA3	PMAGNET	QUAD	QP
SA3	UE90	XTD4_004	QP.2954.SA3	QP.CELL27.SA3	PMAGNET	QUAD	QP
SA3	UE90	XTD4_004	QP.2947.SA3	QP.CELL25.SA3	PMAGNET	QUAD	QP
SA3	UE90	XTD4_003	QP.2943.SA3	QP.CELL24.SA3	PMAGNET	QUAD	QP
SA3	UE90	XTD4_004	QP.2951.SA3	QP.CELL26.SA3	PMAGNET	QUAD	QP
```
# Changes in lattice files
## i1.py (only markers for S2E)
```python
# Markers added manually
d_8_1 = Drift(l=0.5776, eid='D_12')
start_sim = Marker(eid="START_SIM")
d_8_2 = Drift(l=id_79148922_.l - d_8_1.l)
d_8_n = (d_8_1, start_sim, d_8_2)

a1_sim_stop = Marker()
a1_1_stop = Marker()

tds_start = Marker()
tds_stop = Marker()

lh_start = Marker()
lh_stop = Marker()
```

## In t34_sa2.py
we introduced following changes:

* Quad QF.2012.TL replace with combine function SBEND since beam has displacement in vertical direction
```python
angle_n = -5.715204879e-04 
qf_2012_tl = SBend(l=0.5321, angle=angle_n, k1=-0.1791908476, e1=+1.444493782E-04, e2=+7.159698661E-04, tilt=1.570796, eid='QF.2012.TL')
```

* bending magnets: KL kickers have to be ON to transport beam to SA2 branch
```python
alpha=-0.0001019145217
kl_1998_tl = SBend(l=0.93, angle=alpha, e1=0,        e2=alpha, tilt=1.570796, eid="KL.1998.TL")
kl_1999_tl = SBend(l=0.93, angle=alpha, e1=-alpha,   e2=2*alpha,  tilt=1.570796, eid="KL.1999.TL")
kl_2000_tl = SBend(l=0.93, angle=alpha, e1=-2*alpha, e2=3*alpha,  tilt=1.570796, eid="KL.2000.TL")
kl_2001_tl = SBend(l=0.93, angle=alpha, e1=-3*alpha, e2=4*alpha,  tilt=1.570796, eid="KL.2001.TL")
kl_2002_tl = SBend(l=0.93, angle=alpha, e1=-4*alpha, e2=5*alpha,  tilt=1.570796, eid="KL.2002.TL")
kl_2003_tl = SBend(l=0.93, angle=0, tilt=1.570796, eid="KL.2003.TL")
```

## In tl2_tld.py the following changes were introduced:

# Extraction to TLD: KS kicker setup   
# RBends
```python
kspos_1941_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1941.TL')
ksneg_1941_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1941.TL')
kspos_1943_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1943.TL')
ksneg_1943_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1943.TL')
kspos_1945_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1945.TL')
ksneg_1945_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1945.TL')
kspos_1948_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSPOS.1948.TL')
ksneg_1948_tl = RBend(l=1.0, angle=-3.025448745461549e-05, eid='KSNEG.1948.TL')
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
```

* Quads QF.1952.TL and QF.1967.TL are replaced with combine function SBEND 
```python
qf_1952_tl = SBend(l=0.5321, angle=1.771753973e-04, k1=0.17919084758504, e1=3.025448949E-04,  e2=1.253694976E-04, eid='QF.1952.TL')
qf_1967_tl = SBend(l=0.5321, angle=-6.168830834999999e-04, k1=-0.17919084758504, e1=4.279143925E-04, e2=1.044797476E-03, eid='QF.1967.TL')
```

# t1.py 
* quad QK.2027.TL with offsets in both direction was replaced with sliced combine function magnet
```python
xBend = Bend(l=0.005276, angle= -7.791933105545399e-05, k1=-0.090359600075815)
yBend = Bend(l=0.005276, angle= 1.181521439452105e-05, k1=0.090359600075815, tilt=np.pi/2)
qk_2027_tl = ([yBend]*19 + [xBend]) * 10
```

# tld.py 
* QK.1982.TL quad (beam has offset in both directions) was also replaced with sliced combine function magnet
```python
qk_1982_tl = Quadrupole(l=1.0552, k1=0.09035960007960576, eid='QK.1982.TL')
x_bend = Bend(l=0.005276, angle = +1.180477777265855e-05, k1 = +0.090359600075815)
y_bend = Bend(l=0.005276, angle = -7.780804909999998e-05, k1 = -0.090359600075815, tilt=np.pi/2)
QK = ([x_bend] * 19 + [y_bend])*10

qk_drift = (Drift(l=0.4724), QK, Drift(l=2.000002 - 0.4724 - 1.0552))
# Lattice 
cell = (bz_1980_tld, qk_drift, bz_1983_tld,....)
```
