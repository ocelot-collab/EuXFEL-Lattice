from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0.beta_x = 12.958162568054922
tws0.beta_y = 42.969888945121845
tws0.alpha_x = 1.3088879823896227
tws0.alpha_y = 0.9334000934857891
tws0.E = 14
tws0.s = 2152.0090710000186

# Drifts
id_6001301_ = Drift(l=0.29272, eid='ID_6001301_')
id_61060562_ = Drift(l=0.025, eid='ID_61060562_')
d_4 = Drift(l=0.07278, eid='D_4')
d_5 = Drift(l=0.0717, eid='D_5')
d_6 = Drift(l=0.2973, eid='D_6')
d_7 = Drift(l=0.18665, eid='D_7')
id_28120785_ = Drift(l=0.35787, eid='ID_28120785_')
id_82512098_ = Drift(l=0.57915, eid='ID_82512098_')
id_99805086_ = Drift(l=1.2375, eid='ID_99805086_')
d_53 = Drift(l=0.29, eid='D_53')
d_54 = Drift(l=0.735, eid='D_54')
d_56 = Drift(l=0.5205, eid='D_56')
id_59449715_ = Drift(l=0.04015, eid='ID_59449715_')

# Quadrupoles
qa_2203_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2203.SA2')
qa_2209_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2209.SA2')
qa_2215_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2215.SA2')
qa_2221_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2221.SA2')
qa_2227_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2227.SA2')
qa_2234_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2234.SA2')
qa_2240_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2240.SA2')
qa_2246_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2246.SA2')
qa_2252_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2252.SA2')
qa_2258_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2258.SA2')
qa_2264_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2264.SA2')
qa_2270_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2270.SA2')
qa_2276_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2276.SA2')
qa_2282_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2282.SA2')
qa_2288_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2288.SA2')
qa_2295_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2295.SA2')
qa_2301_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2301.SA2')
qa_2307_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2307.SA2')
qa_2313_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2313.SA2')
qa_2319_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2319.SA2')
qa_2325_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2325.SA2')
qa_2331_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2331.SA2')
qa_2337_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2337.SA2')
qa_2343_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2343.SA2')
qa_2349_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2349.SA2')
qa_2355_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2355.SA2')
qa_2362_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2362.SA2')
qa_2368_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2368.SA2')
qa_2374_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2374.SA2')
qa_2380_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2380.SA2')
qa_2386_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2386.SA2')
qa_2392_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2392.SA2')
qa_2398_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2398.SA2')
qa_2404_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2404.SA2')
qa_2410_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2410.SA2')
qa_2416_sa2 = Quadrupole(l=0.1137, k1=0.5620550638962181, eid='QA.2416.SA2')
qa_2422_sa2 = Quadrupole(l=0.1137, k1=-0.5620550638962181, eid='QA.2422.SA2')

# SBends
bs_2247_sa2 = SBend(l=0.3, eid='BS.2247.SA2')
bs_2248_sa2 = SBend(l=0.3, eid='BS.2248.SA2')
bs_2249_sa2 = SBend(l=0.3, eid='BS.2249.SA2')
bs_2251_sa2 = SBend(l=0.3, eid='BS.2251.SA2')
bs_2301_sa2 = SBend(l=0.3, eid='BS.2301.SA2')
bs_2303_sa2 = SBend(l=0.3, eid='BS.2303.SA2')
bs_2304_sa2 = SBend(l=0.3, eid='BS.2304.SA2')
bs_2306_sa2 = SBend(l=0.3, eid='BS.2306.SA2')

