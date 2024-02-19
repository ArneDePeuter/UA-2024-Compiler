# Generated from MyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#program.
    def enterProgram(self, ctx:MyGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#program.
    def exitProgram(self, ctx:MyGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#expression.
    def enterExpression(self, ctx:MyGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#expression.
    def exitExpression(self, ctx:MyGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#logicalExpression.
    def enterLogicalExpression(self, ctx:MyGrammarParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#logicalExpression.
    def exitLogicalExpression(self, ctx:MyGrammarParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#comparisonExpression.
    def enterComparisonExpression(self, ctx:MyGrammarParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#comparisonExpression.
    def exitComparisonExpression(self, ctx:MyGrammarParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:MyGrammarParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:MyGrammarParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:MyGrammarParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:MyGrammarParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#unaryExpression.
    def enterUnaryExpression(self, ctx:MyGrammarParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#unaryExpression.
    def exitUnaryExpression(self, ctx:MyGrammarParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#bitwiseExpression.
    def enterBitwiseExpression(self, ctx:MyGrammarParser.BitwiseExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#bitwiseExpression.
    def exitBitwiseExpression(self, ctx:MyGrammarParser.BitwiseExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#shiftExpression.
    def enterShiftExpression(self, ctx:MyGrammarParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#shiftExpression.
    def exitShiftExpression(self, ctx:MyGrammarParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#primary.
    def enterPrimary(self, ctx:MyGrammarParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#primary.
    def exitPrimary(self, ctx:MyGrammarParser.PrimaryContext):
        pass



del MyGrammarParser