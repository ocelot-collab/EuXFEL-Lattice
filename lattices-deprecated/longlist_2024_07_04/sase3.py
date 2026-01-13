from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 22.6886
tws0.beta_y = 9.6311
tws0.alpha_x = 1.5464
tws0.alpha_y = -0.6632
tws0.E = 14
tws0.s = 2801.0155910000135

# Drifts
id_88369288_ = Drift(l=5.7595, eid='ID_88369288_')
d_4 = Drift(l=0.18665, eid='D_4')
id_49430361_ = Drift(l=0.35787, eid='ID_49430361_')
d_7 = Drift(l=0.07278, eid='D_7')
d_8 = Drift(l=0.0717, eid='D_8')
d_9 = Drift(l=0.2973, eid='D_9')
id_80444588_ = Drift(l=0.33287, eid='ID_80444588_')
id_16496657_ = Drift(l=0.025, eid='ID_16496657_')
id_69556685_ = Drift(l=0.54565, eid='ID_69556685_')
d_73 = Drift(l=1.0145, eid='D_73')
d_74 = Drift(l=0.341, eid='D_74')
d_76 = Drift(l=0.484, eid='D_76')
d_140 = Drift(l=0.40128, eid='D_140')
d_141 = Drift(l=0.0325, eid='D_141')
d_142 = Drift(l=0.2307, eid='D_142')
id_4594986_ = Drift(l=0.65822, eid='ID_4594986_')

# Quadrupoles
qa_2806_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2806.SA3')
qa_2812_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2812.SA3')
qa_2818_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2818.SA3')
qa_2824_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2824.SA3')
qa_2831_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2831.SA3')
qa_2837_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2837.SA3')
qa_2843_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2843.SA3')
qa_2849_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2849.SA3')
qa_2855_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2855.SA3')
qa_2861_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2861.SA3')
qa_2867_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2867.SA3')
qa_2873_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2873.SA3')
qa_2879_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2879.SA3')
qa_2885_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2885.SA3')
qa_2892_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2892.SA3')
qa_2898_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2898.SA3')
qa_2904_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2904.SA3')
qa_2910_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2910.SA3')
qa_2916_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2916.SA3')
qa_2922_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2922.SA3')
qa_2928_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2928.SA3')
qa_2934_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2934.SA3')
qa_2940_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2940.SA3')
qp_2943_sa3 = Quadrupole(l=0.1, eid='QP.2943.SA3')
qp_2947_sa3 = Quadrupole(l=0.1, eid='QP.2947.SA3')
qa_2948_sa3 = Quadrupole(l=0.1137, k1=1.1974301229991204, eid='QA.2948.SA3')
qp_2951_sa3 = Quadrupole(l=0.1, eid='QP.2951.SA3')
qp_2954_sa3 = Quadrupole(l=0.1, eid='QP.2954.SA3')
qa_2955_sa3 = Quadrupole(l=0.1137, k1=-1.1974301229991204, eid='QA.2955.SA3')

# SBends
bsl_2874_sa3 = SBend(l=0.6, eid='BSL.2874.SA3')
bsl_2876_sa3 = SBend(l=0.6, eid='BSL.2876.SA3')
bsl_2877_sa3 = SBend(l=0.6, eid='BSL.2877.SA3')
bsl_2878_sa3 = SBend(l=0.6, eid='BSL.2878.SA3')

