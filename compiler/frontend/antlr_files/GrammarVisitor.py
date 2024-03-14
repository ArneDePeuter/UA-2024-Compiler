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


    # Visit a parse tree produced by GrammarParser#declaration.
    def visitDeclaration(self, ctx:GrammarParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#castExpression.
    def visitCastExpression(self, ctx:GrammarParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expressionStatement.
    def visitExpressionStatement(self, ctx:GrammarParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#mutableExpression.
    def visitMutableExpression(self, ctx:GrammarParser.MutableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#immutableExpression.
    def visitImmutableExpression(self, ctx:GrammarParser.ImmutableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:GrammarParser.AssignmentExpressionContext):
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


    # Visit a parse tree produced by GrammarParser#typeQualifier.
    def visitTypeQualifier(self, ctx:GrammarParser.TypeQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#pointerQualifier.
    def visitPointerQualifier(self, ctx:GrammarParser.PointerQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variableList.
    def visitVariableList(self, ctx:GrammarParser.VariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable.
    def visitVariable(self, ctx:GrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:GrammarParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)



del GrammarParser