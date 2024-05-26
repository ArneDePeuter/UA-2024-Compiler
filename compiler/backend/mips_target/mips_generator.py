import uuid

from mipslite.module import Module
from mipslite.function import Function
from mipslite.block import Block
from mipslite.allocator import Allocator
from mipslite.type import Int, Float, Char, Array, Pointer, Struct
from contextlib import contextmanager

from compiler.core.ast_visitor import AstVisitor
from compiler.core import ast


class MIPSGenerator(AstVisitor):
    def __init__(self):
        super().__init__()
        self.module = Module()
        self.builder = None
        self.variable_addresses = {}
        self.var_types = {}

    @contextmanager
    def get_expression_reg(self, expression: ast.Expression, module: Module):
        reg = self.visit_expression(expression)
        yield reg
        module.register_manager.free(reg)

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
        for i, parameter in enumerate(node.parameters):
            # Allocate memory for the parameter and Store the address in the variable addresses
            self.variable_addresses[parameter.name] = self.builder.allocate(self.visit_type(parameter.type))
            self.var_types[parameter.name] = self.visit_type(parameter.type)
            self.builder.store(f"$a{len(node.parameters)-i-1}", self.variable_addresses[parameter.name])
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
            self.var_types[qualifier.identifier] = type
            # visit the initializer and get register for the value
            reg = self.visit_expression(qualifier.initializer)
            # store the value in the memory
            if isinstance(type, Float):
                self.builder.store_float(reg, allocation_address)
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
        float_data_block.add_instruction(f".float {node.value}")
        self.builder.add_instruction(f"l.s {reg}, {float_data_block.label}")
        return reg

    def visit_char(self, node: ast.CHAR):
        reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"li {reg}, {ord(node.value)}")
        return reg

    def visit_identifier(self, node: ast.IDENTIFIER):
        addr = self.variable_addresses[node.name]
        if isinstance(self.var_types[node.name], Float):
            reg = self.module.register_manager.allocate('float')
            self.builder.load_float(reg, addr)
        else:
            reg = self.module.register_manager.allocate('temp')
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
        # Evaluate the arguments only if the function never has been called
        regs = []
        for arg in node.arguments:
            with self.get_expression_reg(arg, self.module) as arg_eval:
                arg_reg = self.module.register_manager.allocate('arg')
                regs.append(arg_reg)
                self.builder.add_instruction(f"move {arg_reg}, {arg_eval}")

        # Call the function
        self.builder.add_instruction(f"jal {node.name}")
        self.builder.add_instruction("nop")

        # Free the argument registers
        for reg in reversed(regs):
            self.module.register_manager.free(reg)

        reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"move {reg}, $v0")
        return reg

    def visit_printf_call(self, node: ast.PrintFCall):
        # Link the printf block
        label = f"printf_{uuid.uuid4().hex}"

        # Call the printf function to handle data and instruction generation
        args_eval = [self.visit_expression(arg) for arg in node.args] # This is a list of registers
        self.module.printf(label, node.format, args_eval)

        # TODO: When arg is a string this will not work

        self.builder.add_instruction(f"jal {label}")
        self.builder.add_instruction("nop")

    def visit_scanf_call(self, node: ast.ScanFCall):
        # Link the scanf block
        label = f"scanf_{uuid.uuid4().hex}"

        # Call the scanf function to handle data and instruction generation
        args_eval = [self.visit_expression(arg) for arg in node.args] # This is a list of registers
        self.module.scanf(label, node.format, args_eval)

        self.builder.add_instruction(f"jal {label}")
        self.builder.add_instruction("nop")

    def visit_array_specifier(self, node: ast.ArraySpecifier):
        total_size = 1
        for size in node.sizes:
            if isinstance(size, ast.INT):
                total_size *= size.value
            else:
                NotImplementedError("Only int is supported for array sizes")
        return total_size


    def array_elements(self, elements, elements_list=[]):
        for element in elements:
            if isinstance(element, ast.ArrayInitializer):
                self.array_elements(element.elements, elements_list)
            else:
                elements_list.append(repr(element.value))


    def visit_array_initializer(self, node: ast.ArrayInitializer):
        if node.struct_type:
            return self.visit_struct_initializer(node)
        # Store the array data in the data block
        label = f"array_{uuid.uuid4().hex}"
        array_block = self.module.data_block(label)
        elements = []
        self.array_elements(node.elements, elements)
        self.module.array(array_block, elements)
        # Now you should first store the address of the array in a register
        reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"la {reg}, {label}")
        return reg

    def visit_array_access(self, node: ast.ArrayAccess):
        base = node
        indices = []
        while isinstance(base, ast.ArrayAccess):
            indices.append(base.index)
            base = base.target
        indices.reverse()

        array_name = None
        if isinstance(base, ast.IDENTIFIER):
            array_name = base.name

        # Get the type of the array
        array_type = self.var_types[array_name]

        # Compute the dimensions
        dimensions = []
        for dim in array_type.dimensions.sizes:
            dimensions.append(dim.value)

        # Compute the offset
        offset = 0
        for i, index in enumerate(indices):
            stride = array_type.target.width
            for dim in dimensions[i + 1:]:
                stride *= dim
            offset += index.value * stride

        # Load the frame address into a register
        base_reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"lw {base_reg}, {self.variable_addresses[array_name]}")
        # Load the value into another register
        offset_reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"li {offset_reg}, {offset}")
        # Compute the target address
        target_reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"add {target_reg}, {base_reg}, {offset_reg}")
        # Laad the resulut in a new register
        result_reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"lw {result_reg}, 0({target_reg})")

        self.module.register_manager.free(base_reg)
        self.module.register_manager.free(offset_reg)
        self.module.register_manager.free(target_reg)

        # TODO: return (target_reg, result_reg)

        return result_reg
    def visit_struct_definition(self, node: ast.StructDefinition):
        # Implement struct definition logic
        pass

    def visit_struct_initializer(self, node: ast.ArrayInitializer):
        # Implement struct initializer logic
        pass

    def visit_struct_access(self, node: ast.StructAccess):
        # Implement struct access logic
        pass

    def visit_if_statement(self, node: ast.IfStatement):
        condition = self.visit_expression(node.condition)
        if node.else_statement is None:
            with self.builder.if_then(condition):
                self.visit_body(node.body)
        else:
            with self.builder.if_else(condition) as (true_block, false_block):
                with true_block:
                    self.visit_body(node.body)
                with false_block:
                    self.visit_else_statement(node.else_statement)

    def visit_else_statement(self, node: ast.ElseStatement):
        if isinstance(node, ast.IfStatement):
            self.visit_if_statement(node)
        else:
            self.visit_body(node.body)

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
        result_eval = self.visit_expression(node.expression)
        self.builder.add_instruction(f"move $v0, {result_eval}")
        self.module.register_manager.free(result_eval)

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
        elif isinstance(node.type, ast.ArrayType):
            return Array(self.visit_type(node.type.element_type), self.visit_array_specifier(node.type.array_sizes), node.type.array_sizes)
        else:
            raise NotImplementedError("Only int, float and char are supported for default initializers")