# Hcors
cax_2198_sa2 = Hcor(eid='CAX.2198.SA2')
cbx_2203_sa2 = Hcor(eid='CBX.2203.SA2')
cax_2204_sa2 = Hcor(eid='CAX.2204.SA2')
cbx_2209_sa2 = Hcor(eid='CBX.2209.SA2')
cax_2210_sa2 = Hcor(eid='CAX.2210.SA2')
cbx_2215_sa2 = Hcor(eid='CBX.2215.SA2')
cax_2216_sa2 = Hcor(eid='CAX.2216.SA2')
cbx_2221_sa2 = Hcor(eid='CBX.2221.SA2')
cax_2222_sa2 = Hcor(eid='CAX.2222.SA2')
cbx_2227_sa2 = Hcor(eid='CBX.2227.SA2')
cax_2228_sa2 = Hcor(eid='CAX.2228.SA2')
cbx_2233_sa2 = Hcor(eid='CBX.2233.SA2')
cax_2234_sa2 = Hcor(eid='CAX.2234.SA2')
cbx_2239_sa2 = Hcor(eid='CBX.2239.SA2')
cax_2241_sa2 = Hcor(eid='CAX.2241.SA2')
cbx_2245_sa2 = Hcor(eid='CBX.2245.SA2')
cbs_2248_sa2 = Hcor(eid='CBS.2248.SA2')
cbs_2249_sa2 = Hcor(eid='CBS.2249.SA2')
cbs_2251_sa2 = Hcor(eid='CBS.2251.SA2')
cax_2253_sa2 = Hcor(eid='CAX.2253.SA2')
cbx_2257_sa2 = Hcor(eid='CBX.2257.SA2')
cax_2259_sa2 = Hcor(eid='CAX.2259.SA2')
cbx_2263_sa2 = Hcor(eid='CBX.2263.SA2')
cax_2265_sa2 = Hcor(eid='CAX.2265.SA2')
cbx_2270_sa2 = Hcor(eid='CBX.2270.SA2')
cax_2271_sa2 = Hcor(eid='CAX.2271.SA2')
cbx_2276_sa2 = Hcor(eid='CBX.2276.SA2')
cax_2277_sa2 = Hcor(eid='CAX.2277.SA2')
cbx_2282_sa2 = Hcor(eid='CBX.2282.SA2')
cax_2283_sa2 = Hcor(eid='CAX.2283.SA2')
cbx_2288_sa2 = Hcor(eid='CBX.2288.SA2')
cax_2289_sa2 = Hcor(eid='CAX.2289.SA2')
cbx_2294_sa2 = Hcor(eid='CBX.2294.SA2')
cax_2295_sa2 = Hcor(eid='CAX.2295.SA2')
cbx_2300_sa2 = Hcor(eid='CBX.2300.SA2')
cbs_2303_sa2 = Hcor(eid='CBS.2303.SA2')
cbs_2304_sa2 = Hcor(eid='CBS.2304.SA2')
cbs_2306_sa2 = Hcor(eid='CBS.2306.SA2')
cax_2308_sa2 = Hcor(eid='CAX.2308.SA2')
cbx_2312_sa2 = Hcor(eid='CBX.2312.SA2')
cax_2314_sa2 = Hcor(eid='CAX.2314.SA2')
cbx_2318_sa2 = Hcor(eid='CBX.2318.SA2')
cax_2320_sa2 = Hcor(eid='CAX.2320.SA2')
cbx_2324_sa2 = Hcor(eid='CBX.2324.SA2')
cax_2326_sa2 = Hcor(eid='CAX.2326.SA2')
cbx_2331_sa2 = Hcor(eid='CBX.2331.SA2')
cax_2332_sa2 = Hcor(eid='CAX.2332.SA2')
cbx_2337_sa2 = Hcor(eid='CBX.2337.SA2')
cax_2338_sa2 = Hcor(eid='CAX.2338.SA2')
cbx_2343_sa2 = Hcor(eid='CBX.2343.SA2')
cax_2344_sa2 = Hcor(eid='CAX.2344.SA2')
cbx_2349_sa2 = Hcor(eid='CBX.2349.SA2')
cax_2350_sa2 = Hcor(eid='CAX.2350.SA2')
cbx_2355_sa2 = Hcor(eid='CBX.2355.SA2')
cax_2356_sa2 = Hcor(eid='CAX.2356.SA2')
cbx_2361_sa2 = Hcor(eid='CBX.2361.SA2')
cax_2362_sa2 = Hcor(eid='CAX.2362.SA2')
cbx_2367_sa2 = Hcor(eid='CBX.2367.SA2')
cax_2369_sa2 = Hcor(eid='CAX.2369.SA2')
cbx_2373_sa2 = Hcor(eid='CBX.2373.SA2')
cax_2375_sa2 = Hcor(eid='CAX.2375.SA2')
cbx_2379_sa2 = Hcor(eid='CBX.2379.SA2')
cax_2381_sa2 = Hcor(eid='CAX.2381.SA2')
cbx_2385_sa2 = Hcor(eid='CBX.2385.SA2')
cax_2387_sa2 = Hcor(eid='CAX.2387.SA2')
cbx_2391_sa2 = Hcor(eid='CBX.2391.SA2')
cax_2393_sa2 = Hcor(eid='CAX.2393.SA2')
cbx_2398_sa2 = Hcor(eid='CBX.2398.SA2')
cax_2399_sa2 = Hcor(eid='CAX.2399.SA2')
cbx_2404_sa2 = Hcor(eid='CBX.2404.SA2')
cax_2405_sa2 = Hcor(eid='CAX.2405.SA2')
cbx_2410_sa2 = Hcor(eid='CBX.2410.SA2')
cax_2411_sa2 = Hcor(eid='CAX.2411.SA2')
cbx_2416_sa2 = Hcor(eid='CBX.2416.SA2')
cax_2417_sa2 = Hcor(eid='CAX.2417.SA2')
cbx_2422_sa2 = Hcor(eid='CBX.2422.SA2')

