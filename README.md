# EuXFEL-Lattice
Unofficial Ocelot EuXFEL lattice repository

Lattice files based on MS Excel "LongList" https://xfel.desy.de/operation/component_list/

Repository structure:
* Lattices - lattice files in ocelot format
  * LL2ocelot - script to generate ocelot lattice files from MS Excel LongList 
  * longlist_2024_07_04
  * etc
* s2e_sections - EuXFEL accelerator section descriptions 
* wakes - database of wakefield files (cavities, collimators, dechirpers etc)
* beam_files - particle distributions 
  * gun - initial beam distribution from gun (3.2 m position)
  * 
* scripts - s2e main scripts 


Lattice files - 
1. gun to tld: i1, l1, l2, l3, cl, tld
2. gun to t4d: i1, l1, l2, l3, cl, tl34, sase1, t4, sase3, t4d
3. gun to t5d: i1, l1, l2, l3, cl, tl34_sa2, t1, sase2, t3, t5, t5d
4. gun to i1d: i1, i1d
5. gun to b1d: i1, l1, b1d
6. gun to b2d: i1, l1, l2, b2d

Note : To generate files ... 

### NOTE:
1. LH undulator.
   - The length of 0.74 m is the iron length.
   - The model of natural focusing has been created using measured field profiles which are longer (0.918 m).

2. Natural focusing
   - In the design optics the natural undulator focusing is not taking into account (drift).
   - To take into account the natural focusing you have
     to set up the beam parameters (energy) and the undulator setup (gap).
     The natural focusing effect (matrices) is then calculated using analytical formulas. One example can be found in the file:
     SET_LHund_closed_130MeV_42mm.txm
   - If the natural focusing is taken into account, it needs to rematch the beam in the injector.

3. Coupler kick in all RF cavities are off.