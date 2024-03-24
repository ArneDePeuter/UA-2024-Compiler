from typing import Union

from compiler.core import ast
from compiler.core.ast_visitor import AstVisitor


class ConstantFoldingVisitor(AstVisitor):
    @staticmethod
    def upcast(item: Union[ast.INT, ast.CHAR]) -> Union[ast.FLOAT, ast.INT]:
        if isinstance(item, ast.INT):
            return ast.FLOAT(
                value=float(item.value),
                line=item.line,
                position=item.position
            )
        if isinstance(item, ast.CHAR):
            return ast.INT(
                value=ord(item.value),
                line=item.line,
                position=item.position
            )

    def type_match_binary(self, binary: ast.BinaryOperation) -> bool:
        """
        attempts to type match a binary operation
        returns True if possible in context of constant folding
        """
        self.visit_expression(binary.left)
        self.visit_expression(binary.right)

        heirarchy = [ast.CHAR, ast.INT, ast.FLOAT]

        # could be unfoldable expression
        if type(binary.left) not in heirarchy or type(binary.right) not in heirarchy:
            return False

        # same type so types are matched - we can execute binary (==fold)
        if type(binary.left) == type(binary.right):
            return True

        diff = heirarchy.index(type(binary.left)) - heirarchy.index(type(binary.right))

        for _ in range(abs(diff)):
            if diff > 0:
                # left is bigger hierarchy so upcast right
                binary.right = self.upcast(binary.right)
            else:
                # right is bigger so upcast left
                binary.left = self.upcast(binary.left)
        return True

    def visit_type(self, node: ast.Type):
        return node

    def visit_int(self, node: ast.INT):
        return node

    def visit_float(self, node: ast.FLOAT):
        return node

    def visit_char(self, node: ast.CHAR):
        return node

    def visit_identifier(self, node: ast.IDENTIFIER):
        return node

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        node.expression = self.visit_expression(node.expression)
        return node

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        can_fold = self.type_match_binary(node)

        if not can_fold:
            return

        if node.operator == ast.BinaryArithmetic.Operator.PLUS:
            node = node.left + node.right
        elif node.operator == ast.BinaryArithmetic.Operator.MINUS:
            node = node.left - node.right
        elif node.operator == ast.BinaryArithmetic.Operator.MUL:
            node = node.left * node.right
        elif node.operator == ast.BinaryArithmetic.Operator.DIV:
            node = node.left / node.right
        elif node.operator == ast.BinaryArithmetic.Operator.MOD:
            node = node.left % node.right

        return node

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        can_fold = self.type_match_binary(node)

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        can_fold = self.type_match_binary(node)

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        can_fold = self.type_match_binary(node)

    def visit_unary_expression(self, node: ast.UnaryExpression):
        node.value = self.visit_expression(node.value)
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
        for i, statement in enumerate(node.statements):
            node.statements[i] = self.visit_statement(statement)
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
        return node

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        node.value = self.visit_expression(node.value)
        return node

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        node.expression = self.visit_expression(node.expression)
        return node

    def visit_printf_call(self, node: ast.PrintFCall):
        node.expression = self.visit_expression(node.expression)
        return node

    def visit_comment_statement(self, node: ast.CommentStatement):
        return node
