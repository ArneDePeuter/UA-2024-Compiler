from compiler.core.ast_visitor import AstVisitor
from compiler.core.errors.semantic_error import SemanticError
from compiler.core import ast
from compiler.frontend.symbol_table.symboltable import SymbolTable, Symbol

from compiler.core.ast.type import Type, BaseType
from compiler.core.ast.expression import UnaryExpression
class SymbolTableVisitor(AstVisitor):
    def __init__(self, symbol_table):
        super().__init__()  # This is important so that we can call the generic visit method and get usage to the dict
        self.symbol_table = symbol_table

    def get_expression_type(self, node):
        # This method finds out the type of exprression, helping to checki if the program follows rules about how differnt types can be user or combined

        if isinstance(node, ast.INT):
            return Type(base_type=BaseType.int)
        elif isinstance(node, ast.FLOAT):
            return Type(base_type=BaseType.float)
        elif isinstance(node, ast.CHAR):
            return Type(base_type=BaseType.char)
        elif isinstance(node, ast.IDENTIFIER):
            # Lookup the identifier in the symbol table to get its type.
            symbol = self.symbol_table.lookup(node.name)
            if symbol is not None:
                return symbol.type  # Assuming symbol.type is already a Type instance.
            else:
                raise SemanticError(f"Use of undeclared identifier '{node.name}'.")
        elif isinstance(node, (ast.BinaryArithmetic, ast.BinaryBitwiseArithmetic, ast.BinaryLogicalOperation)):
            # For binary operations, the type might depend on the operation and the operand types.
            # This is a simplified approach; actual implementation might need to consider type promotion rules, etc.
            left_type = self.get_expression_type(node.left)
            right_type = self.get_expression_type(node.right)
            if left_type.base_type == right_type.base_type:
                return left_type  # Assuming the operation does not change the type.
            else:
                # Handle type mismatch or implement logic for determining resulting type based on operands
                # This example just returns an int type for demonstration.
                return Type(base_type=BaseType.int)  # Simplification, real logic may vary.
        # Add additional elif branches for other expression types as needed.

        # Handle unknown or unimplemented node types.
        return Type(base_type=BaseType.int)  # Default or error case, adjust as needed.

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
        expression_type = self.get_expression_type(node.expression)
        # Check if the cast from expression_type to node.cast_type is allowed.
        if not self.is_cast_allowed(expression_type, node.cast_type):  # TODO: implement is_cast_allowed
            raise SemanticError(f"Invalid type cast from {expression_type} to {node.cast_type}.", node.line, node.position)

        # Additional checks might include ensuring the expression is not a const if the target type is non-const,
        # or if specific type casts are disallowed or require explicit actions.

    def are_types_compatible_for_arithmetic(self, type1, type2):
        # In C, arithmetic operations are allowed between numeric types
        # and between pointers and integers (pointer arithmetic).

        # Define the numeric types for compatibility checking
        numeric_types = {'int', 'float', 'double', 'char'}

        # Check if both types are non-pointer numeric types
        if (type1.base_type.value in numeric_types and len(type1.address_qualifiers) == 0 and
                type2.base_type.value in numeric_types and len(type2.address_qualifiers) == 0):
            return True

        # Check for pointer arithmetic compatibility (one pointer type and one integer type)
        if ((type1.base_type.value in numeric_types and len(type1.address_qualifiers) == 0 and len(type2.address_qualifiers) > 0) or
                (type2.base_type.value in numeric_types and len(type2.address_qualifiers) == 0 and len(type1.address_qualifiers) > 0)):
            return True

        # Const correctness: if either type is const, arithmetic that modifies the value is not allowed
        if type1.is_const or type2.is_const:
            return False

        # If none of the above conditions are met, types are not compatible for arithmetic
        return False

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        # Visit both the left and right operands to ensure they're semantically valid.
        self.visit(node.left)
        self.visit(node.right)

        # Check if the types of the left and right operands are compatible for arithmetic operations.
        left_type = self.get_expression_type(node.left)
        right_type = self.get_expression_type(node.right)

        if not self.are_types_compatible_for_arithmetic(left_type, right_type):
            raise SemanticError(f"Incompatible types for arithmetic operation: {left_type} and {right_type}.",
                                node.line, node.position)

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        # Similar to arithmetic operations, visit both operands.
        self.visit(node.left)
        self.visit(node.right)

        # Check if the types are compatible for bitwise operations.
        left_type = self.get_expression_type(node.left)
        right_type = self.get_expression_type(node.right)

        if not self.are_types_compatible_for_bitwise(left_type, right_type): # TODO: implement are_types_compatible_for_bitwise
            raise SemanticError(f"Incompatible types for bitwise operation: {left_type} and {right_type}.", node.line, node.position)


    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        # Visit both operands to ensure semantic validity.
        self.visit(node.left)
        self.visit(node.right)

        # Check if the types of operands are compatible for logical operations.
        left_type = self.get_expression_type(node.left)
        right_type = self.get_expression_type(node.right)

        if not self.are_types_compatible_for_logical(left_type, right_type): # TODO: implement are_types_compatible_for_logical
            raise SemanticError(f"Incompatible types for logical operation: {left_type} and {right_type}.", node.line, node.position)

    def are_types_compatible_for_comparison(self, left_type, right_type):
        # Assuming left_type and right_type are instances of the Type class from your AST definition.
        # This function checks if two types are compatible for comparison operations.

        # For simplicity, let's allow comparison between similar types or between int and float.
        # More complex rules may involve implicit type conversions or more detailed type checks.

        if left_type.base_type == right_type.base_type:
            return True  # Types are the same, so they are compatible.

        # Allow comparison between int and float types as well.
        int_float_pairs = [{BaseType.int, BaseType.float}, {BaseType.float, BaseType.int}]
        if {left_type.base_type, right_type.base_type} in int_float_pairs:
            return True

        # Extend this section with additional rules as necessary for your language.
        # For example, you might decide that certain custom types or enums are comparable under specific conditions.

        return False  # Default to false if none of the above conditions are met.

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        # Visit both the left and right operands.
        self.visit(node.left)
        self.visit(node.right)

        # Retrieve the types of both operands.
        left_type = self.get_expression_type(node.left)
        right_type = self.get_expression_type(node.right)

        # Check if the types of the left and right operands are compatible for comparison.
        if not self.are_types_compatible_for_comparison(left_type, right_type):  # TODO: implement are_types_compatible_for_comparison
            raise SemanticError(f"Incompatible types for comparison operation: {left_type} and {right_type}.", node.line, node.position)

    def is_unary_operation_valid(self, operator, operand_type):
        # Mapping from UnaryExpression.Operator to allowed BaseType(s)
        valid_operations = {
            UnaryExpression.Operator.POSITIVE: [BaseType.int, BaseType.float],
            UnaryExpression.Operator.NEGATIVE: [BaseType.int, BaseType.float],
            UnaryExpression.Operator.ONESCOMPLEMENT: [BaseType.int],  # Typically valid for integers
            UnaryExpression.Operator.LOGICALNEGATION: [BaseType.int],  # Assuming boolean is represented as int
            UnaryExpression.Operator.ADDRESSOF: [],  # Depends on context, e.g., any non-const type?
            UnaryExpression.Operator.DEREFERENCE: [],  # Requires pointer types, handled separately
            UnaryExpression.Operator.INCREMENT: [BaseType.int, BaseType.float],
            UnaryExpression.Operator.DECREMENT: [BaseType.int, BaseType.float],
        }

        # Special handling for ADDRESSOF and DEREFERENCE due to pointer involvement
        if operator == UnaryExpression.Operator.ADDRESSOF or operator == UnaryExpression.Operator.DEREFERENCE:
            # Simplified logic: ADDRESSOF is always valid, DEREFERENCE requires pointer types
            if operator == UnaryExpression.Operator.DEREFERENCE and not operand_type.address_qualifiers:
                return False  # DEREFERENCE is invalid for non-pointer types
            return True  # ADDRESSOF is generally valid; DEREFERENCE is valid for pointers

        # Check if the operation is valid for the operand's base type.
        return operand_type.base_type in valid_operations[operator]

    def visit_unary_expression(self, node: ast.UnaryExpression):
        # Visit the operand to ensure it's semantically valid.
        self.visit(node.value)

        # Retrieve the type of the operand.
        operand_type = self.get_expression_type(node.value)

        # Check if the unary operation is valid for the operand's type.
        if not self.is_unary_operation_valid(node.operator, operand_type):
            raise SemanticError(f"Invalid unary operation {node.operator} for type {operand_type}.", node.line, node.position)

    def visit_shift_expression(self, node: ast.ShiftExpression):
        # Visit both the value and the shift amount to ensure they're semantically valid.
        self.visit(node.value)
        self.visit(node.amount)

        # Retrieve the types of the value and the shift amount.
        value_type = self.get_expression_type(node.value)
        amount_type = self.get_expression_type(node.amount)

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
        for statement in node.statements:
            self.visit(statement)

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

    def is_type_compatible(self, variable_type, value_type):
        # This is a stub for type compatibility logic.
        # You should implement the actual logic based on your language's type system.
        # For example, it could be a simple comparison:
        return variable_type.base_type == value_type.base_type
        # Or a more complex set of rules depending on type hierarchies, implicit conversions, etc.

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

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        # Visit the expression to ensure it's semantically valid
        self.visit(node.expression)