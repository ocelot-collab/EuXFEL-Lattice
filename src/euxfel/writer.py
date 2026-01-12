import inspect
from collections import defaultdict
from itertools import groupby
from numbers import Number
from typing import Any

from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.elements import Drift, RBend
from ocelot.cpbd.elements.optic_element import OpticElement

DEFAULT_ELEMENT_ORDER = ["Drift",
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
                         "SlicedElement"]



class PythonSubsequenceWriter:
    PARAMETER_NAME_TO_ATTRIBUTE_DICT = {"eid": "id"}
    SKIPPABLE_PARAMETERS = set(["tm"])  # I just don't write these for some reason
    NAMES_TO_VARIABLES_MAP = {":": "_", ".": "_", "-": "_", "'": "_"}
    def __init__(self, sequence: list[OpticElement], twiss0: Twiss):
        self.sequence = sequence
        self.twiss0 = twiss0

    def twiss_to_string(self):
        """
        Generates a string, in a python readable format, that contains the Twiss parameter to store it in a python file.
        :param twiss: Input twiss
        :return: A string that contains Twiss parameter in a python readable format
        """
        lines = []
        twiss_ref = Twiss()
        lines.append('twiss0 = Twiss()\n')
        twiss = self.twiss0
        for param in twiss.__dict__:
            if twiss.__dict__[param] != twiss_ref.__dict__[param]:
                lines.append('twiss0.' + str(param) + ' = ' + str(twiss.__dict__[param]) + '\n')
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

        return f"{variable_name} = {cls_name}({", ".join(set_params)})"


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

        return "\n".join(lines)

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
        return f"# Sequence:\ncell = ({",\n        ".join(ordered_var_names)})"

    def make_var_names(self, elements: list[OpticElement]) -> dict[OpticElement, str]:
        # Remove duplicate elements in the sequence (i.e. literal
        # shared memory addresses) to avoid
        elements = set(elements)
        variable_names = {}
        ttable = str.maketrans(self.NAMES_TO_VARIABLES_MAP)
        for element in elements:
            name = element.id
            if not (name[0].isalpha() or name[0] == "_"):
                name = f"{type(element).__name__[0]}{name}"
            name = name.lower().translate(ttable)
            if name in variable_names:
                iduplicate = variable_names.count(name)
                name = f"{name}_{iduplicate}"

            variable_names[element] = name
        return variable_names

    def power_supplies_to_string(self,
                                 element_order: list[str] | None = None,
                                 variable_names: dict[OpticElement, str] = None,
                                 write_types_power_supplies: list[str] | None = None) -> str:

        element_order = element_order or DEFAULT_ELEMENT_ORDER
        elements_by_type = self.make_element_class_names_to_instances_map()
        write_types_power_supplies = set(write_types_power_supplies) or set()

        if variable_names is None:
            variable_names = self.make_var_names(self.sequence)
        lines = []
        for element_type_name in element_order:
            if element_type_name not in write_types_power_supplies:
                continue
            elements_of_this_type = elements_by_type[element_type_name]
            elements_with_ps_ids = [e for e in elements_of_this_type if hasattr(e, "ps_id")]
            if elements_with_ps_ids:
                lines.append(f"\n# {element_type_name} power supplies:")

            for element in elements_with_ps_ids:
                variable_name = variable_names[element]
                lines.append(f'{variable_name}.ps_id = "{element.ps_id}"')

        return f"# Power Supply IDs:{"\n".join(lines)}"

    def make_import_string(self) -> str:
        lines = ["from ocelot.cpbd.elements import *",
                 "from ocelot.cpbd.beam import Twiss"]
        return "\n".join(lines)

    def to_module(self, write_types_power_supplies: list[str] | None = None, comment: str = "") -> str:
        variable_names = self.make_var_names(self.sequence)
        return (f"# {comment}\n\n"
                + self.make_import_string()
                + "\n\n"
                + self.twiss_to_string()
                + "\n\n"
                + self.elements_to_string(variable_names=variable_names)
                + "\n\n"
                + self.sequence_to_string(variable_names=variable_names)
                + "\n\n"
                + self.power_supplies_to_string(variable_names=variable_names,
                                                write_types_power_supplies=write_types_power_supplies))

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

            if parameter in ('e1', 'e2'):
                new_e1_e2 = value - element.angle / 2.0
                set_params.append(f"{parameter}={new_e1_e2}")
                continue
            elif self.is_default_value(element, parameter, default_obj=RBend()):
                continue

            set_params.append(self.handle_strings_and_numbers(parameter, value))
        return f"{variable_name} = {type(element).__name__}({", ".join(set_params)})"

    def handle_strings_and_numbers(self, parameter: str, value: Number | str) -> str:
        if isinstance(value, Number):
            return f"{parameter}={value}"
        elif isinstance(value, str):
            return f"{parameter}=\"{value}\""
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
        return type(obj).__init__.__code__.co_varnames[1:-1] # Skip self and kwargs
    return type(obj).__init__.__code__.co_varnames[1:] # Skip self

def init_has_kwargs(cls):
    return any(
        p.kind is inspect.Parameter.VAR_KEYWORD
        for p in inspect.signature(cls.__init__).parameters.values()
    )

class ComponentListWriter:
    pass
