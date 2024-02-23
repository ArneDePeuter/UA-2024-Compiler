from antlr4 import *
from src.antlr_files.MyGrammarLexer import MyGrammarLexer
from src.antlr_files.MyGrammarParser import MyGrammarParser
from src.antlr_files.MyGrammarVisitor import MyGrammarVisitor
from ..ast.expression import *
from ..ast.program import Program

class ConcreteVisitor(MyGrammarVisitor):
    def visitProgram(self, ctx):
        statements = []

        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            statement = self.visit(child)  # Visit each child and get the AST node
            statements.append(statement)
        return Program(statements)

    def visitAdditiveExpression(self, ctx:MyGrammarParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1)
        return BinaryArithmetic(left, right, op)

    def visitMultiplicativeExpression(self, ctx:MyGrammarParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1)
        return BinaryArithmetic(left, right, op)
    def visitLogicalExpression(self, ctx:MyGrammarParser.LogicalExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1)
        return BinaryLogicalOperation(left, right, op)

    def visitComparisonExpression(self, ctx:MyGrammarParser.ComparisonExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1)
        return ComparisonOperation(left, right, op)

    def visitUnaryExpression(self, ctx:MyGrammarParser.UnaryExpressionContext):
        # If the unary expression is just a primary expression
        if ctx.primary():
            return self.visit(ctx.primary())
        # If the unary expression contains another unary expression
        operator = ctx.getChild(0).getText()  # Get the text of the unary operator
        expr = self.visit(ctx.unaryExpression())  # Recursively visit the unary expression
        # Translate string operator to the corresponding Enum
        if operator == '+':
            op = UnaryExpression.Operator.POSITIVE
        elif operator == '-':
            op = UnaryExpression.Operator.NEGATIVE
        elif operator == '!':
            op = UnaryExpression.Operator.LOGICALNEGATION
        else:
            op = UnaryExpression.Operator.ONESCOMPLEMENT
        return UnaryExpression(expr, op)


    def visitBitwiseExpression(self, ctx:MyGrammarParser.BitwiseExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1)
        return BinaryBitwiseArithmetic(left, right, op)

    def visitShiftExpression(self, ctx:MyGrammarParser.ShiftExpressionContext):
        if ctx.getChildCount() == 1:
            # If there's no shift operation (i.e., it's just a unary expression)
            return self.visit(ctx.unaryExpression())
        else:
            # If there is a shift operation
            left = self.visit(ctx.shiftExpression())  # Visit the left-hand side (which is another shiftExpression)
            right = self.visit(ctx.unaryExpression())  # Visit the right-hand side (which should be an unaryExpression, not primary)
            # Determine the operation based on the context's text
            op = ctx.getChild(1).getText()  # Get the operator ('<<' or '>>')
            # Depending on your AST node structure, you may need to create a new ShiftExpression node here.
            # Assuming you have a corresponding AST class and enum for shift operations:
            if op == '<<':
                operation = ShiftExpression.Operator.LEFT
            else:
                operation = ShiftExpression.Operator.RIGHT
            # Assuming your ShiftExpression class takes the left and right operands and the operation
            return ShiftExpression(left, operation, right)  # Note: Adjust according to your actual AST class structure


    def visitPrimary(self, ctx:MyGrammarParser.PrimaryContext):
        if ctx.NUMBER() is not None:
            return INT(int(ctx.NUMBER().getText()))
        elif ctx.expression() is not None:
            return self.visit(ctx.expression())
