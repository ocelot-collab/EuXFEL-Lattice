from ocelot.cpbd.magnetic_lattice import flatten as _flatten

from . import plot, subsequences
from .beamline import (
    AmbiguousKeyError,
    Beamline,
    GangedMagnetError,
    Group,
    KnobOwnedError,
    UnknownKeyError,
    all_machine_elements,
    design_optics,
    set_design_optics,
)
from .kicks import KickError, design_kick, read_kick, stamp_design_kicks, write_kick
from .machine import MATCHED_SECTIONS

# Record what the generated modules say, now, while they still say it.  Every
# design value in the package is read from these stamps, so this has to happen
# before anything can write to an element -- which here means before any user
# code runs at all.  It costs ~12 ms.
#
# The walk lives here rather than in `subsequences/__init__.py` because that
# file is a generated artefact; see CLAUDE.md.
stamp_design_kicks(
    element
    for name in getattr(subsequences, "__all__", ())
    for element in _flatten(getattr(subsequences, name).cell)
)

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
    "design_kick",
    "design_optics",
    "plot",
    "read_kick",
    "set_design_optics",
    "stamp_design_kicks",
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
