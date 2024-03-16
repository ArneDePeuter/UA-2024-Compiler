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

        line = ctx.start.line
        position = ctx.start.column

        return ast.Program(
            statements=statements,
            line=line, position=position
        )

    def visitMainFunction(self, ctx):
        body = self.visit(ctx.body())

        line = ctx.start.line
        position = ctx.start.column

        return ast.FunctionDeclaration(
            return_type=ast.Type(base_type=ast.BaseType.int),
            name='main',
            body=body,
            line=line, position=position
        )

    def visitBody(self, ctx):
        statements = []

        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            statement = self.visit(child)
            statements.append(statement)

        line = ctx.start.line
        position = ctx.start.column

        return ast.Body(
            statements=statements,
            line=line, position=position
        )

    def visitVariableDeclaration(self, ctx):
        var_type = self.visit(ctx.type_())
        qualifiers = self.visit(ctx.variableDeclarationQualifiers())

        line = ctx.start.line
        position = ctx.start.column

        return ast.VariableDeclaration(
            var_type=var_type,
            qualifiers=qualifiers,
            line=line, position=position
        )

    def visitExpressionStatement(self, ctx: GrammarParser.ExpressionStatementContext):
        line = ctx.start.line
        position = ctx.start.column

        return ast.ExpressionStatement(
            expression=self.visitExpression(ctx.expression()),
            line=line, position=position
        )

    def visitType(self, ctx):
        line = ctx.start.line
        position = ctx.start.column

        return ast.Type(
            base_type=self.visit(ctx.baseType()),
            const=ctx.const(),
            address_qualifiers=[self.visitAddressQualifier(qualifier) for qualifier in ctx.addressQualifier()],
            line=line, position=position
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

        line = ctx.start.line
        position = ctx.start.column

        return ast.VariableDeclarationQualifier(identifier=identifier, initializer=initializer, line=line, position=position)

    def visitCastExpression(self, ctx):
        cast_type = self.visit(ctx.type_())
        expression = self.visit(ctx.unaryExpression())

        line = ctx.start.line
        position = ctx.start.column

        return ast.TypeCastExpression(cast_type=cast_type, expression=expression, line=line, position=position)

    def visitAssignmentStatement(self, ctx):
        identifier = ctx.ID()
        expression = self.visit(ctx.expression())

        line = ctx.start.line
        position = ctx.start.column

        return ast.AssignmentStatement(
            identifier=identifier,
            value=expression,
            address_qualifiers=[self.visitAddressQualifier(qualifier) for qualifier in ctx.addressQualifier()],
            line=line, position=position
        )

    def visitLogicalExpression(self, ctx: GrammarParser.LogicalExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()

        line = ctx.start.line
        position = ctx.start.column

        return ast.BinaryLogicalOperation(
            left=left,
            operator=ast.BinaryLogicalOperation.Operator(op),
            right=right,
            line=line, position=position
        )

    def visitComparisonExpression(self, ctx: GrammarParser.ComparisonExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()

        line = ctx.start.line
        position = ctx.start.column

        return ast.ComparisonOperation(
            left=left,
            operator=ast.ComparisonOperation.Operator(op),
            right=right,
            line=line, position=position
        )

    def visitAdditiveExpression(self, ctx: GrammarParser.AdditiveExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()

        line = ctx.start.line
        position = ctx.start.column

        return ast.BinaryArithmetic(
            left=left,
            operator=ast.BinaryArithmetic.Operator(op),
            right=right,
            line=line, position=position
        )

    def visitMultiplicativeExpression(self, ctx: GrammarParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()

        line = ctx.start.line
        position = ctx.start.column

        return ast.BinaryArithmetic(
            left=left,
            operator=ast.BinaryArithmetic.Operator(op),
            right=right,
            line=line, position=position
        )

    def visitBitwiseExpression(self, ctx: GrammarParser.BitwiseExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()

        line = ctx.start.line
        position = ctx.start.column

        return ast.BinaryBitwiseArithmetic(
            left=left,
            operator=ast.BinaryBitwiseArithmetic.Operator(op),
            right=right,
            line=line, position=position
        )

    def visitShiftExpression(self, ctx: GrammarParser.ShiftExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unaryExpression())

        value = self.visit(ctx.shiftExpression())
        amount = self.visit(ctx.unaryExpression())
        op = ctx.getChild(1).getText()

        line = ctx.start.line
        position = ctx.start.column

        return ast.ShiftExpression(
            value=value,
            operator=ast.ShiftExpression.Operator(op),
            amount=amount,
            line=line, position=position
        )

    def visitUnaryExpression(self, ctx: GrammarParser.UnaryExpressionContext):
        if ctx.primary():
            return self.visit(ctx.primary())

        expr = self.visit(ctx.unaryExpression())
        op = ctx.getChild(0).getText()
        operator = ast.UnaryExpression.Operator(op)

        line = ctx.start.line
        position = ctx.start.column

        return ast.UnaryExpression(
            value=expr,
            operator=operator,
            prefix=op not in ['++', '--'],
            line=line, position=position
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
        line = ctx.start.line
        position = ctx.start.column
        if ctx.NUMBER() is not None:
            return ast.INT(int(ctx.NUMBER().getText()), line=line, position=position)
        elif ctx.expression() is not None:
            return self.visit(ctx.expression())
        elif ctx.FLOAT() is not None:
            return ast.FLOAT(float(ctx.FLOAT().getText()), line=line, position=position)
        elif ctx.CHAR() is not None:
            return ast.CHAR(ctx.CHAR().getText()[1:-1], line=line, position=position)  # Remove the surrounding single quotes
        elif ctx.CHAR_ESC() is not None:
            return ast.CHAR(self.process_char_escape(ctx.CHAR_ESC().getText()[1:-1]), line=line, position=position)
        elif ctx.ID() is not None:
            return ast.IDENTIFIER(ctx.ID().getText(), line=line, position=position)
        elif ctx.castExpression() is not None:
            return self.visit(ctx.castExpression())
