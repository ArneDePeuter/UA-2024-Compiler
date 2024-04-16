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


    # Enter a parse tree produced by GrammarParser#whileStatement.
    def enterWhileStatement(self, ctx:GrammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#whileStatement.
    def exitWhileStatement(self, ctx:GrammarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#forStatement.
    def enterForStatement(self, ctx:GrammarParser.ForStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#forStatement.
    def exitForStatement(self, ctx:GrammarParser.ForStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:GrammarParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:GrammarParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#variableDeclarationQualifiers.
    def enterVariableDeclarationQualifiers(self, ctx:GrammarParser.VariableDeclarationQualifiersContext):
        pass

    # Exit a parse tree produced by GrammarParser#variableDeclarationQualifiers.
    def exitVariableDeclarationQualifiers(self, ctx:GrammarParser.VariableDeclarationQualifiersContext):
        pass


    # Enter a parse tree produced by GrammarParser#variableDeclarationQualifier.
    def enterVariableDeclarationQualifier(self, ctx:GrammarParser.VariableDeclarationQualifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#variableDeclarationQualifier.
    def exitVariableDeclarationQualifier(self, ctx:GrammarParser.VariableDeclarationQualifierContext):
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


    # Enter a parse tree produced by GrammarParser#typedefStatement.
    def enterTypedefStatement(self, ctx:GrammarParser.TypedefStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#typedefStatement.
    def exitTypedefStatement(self, ctx:GrammarParser.TypedefStatementContext):
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


    # Enter a parse tree produced by GrammarParser#printCall.
    def enterPrintCall(self, ctx:GrammarParser.PrintCallContext):
        pass

    # Exit a parse tree produced by GrammarParser#printCall.
    def exitPrintCall(self, ctx:GrammarParser.PrintCallContext):
        pass


    # Enter a parse tree produced by GrammarParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:GrammarParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:GrammarParser.AssignmentStatementContext):
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


    # Enter a parse tree produced by GrammarParser#const.
    def enterConst(self, ctx:GrammarParser.ConstContext):
        pass

    # Exit a parse tree produced by GrammarParser#const.
    def exitConst(self, ctx:GrammarParser.ConstContext):
        pass


    # Enter a parse tree produced by GrammarParser#addressQualifier.
    def enterAddressQualifier(self, ctx:GrammarParser.AddressQualifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#addressQualifier.
    def exitAddressQualifier(self, ctx:GrammarParser.AddressQualifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:GrammarParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by GrammarParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:GrammarParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by GrammarParser#comment.
    def enterComment(self, ctx:GrammarParser.CommentContext):
        pass

    # Exit a parse tree produced by GrammarParser#comment.
    def exitComment(self, ctx:GrammarParser.CommentContext):
        pass



del GrammarParser