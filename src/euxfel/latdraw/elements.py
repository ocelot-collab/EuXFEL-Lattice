import numpy as np


class Element:
    def __init__(self, name: str, length, **misc: object) -> None:
        self.name = name
        self.length = length
        self.misc = misc

    def __repr__(self) -> str:
        typename = type(self).__name__
        rstr = f"<{typename}: name={self.name}, l={self.length}"
        if self.misc:
            rstr += ", " + repr(self.misc)
        rstr += ">"
        return rstr

    def __str__(self) -> str:
        return f"{type(self).__name__}: {self.name}"

    def is_active(self) -> bool:
        return True

    def displacement(self) -> np.ndarray:
        return np.array([0, 0, self.length]).reshape(3, 1)

    def rotation(self) -> np.ndarray:
        return np.identity(3)


class ThinElement(Element):
    def __init__(self, name: str, **misc: object):
        super().__init__(name, 0.0, **misc)

    def __repr__(self) -> str:
        typename = type(self).__name__
        return f"<{typename}: name={self.name}>"


class Marker(ThinElement):
    pass


class Monitor(ThinElement):
    pass


class Drift(Element):
    pass


class Dipole(Element):
    def __init__(self, name: str, length: float, angle: float, **misc: object):
        super().__init__(name, length, **misc)
        self.angle = angle

    def is_active(self) -> bool:
        return self.angle != 0

    @property
    def rho(self) -> float:
        return self.length / self.angle

    def displacement(self) -> np.ndarray:
        if self.angle == 0:
            res = np.array([0, 0, self.length])
        else:
            res = np.array(
                [self.rho * (np.cos(self.angle) - 1), 0, self.rho * np.sin(self.angle)]
            )

        return res.reshape(3, 1)

    def rotation(self) -> np.ndarray:
        return np.array(
            [
                [np.cos(self.angle), 0, -np.sin(self.angle)],
                [0, 1, 0],
                [np.sin(self.angle), 0, np.cos(self.angle)],
            ]
        )

    def __repr__(self) -> str:
        typename = type(self).__name__
        return f"<{typename}: name={self.name}, l={self.length}, angle={self.angle}>"


class RBend(Dipole):
    pass


class SBend(Dipole):
    pass


class HKicker(Dipole):
    pass


class VKicker(Dipole):
    pass


class Kicker(Dipole):
    pass


class Quadrupole(Element):
    def __init__(self, name: str, length: float, k1: float, **misc: object):
        super().__init__(name, length, **misc)
        self.k1 = k1

    def is_active(self) -> bool:
        return self.k1 != 0

    def __str__(self) -> str:
        k1 = self.k1
        k1l = self.length * k1
        return f"<Quad: {self.name}, l={self.length}, {k1=}, {k1l=}>"

    def polarity(self) -> int:
        return np.sign(self.k1)


class Sextupole(Element):
    def __init__(self, name: str, length: float, k2: float, **misc: object):
        super().__init__(name, length, **misc)
        self.k2 = k2

    def is_active(self) -> bool:
        return self.k2 != 0


class Octupole(Element):
    def __init__(self, name: str, length: float, k3: float, **misc: object):
        super().__init__(name, length, **misc)
        self.k3 = k3

    def is_active(self) -> bool:
        return self.k3 != 0


class RFCavity(Element):
    def __init__(
        self, name: str, length: float, voltage: float, phase: float, **misc: object
    ):
        super().__init__(name, length, **misc)
        self.voltage = voltage
        self.phase = phase

    def is_active(self) -> bool:
        return self.voltage != 0


class Solenoid(Element):
    def __init__(self, name: str, length: float, ks: float, **misc: object):
        super().__init__(name, length, **misc)
        self.ks = ks

    def is_active(self) -> bool:
        return self.ks != 0


class Collimator(Element):
    pass


class Cavity(Element):
    pass


class GenericMap(Element):
    pass


class TransverseDeflectingCavity(Element):
    def __init__(self, name: str, length: float, voltage: float, **misc: object):
        super().__init__(name, length, **misc)
        self.voltage = voltage

    def is_active(self) -> bool:
        return self.voltage != 0


class Undulator(Element):
    def __init__(self, name: str, length, kx=0.0, ky=0.0, **misc: object):
        super().__init__(name, length, **misc)
        self.kx = kx
        self.ky = ky

    def is_active(self) -> bool:
        return self.kx != 0 or self.ky != 0
