
### Optics in Plain Python

You can of course use the euxfel package in Python as a normal library, for example to access the sequence from the cathode to I1D in Python:

```python
import euxfel.sequences as sequences
from ocelot import *
from ocelot.gui.accelerator import *
import matplotlib.pyplot as plt
twiss0 = sequences.CATHODE_TWISS0
mlat_i1d = MagneticLattice(sequences.cathode_to_i1d)
machine_twiss = twiss(mlat_i1d, twiss0)
# Example of use with plain OCELOT:
plot_opt_func(mlat_i1d, machine_twiss)
plt.show()
```
In addition to `sequences.cathode_to_i1d`, there is also a `squences.cathode_to_` attribute for `b1d`, `b2d`, `tld`, `t4d` and `t5d`.

