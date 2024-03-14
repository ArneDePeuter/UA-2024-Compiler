from antlr4 import *
from src.antlr_files.project_3.MyGrammarParser import MyGrammarParser
from src.antlr_files.project_3.MyGrammarVisitor import MyGrammarVisitor

from src.core.ast import Program
from src.core.ast import MainFunction
from src.core.ast import CompoundStatement
from src.core.ast import Declaration
from src.core.ast import Type
from src.core.ast.variable import Variable
from src.core.ast.comment import Comment

class CSTVisitor(MyGrammarVisitor):
    def visitProgram(self, ctx):
        statements = []

        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            print(f"Child node: {type(child).__name__}")
            statement = self.visit(child)
            print(f"Statement: {statement}")
            statements.append(statement)
        return Program(
            statements=statements
        )

    def visitMainFunction(self, ctx):
        # Visit the compound statement (function body)
        compound_statement = self.visit(ctx.compoundStatement())

        # Create and return the main function AST node
        return MainFunction(
            return_type='int',
            name='main',
            parameters=[],
            body=compound_statement
        )

    def visitCompoundStatement(self, ctx):
        statements = []

        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            if isinstance(child, MyGrammarParser.DeclarationContext):
                statement = self.visitDeclaration(child)
            elif isinstance(child, MyGrammarParser.ExpressionStatementContext):
                statement = self.visitExpressionStatement(child)
            elif isinstance(child, MyGrammarParser.CommentContext):
                statement = self.visitComment(child)
            else:
                statement = self.visit(child)
            statements.append(statement)

        return CompoundStatement(statements=statements)

    def visitComment(self, ctx):
        if ctx.SINGLE_LINE_COMMENT():
            return Comment(ctx.SINGLE_LINE_COMMENT().getText())
        elif ctx.MULTI_LINE_COMMENT():
            return Comment(ctx.MULTI_LINE_COMMENT().getText())

    def visitDeclaration(self, ctx):
        var_type = self.visit(ctx.type_())
        variables = self.visit(ctx.variableList())
        return Declaration(var_type=var_type, variables=variables)

    def visitExpressionStatement(self, ctx):
        return self.visit(ctx.expression())

    def visitType(self, ctx):
        base_type = self.visit(ctx.baseType())
        type_qualifier = self.visit(ctx.typeQualifier()) if ctx.typeQualifier() else None
        pointer_qualifiers = [self.visit(pq) for pq in ctx.pointerQualifier()]
        return Type(base_type=base_type, type_qualifier=type_qualifier, pointer_qualifiers=pointer_qualifiers)

    def visitBaseType(self, ctx):
        return ctx.getText()

    def visitTypeQualifier(self, ctx):
        return ctx.getText()

    def visitPointerQualifier(self, ctx):
        return ctx.getText()

    def visitVariableList(self, ctx):
        variables = [self.visit(variable) for variable in ctx.variable()]
        return variables

    def visitVariable(self, ctx):
        identifier = ctx.ID().getText()
        initializer = self.visit(ctx.expression()) if ctx.expression() else None
        return Variable(identifier=identifier, initializer=initializer)

    def visitCastExpression(self, ctx):
        cast_type = self.visit(ctx.type_())
        expression = self.visit(ctx.unaryExpression())
        return CastExpression(cast_type=cast_type, expression=expression)

    def visitAdditiveExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            if op == "+":
                return BinaryArithmetic(left=left, operator=BinaryArithmetic.Operator.PLUS, right=right)
            elif op == "-":
                return BinaryArithmetic(left=left, operator=BinaryArithmetic.Operator.MINUS, right=right)
            else:
                raise ValueError(f"Unknown additive operator: {op}")

    def visitMultiplicativeExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            if op == "*":
                return BinaryArithmetic(left=left, operator=BinaryArithmetic.Operator.MUL, right=right)
            elif op == "/":
                return BinaryArithmetic(left=left, operator=BinaryArithmetic.Operator.DIV, right=right)
            elif op == "%":
                return BinaryArithmetic(left=left, operator=BinaryArithmetic.Operator.MOD, right=right)
            else:
                raise ValueError(f"Unknown multiplicative operator: {op}")

    def visitAssignmentExpression(self, ctx):
        if ctx.logicalExpression():
            return self.visit(ctx.logicalExpression())
        else:
            left = self.visit(ctx.unaryExpression())
            right = self.visit(ctx.expression())
            op = ctx.assignmentOperator().getText()
            if op == "=":
                return Assignment(left=left, right=right)
            elif op == "+=":
                return BinaryArithmetic(left=left, operator=BinaryArithmetic.Operator.PLUS, right=right)
            elif op == "-=":
                return BinaryArithmetic(left=left, operator=BinaryArithmetic.Operator.MINUS, right=right)
            elif op == "*=":
                return BinaryArithmetic(left=left, operator=BinaryArithmetic.Operator.MUL, right=right)
            elif op == "/=":
                return BinaryArithmetic(left=left, operator=BinaryArithmetic.Operator.DIV, right=right)
            elif op == "%=":
                return BinaryArithmetic(left=left, operator=BinaryArithmetic.Operator.MOD, right=right)
            elif op == "<<=":
                return ShiftExpression(value=left, operator=ShiftExpression.Operator.LEFT, amount=right)
            elif op == ">>=":
                return ShiftExpression(value=left, operator=ShiftExpression.Operator.RIGHT, amount=right)
            elif op == "&=":
                return BinaryBitwiseArithmetic(left=left, operator=BinaryBitwiseArithmetic.Operator.AND, right=right)
            elif op == "^=":
                return BinaryBitwiseArithmetic(left=left, operator=BinaryBitwiseArithmetic.Operator.XOR, right=right)
            elif op == "|=":
                return BinaryBitwiseArithmetic(left=left, operator=BinaryBitwiseArithmetic.Operator.OR, right=right)
            else:
                raise ValueError(f"Unknown assignment operator: {op}")

    def visitLogicalExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            if op == "&&":
                return BinaryLogicalOperation(left=left, operator=BinaryLogicalOperation.Operator.AND, right=right)
            elif op == "||":
                return BinaryLogicalOperation(left=left, operator=BinaryLogicalOperation.Operator.OR, right=right)
            else:
                raise ValueError(f"Unknown logical operator: {op}")

    def visitComparisonExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            op = ctx.getChild(1).getText()
            if op == ">":
                return ComparisonOperation(left=left, operator=ComparisonOperation.Operator.GT, right=right)
            elif op == "<":
                return ComparisonOperation(left=left, operator=ComparisonOperation.Operator.LT, right=right)
            elif op == ">=":
                return ComparisonOperation(left=left, operator=ComparisonOperation.Operator.GTE, right=right)
            elif op == "<=":
                return ComparisonOperation(left=left, operator=ComparisonOperation.Operator.LTE, right=right)
            elif op == "==":
                return ComparisonOperation(left=left, operator=ComparisonOperation.Operator.EQ, right=right)
            elif op == "!=":
                return ComparisonOperation(left=left, operator=ComparisonOperation.Operator.NEQ, right=right)
            else:
                raise ValueError(f"Unknown comparison operator: {op}")

    def visitUnaryExpression(self, ctx: MyGrammarParser.UnaryExpressionContext):
        if ctx.primary():
            return self.visit(ctx.primary())
        elif ctx.unaryExpression():
            expr = self.visit(ctx.unaryExpression())
            if expr is None:
                return None
            op = ctx.getChild(0).getText()
            if op in ['++', '--']:
                # Handle postfix increment/decrement operators
                return UnaryExpression(
                    value=expr,
                    operator=UnaryExpression.Operator(op),
                    prefix=False
                )
            else:
                # Handle prefix operators, including the dereference operator
                op = UnaryExpression.Operator(op)
                return UnaryExpression(
                    value=expr,
                    operator=op,
                    prefix=True
                )
        else:
            raise ValueError("Invalid unary expression")

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

    def visitPrimary(self, ctx: MyGrammarParser.PrimaryContext):
        if ctx.NUMBER() is not None:
            return INT(int(ctx.NUMBER().getText()))
        elif ctx.expression() is not None:
            return self.visit(ctx.expression())
        elif ctx.FLOAT() is not None:
            return FLOAT(float(ctx.FLOAT().getText()))
        elif ctx.CHAR() is not None:
            return CHAR(ctx.CHAR().getText()[1:-1])  # Remove the surrounding single quotes
        elif ctx.CHAR_ESC() is not None:
            return CHAR(self.process_char_escape(ctx.CHAR_ESC().getText()[1:-1]))  # Process the escape sequence
        elif ctx.ID() is not None:
            return VariableReference(ctx.ID().getText())
        elif ctx.castExpression() is not None:
            return self.visit(ctx.castExpression())
        else:
            raise ValueError("Unknown primary expression")

    def process_char_escape(self, char_esc):
        if char_esc == '\\n':
            return '\n'
        elif char_esc == '\\t':
            return '\t'
        elif char_esc == '\\0':
            return '\0'
        else:
            return char_esc
