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
    def __init__(self, stdio_included: bool = True, symbol_table: Optional[SymbolTable] = None):
        super().__init__()  # This is important so that we can call the generic visit method and get usage to the dict
        self.symbol_table = SymbolTable() if not symbol_table else symbol_table
        self.inside_declaration = False
        self.stdio_included = stdio_included

    def visit_type(self, node: ast.Type):
        ...

    def visit_int(self, node: ast.INT):
        return Type(type=ast.BaseType.int, line=node.line, position=node.position)

    def visit_float(self, node: ast.FLOAT):
        return Type(type=ast.BaseType.float, line=node.line, position=node.position)

    def visit_char(self, node: ast.CHAR):
        return Type(type=ast.BaseType.char, line=node.line, position=node.position)

    def visit_identifier(self, node: ast.IDENTIFIER):
        symbol = self.symbol_table.lookup(node.name, current_scope_only=False)
        if symbol is None:
            raise SemanticError(f"Undefined identifier '{node.name}'.", node.line, node.position)
        return symbol.type

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        expression_type = self.visit_expression(node.expression)
        targed_cast_type = node.cast_type
        # TODO: Determine if the cast is valid (currently only n/a)

        return Type(type=targed_cast_type.type, line=node.line, position=node.position)

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        left_type = self.visit_expression(node.left)
        right_type = self.visit_expression(node.right)

        if left_type.type == ast.BaseType.void or right_type.type == ast.BaseType.void:
            raise SemanticError(f"Cannot perform arithmetic operations on void type.", node.line, node.position)

        if len(left_type.address_qualifiers) > 0 and right_type.type == ast.BaseType.int and len(right_type.address_qualifiers) == 0 and node.operator in {ast.BinaryArithmetic.Operator.PLUS, ast.BinaryArithmetic.Operator.MINUS}:
            # For pointer + integer or pointer - integer, the result is a pointer of the same type
            return Type(type=left_type.type, line=node.line, position=node.position, address_qualifiers=left_type.address_qualifiers)
        elif len(right_type.address_qualifiers) > 0 and left_type.type == ast.BaseType.int and node.operator == ast.BinaryArithmetic.Operator.PLUS:
            # For integer + pointer (valid only for addition), the result is a pointer of the same type
            return Type(type=right_type.type, line=node.line, position=node.position, address_qualifiers=right_type.address_qualifiers)
        elif left_type.type != right_type.type or len(left_type.address_qualifiers) != len(right_type.address_qualifiers):
            if len(left_type.address_qualifiers) == 0 and len(right_type.address_qualifiers) == 0:
                # Determine the type of the expression based on the hierarchy  float, int, char
                left_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(left_type.type)
                right_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(right_type.type)
                if left_expression_hierarchy > right_expression_hierarchy:
                    return Type(type=left_type.type, line=node.line, position=node.position,
                                address_qualifiers=left_type.address_qualifiers)

                return Type(type=right_type.type, line=node.line, position=node.position,
                            address_qualifiers=right_type.address_qualifiers)
            raise SemanticError(f"Type mismatch in binary arithmetic operation: {left_type} and {right_type}.", node.line, node.position)

        return Type(type=left_type.type, line=node.line, position=node.position)

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        left_type = self.visit_expression(node.left)
        right_type = self.visit_expression(node.right)

        if left_type.type == ast.BaseType.void or right_type.type == ast.BaseType.void:
            raise SemanticError(f"Cannot perform arithmetic operations on void type.", node.line, node.position)

        if len(left_type.address_qualifiers) > 0 or len(right_type.address_qualifiers) > 0:
            raise SemanticError(f"Cannot perform bitwise operation on pointers.", node.line, node.position)

        if left_type.type == ast.BaseType.float or right_type.type == ast.BaseType.float:
            raise SemanticError(f"Cannot execute binary bitwise expression with arguments of type: {left_type} and {right_type}.", node.line, node.position)

        return Type(type=ast.BaseType.int, line=node.line, position=node.position)

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        left_type = self.visit_expression(node.left)
        right_type = self.visit_expression(node.right)

        if left_type.type == ast.BaseType.void or right_type.type == ast.BaseType.void:
            raise SemanticError(f"Cannot perform arithmetic operations on void type.", node.line, node.position)

        if left_type.type != right_type.type or len(left_type.address_qualifiers) != len(right_type.address_qualifiers):
            WarningError(f"Type mismatch in binary logical operation: {left_type} and {right_type}.", node.line, node.position).warn()

        return Type(type=ast.BaseType.int, line=node.line, position=node.position)

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        left_type = self.visit_expression(node.left)
        right_type = self.visit_expression(node.right)

        if left_type.type == ast.BaseType.void or right_type.type == ast.BaseType.void:
            raise SemanticError(f"Cannot perform arithmetic operations on void type.", node.line, node.position)

        if left_type.type != right_type.type or len(left_type.address_qualifiers) != len(right_type.address_qualifiers):
            if isinstance(node.right, ast.INT) and node.right.value == 0 and len(left_type.address_qualifiers) > 0:
                pass
            else:
                WarningError(f"Type mismatch in binary operation: {left_type} and {right_type}.", node.line, node.position).warn()

        return Type(type=ast.BaseType.int, line=node.line, position=node.position)

    def visit_unary_expression(self, node: ast.UnaryExpression):
        type = self.visit_expression(node.value)

        if type.type == ast.BaseType.void:
            raise SemanticError(f"Cannot perform unary operations on void type.", node.line, node.position)

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
        value_type = self.visit_expression(node.value)
        amount_type = self.visit_expression(node.amount)

        if value_type.type == ast.BaseType.void or amount_type.type == ast.BaseType.void:
            raise SemanticError(f"Cannot perform shift operations on void type.", node.line, node.position)

        if len(value_type.address_qualifiers) > 0 or len(amount_type.address_qualifiers) > 0:
            raise SemanticError(f"Cannot perform bitwise operation on pointers.", node.line, node.position)

        if value_type.type == ast.BaseType.float or amount_type.type == ast.BaseType.float:
            raise SemanticError(f"Cannot execute shift-expression with arguments of type: {value_type} and {amount_type}.", node.line, node.position)

        return Type(type=ast.BaseType.int, line=node.line, position=node.position)

    def visit_program(self, node: ast.Program):
        for statement in node.statements:
            self.visit_statement(statement)
        for symbol in self.symbol_table.global_scope.symbols.values():
            if isinstance(symbol.ast_ref, ast.ForwardDeclaration):
                raise SemanticError(f"Function '{symbol.name}' is forward declared but not defined.", node.line, node.position)

        main_symbol=self.symbol_table.global_scope.lookup("main")
        if not main_symbol:
            raise SemanticError("main function is undefined", 0, 0)
        else:
            main_func = main_symbol.ast_ref
            if not main_func:
                raise SemanticError("main is not defined as a function", 0, 0)
            if not isinstance(main_func, ast.FunctionDeclaration):
                raise SemanticError("main is not defined as a function", main_func.line, main_func.position)
            if main_func.return_type != ast.Type(type=ast.BaseType.int):
                raise SemanticError("Return type of main is invalid", main_func.line, main_func.position)

    def visit_body(self, node: ast.Body):
        self.symbol_table.enter_scope()
        for statement in node.statements:
            self.visit_statement(statement)
        self.symbol_table.exit_scope()

    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        ...

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        if node.var_type.type == ast.BaseType.void and node.var_type.address_qualifiers == []:
            raise SemanticError(f"Cannot declare a variable of type void.", node.line, node.position)

        # Iterate through each qualifier in the variable declaration
        for qualifier in node.qualifiers:
            identifier = qualifier.identifier
            initializer = qualifier.initializer

            # Check if the variable is already declared in the current scope
            if self.symbol_table.lookup(identifier, current_scope_only=False):
                if initializer is None:
                    raise SemanticError(f"Variable '{identifier}' is already declared.", node.line, node.position)
                raise SemanticError(f"Variable '{identifier}' is already defined.", node.line, node.position)

            # Check if the variable is undeclared, meaning it is not initialized (something like int x;)
            if initializer is not None:
                # Get the type of the initializer, to make sure it is compatible with the variable declaration
                initializer_type = self.visit_expression(initializer)

                if isinstance(node.var_type.type, ast.ArrayType):
                    if not isinstance(initializer, ast.ArrayInitializer):
                        raise SemanticError(f"Array '{identifier}' must be initialized with an array initializer.", node.line, node.position)
                    if initializer_type.type.array_sizes != node.var_type.type.array_sizes: # TODO: if initializer_type.type.array_sizes > node.var_type.type.array_sizes
                        print(initializer_type.type.array_sizes, node.var_type.type.array_sizes)
                        raise SemanticError(f"Array '{identifier}' must be initialized with {node.var_type.type.array_sizes} elements.", node.line, node.position)
                    if initializer_type.type.element_type != node.var_type.type.element_type:
                        raise SemanticError(f"Array '{identifier}' must be initialized with elements of type {node.var_type.type.element_type}.", node.line, node.position)

                # Check if the (left)type is compatible with the initializer
                if initializer_type.type != node.var_type.type or len(initializer_type.address_qualifiers) != len(node.var_type.address_qualifiers):
                    # Add an exception for when the array is partially initialized (the type check will not be the same but only in that case it is allowed)
                    #if isinstance(initializer, ast.ArrayInitializer):
                    #    if initializer_type.type.array_sizes < node.var_type.type.array_sizes:
                    #        break

                    # Add the exception to allow null pointers
                    if isinstance(initializer, ast.INT) and initializer.value == 0 and len(
                            node.var_type.address_qualifiers) > 0:
                        pass
                    elif len(node.var_type.address_qualifiers)== 0 and len(initializer_type.address_qualifiers) == 0:
                        # Determine the type of the expression based on the hierarchy  float, int, char
                        left_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(node.var_type.type)
                        right_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(initializer_type.type)
                        if right_expression_hierarchy > left_expression_hierarchy:
                            WarningError(f"Implicit conversion from {initializer_type} to {node.var_type}", node.line, node.position).warn()
                    # Check if we have an array pointer
                    elif node.var_type.address_qualifiers == [ast.AddressQualifier.pointer] and node.var_type.type == ast.BaseType.char:
                        pass
                    else:
                        raise SemanticError(f"Incompatible types for variable '{identifier}': {str(node.var_type)} and {str(initializer_type)}.", node.line, node.position)

                if initializer_type.const and not node.var_type.const:
                    WarningError(f"Discarding const qualifier. Initializing {node.var_type} with an expression of type {initializer_type}", node.line, node.position).warn()

            # Define the variable in the symbol table
            self.symbol_table.define_symbol(Symbol(identifier, node.var_type, scope_level=self.symbol_table.current_scope.level))

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        left_type = self.visit_expression(node.left)
        right_type = self.visit_expression(node.right)

        # Check if the leftvalue is an expression-unary
        if isinstance(node.left, ast.UnaryExpression) and node.left.operator == ast.UnaryExpression.Operator.ADDRESSOF:
            raise SemanticError(f"Cannot assign to an expression.", node.line, node.position)
        if isinstance(node.left, ast.BinaryArithmetic) or isinstance(node.left, ast.BinaryBitwiseArithmetic) or isinstance(node.left, ast.BinaryLogicalOperation) or isinstance(node.left, ast.ComparisonOperation):
            raise SemanticError(f"Cannot assign to an expression.", node.line, node.position)

        if isinstance(left_type.type, ast.ArrayType):
            if left_type.type.element_type != right_type:
                raise SemanticError(f"Type mismatch in assignment: {left_type} and {right_type}.", node.line, node.position)
            if node.left.index > left_type.type.array_sizes:
                raise SemanticError(f"Array index out of bounds", node.line, node.position)

        elif left_type.type != right_type.type or len(left_type.address_qualifiers) != len(right_type.address_qualifiers):
            if len(left_type.address_qualifiers) == 0 and len(right_type.address_qualifiers) == 0:
                # Determine the type of the expression based on the hierarchy  float, int, char
                left_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(left_type.type)
                right_expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(right_type.type)
                if right_expression_hierarchy > left_expression_hierarchy:
                    WarningError(f"Implicit conversion from {right_type} to {left_type}", node.line, node.position).warn()
                    return
            # String literals (array of strings) are allowed to be assigned to char*
            elif left_type.type == ast.BaseType.char and right_type.type == ast.BaseType.char and len(left_type.address_qualifiers) > 0:
                pass
            else:
                raise SemanticError(f"Type mismatch in assignment: {str(left_type)} and {str(right_type)}.", node.line, node.position)

        # Check if the variable is const
        if left_type.const and len(left_type.address_qualifiers) == 0:
            raise SemanticError(f"Cannot assign to a const variable.", node.line, node.position)

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        self.visit_expression(node.expression)

    def visit_comment_statement(self, node: ast.CommentStatement):
        ...

    def visit_if_statement(self, node: ast.IfStatement):
        self.visit_expression(node.condition)
        self.visit_statement(node.body)

    def visit_else_statement(self, node: ast.ElseStatement):
        self.visit_statement(node.body)

    def visit_while_statement(self, node: ast.WhileStatement):
        self.visit_expression(node.expression)
        self.visit_statement(node.to_execute)

    def visit_break_statement(self, node: ast.BreakStatement):
        if node.while_statement is None:
            raise SemanticError(f"Break statement outside of loop.", node.line, node.position)

    def visit_continue_statement(self, node: ast.ContinueStatement):
        if node.while_statement is None:
            raise SemanticError(f"Continue statement outside of loop.", node.line, node.position)

    def visit_printf_call(self, node: ast.PrintFCall):
        if not self.stdio_included:
            raise SemanticError(f"Function 'printf' is not declared.", node.line, node.position)
        for argument in node.args:
            self.visit_expression(argument)
        return ast.Type(ast.BaseType.int)

    def visit_scanf_call(self, node: ast.ScanFCall):
        if not self.stdio_included:
            raise SemanticError(f"Function 'scanf' is not declared.", node.line, node.position)
        for argument in node.args:
            self.visit_expression(argument)
        return ast.Type(ast.BaseType.int)

    def visit_return_statement(self, node: ast.ReturnStatement):
        if node.expression is None:
            return

        expression_type = self.visit_expression(node.expression)
        function_return_type = node.function.return_type
        if expression_type.type != function_return_type.type or len(expression_type.address_qualifiers) != len(function_return_type.address_qualifiers):
            if len(expression_type.address_qualifiers) == 0 and len(function_return_type.address_qualifiers) == 0:
                # Determine the type of the expression based on the hierarchy  float, int, char
                expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(expression_type.type)
                function_hierarchy = TypeCaster.get_heirarchy_of_base_type(function_return_type.type)
                if expression_hierarchy > function_hierarchy:
                    WarningError(f"Implicit conversion from {expression_type} to {function_return_type}", node.line, node.position).warn()
                    return
            else:
                raise SemanticError(f"Type mismatch in return statement: {str(expression_type)} and {str(function_return_type)}.", node.line, node.position)

    def visit_function_declaration(self, node: ast.FunctionDeclaration):
        if self.inside_declaration:
            raise SemanticError("Function definition is not allowed here", node.line, node.position)

        self.inside_declaration = True

        symbol = self.symbol_table.lookup(node.name, current_scope_only=True)
        # Check if function is already declared
        if symbol:
            # if the ref already points to a function declaration we have a redefinition
            if isinstance(symbol.ast_ref, ast.FunctionDeclaration):
                raise SemanticError(f"Function '{node.name}' is already defined.", node.line, node.position)

            if not isinstance(symbol.ast_ref, ast.ForwardDeclaration):
                raise SemanticError(f"{node.name} redeclared as different kind of symbol", node.line, node.position)

            # check if the parameters match
            params_match = True
            if len(symbol.ast_ref.parameters) == len(node.parameters):
                for type_fwd, type_decl in zip(symbol.ast_ref.parameters, [param.type for param in node.parameters]):
                    if type_fwd != type_decl:
                        params_match = False
            else:
                params_match = False

            # if they don't match the declaration was talking about some other thing, so we define the function
            if not params_match:
                self.symbol_table.define_symbol(Symbol(node.name, node.return_type, scope_level=self.symbol_table.current_scope.level, ast_ref=node))
            else:
                # otherwise the forward declaration was talking about this
                symbol.ast_ref = node
        else:
            self.symbol_table.define_symbol(Symbol(node.name, node.return_type, scope_level=self.symbol_table.current_scope.level, ast_ref=node))

        self.symbol_table.enter_scope()

        # Visit each parameter and add it to the symbol table as a variable with the function's scope level
        for param in node.parameters:
            self.visit_variable_declaration(ast.VariableDeclaration(
                var_type=param.type,
                qualifiers=[ast.VariableDeclarationQualifier(identifier=param.name, array_specifier=None, initializer=None)]
            ))

        # Visit the function body
        self.visit_statement(node.body)

        self.symbol_table.exit_scope()
        self.inside_declaration = False

    def visit_function_call(self, node: ast.FunctionCall):
        function_symbol = self.symbol_table.lookup(node.name, current_scope_only=False)
        if function_symbol is None:
            raise SemanticError(f"Undefined function '{node.name}'.", node.line, node.position)

        ref = function_symbol.ast_ref
        if isinstance(ref, ast.ForwardDeclaration):
            param_types = ref.parameters
        elif isinstance(ref, ast.FunctionDeclaration):
            param_types = [param.type for param in ref.parameters]
        else:
            raise SemanticError(f"'{node.name}' called but it is not a function", node.line, node.position)

        # Compare the number of arguments with the number of parameters
        if len(node.arguments) != len(param_types):
            raise SemanticError(f"Function '{node.name}' expects {len(param_types)} arguments but {len(node.arguments)} were given.", node.line, node.position)

        # Iterate over each argument and each parameter
        for argument, expected_type in zip(node.arguments, param_types):
            expression_type = self.visit_expression(argument)
            if expression_type.type != expected_type.type or len(expression_type.address_qualifiers) != len(expected_type.address_qualifiers):
                if isinstance(argument, ast.INT) and argument.value == 0 and len(expected_type.address_qualifiers) > 0:
                    pass
                elif len(expression_type.address_qualifiers) == 0 and len(expected_type.address_qualifiers) == 0:
                    # Determine the type of the expression based on the hierarchy  float, int, char
                    expression_hierarchy = TypeCaster.get_heirarchy_of_base_type(expression_type.type)
                    expected_hierarchy = TypeCaster.get_heirarchy_of_base_type(expected_type.type)
                    if expression_hierarchy > expected_hierarchy:
                        WarningError(f"Implicit conversion from {expression_type} to {expected_hierarchy}", node.line, node.position).warn()
                        return function_symbol.type
                else:
                    raise SemanticError(f"Type mismatch in function parameter: {str(expression_type)} and {str(expected_type)}.",node.line, node.position)

        return function_symbol.type

    def visit_forward_declaration(self, node: ast.ForwardDeclaration):
        if self.symbol_table.lookup(node.name, current_scope_only=True):
            return
        self.symbol_table.define_symbol(Symbol(node.name, node.return_type, scope_level=self.symbol_table.current_scope.level, ast_ref=node))

    def visit_array_specifier(self, node: ast.ArraySpecifier):
        types_of_sizes = set()
        for s in node.sizes:
            if isinstance(s, ast.IDENTIFIER):
                symbol = self.symbol_table.lookup(s.name, current_scope_only=False)
                if symbol is None:
                    raise SemanticError(f"Undefined identifier '{s.name}'.", s.line, s.position)
                types_of_sizes.add(symbol.type.type)
            elif isinstance(s, ast.INT):
                types_of_sizes.add(ast.BaseType.int)
            else:
                raise SemanticError(f"Array size must be a constant expression.", s.line, s.position)
        return ast.Type(type=types_of_sizes.pop(), const=False, address_qualifiers=None)

    @staticmethod
    def fits_dimensions(dimension, node):
        """
        This is a helper function to check if the dimensions of an array are correct
        :param node: the node to check
        :return: True if the dimensions are correct, False otherwise
        """
        if len(dimension) == 0:
            return True
        if len(node.elements) != dimension[0]:
            return False
        fits = True
        for newnode in node.elements:
            fits = fits and SymbolTableVisitor.fits_dimensions(dimension[1:], newnode)
        return fits

    def count_element_types(self, node, counter):
        """
        This count the amount of different element types in the array, usefull for implicit type casting
        :param node:
        :return:
        """
        if isinstance(node, ast.ArrayInitializer):
            for element in node.elements:
                self.count_element_types(element, counter)
        else:
            counter[self.visit_expression(node).type] = 1 + counter.get(self.visit_expression(node).type, 0)

    def element_type_in_set(self, set, node):
        """
        Check if the element type of the node is in the set
        :param set:
        :param elements:
        :return: Changes the set by reference
        """
        if isinstance(node, ast.ArrayInitializer):
            for element in node.elements:
                self.element_type_in_set(set, element)
        else:
            set.add(self.visit_expression(node))

    def process_array_elements_implicit_casting(self, node, most_common_type, org_array):
        """
        Process each element in the node to check type hierarchy and perform necessary upcasting.
        :param node: The node containing elements to process.
        :param most_common_type: The most common base type found in the node for potential upcasting.
        """
        if isinstance(node, ast.ArrayInitializer):
            for i, element in enumerate(node.elements):
                self.process_array_elements_implicit_casting(element, most_common_type, org_array)  # Recursive handling for multi-dimensional arrays
        else:
            element_eval = self.visit_expression(node)
            element_type = element_eval.type
            if TypeCaster.get_heirarchy_of_base_type(most_common_type) > TypeCaster.get_heirarchy_of_base_type(element_type):
                WarningError(f"Implicit conversion from {element_type} to {most_common_type}", node.line, node.position).warn()
                # Loop through the org_array to find the element and replace it with the upcasted version
                for i, element in enumerate(org_array.elements):
                    if element == node:
                        org_array.elements[i] = TypeCaster.upcast(node)

    def visit_array_initializer(self, node: ast.ArrayInitializer):
        if node.struct_type:
            return self.visit_struct_initializer(node)

        # Apply implicit type conversions
        counter = {}
        self.count_element_types(node, counter)
        most_common_type = max(counter, key=counter.get)
        self.process_array_elements_implicit_casting(node, most_common_type, node)

        element_types = set()
        self.element_type_in_set(element_types, node)

        if len(element_types) > 1:
            raise SemanticError("Array initializer elements must all be of the same type.", node.line, node.position)

        array_element_type = next(iter(element_types))
        temp_array_element_type = copy.deepcopy(array_element_type)
        while not isinstance(array_element_type.type, ast.BaseType):
            array_element_type = array_element_type.type.element_type
        array_element_type.address_qualifiers = temp_array_element_type.address_qualifiers
        array_element_type.const = temp_array_element_type.const

        dimensions = []
        current_node = node
        while current_node is not None:
            if isinstance(current_node, ast.ArrayInitializer):
                dimensions.append(len(current_node.elements))
                current_node = current_node.elements[0]
            else:
                current_node = None

        if not SymbolTableVisitor.fits_dimensions(dimensions, node):
            raise SemanticError("Array initializer elements must all be of the same length.", node.line, node.position)

        array_specifier = ast.ArraySpecifier(sizes=[])
        for dimension in dimensions:
            array_specifier.sizes.append(ast.INT(value=dimension))
        array_type = ast.ArrayType(element_type=array_element_type, array_sizes=array_specifier)

        return ast.Type(type=array_type, const=False, address_qualifiers=[], line=node.line, position=node.position)

    def visit_array_access(self, node: ast.ArrayAccess):
        array_symbol = self.symbol_table.lookup(node.array_name, current_scope_only=False)
        if array_symbol is None:
            raise SemanticError(f"Undefined array '{node.array_name}'.", node.line, node.position)

        index_type = self.visit_expression(node.index)
        if index_type.type != ast.BaseType.int:
            raise SemanticError(f"Array index must be of type int, not {index_type}.", node.line, node.position)
        return ast.Type(type=array_symbol.type.type, const=array_symbol.type.const, address_qualifiers=array_symbol.type.address_qualifiers)

    def visit_struct_access(self, node: ast.StructAccess):
        tgt_type: ast.Type = self.visit_expression(node.target)
        struct_type = tgt_type.type
        if not isinstance(struct_type, ast.StructType):
            raise SemanticError(f"Struct access method to an object which isn't a struct.", node.line, node.position)
        if len(tgt_type.address_qualifiers) > 0:
            raise SemanticError(f"Struct access method to a pointer", node.line, node.position)

        target_member = None
        for i, member in enumerate(struct_type.definition.members):
            if member.name == node.member_name:
                target_member = member
                break

        if target_member is None:
            raise SemanticError(f"'{tgt_type}' has no member named '{node.member_name}'", node.line, node.position)

        if tgt_type.const:
            cp = copy.deepcopy(target_member.type)
            cp.const = tgt_type.const
            return cp
        return target_member.type

    def visit_struct_definition(self, node: ast.StructDefinition):
        ...

    def visit_struct_initializer(self, node: ast.ArrayInitializer):
        struct_type = node.struct_type

        if len(struct_type.definition.members) != len(node.elements):
            raise SemanticError(f"Struct initializer has {len(node.elements)} elements but the struct has {len(struct_type.definition.members)} members.", node.line, node.position)

        for i, member in enumerate(struct_type.definition.members):
            member_type = member.type
            element = node.elements[i]
            element_type = self.visit_expression(node.elements[i])
            if member_type.type != element_type.type or len(member_type.address_qualifiers) != len(element_type.address_qualifiers):
                if isinstance(element, ast.INT) and element.value == 0 and len(member_type.address_qualifiers) > 0:
                    pass
                elif isinstance(element_type.type, ast.ArrayType) or isinstance(member_type.type, ast.ArrayType):
                    if member_type.type != element_type.type:
                        raise SemanticError(f"Type mismatch in struct initializer: {str(member_type.type)} and {str(element_type.type)}.", node.line, node.position)
                elif len(member_type.address_qualifiers) == 0 and len(element_type.address_qualifiers) == 0:
                    # Determine the type of the expression based on the hierarchy  float, int, char
                    member_hierarchy = TypeCaster.get_heirarchy_of_base_type(member_type.type)
                    element_hierarchy = TypeCaster.get_heirarchy_of_base_type(element_type.type)
                    if element_hierarchy > member_hierarchy:
                        WarningError(f"Implicit conversion from {element_type} to {member_type}", node.line, node.position).warn()
                else:
                    raise SemanticError(f"Type mismatch in struct initializer: {str(member_type)} and {str(element_type)}.", node.line, node.position)

        return ast.Type(type=struct_type, const=False, address_qualifiers=[], line=node.line, position=node.position)
