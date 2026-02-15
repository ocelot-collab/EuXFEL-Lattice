import ast
import operator

from ocelot.cpbd.elements.element import Element
from ocelot.cpbd.elements.optic_element import OpticElement

ALLOWED_BINOPS = {
    ast.Add: operator.add,
    ast.Mult: operator.mul,
}

ALLOWED_NODES = (
    ast.Expression,
    ast.BinOp,
    ast.Constant,
    ast.Name,
    ast.List,
    ast.Tuple,
)


def eval_slice_expr(expr: str, env: dict):
    """
    Evaluate an expression like '19 * x + 10 * y' where
    x, y are in env. Supports only +, *, ints, strs, and names.
    """
    node = ast.parse(expr, mode="eval")

    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)

        if not isinstance(n, ALLOWED_NODES):
            raise ValueError(f"Disallowed syntax: {type(n).__name__}")

        if isinstance(n, ast.BinOp):
            op_type = type(n.op)
            if op_type not in ALLOWED_BINOPS:
                raise ValueError(f"Operator {op_type.__name__} not allowed")
            left = _eval(n.left)
            right = _eval(n.right)
            return ALLOWED_BINOPS[op_type](left, right)

        if isinstance(n, ast.List):
            return [_eval(elt) for elt in n.elts]

        if isinstance(n, ast.Tuple):
            return tuple(_eval(elt) for elt in n.elts)

        if isinstance(n, ast.Constant):
            # allow ints and strings only
            if isinstance(n.value, (int, str)):
                return n.value
            raise ValueError(f"Constant type {type(n.value)} not allowed")

        if isinstance(n, ast.Name):
            if n.id not in env:
                raise NameError(f"Unknown variable {n.id!r}")
            return env[n.id]

        # You can add more allowed nodes here if needed
        raise ValueError(f"Disallowed expression node: {type(n).__name__}")

    return _eval(node)


class SlicedElement:
    def __init__(
        self, elements: dict[str, Element | OpticElement], expression: str, eid=None
    ):
        self.elements = elements
        self.expression = expression
        self.id = eid

    def expand(self):
        return eval_slice_expr(self.expression, self.elements)

    @property
    def l(self):  # noqa: E743
        return sum(e.l for e in self.expand())

    def __iter__(self):
        return iter(self.expand())