# Hcors
cax_2807_sa3 = Hcor(eid='CAX.2807.SA3')
cbx_2812_sa3 = Hcor(eid='CBX.2812.SA3')
cax_2813_sa3 = Hcor(eid='CAX.2813.SA3')
cbx_2818_sa3 = Hcor(eid='CBX.2818.SA3')
cax_2819_sa3 = Hcor(eid='CAX.2819.SA3')
cbx_2824_sa3 = Hcor(eid='CBX.2824.SA3')
cax_2825_sa3 = Hcor(eid='CAX.2825.SA3')
cbx_2830_sa3 = Hcor(eid='CBX.2830.SA3')
cax_2831_sa3 = Hcor(eid='CAX.2831.SA3')
cbx_2836_sa3 = Hcor(eid='CBX.2836.SA3')
cax_2838_sa3 = Hcor(eid='CAX.2838.SA3')
cbx_2842_sa3 = Hcor(eid='CBX.2842.SA3')
cax_2844_sa3 = Hcor(eid='CAX.2844.SA3')
cbx_2848_sa3 = Hcor(eid='CBX.2848.SA3')
cax_2850_sa3 = Hcor(eid='CAX.2850.SA3')
cbx_2854_sa3 = Hcor(eid='CBX.2854.SA3')
cax_2856_sa3 = Hcor(eid='CAX.2856.SA3')
cbx_2860_sa3 = Hcor(eid='CBX.2860.SA3')
cax_2862_sa3 = Hcor(eid='CAX.2862.SA3')
cbx_2867_sa3 = Hcor(eid='CBX.2867.SA3')
cax_2868_sa3 = Hcor(eid='CAX.2868.SA3')
cbx_2873_sa3 = Hcor(eid='CBX.2873.SA3')
cbsl_2874_sa3 = Hcor(eid='CBSL.2874.SA3')
cbsl_2876_sa3 = Hcor(eid='CBSL.2876.SA3')
cbsl_2877_sa3 = Hcor(eid='CBSL.2877.SA3')
cbsl_2878_sa3 = Hcor(eid='CBSL.2878.SA3')
cax_2880_sa3 = Hcor(eid='CAX.2880.SA3')
cbx_2885_sa3 = Hcor(eid='CBX.2885.SA3')
cax_2886_sa3 = Hcor(eid='CAX.2886.SA3')
cbx_2891_sa3 = Hcor(eid='CBX.2891.SA3')
cax_2892_sa3 = Hcor(eid='CAX.2892.SA3')
cbx_2897_sa3 = Hcor(eid='CBX.2897.SA3')
cax_2899_sa3 = Hcor(eid='CAX.2899.SA3')
cbx_2903_sa3 = Hcor(eid='CBX.2903.SA3')
cax_2905_sa3 = Hcor(eid='CAX.2905.SA3')
cbx_2909_sa3 = Hcor(eid='CBX.2909.SA3')
cax_2911_sa3 = Hcor(eid='CAX.2911.SA3')
cbx_2915_sa3 = Hcor(eid='CBX.2915.SA3')
cax_2917_sa3 = Hcor(eid='CAX.2917.SA3')
cbx_2921_sa3 = Hcor(eid='CBX.2921.SA3')
cax_2923_sa3 = Hcor(eid='CAX.2923.SA3')
cbx_2928_sa3 = Hcor(eid='CBX.2928.SA3')
cax_2929_sa3 = Hcor(eid='CAX.2929.SA3')
cbx_2934_sa3 = Hcor(eid='CBX.2934.SA3')
cax_2935_sa3 = Hcor(eid='CAX.2935.SA3')
cbx_2940_sa3 = Hcor(eid='CBX.2940.SA3')
cax_2941_sa3 = Hcor(eid='CAX.2941.SA3')
cbx_2943_sa3 = Hcor(eid='CBX.2943.SA3')
cax_2945_sa3 = Hcor(eid='CAX.2945.SA3')
cbx_2947_sa3 = Hcor(eid='CBX.2947.SA3')
cax_2949_sa3 = Hcor(eid='CAX.2949.SA3')
cbx_2951_sa3 = Hcor(eid='CBX.2951.SA3')
cax_2952_sa3 = Hcor(eid='CAX.2952.SA3')
cbx_2955_sa3 = Hcor(eid='CBX.2955.SA3')

