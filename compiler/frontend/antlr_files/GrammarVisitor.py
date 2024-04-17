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


    # Visit a parse tree produced by GrammarParser#mainFunction.
    def visitMainFunction(self, ctx:GrammarParser.MainFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#body.
    def visitBody(self, ctx:GrammarParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#iterationStatement.
    def visitIterationStatement(self, ctx:GrammarParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forCondition.
    def visitForCondition(self, ctx:GrammarParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forFirst.
    def visitForFirst(self, ctx:GrammarParser.ForFirstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forSecond.
    def visitForSecond(self, ctx:GrammarParser.ForSecondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forThird.
    def visitForThird(self, ctx:GrammarParser.ForThirdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#breakStatement.
    def visitBreakStatement(self, ctx:GrammarParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#continueStatement.
    def visitContinueStatement(self, ctx:GrammarParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:GrammarParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variableDeclarationQualifiers.
    def visitVariableDeclarationQualifiers(self, ctx:GrammarParser.VariableDeclarationQualifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variableDeclarationQualifier.
    def visitVariableDeclarationQualifier(self, ctx:GrammarParser.VariableDeclarationQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#castExpression.
    def visitCastExpression(self, ctx:GrammarParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#typedefStatement.
    def visitTypedefStatement(self, ctx:GrammarParser.TypedefStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expressionStatement.
    def visitExpressionStatement(self, ctx:GrammarParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#printCall.
    def visitPrintCall(self, ctx:GrammarParser.PrintCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:GrammarParser.AssignmentStatementContext):
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


    # Visit a parse tree produced by GrammarParser#type.
    def visitType(self, ctx:GrammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#baseType.
    def visitBaseType(self, ctx:GrammarParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#const.
    def visitConst(self, ctx:GrammarParser.ConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#addressQualifier.
    def visitAddressQualifier(self, ctx:GrammarParser.AddressQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:GrammarParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#comment.
    def visitComment(self, ctx:GrammarParser.CommentContext):
        return self.visitChildren(ctx)



del GrammarParser