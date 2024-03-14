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


    # Enter a parse tree produced by MainParser#mainFunction.
    def enterMainFunction(self, ctx:MainParser.MainFunctionContext):
        pass

    # Exit a parse tree produced by MainParser#mainFunction.
    def exitMainFunction(self, ctx:MainParser.MainFunctionContext):
        pass


    # Enter a parse tree produced by MainParser#compoundStatement.
    def enterCompoundStatement(self, ctx:MainParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by MainParser#compoundStatement.
    def exitCompoundStatement(self, ctx:MainParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by MainParser#declaration.
    def enterDeclaration(self, ctx:MainParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MainParser#declaration.
    def exitDeclaration(self, ctx:MainParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MainParser#castExpression.
    def enterCastExpression(self, ctx:MainParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#castExpression.
    def exitCastExpression(self, ctx:MainParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#statement.
    def enterStatement(self, ctx:MainParser.StatementContext):
        pass

    # Exit a parse tree produced by MainParser#statement.
    def exitStatement(self, ctx:MainParser.StatementContext):
        pass


    # Enter a parse tree produced by MainParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MainParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MainParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MainParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MainParser#expression.
    def enterExpression(self, ctx:MainParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#expression.
    def exitExpression(self, ctx:MainParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#mutableExpression.
    def enterMutableExpression(self, ctx:MainParser.MutableExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#mutableExpression.
    def exitMutableExpression(self, ctx:MainParser.MutableExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#immutableExpression.
    def enterImmutableExpression(self, ctx:MainParser.ImmutableExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#immutableExpression.
    def exitImmutableExpression(self, ctx:MainParser.ImmutableExpressionContext):
        pass


    # Enter a parse tree produced by MainParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:MainParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by MainParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:MainParser.AssignmentExpressionContext):
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


    # Enter a parse tree produced by MainParser#type.
    def enterType(self, ctx:MainParser.TypeContext):
        pass

    # Exit a parse tree produced by MainParser#type.
    def exitType(self, ctx:MainParser.TypeContext):
        pass


    # Enter a parse tree produced by MainParser#baseType.
    def enterBaseType(self, ctx:MainParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by MainParser#baseType.
    def exitBaseType(self, ctx:MainParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by MainParser#typeQualifier.
    def enterTypeQualifier(self, ctx:MainParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by MainParser#typeQualifier.
    def exitTypeQualifier(self, ctx:MainParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by MainParser#pointerQualifier.
    def enterPointerQualifier(self, ctx:MainParser.PointerQualifierContext):
        pass

    # Exit a parse tree produced by MainParser#pointerQualifier.
    def exitPointerQualifier(self, ctx:MainParser.PointerQualifierContext):
        pass


    # Enter a parse tree produced by MainParser#variableList.
    def enterVariableList(self, ctx:MainParser.VariableListContext):
        pass

    # Exit a parse tree produced by MainParser#variableList.
    def exitVariableList(self, ctx:MainParser.VariableListContext):
        pass


    # Enter a parse tree produced by MainParser#variable.
    def enterVariable(self, ctx:MainParser.VariableContext):
        pass

    # Exit a parse tree produced by MainParser#variable.
    def exitVariable(self, ctx:MainParser.VariableContext):
        pass


    # Enter a parse tree produced by MainParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:MainParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by MainParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:MainParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by MainParser#comment.
    def enterComment(self, ctx:MainParser.CommentContext):
        pass

    # Exit a parse tree produced by MainParser#comment.
    def exitComment(self, ctx:MainParser.CommentContext):
        pass



del MainParser