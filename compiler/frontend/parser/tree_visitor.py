from antlr4 import *

from compiler.frontend.antlr_files.GrammarParser import GrammarParser
from compiler.frontend.antlr_files.GrammarVisitor import GrammarVisitor
from compiler.core import ast


class TreeVisitor(GrammarVisitor):
    def visitProgram(self, ctx) -> ast.Program:
        statements = []

        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            statement = self.visit(child)
            statements.append(statement)
        return ast.Program(
            statements=statements
        )

    def visitMainFunction(self, ctx):
        body = self.visit(ctx.body())

        return ast.FunctionDeclaration(
            return_type=ast.Type(base_type=ast.BaseType.int),
            name='main',
            body=body
        )

    def visitBody(self, ctx):
        statements = []

        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            if isinstance(child, GrammarParser.VariableDeclarationContext):
                statement = self.visitVariableDeclaration(child)
            elif isinstance(child, GrammarParser.ExpressionStatementContext):
                statement = self.visitExpressionStatement(child)
            else:
                statement = self.visit(child)
            statements.append(statement)

        return ast.Body(
            statements=statements
        )

    def visitVariableDeclaration(self, ctx):
        var_type = self.visit(ctx.type_())
        qualifiers = self.visit(ctx.variableDeclarationQualifiers())

        return ast.VariableDeclaration(
            var_type=var_type,
            qualifiers=qualifiers
        )

    def visitExpressionStatement(self, ctx):
        return self.visit(ctx.expression())

    def visitType(self, ctx):
        return ast.Type(
            base_type=self.visit(ctx.baseType()),
            const=ctx.const(),
            address_qualifiers=[self.visitAddressQualifier(qualifier) for qualifier in ctx.addressQualifier()]
        )

    def visitAddressQualifier(self, ctx:GrammarParser.AddressQualifierContext):
        text = ctx.getText()
        return ast.AddressQualifier(text)

    def visitBaseType(self, ctx):
        text = ctx.getText()
        return ast.BaseType(text)

    def visitExpression(self, ctx: GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)

    def visitVariableDeclarationQualifiers(self, ctx):
        return [self.visit(qualifier) for qualifier in ctx.variableDeclarationQualifier()]

    def visitVariableDeclarationQualifier(self, ctx):
        identifier = ctx.ID().getText()
        initializer = self.visit(ctx.expression()) if ctx.expression() else None
        return ast.VariableDeclarationQualifier(identifier=identifier, initializer=initializer)

    def visitCastExpression(self, ctx):
        cast_type = self.visit(ctx.type_())
        expression = self.visit(ctx.unaryExpression())
        return ast.TypeCastExpression(cast_type=cast_type, expression=expression)

    def visitAssignmentExpression(self, ctx):
        if ctx.logicalExpression():
            return self.visit(ctx.logicalExpression())

        identifier = ctx.ID()
        expression = self.visit(ctx.expression())
        return ast.AssignmentStatement(
            identifier=identifier,
            value=expression
        )

    def visitLogicalExpression(self, ctx: GrammarParser.LogicalExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        return ast.BinaryLogicalOperation(
            left=left,
            operator=ast.BinaryLogicalOperation.Operator(op),
            right=right
        )

    def visitComparisonExpression(self, ctx: GrammarParser.ComparisonExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        return ast.ComparisonOperation(
            left=left,
            operator=ast.ComparisonOperation.Operator(op),
            right=right
        )

    def visitAdditiveExpression(self, ctx: GrammarParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        return ast.BinaryArithmetic(
            left=left,
            operator=ast.BinaryArithmetic.Operator(op),
            right=right
        )

    def visitMultiplicativeExpression(self, ctx: GrammarParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        return ast.BinaryArithmetic(
            left=left,
            operator=ast.BinaryArithmetic.Operator(op),
            right=right
        )

    def visitBitwiseExpression(self, ctx: GrammarParser.BitwiseExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()

        return ast.BinaryBitwiseArithmetic(
            left=left,
            operator=ast.BinaryBitwiseArithmetic.Operator(op),
            right=right
        )

    def visitShiftExpression(self, ctx: GrammarParser.ShiftExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unaryExpression())

        value = self.visit(ctx.shiftExpression())
        amount = self.visit(ctx.unaryExpression())
        op = ctx.getChild(1).getText()

        return ast.ShiftExpression(
            value=value,
            operator=ast.ShiftExpression.Operator(op),
            amount=amount
        )

    def visitUnaryExpression(self, ctx: GrammarParser.UnaryExpressionContext):
        if ctx.primary():
            return self.visit(ctx.primary())

        expr = self.visit(ctx.unaryExpression())
        op = ctx.getChild(0).getText()
        operator = ast.UnaryExpression.Operator(op)
        return ast.UnaryExpression(
            value=expr,
            operator=operator,
            prefix=op not in ['++', '--']
        )

    @staticmethod
    def process_char_escape(char_esc):
        if char_esc == '\\n':
            return '\n'
        elif char_esc == '\\t':
            return '\t'
        elif char_esc == '\\0':
            return '\0'
        else:
            return char_esc

    def visitPrimary(self, ctx: GrammarParser.PrimaryContext):
        if ctx.NUMBER() is not None:
            return ast.INT(int(ctx.NUMBER().getText()))
        elif ctx.expression() is not None:
            return self.visit(ctx.expression())
        elif ctx.FLOAT() is not None:
            return ast.FLOAT(float(ctx.FLOAT().getText()))
        elif ctx.CHAR() is not None:
            return ast.CHAR(ctx.CHAR().getText()[1:-1])  # Remove the surrounding single quotes
        elif ctx.CHAR_ESC() is not None:
            return ast.CHAR(self.process_char_escape(ctx.CHAR_ESC().getText()[1:-1]))
        elif ctx.ID() is not None:
            return ast.IDENTIFIER(ctx.ID().getText())
        elif ctx.castExpression() is not None:
            return self.visit(ctx.castExpression())