# Vcors
cay_2198_sa2 = Vcor(eid='CAY.2198.SA2')
cby_2203_sa2 = Vcor(eid='CBY.2203.SA2')
cay_2204_sa2 = Vcor(eid='CAY.2204.SA2')
cby_2209_sa2 = Vcor(eid='CBY.2209.SA2')
cay_2210_sa2 = Vcor(eid='CAY.2210.SA2')
cby_2215_sa2 = Vcor(eid='CBY.2215.SA2')
cay_2216_sa2 = Vcor(eid='CAY.2216.SA2')
cby_2221_sa2 = Vcor(eid='CBY.2221.SA2')
cay_2222_sa2 = Vcor(eid='CAY.2222.SA2')
cby_2227_sa2 = Vcor(eid='CBY.2227.SA2')
cay_2228_sa2 = Vcor(eid='CAY.2228.SA2')
cby_2233_sa2 = Vcor(eid='CBY.2233.SA2')
cay_2234_sa2 = Vcor(eid='CAY.2234.SA2')
cby_2239_sa2 = Vcor(eid='CBY.2239.SA2')
cay_2241_sa2 = Vcor(eid='CAY.2241.SA2')
cby_2245_sa2 = Vcor(eid='CBY.2245.SA2')
cay_2253_sa2 = Vcor(eid='CAY.2253.SA2')
cby_2257_sa2 = Vcor(eid='CBY.2257.SA2')
cay_2259_sa2 = Vcor(eid='CAY.2259.SA2')
cby_2263_sa2 = Vcor(eid='CBY.2263.SA2')
cay_2265_sa2 = Vcor(eid='CAY.2265.SA2')
cby_2270_sa2 = Vcor(eid='CBY.2270.SA2')
cay_2271_sa2 = Vcor(eid='CAY.2271.SA2')
cby_2276_sa2 = Vcor(eid='CBY.2276.SA2')
cay_2277_sa2 = Vcor(eid='CAY.2277.SA2')
cby_2282_sa2 = Vcor(eid='CBY.2282.SA2')
cay_2283_sa2 = Vcor(eid='CAY.2283.SA2')
cby_2288_sa2 = Vcor(eid='CBY.2288.SA2')
cay_2289_sa2 = Vcor(eid='CAY.2289.SA2')
cby_2294_sa2 = Vcor(eid='CBY.2294.SA2')
cay_2295_sa2 = Vcor(eid='CAY.2295.SA2')
cby_2300_sa2 = Vcor(eid='CBY.2300.SA2')
cay_2308_sa2 = Vcor(eid='CAY.2308.SA2')
cby_2312_sa2 = Vcor(eid='CBY.2312.SA2')
cay_2314_sa2 = Vcor(eid='CAY.2314.SA2')
cby_2318_sa2 = Vcor(eid='CBY.2318.SA2')
cay_2320_sa2 = Vcor(eid='CAY.2320.SA2')
cby_2324_sa2 = Vcor(eid='CBY.2324.SA2')
cay_2326_sa2 = Vcor(eid='CAY.2326.SA2')
cby_2331_sa2 = Vcor(eid='CBY.2331.SA2')
cay_2332_sa2 = Vcor(eid='CAY.2332.SA2')
cby_2337_sa2 = Vcor(eid='CBY.2337.SA2')
cay_2338_sa2 = Vcor(eid='CAY.2338.SA2')
cby_2343_sa2 = Vcor(eid='CBY.2343.SA2')
cay_2344_sa2 = Vcor(eid='CAY.2344.SA2')
cby_2349_sa2 = Vcor(eid='CBY.2349.SA2')
cay_2350_sa2 = Vcor(eid='CAY.2350.SA2')
cby_2355_sa2 = Vcor(eid='CBY.2355.SA2')
cay_2356_sa2 = Vcor(eid='CAY.2356.SA2')
cby_2361_sa2 = Vcor(eid='CBY.2361.SA2')
cay_2362_sa2 = Vcor(eid='CAY.2362.SA2')
cby_2367_sa2 = Vcor(eid='CBY.2367.SA2')
cay_2369_sa2 = Vcor(eid='CAY.2369.SA2')
cby_2373_sa2 = Vcor(eid='CBY.2373.SA2')
cay_2375_sa2 = Vcor(eid='CAY.2375.SA2')
cby_2379_sa2 = Vcor(eid='CBY.2379.SA2')
cay_2381_sa2 = Vcor(eid='CAY.2381.SA2')
cby_2385_sa2 = Vcor(eid='CBY.2385.SA2')
cay_2387_sa2 = Vcor(eid='CAY.2387.SA2')
cby_2391_sa2 = Vcor(eid='CBY.2391.SA2')
cay_2393_sa2 = Vcor(eid='CAY.2393.SA2')
cby_2398_sa2 = Vcor(eid='CBY.2398.SA2')
cay_2399_sa2 = Vcor(eid='CAY.2399.SA2')
cby_2404_sa2 = Vcor(eid='CBY.2404.SA2')
cay_2405_sa2 = Vcor(eid='CAY.2405.SA2')
cby_2410_sa2 = Vcor(eid='CBY.2410.SA2')
cay_2411_sa2 = Vcor(eid='CAY.2411.SA2')
cby_2416_sa2 = Vcor(eid='CBY.2416.SA2')
cay_2417_sa2 = Vcor(eid='CAY.2417.SA2')
cby_2422_sa2 = Vcor(eid='CBY.2422.SA2')

