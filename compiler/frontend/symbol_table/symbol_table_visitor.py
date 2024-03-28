import copy
from typing import Optional

from compiler.core import ast
from compiler.core.ast import Type
from compiler.core.ast_visitor import AstVisitor
from compiler.frontend.symbol_table.symboltable import SymbolTable, Symbol
from compiler.core.errors.semantic_error import SemanticError
from compiler.core.errors.warning_error import WarningError
from compiler.core.type_caster import TypeCaster

class SymbolTableVisitor(AstVisitor):
    def __init__(self, symbol_table: Optional[SymbolTable] = None):
        super().__init__()  # This is important so that we can call the generic visit method and get usage to the dict
        self.symbol_table = SymbolTable() if not symbol_table else symbol_table

    def visit_type(self, node: ast.Type):
        ...

    def visit_int(self, node: ast.INT):
        return Type(base_type=ast.BaseType.int, line=node.line, position=node.position)

    def visit_float(self, node: ast.FLOAT):
        return Type(base_type=ast.BaseType.float, line=node.line, position=node.position)

    def visit_char(self, node: ast.CHAR):
        return Type(base_type=ast.BaseType.char, line=node.line, position=node.position)

    def visit_identifier(self, node: ast.IDENTIFIER):
        symbol = self.symbol_table.lookup(node.name, current_scope_only=True)
        if symbol is None:
            raise SemanticError(f"Undefined identifier '{node.name}'.", node.line, node.position)
        return symbol.type


    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        expression_type = self.visit_expression(node.expression)
        targed_cast_type = node.cast_type
        # TODO: Determine if the cast is valid (currently only n/a)

        return Type(base_type=targed_cast_type.base_type, line=node.line, position=node.position)

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        left_type = self.visit_expression(node.left)
        right_type = self.visit_expression(node.right)

        if len(left_type.address_qualifiers) > 0 and right_type.base_type == ast.BaseType.int and len(right_type.address_qualifiers) == 0 and node.operator in {ast.BinaryArithmetic.Operator.PLUS, ast.BinaryArithmetic.Operator.MINUS}:
            # For pointer + integer or pointer - integer, the result is a pointer of the same type
            return Type(base_type=left_type.base_type, line=node.line, position=node.position, address_qualifiers=left_type.address_qualifiers)
        elif len(right_type.address_qualifiers) > 0 and left_type.base_type == ast.BaseType.int and node.operator == ast.BinaryArithmetic.Operator.PLUS:
            # For integer + pointer (valid only for addition), the result is a pointer of the same type
            return Type(base_type=right_type.base_type, line=node.line, position=node.position, address_qualifiers=right_type.address_qualifiers)
        elif left_type.base_type != right_type.base_type or len(left_type.address_qualifiers) != len(right_type.address_qualifiers):
            if len(left_type.address_qualifiers) == 0 and len(right_type.address_qualifiers) == 0:
                # Determine the type of the expression based on the hierarchy  float, int, char
                left_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(left_type.base_type)
                right_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(right_type.base_type)
                if left_expression_hierarchy > right_expression_hierarchy:
                    return Type(base_type=left_type.base_type, line=node.line, position=node.position,
                                address_qualifiers=left_type.address_qualifiers)

                return Type(base_type=right_type.base_type, line=node.line, position=node.position,
                            address_qualifiers=right_type.address_qualifiers)
            raise SemanticError(f"Type mismatch in binary operation: {left_type} and {right_type}.", node.line, node.position)

        return Type(base_type=left_type.base_type, line=node.line, position=node.position)

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        left_type = self.visit_expression(node.left)
        right_type = self.visit_expression(node.right)

        if len(left_type.address_qualifiers) > 0 or len(right_type.address_qualifiers) > 0:
            raise SemanticError(f"Cannot perform bitwise operation on pointers.", node.line, node.position)

        if left_type.base_type == ast.BaseType.float or right_type.base_type == ast.BaseType.float:
            raise SemanticError(f"Type mismatch in binary operation: {left_type.base_type} and {right_type.base_type}.", node.line, node.position)

        return Type(base_type=ast.BaseType.int, line=node.line, position=node.position)

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        left_type = self.visit_expression(node.left)
        right_type = self.visit_expression(node.right)

        if left_type.base_type != right_type.base_type or len(left_type.address_qualifiers) != len(right_type.address_qualifiers):
            WarningError(f"Type mismatch in binary operation: {left_type} and {right_type}.", node.line, node.position).warn()

        return Type(base_type=ast.BaseType.int, line=node.line, position=node.position)

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        left_type = self.visit_expression(node.left)
        right_type = self.visit_expression(node.right)

        if left_type.base_type != right_type.base_type or len(left_type.address_qualifiers) != len(right_type.address_qualifiers):
            WarningError(f"Type mismatch in binary operation: {left_type} and {right_type}.", node.line, node.position).warn()

        return Type(base_type=ast.BaseType.int, line=node.line, position=node.position)

    def visit_unary_expression(self, node: ast.UnaryExpression):
        type = self.visit_expression(node.value)

        # TODO: Possibly implement rest of the unary operations
        if node.operator == ast.UnaryExpression.Operator.ADDRESSOF:
            # TODO: Ensure the operand is addressable (variables, array elements, etc.)
            # if not isinstance(node.value, ast.AddressQualifier):
            #     raise SemanticError(f"Cannot take address of non-addressable value.", node.line, node.position)
            new_type = copy.deepcopy(type)
            new_type.address_qualifiers.append(ast.AddressQualifier.pointer)
            return new_type

        elif node.operator == ast.UnaryExpression.Operator.DEREFERENCE:
            if len(type.address_qualifiers) == 0:
                raise SemanticError(f"Cannot dereference a non pointer type: {type}.", node.line, node.position)
            new_type = copy.deepcopy(type)
            new_type.address_qualifiers.pop()
            return new_type

        return type

    def visit_shift_expression(self, node: ast.ShiftExpression):
        ...

    def visit_program(self, node: ast.Program):
        for statement in node.statements:
            self.visit(statement)

    def visit_body(self, node: ast.Body):
        for statement in node.statements:
            self.visit(statement)

    def visit_function_declaration(self, node: ast.FunctionDeclaration):
        # Check if function is already declared
        if self.symbol_table.lookup(node.name, current_scope_only=True):
            raise SemanticError(f"Function '{node.name}' is already declared.", node.line, node.position)
        # Define the function in the symbol table
        self.symbol_table.define_symbol(Symbol(node.name, node.return_type, scope_level=self.symbol_table.current_scope.level))

        # Create a new scope
        self.symbol_table.enter_scope()

        # TODO: Visit each parameter and add it to the symbol table as a variable with the function's scope level

        # Visit the function body
        self.visit(node.body)

        # Exit the function scope
        self.symbol_table.exit_scope()

    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        ...

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        # Iterate through each qualifier in the variable declaration
        for qualifier in node.qualifiers:
            identifier = qualifier.identifier
            initializer = qualifier.initializer

            # Check if the variable is already declared in the current scope
            if self.symbol_table.lookup(identifier, current_scope_only=True):
                if initializer is None:
                    raise SemanticError(f"Variable '{identifier}' is already declared.", node.line, node.position)
                raise SemanticError(f"Variable '{identifier}' is already defined.", node.line, node.position)

            # Check if the variable is undeclared, meaning it is not initialized (something like int x;)
            if initializer is not None:
                # Get the type of the initializer, to make sure it is compatible with the variable declaration
                initializer_type = self.visit_expression(initializer)

                # Check if the (left)type is compatible with the initializer
                if initializer_type.base_type != node.var_type.base_type or len(initializer_type.address_qualifiers) != len(node.var_type.address_qualifiers):
                    # Add the exception to allow null pointers
                    if isinstance(initializer, ast.INT) and initializer.value == 0 and len(
                            node.var_type.address_qualifiers) > 0:
                        pass
                    elif len(node.var_type.address_qualifiers)== 0 and len(initializer_type.address_qualifiers) == 0:
                        # Determine the type of the expression based on the hierarchy  float, int, char
                        left_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(node.var_type.base_type)
                        right_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(initializer_type.base_type)
                        if right_expression_hierarchy > left_expression_hierarchy:
                            WarningError(f"Implicit conversion from {initializer_type} to {node.var_type}", node.line, node.position).warn()
                            return
                    else:
                        raise SemanticError(f"Incompatible types for variable '{identifier}': {str(node.var_type)} and {str(initializer_type)}.", node.line, node.position)

                if initializer_type.const and not node.var_type.const:
                    WarningError(f"Discarding const qualifier. Initializing {node.var_type} with an expression of type {initializer_type}", node.line, node.position).warn()

            # Define the variable in the symbol table
            self.symbol_table.define_symbol(Symbol(identifier, node.var_type, scope_level=self.symbol_table.current_scope.level))

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)

        # Check if the leftvalue is an expression-unary
        if isinstance(node.left, ast.UnaryExpression) and node.left.operator == ast.UnaryExpression.Operator.ADDRESSOF:
            raise SemanticError(f"Cannot assign to an expression.", node.line, node.position)
        if isinstance(node.left, ast.BinaryArithmetic) or isinstance(node.left, ast.BinaryBitwiseArithmetic) or isinstance(node.left, ast.BinaryLogicalOperation) or isinstance(node.left, ast.ComparisonOperation):
            raise SemanticError(f"Cannot assign to an expression.", node.line, node.position)

        if left_type.base_type != right_type.base_type or len(left_type.address_qualifiers) != len(right_type.address_qualifiers):
            if len(left_type.address_qualifiers) == 0 and len(right_type.address_qualifiers) == 0:
                # Determine the type of the expression based on the hierarchy  float, int, char
                left_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(left_type.base_type)
                right_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(right_type.base_type)
                if right_expression_hierarchy > left_expression_hierarchy:
                    WarningError(f"Implicit conversion from {right_type} to {left_type}", node.line, node.position).warn()
                    return
            raise SemanticError(f"Type mismatch in assignment: {str(left_type)} and {str(right_type)}.", node.line, node.position)

        # Check if the variable is const
        if left_type.const and len(left_type.address_qualifiers) == 0:
            raise SemanticError(f"Cannot assign to a const variable.", node.line, node.position)

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        self.visit(node.expression)

    def visit_printf_call(self, node: ast.PrintFCall):
        ...

    def visit_comment_statement(self, node: ast.CommentStatement):
        ...
