from ocelot import *
from ocelot.gui import *
import os

parray_19 = load_particle_array('2019/section_LH.npz')
section='LH'
show_e_beam(parray_19, figname=(section+' 2019'))
tws_19 = get_envelope(parray_19)
parray = load_particle_array("particles/section_LH.npz")
show_e_beam(parray, figname=section)
tws = get_envelope(parray)
print(section+"        -   2019   -      current ")
print(f"beta_x {tws_19.beta_x} / {tws.beta_x}")
print(f"beta_y {tws_19.beta_y} / {tws.beta_y}")
print(f"alpha_x {tws_19.alpha_x} / {tws.alpha_x}")
print(f"alpha_y {tws_19.alpha_y} / {tws.alpha_y}")
plt.show()


for file in os.listdir('2019'):
    parray_19 = load_particle_array('2019/'+file)
    section=file.split('_')[1].split('.')[0]
    show_e_beam(parray_19, figname=(section+' 2019'))
    tws_19 = get_envelope(parray_19)

    parray = load_particle_array("particles/"+file)
    show_e_beam(parray, figname=section)
    tws = get_envelope(parray)
    print(section+"        -   2019   -      current ")
    print(f"beta_x {tws_19.beta_x} / {tws.beta_x}")
    print(f"beta_y {tws_19.beta_y} / {tws.beta_y}")
    print(f"alpha_x {tws_19.alpha_x} / {tws.alpha_x}")
    print(f"alpha_y {tws_19.alpha_y} / {tws.alpha_y}")
    plt.show()
