from antlr4 import *
import copy

from compiler.frontend.antlr_files.GrammarParser import GrammarParser
from compiler.frontend.antlr_files.GrammarVisitor import GrammarVisitor
from compiler.core import ast


class TreeVisitor(GrammarVisitor):
    def __init__(self):
        self.typedef_scope: dict[str, ast.BaseType] = {}

    def visitProgram(self, ctx) -> ast.Program:
        statements = []

        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            statement = self.visit(child)
            if statement is None:
                continue
            statements.append(statement)

        return ast.Program(
            statements=statements,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitMainFunction(self, ctx):
        body = self.visit(ctx.body())

        return ast.FunctionDeclaration(
            return_type=ast.Type(base_type=ast.BaseType.int),
            name='main',
            body=body,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitBody(self, ctx):
        typedef_scope_before = copy.deepcopy(self.typedef_scope)
        statements = []

        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            statement = self.visit(child)
            if statement is None:
                continue
            statements.append(statement)

        self.typedef_scope = typedef_scope_before

        return ast.Body(
            statements=statements,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitVariableDeclaration(self, ctx):
        var_type = self.visit(ctx.type_())
        qualifiers = self.visit(ctx.variableDeclarationQualifiers())

        return ast.VariableDeclaration(
            var_type=var_type,
            qualifiers=qualifiers,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitExpressionStatement(self, ctx: GrammarParser.ExpressionStatementContext):
        return ast.ExpressionStatement(
            expression=self.visitExpression(ctx.expression()),
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitType(self, ctx):
        return ast.Type(
            base_type=self.visit(ctx.baseType()),
            const=ctx.const() is not None,
            address_qualifiers=[self.visitAddressQualifier(qualifier) for qualifier in ctx.addressQualifier()],
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitAddressQualifier(self, ctx:GrammarParser.AddressQualifierContext):
        text = ctx.getText()
        return ast.AddressQualifier(text)

    def visitTypedefStatement(self, ctx:GrammarParser.TypedefStatementContext):
        base_type = self.visitBaseType(ctx.baseType())
        name = ctx.ID().getText()
        self.typedef_scope[name] = base_type

    def visitBaseType(self, ctx):
        if ctx.ID():
            text = ctx.ID().getText()
            if text in self.typedef_scope:
                return self.typedef_scope[text]
            else:
                raise RuntimeError("Typedef not defined")
        text = ctx.getText()
        return ast.BaseType(text)

    def visitExpression(self, ctx: GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)

    def visitVariableDeclarationQualifiers(self, ctx):
        return [self.visit(qualifier) for qualifier in ctx.variableDeclarationQualifier()]

    def visitVariableDeclarationQualifier(self, ctx):
        identifier = ctx.ID().getText()
        initializer = self.visit(ctx.expression()) if ctx.expression() else None

        return ast.VariableDeclarationQualifier(
            identifier=identifier,
            initializer=initializer,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitCastExpression(self, ctx):
        cast_type = self.visit(ctx.type_())
        expression = self.visit(ctx.unaryExpression())

        return ast.TypeCastExpression(
            cast_type=cast_type,
            expression=expression,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitAssignmentStatement(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))

        return ast.AssignmentStatement(
            left=left,
            right=right,
            line=ctx.start.line,
            position=ctx.start.column
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
            right=right,
            line=ctx.start.line,
            position=ctx.start.column
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
            right=right,
            line=ctx.start.line,
            position=ctx.start.column
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
            right=right,
            line=ctx.start.line,
            position=ctx.start.column
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
            right=right,
            line=ctx.start.line,
            position=ctx.start.column
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
            right=right,
            line=ctx.start.line,
            position=ctx.start.column
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
            amount=amount,
            line=ctx.start.line,
            position=ctx.start.column
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
            prefix=op not in ['++', '--'],
            line=ctx.start.line,
            position=ctx.start.column
        )

    @staticmethod
    def remove_dashes(input):
        return input[1:-1]

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
            return ast.CHAR(self.remove_dashes(ctx.CHAR_ESC().getText()), line=line, position=position)
        elif ctx.ID() is not None:
            return ast.IDENTIFIER(ctx.ID().getText(), line=line, position=position)
        elif ctx.castExpression() is not None:
            return self.visit(ctx.castExpression())

    def visitComment(self, ctx:GrammarParser.CommentContext):
        return ast.CommentStatement(
            content=ctx.getText(),
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitPrintCall(self, ctx:GrammarParser.PrintCallContext):
        return ast.PrintFCall(
            replacer=ast.PrintFCall.Replacer(self.remove_dashes(ctx.PRINTFREPLACER().getText())),
            expression=self.visitLogicalExpression(ctx.logicalExpression()),
            line=ctx.start.line,
            position=ctx.start.column
        )
