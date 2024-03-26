import copy

from compiler.core import ast
from compiler.core.ast_visitor import AstVisitor


class ConstantPropagationVisitor(AstVisitor):
    def __init__(self):
        self.const_scope: dict[str, ast.Expression] = {}
        super().__init__()

    def visit_type(self, node: ast.Type):
        return node
    
    def visit_int(self, node: ast.INT):
        return node

    def visit_float(self, node: ast.FLOAT):
        return node

    def visit_char(self, node: ast.CHAR):
        return node

    def visit_identifier(self, node: ast.IDENTIFIER):
        if node.name in self.const_scope:
            return self.const_scope[node.name]
        return node

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        node.expression = self.visit_expression(node.expression)
        return node
    
    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        node.left = self.visit_expression(node.left)
        node.right = self.visit_expression(node.right)
        return node

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        node.left = self.visit_expression(node.left)
        node.right = self.visit_expression(node.right)
        return node

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        node.left = self.visit_expression(node.left)
        node.right = self.visit_expression(node.right)
        return node

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        node.left = self.visit_expression(node.left)
        node.right = self.visit_expression(node.right)
        return node

    def visit_unary_expression(self, node: ast.UnaryExpression):
        node.left = self.visit_expression(node.left)
        node.right = self.visit_expression(node.right)
        return node

    def visit_shift_expression(self, node: ast.ShiftExpression):
        node.value = self.visit_expression(node.value)
        node.amount = self.visit_expression(node.amount)
        return node

    def visit_program(self, node: ast.Program):
        for i, statement in enumerate(node.statements):
            node.statements[i] = self.visit_statement(statement)
        return node

    def visit_body(self, node: ast.Body):
        scope_before = copy.deepcopy(self.const_scope)
        for i, statement in enumerate(node.statements):
            node.statements[i] = self.visit_statement(statement)
        self.const_scope = scope_before
        return node

    def visit_function_declaration(self, node: ast.FunctionDeclaration):
        node.body = self.visit_body(node.body)
        return node

    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        if node.initializer:
            node.initializer = self.visit_expression(node.initializer)
        return node

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        for i, qualifier in enumerate(node.qualifiers):
            node.qualifiers[i] = self.visit_variable_declaration_qualifier(qualifier)
        if node.var_type.const:
            for qualifier in node.qualifiers:
                self.const_scope[qualifier.identifier] = qualifier.initializer
        return node

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        node.left = self.visit_expression(node.left)
        node.right = self.visit_expression(node.right)
        return node

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        node.expression = self.visit_expression(node.expression)
        return node

    def visit_printf_call(self, node: ast.PrintFCall):
        return node

    def visit_comment_statement(self, node: ast.CommentStatement):
        return node
