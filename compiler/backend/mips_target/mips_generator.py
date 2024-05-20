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
        # unused
        ...

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        # retrieve type of every qualifier
        type = self.visit_type(node.var_type)
        for qualifier in node.qualifiers:
            if qualifier.initializer is None:
                # Add a default initializer
                if node.var_type.type == ast.BaseType.int:
                    qualifier.initializer = ast.INT(0)
                elif node.var_type.type == ast.BaseType.float:
                    qualifier.initializer = ast.FLOAT(0.0)
                elif node.var_type.type == ast.BaseType.char:
                    qualifier.initializer = ast.CHAR('\0')
                else:
                    raise NotImplementedError("Only int, float and char are supported for default initializers")
            # allocate memory for the variable
            allocation_address = self.builder.allocate(type)
            # store in the variable addresses
            self.variable_addresses[qualifier.identifier] = allocation_address
            # visit the initializer and get register for the value
            reg = self.visit_expression(qualifier.initializer)
            # store the value in the memory
            if isinstance(type, Float):
                self.builder.store_double(reg, allocation_address)
            else:
                self.builder.store(reg, allocation_address)
            # free the register
            self.module.register_manager.free(reg)

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
        reg = self.module.register_manager.allocate('float')
        label = f"float_{id(node)}"
        float_data_block = self.module.data_block(label)
        float_data_block.add_instruction(f".double {node.value}")
        self.builder.add_instruction(f"l.d {reg}, {float_data_block.label}")
        return reg

    def visit_char(self, node: ast.CHAR):
        reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"li {reg}, {ord(node.value)}")
        return reg

    def visit_identifier(self, node: ast.IDENTIFIER):
        reg = self.module.register_manager.allocate('temp')
        addr = self.variable_addresses[node.name]
        self.builder.load(reg, addr)
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
        left = self.visit_expression(node.left)
        right = self.visit_expression(node.right)
        result_reg = self.module.register_manager.allocate('temp')

        if node.operator == ast.BinaryBitwiseArithmetic.Operator.AND:
            self.builder.add_instruction(f"and {result_reg}, {left}, {right}")
        elif node.operator == ast.BinaryBitwiseArithmetic.Operator.OR:
            self.builder.add_instruction(f"or {result_reg}, {left}, {right}")
        elif node.operator == ast.BinaryBitwiseArithmetic.Operator.XOR:
            self.builder.add_instruction(f"xor {result_reg}, {left}, {right}")

        self.module.register_manager.free(left)
        self.module.register_manager.free(right)
        return result_reg

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        left = self.visit_expression(node.left)
        right = self.visit_expression(node.right)
        result_reg = self.module.register_manager.allocate('temp')

        if node.operator == ast.BinaryLogicalOperation.Operator.AND:
            self.builder.add_instruction(f"and {result_reg}, {left}, {right}")
        elif node.operator == ast.BinaryLogicalOperation.Operator.OR:
            self.builder.add_instruction(f"or {result_reg}, {left}, {right}")

        self.module.register_manager.free(left)
        self.module.register_manager.free(right)
        return result_reg

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        left = self.visit_expression(node.left)
        right = self.visit_expression(node.right)
        result_reg = self.module.register_manager.allocate('temp')

        if node.operator == ast.ComparisonOperation.Operator.GT:
            self.builder.add_instruction(f"slt {result_reg}, {right}, {left}")
        elif node.operator == ast.ComparisonOperation.Operator.LT:
            self.builder.add_instruction(f"slt {result_reg}, {left}, {right}")
        elif node.operator == ast.ComparisonOperation.Operator.GTE:
            self.builder.add_instruction(f"slt {result_reg}, {left}, {right}")
            self.builder.add_instruction(f"xori {result_reg}, {result_reg}, 1")
        elif node.operator == ast.ComparisonOperation.Operator.LTE:
            self.builder.add_instruction(f"slt {result_reg}, {right}, {left}")
            self.builder.add_instruction(f"xori {result_reg}, {result_reg}, 1")
        elif node.operator == ast.ComparisonOperation.Operator.EQ:
            self.builder.add_instruction(f"seq {result_reg}, {left}, {right}")
        elif node.operator == ast.ComparisonOperation.Operator.NEQ:
            self.builder.add_instruction(f"sne {result_reg}, {left}, {right}")

        self.module.register_manager.free(left)
        self.module.register_manager.free(right)
        return result_reg

    def visit_unary_expression(self, node: ast.UnaryExpression):
        value = self.visit_expression(node.value)
        result_reg = self.module.register_manager.allocate('temp')

        if node.operator == ast.UnaryExpression.Operator.POSITIVE:
            self.builder.add_instruction(f"move {result_reg}, {value}")
        elif node.operator == ast.UnaryExpression.Operator.NEGATIVE:
            self.builder.add_instruction(f"neg {result_reg}, {value}")
        elif node.operator == ast.UnaryExpression.Operator.ONESCOMPLEMENT:
            self.builder.add_instruction(f"not {result_reg}, {value}")
        elif node.operator == ast.UnaryExpression.Operator.LOGICALNEGATION:
            self.builder.add_instruction(f"seq {result_reg}, {value}, $zero")

        self.module.register_manager.free(value)
        return result_reg

    def visit_shift_expression(self, node: ast.ShiftExpression):
        value = self.visit_expression(node.amount)
        amount = self.visit_expression(node.value)

        result_reg = self.module.register_manager.allocate('temp')

        if node.operator == ast.ShiftExpression.Operator.LEFT:
            self.builder.add_instruction(f"sll {result_reg}, {value}, {amount}")
        elif node.operator == ast.ShiftExpression.Operator.RIGHT:
            self.builder.add_instruction(f"srl {result_reg}, {value}, {amount}")

        self.module.register_manager.free(value)
        self.module.register_manager.free(amount)

        return result_reg

    def visit_function_call(self, node: ast.FunctionCall):
        self.builder.add_instruction(f"jal {node.name}")
        self.builder.add_instruction("nop")

    def visit_printf_call(self, node: ast.PrintFCall):
        # Link the printf block
        label = f"printf_{id(node)}"

        # Call the printf function to handle data and instruction generation
        args_eval = [self.visit_expression(arg) for arg in node.args] # This is a list of registers
        self.module.printf(label, node.format, args_eval)

        # TODO: When arg is a string this will not work

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
        condition = self.visit_expression(node.condition) # This will contain the register with the result of the condition
        if_block = self.module.text_block(f"if_{id(node)}")
        funct_block = self.builder
        self.builder = if_block
        self.visit_body(node.body)
        if_block.add_instruction(f"j {funct_block.label}")
        if node.else_statement:
            self.visit_else_statement(node.else_statement)
        self.builder = funct_block

        # Add the branch instruction
        self.builder.add_instruction(f"bne {condition}, $zero, {if_block.label}")
        self.module.register_manager.free(condition)

    def visit_else_statement(self, node: ast.ElseStatement):
        ...

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
        if node.type == ast.BaseType.int:
            return Int()
        elif node.type == ast.BaseType.float:
            return Float()
        elif node.type == ast.BaseType.char:
            return Char()
        else:
            raise NotImplementedError("Only int, float and char are supported for default initializers")