# Vcors
cay_2807_sa3 = Vcor(eid='CAY.2807.SA3')
cby_2812_sa3 = Vcor(eid='CBY.2812.SA3')
cay_2813_sa3 = Vcor(eid='CAY.2813.SA3')
cby_2818_sa3 = Vcor(eid='CBY.2818.SA3')
cay_2819_sa3 = Vcor(eid='CAY.2819.SA3')
cby_2824_sa3 = Vcor(eid='CBY.2824.SA3')
cay_2825_sa3 = Vcor(eid='CAY.2825.SA3')
cby_2830_sa3 = Vcor(eid='CBY.2830.SA3')
cay_2831_sa3 = Vcor(eid='CAY.2831.SA3')
cby_2836_sa3 = Vcor(eid='CBY.2836.SA3')
cay_2838_sa3 = Vcor(eid='CAY.2838.SA3')
cby_2842_sa3 = Vcor(eid='CBY.2842.SA3')
cay_2844_sa3 = Vcor(eid='CAY.2844.SA3')
cby_2848_sa3 = Vcor(eid='CBY.2848.SA3')
cay_2850_sa3 = Vcor(eid='CAY.2850.SA3')
cby_2854_sa3 = Vcor(eid='CBY.2854.SA3')
cay_2856_sa3 = Vcor(eid='CAY.2856.SA3')
cby_2860_sa3 = Vcor(eid='CBY.2860.SA3')
cay_2862_sa3 = Vcor(eid='CAY.2862.SA3')
cby_2867_sa3 = Vcor(eid='CBY.2867.SA3')
cay_2868_sa3 = Vcor(eid='CAY.2868.SA3')
cby_2873_sa3 = Vcor(eid='CBY.2873.SA3')
cay_2880_sa3 = Vcor(eid='CAY.2880.SA3')
cby_2885_sa3 = Vcor(eid='CBY.2885.SA3')
cay_2886_sa3 = Vcor(eid='CAY.2886.SA3')
cby_2891_sa3 = Vcor(eid='CBY.2891.SA3')
cay_2892_sa3 = Vcor(eid='CAY.2892.SA3')
cby_2897_sa3 = Vcor(eid='CBY.2897.SA3')
cay_2899_sa3 = Vcor(eid='CAY.2899.SA3')
cby_2903_sa3 = Vcor(eid='CBY.2903.SA3')
cay_2905_sa3 = Vcor(eid='CAY.2905.SA3')
cby_2909_sa3 = Vcor(eid='CBY.2909.SA3')
cay_2911_sa3 = Vcor(eid='CAY.2911.SA3')
cby_2915_sa3 = Vcor(eid='CBY.2915.SA3')
cay_2917_sa3 = Vcor(eid='CAY.2917.SA3')
cby_2921_sa3 = Vcor(eid='CBY.2921.SA3')
cay_2923_sa3 = Vcor(eid='CAY.2923.SA3')
cby_2928_sa3 = Vcor(eid='CBY.2928.SA3')
cay_2929_sa3 = Vcor(eid='CAY.2929.SA3')
cby_2934_sa3 = Vcor(eid='CBY.2934.SA3')
cay_2935_sa3 = Vcor(eid='CAY.2935.SA3')
cby_2940_sa3 = Vcor(eid='CBY.2940.SA3')
cay_2941_sa3 = Vcor(eid='CAY.2941.SA3')
cby_2943_sa3 = Vcor(eid='CBY.2943.SA3')
cay_2945_sa3 = Vcor(eid='CAY.2945.SA3')
cby_2947_sa3 = Vcor(eid='CBY.2947.SA3')
cay_2949_sa3 = Vcor(eid='CAY.2949.SA3')
cby_2951_sa3 = Vcor(eid='CBY.2951.SA3')
cay_2952_sa3 = Vcor(eid='CAY.2952.SA3')
cby_2955_sa3 = Vcor(eid='CBY.2955.SA3')

