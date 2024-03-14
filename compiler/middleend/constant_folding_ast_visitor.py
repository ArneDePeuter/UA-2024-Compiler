from compiler.core import ast
from compiler.core.ast_visitor import ASTVisitor


class ConstantFoldingASTVisitor(ASTVisitor):
    def __init__(self):
        super().__init__()

    def visit_program(self, program: ast.Program):
        for i, expression in enumerate(program.expressions):
            program.expressions[i] = self.visit_ast(expression)
        return program  # Return the optimized program

    def visit_binary_arithmetic(self, expr: ast.BinaryArithmetic) -> any:
        # Visit left and right operands to potentially simplify them first
        expr.left = self.visit_ast(expr.left)
        expr.right = self.visit_ast(expr.right)

        # If both operands aren't INT expressions, we can't fold them
        if not (isinstance(expr.left, ast.INT) and isinstance(expr.right, ast.INT)):
            return expr

        result = None
        if expr.operator == ast.BinaryArithmetic.Operator.PLUS:
            result = expr.left.value + expr.right.value
        elif expr.operator == ast.BinaryArithmetic.Operator.MINUS:
            result = expr.left.value - expr.right.value
        elif expr.operator == ast.BinaryArithmetic.Operator.MUL:
            result = expr.left.value * expr.right.value
        elif expr.operator == ast.BinaryArithmetic.Operator.DIV:
            result = expr.left.value // expr.right.value
        elif expr.operator == ast.BinaryArithmetic.Operator.MOD:
            result = expr.left.value % expr.right.value
        return ast.INT(result)

    def visit_binary_bitwise_arithmetic(self, expr: ast.BinaryBitwiseArithmetic):
        # Visit left and right operands to potentially simplify them first
        expr.left = self.visit_ast(expr.left)
        expr.right = self.visit_ast(expr.right)

        # If both operands aren't INT expressions, we can't fold them
        if not (isinstance(expr.left, ast.INT) and isinstance(expr.right, ast.INT)):
            return expr

        result = None
        if expr.operator == ast.BinaryBitwiseArithmetic.Operator.AND:
            result = expr.left.value & expr.right.value
        elif expr.operator == ast.BinaryBitwiseArithmetic.Operator.OR:
            result = expr.left.value | expr.right.value
        elif expr.operator == ast.BinaryBitwiseArithmetic.Operator.XOR:
            result = expr.left.value ^ expr.right.value
        return ast.INT(result)

    def visit_binary_logical_operation(self, expr: ast.BinaryLogicalOperation):
        # Visit left and right operands to potentially simplify them first
        expr.left = self.visit_ast(expr.left)
        expr.right = self.visit_ast(expr.right)

        # If both operands aren't INT expressions, we can't fold them
        if not (isinstance(expr.left, ast.INT) and isinstance(expr.right, ast.INT)):
            return expr

        result = None
        if expr.operator == ast.BinaryLogicalOperation.Operator.AND:
            result = expr.left.value and expr.right.value
        elif expr.operator == ast.BinaryLogicalOperation.Operator.OR:
            result = expr.left.value or expr.right.value
        return ast.INT(int(result))

    def visit_comparison_operation(self, expr: ast.ComparisonOperation):
        # Visit left and right operands to potentially simplify them first
        expr.left = self.visit_ast(expr.left)
        expr.right = self.visit_ast(expr.right)

        # If both operands aren't INT expressions, we can't fold them
        if not (isinstance(expr.left, ast.INT) and isinstance(expr.right, ast.INT)):
            return expr

        result = None
        if expr.operator == ast.ComparisonOperation.Operator.GT:
            result = expr.left.value > expr.right.value
        elif expr.operator == ast.ComparisonOperation.Operator.LT:
            result = expr.left.value < expr.right.value
        elif expr.operator == ast.ComparisonOperation.Operator.GTE:
            result = expr.left.value >= expr.right.value
        elif expr.operator == ast.ComparisonOperation.Operator.LTE:
            result = expr.left.value <= expr.right.value
        elif expr.operator == ast.ComparisonOperation.Operator.EQ:
            result = expr.left.value == expr.right.value
        elif expr.operator == ast.ComparisonOperation.Operator.NEQ:
            result = expr.left.value != expr.right.value
        return ast.INT(int(result))

    def visit_unary_expression(self, expr: ast.UnaryExpression):
        # Visit operand to potentially simplify it first
        expr.value = self.visit_ast(expr.value)

        # If operand is not INT expression, we can't fold it
        if not isinstance(expr.value, ast.INT):
            return expr

        value = None
        if expr.operator == ast.UnaryExpression.Operator.POSITIVE:
            value = +expr.value.value
        elif expr.operator == ast.UnaryExpression.Operator.NEGATIVE:
            value = -expr.value.value
        elif expr.operator == ast.UnaryExpression.Operator.ONESCOMPLEMENT:
            value = ~expr.value.value
        elif expr.operator == ast.UnaryExpression.Operator.LOGICALNEGATION:
            value = int(not expr.value.value)
        return ast.INT(value)

    def visit_shift_expression(self, expr: ast.ShiftExpression):
        # Visit left and right operands to potentially simplify them first
        expr.value = self.visit_ast(expr.value)
        expr.amount = self.visit_ast(expr.amount)

        # If both operands are now INT expressions, we can fold them
        if isinstance(expr.value, ast.INT) and isinstance(expr.amount, ast.INT):
            if expr.operator == ast.ShiftExpression.Operator.LEFT:
                # Check if amount is negative
                if expr.amount.value < 0:
                    return ast.INT(expr.value.value >> -expr.amount.value)
                return ast.INT(expr.value.value << expr.amount.value)
            elif expr.operator == ast.ShiftExpression.Operator.RIGHT:
                # Check if amount is negative
                if expr.amount.value < 0:
                    return ast.INT(expr.value.value << -expr.amount.value)
                return ast.INT(expr.value.value >> expr.amount.value)
        # If no folding was possible, return the possibly modified expression
        return expr

    def visit_int(self, expression):
        # Literal expressions are already constant, so no folding needed
        return expression
