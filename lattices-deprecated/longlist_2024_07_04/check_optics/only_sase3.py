import sys
sys.path.insert(1, "../")

import pandas as pd
from ocelot import *
from ocelot.gui import *
import  i1, l1, l2, l3, cl,sase3, l3, tl2, tl34, sase1,t4, sase3,t4d
import numpy as np

# calculate twiss functions with ocelot
#lat = MagneticLattice(sase3.cell)
#tws = twiss(lat, sase3.tws0)


lat = MagneticLattice(cl.cell + tl2.cell + tl34.cell +  sase1.cell+ t4.cell + sase3.cell + t4d.cell)
tws = twiss(lat, cl.tws0)

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

df_tl = df[df["SECTION"] == "TL"]
#df_tl = df_tl[df_tl["SUBSECTION"] != "TL3"]
#df_tl = df_tl[df_tl["SUBSECTION"] != "TL4"]
#df_tl = df_tl[df_tl["SUBSECTION"] != "TL5"]
df_t2 = df[df["SECTION"] == "T2"]
# SASE1
df_sa1 = df[df["SECTION"] == "SA1"]
#df_sa3 = df[df["SECTION"] == "L3"]
# T4
df_t4 = df[df["SECTION"] == "T4"]
#s = df_tl["S"].to_numpy() + 23.2
#beta_x = df_tl["BETX"].to_numpy()
#beta_y = df_tl["BETY"].to_numpy()
# SASE3
df_sa3 = df[df["SECTION"] == "SA3"]
# T4D
df_t4d = df[df["SECTION"] == "T4D"]


s = np.concatenate((df_cl["S"].to_numpy(), df_tl["S"].to_numpy(),
                    df_t2["S"].to_numpy(),df_sa1["S"].to_numpy(),df_t4["S"].to_numpy(),
                    df_sa3["S"].to_numpy(),df_t4d["S"].to_numpy()))+23.2

beta_x = np.concatenate((df_cl["BETX"].to_numpy(), df_tl["BETX"].to_numpy(),
                         df_t2["BETX"].to_numpy(),df_sa1["BETX"].to_numpy(),df_t4["BETX"].to_numpy(),
                         df_sa3["BETX"].to_numpy(),df_t4d["BETX"].to_numpy()))

beta_y = np.concatenate((df_cl["BETY"].to_numpy(), df_tl["BETY"].to_numpy(),
                         df_t2["BETY"].to_numpy(),df_sa1["BETY"].to_numpy(),df_t4["BETY"].to_numpy(),
                         df_sa3["BETY"].to_numpy(),df_t4d["BETY"].to_numpy()))


# concatenate sections
#s = df_cl["S"].to_numpy() + 23.2
#beta_x = df_cl["BETX"].to_numpy()
#beta_y = df_cl["BETY"].to_numpy()


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