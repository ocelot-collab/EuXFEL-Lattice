from ocelot import *
from ocelot.gui import *

parray_bc0_19 = load_particle_array("2019/section_BC0.npz")
show_e_beam(parray_bc0_19, figname="BC0 2019")
tws_19 = get_envelope(parray_bc0_19)

parray_bc0 = load_particle_array("particles/section_BC0.npz")
show_e_beam(parray_bc0, figname="BC0")
tws = get_envelope(parray_bc0)
print("BC0    - 2019   -     current ")
print(f"beta_x {tws_19.beta_x} / {tws.beta_x}")
print(f"beta_y {tws_19.beta_y} / {tws.beta_y}")
print(f"beta_x {tws_19.alpha_x} / {tws.alpha_x}")
print(f"beta_x {tws_19.alpha_y} / {tws.alpha_y}")
plt.show()

parray_bc1_19 = load_particle_array("2019/section_BC1.npz")
show_e_beam(parray_bc1_19, figname="BC0 2019")
tws_19 = get_envelope(parray_bc1_19)

parray_bc1 = load_particle_array("particles/section_BC1.npz")
show_e_beam(parray_bc1, figname="BC0")
tws = get_envelope(parray_bc1)
print("BC1    - 2019   -     current ")
print(f"beta_x {tws_19.beta_x} / {tws.beta_x}")
print(f"beta_y {tws_19.beta_y} / {tws.beta_y}")
print(f"beta_x {tws_19.alpha_x} / {tws.alpha_x}")
print(f"beta_x {tws_19.alpha_y} / {tws.alpha_y}")
plt.show()


parray_bc2_19 = load_particle_array("2019/section_BC2.npz")
show_e_beam(parray_bc2_19, figname="BC2 2019")
tws_19 = get_envelope(parray_bc2_19)

parray_bc2 = load_particle_array("particles/section_BC2.npz")
show_e_beam(parray_bc2, figname="BC2")
tws = get_envelope(parray_bc2)
print("BC2    - 2019   -     current ")
print(f"beta_x {tws_19.beta_x} / {tws.beta_x}")
print(f"beta_y {tws_19.beta_y} / {tws.beta_y}")
print(f"beta_x {tws_19.alpha_x} / {tws.alpha_x}")
print(f"beta_x {tws_19.alpha_y} / {tws.alpha_y}")
plt.show()
