# Automatically generated __init__.py from component_list_2024.07.04.xls
from importlib.resources import files

try:
    from . import i1
    from . import i1d
    from . import l1
    from . import b1d
    from . import l2
    from . import b2d
    from . import l3
    from . import cl
    from . import tl2tld
    from . import tl2
    from . import tl34_sa2
    from . import t1
    from . import sase2
    from . import t3
    from . import t5
    from . import t5d
    from . import tl34
    from . import sase1
    from . import t4
    from . import sase3
    from . import t4d


    __all__ = ["i1",
               "i1d",
               "l1",
               "b1d",
               "l2",
               "b2d",
               "l3",
               "cl",
               "tl2tld",
               "tl2",
               "tl34_sa2",
               "t1",
               "sase2",
               "t3",
               "t5",
               "t5d",
               "tl34",
               "sase1",
               "t4",
               "sase3",
               "t4d"]
except Exception:
    import warnings
    warnings.warn("Failed importing subsequence modules, so one or more modules will be missing.  Consider regenerating one or more of these files to correct this.")
    del warnings

# The longlist file we used to generate the subsequences in this directory:
USED_COMPONENT_LIST = files("euxfel.longlists") / "component_list_2024.07.04.xls"
