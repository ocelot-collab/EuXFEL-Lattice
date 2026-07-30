"""Kicker elements, which Ocelot has no distinct type for.

The machine has three families of kicker, doing quite different jobs, and
`makelist_release.m:447-478` already names them: `FASTKICK`, `RAMPKICK` and
`FBKICK`.  Modelling all of them as plain `RBend` -- which is what the
component-list converter does -- loses that distinction entirely, and with it
the horizontal/vertical split, since `dispatch` keys on `GROUP` and never reaches
the `HKIC -> Hcor` / `VKIC -> Vcor` branch.

| class | count | types |
|---|---|---|
| `HFastKicker` / `VFastKicker` | 30 / 14 | `KAX KAY KDY KL KSPOS KSNEG` |
| `HRampKicker` / `VRampKicker` | 6 / 5 | `KIX KIY KJX KJY KMX KNY` |
| `HFeedbackKicker` / `VFeedbackKicker` | 2 / 2 | `KFBX KFBY`, the IBFB pair |

**The plane is in the class name, not in a tilt.**  Where the source carries a
tilt it is passed through untouched (`KNY` and `KL.1998`-`KL.2003.TL` really are
`pi/2` in MAD-8); where the source encodes the plane in the type instead
(`HKICKER`/`VKICKER`, `HKIC`/`VKIC`) no tilt is invented.  Synthesising `pi/2` on
import only to strip it again on export would be churn that cancels out.

The consequence, deliberately accepted: these classes *record* the plane, they do
not *enforce* it in tracking.  Every kicker in the design lattice has zero
strength, so nothing is wrong today -- but whoever sets a vertical kick has to
apply the tilt themselves.

They subclass `RBend` because that is how a kicker deflects, and because Ocelot
is a pinned dependency this repository does not modify -- the same reasoning as
`rotations.py` and `slicing.py`.
"""

from ocelot.cpbd.elements import RBend

#: Component-list `GROUP` for each family, which is also how the longlist route
#: identifies them.  The tape route has no GROUP column and uses the name-stem
#: table in the conversion config instead.
GROUPS: dict[str, str] = {
    "FastKicker": "FASTKICK",
    "RampKicker": "RAMPKICK",
    "FeedbackKicker": "FBKICK",
}


class _Kicker(RBend):
    """A kicker.  Deflects like a bend; named for what it is for.

    Every parameter is defaulted because `writer.element_to_string` calls
    `cls()` to work out which arguments differ from the default and so need
    writing.
    """

    #: Which plane this class deflects in.  `None` on the base.
    plane: str | None = None

    def __init__(
        self,
        l: float = 0.0,  # noqa: E741 -- Ocelot's own parameter name
        angle: float = 0.0,
        e1: float = 0.0,
        e2: float = 0.0,
        tilt: float = 0.0,
        eid: str | None = None,
    ):
        super().__init__(l=l, angle=angle, e1=e1, e2=e2, tilt=tilt, eid=eid)

    def __repr__(self) -> str:
        return f"<{type(self).__name__}: name={self.id} l={self.l}>"


class HFastKicker(_Kicker):
    """Horizontal fast kicker: `KAX`, `KSPOS`, `KSNEG`, the untilted `KL`s."""

    plane = "H"


class VFastKicker(_Kicker):
    """Vertical fast kicker: `KAY`, `KDY`, `KL.1998`-`KL.2003.TL`."""

    plane = "V"


class HRampKicker(_Kicker):
    """Horizontal ramped kicker: `KIX`, `KJX`, `KMX`, and `KL.2005.TL`."""

    plane = "H"


class VRampKicker(_Kicker):
    """Vertical ramped kicker: `KIY`, `KJY`, `KNY`."""

    plane = "V"


class HFeedbackKicker(_Kicker):
    """Horizontal intra-bunch-train feedback kicker: `KFBX`, 2.0 m."""

    plane = "H"


class VFeedbackKicker(_Kicker):
    """Vertical intra-bunch-train feedback kicker: `KFBY`, 2.0 m."""

    plane = "V"


#: Every kicker class, by family and plane.  `mad8_import` looks a family up from
#: the name-stem table in the conversion config, then picks the plane from the
#: MAD-8 keyword (`HKIC`/`VKIC`) or, for `RBEN`, from the tilt.
BY_FAMILY_AND_PLANE: dict[tuple[str, str], type[_Kicker]] = {
    ("FastKicker", "H"): HFastKicker,
    ("FastKicker", "V"): VFastKicker,
    ("RampKicker", "H"): HRampKicker,
    ("RampKicker", "V"): VRampKicker,
    ("FeedbackKicker", "H"): HFeedbackKicker,
    ("FeedbackKicker", "V"): VFeedbackKicker,
}

CLASSES: tuple[type[_Kicker], ...] = tuple(BY_FAMILY_AND_PLANE.values())
