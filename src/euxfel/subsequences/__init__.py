# Automatically generated __init__.py from component_list_2026.01.21.xls
from importlib.resources import files

try:
    from . import (
        b1d,
        b2d,
        cl,
        i1,
        i1d,
        l1,
        l2,
        l3,
        sase1,
        sase2,
        sase3,
        t1,
        t3,
        t4,
        t4d,
        t5,
        t5d,
        tl2,
        tl2tld,
        tl34,
        tl34_sa2,
    )

    __all__ = [
        "i1",
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
        "t4d",
    ]
except Exception:
    import warnings

    warnings.warn(
        "Failed importing subsequence modules, so one or more modules will be missing.  Consider regenerating one or more of these files to correct this."
    )
    del warnings

# The longlist file we used to generate the subsequences in this directory:
USED_COMPONENT_LIST = files("euxfel.longlists") / "component_list_2026.01.21.xls"
