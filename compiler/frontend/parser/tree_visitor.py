from antlr4 import *
import copy

from antlr4.tree.Tree import TerminalNodeImpl

from compiler.core.errors.semantic_error import SemanticError
from compiler.frontend.antlr_files.GrammarParser import GrammarParser
from compiler.frontend.antlr_files.GrammarVisitor import GrammarVisitor
from compiler.core import ast


class TreeVisitor(GrammarVisitor):
    def __init__(self, input_stream: InputStream):
        self.typedef_scope: dict[str, ast.Type] = {
            "float": ast.Type(base_type=ast.BaseType.float),
            "int": ast.Type(base_type=ast.BaseType.int),
            "char": ast.Type(base_type=ast.BaseType.char)
        }
        self.input_stream = input_stream

    def get_original_text(self, ctx):
        return self.input_stream.getText(ctx.start.start, ctx.stop.stop)

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
    
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        if ctx.getChild(0) == TerminalNodeImpl:
            return None
        ast = super().visitStatement(ctx)
        if ast is not None:
            ast.c_syntax = self.get_original_text(ctx)
        return ast

    def visitVariableDeclaration(self, ctx):
        var_type = self.visit(ctx.type_())
        qualifiers = self.visit(ctx.variableDeclarationQualifiers())

        return ast.VariableDeclaration(
            var_type=var_type,
            qualifiers=qualifiers,
            line=ctx.start.line,
            position=ctx.start.column,
            c_syntax=self.get_original_text(ctx)
        )

    def visitExpressionStatement(self, ctx: GrammarParser.ExpressionStatementContext):
        return ast.ExpressionStatement(
            expression=self.visitExpression(ctx.expression()),
            line=ctx.start.line,
            position=ctx.start.column,
            c_syntax=self.get_original_text(ctx)
        )

    def visitType(self, ctx):
        if ctx.baseType():
            return ast.Type(
                base_type=ast.BaseType((ctx.baseType().getText())),
                const=ctx.const() is not None,
                address_qualifiers=[self.visitAddressQualifier(qualifier) for qualifier in ctx.addressQualifier()],
                line=ctx.start.line,
                position=ctx.start.column
            )
        replace = copy.deepcopy(self.typedef_scope.get(ctx.ID().getText()))
        replace.const = replace.const or ctx.const() is not None
        replace.address_qualifiers += [self.visitAddressQualifier(qualifier) for qualifier in ctx.addressQualifier()]
        replace.line=ctx.start.line
        replace.position=ctx.start.column
        return replace

    def visitAddressQualifier(self, ctx:GrammarParser.AddressQualifierContext):
        text = ctx.getText()
        return ast.AddressQualifier(text)

    def visitTypedefStatement(self, ctx:GrammarParser.TypedefStatementContext):
        my_type = self.visitType(ctx.type_())
        name = ctx.ID().getText()
        if name in self.typedef_scope:
            raise SemanticError(
                f"Typedef redefinition: {name} already defined",
                line=ctx.start.line,
                position=ctx.start.column
            )
        self.typedef_scope[name] = my_type

    def visitExpression(self, ctx: GrammarParser.ExpressionContext):
        ast = self.visitChildren(ctx)
        ast.c_syntax = self.get_original_text(ctx)
        return ast

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
            if ctx.getChild(1):
                op = ast.UnaryExpression.Operator(ctx.getChild(1).getText())
                return ast.UnaryExpression(
                    value=self.visit(ctx.primary()),
                    operator=op,
                    prefix=False,
                    line=ctx.start.line,
                    position=ctx.start.column
                )
            return self.visit(ctx.primary())

        expr = self.visit(ctx.unaryExpression())
        op = ctx.getChild(0).getText()
        operator = ast.UnaryExpression.Operator(op)

        return ast.UnaryExpression(
            value=expr,
            operator=operator,
            prefix=True,
            line=ctx.start.line,
            position=ctx.start.column
        )

    @staticmethod
    def remove_dashes(input):
        out = input[1:-1].replace("\\n", "\n").replace("\\t", "\t").replace("\\0", "\0")
        return out

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
            content=ctx.getText()[:-1],
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

    def visitIfStatement(self, ctx: GrammarParser.IfStatementContext):
        condition = self.visit(ctx.expression())
        body = self.visit(ctx.body())
        else_statement = None

        if ctx.elseStatement():
            else_statement = self.visitElseStatement(ctx.elseStatement())


        return ast.IfStatement(
            condition=condition,
            body=body,
            else_statement=else_statement,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitElseStatement(self, ctx: GrammarParser.ElseStatementContext):
        if ctx.body():
            body = self.visit(ctx.body())

            return ast.ElseStatement(
                body=body,
                line=ctx.start.line,
                position=ctx.start.column
            )
        elif ctx.ifStatement():
            if_statement = self.visitIfStatement(ctx.ifStatement())
            return ast.IfStatement(
                condition=if_statement.condition,
                body=if_statement.body,
                else_statement=if_statement.else_statement,
                line=ctx.start.line,
                position=ctx.start.column
            )

    def visitSwitchStatement(self, ctx:GrammarParser.SwitchStatementContext):
        switch_expression = self.visit(ctx.expression())
        cases = ctx.caseStatement()
        default_case = ctx.defaultCaseStatement()

        switch_if_statements = []

        last_if_statement = None

        # Cases
        for case in cases:
            case_expression = self.visit(case.expression())
            case_body_list = [self.visit(stmt) for stmt in case.statement()]

            case_body = ast.Body(
                statements=case_body_list,
                line=case.start.line,
                position=case.start.column
            )

            condition = ast.ComparisonOperation(
                left=switch_expression,
                operator=ast.ComparisonOperation.Operator.EQ,
                right=case_expression,
                line=case.start.line,
                position=case.start.column
            )

            has_break = False
            for stmt in list(case_body.statements):
                if isinstance(stmt, ast.BreakStatement):
                    case_body.statements.remove(stmt)
                    has_break = True

            if_statement = ast.IfStatement(
                condition=condition,
                body=case_body,
                else_statement=None,
                line=case.start.line,
                position=case.start.column
            )

            if has_break:
                # Add the new if to the deepest else of the last if in switch_if_statements
                if last_if_statement:
                    last_if_statement.else_statement = if_statement
                switch_if_statements.append(if_statement)
                last_if_statement = if_statement
            else:
                # If there is no break, we fall through to this case
                # If there's a previous if statement, attach this if statement as its else_statement
                if last_if_statement:
                    last_if_statement.else_statement = if_statement
                else:
                    # If this is the first case, simply add it to the list
                    switch_if_statements.append(if_statement)
                last_if_statement = None  # Reset last_if_statement since we don't want to attach anything to this block's else

        # Default case
        if default_case:
            default_body_list = [self.visit(stmt) for stmt in default_case.statement()]
            default_statement = ast.ElseStatement(
                body=ast.Body(
                    statements=default_body_list,
                    line=default_case.start.line,
                    position=default_case.start.column
                ),
                line=default_case.start.line,
                position=default_case.start.column
            )
            if last_if_statement:
                last_if_statement.else_statement = default_statement
            else:
                # If no if statements, the default statement is the body
                switch_if_statements.append(default_statement)

        return ast.Body(
            statements=switch_if_statements,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitIterationStatement(self, ctx:GrammarParser.IterationStatementContext):
        if ctx.WHILE():
            return self.visit_while_statement(ctx)
        else:
            return self.visit_for_statement(ctx)

    def visit_while_statement(self, ctx:GrammarParser.IterationStatementContext):
        expression = self.visit(ctx.expression())
        to_execute = self.visit(ctx.statement())
        return ast.WhileStatement(
            expression=expression,
            to_execute=to_execute,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitForFirst(self, ctx:GrammarParser.ForFirstContext):
        if node := ctx.variableDeclaration():
            return self.visitVariableDeclaration(node)
        elif node := ctx.expressionStatement():
            return self.visitExpressionStatement(node)
        elif node := ctx.assignmentStatement():
            return self.visitAssignmentStatement(node)
        return None

    def visitForSecond(self, ctx:GrammarParser.ForSecondContext):
        if node := ctx.expressionStatement():
            expression = self.visitExpressionStatement(node).expression
            expression.c_syntax = self.get_original_text(ctx)
            return expression
        return None

    def visitForThird(self, ctx:GrammarParser.ForThirdContext):
        if node := ctx.expression():
            expr = self.visitExpression(node)
            return ast.ExpressionStatement(
                expression=expr,
                line=ctx.start.line,
                position=ctx.start.column,
                c_syntax=expr.c_syntax
            )
        return None

    def visitForCondition(self, ctx:GrammarParser.ForConditionContext):
        return self.visitForFirst(ctx.forFirst()), self.visitForSecond(ctx.forSecond()), self.visitForThird(ctx.forThird())

    def visit_for_statement(self, ctx: GrammarParser.IterationStatementContext):
        first, second, third = self.visitForCondition(ctx.forCondition())
        statement = self.visitStatement(ctx.statement())

        if third:
            if isinstance(statement, ast.Body):
                statement.statements.append(third)
                to_execute = statement
            else:
                to_execute = ast.Body(
                    statements=[
                        statement,
                        third
                    ],
                    line=ctx.start.line,
                    position=ctx.start.column
                )
        else:
            to_execute = statement

        while_statement = ast.WhileStatement(
            expression=second if second else ast.INT(1),
            to_execute=to_execute,
            line=ctx.start.line,
            position=ctx.start.column
        )

        if not first:
            return while_statement
        return ast.Body(
            statements=[
                first,
                while_statement
            ],
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitBreakStatement(self, ctx:GrammarParser.BreakStatementContext):
        return ast.BreakStatement(
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitContinueStatement(self, ctx:GrammarParser.ContinueStatementContext):
        return ast.ContinueStatement(
            line=ctx.start.line,
            position=ctx.start.column
        )