# Undulators
u40_2200_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2200.SA2')
u40_2206_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2206.SA2')
u40_2212_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2212.SA2')
u40_2218_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2218.SA2')
u40_2224_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2224.SA2')
u40_2230_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2230.SA2')
u40_2237_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2237.SA2')
u40_2243_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2243.SA2')
u40_2255_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2255.SA2')
u40_2261_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2261.SA2')
u40_2267_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2267.SA2')
u40_2273_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2273.SA2')
u40_2279_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2279.SA2')
u40_2285_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2285.SA2')
u40_2291_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2291.SA2')
u40_2297_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2297.SA2')
u40_2310_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2310.SA2')
u40_2316_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2316.SA2')
u40_2322_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2322.SA2')
u40_2328_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2328.SA2')
u40_2334_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2334.SA2')
u40_2340_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2340.SA2')
u40_2346_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2346.SA2')
u40_2352_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2352.SA2')
u40_2358_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2358.SA2')
u40_2365_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2365.SA2')
u40_2371_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2371.SA2')
u40_2377_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2377.SA2')
u40_2383_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2383.SA2')
u40_2389_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2389.SA2')
u40_2395_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2395.SA2')
u40_2401_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2401.SA2')
u40_2407_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2407.SA2')
u40_2413_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2413.SA2')
u40_2419_sa2 = Undulator(lperiod=0.04, nperiods=125.0, eid='U40.2419.SA2')

