from ocelot import *
from ocelot.gui import *
import os

section='LH'
parray = load_particle_array("particles/section_LH.npz")
show_e_beam(parray, figname=section)
tws = get_envelope(parray)
print(section)
print(f"beta_x {tws.beta_x}")
print(f"beta_y {tws.beta_y}")
print(f"alpha_x {tws.alpha_x}")
print(f"alpha_y {tws.alpha_y}")
plt.show()

for file in os.listdir('2019'):
   
    section=file.split('_')[1].split('.')[0]
    parray = load_particle_array("particles/"+file)
    show_e_beam(parray, figname=section)
    tws = get_envelope(parray)
    print(section)
    print(f"beta_x  {tws.beta_x}")
    print(f"beta_y  {tws.beta_y}")
    print(f"alpha_x {tws.alpha_x}")
    print(f"alpha_y {tws.alpha_y}")
    plt.show()
