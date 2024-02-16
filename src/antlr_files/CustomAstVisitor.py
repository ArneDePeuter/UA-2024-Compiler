# CustomAstVisitor.py

from antlr4 import *
from GrammarParser import GrammarParser
from GrammarVisitor import GrammarVisitor
from AstNodes import *  # Make sure this matches the name of the file where your AST nodes are defined

class CustomAstVisitor(GrammarVisitor):
    def visitExpressionSequence(self, ctx:GrammarParser.ExpressionSequenceContext):
        return self.visit(ctx.logicalExpression())

    def visitLogicalExpression(self, ctx:GrammarParser.LogicalExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.comparisonExpression(0))
        else:
            left = self.visit(ctx.comparisonExpression(0))
            for i in range(1, ctx.getChildCount(), 2):
                op = ctx.getChild(i).getText()
                right = self.visit(ctx.comparisonExpression(i + 1))
                left = BinaryOpNode(left, op, right)
            return left

    def visitComparisonExpression(self, ctx:GrammarParser.ComparisonExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.additiveExpression(0))
        else:
            left = self.visit(ctx.additiveExpression(0))
            for i in range(1, ctx.getChildCount(), 2):
                op = ctx.getChild(i).getText()
                right = self.visit(ctx.additiveExpression(i + 1))
                left = BinaryOpNode(left, op, right)
            return left

    def visitAdditiveExpression(self, ctx:GrammarParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiplicativeExpression(0))

        left = self.visit(ctx.multiplicativeExpression(0))
        for i in range(2, ctx.getChildCount(), 2):  # Process remaining children
            op = ctx.getChild(i - 1).getText()  # Operator is always before the expression
            right_expr = ctx.multiplicativeExpression(i // 2)
            if right_expr:  # Ensure the expression exists
                right = self.visit(right_expr)
                left = BinaryOpNode(left, op, right)
        
        return left


    def visitMultiplicativeExpression(self, ctx:GrammarParser.MultiplicativeExpressionContext):
        # Base case: only one child (a simple unary expression)
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unaryExpression(0))

        # Recursive case: multiple children (binary operation)
        left = self.visit(ctx.unaryExpression(0))
        # Iterate over all binary operations (if any)
        for i in range(2, ctx.getChildCount(), 2):  # Skip operator, start from first right-hand operand
            op = ctx.getChild(i - 1).getText()
            right_expr = ctx.unaryExpression(i // 2)
            if right_expr:  # Check if the right-hand side exists
                right = self.visit(right_expr)
                left = BinaryOpNode(left, op, right)
        
        return left



    def visitUnaryExpression(self, ctx:GrammarParser.UnaryExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())
        else:
            op = ctx.getChild(0).getText()
            expr = self.visit(ctx.unaryExpression())
            return UnaryOpNode(op, expr)

    def visitPrimary(self, ctx:GrammarParser.PrimaryContext):
        # This handles both NUMBER and '(' expressionSequence ')' cases
        if ctx.NUMBER() is not None:
            return NumberNode(int(ctx.NUMBER().getText()))
        else:
            return self.visit(ctx.expressionSequence())

    def visitAtom(self, ctx:GrammarParser.AtomContext):
        # Depending on how 'atom' is used in your grammar, adjust this method.
        # If 'atom' directly maps to 'primary' in your use case, you can either handle it similarly
        # to 'visitPrimary' or redirect to the appropriate context method if it's a distinct case.
        return self.visit(ctx.primary())  # Adjust based on actual usage in grammar
