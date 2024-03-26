from compiler.core import ast
from compiler.core.type_caster import TypeCaster
from compiler.core.ast_visitor import AstVisitor


class ConstantFoldingVisitor(AstVisitor):
    foldables = [ast.CHAR, ast.INT, ast.FLOAT]

    def type_match_binary(self, binary: ast.BinaryOperation) -> bool:
        """
        attempts to type match a binary operation
        returns True if possible in context of constant folding
        """
        binary.left = self.visit_expression(binary.left)
        binary.right = self.visit_expression(binary.right)

        if type(binary.left) not in ConstantFoldingVisitor.foldables or type(binary.right) not in ConstantFoldingVisitor.foldables:
            return False

        # same type so types are matched - we can execute binary (==fold)
        if type(binary.left) == type(binary.right):
            return True

        diff = TypeCaster.get_heirarchy_of_ast(binary.left) - TypeCaster.get_heirarchy_of_ast(binary.right)

        for _ in range(abs(diff)):
            if diff > 0:
                # left is bigger hierarchy so upcast right
                binary.right = TypeCaster.upcast(binary.right)
            else:
                # right is bigger so upcast left
                binary.left = TypeCaster.upcast(binary.left)
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

        if type(node.expression) not in ConstantFoldingVisitor.foldables:
            return node

        diff = TypeCaster.get_heirarchy_of_ast(node.expression) - TypeCaster.get_heirarchy_of_base_type(node.cast_type.base_type)

        result = node.expression
        for _ in range(abs(diff)):
            if diff > 0:
                # my type is bigger so downcast
                result = TypeCaster.downcast(result)
            else:
                # cast type is bigger so upcast
                result = TypeCaster.upcast(result)

        return result

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        can_fold = self.type_match_binary(node)

        if not can_fold:
            return node

        if node.operator == ast.BinaryArithmetic.Operator.PLUS:
            node = node.left + node.right
        elif node.operator == ast.BinaryArithmetic.Operator.MINUS:
            node = node.left - node.right
        elif node.operator == ast.BinaryArithmetic.Operator.MUL:
            node = node.left * node.right
        elif node.operator == ast.BinaryArithmetic.Operator.DIV:
            node = node.left / node.right
        elif node.operator == ast.BinaryArithmetic.Operator.MOD:
            print(node.left, node.right)
            node = node.left % node.right

        return node

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        can_fold = self.type_match_binary(node)

        if not can_fold:
            return node

        if not isinstance(node.left, ast.INT) or not isinstance(node.right, ast.INT):
            return node

        if node.operator == ast.BinaryBitwiseArithmetic.Operator.AND:
            node = node.left & node.right
        elif node.operator == ast.BinaryBitwiseArithmetic.Operator.OR:
            node = node.left | node.right
        elif node.operator == ast.BinaryBitwiseArithmetic.Operator.XOR:
            node = node.left ^ node.right

        return node

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        can_fold = self.type_match_binary(node)

        if not can_fold:
            return node

        if node.operator == ast.BinaryLogicalOperation.Operator.AND:
            result = node.left.value and node.right.value
        elif node.operator == ast.BinaryLogicalOperation.Operator.OR:
            result = node.left.value or node.right.value

        return ast.INT(
            value=1 if result else 0,
            position=node.left.position,
            line=node.left.line
        )

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        can_fold = self.type_match_binary(node)

        if not can_fold:
            return node

        if node.operator == ast.ComparisonOperation.Operator.EQ:
            result = node.left == node.right
        elif node.operator == ast.ComparisonOperation.Operator.NEQ:
            result = node.left != node.right
        elif node.operator == ast.ComparisonOperation.Operator.LT:
            result = node.left < node.right
        elif node.operator == ast.ComparisonOperation.Operator.GT:
            result = node.left > node.right
        elif node.operator == ast.ComparisonOperation.Operator.LTE:
            result = node.left <= node.right
        elif node.operator == ast.ComparisonOperation.Operator.GTE:
            result = node.left >= node.right

        return ast.INT(
            value=1 if result else 0,
            position=node.left.position,
            line=node.left.line
        )

    def visit_unary_expression(self, node: ast.UnaryExpression):
        node.value = self.visit_expression(node.value)

        if type(node.value) not in ConstantFoldingVisitor.foldables:
            return node

        if node.operator == ast.UnaryExpression.Operator.POSITIVE:
            return node.value
        elif node.operator == ast.UnaryExpression.Operator.NEGATIVE:
            if isinstance(node.value, ast.INT):
                return ast.INT(
                    value=-node.value.value,
                    line=node.line,
                    position=node.position
                )
            elif isinstance(node.value, ast.FLOAT):
                return ast.FLOAT(
                    value=-node.value.value,
                    line=node.line,
                    position=node.position
                )
        elif node.operator == ast.UnaryExpression.Operator.ONESCOMPLEMENT:
            if isinstance(node.value, ast.INT):
                return ast.INT(
                    value=~node.value.value,
                    line=node.line,
                    position=node.position
                )
        elif node.operator == ast.UnaryExpression.Operator.LOGICALNEGATION:
            return ast.INT(
                value=1 if not bool(node.value) else 0,
                position=node.position,
                line=node.line
            )

        return node

    def visit_shift_expression(self, node: ast.ShiftExpression):
        node.value = self.visit_expression(node.value)
        node.amount = self.visit_expression(node.amount)

        if not isinstance(node.value, ast.INT) or not isinstance(node.amount, ast.INT):
            return node

        if node.operator == ast.ShiftExpression.Operator.LEFT:
            if node.amount.value < 0:
                return ast.INT(
                    value=node.value.value >> -node.amount.value,
                    line=node.line,
                    position=node.position
                )
            return ast.INT(
                value=node.value.value << node.amount.value,
                line=node.line,
                position=node.position
            )
        elif node.operator == ast.ShiftExpression.Operator.RIGHT:
            if node.amount.value < 0:
                return ast.INT(
                    value=node.value.value << -node.amount.value,
                    line=node.line,
                    position=node.position
                )
            return ast.INT(
                value=node.value.value >> node.amount.value,
                line=node.line,
                position=node.position
            )

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
        node.left = self.visit_expression(node.left)
        node.right = self.visit_expression(node.right)
        return node

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        node.expression = self.visit_expression(node.expression)
        return node

    def visit_printf_call(self, node: ast.PrintFCall):
        node.expression = self.visit_expression(node.expression)
        return node

    def visit_comment_statement(self, node: ast.CommentStatement):
        return node
