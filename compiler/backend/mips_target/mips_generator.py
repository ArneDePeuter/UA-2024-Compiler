from mipslite.module import Module
from mipslite.function import Function
from mipslite.block import Block
from mipslite.allocator import Allocator
from mipslite.type import Int, Float, Char, Array, Pointer, Struct

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
        initializer_reg = self.visit_expression(node.initializer)
        self.variable_addresses[node.identifier] = initializer_reg

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        for qualifier in node.qualifiers:
            if qualifier.initializer is None:
                # Add a default initializer
                if node.var_type.type == ast.BaseType.int:
                    qualifier.initializer = ast.INT(0)
                elif node.var_type.type == ast.BaseType.float:
                    qualifier.initializer = ast.FLOAT(0.0)
                elif node.var_type.type == ast.BaseType.char:
                    qualifier.initializer = ast.CHAR('')
                else:
                    raise NotImplementedError("Only int, float and char are supported for default initializers")
            self.visit_variable_declaration_qualifier(qualifier)

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        right = self.visit_expression(node.right)
        left = self.visit_expression(node.left)
        addr = self.variable_addresses[node.left.name]
        self.builder.store(right, addr)

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
        reg = self.module.register_manager.allocate('temp')
        addr = self.variable_addresses[node.name]
        self.builder.add_instruction(f"move {reg}, {addr}")
        return reg

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        # Implement type casting logic if needed
        pass

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        left = self.visit_expression(node.left)
        right = self.visit_expression(node.right)

        result_reg = self.module.register_manager.allocate('temp')

        if node.operator == ast.BinaryArithmetic.Operator.PLUS:
            self.builder.add_instruction(f"add {result_reg}, {left}, {right}")
        elif node.operator == ast.BinaryArithmetic.Operator.MINUS:
            self.builder.add_instruction(f"sub {result_reg}, {left}, {right}")
        elif node.operator == ast.BinaryArithmetic.Operator.MUL:
            self.builder.add_instruction(f"mul {result_reg}, {left}, {right}")
        elif node.operator == ast.BinaryArithmetic.Operator.DIV:
            self.builder.add_instruction(f"div {result_reg}, {left}, {right}")
        elif node.operator == ast.BinaryArithmetic.Operator.MOD:
            self.builder.add_instruction(f"rem {result_reg}, {left}, {right}")

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
        self.builder.add_instruction(f"jal {node.name}")
        self.builder.add_instruction("nop")

    def visit_printf_call(self, node: ast.PrintFCall):
        # Link the printf block
        label = f"printf_{id(node)}"

        # Call the printf function to handle data and instruction generation
        args_eval = [self.visit_expression(arg) for arg in node.args] # This is a list of registers
        self.module.printf(label, node.format, args_eval)

        self.builder.add_instruction(f"jal {label}")
        self.builder.add_instruction("nop")

    def visit_scanf_call(self, node: ast.ScanFCall):
        # Link the scanf block
        label = f"scanf_{id(node)}"

        # Call the scanf function to handle data and instruction generation
        args_eval = [self.visit_expression(arg) for arg in node.args] # This is a list of registers
        self.module.scanf(label, node.format, args_eval)

        self.builder.add_instruction(f"jal {label}")
        self.builder.add_instruction("nop")

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
        self.visit_expression(node.expression)
        # The rest gets handled in the function block

    def visit_forward_declaration(self, node: ast.ForwardDeclaration):
        # Forward declaration is n/a for MIPS
        pass

    def visit_comment_statement(self, node: ast.CommentStatement):
        # Implement comment statement logic
        pass

    def visit_type(self, node: ast.Type):
        # Implement type logic
        pass