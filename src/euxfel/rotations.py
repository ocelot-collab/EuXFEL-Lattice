"""Zero-length coordinate rotations, as MAD-8's `SROT` and `YROT`.

MAD-8's lattice for the SASE2 branch applies frame rotations that never reach
the component list.  `Run_South_2025.txm:299-322` defines

    az1 = -0.00440392786446921;  ay = +9.27121409529346e-08;
    az2 = +0.00441369699554469;
    RotSystemTD1: Line = (Rot.Z1.T1, Rot.Y.T1, Rot.Z2.T1);
    T1_survey: Line = (RotSystemTD1, T1M, T1D, ENSEC.T1.T1);

used by the *survey* line only, never by the Twiss line.  They patch the design
geometry onto the as-built XTD1 tunnel -- the roll-pitch-roll sandwich is the
usual way to pitch about an axis that is not the local vertical, and because
`az1 != -az2` a residual roll of `az1 + az2 = +9.769e-06` is left behind on
purpose.  `makelist_release.m:56` discards every row whose name begins `ROT`,
so the spreadsheet has no record of them and `euxfel convert` cannot know they
exist.  Without them our SASE2 branch is rolled by 9.769 urad and the T5D dump
lands 2.3 mm out.

Ocelot has no such element and is a pinned dependency we do not modify, so they
live here, following the precedent of `slicing.py`.

Both subclass `Marker`, whose transfer map is the identity: these change where
the beamline points, not what happens to the beam.  Ocelot's survey works
entirely through `get_transfer_geometry`, so overriding that is enough
(`MagneticLattice.survey`, `magnetic_lattice.py:377`).
"""

import numpy as np
from ocelot.cpbd.elements import Marker


class _Rotation(Marker):
    """A zero-length rotation of the reference frame.

    Subclasses supply `rotation_matrix`, which gives the orientation of the
    local frame at the exit relative to the entrance.
    """

    def __init__(self, angle: float = 0.0, eid: str | None = None):
        super().__init__(eid=eid)
        self.angle = angle

    def rotation_matrix(self) -> np.ndarray:
        raise NotImplementedError

    def get_transfer_geometry(self):
        rotation = self.rotation_matrix()
        no_displacement = np.zeros(3)
        # Zero length, so the midpoint and the exit are the same place and the
        # rotation is applied in full at both.
        return no_displacement, rotation, no_displacement.copy(), rotation.copy()

    def __repr__(self) -> str:
        return f"<{type(self).__name__}: name={self.id} angle={self.angle}>"


class SRot(_Rotation):
    """A roll about the longitudinal axis, MAD-8's `SROT`.

    Adds its angle to the survey roll `PSI` (`CHI` in component-list
    convention), which the MAD-8 tapes confirm directly: at `SURVEY_T5D` index
    6768 `PSI` is -7.479365479e-06, and after `ROT.Z1.T1` (angle
    -4.40392786446921e-03) it is -4.411407230e-03, the exact sum.
    """

    def rotation_matrix(self) -> np.ndarray:
        # MAD-8 Eq. 9.7, the same convention Ocelot seeds `psi0` with.
        cos, sin = np.cos(self.angle), np.sin(self.angle)
        return np.array([[cos, -sin, 0.0], [sin, cos, 0.0], [0.0, 0.0, 1.0]])


class YRot(_Rotation):
    """A rotation about the vertical axis, MAD-8's `YROT`.

    Changes the azimuth `THETA`.  Note the sign: a positive `YROT` angle
    *decreases* `THETA` in the convention Ocelot's survey uses, which is the
    opposite of its `theta0` seed matrix (`magnetic_lattice.py:395`).  Measured
    against the tape rather than assumed -- taking the seed's sense left
    `THETA` wrong by 2*ay after `ROT.Y.T1`.
    """

    def rotation_matrix(self) -> np.ndarray:
        cos, sin = np.cos(self.angle), np.sin(self.angle)
        return np.array([[cos, 0.0, -sin], [0.0, 1.0, 0.0], [sin, 0.0, cos]])