# Undulators
u68_2809_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2809.SA3')
u68_2815_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2815.SA3')
u68_2821_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2821.SA3')
u68_2827_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2827.SA3')
u68_2834_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2834.SA3')
u68_2840_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2840.SA3')
u68_2846_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2846.SA3')
u68_2852_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2852.SA3')
u68_2858_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2858.SA3')
u68_2864_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2864.SA3')
u68_2870_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2870.SA3')
u68_2882_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2882.SA3')
u68_2888_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2888.SA3')
u68_2894_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2894.SA3')
u68_2901_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2901.SA3')
u68_2907_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2907.SA3')
u68_2913_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2913.SA3')
u68_2919_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2919.SA3')
u68_2925_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2925.SA3')
u68_2931_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2931.SA3')
u68_2937_sa3 = Undulator(lperiod=0.068, nperiods=73.52941176470588, eid='U68.2937.SA3')
ue90_2942_sa3 = Undulator(lperiod=0.09, nperiods=22.0, eid='UE90.2942.SA3')
ue90_2946_sa3 = Undulator(lperiod=0.09, nperiods=22.0, eid='UE90.2946.SA3')
ue90_2950_sa3 = Undulator(lperiod=0.09, nperiods=22.0, eid='UE90.2950.SA3')
ue90_2953_sa3 = Undulator(lperiod=0.09, nperiods=22.0, eid='UE90.2953.SA3')

# Monitors
bpme_2806_sa3 = Monitor(eid='BPME.2806.SA3')
bpme_2812_sa3 = Monitor(eid='BPME.2812.SA3')
bpme_2818_sa3 = Monitor(eid='BPME.2818.SA3')
bpme_2824_sa3 = Monitor(eid='BPME.2824.SA3')
bpme_2830_sa3 = Monitor(eid='BPME.2830.SA3')
bpme_2836_sa3 = Monitor(eid='BPME.2836.SA3')
bpme_2842_sa3 = Monitor(eid='BPME.2842.SA3')
bpme_2849_sa3 = Monitor(eid='BPME.2849.SA3')
bpme_2855_sa3 = Monitor(eid='BPME.2855.SA3')
bpme_2861_sa3 = Monitor(eid='BPME.2861.SA3')
bpme_2867_sa3 = Monitor(eid='BPME.2867.SA3')
bpme_2873_sa3 = Monitor(eid='BPME.2873.SA3')
bpme_2879_sa3 = Monitor(eid='BPME.2879.SA3')
bpme_2885_sa3 = Monitor(eid='BPME.2885.SA3')
bpme_2891_sa3 = Monitor(eid='BPME.2891.SA3')
bpme_2897_sa3 = Monitor(eid='BPME.2897.SA3')
bpme_2903_sa3 = Monitor(eid='BPME.2903.SA3')
bpme_2910_sa3 = Monitor(eid='BPME.2910.SA3')
bpme_2916_sa3 = Monitor(eid='BPME.2916.SA3')
bpme_2922_sa3 = Monitor(eid='BPME.2922.SA3')
bpme_2928_sa3 = Monitor(eid='BPME.2928.SA3')
bpme_2934_sa3 = Monitor(eid='BPME.2934.SA3')
bpme_2940_sa3 = Monitor(eid='BPME.2940.SA3')
bpme_2944_sa3 = Monitor(eid='BPME.2944.SA3')
bpme_2947_sa3 = Monitor(eid='BPME.2947.SA3')
bpme_2951_sa3 = Monitor(eid='BPME.2951.SA3')
bpme_2955_sa3 = Monitor(eid='BPME.2955.SA3')

# Markers
ensec_2800_t4 = Marker(eid='ENSEC.2800.T4')
match_2813_sa3 = Marker(eid='MATCH.2813.SA3')

