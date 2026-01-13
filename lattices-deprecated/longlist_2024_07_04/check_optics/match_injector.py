import sys
sys.path.insert(1, "../")

from ocelot import *
from ocelot.gui import *
import i1_track as i1

lat = MagneticLattice(i1.cell)

betx = 3.131695851; alfx = -0.9249364470
bety = 5.417462794; alfy = +1.730107901
tws_end = Twiss(beta_x=betx, beta_y=bety, alpha_x=alfx, alpha_y=alfy, E=0.13)
constr = {i1.match_52_i1: {'beta_x':betx, 'beta_y':bety, "alpha_x": alfx, "alpha_y": alfy}}

vars = [i1.q_37_i1, i1.q_38_i1, i1.qi_46_i1, i1.qi_47_i1, i1.qi_50_i1]

match(lat, constr, vars, tw=i1.tws0)

for q in vars:
    print(q)

tws = twiss(lat, tws0=i1.tws0)

plot_opt_func(lat, tws)
plt.show()