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
        self.while_statement = None
        self.inside_switch = False
        self.current_scope = None
        self.struct_defintions: dict[str, ast.StructDefinition] = {}

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
        struct_definitions_before = copy.deepcopy(self.struct_defintions)

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
        self.struct_defintions = struct_definitions_before

        return ast.Body(
            statements=statements,
            line=ctx.start.line,
            position=ctx.start.column
        )
    
    def visitStatement(self, ctx: GrammarParser.StatementContext):
        if ctx.Comment():
            return ast.CommentStatement(
                content=ctx.Comment().getText(),
                line=ctx.start.line,
                position=ctx.start.column
            )

        if ctx.getChild(0) == TerminalNodeImpl:
            return None
        new_ast = super().visitStatement(ctx)
        if new_ast is not None:
            new_ast.c_syntax = self.get_original_text(ctx)
        return new_ast

    def visitExpressionStatement(self, ctx: GrammarParser.ExpressionStatementContext):
        return ast.ExpressionStatement(
            expression=self.visitExpression(ctx.expression()),
            line=ctx.start.line,
            position=ctx.start.column,
            c_syntax=self.get_original_text(ctx)
        )

    def visitType(self, ctx):
        if ctx.BaseType():
            return ast.Type(
                type=ast.BaseType((ctx.BaseType().getText())),
                const=ctx.Const() is not None,
                address_qualifiers=[ast.AddressQualifier(addr.getText()) for addr in ctx.Multiply()],
                line=ctx.start.line,
                position=ctx.start.column
            )
        elif ctx.enumType():
            enum_type_name = ctx.enumType().Identifier().getText()

            # Check if the enum type is already declared
            if enum_type_name not in self.enum_scope:
                raise SemanticError(
                    f"Enum type '{enum_type_name}' is not declared.",
                    line=ctx.start.line,
                    position=ctx.start.column
                )

            const_qualifier = ctx.Const() is not None
            address_qualifiers = [ast.AddressQualifier(addr.getText()) for addr in ctx.Multiply()]
            return ast.Type(
                type=ast.BaseType.int,  # Enum types are treated as integers
                const=const_qualifier,
                address_qualifiers=address_qualifiers,
                line=ctx.start.line,
                position=ctx.start.column
            )
        if ctx.structType():
            const_qualifier = ctx.Const() is not None
            address_qualifiers = [ast.AddressQualifier(addr.getText()) for addr in ctx.Multiply()]
            return ast.Type(
                type=self.visitStructType(ctx.structType()),
                const=const_qualifier,
                address_qualifiers=address_qualifiers,
                line=ctx.start.line,
                position=ctx.start.column
            )
        else:
            # Handle typedef replacements
            typedef_name = self.visitTypedefName(ctx.typedefName())
            replace = copy.deepcopy(self.typedef_scope.get(typedef_name))
            if not replace:
                raise SemanticError(f"Typedef with name: {typedef_name} not defined", ctx.start.line, ctx.start.column)
            replace.const = replace.const or ctx.Const() is not None
            replace.address_qualifiers += [ast.AddressQualifier(addr.getText()) for addr in ctx.Multiply()]
            replace.line = ctx.start.line
            replace.position = ctx.start.column
            return replace

    def visitStructType(self, ctx: GrammarParser.StructTypeContext):
        name = ctx.Identifier().getText()
        definition = self.struct_defintions.get(name)
        if not definition:
            raise SemanticError(f"Struct with name: {name} is not defined", ctx.start.line, ctx.start.column)
        return ast.StructType(
            definition=definition
        )

    def visitTypedefStatement(self, ctx: GrammarParser.TypedefStatementContext):
        my_type = self.visitType(ctx.type_())
        name = self.visitTypedefName(ctx.typedefName())
        if name in self.typedef_scope:
            raise SemanticError(
                f"Typedef redefinition: {name} already defined",
                line=ctx.start.line,
                position=ctx.start.column
            )
        self.typedef_scope[name] = my_type

    def visitTypedefName(self, ctx: GrammarParser.TypedefNameContext):
        if ctx.Identifier():
            return ctx.Identifier().getText()
        return ctx.BaseType().getText()

    def visitVariableDeclaration(self, ctx):
        var_type = self.visit(ctx.type_())
        qualifiers = self.visit(ctx.variableDeclarationQualifiers())

        # Check if the type needs to be changed to an array type
        for qualifier in qualifiers:
            if qualifier.array_specifier:
                array_type = ast.ArrayType(
                    element_type=var_type,
                    array_sizes=qualifier.array_specifier,
                    line=ctx.start.line, position=ctx.start.column
                )
                qualifier.array_specifier = None  # We can remove the qualifier since we have it in the array type
                var_type = ast.Type(
                    type=array_type,
                    const=var_type.const,
                    address_qualifiers=[],
                    line=ctx.start.line,
                    position=ctx.start.column
                )

        # Check if the list initializer needs to be interpreted as a struct initializer
        if isinstance(var_type.type, ast.StructType) and len(var_type.address_qualifiers) == 0:
            for qualifier in qualifiers:
                if qualifier.initializer and isinstance(qualifier.initializer, ast.ArrayInitializer):
                    qualifier.initializer.set_struct_type(var_type.type)

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
        identifier = ctx.Identifier().getText()
        array_specifier = self.visit(ctx.arraySpecifier()) if ctx.arraySpecifier() else None
        initializer = self.visit(ctx.expression()) if ctx.expression() else None

        if array_specifier and initializer:
            if len(array_specifier.sizes) < 1:
                dimensions = []
                current_node = initializer
                while current_node is not None:
                    if isinstance(current_node, ast.ArrayInitializer):
                        dimensions.append(len(current_node.elements))
                        current_node = current_node.elements[0]
                    else:
                        current_node = None
                array_specifier.sizes = [ast.INT(value=size) for size in dimensions]


        return ast.VariableDeclarationQualifier(
            identifier=identifier,
            array_specifier=array_specifier,
            initializer=initializer,
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

    def visitSwitchStatement(self, ctx: GrammarParser.SwitchStatementContext):
        prev_inside_switch = copy.deepcopy(self.inside_switch)
        self.inside_switch = True

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

        self.inside_switch = prev_inside_switch

        return ast.Body(
            statements=switch_if_statements,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitIterationStatement(self, ctx: GrammarParser.IterationStatementContext):
        if ctx.While():
            return self.visit_while_statement(ctx)
        else:
            return self.visit_for_statement(ctx)

    def visit_while_statement(self, ctx: GrammarParser.IterationStatementContext):
        expression = self.visit(ctx.expression())

        prev_while = copy.deepcopy(self.while_statement)
        current_while = ast.WhileStatement(
            expression=expression,
            to_execute=None,
            line=ctx.start.line,
            position=ctx.start.column
        )
        self.while_statement = current_while

        to_execute = self.visit(ctx.statement())

        current_while.to_execute = to_execute
        self.while_statement = prev_while
        return current_while

    def visitForFirst(self, ctx: GrammarParser.ForFirstContext):
        if node := ctx.variableDeclaration():
            return self.visitVariableDeclaration(node)
        elif node := ctx.expressionStatement():
            return self.visitExpressionStatement(node)
        elif node := ctx.assignmentStatement():
            return self.visitAssignmentStatement(node)
        return None

    def visitForSecond(self, ctx: GrammarParser.ForSecondContext):
        if node := ctx.expressionStatement():
            expression = self.visitExpressionStatement(node).expression
            expression.c_syntax = self.get_original_text(ctx)
            return expression
        return None

    def visitForThird(self, ctx: GrammarParser.ForThirdContext):
        if node := ctx.expression():
            expr = self.visitExpression(node)
            return ast.ExpressionStatement(
                expression=expr,
                line=ctx.start.line,
                position=ctx.start.column,
                c_syntax=expr.c_syntax
            )
        return None

    def visitForCondition(self, ctx: GrammarParser.ForConditionContext):
        return self.visitForFirst(ctx.forFirst()), self.visitForSecond(ctx.forSecond()), self.visitForThird(ctx.forThird())

    def replace_continues(self, statement, third) -> ast.Statement:
        """
        Make sure that all continue statements are replaced with third and then continue
        :param statement:
        :param third:
        :return:
        """
        if isinstance(statement, ast.ContinueStatement):
            return ast.Body(
                statements=[
                    copy.deepcopy(third),
                    statement
                ],
                line=statement.line,
                position=statement.position
            )
        if isinstance(statement, ast.Body):
            for i, stmt in enumerate(statement.statements):
                statement.statements[i] = self.replace_continues(stmt, third)
            return statement
        if isinstance(statement, ast.IfStatement):
            statement.body = self.replace_continues(statement.body, third)
            if statement.else_statement:
                statement.else_statement = self.replace_continues(statement.else_statement, third)
            return statement
        return statement

    def visit_for_statement(self, ctx: GrammarParser.IterationStatementContext):
        first, second, third = self.visitForCondition(ctx.forCondition())

        prev_while = copy.deepcopy(self.while_statement)
        current_while = ast.WhileStatement(
            expression=second if second else ast.INT(1),
            to_execute=None,
            line=ctx.start.line,
            position=ctx.start.column
        )
        self.while_statement = current_while

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
            to_execute = self.replace_continues(to_execute, third)
        else:
            to_execute = statement

        current_while.to_execute = to_execute
        self.while_statement = prev_while

        if not first:
            return current_while
        return ast.Body(
            statements=[
                first,
                current_while
            ],
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitBreakStatement(self, ctx:GrammarParser.BreakStatementContext):
        if self.while_statement is None and not self.inside_switch:
            raise SemanticError(
                "Break statement outside of loop",
                line=ctx.start.line,
                position=ctx.start.column
            )
        return ast.BreakStatement(
            while_statement=self.while_statement,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitContinueStatement(self, ctx:GrammarParser.ContinueStatementContext):
        if self.while_statement is None:
            raise SemanticError(
                "Continue statement outside of loop",
                line=ctx.start.line,
                position=ctx.start.column
            )
        return ast.ContinueStatement(
            while_statement=self.while_statement,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitTypedIdentifier(self, ctx: GrammarParser.TypedIdentifierContext):
        identifier = ctx.Identifier().getText()
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

    def visitParamList(self, ctx: GrammarParser.ParamListContext):
        params = []
        for i in range(len(ctx.typedIdentifier())):  # This is done to match the type with the name
            param_type, param_name = self.visitTypedIdentifier(ctx.typedIdentifier(i))

            params.append(ast.FunctionParameter(
                type=param_type,
                name=param_name
            ))
        return params

    def visitFunctionDeclaration(self, ctx: GrammarParser.FunctionDeclarationContext):
        return_type = self.visit(ctx.type_())
        name = ctx.Identifier().getText()
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

    def visitArgumentList(self, ctx: GrammarParser.ArgumentExpressionListContext):
        return [self.visitLogicalOrExpression(arg) for arg in ctx.logicalOrExpression()]

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
    
    def visitEnumDeclaration(self, ctx):
        name = ctx.Identifier().getText() if ctx.Identifier() else None
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
        for enumerator in ctx.Identifier():
            enumerators.append(enumerator.getText())
        return enumerators

    def visitStructDefinition(self, ctx: GrammarParser.StructDefinitionContext):
        name = ctx.Identifier().getText()
        struct = ast.StructDefinition(
            name=name,
            members=[],
            line=ctx.start.line,
            position=ctx.start.column
        )

        if name in self.struct_defintions:
            raise SemanticError(
                f"Struct redefinition: {name} already defined",
                line=ctx.start.line,
                position=ctx.start.column
            )

        self.struct_defintions[name] = struct
        struct.members = self.visitStructList(ctx.structList())
        return struct

    def visitStructList(self, ctx: GrammarParser.StructListContext):
        return [
            ast.StructMember(name=name, type=type_)
            for type_, name in (self.visitTypedIdentifier(typed_id) for typed_id in ctx.typedIdentifier())
        ]

    def visitExpression(self, ctx: GrammarParser.ExpressionContext):
        ast = self.visitChildren(ctx)
        ast.c_syntax = self.get_original_text(ctx)
        return ast

    def visitLogicalOrExpression(self, ctx: GrammarParser.LogicalOrExpressionContext):
        current_expr = self.visitLogicalAndExpression(ctx.logicalAndExpression(0))

        for i in range(1, len(ctx.logicalAndExpression())):
            current_expr = ast.BinaryLogicalOperation(
                left=current_expr,
                operator=ast.BinaryLogicalOperation.Operator.OR,
                right=self.visitLogicalAndExpression(ctx.logicalAndExpression(i)),
                line=ctx.start.line,
                position=ctx.start.column
            )
        return current_expr

    def visitLogicalAndExpression(self, ctx: GrammarParser.LogicalAndExpressionContext):
        current_expr = self.visitInclusiveOrExpression(ctx.inclusiveOrExpression(0))

        for i in range(1, len(ctx.inclusiveOrExpression())):
            current_expr = ast.BinaryLogicalOperation(
                left=current_expr,
                operator=ast.BinaryLogicalOperation.Operator.AND,
                right=self.visitInclusiveOrExpression(ctx.inclusiveOrExpression(i)),
                line=ctx.start.line,
                position=ctx.start.column
            )
        return current_expr

    def visitInclusiveOrExpression(self, ctx: GrammarParser.InclusiveOrExpressionContext):
        current_expr = self.visitExclusiveOrExpression(ctx.exclusiveOrExpression(0))

        for i in range(1, len(ctx.exclusiveOrExpression())):
            current_expr = ast.BinaryBitwiseArithmetic(
                left=current_expr,
                operator=ast.BinaryBitwiseArithmetic.Operator.OR,
                right=self.visitExclusiveOrExpression(ctx.exclusiveOrExpression(i)),
                line=ctx.start.line,
                position=ctx.start.column
            )
        return current_expr

    def visitExclusiveOrExpression(self, ctx: GrammarParser.ExclusiveOrExpressionContext):
        current_expr = self.visitAndExpression(ctx.andExpression(0))

        for i in range(1, len(ctx.andExpression())):
            current_expr = ast.BinaryBitwiseArithmetic(
                left=current_expr,
                operator=ast.BinaryBitwiseArithmetic.Operator.XOR,
                right=self.visitAndExpression(ctx.andExpression(i)),
                line=ctx.start.line,
                position=ctx.start.column
            )
        return current_expr

    def visitAndExpression(self, ctx: GrammarParser.AndExpressionContext):
        current_expr = self.visitEqualityExpression(ctx.equalityExpression(0))

        for i in range(1, len(ctx.equalityExpression())):
            current_expr = ast.BinaryBitwiseArithmetic(
                left=current_expr,
                operator=ast.BinaryBitwiseArithmetic.Operator.AND,
                right=self.visitEqualityExpression(ctx.equalityExpression(i)),
                line=ctx.start.line,
                position=ctx.start.column
            )
        return current_expr

    def visitEqualityExpression(self, ctx: GrammarParser.EqualityExpressionContext):
        current_expr = self.visitRelationalExpression(ctx.relationalExpression(0))

        for i in range(1, len(ctx.relationalExpression())):
            current_expr = ast.ComparisonOperation(
                left=current_expr,
                operator=ast.ComparisonOperation.Operator(ctx.getChild(2*i-1).getText()),
                right=self.visitRelationalExpression(ctx.relationalExpression(i)),
                line=ctx.start.line,
                position=ctx.start.column
            )
        return current_expr

    def visitRelationalExpression(self, ctx: GrammarParser.RelationalExpressionContext):
        current_expr = self.visitShiftExpression(ctx.shiftExpression(0))

        for i in range(1, len(ctx.shiftExpression())):
            current_expr = ast.ComparisonOperation(
                left=current_expr,
                operator=ast.ComparisonOperation.Operator(ctx.getChild(2*i-1).getText()),
                right=self.visitShiftExpression(ctx.shiftExpression(i)),
                line=ctx.start.line,
                position=ctx.start.column
            )
        return current_expr

    def visitShiftExpression(self, ctx: GrammarParser.ShiftExpressionContext):
        current_expr = self.visitAdditiveExpression(ctx.additiveExpression(0))

        for i in range(1, len(ctx.additiveExpression())):
            current_expr = ast.ShiftExpression(
                value=current_expr,
                operator=ast.ShiftExpression.Operator(ctx.getChild(2*i-1).getText()),
                amount=self.visitAdditiveExpression(ctx.additiveExpression(i)),
                line=ctx.start.line,
                position=ctx.start.column
            )
        return current_expr

    def visitAdditiveExpression(self, ctx: GrammarParser.AdditiveExpressionContext):
        current_expr = self.visitMultiplicativeExpression(ctx.multiplicativeExpression(0))

        for i in range(1, len(ctx.multiplicativeExpression())):
            current_expr = ast.BinaryArithmetic(
                left=current_expr,
                operator=ast.BinaryArithmetic.Operator(ctx.getChild(2*i-1).getText()),
                right=self.visitMultiplicativeExpression(ctx.multiplicativeExpression(i)),
                line=ctx.start.line,
                position=ctx.start.column
            )
        return current_expr

    def visitMultiplicativeExpression(self, ctx: GrammarParser.MultiplicativeExpressionContext):
        current_expr = self.visitCastExpression(ctx.castExpression(0))

        for i in range(1, len(ctx.castExpression())):
            current_expr = ast.BinaryArithmetic(
                left=current_expr,
                operator=ast.BinaryArithmetic.Operator(ctx.getChild(2*i-1).getText()),
                right=self.visitCastExpression(ctx.castExpression(i)),
                line=ctx.start.line,
                position=ctx.start.column
            )

        return current_expr

    def visitCastExpression(self, ctx: GrammarParser.CastExpressionContext):
        if type_ := ctx.type_():
            cast_type = self.visit(type_)
            expression = self.visitCastExpression(ctx.castExpression())

            # check if the cast is for explicit struct definition
            if isinstance(cast_type.type, ast.StructType) and len(cast_type.address_qualifiers) == 0:
                if isinstance(expression, ast.ArrayInitializer):
                    expression.set_struct_type(cast_type.type)

            return ast.TypeCastExpression(
                cast_type=cast_type,
                expression=expression,
                line=ctx.start.line,
                position=ctx.start.column
            )
        return self.visitUnaryExpression(ctx.unaryExpression())

    def visitUnaryExpression(self, ctx: GrammarParser.UnaryExpressionContext):
        if postfix_expression := ctx.postfixExpression():
            return self.visitPostfixExpression(postfix_expression)

        return ast.UnaryExpression(
            value=self.visitCastExpression(ctx.castExpression()),
            operator=ast.UnaryExpression.Operator(ctx.unaryOperator().getText()),
            prefix=True,
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitPostfixExpression(self, ctx: GrammarParser.PostfixExpressionContext):
        current_expr = self.visitPrimaryExpression(ctx.primaryExpression())

        i = 1
        while i < len(ctx.children):
            if ctx.getChild(i).getText() == "(":
                if not isinstance(current_expr, ast.IDENTIFIER):
                    raise NotImplementedError("Function calls on non-identifiers are not supported")

                if ctx.getChild(i+1).getText() == ")":
                    current_expr = ast.FunctionCall(
                        name=current_expr.name,
                        arguments=[],
                        line=ctx.start.line,
                        position=ctx.start.column
                    )
                    i += 2
                    continue

                if current_expr.name == "scanf":
                    args = ctx.getChild(i+1)
                    fmt = args.logicalOrExpression(0).getText()
                    current_expr = ast.ScanFCall(
                        format=fmt,
                        args=self.visitArgumentExpressionList(args, skip_first=True),
                        line=ctx.start.line,
                        position=ctx.start.column
                    )
                elif current_expr.name == "printf":
                    args = ctx.getChild(i+1)
                    fmt = args.logicalOrExpression(0).getText()
                    current_expr = ast.PrintFCall(
                        format=fmt,
                        args=self.visitArgumentExpressionList(args, skip_first=True),
                        line=ctx.start.line,
                        position=ctx.start.column
                    )
                else:
                    current_expr = ast.FunctionCall(
                        name=current_expr.name,
                        arguments=self.visitArgumentList(ctx.getChild(i+1)),
                        line=ctx.start.line,
                        position=ctx.start.column
                    )
                i += 3
            elif ctx.getChild(i).getText() == "[":
                current_expr = ast.ArrayAccess(
                    target=current_expr,
                    index=self.visitLogicalOrExpression(ctx.getChild(i+1)),
                    line=ctx.start.line,
                    position=ctx.start.column
                )
                i += 3
            elif ctx.getChild(i).getText() in [".", "->"]:
                if ctx.getChild(i).getText() == "->":
                    current_expr = ast.UnaryExpression(
                        value=current_expr,
                        operator=ast.UnaryExpression.Operator.DEREFERENCE,
                        prefix=True,
                        line=ctx.start.line,
                        position=ctx.start.column
                    )
                current_expr = ast.StructAccess(
                    target=current_expr,
                    member_name=ctx.getChild(i+1).getText(),
                    line=ctx.start.line,
                    position=ctx.start.column
                )
                i += 2
            elif ctx.getChild(i).getText() in ["++", "--"]:
                current_expr = ast.UnaryExpression(
                    value=current_expr,
                    operator=ast.UnaryExpression.Operator(ctx.getChild(i).getText()),
                    prefix=False,
                    line=ctx.start.line,
                    position=ctx.start.column
                )
                i += 1

        return current_expr

    def visitPrimaryExpression(self, ctx: GrammarParser.PrimaryExpressionContext):
        if ctx.Identifier():
            return ast.IDENTIFIER(
                name=ctx.Identifier().getText(),
                line=ctx.start.line,
                position=ctx.start.column
            )
        elif constant := ctx.constant():
            return self.visitConstant(constant)
        elif str_lit := ctx.StringLiteral():
            string = str_lit.getText()
            # Zero terminate the string
            string = string[1:-1] + "\0"
            return ast.ArrayInitializer(
                elements=[
                    ast.CHAR(
                        value=char,
                        line=ctx.start.line,
                        position=ctx.start.column
                    ) for char in string],
                line=ctx.start.line,
                position=ctx.start.column
            )
        elif expr := ctx.expression():
            return self.visitExpression(expr)
        elif init_list := ctx.initializerList():
            return self.visitInitializerList(init_list)

    def visitConstant(self, ctx: GrammarParser.ConstantContext):
        if int_ := ctx.Int():
            return ast.INT(
                value=int(int_.getText()),
                line=ctx.start.line,
                position=ctx.start.column
            )
        elif float_ := ctx.Float():
            return ast.FLOAT(
                value=float(float_.getText()),
                line=ctx.start.line,
                position=ctx.start.column
            )
        elif char := ctx.Char():
            # remove single quotes
            char = char.getText()[1:-1]
            # decode escape sequences
            char = char.encode().decode('unicode_escape')
            return ast.CHAR(
                value=char,
                line=ctx.start.line,
                position=ctx.start.column
            )

    def visitArgumentExpressionList(self, ctx: GrammarParser.ArgumentExpressionListContext, skip_first: bool = False):
        if skip_first:
            return [self.visitLogicalOrExpression(arg) for arg in ctx.logicalOrExpression()[1:]]
        return [self.visitLogicalOrExpression(arg) for arg in ctx.logicalOrExpression()]

    def visitInitializerList(self, ctx: GrammarParser.InitializerListContext):
        return ast.ArrayInitializer(
            elements=self.visitInitializerListBody(ctx.initializerListBody()),
            line=ctx.start.line,
            position=ctx.start.column
        )

    def visitInitializerListBody(self, ctx: GrammarParser.InitializerListBodyContext):
        return [self.visitExpression(expression) for expression in ctx.expression()]
