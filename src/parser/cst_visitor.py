from antlr4 import *
from src.antlr_files.project_1.MyGrammarParser import MyGrammarParser
from src.antlr_files.project_1.MyGrammarVisitor import MyGrammarVisitor

from .ast.expression import *
from .ast.program import Program


class CSTVisitor(MyGrammarVisitor):
    def visitProgram(self, ctx):
        statements = []

        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            statement = self.visit(child)
            statements.append(statement)
        return Program(
            statements=statements
        )

    def visitAdditiveExpression(self, ctx:MyGrammarParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return BinaryArithmetic(
            left=left,
            operator=BinaryArithmetic.Operator.PLUS,
            right=right
        )

    def visitMultiplicativeExpression(self, ctx:MyGrammarParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return BinaryArithmetic(
            left=left,
            operator=BinaryArithmetic.Operator.MUL,
            right=right
        )

    def visitLogicalExpression(self, ctx:MyGrammarParser.LogicalExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        op = BinaryLogicalOperation.Operator(op)
        return BinaryLogicalOperation(
            left=left,
            operator=op,
            right=right
        )

    def visitComparisonExpression(self, ctx:MyGrammarParser.ComparisonExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        op = ComparisonOperation.Operator(op)
        return ComparisonOperation(
            left=left,
            operator=op,
            right=right
        )

    def visitUnaryExpression(self, ctx:MyGrammarParser.UnaryExpressionContext):
        if ctx.primary():
            return self.visit(ctx.primary())
        expr = self.visit(ctx.unaryExpression())
        op = ctx.getChild(0).getText()
        op = UnaryExpression.Operator(op)
        return UnaryExpression(
            value=expr,
            operator=op
        )

    def visitBitwiseExpression(self, ctx:MyGrammarParser.BitwiseExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        op = BinaryBitwiseArithmetic.Operator(op)
        return BinaryBitwiseArithmetic(
            left=left,
            operator=op,
            right=right
        )

    def visitShiftExpression(self, ctx:MyGrammarParser.ShiftExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unaryExpression())
        else:
            value = self.visit(ctx.shiftExpression())
            amount = self.visit(ctx.unaryExpression())
            op = ctx.getChild(1).getText()
            op = ShiftExpression.Operator(op)
            return ShiftExpression(
                value=value,
                operator=op,
                amount=amount
            )

    def visitPrimary(self, ctx:MyGrammarParser.PrimaryContext):
        if ctx.NUMBER() is not None:
            return INT(int(ctx.NUMBER().getText()))
        elif ctx.expression() is not None:
            return self.visit(ctx.expression())
