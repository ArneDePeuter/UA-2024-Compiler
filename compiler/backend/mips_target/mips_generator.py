from mipslite.module import Module
from mipslite.function import Function
from mipslite.block import Block
from mipslite.allocator import Allocator

from compiler.core.ast_visitor import AstVisitor
from compiler.core import ast

class MIPSGenerator(AstVisitor):
    def __init__(self):
        super().__init__()
        self.module = Module()
        self.builder = None
        self.variable_addresses = {}


    def generate_mips(self, node):
        self.visit_program(node)
        result = str(self.module)
        lines = result.split("\n")
        return "\n".join(lines)

    def visit_program(self, node: ast.Program):
        for statement in node.statements:
            self.visit_statement(statement)

    def visit_body(self, node: ast.Body):
        for statement in node.statements:
            self.visit_statement(statement)

    def visit_function_declaration(self, node: ast.FunctionDeclaration):
        func = self.module.function(node.name)
        self.builder = func
        self.visit_body(node.body)
        self.builder = None

    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        initializer = self.visit_expression(node.initializer)
        addr = self.variable_addresses[node.identifier]
        self.builder.store(addr, initializer)
        self.module.register_manager.free(initializer)

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        addr = self.builder.allocate(4)  # Assuming 4 bytes for simplicity
        for qualifier in node.qualifiers:
            self.variable_addresses[qualifier.identifier] = addr
            self.visit_variable_declaration_qualifier(qualifier)

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        right = self.visit_expression(node.right)
        left = self.visit_expression(node.left)
        addr = self.variable_addresses[node.left.name]
        self.builder.store(right, addr)
        self.module.register_manager.free(right)

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        self.visit_expression(node.expression)

    def visit_int(self, node: ast.INT):
        reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"li {reg}, {node.value}")
        return reg

    def visit_float(self, node: ast.FLOAT):
        reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"li.s {reg}, {node.value}")
        return reg

    def visit_char(self, node: ast.CHAR):
        reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"li {reg}, {ord(node.value)}")
        return reg

    def visit_identifier(self, node: ast.IDENTIFIER):
        reg = self.module.register_manager.allocate()
        addr = self.variable_addresses[node.name]
        self.builder.load(reg, addr)
        return reg

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        # Implement type casting logic if needed
        pass

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        left = self.visit_expression(node.left)
        right = self.visit_expression(node.right)

        left_value = left
        right_value = right

        result_reg = self.module.register_manager.allocate()

        if node.operator == ast.BinaryArithmetic.Operator.PLUS:
            self.builder.fadd(result_reg, left, right)
        elif node.operator == ast.BinaryArithmetic.Operator.MINUS:
            self.builder.fsub(result_reg, left, right)
        # Add more operators as needed

        self.module.register_manager.free(left)
        self.module.register_manager.free(right)
        return result_reg

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        # Implement bitwise arithmetic logic
        pass

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        # Implement logical operation logic
        pass

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        # Implement comparison operation logic
        pass

    def visit_unary_expression(self, node: ast.UnaryExpression):
        # Implement unary expression logic
        pass

    def visit_shift_expression(self, node: ast.ShiftExpression):
        # Implement shift expression logic
        pass

    def visit_function_call(self, node: ast.FunctionCall):
        # Implement function call logic
        pass

    def visit_printf_call(self, node: ast.PrintFCall):
        # Link the printf block
        self.builder.add_instruction("jal printf")
        self.builder.add_instruction("nop")

        # Call the printf function to handle data and instruction generation
        self.module.printf(node.format, node.args)


    def visit_scanf_call(self, node: ast.ScanFCall):
        # Implement scanf call logic
        pass

    def visit_array_specifier(self, node: ast.ArraySpecifier):
        # Implement array specifier logic
        pass

    def visit_array_initializer(self, node: ast.ArrayInitializer):
        # Implement array initializer logic
        pass

    def visit_array_access(self, node: ast.ArrayAccess):
        # Implement array access logic
        pass

    def visit_struct_definition(self, node: ast.StructDefinition):
        # Implement struct definition logic
        pass

    def visit_struct_access(self, node: ast.StructAccess):
        # Implement struct access logic
        pass

    def visit_if_statement(self, node: ast.IfStatement):
        # Implement if statement logic
        pass

    def visit_else_statement(self, node: ast.ElseStatement):
        # Implement else statement logic
        pass

    def visit_while_statement(self, node: ast.WhileStatement):
        # Implement while statement logic
        pass

    def visit_break_statement(self, node: ast.BreakStatement):
        # Implement break statement logic
        pass

    def visit_continue_statement(self, node: ast.ContinueStatement):
        # Implement continue statement logic
        pass

    def visit_return_statement(self, node: ast.ReturnStatement):
        value = self.visit_expression(node.expression)
        self.builder.ret(value)

    def visit_forward_declaration(self, node: ast.ForwardDeclaration):
        # Implement forward declaration logic
        pass

    def visit_comment_statement(self, node: ast.CommentStatement):
        # Implement comment statement logic
        pass

    def visit_type(self, node: ast.Type):
        # Implement type logic
        pass