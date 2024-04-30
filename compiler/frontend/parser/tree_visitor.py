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
            "float": ast.Type(type=ast.BaseType.float),
            "int": ast.Type(type=ast.BaseType.int),
            "char": ast.Type(type=ast.BaseType.char)
        }
        self.enum_scope: dict[str, dict[str, int]] = {}
        self.input_stream = input_stream
        self.function_decl = None
        self.current_scope = None

    def get_original_text(self, ctx):
        return self.input_stream.getText(ctx.start.start, ctx.stop.stop)

    def visitProgram(self, ctx) -> ast.Program:
        statements = []
        self.current_scope = statements

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

    def visitBody(self, ctx):
        typedef_scope_before = copy.deepcopy(self.typedef_scope)
        prev_enum_scope = copy.deepcopy(self.enum_scope)
        prev_scope = self.current_scope
        statements = []
        self.current_scope = statements
        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            statement = self.visit(child)
            if statement is None:
                continue
            statements.append(statement)

        self.typedef_scope = typedef_scope_before
        self.current_scope = prev_scope
        self.enum_scope = prev_enum_scope
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
                type=ast.BaseType((ctx.baseType().getText())),
                const=ctx.const() is not None,
                address_qualifiers=[self.visitAddressQualifier(qualifier) for qualifier in ctx.addressQualifier()],
                line=ctx.start.line,
                position=ctx.start.column
            )
        elif ctx.enumType():
            enum_type_name = ctx.enumType().ID().getText()

            # Check if the enum type is already declared
            if enum_type_name not in self.enum_scope:
                raise SemanticError(
                    f"Enum type '{enum_type_name}' is not declared.",
                    line=ctx.start.line,
                    position=ctx.start.column
                )

            const_qualifier = ctx.const() is not None
            address_qualifiers = [self.visitAddressQualifier(qualifier) for qualifier in ctx.addressQualifier()]
            return ast.Type(
                type=ast.BaseType.int,  # Enum types are treated as integers
                const=const_qualifier,
                address_qualifiers=address_qualifiers,
                line=ctx.start.line,
                position=ctx.start.column
            )
        else:
            # Handle typedef replacements
            typedef_name = ctx.ID().getText()
            replace = copy.deepcopy(self.typedef_scope.get(typedef_name))
            replace.const = replace.const or ctx.const() is not None
            replace.address_qualifiers += [self.visitAddressQualifier(qualifier) for qualifier in
                                           ctx.addressQualifier()]
            replace.line = ctx.start.line
            replace.position = ctx.start.column
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
    
    def visitVariableDeclaration(self, ctx):
        var_type = self.visit(ctx.type_())
        qualifiers = self.visit(ctx.variableDeclarationQualifiers())

        # Check if the type needs to be changed to an array type
        for qualifier in qualifiers:
            if qualifier.array_specifier:
                array_size = ast.INT(value=len(qualifier.initializer.elements)) if qualifier.initializer else ast.INT(value=0)
                array_type = ast.ArrayType(
                    element_type=var_type,
                    array_sizes=qualifier.array_specifier if qualifier.array_specifier.sizes else ast.ArraySpecifier(sizes=[array_size]),
                    line=ctx.start.line, position=ctx.start.column
                )
                qualifier.array_specifier = None # We can remove the qualifier since we have it in the array type
                #qualifiers.remove(qualifier)
                var_type = ast.Type(
                    type=array_type,
                    const=var_type.const,
                    address_qualifiers=[],
                    line=ctx.start.line,
                    position=ctx.start.column
                )

        return ast.VariableDeclaration(
            var_type=var_type,
            qualifiers=qualifiers,
            line=ctx.start.line,
            position=ctx.start.column,
            c_syntax=self.get_original_text(ctx)
        )

    def visitVariableDeclarationQualifiers(self, ctx):
        return [self.visit(qualifier) for qualifier in ctx.variableDeclarationQualifier()]

    def visitVariableDeclarationQualifier(self, ctx):
        identifier = ctx.ID().getText()
        array_specifier = self.visit(ctx.arraySpecifier()) if ctx.arraySpecifier() else None
        initializer = self.visit(ctx.expression()) if ctx.expression() else None

        return ast.VariableDeclarationQualifier(
            identifier=identifier,
            array_specifier=array_specifier,
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
        elif ctx.FLOAT() is not None:
            return ast.FLOAT(float(ctx.FLOAT().getText()), line=line, position=position)
        elif ctx.CHAR() is not None:
            return ast.CHAR(ctx.CHAR().getText()[1:-1], line=line, position=position)  # Remove the surrounding single quotes
        elif ctx.CHAR_ESC() is not None:
            return ast.CHAR(self.remove_dashes(ctx.CHAR_ESC().getText()), line=line, position=position)
        elif ctx.ID() is not None:
            identifier = ctx.ID().getText()
            if ctx.arraySpecifier():  # This checks for the optional array access
                array_access = self.visitArraySpecifier(ctx.arraySpecifier())
                return ast.ArrayAccess(array_name=identifier, index=array_access, line=line, position=position)
            else:
                return ast.IDENTIFIER(name=identifier, line=line, position=position)
        elif ctx.expression() is not None:
            return self.visit(ctx.expression())
        elif ctx.arrayInitializer() is not None:
            return self.visitArrayInitializer(ctx.arrayInitializer())
        elif ctx.castExpression() is not None:
            return self.visit(ctx.castExpression())
        elif ctx.printfCall():
            return self.visitPrintfCall(ctx.printfCall())
        elif ctx.functionCall():
            return self.visitFunctionCall(ctx.functionCall())
        elif ctx.STRING_LITERAL():
            string = ctx.STRING_LITERAL().getText()
            # Zero terminate the string
            string = string[1:-1] + "\0"
            return ast.ArrayInitializer(elements=[ast.CHAR(char, line=line, position=position) for char in string], line=line, position=position)

    def visitComment(self, ctx:GrammarParser.CommentContext):
        return ast.CommentStatement(
            content=ctx.getText()[:-1],
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
                else:
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

    def visitTypedIdentifier(self, ctx:GrammarParser.TypedIdentifierContext):
        identifier = ctx.ID().getText()
        type_ = self.visitType(ctx.type_())
        if ctx.arraySpecifier():
            array_specifier = self.visitArraySpecifier(ctx.arraySpecifier())
            array_type = ast.ArrayType(
                element_type=type_,
                array_sizes=array_specifier,
                line=ctx.start.line,
                position=ctx.start.column
            )
            return ast.Type(
                type=array_type,
                const=type_.const,
                address_qualifiers=[],
                line=ctx.start.line,
                position=ctx.start.column
            ), identifier
        return type_, identifier


    def visitParamList(self, ctx:GrammarParser.ParamListContext):
        params = []
        for i in range(len(ctx.typedIdentifier())):  # This is done to match the type with the name
            param_type, param_name = self.visitTypedIdentifier(ctx.typedIdentifier(i))

            params.append(ast.FunctionParameter(
                type=param_type,
                name=param_name
            ))
        return params

    def visitPrintfCall(self, ctx:GrammarParser.PrintfCallContext):
        return ast.PrintFCall(
            replacer=ast.PrintFCall.Replacer(self.remove_dashes(ctx.PRINTFREPLACER().getText())),
            expression=self.visitExpression(ctx.expression()),
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitFunctionDeclaration(self, ctx: GrammarParser.FunctionDeclarationContext):
        return_type = self.visit(ctx.type_())
        name = ctx.ID().getText()
        parameters = self.visitParamList(ctx.paramList()) if ctx.paramList() else []

        func_declaration = ast.FunctionDeclaration(
            return_type=return_type,
            name=name,
            parameters=parameters,
            body=ast.Body(statements=[]),
            line=ctx.start.line,
            position=ctx.start.column
        )
        decl_b4 = copy.deepcopy(self.function_decl)
        self.function_decl = func_declaration
        func_declaration.body = self.visit(ctx.body())
        self.function_decl = decl_b4
        return func_declaration

    def visitReturnStatement(self, ctx:GrammarParser.ReturnStatementContext):
        if self.function_decl is None:
            raise SemanticError(
                "Return statement outside of function",
                line=ctx.start.line,
                position=ctx.start.column
            )
        return ast.ReturnStatement(
            function=self.function_decl,
            expression=self.visit(ctx.expression()) if ctx.expression() else None,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitArgumentList(self, ctx:GrammarParser.ArgumentListContext):
        return [self.visitExpression(arg) for arg in ctx.expression()]

    def visitFunctionCall(self, ctx: GrammarParser.FunctionCallContext):
        name = ctx.ID().getText()
        arguments = self.visitArgumentList(ctx.argumentList()) if ctx.argumentList() else []
        return ast.FunctionCall(
            name=name,
            arguments=arguments,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitTypeList(self, ctx:GrammarParser.TypeListContext):
        return [self.visitType(type_) for type_ in ctx.type_()]

    def visitForwardDeclaration(self, ctx:GrammarParser.ForwardDeclarationContext):
        type_fwd, name_fwd = self.visitTypedIdentifier(ctx.typedIdentifier())
        return ast.ForwardDeclaration(
            return_type=type_fwd,
            name=name_fwd,
            parameters=self.visitTypeList(ctx.typeList()) if ctx.typeList() else [],
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitArraySpecifier(self, ctx: GrammarParser.ArraySpecifierContext):
        sizes = [self.visitExpression(size) for size in ctx.expression()]
        return ast.ArraySpecifier(
            sizes=sizes,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitArrayInitializer(self, ctx: GrammarParser.ArrayInitializerContext):
        elements = []
        for child in ctx.children:
            if isinstance(child, GrammarParser.ArrayInitializerContext):
                elements.append(self.visitArrayInitializer(child))
            elif isinstance(child, GrammarParser.ExpressionContext):
                elements.append(self.visit(child))

        return ast.ArrayInitializer(elements=elements, line=ctx.start.line, position=ctx.start.column)
    
    def visitEnumDeclaration(self, ctx):
        name = ctx.ID().getText() if ctx.ID() else None
        enumerators = self.visitEnumBody(ctx.enumBody())
        const_int_declarations = []

        # Create a dictionary to store the enum values
        enum_values = {}
        value = 0  # Default start value for enums
        for enumerator in enumerators:
            const_int_declaration = ast.VariableDeclaration(
                var_type=ast.Type(type=ast.BaseType.int, const=True),
                qualifiers=[ast.VariableDeclarationQualifier(
                    identifier=enumerator,
                    initializer=ast.INT(value=value)
                )]
            )
            const_int_declarations.append(const_int_declaration)

            enum_values[enumerator] = value
            value += 1  # Increment for the next enum value

        # Add the enum type and its values to the enum_scope dictionary
        self.enum_scope[name] = enum_values

        self.current_scope.extend(const_int_declarations)
        return None

    def visitEnumBody(self, ctx):
        enumerators = []
        for enumList in ctx.enumList():
            enumerators.extend(self.visitEnumList(enumList))
        return enumerators

    def visitEnumList(self, ctx):
        enumerators = []
        for enumerator in ctx.ID():
            enumerators.append(enumerator.getText())
        return enumerators
