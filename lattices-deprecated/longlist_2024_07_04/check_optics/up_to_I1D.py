import sys

import matplotlib.pyplot as plt

sys.path.insert(1, "../")
import pandas as pd
from ocelot import *
from ocelot.gui import *
import i1, i1d

# calculate twiss functions with ocelot
lat = MagneticLattice(i1.cell + i1d.cell)
tws = twiss(lat, i1.tws0)


# READ LONGLIST TWISS PATAMETERS for crosschecking with ocelot

# NOTE:
# we renamed line 2346 SECTION CL to TL which affect this marker ENBLOCK.1891.CL
# we renamed line 2470 SUBSECTION TL to TL5 which affect this marker ENSEC.2058.TL

file_path = "../component_list_2024.07.04.xls"
sheet_name = "LONGLIST"  
# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# I1
df_i1 = df[df["SECTION"] == "I1"]
df_i1 = df_i1[df_i1["SUBSECTION"] != "G1D"]
df_i1 = df_i1[df_i1["SUBSECTION"] != "I1T"]
df_i1 = df_i1[df_i1["SUBSECTION"] != "B0"]
df_i1 = df_i1[df_i1["SUBSECTION"] != "I1"]
# L1
df_i1d = df[df["SECTION"] == "I1D"]

# concatenate sections
s = np.concatenate((df_i1["S"].to_numpy() , df_i1d["S"].to_numpy()))+23.2
beta_x = np.concatenate((df_i1["BETX"].to_numpy() , df_i1d["BETX"].to_numpy()))
beta_y = np.concatenate((df_i1["BETY"].to_numpy() , df_i1d["BETY"].to_numpy()))
D_x = np.concatenate((df_i1["DX"].to_numpy() , df_i1d["DX"].to_numpy()))
D_y = np.concatenate((df_i1["DY"].to_numpy() , df_i1d["DY"].to_numpy()))

plt.figure(1)
plt.title("BETA_X")
plt.plot(s, beta_x, label="beta_x, mad8")
s_ocl = [tw.s for tw in tws]
beta_x_ocl = [tw.beta_x for tw in tws]
beta_y_ocl = [tw.beta_y for tw in tws]
plt.plot(s_ocl, beta_x_ocl,"--", label="beta_x, ocelot")
plt.ylabel(r"$\beta_x$ [m]")
plt.xlabel("s [m]")
plt.legend()

plt.figure(2)
plt.title("BETA_Y")
plt.plot(s, beta_y, label="beta_y, mad8")
plt.plot(s_ocl, beta_y_ocl,"--", label="beta_y, ocelot")
plt.xlabel("s [m]")
plt.ylabel(r"$\beta_y$ [m]")
plt.legend()

d_x_ocl = [tw.Dx for tw in tws]
d_y_ocl = [tw.Dy for tw in tws]

plt.figure(3)
plt.title("D_X")
plt.plot(s, D_x, label="D_x, mad8")
plt.plot(s_ocl, d_x_ocl, "--", label="D_x, ocelot")
plt.xlabel("s [m]")
plt.ylabel(r"$D_x$ [m]")
plt.legend()

plt.figure(4)
plt.title("D_Y")
plt.plot(s, D_y, label="D_y, mad8")
plt.plot(s_ocl, d_y_ocl, "--", label="D_y, ocelot")
plt.xlabel("s [m]")
plt.ylabel(r"$D_x$ [m]")
plt.legend()

plt.show()