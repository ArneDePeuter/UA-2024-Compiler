# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
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


    # Enter a parse tree produced by GrammarParser#atom.
    def enterAtom(self, ctx:GrammarParser.AtomContext):
        pass

    # Exit a parse tree produced by GrammarParser#atom.
    def exitAtom(self, ctx:GrammarParser.AtomContext):
        pass



del GrammarParser