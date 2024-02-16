from typing import Any

from .visitor import Visitor
from ..ast import expression as EXPR


class DotVisitor(Visitor):
    def __init__(self):
        super().__init__()
        self.total = ""

    def output(self, filename: str):
        with open(filename, "w") as file:
            file.write("digraph ExpressionGraph {\n")
            file.write(self.total)
            file.write("}\n")

    def gen_binary_dot(self, me: EXPR.BinaryOperation, op_str: str) -> None:
        node_name = id(me)
        self.total += f"{node_name} [label=\"{op_str}\"];\n"
        left_node_name = id(me.left)
        right_node_name = id(me.right)
        self.total += f"{node_name} -> {left_node_name};\n"
        self.total += f"{node_name} -> {right_node_name};\n"
        self.visit_ast(me.left)
        self.visit_ast(me.right)

    def visit_binary_arithmetic(self, expr: EXPR.BinaryArithmetic) -> Any:
        self.gen_binary_dot(expr, expr.operator.value)

    def visit_binary_bitwise_arithmetic(self, expr: EXPR.BinaryBitwiseArithmetic) -> Any:
        self.gen_binary_dot(expr, expr.operator.value)

    def visit_binary_logical_operation(self, expr: EXPR.BinaryLogicalOperation) -> Any:
        self.gen_binary_dot(expr, expr.operator.value)

    def visit_comparison_operation(self, expr: EXPR.ComparisonOperation) -> Any:
        self.gen_binary_dot(expr, expr.operator.value)

    def visit_unary_expression(self, expr: EXPR.UnaryExpression) -> Any:
        node_name = id(expr)
        self.total += f"{node_name} [label=\"{expr.operator.value}\"];\n"
        child_name = id(expr.value)
        self.total += f"{node_name} -> {child_name};\n"
        self.visit_ast(expr.value)

    def visit_shift_expression(self, expr: EXPR.ShiftExpression) -> Any:
        node_name = id(expr)
        self.total += f"{node_name} [label=\"{expr.operator.value}{expr.shamt}\"];\n"
        child_name = id(expr.value)
        self.total += f"{node_name} -> {child_name};\n"
        self.visit_ast(expr.value)

    def visit_int(self, expr: EXPR.INT) -> Any:
        node_name = id(expr)
        self.total += f"{node_name} [label=\"INT({expr.value})\"];\n"
