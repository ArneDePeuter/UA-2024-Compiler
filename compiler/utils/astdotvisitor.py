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
        # Map common escape sequences to their .dot file representations
        escape_sequences = {
            "\\": "\\\\",  # Backslash
            "\"": "\\\"",  # Double quote
            "\n": "\\n",  # Newline
            "\t": "\\t",  # Tab
            "\0": "\\0",  # Null
            # Add more escape sequences as needed
        }
        # Replace each escape sequence in node.value
        escaped_value = "".join(escape_sequences.get(char, char) for char in node.value)
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
        expression_node_name = str(id(ast.expression))
        self.total += f'{node_name} -> {expression_node_name};\n'
        self.visit_expression(node.expression)

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        self.gen_binary_dot(node, node.operator.name)

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        self.gen_binary_dot(node, node.operator.name)

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        self.gen_binary_dot(node, node.operator.name)

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
        body_node_name = str(id(node.body))
        self.total += f'{node_name} -> {body_node_name};\n'
        self.visit_body(node.body)
    
    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        node_name = str(id(node))
        self.total += f'{node_name} [label="Declaration Qualifier: {node.identifier}"];\n'
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
        descr = f"{const}{node.base_type.name} {addrs}"
        self.total += f"{node_name} [label=\"Type: {descr}\"];\n"

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        node_name = id(node)
        self.total += f"{node_name} [label=\"ExpressionStatement\"];\n"

        expression_node_name = str(id(node.expression))
        self.total += f'{node_name} -> {expression_node_name};\n'
        self.visit_expression(node.expression)

    def visit_printf_call(self, node: ast.PrintFCall):
        node_name = id(node)

        self.total += f"{node_name} [label=\"PrintFCall {node.replacer.value}\"];\n"

        expression_node_name = str(id(node.expression))
        self.total += f'{node_name} -> {expression_node_name};\n'
        self.visit_expression(node.expression)

    def visit_comment_statement(self, node: ast.CommentStatement):
        node_name = id(node)

        self.total += f"{node_name} [label=\"Comment: \n {node.content}\"];\n"

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
            self.visit(node.else_statement)

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