# Lattice 
cell = (ensec_2800_t4, id_88369288_, bpme_2806_sa3, d_4, qa_2806_sa3, id_49430361_, cax_2807_sa3, cay_2807_sa3,
d_7, u68_2809_sa3, d_8, cbx_2812_sa3, cby_2812_sa3, d_9, bpme_2812_sa3, d_4, qa_2812_sa3, id_80444588_, 
match_2813_sa3, id_16496657_, cax_2813_sa3, cay_2813_sa3, d_7, u68_2815_sa3, d_8, cbx_2818_sa3, cby_2818_sa3, d_9, 
bpme_2818_sa3, d_4, qa_2818_sa3, id_49430361_, cax_2819_sa3, cay_2819_sa3, d_7, u68_2821_sa3, d_8, cbx_2824_sa3, 
cby_2824_sa3, d_9, bpme_2824_sa3, d_4, qa_2824_sa3, id_49430361_, cax_2825_sa3, cay_2825_sa3, d_7, u68_2827_sa3, 
d_8, cbx_2830_sa3, cby_2830_sa3, d_9, bpme_2830_sa3, d_4, qa_2831_sa3, id_49430361_, cax_2831_sa3, cay_2831_sa3, 
d_7, u68_2834_sa3, d_8, cbx_2836_sa3, cby_2836_sa3, d_9, bpme_2836_sa3, d_4, qa_2837_sa3, id_49430361_, 
cax_2838_sa3, cay_2838_sa3, d_7, u68_2840_sa3, d_8, cbx_2842_sa3, cby_2842_sa3, d_9, bpme_2842_sa3, d_4, 
qa_2843_sa3, id_49430361_, cax_2844_sa3, cay_2844_sa3, d_7, u68_2846_sa3, d_8, cbx_2848_sa3, cby_2848_sa3, d_9, 
bpme_2849_sa3, d_4, qa_2849_sa3, id_49430361_, cax_2850_sa3, cay_2850_sa3, d_7, u68_2852_sa3, d_8, cbx_2854_sa3, 
cby_2854_sa3, d_9, bpme_2855_sa3, d_4, qa_2855_sa3, id_49430361_, cax_2856_sa3, cay_2856_sa3, d_7, u68_2858_sa3, 
d_8, cbx_2860_sa3, cby_2860_sa3, d_9, bpme_2861_sa3, d_4, qa_2861_sa3, id_49430361_, cax_2862_sa3, cay_2862_sa3, 
d_7, u68_2864_sa3, d_8, cbx_2867_sa3, cby_2867_sa3, d_9, bpme_2867_sa3, d_4, qa_2867_sa3, id_49430361_, 
cax_2868_sa3, cay_2868_sa3, d_7, u68_2870_sa3, d_8, cbx_2873_sa3, cby_2873_sa3, d_9, bpme_2873_sa3, d_4, 
qa_2873_sa3, id_69556685_, bsl_2874_sa3, cbsl_2874_sa3, d_73, bsl_2876_sa3, cbsl_2876_sa3, d_74, bsl_2877_sa3, cbsl_2877_sa3, 
d_73, bsl_2878_sa3, cbsl_2878_sa3, d_76, bpme_2879_sa3, d_4, qa_2879_sa3, id_49430361_, cax_2880_sa3, cay_2880_sa3, 
d_7, u68_2882_sa3, d_8, cbx_2885_sa3, cby_2885_sa3, d_9, bpme_2885_sa3, d_4, qa_2885_sa3, id_49430361_, 
cax_2886_sa3, cay_2886_sa3, d_7, u68_2888_sa3, d_8, cbx_2891_sa3, cby_2891_sa3, d_9, bpme_2891_sa3, d_4, 
qa_2892_sa3, id_49430361_, cax_2892_sa3, cay_2892_sa3, d_7, u68_2894_sa3, d_8, cbx_2897_sa3, cby_2897_sa3, d_9, 
bpme_2897_sa3, d_4, qa_2898_sa3, id_49430361_, cax_2899_sa3, cay_2899_sa3, d_7, u68_2901_sa3, d_8, cbx_2903_sa3, 
cby_2903_sa3, d_9, bpme_2903_sa3, d_4, qa_2904_sa3, id_49430361_, cax_2905_sa3, cay_2905_sa3, d_7, u68_2907_sa3, 
d_8, cbx_2909_sa3, cby_2909_sa3, d_9, bpme_2910_sa3, d_4, qa_2910_sa3, id_49430361_, cax_2911_sa3, cay_2911_sa3, 
d_7, u68_2913_sa3, d_8, cbx_2915_sa3, cby_2915_sa3, d_9, bpme_2916_sa3, d_4, qa_2916_sa3, id_49430361_, 
cax_2917_sa3, cay_2917_sa3, d_7, u68_2919_sa3, d_8, cbx_2921_sa3, cby_2921_sa3, d_9, bpme_2922_sa3, d_4, 
qa_2922_sa3, id_49430361_, cax_2923_sa3, cay_2923_sa3, d_7, u68_2925_sa3, d_8, cbx_2928_sa3, cby_2928_sa3, d_9, 
bpme_2928_sa3, d_4, qa_2928_sa3, id_49430361_, cax_2929_sa3, cay_2929_sa3, d_7, u68_2931_sa3, d_8, cbx_2934_sa3, 
cby_2934_sa3, d_9, bpme_2934_sa3, d_4, qa_2934_sa3, id_49430361_, cax_2935_sa3, cay_2935_sa3, d_7, u68_2937_sa3, 
d_8, cbx_2940_sa3, cby_2940_sa3, d_9, bpme_2940_sa3, d_4, qa_2940_sa3, id_49430361_, cax_2941_sa3, cay_2941_sa3, 
d_140, ue90_2942_sa3, d_141, qp_2943_sa3, d_142, cbx_2943_sa3, cby_2943_sa3, d_9, bpme_2944_sa3, id_4594986_, 
cax_2945_sa3, cay_2945_sa3, d_140, ue90_2946_sa3, d_141, qp_2947_sa3, d_142, cbx_2947_sa3, cby_2947_sa3, d_9, 
bpme_2947_sa3, d_4, qa_2948_sa3, id_49430361_, cax_2949_sa3, cay_2949_sa3, d_140, ue90_2950_sa3, d_141, qp_2951_sa3, 
d_142, cbx_2951_sa3, cby_2951_sa3, d_9, bpme_2951_sa3, id_4594986_, cax_2952_sa3, cay_2952_sa3, d_140, ue90_2953_sa3, 
d_141, qp_2954_sa3, d_142, cbx_2955_sa3, cby_2955_sa3, d_9, bpme_2955_sa3, d_4, qa_2955_sa3)

