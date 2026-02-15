from . import plot, subsequences

try:
    from .sequences import (
        CATHODE_TWISS0,
        cathode_to_b1d,
        cathode_to_b2d,
        cathode_to_i1d,
        cathode_to_t4d,
        cathode_to_t5d,
        cathode_to_tld,
    )
except Exception:
    # Then probably the conversion failed and the sequences are missing
    import warnings

    warnings.warn(
        "Failed importing subsequence modules, so one or more modules will be missing."
        "  Consider regenerating one or more of these files to correct this."
    )
    del warnings
    __all__ = ["plot", "subsequences"]
else:
    __all__ = [
        "cathode_to_i1d",
        "cathode_to_b1d",
        "cathode_to_b2d",
        "cathode_to_tld",
        "cathode_to_t4d",
        "cathode_to_t5d",
        "CATHODE_TWISS0",
        "plot",
        "subsequences",
    ]
