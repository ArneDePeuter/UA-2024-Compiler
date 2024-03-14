from abc import ABC, abstractmethod
from typing import Any, Dict

from compiler.core import ast


class ASTVisitor(ABC):
    def __init__(self):
        self.forward_dict: Dict[type, Any] = {
            ast.Program: self.visit_program,
            ast.INT: self.visit_int,
            ast.BinaryArithmetic: self.visit_binary_arithmetic,
            ast.BinaryBitwiseArithmetic: self.visit_binary_bitwise_arithmetic,
            ast.BinaryLogicalOperation: self.visit_binary_logical_operation,
            ast.ComparisonOperation: self.visit_comparison_operation,
            ast.UnaryExpression: self.visit_unary_expression,
            ast.ShiftExpression: self.visit_shift_expression,
        }

    def visit_ast(self, ast: ast.AST) -> Any:
        ast_type = type(ast)
        handler = self.forward_dict.get(ast_type)
        if handler:
            return handler(ast)
        else:
            raise NotImplementedError(f"No handler found for ast of type: {ast_type}")

    @abstractmethod
    def visit_program(self, program: ast.Program) -> Any:
        pass

    @abstractmethod
    def visit_binary_arithmetic(self, expr: ast.BinaryArithmetic) -> Any:
        pass

    @abstractmethod
    def visit_binary_bitwise_arithmetic(self, expr: ast.BinaryBitwiseArithmetic) -> Any:
        pass

    @abstractmethod
    def visit_binary_logical_operation(self, expr: ast.BinaryLogicalOperation) -> Any:
        pass

    @abstractmethod
    def visit_comparison_operation(self, expr: ast.ComparisonOperation) -> Any:
        pass

    @abstractmethod
    def visit_unary_expression(self, expr: ast.UnaryExpression) -> Any:
        pass

    @abstractmethod
    def visit_shift_expression(self, expr: ast.ShiftExpression) -> Any:
        pass

    @abstractmethod
    def visit_int(self, expr: ast.INT) -> Any:
        pass
