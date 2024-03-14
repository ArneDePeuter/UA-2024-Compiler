from typing import Any

from compiler.core.ast_visitor import ASTVisitor
from compiler.core import ast


class ASTDotVisitor(ASTVisitor):
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
        for expression in program.expressions:
            statement_node_name = str(id(expression))
            self.total += f'{program_node_name} -> {statement_node_name};\n'
            self.visit_ast(expression)

    def gen_binary_dot(self, me: ast.BinaryOperation, operator_str: str) -> None:
        node_name = str(id(me))
        self.total += f"{node_name} [label=\"{operator_str}\"];\n"
        left_node_name = str(id(me.left))
        right_node_name = str(id(me.right))
        self.total += f"{node_name} -> {left_node_name};\n"
        self.total += f"{node_name} -> {right_node_name};\n"
        self.visit_ast(me.left)
        self.visit_ast(me.right)

    def visit_binary_arithmetic(self, expr: ast.BinaryArithmetic) -> Any:
        self.gen_binary_dot(expr, expr.operator.name)

    def visit_binary_bitwise_arithmetic(self, expr: ast.BinaryBitwiseArithmetic) -> Any:
        self.gen_binary_dot(expr, expr.operator.name)

    def visit_binary_logical_operation(self, expr: ast.BinaryLogicalOperation) -> Any:
        self.gen_binary_dot(expr, expr.operator.name)

    def visit_comparison_operation(self, expr: ast.ComparisonOperation) -> Any:
        self.gen_binary_dot(expr, expr.operator.name)

    def visit_shift_expression(self, expr: ast.ShiftExpression) -> Any:
        node_name = str(id(expr))
        label = f"{expr.operator.name}"
        self.total += f"{node_name} [label=\"{label}\"];\n"

        value_node_name = str(id(expr.value))
        self.total += f"{node_name} -> {value_node_name};\n"
        self.visit_ast(expr.value)

        shamt_node_name = str(id(expr.amount))
        self.total += f"{node_name} -> {shamt_node_name};\n"
        self.visit_ast(expr.amount)

    def visit_unary_expression(self, expr: ast.UnaryExpression) -> Any:
        node_name = str(id(expr))
        operator_str = expr.operator.name
        self.total += f"{node_name} [label=\"{operator_str}\"];\n"

        operand_node_name = str(id(expr.value))
        self.total += f"{node_name} -> {operand_node_name};\n"
        self.visit_ast(expr.value)

    def visit_int(self, expr: ast.INT) -> Any:
        node_name = id(expr)
        self.total += f"{node_name} [label=\"{expr.value}\"];\n"
