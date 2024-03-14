from src.core.abstract_visitor import Visitor

class ASTPrintVisitor(Visitor):
    def __init__(self):
        super().__init__()

    def visit_program(self, program):
        print("Program:")
        for statement in program.statements:
            self.visit_ast(statement)

    def visit_main_function(self, main_function):
        print("MainFunction:")
        print(f"  return_type: {main_function.return_type}")
        print(f"  name: {main_function.name}")
        print(f"  parameters: {main_function.parameters}")
        self.visit_ast(main_function.body)

    def visit_compound_statement(self, compound_statement):
        print("CompoundStatement:")
        for statement in compound_statement.statements:
            self.visit_ast(statement)

    def visit_declaration(self, declaration):
        print("Declaration:")
        self.visit_ast(declaration.var_type)
        for variable in declaration.variables:
            self.visit_ast(variable)

    def visit_type(self, type_node):
        print("Type:")
        print(f"  base_type: {type_node.base_type}")
        print(f"  type_qualifier: {type_node.type_qualifier}")
        print(f"  pointer_qualifiers: {type_node.pointer_qualifiers}")

    def visit_variable(self, variable):
        print("Variable:")
        print(f"  identifier: {variable.identifier}")
        if variable.initializer is not None:
            self.visit_ast(variable.initializer)

    def visit_int(self, expr):
        print(f"INT: {expr.value}")

    def visit_float(self, expr):
        print(f"FLOAT: {expr.value}")

    def visit_char(self, expr):
        print(f"CHAR: {expr.value}")

    def visit_variable_reference(self, expr):
        print(f"VariableReference: {expr.identifier}")

    def visit_binary_arithmetic(self, expr):
        print("BinaryArithmetic:")
        print(f"  operator: {expr.operator}")
        self.visit_ast(expr.left)
        self.visit_ast(expr.right)

    def visit_binary_bitwise_arithmetic(self, expr):
        print("BinaryBitwiseArithmetic:")
        print(f"  operator: {expr.operator}")
        self.visit_ast(expr.left)
        self.visit_ast(expr.right)

    def visit_binary_logical_operation(self, expr):
        print("BinaryLogicalOperation:")
        print(f"  operator: {expr.operator}")
        self.visit_ast(expr.left)
        self.visit_ast(expr.right)

    def visit_cast_expression(self, expr):
        print("CastExpression:")
        self.visit_ast(expr.cast_type)
        self.visit_ast(expr.expression)

    def visit_comparison_operation(self, expr):
        print("ComparisonOperation:")
        print(f"  operator: {expr.operator}")
        self.visit_ast(expr.left)
        self.visit_ast(expr.right)

    def visit_shift_expression(self, expr):
        print("ShiftExpression:")
        print(f"  operator: {expr.operator}")
        self.visit_ast(expr.value)
        self.visit_ast(expr.amount)

    def visit_unary_expression(self, expr):
        print("UnaryExpression:")
        print(f"  operator: {expr.operator}")
        print(f"  prefix: {expr.prefix}")
        self.visit_ast(expr.value)