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
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        return BinaryArithmetic(left, right, op)

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

    # TODO: Implement other visit methods for shiftExpression, bitwiseExpression, etc.
