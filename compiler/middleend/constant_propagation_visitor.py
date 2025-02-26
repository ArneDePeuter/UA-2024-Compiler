import copy

from compiler.core import ast
from compiler.core.ast_visitor import AstVisitor


class ConstantPropagationVisitor(AstVisitor):
    def __init__(self):
        self.const_scope: dict[str, tuple[ast.Expression, bool]] = {}
        self.lock_propagation = False
        self.prevLine = -1
        super().__init__()

    def visit_statement(self, node: ast.Statement):
        # visit statement
        result = super().visit_statement(node)
        # cleanup prev line because we need to use prev line in above statement
        curr_line = node.line
        remove_keys = []
        for identifier, item in self.const_scope.items():
            value, const = item
            if value.line == self.prevLine and not const:
                remove_keys.append(identifier)
        for key in remove_keys:
            del self.const_scope[key]
        self.prevLine = curr_line
        # return result
        return result

    def visit_type(self, node: ast.Type):
        return node
    
    def visit_int(self, node: ast.INT):
        return node

    def visit_float(self, node: ast.FLOAT):
        return node

    def visit_char(self, node: ast.CHAR):
        return node

    def visit_identifier(self, node: ast.IDENTIFIER):
        if node.name in self.const_scope and not self.lock_propagation:
            propagated = copy.deepcopy(self.const_scope[node.name][0])
            propagated.line = node.line
            propagated.position = node.position
            return propagated
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
        if node.operator in [
            ast.UnaryExpression.Operator.ADDRESSOF,
            ast.UnaryExpression.Operator.DECREMENT,
            ast.UnaryExpression.Operator.INCREMENT,
            ast.UnaryExpression.Operator.DEREFERENCE,
        ]:
            self.lock_propagation = True
        node.value = self.visit_expression(node.value)
        self.lock_propagation = False
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
        if node.initializer is not None:
            node.initializer = self.visit_expression(node.initializer)
        return node

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        for i, qualifier in enumerate(node.qualifiers):
            node.qualifiers[i] = self.visit_variable_declaration_qualifier(qualifier)

        for qual in node.qualifiers:
            if qual.initializer is not None and not isinstance(qual.initializer, ast.FunctionCall):
                self.const_scope[qual.identifier] = (qual.initializer, node.var_type.const)
        return node

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        self.lock_propagation = True
        node.left = self.visit_expression(node.left)
        self.lock_propagation = False
        node.right = self.visit_expression(node.right)
        return node

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        node.expression = self.visit_expression(node.expression)
        return node

    def visit_comment_statement(self, node: ast.CommentStatement):
        return node

    def visit_while_statement(self, node: ast.WhileStatement):
        # dont constant propagate while loop because referenced variables can change
        # node.expression = self.visit_expression(node.expression)
        # node.to_execute = self.visit_statement(node.to_execute)
        return node

    def visit_break_statement(self, node: ast.BreakStatement):
        return node

    def visit_continue_statement(self, node: ast.ContinueStatement):
        return node

    def visit_if_statement(self, node: ast.IfStatement):
        node.condition = self.visit_expression(node.condition)
        node.body = self.visit_body(node.body)
        if node.else_statement:
            node.else_statement = self.visit_statement(node.else_statement)
        return node

    def visit_else_statement(self, node: ast.ElseStatement):
        node.body = self.visit_body(node.body)
        return node

    def visit_function_call(self, node: ast.FunctionCall):
        for i, arg in enumerate(node.arguments):
            node.arguments[i] = self.visit_expression(arg)
        return node

    def visit_return_statement(self, node: ast.ReturnStatement):
        if node.expression:
            node.expression = self.visit_expression(node.expression)
        return node

    def visit_forward_declaration(self, node: ast.ForwardDeclaration):
        return node

    def visit_printf_call(self, node: ast.PrintFCall):
        for i, arg in enumerate(node.args):
            node.args[i] = self.visit_expression(arg)
        return node

    def visit_scanf_call(self, node: ast.ScanFCall):
        for i, arg in enumerate(node.args):
            node.args[i] = self.visit_expression(arg)
        return node

    def visit_array_specifier(self, node: ast.ArraySpecifier):
        for i, size in enumerate(node.sizes):
            simplified_size = self.visit_expression(size)
            if not isinstance(simplified_size, ast.ArraySpecifier):
                node.sizes[i] = simplified_size
            else:
                node.sizes[i] = size

        return node

    def visit_array_initializer(self, node: ast.ArrayInitializer):
        for i, element in enumerate(node.elements):
            simplified_element = self.visit_expression(element)
            if not isinstance(simplified_element, ast.ArraySpecifier):
                node.elements[i] = simplified_element
            else:
                node.elements[i] = element
        return node

    def visit_array_access(self, node: ast.ArrayAccess):
        node.index = self.visit_expression(node.index)
        return node

    def visit_struct_access(self, node: ast.StructAccess):
        node.target = self.visit_expression(node.target)
        return node

    def visit_struct_definition(self, node: ast.StructDefinition):
        return node
