ocelot_dir = "/Users/tomins/Nextcloud/DESY/repository/ocelot"
import sys

sys.path.append(ocelot_dir)
sys.path.insert(1, "../")

from ocelot import *
from ocelot.gui import *
import lattices.longlist_2024_07_04.i1 as i1
import lattices.longlist_2024_07_04.i1d as i1d

lat = MagneticLattice(i1.cell + i1d.cell)

tws = twiss(lat, i1.tws0)

plot_opt_func(lat, tws,fig_name="Design Optics", legend=False)
plt.show()

# different dispersions amplitude on screen OTRC.64.I1D
# DDx = {Dx: ['QI.60.I1'.k1, 'QI.61.I1'.k1, 'QI.63.I1D'.k1]}
DDx = {1.197: [-2.14371, 3.50288, -1.05],
       1.024: [ -2.1415, 3.50095, 0.45],
       0.801: [-2.14121, 3.45060, 2.45],
       0.592: [-2.14030, 3.32194, 4.401795] }

quads_to_change = [i1.qi_60_i1, i1.qi_61_i1, i1d.qi_63_i1d]

# check optics with dispersion Dx = 1.197 m

for i, q in enumerate(quads_to_change):
    q.k1 = DDx[1.197][i]

lat = MagneticLattice(i1.cell + i1d.cell, stop=i1d.otrc_64_i1d)
tws = twiss(lat, i1.tws0)

plot_opt_func(lat, tws,fig_name="HiRes optics up to OTRC.64.I1D", legend=False)
plt.show()