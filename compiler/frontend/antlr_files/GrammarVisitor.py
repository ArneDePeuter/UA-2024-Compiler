# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#program.
    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#logicalExpression.
    def visitLogicalExpression(self, ctx:GrammarParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:GrammarParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:GrammarParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:GrammarParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#bitwiseExpression.
    def visitBitwiseExpression(self, ctx:GrammarParser.BitwiseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#shiftExpression.
    def visitShiftExpression(self, ctx:GrammarParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#unaryExpression.
    def visitUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#primary.
    def visitPrimary(self, ctx:GrammarParser.PrimaryContext):
        return self.visitChildren(ctx)



del GrammarParser