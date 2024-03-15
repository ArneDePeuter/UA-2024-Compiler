from compiler.core.ast_visitor import AstVisitor
from compiler.core.errors.semantic_error import SemanticError
from compiler.core import ast
from symboltable import SymbolTable, Symbol
class SymbolTableVisitor(AstVisitor):
    def __init__(self, symbol_table):
        # super().__init__()  # Aanroep constructor van ASTVisitor indien nodig
        self.symbol_table = symbol_table

    def visit_type(self, node: ast.Type):
        # Because the type node doens't perform an operation, we can ignore it
        pass

    def visit_int(self, node: ast.INT):
        pass

    def visit_float(self, node: ast.FLOAT):
        pass

    def visit_char(self, node: ast.CHAR):
        pass

    def visit_identifier(self, node: ast.IDENTIFIER):
        # This is important for checking the declaration of identifiersCan
        if self.symbol_table.lookup(node.name) is None:
            raise SemanticError(f"Use of undeclared identifier '{node.name}'.", node.line, node.position)

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        # First, visit the expression being cast to ensure it's semantically valid on its own.
        self.visit(node.expression)
        # Retrieve the type of the expression being cast.
        expression_type = self.get_expression_type(node.expression)  # TODO: implement get_expression_type
        # Check if the cast from expression_type to node.cast_type is allowed.
        if not self.is_cast_allowed(expression_type, node.cast_type):  # TODO: implement is_cast_allowed
            raise SemanticError(f"Invalid type cast from {expression_type} to {node.cast_type}.", node.line, node.position)

        # Additional checks might include ensuring the expression is not a const if the target type is non-const,
        # or if specific type casts are disallowed or require explicit actions.

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        # Visit both the left and right operands to ensure they're semantically valid.
        self.visit(node.left)
        self.visit(node.right)

        # Check if the types of the left and right operands are compatible for arithmetic operations.
        left_type = self.get_expression_type(node.left) # TODO: implement get_expression_type
        right_type = self.get_expression_type(node.right) # TODO: implement get_expression_type

        if not self.are_types_compatible_for_arithmetic(left_type, right_type): # TODO: implement are_types_compatible_for_arithmetic
            raise SemanticError(f"Incompatible types for arithmetic operation: {left_type} and {right_type}.",
                                node.line, node.position)

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        # Similar to arithmetic operations, visit both operands.
        self.visit(node.left)
        self.visit(node.right)

        # Check if the types are compatible for bitwise operations.
        left_type = self.get_expression_type(node.left) # TODO: implement get_expression_type
        right_type = self.get_expression_type(node.right) # TODO: implement get_expression_type

        if not self.are_types_compatible_for_bitwise(left_type, right_type): # TODO: implement are_types_compatible_for_bitwise
            raise SemanticError(f"Incompatible types for bitwise operation: {left_type} and {right_type}.", node.line, node.position)


    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        # Visit both operands to ensure semantic validity.
        self.visit(node.left)
        self.visit(node.right)

        # Check if the types of operands are compatible for logical operations.
        left_type = self.get_expression_type(node.left) # TODO: implement get_expression_type
        right_type = self.get_expression_type(node.right) # TODO: implement get_expression_type

        if not self.are_types_compatible_for_logical(left_type, right_type): # TODO: implement are_types_compatible_for_logical
            raise SemanticError(f"Incompatible types for logical operation: {left_type} and {right_type}.", node.line, node.position)

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        # Visit both the left and right operands.
        self.visit(node.left)
        self.visit(node.right)

        # Retrieve the types of both operands.
        left_type = self.get_expression_type(node.left)  # TODO: implement get_expression_type
        right_type = self.get_expression_type(node.right)  # TODO: implement get_expression_type

        # Check if the types of the left and right operands are compatible for comparison.
        if not self.are_types_compatible_for_comparison(left_type, right_type):  # TODO: implement are_types_compatible_for_comparison
            raise SemanticError(f"Incompatible types for comparison operation: {left_type} and {right_type}.", node.line, node.position)

    def visit_unary_expression(self, node: ast.UnaryExpression):
        # Visit the operand to ensure it's semantically valid.
        self.visit(node.value)

        # Retrieve the type of the operand.
        operand_type = self.get_expression_type(node.value)  # TODO: implement get_expression_type

        # Check if the unary operation is valid for the operand's type.
        if not self.is_unary_operation_valid(node.operator, operand_type):  # TODO: implement is_unary_operation_valid
            raise SemanticError(f"Invalid unary operation {node.operator} for type {operand_type}.", node.line, node.position)

    def visit_shift_expression(self, node: ast.ShiftExpression):
        # Visit both the value and the shift amount to ensure they're semantically valid.
        self.visit(node.value)
        self.visit(node.amount)

        # Retrieve the types of the value and the shift amount.
        value_type = self.get_expression_type(node.value)  # TODO: implement get_expression_type
        amount_type = self.get_expression_type(node.amount)  # TODO: implement get_expression_type

        # Check if the types are compatible for shift operations.
        if not self.are_types_compatible_for_shift(value_type, amount_type):  # TODO: implement are_types_compatible_for_shift
            raise SemanticError(
                f"Incompatible types for shift operation: {value_type} (value) and {amount_type} (amount).", node.line,
                node.position)

    def visit_program(self, node: ast.Program):
        # Assuming Program node contains a list of statements, declarations, or function definitions.
        for statement in node.statements:
            self.visit(statement)

    def visit_body(self, node: ast.Body):
        # Enter a new scope when starting to visit a body
        self.symbol_table.enter_scope()

        for statement in node.statements:
            self.visit(statement)

        # Exit the scope after visiting all statements in the body
        self.symbol_table.exit_scope()

    def visit_function_declaration(self, node: ast.FunctionDeclaration):
        # Check if the function is already declared in the current scope
        if self.symbol_table.lookup(node.name, current_scope_only=True):
            raise SemanticError(f"Function '{node.name}' is already declared.", node.line, node.position)

        # Register the function in the symbol table with its return type and parameter types
        self.symbol_table.define_symbol(
            Symbol(node.name, node.return_type, scope_level=self.symbol_table.current_scope.level))

        # Enter a new scope for the function's body
        self.symbol_table.enter_scope()

        # Visit the function's body
        self.visit(node.body)

        # Exit the function's scope
        self.symbol_table.exit_scope()

    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        # If there's an initializer, visit it to ensure it's semantically valid
        if node.initializer is not None:
            self.visit(node.initializer)

        # Further checks for qualifiers could be implemented here, based on language semantics

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        # Iterate through each qualifier in the variable declaration
        for qualifier in node.qualifiers:
            # Ensure the variable is not already declared in the current scope
            if self.symbol_table.lookup(qualifier.identifier, current_scope_only=True):
                raise SemanticError(f"Variable '{qualifier.identifier}' is already declared.", node.line, node.position)

            # Visit the qualifier, which will check the initializer
            self.visit(qualifier)

            # Define the symbol in the symbol table
            self.symbol_table.define_symbol(
                Symbol(qualifier.identifier, node.var_type, scope_level=self.symbol_table.current_scope.level))

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        # Ensure the variable is declared
        symbol = self.symbol_table.lookup(node.identifier)
        if symbol is None:
            raise SemanticError(f"Use of undeclared variable '{node.identifier}'.", node.line, node.position)

        # Visit the value to be assigned to ensure it's semantically valid
        self.visit(node.value)

        # Optionally, check if the assignment's value type is compatible with the variable's type
        value_type = self.get_expression_type(node.value)
        if not self.is_type_compatible(symbol.type, value_type):
            raise SemanticError(
                f"Type mismatch in assignment to '{node.identifier}': cannot assign {value_type} to {symbol.type}.",
                node.line, node.position)
