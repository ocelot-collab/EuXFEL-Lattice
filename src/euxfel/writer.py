import inspect
import subprocess
import sys
from collections import Counter, defaultdict
from math import isclose
from numbers import Number
from typing import Any

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import RBend
from ocelot.cpbd.elements.optic_element import OpticElement

from euxfel import metadata

DEFAULT_ELEMENT_ORDER = [
    "Drift",
    "Quadrupole",
    "SBend",
    "RBend",
    "Bend",
    "Sextupole",
    "Octupole",
    "Multipole",
    "Hcor",
    "Vcor",
    "Undulator",
    "Cavity",
    "TDCavity",
    "Solenoid",
    "Monitor",
    "Marker",
    "Matrix",
    "Aperture",
    "SlicedElement",
    "SRot",
    "YRot",
    "HFastKicker",
    "VFastKicker",
    "HRampKicker",
    "VRampKicker",
    "HFeedbackKicker",
    "VFeedbackKicker",
]

# Elements this repository defines because Ocelot has no equivalent.  They are
# written the same way as any other element, but imported from here.
EUXFEL_ELEMENT_MODULES = {
    "SRot": "euxfel.rotations",
    "YRot": "euxfel.rotations",
    "HFastKicker": "euxfel.kickers",
    "VFastKicker": "euxfel.kickers",
    "HRampKicker": "euxfel.kickers",
    "VRampKicker": "euxfel.kickers",
    "HFeedbackKicker": "euxfel.kickers",
    "VFeedbackKicker": "euxfel.kickers",
}


