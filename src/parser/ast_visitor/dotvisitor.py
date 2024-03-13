from typing import Any

from .visitor import Visitor
from ..ast import expression as EXPR
from ..ast.comment import Comment
from ..ast.declaration import Declaration


class DotVisitor(Visitor):
    def __init__(self):
        super().__init__()
        self.total = ""

    def output(self, filename: str):
        with open(filename, "w") as file:
            file.write("digraph ExpressionGraph {\n")
            file.write(self.total)
            file.write("}\n")

    def visit_program(self, program):
        program_node_name = str(id(program))
        self.total += f'{program_node_name} [label="Program"];\n'
        for statement in program.statements:
            statement_node_name = str(id(statement))
            self.total += f'{program_node_name} -> {statement_node_name};\n'
            self.visit_ast(statement)

    def visit_main_function(self, main_function):
        node_name = str(id(main_function))
        self.total += f'{node_name} [label="MainFunction\\nreturn_type: {main_function.return_type}\\nname: {main_function.name}"];\n'
        body_node_name = str(id(main_function.body))
        self.total += f'{node_name} -> {body_node_name};\n'
        self.visit_ast(main_function.body)

    def visit_compound_statement(self, compound_statement):
        node_name = str(id(compound_statement))
        self.total += f'{node_name} [label="CompoundStatement"];\n'
        prev_statement_node_name = None
        for statement in compound_statement.statements:
            if isinstance(statement, Comment):
                comment_node_name = str(id(statement))
                self.total += f'{comment_node_name} [label="Comment\\n{statement.content}"];\n'
                if prev_statement_node_name:
                    self.total += f'{prev_statement_node_name} -> {comment_node_name} [style=dashed];\n'
                else:
                    self.total += f'{node_name} -> {comment_node_name} [style=dashed];\n'
            elif isinstance(statement, Declaration):
                declaration_node_name = str(id(statement))
                self.total += f'{node_name} -> {declaration_node_name};\n'
                self.visit_declaration(statement)
                prev_statement_node_name = declaration_node_name
            else:
                statement_node_name = str(id(statement))
                self.total += f'{node_name} -> {statement_node_name};\n'
                self.visit_ast(statement)
                prev_statement_node_name = statement_node_name

    def visit_comment(self, comment: Comment):
        node_name = str(id(comment))
        self.total += f'{node_name} [label="Comment\\n{comment.content}"];\n'

    def visit_declaration(self, declaration):
        node_name = str(id(declaration))
        self.total += f'{node_name} [label="Declaration"];\n'
        type_node_name = str(id(declaration.var_type))
        self.total += f'{node_name} -> {type_node_name};\n'
        self.visit_ast(declaration.var_type)
        for variable in declaration.variables:
            variable_node_name = str(id(variable))
            self.total += f'{node_name} -> {variable_node_name};\n'
            self.visit_ast(variable)

    def visit_type(self, type_node):
        node_name = str(id(type_node))
        label = f"Type\\nbase_type: {type_node.base_type}\\ntype_qualifier: {type_node.type_qualifier}\\npointer_qualifiers: {type_node.pointer_qualifiers}"
        self.total += f'{node_name} [label="{label}"];\n'

    def visit_variable(self, variable):
        node_name = str(id(variable))
        label = f"Variable\\nidentifier: {variable.identifier}"
        self.total += f'{node_name} [label="{label}"];\n'
        if variable.initializer is not None:
            initializer_node_name = str(id(variable.initializer))
            self.total += f'{node_name} -> {initializer_node_name};\n'
            self.visit_ast(variable.initializer)

    def visit_cast_expression(self, cast_expression):
        node_name = str(id(cast_expression))
        self.total += f'{node_name} [label="CastExpression"];\n'
        type_node_name = str(id(cast_expression.cast_type))
        self.total += f'{node_name} -> {type_node_name};\n'
        self.visit_ast(cast_expression.cast_type)
        expression_node_name = str(id(cast_expression.expression))
        self.total += f'{node_name} -> {expression_node_name};\n'
        self.visit_ast(cast_expression.expression)

    def visit_assignment(self, expr: EXPR.Assignment) -> Any:
        node_name = str(id(expr))
        label = "Assignment"
        self.total += f'{node_name} [label="{label}"];\n'

        # Handling the left-hand side of the assignment
        left_node_name = str(id(expr.left))
        self.total += f'{node_name} -> {left_node_name};\n'
        self.visit_ast(expr.left)

        # Handling the right-hand side of the assignment
        right_node_name = str(id(expr.right))
        self.total += f'{node_name} -> {right_node_name};\n'
        self.visit_ast(expr.right)

    def gen_binary_dot(self, me: EXPR.BinaryOperation, operator_str: str) -> None:
        node_name = str(id(me))
        self.total += f"{node_name} [label=\"{operator_str}\"];\n"
        left_node_name = str(id(me.left))
        right_node_name = str(id(me.right))
        self.total += f"{node_name} -> {left_node_name};\n"
        self.total += f"{node_name} -> {right_node_name};\n"
        self.visit_ast(me.left)
        self.visit_ast(me.right)

    def visit_binary_arithmetic(self, expr: EXPR.BinaryArithmetic) -> Any:
        node_name = str(id(expr))
        operator_str = expr.operator.name
        self.total += f'{node_name} [label="{operator_str}"];\n'
        left_node_name = str(id(expr.left))
        right_node_name = str(id(expr.right))
        self.total += f"{node_name} -> {left_node_name};\n"
        self.total += f"{node_name} -> {right_node_name};\n"
        self.visit_ast(expr.left)
        self.visit_ast(expr.right)

    def visit_binary_bitwise_arithmetic(self, expr: EXPR.BinaryBitwiseArithmetic) -> Any:
        self.gen_binary_dot(expr, expr.operator.name)

    def visit_binary_logical_operation(self, expr: EXPR.BinaryLogicalOperation) -> Any:
        self.gen_binary_dot(expr, expr.operator.name)

    def visit_comparison_operation(self, expr: EXPR.ComparisonOperation) -> Any:
        self.gen_binary_dot(expr, expr.operator.name)

    def visit_shift_expression(self, expr: EXPR.ShiftExpression) -> Any:
        node_name = str(id(expr))
        label = f"{expr.operator.name}"
        self.total += f"{node_name} [label=\"{label}\"];\n"

        value_node_name = str(id(expr.value))
        self.total += f"{node_name} -> {value_node_name};\n"
        self.visit_ast(expr.value)

        shamt_node_name = str(id(expr.amount))
        self.total += f"{node_name} -> {shamt_node_name};\n"
        self.visit_ast(expr.amount)

    def visit_unary_expression(self, expr: EXPR.UnaryExpression) -> Any:
        node_name = str(id(expr))
        operator_str = expr.operator.name
        self.total += f"{node_name} [label=\"{operator_str}\"];\n"

        operand_node_name = str(id(expr.value))
        self.total += f"{node_name} -> {operand_node_name};\n"
        self.visit_ast(expr.value)

    def visit_int(self, expr: EXPR.INT) -> Any:
        node_name = id(expr)
        self.total += f"{node_name} [label=\"{expr.value}\"];\n"

    def visit_float(self, expr: EXPR.FLOAT) -> Any:
        node_name = id(expr)
        self.total += f"{node_name} [label=\"{expr.value}\"];\n"

    def visit_char(self, expr: EXPR.CHAR) -> Any:
        node_name = id(expr)
        self.total += f"{node_name} [label=\"'{expr.value}'\"];\n"

    def visit_variable_reference(self, expr: EXPR.VariableReference) -> Any:
        node_name = id(expr)
        self.total += f"{node_name} [label=\"{expr.identifier}\"];\n"

    def visit_symbol_table(self, symbol_table, parent_id=None):
        # Generate a unique identifier for the symbol table node
        table_node_id = f"symbol_table_{id(symbol_table)}"

        # Label the node with the scope name and level
        label = f"SymbolTable: {symbol_table.scope_name} (Level: {symbol_table.scope_level})"
        self.total += f'{table_node_id} [label="{label}", shape=box];\n'

        # If there's a parent symbol table, add an edge from the parent to this symbol table
        if parent_id is not None:
            self.total += f'{parent_id} -> {table_node_id};\n'

        # Visit symbols within this symbol table
        for symbol_name, symbol in symbol_table.symbols.items():
            symbol_node_id = f"symbol_{id(symbol)}"
            symbol_label = f"{symbol_name} (Type: {symbol.type}, Level: {symbol.scope_level})"
            self.total += f'{symbol_node_id} [label="{symbol_label}", shape=ellipse];\n'
            self.total += f'{table_node_id} -> {symbol_node_id};\n'

        # Recursively visit child symbol tables
        for child in symbol_table.children:
            self.visit_symbol_table(child, table_node_id)