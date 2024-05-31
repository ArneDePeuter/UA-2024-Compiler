from dataclasses import dataclass
import uuid
from contextlib import contextmanager
import re
from typing import Optional
from typing import Union

from mipslite.module import Module
from mipslite.function import Function
from mipslite.block import Block
from mipslite.allocator import Allocator
from mipslite.type import Int, Float, Char, Array, Pointer, Struct, Any
from mipslite.register_manager import Register

from compiler.core.ast_visitor import AstVisitor
from compiler.core import ast


@dataclass
class ExpressionEval:
    l_value: Optional[Register] = None
    r_value: Optional[Register] = None


class MIPSGenerator(AstVisitor):
    def __init__(self):
        super().__init__()
        self.module = Module()
        self.builder = None
        self.variable_addresses = {}
        self.while_fd = {}
        self.structs = {}
        self.functions = {}

    @contextmanager
    def eval(self, expression: ast.Expression) -> ExpressionEval:
        eval_result = self.visit_expression(expression)
        right_reg_expr = eval_result.r_value
        left_reg_expr = eval_result.l_value
        try:
            yield eval_result
        finally:
            if right_reg_expr in self.module.register_manager.used_registers['temp'] or right_reg_expr in \
                    self.module.register_manager.used_registers['float']:
                self.module.register_manager.free(right_reg_expr)
            if left_reg_expr in self.module.register_manager.used_registers['temp'] or left_reg_expr in \
                    self.module.register_manager.used_registers['float']:
                self.module.register_manager.free(left_reg_expr)

    def generate_mips(self, node):
        self.visit_program(node)
        result = str(self.module)
        lines = result.split("\n")
        return "\n".join(lines)

    def visit_variable_declaration_global(self, node: ast.VariableDeclaration):
        var_type = self.visit_type(node.var_type)

        for qualifier in node.qualifiers:
            if qualifier.initializer is None:
                value = None
            else:
                with self.eval(qualifier.initializer) as eval:
                    value = eval.r_value

            self.module.global_variable(qualifier.identifier, var_type, value)
            self.variable_addresses[qualifier.identifier] = qualifier.identifier

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
        func = self.module.function(node.name, self.visit_type(node.return_type))
        self.functions[node.name] = func
        self.builder = func
        for i, parameter in enumerate(node.parameters):
            param_type = self.visit_type(parameter.type)
            self.variable_addresses[parameter.name] = self.builder.allocate(param_type)
            self.builder.store(f"$a{len(node.parameters) - i - 1}", self.variable_addresses[parameter.name])
        self.visit_body(node.body)
        self.builder = None

    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        # unused
        ...

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        var_type = self.visit_type(node.var_type)

        for qualifier in node.qualifiers:
            allocation_address = self.builder.allocate(var_type)
            self.variable_addresses[qualifier.identifier] = allocation_address

            if qualifier.initializer is None:
                # leave the variable uninitialised
                return

            with self.eval(qualifier.initializer) as eval:
                # we only care about the r_value
                reg = eval.r_value
                initializer_type = reg.type

                # Handle implicit conversion if necessary
                if isinstance(var_type, Float) and isinstance(initializer_type, Int):
                    float_reg = self.module.register_manager.allocate_float()
                    self.builder.add_instruction(f"mtc1 {reg.r_value}, {float_reg}")
                    self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                    self.builder.store_float(float_reg, allocation_address)
                    self.module.register_manager.free(float_reg)
                elif isinstance(var_type, Int) and isinstance(initializer_type, Float):
                    float_reg = self.module.register_manager.allocate_float()
                    self.builder.add_instruction(f"cvt.w.s {float_reg}, {reg.r_value}")
                    int_reg = self.module.register_manager.allocate_temp()
                    self.builder.add_instruction(f"mfc1 {int_reg}, {float_reg}")
                    self.builder.store(int_reg, allocation_address)
                    self.module.register_manager.free(float_reg)
                    self.module.register_manager.free(int_reg)
                elif isinstance(var_type, Float):
                    self.builder.store_float(reg.r_value, allocation_address)
                else:
                    self.builder.store(reg.r_value, allocation_address)

    def get_array_dimensions(self, array_initializer: ast.ArrayInitializer):
        def get_dimensions(node, depth):
            if isinstance(node, ast.ArrayInitializer):
                if len(node.elements) == 0:
                    return [0]
                else:
                    sub_dimensions = get_dimensions(node.elements[0], depth + 1)
                    return [len(node.elements)] + sub_dimensions
            else:
                return []
        return get_dimensions(array_initializer, 0)

    def get_array_access_identifier(self, array_access_node):
        target_node = array_access_node.target
        while isinstance(target_node, ast.ArrayAccess):
            target_node = target_node.target
        if isinstance(target_node, ast.IDENTIFIER):
            return target_node.name
        else:
            raise ValueError(f"Unexpected node type in array access target: {type(target_node)}")

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        with self.eval(node.left) as left_eval, self.eval(node.right) as right_eval:
            if not left_eval.l_value:
                raise NotImplementedError("Cannot assign value to variable, l_value is None")
            if not right_eval.r_value:
                raise NotImplementedError("Cannot assign value to variable, r_value is None")

            left_type = left_eval.l_value.type
            right_type = right_eval.r_value.type

            # Type checking pointer, and safety checks for right-hand side
            if isinstance(left_type, Pointer) and not isinstance(right_type, Pointer):
                # Handle char* assignment
                if isinstance(right_type, Char):
                    self.builder.add_instruction(f"la {left_eval.r_value}, {right_eval.r_value}")
                else:
                    raise TypeError(f"Cannot assign value of type {right_type} to pointer of type {left_type}")

            value = right_eval.r_value

            # Type conversion and assignment
            if isinstance(left_type, Int) and isinstance(right_type, Float):
                # Convert float to int
                float_reg = right_eval.r_value
                int_reg = self.module.register_manager.allocate_temp()
                self.builder.add_instruction(f"cvt.w.s {float_reg}, {float_reg}")
                self.builder.add_instruction(f"mfc1 {int_reg}, {float_reg}")
                self.builder.add_instruction(f"move {left_eval.r_value}, {int_reg}")
                self.module.register_manager.free(int_reg)
            elif isinstance(left_type, Float) and isinstance(right_type, Int):
                # Convert int to float
                int_reg = right_eval.r_value
                float_reg = self.module.register_manager.allocate_float()
                self.builder.add_instruction(f"mtc1 {int_reg}, {float_reg}")
                self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                self.builder.add_instruction(f"mov.s {left_eval.r_value}, {float_reg}")
                self.module.register_manager.free(float_reg)

            self.builder.store(value, f"0({left_eval.l_value})")

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        if node.c_syntax:
            self.builder.current_block.add_instruction(f"# {node.c_syntax}")
        self.visit_expression(node.expression)

    def visit_int(self, node: ast.INT):
        reg = self.module.register_manager.allocate('temp', Int)
        self.builder.add_instruction(f"li {reg}, {node.value}")
        return ExpressionEval(r_value=reg)

    def visit_float(self, node: ast.FLOAT):
        reg = self.module.register_manager.allocate('float', Float)
        label = f"float_{id(node)}"
        float_data_block = self.module.data_block(label)
        float_data_block.add_instruction(f".float {node.value}")
        self.builder.add_instruction(f"l.s {reg}, {label}")
        return ExpressionEval(r_value=reg)

    def visit_char(self, node: ast.CHAR):
        reg = self.module.register_manager.allocate('temp', Char)
        self.builder.add_instruction(f"li {reg}, {ord(node.value)}")
        return ExpressionEval(r_value=reg)

    def visit_identifier(self, node: ast.IDENTIFIER):
        addr = self.variable_addresses[node.name]
        if addr.type == Float:
            reg = self.module.register_manager.allocate('float', Float)
        else:
            reg = self.module.register_manager.allocate('temp', addr.type)
        self.builder.load(reg, addr)
        addr_reg = self.module.register_manager.allocate('temp', addr.type)
        self.builder.add_instruction(f"la {addr_reg}, {addr}")
        return ExpressionEval(l_value=addr_reg, r_value=reg)

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        with self.eval(node.expression) as eval:
            target_type = self.visit_type(node.cast_type)
            r_value = eval.r_value
            source_type = r_value.type

            if isinstance(target_type, Float) and isinstance(source_type, Int):
                float_reg = self.module.register_manager.allocate('float', Float)
                self.builder.add_instruction(f"mtc1 {r_value}, {float_reg}")
                self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                self.builder.add_instruction(f"mov.s {float_reg}, {float_reg}")
                self.module.register_manager.free(float_reg)
                res = ExpressionEval(r_value=float_reg)
            elif isinstance(target_type, Int) and isinstance(source_type, Float):
                float_reg = self.module.register_manager.allocate('float', Float)
                self.builder.add_instruction(f"mov.s {float_reg}, {r_value}")
                int_reg = self.module.register_manager.allocate_temp()
                self.builder.add_instruction(f"cvt.w.s {float_reg}, {float_reg}")
                self.builder.add_instruction(f"mfc1 {int_reg}, {float_reg}")
                self.module.register_manager.free(float_reg)
                res = ExpressionEval(r_value=int_reg)
            elif isinstance(target_type, Char) and isinstance(source_type, Int):
                char_reg = self.module.register_manager.allocate('temp', Char)
                self.builder.add_instruction(f"andi {char_reg}, {r_value}, 0xFF")
                res = ExpressionEval(r_value=char_reg)
            elif isinstance(target_type, Int) and isinstance(source_type, Char):
                int_reg = self.module.register_manager.allocate('temp', Int)
                self.builder.add_instruction(f"seb {int_reg}, {r_value}")
                res = ExpressionEval(r_value=int_reg)
            else:
                result_reg = self.module.register_manager.allocate('temp', target_type)
                self.builder.add_instruction(f"move {result_reg}, {r_value}")
                res = ExpressionEval(r_value=result_reg)
        # we return here so context manager can free the used registers
        return res

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        with self.eval(node.left) as left, self.eval(node.right) as right:
            left = left.r_value
            right = right.r_value

            left_type = left.type
            right_type = right.type

            if isinstance(left_type, Float) or isinstance(right_type, Float):
                # cast to float if necessary
                if not isinstance(left_type, Float):
                    float_reg = self.module.register_manager.allocate('float', Float)
                    self.builder.add_instruction(f"mtc1 {left}, {float_reg}")
                    self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                    left = float_reg

                if not isinstance(right_type, Float):
                    float_reg = self.module.register_manager.allocate('float', Float)
                    self.builder.add_instruction(f"mtc1 {right}, {float_reg}")
                    self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                    right = float_reg

                result_reg = self.module.register_manager.allocate('float', Float)
                if node.operator == ast.BinaryArithmetic.Operator.PLUS:
                    self.builder.add_instruction(f"add.s {result_reg}, {left}, {right}")
                elif node.operator == ast.BinaryArithmetic.Operator.MINUS:
                    self.builder.add_instruction(f"sub.s {result_reg}, {left}, {right}")
                elif node.operator == ast.BinaryArithmetic.Operator.MUL:
                    self.builder.add_instruction(f"mul.s {result_reg}, {left}, {right}")
                elif node.operator == ast.BinaryArithmetic.Operator.DIV:
                    self.builder.add_instruction(f"div.s {result_reg}, {left}, {right}")
                ret = ExpressionEval(r_value=result_reg)
            else:
                result_reg = self.module.register_manager.allocate('temp', Int)
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
                ret = ExpressionEval(r_value=result_reg)
        # we return here so context manager can free the used registers
        return ret

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        with self.eval(node.left) as left, self.eval(node.right) as right:
            result_reg = self.module.register_manager.allocate('temp', Int)

            left = left.r_value
            right = right.r_value

            if node.operator == ast.BinaryBitwiseArithmetic.Operator.AND:
                self.builder.add_instruction(f"and {result_reg}, {left}, {right}")
            elif node.operator == ast.BinaryBitwiseArithmetic.Operator.OR:
                self.builder.add_instruction(f"or {result_reg}, {left}, {right}")
            elif node.operator == ast.BinaryBitwiseArithmetic.Operator.XOR:
                self.builder.add_instruction(f"xor {result_reg}, {left}, {right}")

        return ExpressionEval(r_value=result_reg)

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        with self.eval(node.left) as left, self.eval(node.right) as right:
            result_reg = self.module.register_manager.allocate_temp('temp', Int)

            left = left.r_value
            right = right.r_value

            if node.operator == ast.BinaryLogicalOperation.Operator.AND:
                self.builder.add_instruction(f"and {result_reg}, {left}, {right}")
            elif node.operator == ast.BinaryLogicalOperation.Operator.OR:
                self.builder.add_instruction(f"or {result_reg}, {left}, {right}")
        return ExpressionEval(r_value=result_reg)

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        with self.eval(node.left) as left, self.eval(node.right) as right:

            result_reg = self.module.register_manager.allocate_temp('temp', Int)
            left = left.r_value
            right = right.r_value

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
        return ExpressionEval(r_value=result_reg)

    def visit_unary_expression(self, node: ast.UnaryExpression):
        with self.eval(node.value) as value_eval:
            value = value_eval

            if node.operator == ast.UnaryExpression.Operator.POSITIVE:
                ret = ExpressionEval(r_value=value.r_value)
            elif node.operator == ast.UnaryExpression.Operator.NEGATIVE:
                result_reg = self.module.register_manager.allocate('temp', value.r_value.type)
                self.builder.add_instruction(f"neg {result_reg}, {value.r_value}")
                ret = ExpressionEval(r_value=result_reg)
            elif node.operator == ast.UnaryExpression.Operator.ONESCOMPLEMENT:
                result_reg = self.module.register_manager.allocate('temp', value.r_value.type)
                self.builder.add_instruction(f"not {result_reg}, {value.r_value}")
                ret = ExpressionEval(r_value=result_reg)
            elif node.operator == ast.UnaryExpression.Operator.LOGICALNEGATION:
                result_reg = self.module.register_manager.allocate('temp', Int)
                self.builder.add_instruction(f"seq {result_reg}, {value.r_value}, $zero")
                ret = ExpressionEval(r_value=result_reg)
            elif node.operator == ast.UnaryExpression.Operator.ADDRESSOF:
                r_reg = self.module.register_manager.allocate('temp', Pointer(value.l_value.type))
                self.builder.add_instruction(f"la {r_reg}, {value.l_value}")
                ret = ExpressionEval(r_value=r_reg)
            elif node.operator == ast.UnaryExpression.Operator.DEREFERENCE:
                r_reg = self.module.register_manager.allocate('temp', value.l_value.type.target)
                self.builder.add_instruction(f"lw {r_reg}, 0({value.r_value})")
                l_reg = self.module.register_manager.allocate('temp', value.l_value.type.target)
                self.builder.add_instruction(f"la {l_reg}, {value.r_value}")
                ret = ExpressionEval(l_value=l_reg, r_value=r_reg)
            elif node.operator == ast.UnaryExpression.Operator.INCREMENT:
                # TODO: pointer arithmetic
                reg = self.module.register_manager.allocate('temp', value.r_value.type)
                if not node.prefix:
                    # we need to return the value before the operation is done
                    self.builder.add_instruction(f"move {reg}, {value.r_value}")

                self.builder.add_instruction(f"addi {value.r_value}, {value.r_value}, 1")

                if node.prefix:
                    # we need the value after the opration is done
                    self.builder.add_instruction(f"move {reg}, {value.r_value}")

                self.builder.add_instruction(f"sw {value.r_value}, 0({value.l_value})")
                ret = ExpressionEval(r_value=reg)

            elif node.operator == ast.UnaryExpression.Operator.DECREMENT:
                # TODO: pointer arithmetic
                reg = self.module.register_manager.allocate('temp', value.r_value.type)
                if not node.prefix:
                    # we need to return the value before the operation is done
                    self.builder.add_instruction(f"move {reg}, {value.r_value}")

                self.builder.add_instruction(f"addi {value.r_value}, {value.r_value}, -1")

                if node.prefix:
                    # we need the value after the opration is done
                    self.builder.add_instruction(f"move {reg}, {value.r_value}")

                self.builder.add_instruction(f"sw {value.r_value}, 0({value.l_value})")
                ret = ExpressionEval(r_value=reg)
            else:
                raise NotImplementedError(f"Unary operator {node.operator} is not supported")
        # we return here so context manager can free the used registers
        return ret

    def visit_shift_expression(self, node: ast.ShiftExpression):
        with self.eval(node.value) as value, self.eval(node.amount) as amount:
            result_reg = self.module.register_manager.allocate('temp', value.r_value.type)

            value = value.r_value
            amount = amount.r_value

            if node.operator == ast.ShiftExpression.Operator.LEFT:
                self.builder.add_instruction(f"sllv {result_reg}, {value}, {amount}")
            elif node.operator == ast.ShiftExpression.Operator.RIGHT:
                self.builder.add_instruction(f"srlv {result_reg}, {value}, {amount}")

        return ExpressionEval(r_value=result_reg)

    def visit_function_call(self, node: ast.FunctionCall):
        arg_regs = []
        for arg in node.arguments:
            with self.eval(arg) as arg_eval:
                arg_reg = self.module.register_manager.allocate('arg', arg_eval.r_value.type)
                arg_regs.append(arg_reg)
                self.builder.add_instruction(f"move {arg_reg}, {arg_eval.r_value}")

        self.builder.add_instruction(f"jal {node.name}")
        self.builder.add_instruction("nop")

        for reg in reversed(arg_regs):
            self.module.register_manager.free(reg)

        return_type = self.functions[node.name].return_type
        if return_type == Float:
            result_reg = self.module.register_manager.allocate('float', Float)
            self.builder.add_instruction(f"mov.s {result_reg}, $f0")
        else:
            result_reg = self.module.register_manager.allocate('temp', return_type)
            self.builder.add_instruction(f"move {result_reg}, $v0")
        self.builder.add_instruction(f"move {result_reg}, $v0")
        return ExpressionEval(r_value=result_reg)

    def visit_string_literal(self, node: ast.ArrayInitializer):
        label = f"string_{uuid.uuid4().hex}"
        string_data_block = self.module.data_block(label)
        elements = []
        self.array_elements(node.elements, elements)
        # Remove the qoutes from the string
        elements= [element.replace('\'', '') for element in elements]
        string_data_block.add_instruction(f".asciiz \"{''.join(elements)}\"")
        # Now you should first store the address of the array in a register
        reg = self.module.register_manager.allocate('temp', Pointer(Char()))
        self.builder.add_instruction(f"la {reg}, {label}")
        return ExpressionEval(r_value=reg)

    def visit_printf_call(self, node: ast.PrintFCall):
        # Link the printf block
        label = f"printf_{uuid.uuid4().hex}"

        # Call the printf function to handle data and instruction generation
        args_eval = []
        for arg in node.args:
            if isinstance(arg, ast.ArrayInitializer):
                args_eval.append(self.visit_string_literal(arg))
            else:
                args_eval.append(self.visit_expression(arg))
        #args_eval = [self.visit_expression(arg) for arg in node.args] # This is a list of registers
        self.module.printf(label, node.format, args_eval)

        # Free the registers
        for reg in reversed(args_eval):
            self.module.register_manager.free(reg.r_value)

        # Add instruction to call the printf function
        self.builder.add_instruction(f"jal {label}")
        self.builder.add_instruction("nop")

    def visit_scanf_call(self, node: ast.ScanFCall):
        label = f"scanf_{uuid.uuid4().hex}"

        regs = [self.visit_expression(arg) for arg in node.args]
        self.module.scanf(label, node.format, regs)

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
                # Only append the element value if it is not zero-terminated
                if element.value != '\x00':
                    elements_list.append(repr(element.value))


    def visit_array_initializer(self, node: ast.ArrayInitializer):
        if node.struct_type:
            return self.visit_struct_initializer(node)
        label = f"array_{uuid.uuid4().hex}"
        array_block = self.module.data_block(label)
        elements = []
        self.array_elements(node.elements, elements)
        self.module.array(array_block, elements)
        # Now you should first store the address of the array in a register
        reg = self.module.register_manager.allocate('temp', Pointer(Any()))
        self.builder.add_instruction(f"la {reg}, {label}")
        return ExpressionEval(r_value=reg)

    def visit_array_access(self, node: ast.ArrayAccess):
        with self.eval(node.target) as base_eval, self.eval(node.index) as index_eval:
            base = base_eval.l_value
            index = index_eval.r_value

            l_reg = self.module.register_manager.allocate('temp', base_eval.r_value.type.target)
            self.builder.add_instruction(f"add {l_reg}, {base}, {index}")
            r_reg = self.module.register_manager.allocate('temp', base_eval.r_value.type.target)
            self.builder.add_instruction(f"lw {r_reg}, 0({l_reg})")

        return ExpressionEval(r_value=r_reg, l_value=l_reg)

    def visit_struct_definition(self, node: ast.StructDefinition):
        new_type = Struct(name=node.name, fields=[])
        self.structs[node.name] = new_type
        new_type.fields = [(member.name, self.visit_type(member.type)) for member in node.members]

    def visit_struct_initializer(self, node: ast.ArrayInitializer):
        raise NotImplementedError("Struct initializer not implemented")

    def visit_struct_access(self, node: ast.StructAccess):
        with self.eval(node.target) as target_eval:
            struct_type = target_eval.l_value.type
            offset = struct_type.get_member_offset(node.member_name)

            rval = self.module.register_manager.allocate('temp')
            self.builder.add_instruction(f"lw {rval}, {offset}({target_eval.l_value})")
            lval = self.module.register_manager.allocate('temp')
            self.builder.add_instruction(f"addi {lval}, {target_eval.l_value}, {offset}")
        return ExpressionEval(l_value=lval, r_value=rval)

    def visit_if_statement(self, node: ast.IfStatement):
        with self.eval(node.condition) as condition:
            if node.else_statement is None:
                with self.builder.if_then(condition.r_value):
                    self.visit_body(node.body)
            else:
                with self.builder.if_else(condition.r_value) as (true_block, false_block):
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
                with self.eval(node.expression) as condition_reg:
                    with start(condition_reg.r_value):
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
        with self.eval(node.expression) as result_eval:
            self.builder.add_instruction(f"move $v0, {result_eval.r_value}")
            # TODO: do a jump

    def visit_forward_declaration(self, node: ast.ForwardDeclaration):
        pass

    def visit_comment_statement(self, node: ast.CommentStatement):
        for line in node.content.split("\n"):
            self.builder.add_instruction(f"# {line}")

    def visit_type(self, node: ast.Type):
        mips_type = None
        if isinstance(node.type, ast.BaseType):
            if node.type == ast.BaseType.int:
                mips_type = Int()
            elif node.type == ast.BaseType.float:
                mips_type = Float()
            elif node.type == ast.BaseType.char:
                mips_type = Char()
            else:
                raise NotImplementedError(f"Base type {node.type} is not supported")

        elif isinstance(node.type, ast.ArrayType):
            mips_type = Array(self.visit_type(node.type.element_type), self.visit_array_specifier(node.type.array_sizes), node.type.array_sizes)
        elif isinstance(node.type, ast.StructType):
            mips_type = self.structs[node.type.definition.name]

        if node.address_qualifiers:
            for qualifier in node.address_qualifiers:
                if qualifier == ast.AddressQualifier.pointer:
                    mips_type = Pointer(mips_type)
        return mips_type