# Monitors
bpme_2203_sa2 = Monitor(eid='BPME.2203.SA2')
bpme_2209_sa2 = Monitor(eid='BPME.2209.SA2')
bpme_2215_sa2 = Monitor(eid='BPME.2215.SA2')
bpme_2221_sa2 = Monitor(eid='BPME.2221.SA2')
bpme_2227_sa2 = Monitor(eid='BPME.2227.SA2')
bpme_2233_sa2 = Monitor(eid='BPME.2233.SA2')
bpme_2239_sa2 = Monitor(eid='BPME.2239.SA2')
bpme_2245_sa2 = Monitor(eid='BPME.2245.SA2')
bpmh_2249_sa2 = Monitor(eid='BPMH.2249.SA2')
bpme_2252_sa2 = Monitor(eid='BPME.2252.SA2')
bpme_2258_sa2 = Monitor(eid='BPME.2258.SA2')
bpme_2264_sa2 = Monitor(eid='BPME.2264.SA2')
bpme_2270_sa2 = Monitor(eid='BPME.2270.SA2')
bpme_2276_sa2 = Monitor(eid='BPME.2276.SA2')
bpme_2282_sa2 = Monitor(eid='BPME.2282.SA2')
bpme_2288_sa2 = Monitor(eid='BPME.2288.SA2')
bpme_2294_sa2 = Monitor(eid='BPME.2294.SA2')
bpme_2300_sa2 = Monitor(eid='BPME.2300.SA2')
bpmh_2303_sa2 = Monitor(eid='BPMH.2303.SA2')
bpme_2306_sa2 = Monitor(eid='BPME.2306.SA2')
bpme_2313_sa2 = Monitor(eid='BPME.2313.SA2')
bpme_2319_sa2 = Monitor(eid='BPME.2319.SA2')
bpme_2325_sa2 = Monitor(eid='BPME.2325.SA2')
bpme_2331_sa2 = Monitor(eid='BPME.2331.SA2')
bpme_2337_sa2 = Monitor(eid='BPME.2337.SA2')
bpme_2343_sa2 = Monitor(eid='BPME.2343.SA2')
bpme_2349_sa2 = Monitor(eid='BPME.2349.SA2')
bpme_2355_sa2 = Monitor(eid='BPME.2355.SA2')
bpme_2361_sa2 = Monitor(eid='BPME.2361.SA2')
bpme_2367_sa2 = Monitor(eid='BPME.2367.SA2')
bpme_2373_sa2 = Monitor(eid='BPME.2373.SA2')
bpme_2380_sa2 = Monitor(eid='BPME.2380.SA2')
bpme_2386_sa2 = Monitor(eid='BPME.2386.SA2')
bpme_2392_sa2 = Monitor(eid='BPME.2392.SA2')
bpme_2398_sa2 = Monitor(eid='BPME.2398.SA2')
bpme_2404_sa2 = Monitor(eid='BPME.2404.SA2')
bpme_2410_sa2 = Monitor(eid='BPME.2410.SA2')
bpme_2416_sa2 = Monitor(eid='BPME.2416.SA2')
bpme_2422_sa2 = Monitor(eid='BPME.2422.SA2')

# Markers
match_2197_sa2 = Marker(eid='MATCH.2197.SA2')
ensec_2423_sa2 = Marker(eid='ENSEC.2423.SA2')

