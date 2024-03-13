from abc import ABC, abstractmethod
from typing import Any, Dict

from ..ast.program import Program
from ..ast import expression as EXPR
from ..ast import ast as AST
from ..ast.main_function import MainFunction
from ..ast.compound_statement import CompoundStatement
from ..ast.expression import CastExpression
from ..ast.type import Type
from ..ast.declaration import Declaration
from ..ast.variable import Variable
from ..ast.comment import Comment


class Visitor(ABC):
    def __init__(self):
        self.forward_dict: Dict[type, Any] = {
            Program: self.visit_program,
            MainFunction: self.visit_main_function,
            CompoundStatement: self.visit_compound_statement,
            Comment: self.visit_comment,
            Declaration: self.visit_declaration,
            Type: self.visit_type,
            Variable: self.visit_variable,
            CastExpression: self.visit_cast_expression,
            EXPR.INT: self.visit_int,
            EXPR.BinaryArithmetic: self.visit_binary_arithmetic,
            EXPR.BinaryBitwiseArithmetic: self.visit_binary_bitwise_arithmetic,
            EXPR.BinaryLogicalOperation: self.visit_binary_logical_operation,
            EXPR.ComparisonOperation: self.visit_comparison_operation,
            EXPR.UnaryExpression: self.visit_unary_expression,
            EXPR.ShiftExpression: self.visit_shift_expression,
            EXPR.FLOAT: self.visit_float,
            EXPR.CHAR: self.visit_char,
            EXPR.VariableReference: self.visit_variable_reference,
            EXPR.Assignment: self.visit_assignment,
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
    def visit_main_function(self, main_function: MainFunction) -> Any:
        pass

    @abstractmethod
    def visit_compound_statement(self, compound_statement: CompoundStatement) -> Any:
        pass

    def visit_comment(self, comment: Comment) -> Any:
        pass

    @abstractmethod
    def visit_declaration(self, declaration: Declaration) -> Any:
        pass

    @abstractmethod
    def visit_type(self, type_node: Type) -> Any:
        pass

    @abstractmethod
    def visit_variable(self, variable: Variable) -> Any:
        pass

    @abstractmethod
    def visit_cast_expression(self, cast_expression: CastExpression) -> Any:
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