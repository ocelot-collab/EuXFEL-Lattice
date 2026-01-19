from ocelot import *
from ocelot.gui import *
import i1 as i1
import l1, l2, l3, cl, tl34_sa2, sase1, t4, t1,  sase2 , t3, t5, t5d, tl34


## I1 check
#lat = MagneticLattice(i1.cell)
#
#tws = twiss(lat, i1.tws0)
##print(tws[-1])
#plot_opt_func(lat, tws)
#plt.show()
#
## L1 check
#
#lat = MagneticLattice(l1.cell)
#
#tws = twiss(lat, l1.tws0)
#
#plot_opt_func(lat, tws)
#plt.show()

# L2 check

lat = MagneticLattice(sase2.cell)

tws = twiss(lat, sase2.tws0)
print(tws[-1])
plot_opt_func(lat, tws)
plt.show()

# I1 + l1 + l2 + l3 + cl + tl34 + sase1 + t4 + sase3 + t4d

#lat = MagneticLattice(i1.cell + l1.cell + l2.cell + l3.cell + cl.cell + t34_sa2.cell + t1.cell + sase2.cell + t3.cell + t5.cell + t5d.cell)
lat = MagneticLattice(i1.cell + l1.cell + l2.cell + l3.cell + cl.cell + tl34.cell + sase1.cell)#t1.cell + sase2.cell + t3.cell + t5.cell + t5d.cell)

tws = twiss(lat, i1.tws0)

plot_opt_func(lat, tws)
plt.show()