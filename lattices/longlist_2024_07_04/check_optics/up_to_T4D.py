import sys
sys.path.insert(1, "../")

import pandas as pd
from ocelot import *
from ocelot.gui import *
import i1, l1, l2, l3, cl, tl34, sase1, t4, sase3, t4d

# calculate twiss functions with ocelot
lat = MagneticLattice(i1.cell + l1.cell + l2.cell + l3.cell + cl.cell + tl34.cell +  sase1.cell+ t4.cell + sase3.cell)
tws = twiss(lat, i1.tws0)


# READ LONGLIST TWISS PATAMETERS for crosschecking with ocelot

# NOTE:
# we renamed line 2346 SECTION CL to TL which affect this marker ENBLOCK.1891.CL
# we renamed line 2470 SUBSECTION TL to TL5 which affect this marker ENSEC.2058.TL

file_path = "../component_list_2024.07.04.xls"
sheet_name = "LONGLIST"  # Replace with your sheet name
# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# I1
df_i1 = df[df["SECTION"] == "I1"]
df_i1 = df_i1[df_i1["SUBSECTION"] != "G1D"]
# L1
df_l1 = df[df["SECTION"] == "L1"]
# B1
df_b1 = df[df["SECTION"] == "B1"]
# L2
df_l2 = df[df["SECTION"] == "L2"]
# B2
df_b2 = df[df["SECTION"] == "B2"]
# L3
df_l3 = df[df["SECTION"] == "L3"]
# CL
df_cl = df[df["SECTION"] == "CL"]
# TL1 and TL2
df_tl = df[df["SECTION"] == "TL"]
df_tl = df_tl[df_tl["SUBSECTION"] != "TL3"]
df_tl = df_tl[df_tl["SUBSECTION"] != "TL4"]
df_tl = df_tl[df_tl["SUBSECTION"] != "TL5"]

# SASA1

# T4

# SASE3



# concatenate sections
s = np.concatenate((df_i1["S"].to_numpy() , df_l1["S"].to_numpy(),df_b1["S"].to_numpy(),  df_l2["S"].to_numpy(), df_b2["S"].to_numpy(), df_l3["S"].to_numpy(), df_cl["S"].to_numpy(), df_tl["S"].to_numpy()))+23.2
beta_x = np.concatenate((df_i1["BETX"].to_numpy() , df_l1["BETX"].to_numpy(),df_b1["BETX"].to_numpy(),  df_l2["BETX"].to_numpy(), df_b2["BETX"].to_numpy(), df_l3["BETX"].to_numpy(), df_cl["BETX"].to_numpy(), df_tl["BETX"].to_numpy()))
beta_y = np.concatenate((df_i1["BETY"].to_numpy() , df_l1["BETY"].to_numpy(),df_b1["BETY"].to_numpy(),  df_l2["BETY"].to_numpy(), df_b2["BETY"].to_numpy(), df_l3["BETY"].to_numpy(), df_cl["BETY"].to_numpy(), df_tl["BETY"].to_numpy()))


plt.figure(1)
plt.title("BETA_X")
plt.plot(s, beta_x, label="beta_x, mad8")
s_ocl = [tw.s for tw in tws]
beta_x_ocl = [tw.beta_x for tw in tws]
beta_y_ocl = [tw.beta_y for tw in tws]
plt.plot(s_ocl, beta_x_ocl, label="beta_x, ocelot")
plt.ylabel(r"$\beta_x$ [m]")
plt.xlabel("s [m]")
plt.legend()

plt.figure(2)
plt.title("BETA_Y")
plt.plot(s, beta_y, label="beta_y, mad8")
plt.plot(s_ocl, beta_y_ocl, label="beta_y, ocelot")
plt.xlabel("s [m]")
plt.ylabel(r"$\beta_y$ [m]")
plt.legend()
plt.show()