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
            ast.ShiftExpression: self.visit_shift_expression,
            ast.FunctionCall: self.visit_function_call,
            ast.PrintFCall: self.visit_printf_call,
            ast.ArraySpecifier: self.visit_array_specifier,
            ast.ArrayInitializer: self.visit_array_initializer,
            ast.ArrayAccess: self.visit_array_access,
        }
        self.statement_fd = {
            ast.ExpressionStatement: self.visit_expression_statement,
            ast.Program: self.visit_program,
            ast.Body: self.visit_body,
            ast.FunctionDeclaration: self.visit_function_declaration,
            ast.VariableDeclarationQualifier: self.visit_variable_declaration_qualifier,
            ast.VariableDeclaration: self.visit_variable_declaration,
            ast.AssignmentStatement: self.visit_assignment_statement,
            ast.CommentStatement: self.visit_comment_statement,
            ast.IfStatement: self.visit_if_statement,
            ast.ElseStatement: self.visit_else_statement,
            ast.WhileStatement: self.visit_while_statement,
            ast.BreakStatement: self.visit_break_statement,
            ast.ContinueStatement: self.visit_continue_statement,
            ast.ReturnStatement: self.visit_return_statement,
            ast.ForwardDeclaration: self.visit_forward_declaration,
        }

    def visit(self, node: ast.AST):
        # This is the generic visit method.
        if isinstance(node, ast.Expression):
            return self.visit_expression(node)
        elif isinstance(node, ast.Statement):
            return self.visit_statement(node)
        else:
            raise TypeError(f"Unknown node type: {type(node)}")

    def visit_expression(self, node: ast.Expression):
        return self.expression_fd.get(type(node))(node)

    def visit_statement(self, node: ast.Statement):
        return self.statement_fd.get(type(node))(node)

    @abstractmethod
    def visit_type(self, node: ast.Type):
        ...

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
    def visit_expression_statement(self, node: ast.ExpressionStatement):
        ...

    @abstractmethod
    def visit_function_call(self, node: ast.FunctionCall):
        ...

    @abstractmethod
    def visit_comment_statement(self, node: ast.CommentStatement):
        ...

    @abstractmethod
    def visit_if_statement(self, node: ast.IfStatement):
        ...

    @abstractmethod
    def visit_else_statement(self, node: ast.ElseStatement):
        ...

    @abstractmethod
    def visit_while_statement(self, node: ast.WhileStatement):
        ...

    @abstractmethod
    def visit_break_statement(self, node: ast.BreakStatement):
        ...

    @abstractmethod
    def visit_continue_statement(self, node: ast.ContinueStatement):
        ...

    @abstractmethod
    def visit_return_statement(self, node: ast.ReturnStatement):
        ...

    @abstractmethod
    def visit_forward_declaration(self, node: ast.ForwardDeclaration):
        ...

    @abstractmethod
    def visit_printf_call(self, node: ast.PrintFCall):
        ...

    @abstractmethod
    def visit_array_specifier(self, node: ast.ArraySpecifier):
        ...

    @abstractmethod
    def visit_array_initializer(self, node: ast.ArrayInitializer):
        ...

    @abstractmethod
    def visit_array_access(self, node: ast.ArrayAccess):
        ...
