import sys
sys.path.insert(1, "/Users/tomins/Nextcloud/DESY/repository/EuXFEL-Lattice/lattices/longlist_2024_07_04/")

import pandas as pd
from ocelot import *
from ocelot.gui import *
import sase3

# calculate twiss functions with ocelot
lat = MagneticLattice(sase3.cell)
tws = twiss(lat, sase3.tws0)

file_path = "../component_list_2024.07.04.xls"
sheet_name = "LONGLIST"  # Replace with your sheet name
# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# SASE3
df_sa3 = df[df["SECTION"] == "SA3"]


# concatenate sections
s = df_sa3["S"].to_numpy() + 23.2
beta_x = df_sa3["BETX"].to_numpy()
beta_y = df_sa3["BETY"].to_numpy()


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