# power supplies 

#  
qa_2806_sa3.ps_id = 'QA.1.SA3'
qa_2812_sa3.ps_id = 'QA.2.SA3'
qa_2818_sa3.ps_id = 'QA.1.SA3'
qa_2824_sa3.ps_id = 'QA.2.SA3'
qa_2831_sa3.ps_id = 'QA.1.SA3'
qa_2837_sa3.ps_id = 'QA.2.SA3'
qa_2843_sa3.ps_id = 'QA.1.SA3'
qa_2849_sa3.ps_id = 'QA.2.SA3'
qa_2855_sa3.ps_id = 'QA.1.SA3'
qa_2861_sa3.ps_id = 'QA.2.SA3'
qa_2867_sa3.ps_id = 'QA.1.SA3'
qa_2873_sa3.ps_id = 'QA.2.SA3'
qa_2879_sa3.ps_id = 'QA.1.SA3'
qa_2885_sa3.ps_id = 'QA.2.SA3'
qa_2892_sa3.ps_id = 'QA.1.SA3'
qa_2898_sa3.ps_id = 'QA.2.SA3'
qa_2904_sa3.ps_id = 'QA.1.SA3'
qa_2910_sa3.ps_id = 'QA.2.SA3'
qa_2916_sa3.ps_id = 'QA.1.SA3'
qa_2922_sa3.ps_id = 'QA.2.SA3'
qa_2928_sa3.ps_id = 'QA.1.SA3'
qa_2934_sa3.ps_id = 'QA.2.SA3'
qa_2940_sa3.ps_id = 'QA.1.SA3'
qp_2943_sa3.ps_id = 'QP.CELL24.SA3'
qp_2947_sa3.ps_id = 'QP.CELL25.SA3'
qa_2948_sa3.ps_id = 'QA.2.SA3'
qp_2951_sa3.ps_id = 'QP.CELL26.SA3'
qp_2954_sa3.ps_id = 'QP.CELL27.SA3'
qa_2955_sa3.ps_id = 'QA.1.SA3'

#  

#  

#  

#  
bsl_2874_sa3.ps_id = 'BSL.1.SA3'
bsl_2876_sa3.ps_id = 'BSL.1.SA3'
bsl_2877_sa3.ps_id = 'BSL.1.SA3'
bsl_2878_sa3.ps_id = 'BSL.1.SA3'
