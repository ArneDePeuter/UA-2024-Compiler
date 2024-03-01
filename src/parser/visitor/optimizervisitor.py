from .visitor import Visitor
from ..ast import expression as EXPR
from ..ast.expression import INT
from ..ast.program import Program
from ..ast import ast as AST


class OptimizerVisitor(Visitor):
    def __init__(self):
        super().__init__()

    def visit_ast(self, ast: AST.AST):
        return super().visit_ast(ast)

    def visit_program(self, program: Program):
        pass

    def visit_binary_arithmetic(self, expr: EXPR.BinaryArithmetic):
        if expr.operator == EXPR.BinaryArithmetic.Operator.PLUS:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value + expr.right.value)

        if expr.operator == EXPR.BinaryArithmetic.Operator.MINUS:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value - expr.right.value)

        if expr.operator == EXPR.BinaryArithmetic.Operator.MUL:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value * expr.right.value)

        if expr.operator == EXPR.BinaryArithmetic.Operator.DIV:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value // expr.right.value)

        if expr.operator == EXPR.BinaryArithmetic.Operator.MOD:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value % expr.right.value)

        return expr

    def visit_binary_bitwise_arithmetic(self, expr: EXPR.BinaryBitwiseArithmetic):
        if expr.operator == EXPR.BinaryBitwiseArithmetic.Operator.AND:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value & expr.right.value)

        if expr.operator == EXPR.BinaryBitwiseArithmetic.Operator.OR:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value | expr.right.value)

        if expr.operator == EXPR.BinaryBitwiseArithmetic.Operator.XOR:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value ^ expr.right.value)

        return expr

    def visit_binary_logical_operation(self, expr: EXPR.BinaryLogicalOperation):
        if expr.operator == EXPR.BinaryLogicalOperation.Operator.AND:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value and expr.right.value)

        if expr.operator == EXPR.BinaryLogicalOperation.Operator.OR:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value or expr.right.value)

        return expr

    def visit_comparison_operation(self, expr: EXPR.ComparisonOperation):
        if expr.operator == EXPR.ComparisonOperation.Operator.EQ:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value == expr.right.value)

        if expr.operator == EXPR.ComparisonOperation.Operator.NEQ:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value != expr.right.value)

        if expr.operator == EXPR.ComparisonOperation.Operator.LT:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value < expr.right.value)

        if expr.operator == EXPR.ComparisonOperation.Operator.LTE:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value <= expr.right.value)

        if expr.operator == EXPR.ComparisonOperation.Operator.GT:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value > expr.right.value)

        if expr.operator == EXPR.ComparisonOperation.Operator.GTE:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value >= expr.right.value)

        return expr

    def visit_unary_expression(self, expr: EXPR.UnaryExpression):
        if expr.operator == EXPR.UnaryExpression.Operator.NEGATIVE:
            if isinstance(expr.value, INT):
                return INT(-expr.value.value)

        if expr.operator == EXPR.UnaryExpression.Operator.POSITIVE:
            if isinstance(expr.value, INT):
                return INT(expr.value.value)

        if expr.operator == EXPR.UnaryExpression.Operator.LOGICALNEGATION:
            if isinstance(expr.value, INT):
                return INT(not expr.value.value)

        if expr.operator == EXPR.UnaryExpression.Operator.ONESCOMPLEMENT:
            if isinstance(expr.value, INT):
                return INT(~expr.value.value)

        return expr

    def visit_bitwise_expression(self, expr: EXPR.BitwiseExpression):
        if expr.operator == EXPR.BitwiseExpression.Operator.BITOR:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value | expr.right.value)

        if expr.operator == EXPR.BitwiseExpression.Operator.BITXOR:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value ^ expr.right.value)

        if expr.operator == EXPR.BitwiseExpression.Operator.BITAND:
            if isinstance(expr.left, INT) and isinstance(expr.right, INT):
                return INT(expr.left.value & expr.right.value)

        if expr.operator == EXPR.BitwiseExpression.Operator.BITNOT:
            if isinstance(expr.value, INT):
                return INT(~expr.value.value)

        return expr
    def visit_shift_expression(self, expr: EXPR.ShiftExpression):
        if expr.operator == EXPR.ShiftExpression.Operator.LEFT:
            if isinstance(expr.value, INT) and isinstance(expr.amount, INT):
                return INT(expr.value.value << expr.amount.value)

        if expr.operator == EXPR.ShiftExpression.Operator.RIGHT:
            if isinstance(expr.value, INT) and isinstance(expr.amount, INT):
                return INT(expr.value.value >> expr.amount.value)

        return expr

    def visit_int(self, expression):
        # Literal expressions are already constant, so no folding needed
        return expression