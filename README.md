# EuXFEL-Lattice
Unofficial Ocelot EuXFEL lattice repository. Created by Bianca,  Sergey and Stuart.

This is the repository for the EuXFEL ocelot repository.  The idea
 should be one transparent model that everyone uses and we can all
 contribute to and benefit from.

Currently the OCELOT Python EuXFEL sequences are generated from the
"Component List", an Excel spreadsheet generated internally by the
group leader as the "single source of truth" for what actually is in
the tunnel.  These files can be found here https://xfel.desy.de/operation/component_list/.


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
  * gun_2019 - initial beam distribution used in the settings https://www.desy.de/fel-beam/s2e/xfel/Nominal/nom250pC.html used for the 2019 simulation studies published in [this article](https://www.sciencedirect.com/science/article/abs/pii/S0168900221000954)
* Astra_gun_simulation/250pC_phi42 - by downloading the Astra executables from the official page https://www.desy.de/~mpyflo/ and adjusting the parameters in generator.in first (the laser pulse length sig_clock) and in the rfgun.in file later (phi(1)), it is possible to simulate the particle distribution from the gun till the position specified in the ZSTOP parameter. The current setting was developed by Igor Zagorodnov for 250pC. The radial_smear.m is a Matlab script for smoothing the profile obtain by the generator
* scripts - s2e main scripts 
* utils - beam matching script
* src/euxfel - the location of a new Python package that aims to
  encapsulate all or most of the above and will replace many of these
  features.  


## Getting started

Clone the repository and install the package.

```
$ cd EuXFEL-Lattice
pip install .
```

Some key functionality can then be accessed from the command line:

```bash
$ euxfel convert # Regenerate the Python subsequences
$ euxfel compare # Compare the OCELOT optics for all the paths through the machine with the Component List.
$ euxfel plot i1d # Just plot for I1D.
```

Otherwise you can use it in Python, for example to access the sequence from the cathode to I1D in Python

```python
import euxfel.sequences as sequences
from ocelot import *
import matplotlib.pyplot as plt
twiss0 = sequences.CATHODE_TWISS0
sequence = sequences.cathode_to_i1d
# Example of use with plain OCELOT:
plot_opt_funct(MagneticLattice(sequence), twiss0)
plt.show()
```

## TODO:

- [ ] Integration of physics processes stuff (i.e. SectionTrack and friends) into package
- [ ] Particle tracking helper stuff into Python package.
- [ ] Python to Longlist (i.e. full round trip) converter.


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

📚 Citation Notice

If you use the s2e scripts from this repository or any of their derivatives in your work, please cite the following:
1. S. Tomin, I. Agapov, M. Dohlus, and I. Zagorodnov, Ocelot as a framework for beam dynamics simulations of x-ray sources,
in Proceedings of the International Particle Accelerator Conference (IPAC), Copenhagen, Denmark (2017), WEPAB031.
2. I. Zagorodnov, M. Dohlus, and S. Tomin, Accelerator beam dynamics at the European X-ray free-electron laser,
Phys. Rev. Accel. Beams 22, 024401 (2019). https://doi.org/10.1103/PhysRevAccelBeams.22.024401

