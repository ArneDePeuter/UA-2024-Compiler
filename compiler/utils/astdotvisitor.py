from compiler.core.ast_visitor import AstVisitor
from compiler.core import ast


class AstDotVisitor(AstVisitor):
    def __init__(self):
        self.total = ""
        super().__init__()

    def output(self, filename: str):
        with open(filename, "w") as file:
            file.write("digraph ExpressionGraph {\n")
            file.write(self.total)
            file.write("}\n")

    def gen_binary_dot(self, me: ast.BinaryOperation, operator_str: str) -> None:
        node_name = str(id(me))
        self.total += f"{node_name} [label=\"{operator_str}\"];\n"
        left_node_name = str(id(me.left))
        right_node_name = str(id(me.right))
        self.total += f"{node_name} -> {left_node_name};\n"
        self.total += f"{node_name} -> {right_node_name};\n"
        self.visit_expression(me.left)
        self.visit_expression(me.right)

    def visit_int(self, node: ast.INT):
        node_name = id(node)
        self.total += f"{node_name} [label=\"INT: {node.value}\"];\n"

    def visit_float(self, node: ast.FLOAT):
        node_name = id(node)
        self.total += f"{node_name} [label=\"FLOAT: {node.value}\"];\n"

    def visit_char(self, node: ast.CHAR):
        node_name = id(node)
        escaped_value = repr(node.value).replace('\\', '\\\\')[1:-1]
        self.total += f"{node_name} [label=\"CHAR: {escaped_value}\"];\n"

    def visit_identifier(self, node: ast.IDENTIFIER):
        node_name = id(node)
        self.total += f"{node_name} [label=\"IDENTIFIER: {node.name}\"];\n"

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        node_name = str(id(node))
        self.total += f'{node_name} [label="TypeCastExpression"];\n'
        type_node_name = str(id(node.cast_type))
        self.total += f'{node_name} -> {type_node_name};\n'
        self.visit_type(node.cast_type)
        self.visit_expression(node.expression)
        expression_node_name = id(node.expression)
        self.total += f'{node_name} -> {expression_node_name};\n'

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        self.gen_binary_dot(node, node.operator.name)

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        self.gen_binary_dot(node, "bitwise " + node.operator.name)

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        self.gen_binary_dot(node, "logical " + node.operator.name)

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        self.gen_binary_dot(node, node.operator.name)

    def visit_unary_expression(self, node: ast.UnaryExpression):
        node_name = str(id(node))
        operator_str = node.operator.name
        self.total += f"{node_name} [label=\"Unary: {operator_str}\"];\n"

        operand_node_name = str(id(node.value))
        self.total += f"{node_name} -> {operand_node_name};\n"
        self.visit_expression(node.value)

    def visit_shift_expression(self, node: ast.ShiftExpression):
        node_name = str(id(node))
        label = f"{node.operator.name}"
        self.total += f"{node_name} [label=\"SHIFT: {label}\"];\n"

        value_node_name = str(id(node.value))
        self.total += f"{node_name} -> {value_node_name};\n"
        self.visit_expression(node.value)

        shamt_node_name = str(id(node.amount))
        self.total += f"{node_name} -> {shamt_node_name};\n"
        self.visit_expression(node.amount)
    
    def visit_program(self, node: ast.Program):
        program_node_name = str(id(node))
        self.total += f'{program_node_name} [label="Program"];\n'
        for statement in node.statements:
            statement_node_name = str(id(statement))
            self.total += f'{program_node_name} -> {statement_node_name};\n'
            self.visit_statement(statement)
    
    def visit_body(self, node: ast.Body):
        node_name = str(id(node))
        self.total += f'{node_name} [label="CompoundStatement"];\n'
        for statement in node.statements:
            statement_name = str(id(statement))
            self.total += f'{node_name} -> {statement_name};\n'
            self.visit_statement(statement)

    def visit_function_declaration(self, node: ast.FunctionDeclaration):
        node_name = str(id(node))
        self.total += f'{node_name} [label="Function: {node.name}"];\n'

        return_type_node_name = str(id(node.return_type))
        self.total += f'{node_name} -> {return_type_node_name};\n'
        self.visit_type(node.return_type)

        for param in node.parameters:
            param_node_name = str(id(param))
            self.total += f'{param_node_name} [label="Function parameter: {param.name}"];\n'
            self.total += f'{node_name} -> {param_node_name};\n'

            param_type_name = str(id(param.type))
            self.total += f'{param_node_name} -> {param_type_name};\n'
            self.visit_type(param.type)

        body_node_name = str(id(node.body))
        self.total += f'{node_name} -> {body_node_name};\n'
        self.visit_body(node.body)
    
    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        node_name = str(id(node))
        self.total += f'{node_name} [label="Declaration Qualifier: {node.identifier}"];\n'

        if node.array_specifier is not None:
            array_specifier_node_name = str(id(node.array_specifier))
            self.total += f'{node_name} -> {array_specifier_node_name};\n'
            self.visit_expression(node.array_specifier)

        if node.initializer is not None:
            initializer_node_name = str(id(node.initializer))
            self.total += f'{node_name} -> {initializer_node_name};\n'
            self.visit_expression(node.initializer)
    
    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        node_name = str(id(node))
        self.total += f'{node_name} [label="Variable Declaration"];\n'
        type_node_name = str(id(node.var_type))
        self.total += f'{node_name} -> {type_node_name};\n'
        self.visit_type(node.var_type)

        for qualifier in node.qualifiers:
            variable_node_name = str(id(qualifier))
            self.total += f'{node_name} -> {variable_node_name};\n'
            self.visit_variable_declaration_qualifier(qualifier)
    
    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        node_name = str(id(node))
        self.total += f'{node_name} [label="Assignment"];\n'

        left_node_name = str(id(node.left))
        self.total += f'{node_name} -> {left_node_name};\n'
        self.visit_expression(node.left)

        right_node_name = str(id(node.right))
        self.total += f'{node_name} -> {right_node_name};\n'
        self.visit_expression(node.right)
    
    def visit_type(self, node: ast.Type):
        node_name = id(node)
        const = "const " if node.const else ""
        addrs = "".join([str(addr.value) for addr in node.address_qualifiers])
        if isinstance(node.type, ast.ArrayType):
            descr = f"{const}{'array with elements of type'} {node.type.element_type} {addrs}"
            array_spec_id = self.visit_array_specifier(node.type.array_sizes)
            self.total += f"{node_name} [label=\"Type: {descr}\"];\n"
            self.total += f"{node_name} -> {array_spec_id};\n"
        elif isinstance(node.type, ast.StructType):
            descr = f"{const} struct {node.type.definition.name} {addrs}"
            self.total += f"{node_name} [label=\"Type: {descr}\"];\n"
        else:
            descr = f"{const}{node.type.name} {addrs}"
            self.total += f"{node_name} [label=\"Type: {descr}\"];\n"

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        node_name = id(node)
        self.total += f"{node_name} [label=\"ExpressionStatement\"];\n"

        expression_node_name = str(id(node.expression))
        self.total += f'{node_name} -> {expression_node_name};\n'
        self.visit_expression(node.expression)

    def visit_comment_statement(self, node: ast.CommentStatement):
        node_name = id(node)
        valid_content = node.content.replace('"', "'")
        self.total += f"{node_name} [label=\"Comment: \n {valid_content}\"];\n"

    def visit_if_statement(self, node: ast.IfStatement):
        node_name = str(id(node))
        self.total += f"{node_name} [label=\"If\"];\n"

        condition_node_name = str(id(node.condition))
        self.total += f'{node_name} -> {condition_node_name} [label="condition"];\n'
        self.visit_expression(node.condition)

        body_node_name = str(id(node.body))
        self.total += f'{node_name} -> {body_node_name} [label="body"];\n'
        self.visit_body(node.body)

        if hasattr(node, 'else_statement') and node.else_statement:
            else_node_name = str(id(node.else_statement))
            self.total += f'{node_name} -> {else_node_name} [label="else"];\n'
            self.visit_statement(node.else_statement)

    def visit_else_statement(self, node):
        node_name = str(id(node))
        self.total += f"{node_name} [label=\"Else\"];\n"

        if isinstance(node.body, ast.IfStatement):
            self.total += f'{node_name} -> {str(id(node.body))} [label="elseif"];\n'
            self.visit_if_statement(node.body)
        else:
            body_node_name = str(id(node.body))
            self.total += f'{node_name} -> {body_node_name} [label="body"];\n'
            self.visit_body(node.body)

    def visit_while_statement(self, node: ast.WhileStatement):
        node_name = id(node)

        self.total += f"{node_name} [label=\"While\"];\n"

        expression_node_name = str(id(node.expression))
        self.total += f'{node_name} -> {expression_node_name};\n'
        self.visit_expression(node.expression)

        statement_node_name = str(id(node.to_execute))
        self.total += f'{node_name} -> {statement_node_name};\n'
        self.visit_statement(node.to_execute)

    def visit_break_statement(self, node: ast.BreakStatement):
        node_name = id(node)
        self.total += f"{node_name} [label=\"Break\"];\n"

    def visit_continue_statement(self, node: ast.ContinueStatement):
        node_name = id(node)
        self.total += f"{node_name} [label=\"Continue\"];\n"

    def visit_return_statement(self, node: ast.ReturnStatement):
        node_name = id(node)
        self.total += f"{node_name} [label=\"Return\"];\n"

        if node.expression:
            expression_node_name = str(id(node.expression))
            self.total += f'{node_name} -> {expression_node_name};\n'
            self.visit_expression(node.expression)

    def visit_function_call(self, node: ast.FunctionCall):
        node_name = id(node)
        self.total += f"{node_name} [label=\"Function Call: {node.name}\"];\n"

        for arg in node.arguments:
            arg_node_name = str(id(arg))
            self.total += f'{node_name} -> {arg_node_name};\n'
            self.visit_expression(arg)

    def visit_forward_declaration(self, node: ast.ForwardDeclaration):
        node_name = id(node)
        self.total += f"{node_name} [label=\"Forward Declaration: {node.name}\"];\n"

        return_type_name = str(id(node.return_type))
        self.total += f'{node_name} -> {return_type_name};\n'
        self.visit_type(node.return_type)

        for param in node.parameters:
            param_name = str(id(param))
            self.total += f'{node_name} -> {param_name};\n'
            self.visit_type(param)

    @staticmethod
    def escape_dot_string(raw_string):
        # Replace backslashes first to avoid escaping already escaped characters
        escaped_string = raw_string.replace("\\", "\\\\")

        # Escape quotes
        escaped_string = escaped_string.replace('"', '')

        # Escape newlines (if you intend to preserve format in labels)
        escaped_string = escaped_string.replace('\n', '\\n')

        # Escape other potentially problematic characters
        special_chars = {
            ',': '\\,',
            '{': '\\{',
            '}': '\\}',
            '[': '\\[',
            ']': '\\]',
            '=': '\\=',
            '\x00': '\\x00',
        }

        for char, escape in special_chars.items():
            escaped_string = escaped_string.replace(char, escape)

        return escaped_string

    def visit_printf_call(self, node: ast.PrintFCall):
        node_name = str(id(node))
        self.total += f'{node_name} [label="PrintFCall"];\n'

        # Arrow to the format string
        format_string_node_name = str(id(node.format))
        self.total += f'{node_name} -> {format_string_node_name} [label="Format"];\n'
        # Escape the format string to prevent breaking the DOT syntax
        escaped_format_string = self.escape_dot_string(node.format)
        self.total += f'{format_string_node_name} [label="{escaped_format_string}"];\n'

        # Arrow to the arguments
        for i, arg in enumerate(node.args):
            arg_node_name = str(id(arg))
            self.total += f'{node_name} -> {arg_node_name} [label="arg {i + 1}"];\n'
            self.visit_expression(arg)

    def visit_scanf_call(self, node: ast.ScanFCall):
        node_name = str(id(node))
        self.total += f'{node_name} [label="ScanFCall"];\n'

        # Arrow to the format string
        format_string_node_name = str(id(node.format))
        self.total += f'{node_name} -> {format_string_node_name} [label="Format"];\n'
        # Escape the format string to prevent breaking the DOT syntax
        escaped_format_string = self.escape_dot_string(node.format)
        self.total += f'{format_string_node_name} [label="{escaped_format_string}"];\n'

        # Arrow to the arguments
        for i, arg in enumerate(node.args):
            arg_node_name = str(id(arg))
            self.total += f'{node_name} -> {arg_node_name} [label="arg {i + 1}"];\n'
            self.visit_expression(arg)

    def visit_array_specifier(self, node: ast.ArraySpecifier):
        node_id = id(node)
        self.total += f'{node_id} [label="ArraySpecifier"];\n'
        if node.sizes:
            for i, size in enumerate(node.sizes):
                if isinstance(size, ast.INT):
                    size_id = id(size)
                    self.total += f'{size_id} [label="INT: {size.value}"];\n'
                elif isinstance(size, ast.IDENTIFIER):
                    size_id = id(size)
                    self.total += f'{size_id} [label="IDENTIFIER: {size.name}"];\n'
                self.total += f'{node_id} -> {size_id} [label="dim{i + 1}"];\n'
        else:
            size_str = "Undefined"
            self.total += f'{node_id} [label="ArraySpecifier: (size={size_str})"];\n'
        return node_id

    def visit_array_initializer(self, node: ast.ArrayInitializer):
        node_id = id(node)
        if node.struct_type:
            self.total += f"{node_id} [label=\"StructInitializer\"];\n"
        else:
            self.total += f"{node_id} [label=\"ArrayInitializer\"];\n"

        for element in node.elements:
            self.visit_expression(element)
            element_id = id(element)
            self.total += f"{node_id} -> {element_id};\n"

    def visit_array_access(self, node: ast.ArrayAccess):
        node_id = id(node)

        # Add node label for ArrayAccess
        self.total += f'"{node_id}" [label="ArrayAccess"];\n'

        self.visit_expression(node.target)
        target_id = id(node.target)
        self.total += f'"{node_id}" -> "{target_id}" [label="target"];\n'

        # Process index and connect it
        self.visit_expression(node.index)
        index_id = id(node.index)
        self.total += f'"{node_id}" -> "{index_id}" [label="index"];\n'

    def visit_struct_access(self, node: ast.StructAccess):
        node_id = id(node)
        # Add node label for StructAccess
        self.total += f'"{node_id}" [label="Struct access to member {node.member_name}"];\n'

        # Visit target and connect it
        self.visit_expression(node.target)
        target_id = id(node.target)
        self.total += f'"{node_id}" -> "{target_id}" [label="target"];\n'

    def visit_struct_definition(self, node: ast.StructDefinition):
        node_id = id(node)
        self.total += f"{node_id} [label=\"StructDefinition: {node.name}\"];\n"

        for member in node.members:
            member_id = id(member)
            self.visit_struct_member(member)
            self.total += f"{node_id} -> {member_id};\n"

    def visit_struct_member(self, node: ast.StructMember):
        node_id = id(node)

        self.total += f"{node_id} [label=\"Struct Member: {node.name}\"];\n"

        type_id = id(node.type)
        self.visit_type(node.type)
        self.total += f"{node_id} -> {type_id};\n"
