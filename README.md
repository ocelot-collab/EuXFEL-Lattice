[![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Focelot-collab%2FEuXFEL-Lattice%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&style=flat&logo=python)](https://www.python.org)
[![Static Badge](https://img.shields.io/badge/10.1103%2FPhysRevAccelBeams.22.024401-purple?label=PRAB&link=https%3A%2F%2Fdoi.org%2F10.1103%2FPhysRevAccelBeams.22.024401)](https://doi.org/10.1103/PhysRevAccelBeams.22.024401)
[![Static Badge](https://img.shields.io/badge/10.18429%2FJACoW--IPAC2017--WEPAB031-purple?label=IPAC&link=https%3A%2F%2Fdoi.org%2F10.18429%2FJACoW-IPAC2017-WEPAB031)](https://doi.org/10.18429/JACoW-IPAC2017-WEPAB031)


# EuXFEL-Lattice
This is the repository for the EuXFEL ocelot repository.  The idea
 behind it is to have one transparent model that everyone uses,
 everyone can contribute to, and in turn everyone can benefit from
 each other's work.

The full documentation can be found [here](https://www.ocelot-collab.com/EuXFEL-Lattice/).

## Getting started

Clone the repository and install the package.

```bash
git clone git@github.com:ocelot-collab/EuXFEL-Lattice.git
cd EuXFEL-Lattice
pip install .
```

Optionally install in editable mode:

```bash
pip install --editable .
```

### Command Line Interface

To check the installation has worked, try using the command line
interface to look at the optics for the cathode to each of the dumps
(run `euxfel --help` to see full set of available commands):

```bash
euxfel plot
```


### Full Start to End Simulations

Look in the top-level directory `s2e_scripts` for examples of start to
end simulation scripts from 3.2m to various targets downstream.

After installing, running a simulation from 3.2m after the cathode to,
for example, just in front of the SASE1 undulators can be done with:

```bash
cd s2e_scripts
python s2e_up_to_SA1.py
```

this script and the others in the directory are preconfigured to give
a reasonable final beam distribution.  For adjustment or refinement of
the model, please check the documentation.


## Repository structure
* src/euxfel - the main Python package for the Ocelot lattices and so on.
* beam_files - particle distributions
  * gun - initial beam distribution from gun (3.2 m position)
  * gun_2019 - initial beam distribution used in the settings https://www.desy.de/fel-beam/s2e/xfel/Nominal/nom250pC.html used for the 2019 simulation studies published in [this article](https://www.sciencedirect.com/science/article/abs/pii/S0168900221000954)
* Astra_gun_simulation/250pC_phi42 - by downloading the Astra executables from the official page https://www.desy.de/~mpyflo/ and adjusting the parameters in generator.in first (the laser pulse length sig_clock) and in the rfgun.in file later (phi(1)), it is possible to simulate the particle distribution from the gun till the position specified in the ZSTOP parameter. The current setting was developed by Igor Zagorodnov for 250pC. The radial_smear.m is a Matlab script for smoothing the profile obtain by the generator
* s2e_scripts - example scripts for running a start to end simulation from 3.2m to anywhere in the machine.
* tests - tests for the euxfel package.
* utils - beam matching script

## Citation 📚

If you use the s2e scripts from this repository or any of their derivatives in your work, please cite the following:
1. S. Tomin, I. Agapov, M. Dohlus, and I. Zagorodnov, Ocelot as a framework for beam dynamics simulations of x-ray sources,
in Proceedings of the International Particle Accelerator Conference (IPAC), Copenhagen, Denmark (2017), WEPAB031.
2. I. Zagorodnov, M. Dohlus, and S. Tomin, Accelerator beam dynamics at the European X-ray free-electron laser,
Phys. Rev. Accel. Beams 22, 024401 (2019). https://doi.org/10.1103/PhysRevAccelBeams.22.024401
