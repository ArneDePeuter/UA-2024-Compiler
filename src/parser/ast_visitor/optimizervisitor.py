from typing import Any
from .visitor import Visitor
from ..ast import expression as EXPR
from ..ast.expression import INT, CastExpression, Assignment
from ..ast.program import Program
from ..ast.main_function import MainFunction
from ..ast.compound_statement import CompoundStatement
from ..ast.declaration import Declaration
from ..ast.type import Type
from ..ast.variable import Variable
from ..ast import ast as AST


class OptimizerVisitor(Visitor):
    def __init__(self):
        super().__init__()

    def visit_ast(self, ast: AST.AST) -> Any:
        try:
            return super().visit_ast(ast)
        except NotImplementedError as e:
            print(f"Error visiting AST node: {ast}")
            raise e

    def visit_program(self, program: Program):
        for i, statement in enumerate(program.statements):
            program.statements[i] = self.visit_ast(statement)
        return program  # Return the optimized program

    def visit_main_function(self, main_function: MainFunction):
        # Optimize the compound statement (function body)
        main_function.body = self.visit_ast(main_function.body)
        return main_function

    def visit_compound_statement(self, compound_statement: CompoundStatement):
        for i, statement in enumerate(compound_statement.statements):
            compound_statement.statements[i] = self.visit_ast(statement)
        return compound_statement

    def visit_declaration(self, declaration: Declaration):
        declaration.var_type = self.visit_ast(declaration.var_type)
        declaration.variables = [self.visit_ast(var) for var in declaration.variables]
        return declaration

    def visit_assignment(self, expr: Assignment) -> Any:
        expr.left = self.visit_ast(expr.left)
        expr.right = self.visit_ast(expr.right)
        return expr

    def visit_type(self, type_node: Type):
        return type_node

    def visit_variable(self, variable: Variable):
        if variable.initializer is not None:
            variable.initializer = self.visit_ast(variable.initializer)
        return variable

    def visit_cast_expression(self, cast_expression: CastExpression):
        cast_expression.cast_type = self.visit_ast(cast_expression.cast_type)
        cast_expression.expression = self.visit_ast(cast_expression.expression)
        return cast_expression

    def visit_binary_arithmetic(self, expr: EXPR.BinaryArithmetic) -> any:
        # Visit left and right operands to potentially simplify them first
        expr.left = self.visit_ast(expr.left)
        expr.right = self.visit_ast(expr.right)

        # If both operands are now INT expressions, we can fold them
        if isinstance(expr.left, EXPR.INT) and isinstance(expr.right, EXPR.INT):
            if expr.operator == EXPR.BinaryArithmetic.Operator.PLUS:
                return INT(expr.left.value + expr.right.value)
            elif expr.operator == EXPR.BinaryArithmetic.Operator.MINUS:
                return INT(expr.left.value - expr.right.value)
            elif expr.operator == EXPR.BinaryArithmetic.Operator.MUL:
                return INT(expr.left.value * expr.right.value)
            elif expr.operator == EXPR.BinaryArithmetic.Operator.DIV:
                return INT(expr.left.value // expr.right.value)
            elif expr.operator == EXPR.BinaryArithmetic.Operator.MOD:
                return INT(expr.left.value % expr.right.value)
        # If no folding was possible, return the possibly modified expression
        return expr

    def visit_binary_bitwise_arithmetic(self, expr: EXPR.BinaryBitwiseArithmetic):
        # Visit left and right operands to potentially simplify them first
        expr.left = self.visit_ast(expr.left)
        expr.right = self.visit_ast(expr.right)

        # If both operands are now INT expressions, we can fold them
        if isinstance(expr.left, EXPR.INT) and isinstance(expr.right, EXPR.INT):
            if expr.operator == EXPR.BinaryBitwiseArithmetic.Operator.AND:
                return INT(expr.left.value & expr.right.value)
            elif expr.operator == EXPR.BinaryBitwiseArithmetic.Operator.OR:
                return INT(expr.left.value | expr.right.value)
            elif expr.operator == EXPR.BinaryBitwiseArithmetic.Operator.XOR:
                return INT(expr.left.value ^ expr.right.value)
        # If no folding was possible, return the possibly modified expression
        return expr

    def visit_binary_logical_operation(self, expr: EXPR.BinaryLogicalOperation):
        # Visit left and right operands to potentially simplify them first
        expr.left = self.visit_ast(expr.left)
        expr.right = self.visit_ast(expr.right)

        # If both operands are now INT expressions, we can fold them
        if isinstance(expr.left, EXPR.INT) and isinstance(expr.right, EXPR.INT):
            if expr.operator == EXPR.BinaryLogicalOperation.Operator.AND:
                return INT(expr.left.value and expr.right.value)
            elif expr.operator == EXPR.BinaryLogicalOperation.Operator.OR:
                return INT(expr.left.value or expr.right.value)
        # If no folding was possible, return the possibly modified expression
        return expr

    def visit_comparison_operation(self, expr: EXPR.ComparisonOperation):
        # Visit left and right operands to potentially simplify them first
        expr.left = self.visit_ast(expr.left)
        expr.right = self.visit_ast(expr.right)

        # If both operands are now INT expressions, we can fold them
        if isinstance(expr.left, EXPR.INT) and isinstance(expr.right, EXPR.INT):
            if expr.operator == EXPR.ComparisonOperation.Operator.GT:
                return INT(expr.left.value > expr.right.value)
            elif expr.operator == EXPR.ComparisonOperation.Operator.LT:
                return INT(expr.left.value < expr.right.value)
            elif expr.operator == EXPR.ComparisonOperation.Operator.GTE:
                return INT(expr.left.value >= expr.right.value)
            elif expr.operator == EXPR.ComparisonOperation.Operator.LTE:
                return INT(expr.left.value <= expr.right.value)
            elif expr.operator == EXPR.ComparisonOperation.Operator.EQ:
                return INT(expr.left.value == expr.right.value)
            elif expr.operator == EXPR.ComparisonOperation.Operator.NEQ:
                return INT(expr.left.value != expr.right.value)
        # If no folding was possible, return the possibly modified expression
        return expr

    def visit_unary_expression(self, expr: EXPR.UnaryExpression):
        # Visit operand to potentially simplify it first
        expr.value = self.visit_ast(expr.value)

        # If operand is now INT expression, we can fold it
        if isinstance(expr.value, EXPR.INT):
            if expr.operator == EXPR.UnaryExpression.Operator.POSITIVE:
                return INT(+expr.value.value)
            elif expr.operator == EXPR.UnaryExpression.Operator.NEGATIVE:
                return INT(-expr.value.value)
            elif expr.operator == EXPR.UnaryExpression.Operator.ONESCOMPLEMENT:
                return INT(~expr.value.value)
            elif expr.operator == EXPR.UnaryExpression.Operator.LOGICALNEGATION:
                return INT(not expr.value.value)

        # If no folding was possible, return the possibly modified expression
        return expr

    def visit_bitwise_expression(self, expr: EXPR.BitwiseExpression):
        # Visit left and right operands to potentially simplify them first
        expr.left = self.visit_ast(expr.left)
        expr.right = self.visit_ast(expr.right)

        # If both operands are now INT expressions, we can fold them
        if isinstance(expr.left, EXPR.INT) and isinstance(expr.right, EXPR.INT):
            if expr.operator == EXPR.BitwiseExpression.Operator.BITAND:
                return INT(expr.left.value & expr.right.value)
            elif expr.operator == EXPR.BitwiseExpression.Operator.BITOR:
                return INT(expr.left.value | expr.right.value)
            elif expr.operator == EXPR.BitwiseExpression.Operator.BITXOR:
                return INT(expr.left.value ^ expr.right.value)
            elif expr.operator == EXPR.BitwiseExpression.Operator.BITNOT:
                return INT(~expr.left.value)
        # If no folding was possible, return the possibly modified expression
        return expr

    def visit_shift_expression(self, expr: EXPR.ShiftExpression):
        # Visit left and right operands to potentially simplify them first
        expr.value = self.visit_ast(expr.value)
        expr.amount = self.visit_ast(expr.amount)

        # If both operands are now INT expressions, we can fold them
        if isinstance(expr.value, EXPR.INT) and isinstance(expr.amount, EXPR.INT):
            if expr.operator == EXPR.ShiftExpression.Operator.LEFT:
                # Check if amount is negative
                if expr.amount.value < 0:
                    return EXPR.INT(expr.value.value >> -expr.amount.value)
                return EXPR.INT(expr.value.value << expr.amount.value)
            elif expr.operator == EXPR.ShiftExpression.Operator.RIGHT:
                # Check if amount is negative
                if expr.amount.value < 0:
                    return EXPR.INT(expr.value.value << -expr.amount.value)
                return EXPR.INT(expr.value.value >> expr.amount.value)
        # If no folding was possible, return the possibly modified expression
        return expr

    def visit_int(self, expression):
        # Literal expressions are already constant, so no folding needed
        return expression

    def visit_float(self, expr: EXPR.FLOAT) -> Any:
        # Literal expressions are already constant, so no folding needed
        return expr

    def visit_char(self, expr: EXPR.CHAR) -> Any:
        # Literal expressions are already constant, so no folding needed
        return expr

    def visit_variable_reference(self, expr: EXPR.VariableReference) -> Any:
        # Variable references cannot be folded, so return the expression as is
        return expr