# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#logicalExpression.
    def enterLogicalExpression(self, ctx:GrammarParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#logicalExpression.
    def exitLogicalExpression(self, ctx:GrammarParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#comparisonExpression.
    def enterComparisonExpression(self, ctx:GrammarParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#comparisonExpression.
    def exitComparisonExpression(self, ctx:GrammarParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:GrammarParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:GrammarParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:GrammarParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:GrammarParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#bitwiseExpression.
    def enterBitwiseExpression(self, ctx:GrammarParser.BitwiseExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#bitwiseExpression.
    def exitBitwiseExpression(self, ctx:GrammarParser.BitwiseExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#shiftExpression.
    def enterShiftExpression(self, ctx:GrammarParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#shiftExpression.
    def exitShiftExpression(self, ctx:GrammarParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#unaryExpression.
    def enterUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#unaryExpression.
    def exitUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#primary.
    def enterPrimary(self, ctx:GrammarParser.PrimaryContext):
        pass

    # Exit a parse tree produced by GrammarParser#primary.
    def exitPrimary(self, ctx:GrammarParser.PrimaryContext):
        pass



del GrammarParser