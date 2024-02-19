from antlr4 import *
from src.antlr_files.MyGrammarLexer import MyGrammarLexer
from src.antlr_files.MyGrammarParser import MyGrammarParser
from src.antlr_files.MyGrammarVisitor import MyGrammarVisitor
from ..ast.expression import *

class ConcreteVisitor(MyGrammarVisitor):
    def visitLogicalExpression(self, ctx:MyGrammarParser.LogicalExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        return BinaryLogicalOperation(left, right, op)

    def visitComparisonExpression(self, ctx:MyGrammarParser.ComparisonExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        return ComparisonOperation(left, right, op)

    def visitAdditiveExpression(self, ctx:MyGrammarParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 3:  # It means there's a left operand, an operator, and a right operand
            left = self.visit(ctx.getChild(0))  # Visit the left side
            op = ctx.getChild(1).getText()  # Get the operator as text
            right = self.visit(ctx.getChild(2))  # Visit the right side

            # Assuming BinaryArithmetic is a class in your AST that can hold these
            return BinaryArithmetic(left, op, right)
        else:
            # This covers the case where it directly reduces to multiplicativeExpression
            return self.visit(ctx.multiplicativeExpression())

    def visitMultiplicativeExpression(self, ctx:MyGrammarParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        return BinaryArithmetic(left, right, op)

    def visitUnaryExpression(self, ctx:MyGrammarParser.UnaryExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.bitwiseExpression())
        op = ctx.op.text
        expr = self.visit(ctx.unaryExpression())
        return UnaryExpression(expr, op)

    def visitShiftExpression(self, ctx:MyGrammarParser.ShiftExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        value = self.visit(ctx.shiftExpression())
        direction = ctx.op.text  # '<<' or '>>'
        shiftBy = self.visit(ctx.primary())
        return ShiftExpression(value, direction, shiftBy)  # Assuming a class ShiftExpression

    def visitBitwiseExpression(self, ctx:MyGrammarParser.BitwiseExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text  # '&', '|', '^'
        return BitwiseExpression(left, right, op)  # Assuming a class BitwiseOperation

    def visitUnaryExpression(self, ctx:MyGrammarParser.UnaryExpressionContext):
        # Adjusted to handle bitwise NOT ('~')
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))  # Directly visit bitwiseExpression if no unary operator
        op = ctx.op.text  # '+', '-', '!', or '~'
        expr = self.visit(ctx.unaryExpression())
        return UnaryExpression(expr, op)  # Assuming a class UnaryExpression, already defined but adjusted for '~'

    def visitPrimary(self, ctx:MyGrammarParser.PrimaryContext):
        if ctx.NUMBER() is not None:
            return INT(int(ctx.NUMBER().getText()))  # Assuming a class NumberNode for numeric literals
        elif ctx.expression() is not None:
            return self.visit(ctx.expression())  # Parenthesized expression
