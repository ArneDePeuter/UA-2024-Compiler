# Generated from Main.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MainParser import MainParser
else:
    from MainParser import MainParser

# This class defines a complete generic visitor for a parse tree produced by MainParser.

class MainVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MainParser#program.
    def visitProgram(self, ctx:MainParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#expression.
    def visitExpression(self, ctx:MainParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#logicalExpression.
    def visitLogicalExpression(self, ctx:MainParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:MainParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MainParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MainParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#bitwiseExpression.
    def visitBitwiseExpression(self, ctx:MainParser.BitwiseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#shiftExpression.
    def visitShiftExpression(self, ctx:MainParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#unaryExpression.
    def visitUnaryExpression(self, ctx:MainParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#primary.
    def visitPrimary(self, ctx:MainParser.PrimaryContext):
        return self.visitChildren(ctx)



del MainParser