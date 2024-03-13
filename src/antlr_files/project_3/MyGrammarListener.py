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


    # Enter a parse tree produced by MyGrammarParser#mainFunction.
    def enterMainFunction(self, ctx:MyGrammarParser.MainFunctionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#mainFunction.
    def exitMainFunction(self, ctx:MyGrammarParser.MainFunctionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#compoundStatement.
    def enterCompoundStatement(self, ctx:MyGrammarParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#compoundStatement.
    def exitCompoundStatement(self, ctx:MyGrammarParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#declaration.
    def enterDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#declaration.
    def exitDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#castExpression.
    def enterCastExpression(self, ctx:MyGrammarParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#castExpression.
    def exitCastExpression(self, ctx:MyGrammarParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#statement.
    def enterStatement(self, ctx:MyGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#statement.
    def exitStatement(self, ctx:MyGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MyGrammarParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MyGrammarParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#expression.
    def enterExpression(self, ctx:MyGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#expression.
    def exitExpression(self, ctx:MyGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#mutableExpression.
    def enterMutableExpression(self, ctx:MyGrammarParser.MutableExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#mutableExpression.
    def exitMutableExpression(self, ctx:MyGrammarParser.MutableExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#immutableExpression.
    def enterImmutableExpression(self, ctx:MyGrammarParser.ImmutableExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#immutableExpression.
    def exitImmutableExpression(self, ctx:MyGrammarParser.ImmutableExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:MyGrammarParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:MyGrammarParser.AssignmentExpressionContext):
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


    # Enter a parse tree produced by MyGrammarParser#unaryExpression.
    def enterUnaryExpression(self, ctx:MyGrammarParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#unaryExpression.
    def exitUnaryExpression(self, ctx:MyGrammarParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#primary.
    def enterPrimary(self, ctx:MyGrammarParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#primary.
    def exitPrimary(self, ctx:MyGrammarParser.PrimaryContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#type.
    def enterType(self, ctx:MyGrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#type.
    def exitType(self, ctx:MyGrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#baseType.
    def enterBaseType(self, ctx:MyGrammarParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#baseType.
    def exitBaseType(self, ctx:MyGrammarParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#typeQualifier.
    def enterTypeQualifier(self, ctx:MyGrammarParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#typeQualifier.
    def exitTypeQualifier(self, ctx:MyGrammarParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#pointerQualifier.
    def enterPointerQualifier(self, ctx:MyGrammarParser.PointerQualifierContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#pointerQualifier.
    def exitPointerQualifier(self, ctx:MyGrammarParser.PointerQualifierContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#variableList.
    def enterVariableList(self, ctx:MyGrammarParser.VariableListContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#variableList.
    def exitVariableList(self, ctx:MyGrammarParser.VariableListContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#variable.
    def enterVariable(self, ctx:MyGrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#variable.
    def exitVariable(self, ctx:MyGrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:MyGrammarParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:MyGrammarParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#comment.
    def enterComment(self, ctx:MyGrammarParser.CommentContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#comment.
    def exitComment(self, ctx:MyGrammarParser.CommentContext):
        pass



del MyGrammarParser