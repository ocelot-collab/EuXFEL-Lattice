from ocelot.cpbd.magnetic_lattice import flatten

from . import subsequences

CATHODE_TWISS0 = subsequences.i1.twiss0

TARGET_NAMES = ["I1D", "B1D", "B2D", "TLD", "T4D", "T5D"]

I1D_SUBSEQUENCES = ["i1", "i1d"]
B1D_SUBSEQUENCES = ["i1", "l1", "b1d"]
B2D_SUBSEQUENCES = ["i1", "l1",  "l2", "b2d"]
TLD_SUBSEQUENCES = ["i1", "l1", "l2", "l3", "cl", "tl2tld"]
T4D_SUBSEQUENCES = ["i1", "l1", "l2", "l3", "cl", "tl2", "tl34", "sase1", "t4", "sase3", "t4d"]
T5D_SUBSEQUENCES = ["i1", "l1", "l2", "l3", "cl", "tl2", "tl34_sa2", "t1", "sase2", "t3", "t5", "t5d"]

def _init_module_level_cells(module_names):
    return list(flatten((getattr(subsequences, mname).cell for mname in module_names)))

cathode_to_i1d = _init_module_level_cells(I1D_SUBSEQUENCES)
cathode_to_b1d = _init_module_level_cells(B1D_SUBSEQUENCES)
cathode_to_b2d = _init_module_level_cells(B2D_SUBSEQUENCES)
cathode_to_tld = _init_module_level_cells(TLD_SUBSEQUENCES)
cathode_to_t4d = _init_module_level_cells(T4D_SUBSEQUENCES)
cathode_to_t5d = _init_module_level_cells(T5D_SUBSEQUENCES)
