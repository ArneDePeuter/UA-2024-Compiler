# Generated from Main.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MainParser import MainParser
else:
    from MainParser import MainParser

# This class defines a complete generic visitor for a parse tree produced by MainParser.

class MainVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MainParser#program.
    def visitProgram(self, ctx:MainParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#mainFunction.
    def visitMainFunction(self, ctx:MainParser.MainFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#compoundStatement.
    def visitCompoundStatement(self, ctx:MainParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#declaration.
    def visitDeclaration(self, ctx:MainParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#castExpression.
    def visitCastExpression(self, ctx:MainParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#statement.
    def visitStatement(self, ctx:MainParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MainParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#expression.
    def visitExpression(self, ctx:MainParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#mutableExpression.
    def visitMutableExpression(self, ctx:MainParser.MutableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#immutableExpression.
    def visitImmutableExpression(self, ctx:MainParser.ImmutableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:MainParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#logicalExpression.
    def visitLogicalExpression(self, ctx:MainParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:MainParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MainParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MainParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#bitwiseExpression.
    def visitBitwiseExpression(self, ctx:MainParser.BitwiseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#shiftExpression.
    def visitShiftExpression(self, ctx:MainParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#unaryExpression.
    def visitUnaryExpression(self, ctx:MainParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#primary.
    def visitPrimary(self, ctx:MainParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#type.
    def visitType(self, ctx:MainParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#baseType.
    def visitBaseType(self, ctx:MainParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#typeQualifier.
    def visitTypeQualifier(self, ctx:MainParser.TypeQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#pointerQualifier.
    def visitPointerQualifier(self, ctx:MainParser.PointerQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#variableList.
    def visitVariableList(self, ctx:MainParser.VariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#variable.
    def visitVariable(self, ctx:MainParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:MainParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MainParser#comment.
    def visitComment(self, ctx:MainParser.CommentContext):
        return self.visitChildren(ctx)



del MainParser