# Lattice 
cell = (id_6001301_, match_2197_sa2, id_61060562_, cax_2198_sa2, cay_2198_sa2, d_4, u40_2200_sa2, d_5, cbx_2203_sa2, 
cby_2203_sa2, d_6, bpme_2203_sa2, d_7, qa_2203_sa2, id_28120785_, cax_2204_sa2, cay_2204_sa2, d_4, u40_2206_sa2, 
d_5, cbx_2209_sa2, cby_2209_sa2, d_6, bpme_2209_sa2, d_7, qa_2209_sa2, id_28120785_, cax_2210_sa2, cay_2210_sa2, 
d_4, u40_2212_sa2, d_5, cbx_2215_sa2, cby_2215_sa2, d_6, bpme_2215_sa2, d_7, qa_2215_sa2, id_28120785_, 
cax_2216_sa2, cay_2216_sa2, d_4, u40_2218_sa2, d_5, cbx_2221_sa2, cby_2221_sa2, d_6, bpme_2221_sa2, d_7, 
qa_2221_sa2, id_28120785_, cax_2222_sa2, cay_2222_sa2, d_4, u40_2224_sa2, d_5, cbx_2227_sa2, cby_2227_sa2, d_6, 
bpme_2227_sa2, d_7, qa_2227_sa2, id_28120785_, cax_2228_sa2, cay_2228_sa2, d_4, u40_2230_sa2, d_5, cbx_2233_sa2, 
cby_2233_sa2, d_6, bpme_2233_sa2, d_7, qa_2234_sa2, id_28120785_, cax_2234_sa2, cay_2234_sa2, d_4, u40_2237_sa2, 
d_5, cbx_2239_sa2, cby_2239_sa2, d_6, bpme_2239_sa2, d_7, qa_2240_sa2, id_28120785_, cax_2241_sa2, cay_2241_sa2, 
d_4, u40_2243_sa2, d_5, cbx_2245_sa2, cby_2245_sa2, d_6, bpme_2245_sa2, d_7, qa_2246_sa2, id_82512098_, 
bs_2247_sa2, id_99805086_, bs_2248_sa2, cbs_2248_sa2, d_53, bpmh_2249_sa2, d_54, bs_2249_sa2, cbs_2249_sa2, id_99805086_, 
bs_2251_sa2, cbs_2251_sa2, d_56, bpme_2252_sa2, d_7, qa_2252_sa2, id_28120785_, cax_2253_sa2, cay_2253_sa2, d_4, 
u40_2255_sa2, d_5, cbx_2257_sa2, cby_2257_sa2, d_6, bpme_2258_sa2, d_7, qa_2258_sa2, id_28120785_, cax_2259_sa2, 
cay_2259_sa2, d_4, u40_2261_sa2, d_5, cbx_2263_sa2, cby_2263_sa2, d_6, bpme_2264_sa2, d_7, qa_2264_sa2, 
id_28120785_, cax_2265_sa2, cay_2265_sa2, d_4, u40_2267_sa2, d_5, cbx_2270_sa2, cby_2270_sa2, d_6, bpme_2270_sa2, 
d_7, qa_2270_sa2, id_28120785_, cax_2271_sa2, cay_2271_sa2, d_4, u40_2273_sa2, d_5, cbx_2276_sa2, cby_2276_sa2, 
d_6, bpme_2276_sa2, d_7, qa_2276_sa2, id_28120785_, cax_2277_sa2, cay_2277_sa2, d_4, u40_2279_sa2, d_5, 
cbx_2282_sa2, cby_2282_sa2, d_6, bpme_2282_sa2, d_7, qa_2282_sa2, id_28120785_, cax_2283_sa2, cay_2283_sa2, d_4, 
u40_2285_sa2, d_5, cbx_2288_sa2, cby_2288_sa2, d_6, bpme_2288_sa2, d_7, qa_2288_sa2, id_28120785_, cax_2289_sa2, 
cay_2289_sa2, d_4, u40_2291_sa2, d_5, cbx_2294_sa2, cby_2294_sa2, d_6, bpme_2294_sa2, d_7, qa_2295_sa2, 
id_28120785_, cax_2295_sa2, cay_2295_sa2, d_4, u40_2297_sa2, d_5, cbx_2300_sa2, cby_2300_sa2, d_6, bpme_2300_sa2, 
d_7, qa_2301_sa2, id_82512098_, bs_2301_sa2, id_99805086_, bs_2303_sa2, cbs_2303_sa2, d_53, bpmh_2303_sa2, d_54, 
bs_2304_sa2, cbs_2304_sa2, id_99805086_, bs_2306_sa2, cbs_2306_sa2, d_56, bpme_2306_sa2, d_7, qa_2307_sa2, id_28120785_, 
cax_2308_sa2, cay_2308_sa2, d_4, u40_2310_sa2, d_5, cbx_2312_sa2, cby_2312_sa2, d_6, bpme_2313_sa2, d_7, 
qa_2313_sa2, id_28120785_, cax_2314_sa2, cay_2314_sa2, d_4, u40_2316_sa2, d_5, cbx_2318_sa2, cby_2318_sa2, d_6, 
bpme_2319_sa2, d_7, qa_2319_sa2, id_28120785_, cax_2320_sa2, cay_2320_sa2, d_4, u40_2322_sa2, d_5, cbx_2324_sa2, 
cby_2324_sa2, d_6, bpme_2325_sa2, d_7, qa_2325_sa2, id_28120785_, cax_2326_sa2, cay_2326_sa2, d_4, u40_2328_sa2, 
d_5, cbx_2331_sa2, cby_2331_sa2, d_6, bpme_2331_sa2, d_7, qa_2331_sa2, id_28120785_, cax_2332_sa2, cay_2332_sa2, 
d_4, u40_2334_sa2, d_5, cbx_2337_sa2, cby_2337_sa2, d_6, bpme_2337_sa2, d_7, qa_2337_sa2, id_28120785_, 
cax_2338_sa2, cay_2338_sa2, d_4, u40_2340_sa2, d_5, cbx_2343_sa2, cby_2343_sa2, d_6, bpme_2343_sa2, d_7, 
qa_2343_sa2, id_28120785_, cax_2344_sa2, cay_2344_sa2, d_4, u40_2346_sa2, d_5, cbx_2349_sa2, cby_2349_sa2, d_6, 
bpme_2349_sa2, d_7, qa_2349_sa2, id_28120785_, cax_2350_sa2, cay_2350_sa2, d_4, u40_2352_sa2, d_5, cbx_2355_sa2, 
cby_2355_sa2, d_6, bpme_2355_sa2, d_7, qa_2355_sa2, id_28120785_, cax_2356_sa2, cay_2356_sa2, d_4, u40_2358_sa2, 
d_5, cbx_2361_sa2, cby_2361_sa2, d_6, bpme_2361_sa2, d_7, qa_2362_sa2, id_28120785_, cax_2362_sa2, cay_2362_sa2, 
d_4, u40_2365_sa2, d_5, cbx_2367_sa2, cby_2367_sa2, d_6, bpme_2367_sa2, d_7, qa_2368_sa2, id_28120785_, 
cax_2369_sa2, cay_2369_sa2, d_4, u40_2371_sa2, d_5, cbx_2373_sa2, cby_2373_sa2, d_6, bpme_2373_sa2, d_7, 
qa_2374_sa2, id_28120785_, cax_2375_sa2, cay_2375_sa2, d_4, u40_2377_sa2, d_5, cbx_2379_sa2, cby_2379_sa2, d_6, 
bpme_2380_sa2, d_7, qa_2380_sa2, id_28120785_, cax_2381_sa2, cay_2381_sa2, d_4, u40_2383_sa2, d_5, cbx_2385_sa2, 
cby_2385_sa2, d_6, bpme_2386_sa2, d_7, qa_2386_sa2, id_28120785_, cax_2387_sa2, cay_2387_sa2, d_4, u40_2389_sa2, 
d_5, cbx_2391_sa2, cby_2391_sa2, d_6, bpme_2392_sa2, d_7, qa_2392_sa2, id_28120785_, cax_2393_sa2, cay_2393_sa2, 
d_4, u40_2395_sa2, d_5, cbx_2398_sa2, cby_2398_sa2, d_6, bpme_2398_sa2, d_7, qa_2398_sa2, id_28120785_, 
cax_2399_sa2, cay_2399_sa2, d_4, u40_2401_sa2, d_5, cbx_2404_sa2, cby_2404_sa2, d_6, bpme_2404_sa2, d_7, 
qa_2404_sa2, id_28120785_, cax_2405_sa2, cay_2405_sa2, d_4, u40_2407_sa2, d_5, cbx_2410_sa2, cby_2410_sa2, d_6, 
bpme_2410_sa2, d_7, qa_2410_sa2, id_28120785_, cax_2411_sa2, cay_2411_sa2, d_4, u40_2413_sa2, d_5, cbx_2416_sa2, 
cby_2416_sa2, d_6, bpme_2416_sa2, d_7, qa_2416_sa2, id_28120785_, cax_2417_sa2, cay_2417_sa2, d_4, u40_2419_sa2, 
d_5, cbx_2422_sa2, cby_2422_sa2, d_6, bpme_2422_sa2, d_7, qa_2422_sa2, id_59449715_, ensec_2423_sa2)

