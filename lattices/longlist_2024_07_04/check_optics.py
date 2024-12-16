from ocelot import *
from ocelot.gui import *
import i1 as i1
import l1


# I1 check
lat = MagneticLattice(i1.cell)

tws = twiss(lat, i1.tws0)
print(tws[-1])
plot_opt_func(lat, tws)
plt.show()

# L1 check

lat = MagneticLattice(l1.cell)

tws = twiss(lat, l1.tws0)

plot_opt_func(lat, tws)
plt.show()

# I1 + l1

lat = MagneticLattice(i1.cell + l1.cell)

tws = twiss(lat, i1.tws0)

plot_opt_func(lat, tws)
plt.show()