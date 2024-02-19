from antlr4 import *
from src.antlr_files.GrammarLexer import GrammarLexer
from src.antlr_files.GrammarParser import GrammarParser
from src.antlr_files.GrammarVisitor import GrammarVisitor
from ..ast.expression import *

class ConcreteVisitor(GrammarVisitor):
    def visitLogicalExpression(self, ctx:GrammarParser.LogicalExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        return BinaryLogicalOperation(left, right, op)

    def visitComparisonExpression(self, ctx:GrammarParser.ComparisonExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        return ComparisonOperation(left, right, op)

    def visitAdditiveExpression(self, ctx:GrammarParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        return BinaryArithmetic(left, right, op)

    def visitMultiplicativeExpression(self, ctx:GrammarParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        return BinaryArithmetic(left, right, op)

    def visitUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.bitwiseExpression())
        op = ctx.op.text
        expr = self.visit(ctx.unaryExpression())
        return UnaryExpression(expr, op)

    # TODO: Implement other visit methods for shiftExpression, bitwiseExpression, etc.
