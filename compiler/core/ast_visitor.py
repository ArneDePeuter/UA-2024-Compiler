from abc import ABC, abstractmethod

from compiler.core import ast


class AstVisitor(ABC):
    def __init__(self):
        self.expression_fd = {
            ast.INT: self.visit_int,
            ast.FLOAT: self.visit_float,
            ast.CHAR: self.visit_char,
            ast.IDENTIFIER: self.visit_identifier,
            ast.TypeCastExpression: self.visit_type_cast_expression,
            ast.BinaryArithmetic: self.visit_binary_arithmetic,
            ast.BinaryBitwiseArithmetic: self.visit_binary_bitwise_arithmetic,
            ast.BinaryLogicalOperation: self.visit_binary_logical_operation,
            ast.ComparisonOperation: self.visit_comparison_operation,
            ast.UnaryExpression: self.visit_unary_expression,
            ast.ShiftExpression: self.visit_shift_expression
        }
        self.statement_fd = {
            ast.Program: self.visit_program,
            ast.Body: self.visit_body,
            ast.FunctionDeclaration: self.visit_function_declaration,
            ast.VariableDeclarationQualifier: self.visit_variable_declaration_qualifier,
            ast.VariableDeclaration: self.visit_variable_declaration,
            ast.AssignmentStatement: self.visit_assignment_statement
        }
        self.type_fd = {
            ast.FloatType: self.visit_float_type,
            ast.IntegerType: self.visit_integer_type,
            ast.CharType: self.visit_char_type,
            ast.ConstType: self.visit_const_type,
            ast.DereferenceType: self.visit_dereference_type,
            ast.AddressType: self.visit_address_type
        }

    def visit_expression(self, node: ast.Expression):
        return self.expression_fd.get(type(node))(node)

    def visit_statement(self, node: ast.Statement):
        return self.statement_fd.get(type(node))(node)

    def visit_type(self, node: ast.Type):
        return self.type_fd.get(type(node))(node)

    @abstractmethod
    def visit_int(self, node: ast.INT):
        ...

    @abstractmethod
    def visit_float(self, node: ast.FLOAT):
        ...

    @abstractmethod
    def visit_char(self, node: ast.CHAR):
        ...

    @abstractmethod
    def visit_identifier(self, node: ast.IDENTIFIER):
        ...

    @abstractmethod
    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        ...

    @abstractmethod
    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        ...

    @abstractmethod
    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        ...

    @abstractmethod
    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        ...

    @abstractmethod
    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        ...

    @abstractmethod
    def visit_unary_expression(self, node: ast.UnaryExpression):
        ...

    @abstractmethod
    def visit_shift_expression(self, node: ast.ShiftExpression):
        ...

    @abstractmethod
    def visit_program(self, node: ast.Program):
        ...

    @abstractmethod
    def visit_body(self, node: ast.Body):
        ...

    @abstractmethod
    def visit_function_declaration(self, node: ast.FunctionDeclaration):
        ...

    @abstractmethod
    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        ...

    @abstractmethod
    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        ...

    @abstractmethod
    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        ...

    @abstractmethod
    def visit_float_type(self, node: ast.FloatType):
        ...

    @abstractmethod
    def visit_integer_type(self, node: ast.IntegerType):
        ...

    @abstractmethod
    def visit_char_type(self, node: ast.CharType):
        ...

    @abstractmethod
    def visit_const_type(self, node: ast.ConstType):
        ...

    @abstractmethod
    def visit_dereference_type(self, node: ast.DereferenceType):
        ...

    @abstractmethod
    def visit_address_type(self, node: ast.AddressType):
        ...
