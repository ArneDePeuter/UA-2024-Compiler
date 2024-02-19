from antlr4 import *
from src.antlr_files.MyGrammarLexer import MyGrammarLexer
from src.antlr_files.MyGrammarParser import MyGrammarParser
from src.antlr_files.MyGrammarVisitor import MyGrammarVisitor
from ..ast.expression import *

class ConcreteVisitor(MyGrammarVisitor):
    def visitAdditiveExpression(self, ctx:MyGrammarParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1)
        return BinaryArithmetic(left, right, op)

    def visitMultiplicativeExpression(self, ctx:MyGrammarParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1)
        return BinaryArithmetic(left, right, op)
    def visitLogicalExpression(self, ctx:MyGrammarParser.LogicalExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1)
        return BinaryLogicalOperation(left, right, op)

    def visitComparisonExpression(self, ctx:MyGrammarParser.ComparisonExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1)
        return ComparisonOperation(left, right, op)

    def visitUnaryExpression(self, ctx:MyGrammarParser.UnaryExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.bitwiseExpression())
        op = ctx.getChild(0)
        expr = self.visit(ctx.unaryExpression())
        return UnaryExpression(expr, op)

    def visitBitwiseExpression(self, ctx:MyGrammarParser.BitwiseExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1)  # '&', '|', '^'
        return BitwiseExpression(left, right, op)  # Assuming a class BitwiseOperation

    # TODO: handle ShiftExpression properly
    def visitShiftExpression(self, ctx:MyGrammarParser.ShiftExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        value = self.visit(ctx.shiftExpression())
        direction = ctx.getChild(0).getText()
        shiftBy = self.visit(ctx.primary())
        return ShiftExpression(value, direction, shiftBy)  # Assuming a class ShiftExpression

    def visitPrimary(self, ctx:MyGrammarParser.PrimaryContext):
        if ctx.NUMBER() is not None:
            return INT(int(ctx.NUMBER().getText()))  # Assuming a class NumberNode for numeric literals
        elif ctx.expression() is not None:
            return self.visit(ctx.expression())  # Parenthesized expression
