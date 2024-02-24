from abc import ABC, abstractmethod
from typing import Any, Dict

from ..ast.program import Program
from ..ast import expression as EXPR
from ..ast import ast as AST


class Visitor(ABC):
    def __init__(self):
        self.forward_dict: Dict[type, Any] = {
            Program: self.visit_program,
            EXPR.INT: self.visit_int,
            EXPR.BinaryArithmetic: self.visit_binary_arithmetic,
            EXPR.BinaryBitwiseArithmetic: self.visit_binary_bitwise_arithmetic,
            EXPR.BinaryLogicalOperation: self.visit_binary_logical_operation,
            EXPR.ComparisonOperation: self.visit_comparison_operation,
            EXPR.UnaryExpression: self.visit_unary_expression,
            EXPR.ShiftExpression: self.visit_shift_expression,
        }

    def visit_ast(self, ast: AST.AST) -> Any:
        ast_type = type(ast)
        handler = self.forward_dict.get(ast_type)
        if handler:
            return handler(ast)
        else:
            raise NotImplementedError(f"No handler found for ast: {ast_type}")


    @abstractmethod
    def visit_program(self, program: Program) -> Any:
        pass

    @abstractmethod
    def visit_binary_arithmetic(self, expr: EXPR.BinaryArithmetic) -> Any:
        pass

    @abstractmethod
    def visit_binary_bitwise_arithmetic(self, expr: EXPR.BinaryBitwiseArithmetic) -> Any:
        pass

    @abstractmethod
    def visit_binary_logical_operation(self, expr: EXPR.BinaryLogicalOperation) -> Any:
        pass

    @abstractmethod
    def visit_comparison_operation(self, expr: EXPR.ComparisonOperation) -> Any:
        pass

    @abstractmethod
    def visit_unary_expression(self, expr: EXPR.UnaryExpression) -> Any:
        pass

    @abstractmethod
    def visit_shift_expression(self, expr: EXPR.ShiftExpression) -> Any:
        pass

    @abstractmethod
    def visit_int(self, expr: EXPR.INT) -> Any:
        pass