# power supplies 

#  
qa_2203_sa2.ps_id = 'QA.1.SA2'
qa_2209_sa2.ps_id = 'QA.2.SA2'
qa_2215_sa2.ps_id = 'QA.1.SA2'
qa_2221_sa2.ps_id = 'QA.2.SA2'
qa_2227_sa2.ps_id = 'QA.1.SA2'
qa_2234_sa2.ps_id = 'QA.2.SA2'
qa_2240_sa2.ps_id = 'QA.1.SA2'
qa_2246_sa2.ps_id = 'QA.2.SA2'
qa_2252_sa2.ps_id = 'QA.1.SA2'
qa_2258_sa2.ps_id = 'QA.2.SA2'
qa_2264_sa2.ps_id = 'QA.1.SA2'
qa_2270_sa2.ps_id = 'QA.2.SA2'
qa_2276_sa2.ps_id = 'QA.1.SA2'
qa_2282_sa2.ps_id = 'QA.2.SA2'
qa_2288_sa2.ps_id = 'QA.1.SA2'
qa_2295_sa2.ps_id = 'QA.2.SA2'
qa_2301_sa2.ps_id = 'QA.1.SA2'
qa_2307_sa2.ps_id = 'QA.2.SA2'
qa_2313_sa2.ps_id = 'QA.1.SA2'
qa_2319_sa2.ps_id = 'QA.2.SA2'
qa_2325_sa2.ps_id = 'QA.1.SA2'
qa_2331_sa2.ps_id = 'QA.2.SA2'
qa_2337_sa2.ps_id = 'QA.1.SA2'
qa_2343_sa2.ps_id = 'QA.2.SA2'
qa_2349_sa2.ps_id = 'QA.1.SA2'
qa_2355_sa2.ps_id = 'QA.2.SA2'
qa_2362_sa2.ps_id = 'QA.1.SA2'
qa_2368_sa2.ps_id = 'QA.2.SA2'
qa_2374_sa2.ps_id = 'QA.1.SA2'
qa_2380_sa2.ps_id = 'QA.2.SA2'
qa_2386_sa2.ps_id = 'QA.1.SA2'
qa_2392_sa2.ps_id = 'QA.2.SA2'
qa_2398_sa2.ps_id = 'QA.1.SA2'
qa_2404_sa2.ps_id = 'QA.2.SA2'
qa_2410_sa2.ps_id = 'QA.1.SA2'
qa_2416_sa2.ps_id = 'QA.2.SA2'
qa_2422_sa2.ps_id = 'QA.1.SA2'

#  

#  

#  

#  
bs_2247_sa2.ps_id = 'BS.1.SA2'
bs_2248_sa2.ps_id = 'BS.1.SA2'
bs_2249_sa2.ps_id = 'BS.1.SA2'
bs_2251_sa2.ps_id = 'BS.1.SA2'
bs_2301_sa2.ps_id = 'BS.2.SA2'
bs_2303_sa2.ps_id = 'BS.2.SA2'
bs_2304_sa2.ps_id = 'BS.2.SA2'
bs_2306_sa2.ps_id = 'BS.2.SA2'
