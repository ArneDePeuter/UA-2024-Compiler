# Generated from Main.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MainParser import MainParser
else:
    from MainParser import MainParser

# This class defines a complete listener for a parse tree produced by MainParser.
class MainListener(ParseTreeListener):

    # Enter a parse tree produced by MainParser#program.
    def enterProgram(self, ctx:MainParser.ProgramContext):
        pass

    # Exit a parse tree produced by MainParser#program.
    def exitProgram(self, ctx:MainParser.ProgramContext):
        pass


    # Enter a parse tree produced by MainParser#expression.
    def enterExpression(self, ctx:MainParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#expression.
    def exitExpression(self, ctx:MainParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#logicalExpression.
    def enterLogicalExpression(self, ctx:MainParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#logicalExpression.
    def exitLogicalExpression(self, ctx:MainParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#comparisonExpression.
    def enterComparisonExpression(self, ctx:MainParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#comparisonExpression.
    def exitComparisonExpression(self, ctx:MainParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:MainParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:MainParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:MainParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:MainParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#bitwiseExpression.
    def enterBitwiseExpression(self, ctx:MainParser.BitwiseExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#bitwiseExpression.
    def exitBitwiseExpression(self, ctx:MainParser.BitwiseExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#shiftExpression.
    def enterShiftExpression(self, ctx:MainParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#shiftExpression.
    def exitShiftExpression(self, ctx:MainParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#unaryExpression.
    def enterUnaryExpression(self, ctx:MainParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#unaryExpression.
    def exitUnaryExpression(self, ctx:MainParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#primary.
    def enterPrimary(self, ctx:MainParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MainParser#primary.
    def exitPrimary(self, ctx:MainParser.PrimaryContext):
        pass



del MainParser