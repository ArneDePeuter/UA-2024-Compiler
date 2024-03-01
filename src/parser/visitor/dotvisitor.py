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

    def visit_program(self, program):
        program_node_name = str(id(program))
        self.total += f'{program_node_name} [label="Program"];\n'
        for statement in program.statements:
            statement_node_name = str(id(statement))
            self.total += f'{program_node_name} -> {statement_node_name};\n'
            self.visit_ast(statement)  # Assuming visit_ast can dispatch to the correct visit method

    def gen_binary_dot(self, me: EXPR.BinaryOperation, operator_str: str) -> None:
        node_name = str(id(me))
        self.total += f"{node_name} [label=\"{operator_str}\"];\n"
        left_node_name = str(id(me.left))
        right_node_name = str(id(me.right))
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

    def visit_shift_expression(self, expr: EXPR.ShiftExpression) -> Any:
        node_name = str(id(expr))
        label = f"{expr.operator.value}"
        self.total += f"{node_name} [label=\"{label}\"];\n"

        value_node_name = str(id(expr.value))
        self.total += f"{node_name} -> {value_node_name};\n"
        self.visit_ast(expr.value)

        shamt_node_name = str(id(expr.amount))
        self.total += f"{node_name} -> {shamt_node_name};\n"
        self.visit_ast(expr.amount)

    def visit_unary_expression(self, expr: EXPR.UnaryExpression) -> Any:
        node_name = str(id(expr))
        label = f"{expr.operator.value}"
        self.total += f"{node_name} [label=\"{label}\"];\n"

        operand_node_name = str(id(expr.value))
        self.total += f"{node_name} -> {operand_node_name};\n"
        self.visit_ast(expr.value)

    def visit_int(self, expr: EXPR.INT) -> Any:
        node_name = id(expr)
        self.total += f"{node_name} [label=\"INT({expr.value})\"];\n"
