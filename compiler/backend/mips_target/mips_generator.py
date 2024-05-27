import uuid
from typing import Union
from mipslite.module import Module
from mipslite.function import Function
from mipslite.block import Block
from mipslite.allocator import Allocator
from mipslite.type import Int, Float, Char, Array, Pointer, Struct
from contextlib import contextmanager
import re

from compiler.core.ast_visitor import AstVisitor
from compiler.core import ast

class MIPSGenerator(AstVisitor):
    def __init__(self):
        super().__init__()
        self.module = Module()
        self.builder = None
        self.variable_addresses = {}
        self.var_types = {}
        self.while_fd = {}

    @contextmanager
    def get_expression_reg(self, expression: ast.Expression, module: Module):
        reg = self.visit_expression(expression)
        print(f"Allocated {reg} of type temp for expression {expression}")
        try:
            yield reg
        finally:
            if reg in module.register_manager.used_registers['temp'] or reg in module.register_manager.used_registers[
                'float']:
                module.register_manager.free(reg)
                print(f"Freed {reg} of type temp for expression {expression}")
            else:
                print(f"Warning: Attempted to free register {reg} which was not in use for expression {expression}")

    def generate_mips(self, node):
        self.visit_program(node)
        result = str(self.module)
        lines = result.split("\n")
        return "\n".join(lines)

    def visit_variable_declaration_global(self, node: ast.VariableDeclaration):
        var_type = self.visit_type(node.var_type)

        for qualifier in node.qualifiers:
            if qualifier.initializer is None:
                if node.var_type.type == ast.BaseType.int:
                    qualifier.initializer = ast.INT(0)
                elif node.var_type.type == ast.BaseType.float:
                    qualifier.initializer = ast.FLOAT(0.0)
                elif node.var_type.type == ast.BaseType.char:
                    qualifier.initializer = ast.CHAR('\0')
                else:
                    raise NotImplementedError("Only int, float, and char are supported for default initializers")

            initializer_value = qualifier.initializer.value

            if isinstance(initializer_value, int):
                value = initializer_value
            elif isinstance(initializer_value, float):
                value = hex(initializer_value)  # Convert float to hexadecimal representation
            elif isinstance(initializer_value, str) and len(initializer_value) == 1:
                value = ord(initializer_value)
            else:
                raise NotImplementedError("Unsupported initializer type")
            self.module.global_variable(qualifier.identifier, value)
            self.variable_addresses[qualifier.identifier] = qualifier.identifier
            self.var_types[qualifier.identifier] = var_type

    def visit_program(self, node: ast.Program):
        for statement in node.statements:
            if isinstance(statement, ast.VariableDeclaration):
                self.visit_variable_declaration_global(statement)
                continue
            self.visit_statement(statement)

    def visit_body(self, node: ast.Body):
        for statement in node.statements:
            self.visit_statement(statement)

    def visit_function_declaration(self, node: ast.FunctionDeclaration):
        func = self.module.function(node.name)
        self.builder = func
        for i, parameter in enumerate(node.parameters):
            param_type = self.visit_type(parameter.type)
            self.variable_addresses[parameter.name] = self.builder.allocate(param_type)
            self.var_types[parameter.name] = param_type
            self.builder.store(f"$a{len(node.parameters) - i - 1}", self.variable_addresses[parameter.name])
        self.var_types[node.name] = self.visit_type(node.return_type)
        self.visit_body(node.body)
        self.builder = None

    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        # unused
        ...

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        var_type = self.visit_type(node.var_type)
        for qualifier in node.qualifiers:
            if qualifier.initializer is None:
                if node.var_type.type == ast.BaseType.int:
                    qualifier.initializer = ast.INT(0)
                elif node.var_type.type == ast.BaseType.float:
                    qualifier.initializer = ast.FLOAT(0.0)
                elif node.var_type.type == ast.BaseType.char:
                    qualifier.initializer = ast.CHAR('\0')
                else:
                    raise NotImplementedError(f"Only int, float, and char are supported for default initializers, not {node.var_type.type}")
            allocation_address = self.builder.allocate(var_type)
            self.variable_addresses[qualifier.identifier] = allocation_address
            self.var_types[qualifier.identifier] = var_type

            with self.get_expression_reg(qualifier.initializer, self.module) as reg:
                # Determine the type of the initializer
                initializer_type = self.determine_type(qualifier.initializer)

                # Handle implicit conversion if necessary
                if isinstance(var_type, Float) and isinstance(initializer_type, Int):
                    float_reg = self.module.register_manager.allocate_float()
                    self.builder.add_instruction(f"mtc1 {reg}, {float_reg}")
                    self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                    self.builder.store_float(float_reg, allocation_address)
                    self.module.register_manager.free(float_reg)
                elif isinstance(var_type, Int) and isinstance(initializer_type, Float):
                    float_reg = self.module.register_manager.allocate_float()
                    self.builder.add_instruction(f"cvt.w.s {float_reg}, {reg}")
                    int_reg = self.module.register_manager.allocate_temp()
                    self.builder.add_instruction(f"mfc1 {int_reg}, {float_reg}")
                    self.builder.store(int_reg, allocation_address)
                    self.module.register_manager.free(float_reg)
                    self.module.register_manager.free(int_reg)
                elif isinstance(var_type, Float):
                    self.builder.store_float(reg, allocation_address)
                else:
                    self.builder.store(reg, allocation_address)

    def determine_type(self, expr):
        if isinstance(expr, ast.INT):
            return Int()
        elif isinstance(expr, ast.FLOAT):
            return Float()
        elif isinstance(expr, ast.CHAR):
            return Char()
        elif isinstance(expr, ast.IDENTIFIER):
            return self.var_types[expr.name]
        elif isinstance(expr, ast.TypeCastExpression):
            return self.visit_type(expr.cast_type)
        elif isinstance(expr, ast.UnaryExpression):
            expr_type = self.determine_type(expr.value)
            if expr.operator == ast.UnaryExpression.Operator.ADDRESSOF:
                return Pointer(expr_type)
            elif expr.operator == ast.UnaryExpression.Operator.DEREFERENCE:
                if isinstance(expr_type, Pointer):
                    return expr_type.target
                else:
                    raise TypeError(f"Cannot dereference non-pointer type {expr_type}")
            else:
                return expr_type
        elif isinstance(expr, ast.BinaryArithmetic):
            left_type = self.determine_type(expr.left)
            right_type = self.determine_type(expr.right)
            if isinstance(left_type, Float) or isinstance(right_type, Float):
                return Float()
            else:
                return Int()
        elif isinstance(expr, ast.FunctionCall):
            return self.var_types[expr.name]
        else:
            raise NotImplementedError(f"Type determination not implemented for {type(expr)}")

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        with self.get_expression_reg(node.right, self.module) as right_eval:
            if isinstance(node.left,
                          ast.UnaryExpression) and node.left.operator == ast.UnaryExpression.Operator.DEREFERENCE:
                # Handle dereferencing on the left side
                with self.get_expression_reg(node.left.value, self.module) as left_addr:
                    self.builder.add_instruction(f"sw {right_eval}, 0({left_addr})")
            else:
                with self.get_expression_reg(node.left, self.module) as left_eval:
                    if not left_eval.startswith('$'):
                        # If the left side is not a register, it should be an address
                        self.builder.add_instruction(f"sw {right_eval}, {left_eval}")
                    else:
                        # If the left side is a register, move the value from the right register to the left register
                        left_type = self.var_types[node.left.name]
                        right_type = self.determine_type(node.right)

                        if isinstance(left_type, Int) and isinstance(right_type, Float):
                            # Convert float to int
                            float_reg = right_eval
                            int_reg = self.module.register_manager.allocate_temp()
                            self.builder.add_instruction(f"cvt.w.s {float_reg}, {float_reg}")
                            self.builder.add_instruction(f"mfc1 {int_reg}, {float_reg}")
                            self.builder.add_instruction(f"move {left_eval}, {int_reg}")
                            self.module.register_manager.free(int_reg)
                        elif isinstance(left_type, Float) and isinstance(right_type, Int):
                            # Convert int to float
                            int_reg = right_eval
                            float_reg = self.module.register_manager.allocate_float()
                            self.builder.add_instruction(f"mtc1 {int_reg}, {float_reg}")
                            self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                            self.builder.add_instruction(f"mov.s {left_eval}, {float_reg}")
                            self.module.register_manager.free(float_reg)
                        else:
                            if isinstance(left_type, Float):
                                self.builder.add_instruction(f"mov.s {left_eval}, {right_eval}")
                            else:
                                self.builder.add_instruction(f"move {left_eval}, {right_eval}")

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        if node.c_syntax:
            self.builder.current_block.add_instruction(f"# {node.c_syntax}")
        self.visit_expression(node.expression)

    def visit_int(self, node: ast.INT):
        reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"li {reg}, {node.value}")
        return reg

    def visit_float(self, node: ast.FLOAT):
        reg = self.module.register_manager.allocate_float()
        label = f"float_{id(node)}"
        float_data_block = self.module.data_block(label)
        float_data_block.add_instruction(f".float {node.value}")
        self.builder.add_instruction(f"l.s {reg}, {label}")
        return reg

    def visit_char(self, node: ast.CHAR):
        reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"li {reg}, {ord(node.value)}")
        return reg

    def visit_identifier(self, node: ast.IDENTIFIER):
        addr = self.variable_addresses[node.name]
        if isinstance(self.var_types[node.name], Float):
            reg = self.module.register_manager.allocate_float()
            self.builder.load_float(reg, addr)
        else:
            reg = self.module.register_manager.allocate_temp()
            self.builder.load(reg, addr)
        return reg

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        with self.get_expression_reg(node.expression, self.module) as expr_reg:
            target_type = self.visit_type(node.cast_type)
            source_type = self.visit_type(node.expression)

            if isinstance(target_type, Float) and isinstance(source_type, Int):
                float_reg = self.module.register_manager.allocate_float()
                self.builder.add_instruction(f"mtc1 {expr_reg}, {float_reg}")
                self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                return float_reg
            elif isinstance(target_type, Int) and isinstance(source_type, Float):
                float_reg = self.module.register_manager.allocate_float()
                self.builder.add_instruction(f"mov.s {float_reg}, {expr_reg}")
                int_reg = self.module.register_manager.allocate_temp()
                self.builder.add_instruction(f"cvt.w.s {float_reg}, {float_reg}")
                self.builder.add_instruction(f"mfc1 {int_reg}, {float_reg}")
                self.module.register_manager.free(float_reg)
                return int_reg
            elif isinstance(target_type, Char) and isinstance(source_type, Int):
                char_reg = self.module.register_manager.allocate_temp()
                self.builder.add_instruction(f"andi {char_reg}, {expr_reg}, 0xFF")
                return char_reg
            else:
                return expr_reg

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        with self.get_expression_reg(node.left, self.module) as left, \
                self.get_expression_reg(node.right, self.module) as right:

            left_type = self.determine_type(node.left)
            right_type = self.determine_type(node.right)

            if isinstance(left_type, Float) or isinstance(right_type, Float):
                if not isinstance(left_type, Float):
                    with self.get_expression_reg(node.left, self.module) as float_left:
                        self.builder.add_instruction(f"mtc1 {left}, {float_left}")
                        self.builder.add_instruction(f"cvt.s.w {float_left}, {float_left}")
                        left = float_left

                if not isinstance(right_type, Float):
                    with self.get_expression_reg(node.right, self.module) as float_right:
                        self.builder.add_instruction(f"mtc1 {right}, {float_right}")
                        self.builder.add_instruction(f"cvt.s.w {float_right}, {float_right}")
                        right = float_right

                result_reg = self.module.register_manager.allocate_float()
                if node.operator == ast.BinaryArithmetic.Operator.PLUS:
                    self.builder.add_instruction(f"add.s {result_reg}, {left}, {right}")
                elif node.operator == ast.BinaryArithmetic.Operator.MINUS:
                    self.builder.add_instruction(f"sub.s {result_reg}, {left}, {right}")
                elif node.operator == ast.BinaryArithmetic.Operator.MUL:
                    self.builder.add_instruction(f"mul.s {result_reg}, {left}, {right}")
                elif node.operator == ast.BinaryArithmetic.Operator.DIV:
                    self.builder.add_instruction(f"div.s {result_reg}, {left}, {right}")
                return result_reg
            else:
                result_reg = self.module.register_manager.allocate_temp()
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
                return result_reg

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        with self.get_expression_reg(node.left, self.module) as left, \
                self.get_expression_reg(node.right, self.module) as right:
            result_reg = self.module.register_manager.allocate_temp()

            if node.operator == ast.BinaryBitwiseArithmetic.Operator.AND:
                self.builder.add_instruction(f"and {result_reg}, {left}, {right}")
            elif node.operator == ast.BinaryBitwiseArithmetic.Operator.OR:
                self.builder.add_instruction(f"or {result_reg}, {left}, {right}")
            elif node.operator == ast.BinaryBitwiseArithmetic.Operator.XOR:
                self.builder.add_instruction(f"xor {result_reg}, {left}, {right}")

        return result_reg

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        with self.get_expression_reg(node.left, self.module) as left, \
                self.get_expression_reg(node.right, self.module) as right:
            result_reg = self.module.register_manager.allocate_temp()
            if node.operator == ast.BinaryLogicalOperation.Operator.AND:
                self.builder.add_instruction(f"and {result_reg}, {left}, {right}")
            elif node.operator == ast.BinaryLogicalOperation.Operator.OR:
                self.builder.add_instruction(f"or {result_reg}, {left}, {right}")
            return result_reg


    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        with self.get_expression_reg(node.left, self.module) as left, \
                self.get_expression_reg(node.right, self.module) as right:
            result_reg = self.module.register_manager.allocate_temp()
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
            return result_reg

    def visit_unary_expression(self, node: ast.UnaryExpression):
        with self.get_expression_reg(node.value, self.module) as value:
            if node.operator == ast.UnaryExpression.Operator.POSITIVE:
                return value
            elif node.operator == ast.UnaryExpression.Operator.NEGATIVE:
                result_reg = self.module.register_manager.allocate_temp()
                self.builder.add_instruction(f"neg {result_reg}, {value}")
                return result_reg
            elif node.operator == ast.UnaryExpression.Operator.ONESCOMPLEMENT:
                result_reg = self.module.register_manager.allocate_temp()
                self.builder.add_instruction(f"not {result_reg}, {value}")
                return result_reg
            elif node.operator == ast.UnaryExpression.Operator.LOGICALNEGATION:
                result_reg = self.module.register_manager.allocate_temp()
                self.builder.add_instruction(f"seq {result_reg}, {value}, $zero")
                return result_reg
            elif node.operator == ast.UnaryExpression.Operator.ADDRESSOF:
                result_reg = self.module.register_manager.allocate_temp()
                addr = self.variable_addresses[node.value.name]
                self.builder.add_instruction(f"la {result_reg}, {addr}")
                return result_reg
            elif node.operator == ast.UnaryExpression.Operator.DEREFERENCE:
                result_reg = self.module.register_manager.allocate_temp()
                self.builder.add_instruction(f"lw {result_reg}, 0({value})")
                return result_reg
            elif node.operator == ast.UnaryExpression.Operator.INCREMENT:
                result_reg = self.module.register_manager.allocate_temp()
                self.builder.add_instruction(f"addi {result_reg}, {value}, 1")
                if not node.prefix:
                    return value
                return result_reg
            elif node.operator == ast.UnaryExpression.Operator.DECREMENT:
                result_reg = self.module.register_manager.allocate_temp()
                self.builder.add_instruction(f"addi {result_reg}, {value}, -1")
                if not node.prefix:
                    return value
                return result_reg
            else:
                raise NotImplementedError(f"Unary operator {node.operator} is not supported")

    def visit_shift_expression(self, node: ast.ShiftExpression):
        with self.get_expression_reg(node.value, self.module) as value, \
                self.get_expression_reg(node.amount, self.module) as amount:

            result_reg = self.module.register_manager.allocate_temp()

            if node.operator == ast.ShiftExpression.Operator.LEFT:
                self.builder.add_instruction(f"sllv {result_reg}, {value}, {amount}")
            elif node.operator == ast.ShiftExpression.Operator.RIGHT:
                self.builder.add_instruction(f"srlv {result_reg}, {value}, {amount}")

        return result_reg

    def visit_function_call(self, node: ast.FunctionCall):
        arg_regs = []
        for arg in node.arguments:
            with self.get_expression_reg(arg, self.module) as arg_eval:
                arg_reg = self.module.register_manager.allocate('arg')
                arg_regs.append(arg_reg)
                self.builder.add_instruction(f"move {arg_reg}, {arg_eval}")

        self.builder.add_instruction(f"jal {node.name}")
        self.builder.add_instruction("nop")

        for reg in reversed(arg_regs):
            self.module.register_manager.free(reg)

        result_reg = self.module.register_manager.allocate_temp()
        self.builder.add_instruction(f"move {result_reg}, $v0")
        return result_reg

    def visit_printf_call(self, node: ast.PrintFCall):
        # Link the printf block
        label = f"printf_{uuid.uuid4().hex}"

        # Call the printf function to handle data and instruction generation
        args_eval = [self.visit_expression(arg) for arg in node.args] # This is a list of registers
        self.module.printf(label, node.format, args_eval)

        for reg in reversed(args_eval):
            self.module.register_manager.free(reg)

        # Add instruction to call the printf function
        self.builder.add_instruction(f"jal {label}")
        self.builder.add_instruction("nop")

    def visit_scanf_call(self, node: ast.ScanFCall):
        label = f"scanf_{uuid.uuid4().hex}"

        regs = [self.visit_expression(arg) for arg in node.args]
        self.module.scanf(label, node.format, regs)

        for reg in reversed(regs):
            self.module.register_manager.free(reg)

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
        label = f"array_{uuid.uuid4().hex}"
        array_block = self.module.data_block(label)
        self.module.array(array_block, node.elements)
        elements = []
        self.array_elements(node.elements, elements)
        self.module.array(array_block, elements)
        # Now you should first store the address of the array in a register
        reg = self.module.register_manager.allocate('temp')
        self.builder.add_instruction(f"la {reg}, {label}")
        return reg

    def visit_array_access(self, node: ast.ArrayAccess):
        # TODO: context manager usage
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
        pass

    def visit_struct_initializer(self, node: ast.ArrayInitializer):
        pass

    def visit_struct_access(self, node: ast.StructAccess):
        pass

    def visit_if_statement(self, node: ast.IfStatement):
        with self.get_expression_reg(node.condition, self.module) as condition:
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
        with self.builder.while_loop() as (condition, start, labels):
            condition_label, start_label, end_label = labels
            self.while_fd[(node.line, node.position)] = (condition_label, end_label)
            with condition:
                with self.get_expression_reg(node.expression, self.module) as condition_reg:
                    with start(condition_reg):
                        self.visit_body(node.to_execute)


    def visit_break_statement(self, node: ast.BreakStatement):
        start_block, end_block = self.while_fd[(node.while_statement.line, node.while_statement.position)]
        self.builder.add_instruction(f"j {end_block}")
        self.builder.add_instruction("nop")

    def visit_continue_statement(self, node: ast.ContinueStatement):
        start_block, end_block = self.while_fd[(node.while_statement.line, node.while_statement.position)]
        self.builder.add_instruction(f"j {start_block}")
        self.builder.add_instruction("nop")

    def visit_return_statement(self, node: ast.ReturnStatement):
        with self.get_expression_reg(node.expression, self.module) as result_eval:
            self.builder.add_instruction(f"move $v0, {result_eval}")

    def visit_forward_declaration(self, node: ast.ForwardDeclaration):
        pass

    def visit_comment_statement(self, node: ast.CommentStatement):
        pass

    def visit_type(self, node: Union[ast.Type, ast.Expression]):
        if isinstance(node, ast.Type):
            if isinstance(node.type, ast.BaseType):
                if node.type == ast.BaseType.int:
                    base_type = Int()
                elif node.type == ast.BaseType.float:
                    base_type = Float()
                elif node.type == ast.BaseType.char:
                    base_type = Char()
                else:
                    raise NotImplementedError(f"Base type {node.type} is not supported")

                # Handle pointers
                if node.address_qualifiers:
                    for qualifier in node.address_qualifiers:
                        if qualifier == ast.AddressQualifier.pointer:
                            base_type = Pointer(base_type)
                return base_type
            elif isinstance(node.type, ast.ArrayType):
                return Array(self.visit_type(node.type.element_type), self.visit_array_specifier(node.type.array_sizes), node.type.array_sizes)
            elif isinstance(node.type, ast.StructType):
                return Struct(node.type.definition)
        elif isinstance(node, ast.INT):
            return Int()
        elif isinstance(node, ast.FLOAT):
            return Float()
        elif isinstance(node, ast.CHAR):
            return Char()
        elif isinstance(node, ast.IDENTIFIER):
            return self.var_types[node.name]
        elif isinstance(node, ast.BinaryArithmetic):
            left_type = self.visit_type(node.left)
            right_type = self.visit_type(node.right)
            if isinstance(left_type, Float) or isinstance(right_type, Float):
                return Float()
            else:
                return Int()
        elif isinstance(node, ast.TypeCastExpression):
            return self.visit_type(node.cast_type)
        else:
            raise NotImplementedError(f"Type visit not implemented for {type(node)}")
