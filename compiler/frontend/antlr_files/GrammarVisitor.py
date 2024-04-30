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


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#structDefinition.
    def visitStructDefinition(self, ctx:GrammarParser.StructDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#structList.
    def visitStructList(self, ctx:GrammarParser.StructListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#typedIdentifier.
    def visitTypedIdentifier(self, ctx:GrammarParser.TypedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:GrammarParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#enumBody.
    def visitEnumBody(self, ctx:GrammarParser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#enumList.
    def visitEnumList(self, ctx:GrammarParser.EnumListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forwardDeclaration.
    def visitForwardDeclaration(self, ctx:GrammarParser.ForwardDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#typeList.
    def visitTypeList(self, ctx:GrammarParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#returnStatement.
    def visitReturnStatement(self, ctx:GrammarParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:GrammarParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#paramList.
    def visitParamList(self, ctx:GrammarParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#functionCall.
    def visitFunctionCall(self, ctx:GrammarParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#argumentList.
    def visitArgumentList(self, ctx:GrammarParser.ArgumentListContext):
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


    # Visit a parse tree produced by GrammarParser#printfCall.
    def visitPrintfCall(self, ctx:GrammarParser.PrintfCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#continueStatement.
    def visitContinueStatement(self, ctx:GrammarParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:GrammarParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#enumType.
    def visitEnumType(self, ctx:GrammarParser.EnumTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variableDeclarationQualifiers.
    def visitVariableDeclarationQualifiers(self, ctx:GrammarParser.VariableDeclarationQualifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variableDeclarationQualifier.
    def visitVariableDeclarationQualifier(self, ctx:GrammarParser.VariableDeclarationQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arraySpecifier.
    def visitArraySpecifier(self, ctx:GrammarParser.ArraySpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:GrammarParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#castExpression.
    def visitCastExpression(self, ctx:GrammarParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#switchStatement.
    def visitSwitchStatement(self, ctx:GrammarParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#caseStatement.
    def visitCaseStatement(self, ctx:GrammarParser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#defaultCaseStatement.
    def visitDefaultCaseStatement(self, ctx:GrammarParser.DefaultCaseStatementContext):
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


    # Visit a parse tree produced by GrammarParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:GrammarParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ifStatement.
    def visitIfStatement(self, ctx:GrammarParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#elseStatement.
    def visitElseStatement(self, ctx:GrammarParser.ElseStatementContext):
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


    # Visit a parse tree produced by GrammarParser#structAccess.
    def visitStructAccess(self, ctx:GrammarParser.StructAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#unaryExpression.
    def visitUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#primary.
    def visitPrimary(self, ctx:GrammarParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#structType.
    def visitStructType(self, ctx:GrammarParser.StructTypeContext):
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