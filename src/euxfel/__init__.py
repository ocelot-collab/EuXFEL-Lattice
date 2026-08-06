from . import plot, subsequences
from .beamline import (
    AmbiguousKeyError,
    Beamline,
    GangedMagnetError,
    Group,
    KnobOwnedError,
    UnknownKeyError,
    all_machine_elements,
    clear_design_factors,
)
from .kicks import KickError, read_kick, write_kick
from .machine import MATCHED_SECTIONS

# The lattice model, which is here whether or not the generated subsequences
# imported: none of it depends on them, so it should not go missing with them.
__all__ = [
    "MATCHED_SECTIONS",
    "AmbiguousKeyError",
    "Beamline",
    "GangedMagnetError",
    "Group",
    "KickError",
    "KnobOwnedError",
    "UnknownKeyError",
    "all_machine_elements",
    "clear_design_factors",
    "plot",
    "read_kick",
    "subsequences",
    "write_kick",
]

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
else:
    __all__ += [
        "CATHODE_TWISS0",
        "cathode_to_b1d",
        "cathode_to_b2d",
        "cathode_to_i1d",
        "cathode_to_t4d",
        "cathode_to_t5d",
        "cathode_to_tld",
    ]
