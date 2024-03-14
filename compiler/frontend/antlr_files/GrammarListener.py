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


    # Enter a parse tree produced by GrammarParser#mainFunction.
    def enterMainFunction(self, ctx:GrammarParser.MainFunctionContext):
        pass

    # Exit a parse tree produced by GrammarParser#mainFunction.
    def exitMainFunction(self, ctx:GrammarParser.MainFunctionContext):
        pass


    # Enter a parse tree produced by GrammarParser#body.
    def enterBody(self, ctx:GrammarParser.BodyContext):
        pass

    # Exit a parse tree produced by GrammarParser#body.
    def exitBody(self, ctx:GrammarParser.BodyContext):
        pass


    # Enter a parse tree produced by GrammarParser#declaration.
    def enterDeclaration(self, ctx:GrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#declaration.
    def exitDeclaration(self, ctx:GrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#castExpression.
    def enterCastExpression(self, ctx:GrammarParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#castExpression.
    def exitCastExpression(self, ctx:GrammarParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#expressionStatement.
    def enterExpressionStatement(self, ctx:GrammarParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#expressionStatement.
    def exitExpressionStatement(self, ctx:GrammarParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#mutableExpression.
    def enterMutableExpression(self, ctx:GrammarParser.MutableExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#mutableExpression.
    def exitMutableExpression(self, ctx:GrammarParser.MutableExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#immutableExpression.
    def enterImmutableExpression(self, ctx:GrammarParser.ImmutableExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#immutableExpression.
    def exitImmutableExpression(self, ctx:GrammarParser.ImmutableExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:GrammarParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:GrammarParser.AssignmentExpressionContext):
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


    # Enter a parse tree produced by GrammarParser#type.
    def enterType(self, ctx:GrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#type.
    def exitType(self, ctx:GrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#baseType.
    def enterBaseType(self, ctx:GrammarParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#baseType.
    def exitBaseType(self, ctx:GrammarParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#typeQualifier.
    def enterTypeQualifier(self, ctx:GrammarParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#typeQualifier.
    def exitTypeQualifier(self, ctx:GrammarParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#pointerQualifier.
    def enterPointerQualifier(self, ctx:GrammarParser.PointerQualifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#pointerQualifier.
    def exitPointerQualifier(self, ctx:GrammarParser.PointerQualifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#variableList.
    def enterVariableList(self, ctx:GrammarParser.VariableListContext):
        pass

    # Exit a parse tree produced by GrammarParser#variableList.
    def exitVariableList(self, ctx:GrammarParser.VariableListContext):
        pass


    # Enter a parse tree produced by GrammarParser#variable.
    def enterVariable(self, ctx:GrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by GrammarParser#variable.
    def exitVariable(self, ctx:GrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by GrammarParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:GrammarParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by GrammarParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:GrammarParser.AssignmentOperatorContext):
        pass



del GrammarParser