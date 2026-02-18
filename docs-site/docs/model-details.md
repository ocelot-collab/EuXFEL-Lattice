## Further Comments

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
