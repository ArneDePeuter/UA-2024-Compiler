# Generated from MyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#program.
    def visitProgram(self, ctx:MyGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#expression.
    def visitExpression(self, ctx:MyGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#logicalExpression.
    def visitLogicalExpression(self, ctx:MyGrammarParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:MyGrammarParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MyGrammarParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MyGrammarParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#bitwiseExpression.
    def visitBitwiseExpression(self, ctx:MyGrammarParser.BitwiseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#shiftExpression.
    def visitShiftExpression(self, ctx:MyGrammarParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#unaryExpression.
    def visitUnaryExpression(self, ctx:MyGrammarParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#primary.
    def visitPrimary(self, ctx:MyGrammarParser.PrimaryContext):
        return self.visitChildren(ctx)



del MyGrammarParser