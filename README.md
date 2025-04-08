# EuXFEL-Lattice
Unofficial Ocelot EuXFEL lattice repository. Created by Bianca and Sergey. 

Lattice files based on MS Excel "LongList" https://xfel.desy.de/operation/component_list/

Repository structure:
* Lattices - lattice files in ocelot format
  * LL2ocelot - scripts to generate ocelot lattice files from MS Excel LongList 
  * longlist_2024_07_04
    * check_optics - comparison scripts for plotting the beta functions and dispersions calculated with Ocelot and read from the longlist (obtained with Mad8)
    * ocelot lattice files for each section of the machine (building up s2e-lines as explained in the list below)
    * readme.txt lists the modifications done to the excel file or to the generated python lattice files in order to accurately model all the elements
* s2e_sections - EuXFEL accelerator section descriptions 
* wakes - database of wakefield files (cavities, collimators, dechirpers etc)
* beam_files - particle distributions 
  * gun - initial beam distribution from gun (3.2 m position)
  * 
* scripts - s2e main scripts 
* utils - beam matching script
* Astra_gun_simulation/250pC_phi42 - by downloading the Astra executables from the official page https://www.desy.de/~mpyflo/ and adjusting the parameters in generator.in first (the laser pulse length sig_clock) and in the rfgun.in file later (phi(1)), it is possible to simulate the particle distribution from the gun till the position specified in the ZSTOP parameter. The current setting was developed by Igor Zagorodnov for 250pC. The radial_smear.m is a Matlab script for smoothing the profile obtain by the generator


Lattice files - 
1. gun to tld: i1, l1, l2, l3, cl, tl2_tld, tld
2. gun to t4d: i1, l1, l2, l3, cl, tl2, tl34, sase1, t4, sase3, t4d
3. gun to t5d: i1, l1, l2, l3, cl, tl2, tl34_sa2, t1, sase2, t3, t5, t5d
4. gun to i1d: i1, i1d
5. gun to b1d: i1, l1, b1d
6. gun to b2d: i1, l1, l2, b2d

######  IMPORTANT ######
In the distribution section two beams (straight and kicked) are going through the same quadrupoles and hence see the different magnetic fields:
          • straight beam only quadrupole component
          • kicked beam - main quadrupole component and additional dipole components. 
The model of the magnets for the kicked beams needs to take into account these components.

Specifically, the extraction to T5D and the extraction to TLD lines have offsets on bot horizontal and vertical planes. The magnet needs to be split into N slices: sequence of horizontal and vertical combine function magnets.
More details about the modelling of the magnetic elements for the kicked beams can be found in [ this presentation ](NewModel_T1_TLD_Jan2025.pdf), courtesy of *Nina Golubeva*.


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