class PythonSubsequenceWriter:
    PARAMETER_NAME_TO_ATTRIBUTE_DICT = {"eid": "id"}
    SKIPPABLE_PARAMETERS = set(["tm"])  # I just don't write these for some reason
    NAMES_TO_VARIABLES_MAP = {":": "_", ".": "_", "-": "_", "'": "_"}
    BEAM_PARAMETERS_TO_WRITE = [
        "E",
        "alpha_x",
        "alpha_y",
        "beta_x",
        "beta_y",
        "Dx",
        "Dxp",
        "Dy",
        "Dyp",
        "s",
    ]
    ABS_TOL_FOR_DEFAULT_BEAM_PARAMETERS = 1e-6
    # REL_TOL_FOR_DEFAULT_BEAM_PARAMETERS = 1e-

    def __init__(self, sequence: list[OpticElement], twiss0: Twiss):
        self.sequence = sequence
        self.twiss0 = twiss0

    def twiss_to_string(self):
        """Generates a string, in a python readable format, that
        contains the Twiss parameter to store it in a python file.
        :param twiss: Input twiss :return: A string that contains
        Twiss parameter in a python readable format

        """
        lines = []
        twiss_ref = Twiss()
        lines.append("twiss0 = Twiss()\n")
        twiss = self.twiss0
        for name in self.BEAM_PARAMETERS_TO_WRITE:
            value = getattr(twiss, name)  # Just to check that it doesn't raise an error
            ref_value = getattr(twiss_ref, name)
            # If it's the default value or close to it in absolute
            # terms (the defaults I know are always 0.0 for Twiss
            # instances).  This is to avoid specious dispersion values
            # being written out on the order of a few 10s of
            # nanometres, for example.
            if isclose(
                value, ref_value, abs_tol=self.ABS_TOL_FOR_DEFAULT_BEAM_PARAMETERS
            ):
                continue

            lines.append(f"twiss0.{name} = {value}\n")

        return "".join(lines)

    def element_to_string(self, element, variable_name) -> str:
        cls = type(element)

        cls_name = cls.__name__
        name_lower = cls_name.lower()
        specific_method_name = f"{name_lower}_to_string"

        # Check if we have special converter for this element type,
        # which we would use instead.
        if hasattr(self, specific_method_name) and name_lower != element:
            return getattr(self, specific_method_name)(element, variable_name)

        parameters = get_obj_init_parameters(element)

        set_params = []
        default_element = cls()
        # Loop over the __init__'s args and kwargs, and if they differ
        # from the default value, then set them.
        for parameter in parameters:
            if parameter in self.SKIPPABLE_PARAMETERS:
                continue

            if self.is_default_value(element, parameter, default_obj=default_element):
                continue

            if parameter == "eid":
                value = element.id
            else:
                value = getattr(element, parameter)

            set_params.append(self.handle_strings_and_numbers(parameter, value))

        return f"{variable_name} = {cls_name}({', '.join(set_params)})"

    def make_element_class_names_to_instances_map(self):
        elements_by_type = defaultdict(list)
        for element in self.sequence:
            elements_by_type[type(element).__name__].append(element)
        return elements_by_type

    def elements_to_string(self, element_order=None, variable_names=None) -> str:
        element_order = element_order or DEFAULT_ELEMENT_ORDER

        elements_by_type = self.make_element_class_names_to_instances_map()

        if variable_names is None:
            variable_names = self.make_var_names(self.sequence)
        lines = []
        for element_type_name in element_order:
            elements_of_this_type = elements_by_type[element_type_name]
            if not elements_of_this_type:
                continue
            lines.append(f"\n# {element_type_name}s:")
            for element in elements_of_this_type:
                lines.append(self.element_to_string(element, variable_names[element]))

        # ruff format would otherwise wrap the longest element definitions over
        # several lines.  Bracket the block so the one-element-per-line layout
        # emitted here survives every ruff invocation: write_module's own,
        # `tox -e format`, and editors-on-save.  Anything added to to_module
        # between here and sequence_to_string would land inside the region.
        # lstrip: the first section header carries a leading newline as a
        # separator; drop it so the blank lines before `# fmt: off` stay
        # outside the region, where ruff still caps them at two.
        body = "\n".join(lines).lstrip("\n")
        return f"# fmt: off\n{body}\n# fmt: on"

    def slicedelement_to_string(self, element, variable_name):
        lines = []
        for slice_name, slice_element in element.elements.items():
            lines.append(self.element_to_string(slice_element, slice_name))

        lines.append(f"{variable_name} = {element.expression}")
        return "\n".join(lines)

    def sequence_to_string(self, variable_names=None) -> str:
        if variable_names is None:
            variable_names = self.make_var_names(self.sequence)
        ordered_var_names = [variable_names[element] for element in self.sequence]
        return f"# Sequence:\ncell = ({',\n        '.join(ordered_var_names)})"

    def make_var_names(self, elements: list[OpticElement]) -> dict[OpticElement, str]:
        """A unique Python variable name for each distinct element object.

        Keyed by object identity, not by `id`: two elements may legitimately
        share a name.  MAD-8 reuses names heavily -- `D0100` occurs hundreds of
        times in a single path -- and Ocelot requires the *objects* to be
        distinct, because `navi._find_unique_index` matches physics-process
        anchors with `is` and raises on a repeat.  So one object per placement,
        each needing its own variable.

        Iteration follows the sequence rather than a `set`, so the suffixes a
        repeated name picks up are stable between runs; a set's ordering is not,
        and the generated modules are committed and diffed.
        """
        variable_names: dict[int, str] = {}
        by_identity: dict[int, OpticElement] = {}
        used: Counter[str] = Counter()
        ttable = str.maketrans(self.NAMES_TO_VARIABLES_MAP)

        for element in elements:
            key = id(element)
            if key in variable_names:
                continue
            by_identity[key] = element

            name = element.id
            if not (name[0].isalpha() or name[0] == "_"):
                name = f"{type(element).__name__[0]}{name}"
            name = name.lower().translate(ttable)

            used[name] += 1
            if used[name] > 1:
                name = f"{name}_{used[name] - 1}"
            variable_names[key] = name

        return {by_identity[key]: name for key, name in variable_names.items()}

    def power_supplies_to_string(
        self,
        element_order: list[str] | None = None,
        variable_names: dict[OpticElement, str] = None,
        write_types_power_supplies: list[str] | None = None,
    ) -> str:

        element_order = element_order or DEFAULT_ELEMENT_ORDER
        elements_by_type = self.make_element_class_names_to_instances_map()
        # None means every type.  `ps_id` holds the component list's NAME2 for
        # every element, magnet or not, and writing the component list back out
        # needs all of them -- so restricting this to the magnet types would
        # discard data the reverse conversion depends on.
        if write_types_power_supplies is None:
            write_types_power_supplies = set(element_order)
        else:
            write_types_power_supplies = set(write_types_power_supplies)

        if variable_names is None:
            variable_names = self.make_var_names(self.sequence)
        lines = []
        for element_type_name in element_order:
            if element_type_name not in write_types_power_supplies:
                continue
            elements_of_this_type = elements_by_type[element_type_name]
            elements_with_ps_ids = [
                e for e in elements_of_this_type if hasattr(e, "ps_id")
            ]
            if elements_with_ps_ids:
                lines.append(f"\n# {element_type_name} power supplies:")

            for element in elements_with_ps_ids:
                variable_name = variable_names[element]
                lines.append(f'{variable_name}.ps_id = "{element.ps_id}"')

        return f"# Power Supply IDs:{'\n'.join(lines)}"

    def metadata_to_string(
        self,
        element_order: list[str] | None = None,
        variable_names: dict[OpticElement, str] = None,
    ) -> str:
        """Write each element's component-list bookkeeping.

        See `euxfel.metadata` for what these fields are and why they are stored
        rather than derived.  Elements inserted by the conversion config rather
        than read from the component list have none, and are skipped.
        """
        element_order = element_order or DEFAULT_ELEMENT_ORDER
        elements_by_type = self.make_element_class_names_to_instances_map()

        if variable_names is None:
            variable_names = self.make_var_names(self.sequence)

        lines = []
        for element_type_name in element_order:
            with_metadata = [
                element
                for element in elements_by_type[element_type_name]
                if metadata.of(element)
            ]
            if with_metadata:
                lines.append(f"\n# {element_type_name} metadata:")
            for element in with_metadata:
                fields = ", ".join(
                    f"{key!r}: {value!r}" for key, value in metadata.of(element).items()
                )
                lines.append(f"{variable_names[element]}.metadata = {{{fields}}}")

        # As in elements_to_string: without this ruff format would break every
        # dict over nine lines, which across the whole lattice is tens of
        # thousands of lines of nothing.
        body = "\n".join(lines).lstrip("\n")
        return f"# Component list metadata:\n# fmt: off\n{body}\n# fmt: on"

    def make_import_string(self) -> str:
        class_names = set(type(element).__name__ for element in self.sequence)
        # This is a special case, as it is written not as a SlicedElement at all,
        # And instead just as lists of elements multiplied by integers:
        class_names.discard("SlicedElement")

        # Elements we define ourselves come from euxfel, not ocelot.
        by_module = defaultdict(set)
        for name in class_names:
            by_module[EUXFEL_ELEMENT_MODULES.get(name, "ocelot.cpbd.elements")].add(
                name
            )

        lines = ["from ocelot.cpbd.beam import Twiss"]
        for module in sorted(by_module):
            names = ", ".join(sorted(by_module[module]))
            lines.append(f"from {module} import {names}")
        return "\n".join(lines)

    def write_module(
        self,
        fname: str,
        write_types_power_supplies: list[str] | None = None,
        comment: str = "",
    ):
        with open(fname, "w") as f:
            f.write(
                self.to_module(
                    write_types_power_supplies=write_types_power_supplies,
                    comment=comment,
                )
            )

        # Tidy and format what we have just written to file.
        subprocess.run(
            [sys.executable, "-m", "ruff", "check", "--select", "I", "--fix", fname],
            check=True,
            capture_output=True,
        )
        subprocess.run([sys.executable, "-m", "ruff", "format", fname], check=True)

    def to_module(
        self, write_types_power_supplies: list[str] | None = None, comment: str = ""
    ) -> str:
        variable_names = self.make_var_names(self.sequence)
        return (
            f"# {comment}\n\n"
            + self.make_import_string()
            + "\n\n"
            + self.twiss_to_string()
            + "\n\n"
            + self.elements_to_string(variable_names=variable_names)
            + "\n\n"
            + self.sequence_to_string(variable_names=variable_names)
            + "\n\n"
            + self.power_supplies_to_string(
                variable_names=variable_names,
                write_types_power_supplies=write_types_power_supplies,
            )
            + "\n\n"
            + self.metadata_to_string(variable_names=variable_names)
        )

    def rbend_to_string(self, element: RBend, variable_name: str) -> str:
        parameters = get_obj_init_parameters(element)
        set_params = []
        for parameter in parameters:
            if parameter in self.SKIPPABLE_PARAMETERS:
                continue

            if parameter == "eid":
                value = element.id
            else:
                value = getattr(element, parameter)

            if parameter in ("e1", "e2"):
                new_e1_e2 = value - element.angle / 2.0
                set_params.append(f"{parameter}={new_e1_e2}")
                continue
            elif self.is_default_value(element, parameter, default_obj=RBend()):
                continue

            set_params.append(self.handle_strings_and_numbers(parameter, value))
        return f"{variable_name} = {type(element).__name__}({', '.join(set_params)})"

    def handle_strings_and_numbers(self, parameter: str, value: Number | str) -> str:
        if isinstance(value, Number):
            return f"{parameter}={value}"
        elif isinstance(value, str):
            return f'{parameter}="{value}"'
        else:
            raise ValueError(parameter)

    def is_default_value(self, object: Any, parameter: str, default_obj=None) -> bool:
        if default_obj is None:
            default_obj = type(object)()
        attribute_name = self.PARAMETER_NAME_TO_ATTRIBUTE_DICT.get(parameter, parameter)
        return getattr(object, attribute_name) == getattr(default_obj, attribute_name)


def check_eid_id(object, default_obj=None):
    if default_obj is None:
        default_obj = type(object)()


def get_obj_init_parameters(obj) -> list[str]:
    if init_has_kwargs(type(obj)):
        return type(obj).__init__.__code__.co_varnames[1:-1]  # Skip self and kwargs
    return type(obj).__init__.__code__.co_varnames[1:]  # Skip self


def init_has_kwargs(cls):
    return any(
        p.kind is inspect.Parameter.VAR_KEYWORD
        for p in inspect.signature(cls.__init__).parameters.values()
    )


class ComponentListWriter:
    pass
