# Generated from MyGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#program.
    def visitProgram(self, ctx:MyGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#mainFunction.
    def visitMainFunction(self, ctx:MyGrammarParser.MainFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#compoundStatement.
    def visitCompoundStatement(self, ctx:MyGrammarParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#declaration.
    def visitDeclaration(self, ctx:MyGrammarParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#castExpression.
    def visitCastExpression(self, ctx:MyGrammarParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#statement.
    def visitStatement(self, ctx:MyGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MyGrammarParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#expression.
    def visitExpression(self, ctx:MyGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#mutableExpression.
    def visitMutableExpression(self, ctx:MyGrammarParser.MutableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#immutableExpression.
    def visitImmutableExpression(self, ctx:MyGrammarParser.ImmutableExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:MyGrammarParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#logicalExpression.
    def visitLogicalExpression(self, ctx:MyGrammarParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:MyGrammarParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:MyGrammarParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:MyGrammarParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#bitwiseExpression.
    def visitBitwiseExpression(self, ctx:MyGrammarParser.BitwiseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#shiftExpression.
    def visitShiftExpression(self, ctx:MyGrammarParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#unaryExpression.
    def visitUnaryExpression(self, ctx:MyGrammarParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#primary.
    def visitPrimary(self, ctx:MyGrammarParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#type.
    def visitType(self, ctx:MyGrammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#baseType.
    def visitBaseType(self, ctx:MyGrammarParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#typeQualifier.
    def visitTypeQualifier(self, ctx:MyGrammarParser.TypeQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#pointerQualifier.
    def visitPointerQualifier(self, ctx:MyGrammarParser.PointerQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#variableList.
    def visitVariableList(self, ctx:MyGrammarParser.VariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#variable.
    def visitVariable(self, ctx:MyGrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:MyGrammarParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)



del MyGrammarParser