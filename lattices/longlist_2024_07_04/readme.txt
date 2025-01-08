Renamed:
line 2346 SECTION CL to TL which affect this marker ENBLOCK.1891.CL
line 2470 SUBSECTION TL to TL5 which affect this marker ENSEC.2058.TL
SUBSECTION TL to TL1: TL	TL1	XTL_035	STSEC.1854.TL	STSEC.TL.TL	MARK

Removed
U90 CUS elements. it is coils for magnetic earth correction
and all QP quads which are used only for alignment

# 3493 SA3	UE90	XTD4_003	CUSX.2942.SA3	CUSX.CELL24.SA3	MAGNET
# 3494 SA3	UE90	XTD4_003	CUSY.2942.SA3	CUSY.CELL24.SA3	MAGNET
# 3495 SA3	UE90	XTD4_003	QP.2941.SA3	QP.CELL24.SA3	PMAGNET	QUAD	QP
#
# 3508 SA3	UE90	XTD4_004	CUSX.2946.SA3	CUSX.CELL25.SA3	MAGNET	HKIC	CUSX
# 3509 SA3	UE90	XTD4_004	CUSY.2946.SA3	CUSY.CELL25.SA3	MAGNET	HKIC	CUSY
# 3510 SA3	UE90	XTD4_004	QP.2945.SA3	QP.CELL25.SA3	PMAGNET	QUAD	QP
#
# 3525 SA3	UE90	XTD4_004	CUSX.2949.SA3	CUSX.CELL26.SA3	MAGNET	HKIC	CUSX
# 3526 SA3	UE90	XTD4_004	CUSY.2949.SA3	CUSY.CELL26.SA3	MAGNET	HKIC	CUSY
# 3527 SA3	UE90	XTD4_004	QP.2948.SA3	QP.CELL26.SA3	PMAGNET	QUAD	QP
#
# 3540 SA3	UE90	XTD4_004	CUSX.2953.SA3	CUSX.CELL27.SA3	MAGNET	HKIC	CUSX
# 3541 SA3	UE90	XTD4_004	CUSY.2953.SA3	CUSY.CELL27.SA3	MAGNET	HKIC	CUSY
# 3542 SA3	UE90	XTD4_004	QP.2952.SA3	QP.CELL27.SA3	PMAGNET	QUAD	QP

# SA3	UE90	XTD4_004	QP.2954.SA3	QP.CELL27.SA3	PMAGNET	QUAD	QP
# SA3	UE90	XTD4_004	QP.2947.SA3	QP.CELL25.SA3	PMAGNET	QUAD	QP
# SA3	UE90	XTD4_003	QP.2943.SA3	QP.CELL24.SA3	PMAGNET	QUAD	QP
# SA3	UE90	XTD4_004	QP.2951.SA3	QP.CELL26.SA3	PMAGNET	QUAD	QP

*****************************
In t34_sa2.py
we introduced following changes:

# Quad QF.2012.TL replace with combine function SBEND since beam has displacement 0.00581165 m
dy = 0.00581165
qf_2012_tl = SBend(l=0.5321, angle=-0.5321*0.1791908476*dy, k1=-0.1791908476, e1=0.0005095, e2=0.0010813, tilt=1.570796, eid='QF.2012.TL')

# bending magnets: KL kickers have to be ON to transport beam to SA2 branch
alpha=-0.0001019145217
kl_1998_tl = SBend(l=0.93, angle=alpha, e1=0,        e2=alpha, tilt=1.570796, eid="KL.1998.TL")
kl_1999_tl = SBend(l=0.93, angle=alpha, e1=-alpha,   e2=2*alpha,  tilt=1.570796, eid="KL.1999.TL")
kl_2000_tl = SBend(l=0.93, angle=alpha, e1=-2*alpha, e2=3*alpha,  tilt=1.570796, eid="KL.2000.TL")
kl_2001_tl = SBend(l=0.93, angle=alpha, e1=-3*alpha, e2=4*alpha,  tilt=1.570796, eid="KL.2001.TL")
kl_2002_tl = SBend(l=0.93, angle=alpha, e1=-4*alpha, e2=5*alpha,  tilt=1.570796, eid="KL.2002.TL")
kl_2003_tl = SBend(l=0.93, angle=0, tilt=1.570796, eid="KL.2003.TL")
**************************************************
In tl2_tld.py the following changes were introduced:

# Extraction to TLD: KS kicker setup   
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

QF.1952.TL: Combine function magnet in TLD line (quadrupole and horizontal dipole components)

