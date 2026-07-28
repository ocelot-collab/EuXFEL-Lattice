from __future__ import annotations

from collections.abc import Iterable, MutableSequence
from typing import Self, overload

import numpy as np
import polars as pl
from numpy.typing import NDArray

from .elements import Element


class Beamline(MutableSequence[Element]):
    def __init__(self, items: Iterable[Element]):
        self._sequence: list[Element] = list(items)

    @overload
    def __getitem__(self, key: int) -> Element: ...
    @overload
    def __getitem__(self, key: slice) -> Self: ...

    def __getitem__(self, key: int | slice) -> Element | Self:
        if isinstance(key, int):
            return self._sequence[key]
        elif isinstance(key, slice):
            return type(self)(self._sequence[key])

    @overload
    def __setitem__(self, key: int, value: Element) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Iterable[Element]) -> None: ...

    def __setitem__(self, key: int | slice, value) -> None:
        self._sequence[key] = value

    def __delitem__(self, key: int | slice) -> None:
        del self._sequence[key]

    def __len__(self) -> int:
        return len(self._sequence)

    def insert(self, index: int, value: Element) -> None:
        self._sequence.insert(index, value)

    def survey(self) -> pl.DataFrame:
        initial_offset: NDArray[np.float64] = np.array([0.0, 0.0, 0.0]).reshape(3, 1)
        initial_rotation: NDArray[np.float64] = np.identity(3)

        global_rotations: list[NDArray[np.float64]] = [initial_rotation]
        global_placements: list[NDArray[np.float64]] = [initial_offset]

        for element in self:
            local_displacement: NDArray[np.float64] = element.displacement()
            local_rotation: NDArray[np.float64] = element.rotation()

            previous_rotation = global_rotations[-1]
            previous_placement = global_placements[-1]

            global_placement = (
                previous_rotation @ local_displacement + previous_placement
            )
            global_rotation = previous_rotation @ local_rotation

            global_placements.append(global_placement)
            global_rotations.append(global_rotation)

        global_placements_arr: NDArray[np.float64] = np.hstack(global_placements)
        coords: NDArray[np.float64] = global_placements_arr[..., 1:]
        x = coords[0]
        y = coords[1]
        z = coords[2]

        active = [elem.is_active() for elem in self]
        length = [elem.length for elem in self]

        theta, _, _ = rotation_matrices_to_madx_rotations(global_rotations[1:])
        xlocal, ylocal, zlocal = rotation_matrices_to_local_axis(global_rotations[1:])

        df = pl.from_dict(
            {
                "name": self.name(),
                "keyword": self.keyword(),
                "x": x,
                "y": y,
                "z": z,
                "xlocal": xlocal,
                "ylocal": ylocal,
                "zlocal": zlocal,
                "s": list(self.s()),
                "theta": theta,
                "length": length,
                "active": active,
                "k1": self._get_attr_or_zero("k1"),
                "angle": self._get_attr_or_zero("angle"),
            }
        )

        return df

    def _get_attr_or_zero(self, attr_name: str) -> list[str] | list[float] | list[bool]:
        result = []
        for x in self:
            try:
                result.append(getattr(x, attr_name))
            except AttributeError:
                result.append(0.0)
        return result

    def keyword(self) -> list[str]:
        return [type(element).__name__ for element in self]

    def name(self) -> list[str]:
        return [element.name for element in self]

    def s(self) -> np.ndarray:
        return np.cumsum([element.length for element in self])


def rotation_matrices_to_madx_rotations(
    matrices: list[np.ndarray],
) -> tuple[list[float], list[float], list[float]]:
    thetas = []
    unit_z = [0, 0, 1]
    # import ipdb; ipdb.set_trace()
    for matrix in matrices:
        # New direction, starting from pointing along global z:
        # vec = matrix @ unit_z
        new_z = matrix[:, 2]
        # Project the new z onto the x-z plane
        new_z[1] = 0.0

        theta = np.arccos(np.dot(unit_z, new_z) / np.linalg.norm(new_z))
        thetas.append(theta)

    return thetas, [], []


def rotation_matrices_to_local_axis(
    matrices: Iterable[np.ndarray],
) -> tuple[list[np.ndarray], list[np.ndarray], list[np.ndarray]]:
    x = []
    y = []
    z = []
    for matrix in matrices:
        # Third column is new z axis (i.e. comoving s)
        new_x = matrix[:, 0]
        new_y = matrix[:, 1]
        new_z = matrix[:, 2]

        x.append(new_x)
        y.append(new_y)
        z.append(new_z)

    return x, y, z
