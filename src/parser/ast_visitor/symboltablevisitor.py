from typing import Any

from .visitor import Visitor
from ..ast import ast as AST, expression as EXPR


class SemanticAnalysisVisitor(Visitor):
    def __init__(self):
        self.current_scope = None  # Keep track of the current scope's symbol table

    def visit_program(self, ast: AST.AST):
        # Set up the global scope symbol table
        self.current_scope = ast.symbol_table
        # Visit children nodes
        for statement in ast.statements:
            self.visit_ast(statement)

    def visit_binary_arithmetic(self, expr: EXPR.BinaryArithmetic) -> Any:
        pass

    def visit_binary_bitwise_arithmetic(self, expr: EXPR.BinaryBitwiseArithmetic) -> Any:
        pass

    def visit_binary_logical_operation(self, expr: EXPR.BinaryLogicalOperation) -> Any:
        pass

    def visit_comparison_operation(self, expr: EXPR.ComparisonOperation) -> Any:
        pass

    def visit_unary_expression(self, expr: EXPR.UnaryExpression) -> Any:
        pass

    def visit_shift_expression(self, expr: EXPR.ShiftExpression) -> Any:
        pass

    def visit_int(self, expr: EXPR.INT) -> Any:
        pass
