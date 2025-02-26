from dataclasses import dataclass
import uuid
from contextlib import contextmanager
from typing import Optional

from mipslite.module import Module
from mipslite.function import Function
from mipslite.block import Block
from mipslite.type import Int, Float, Char, Array, Pointer, Struct, Any, Void
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
        self.builder: Block|Function = None
        self.variable_addresses = {}
        self.while_fd = {}
        self.structs = {}
        self.functions = {}

    @contextmanager
    def eval(self, expression: ast.Expression) -> ExpressionEval:
        eval_result = self.visit_expression(expression)
        try:
            yield eval_result
        finally:
            if eval_result is None:
                return
            right_reg_expr = eval_result.r_value
            left_reg_expr = eval_result.l_value
            if right_reg_expr:
                self.module.register_manager.free(right_reg_expr)
            if left_reg_expr:
                self.module.register_manager.free(left_reg_expr)

    def visit_expression(self, node: ast.Expression):
        if self.builder is None or (isinstance(self.builder, Function) and self.builder.current_block is None):
            return super().visit_expression(node)
        else:
            if node.c_syntax is None:
                return super().visit_expression(node)
            for line in node.c_syntax.split("\n"):
                self.builder.comment(line)
            return super().visit_expression(node)

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
                self.builder = self.module.global_blocks
                with self.eval(qualifier.initializer) as eval:
                    value = eval.r_value
                self.builder.store_word(value, qualifier.identifier)
                self.builder = None


            self.module.global_variable(qualifier.identifier, var_type)
            self.variable_addresses[qualifier.identifier] = Register(qualifier.identifier, var_type)

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
        # if not forward declared create function and add to dict
        if node.name not in self.functions:
            func = self.module.function(node.name, self.visit_type(node.return_type))
            self.functions[node.name] = func
        self.builder = self.functions[node.name]
        for i, parameter in enumerate(node.parameters):
            param_type = self.visit_type(parameter.type)
            self.variable_addresses[parameter.name] = self.builder.allocate(param_type)
            if isinstance(param_type, Float):
                reg = self.module.register_manager.allocate(f"float", Float())
                self.builder.add_instruction(f"mtc1 $a{i}, {reg}")
                self.builder.store_word(reg, self.variable_addresses[parameter.name])
                self.module.register_manager.free(reg)
            elif isinstance(param_type, Struct):
                # we get the pointer and fully allocate the struct on the stack
                for name, type in param_type.fields:
                    reg = self.module.register_manager.allocate(f"temp", type)
                    from_reg = Register(f"$a{i}", Any(), offset=param_type.get_member_offset(name))
                    self.builder.load_word(reg, from_reg)
                    to_addr = self.variable_addresses[parameter.name]
                    to_addr.offset = param_type.get_member_offset(name)
                    self.builder.store_word(reg, to_addr)
                    to_addr.offset = 0
                    self.module.register_manager.free(reg)
            else:
                self.builder.store_word(Register(f"$a{i}", param_type), self.variable_addresses[parameter.name])
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
                # leave the variable uninitialised, but if it is an array  you allocate space for it
                if isinstance(var_type, Array):
                    label = f"array_{uuid.uuid4().hex}"
                    array_block = self.module.data_block(label)
                    array_block.add_instruction(f".space {var_type.width}")
                    temp_reg = self.module.register_manager.allocate('temp', Pointer(Any()))
                    self.builder.load_address(temp_reg, label)
                    self.builder.store_word(temp_reg, allocation_address)
                    self.module.register_manager.free(temp_reg)
                elif isinstance(var_type, Struct):
                    # allocate space for all arrays in the struct and assign the address to the struct
                    for name, type in var_type.fields:
                        if isinstance(type, Array):
                            label = f"array_{uuid.uuid4().hex}"
                            array_block = self.module.data_block(label)
                            array_block.add_instruction(f".space {type.width}")
                            temp_reg = self.module.register_manager.allocate('temp', Pointer(Any()))
                            self.builder.load_address(temp_reg, label)
                            allocation_address.offset = var_type.get_member_offset(name)
                            self.builder.store_word(temp_reg, allocation_address)
                            allocation_address.offset = 0
                            self.module.register_manager.free(temp_reg)
                return

            # Check if it is a char* meaning it is a string_literal
            if isinstance(qualifier.initializer, ast.ArrayInitializer) and isinstance(var_type, Pointer) and isinstance(var_type.target, Char):
                string_literal_eval = self.visit_string_literal(qualifier.initializer)
                self.builder.store_word(string_literal_eval.r_value, allocation_address)
                return

            with self.eval(qualifier.initializer) as eval:
                # we only care about the r_value
                rval = eval.r_value
                initializer_type = rval.type

                # Check if the var_type is a poiter and the initializer is an array
                if isinstance(var_type, Pointer) and isinstance(rval.type, Array):
                    var_type.target = rval.type

                # Handle implicit conversion if necessary
                if isinstance(var_type, Float) and isinstance(initializer_type, Int):
                    float_reg = self.module.register_manager.allocate('float', Float())
                    self.builder.add_instruction(f"mtc1 {rval}, {float_reg}")
                    self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                    self.builder.store_word(float_reg, allocation_address)
                    self.module.register_manager.free(float_reg)
                elif isinstance(var_type, Int) and isinstance(initializer_type, Float):
                    float_reg = self.module.register_manager.allocate('float', Float())
                    self.builder.add_instruction(f"cvt.w.s {float_reg}, {rval}")
                    int_reg = self.module.register_manager.allocate('temp', Int())
                    self.builder.add_instruction(f"mfc1 {int_reg}, {float_reg}")
                    self.builder.store_word(int_reg, allocation_address)
                    self.module.register_manager.free(float_reg)
                    self.module.register_manager.free(int_reg)
                elif isinstance(var_type, Float):
                    self.builder.store_word(rval, allocation_address)
                else:
                    self.builder.store_word(rval, allocation_address)

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
        with self.eval(node.right) as right_eval, self.eval(node.left) as left_eval:
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
                    self.builder.load_address(left_eval.r_value, left_eval.r_value)
                elif isinstance(node.right, ast.INT) and node.right.value == 0:
                    # null pointer assignment
                    pass
                else:
                    raise TypeError(f"Cannot assign value of type {right_type} to pointer of type {left_type}")

            value = right_eval.r_value

            # Type conversion and assignment
            if isinstance(left_type, Int) and isinstance(right_type, Float):
                # Convert float to int
                float_reg = right_eval.r_value
                int_reg = self.module.register_manager.allocate('temp', Int())
                self.builder.add_instruction(f"cvt.w.s {float_reg}, {float_reg}")
                self.builder.add_instruction(f"mfc1 {int_reg}, {float_reg}")
                self.builder.add_instruction(f"move {left_eval.r_value}, {int_reg}")
                self.module.register_manager.free(int_reg)
            elif isinstance(left_type, Float) and isinstance(right_type, Int):
                # Convert int to float
                int_reg = right_eval.r_value
                float_reg = self.module.register_manager.allocate('float', Float())
                self.builder.add_instruction(f"mtc1 {int_reg}, {float_reg}")
                self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                self.builder.add_instruction(f"mov.s {left_eval.r_value}, {float_reg}")
                self.module.register_manager.free(float_reg)

            self.builder.store_word(value, left_eval.l_value)

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        with self.eval(node.expression) as eval:
            pass

    def visit_int(self, node: ast.INT):
        reg = self.module.register_manager.allocate('temp', Int())
        self.builder.add_instruction(f"li {reg}, {node.value}")
        return ExpressionEval(r_value=reg)

    def visit_float(self, node: ast.FLOAT):
        reg = self.module.register_manager.allocate('float', Float())
        label = f"float_{id(node)}"
        float_data_block = self.module.data_block(label)
        float_data_block.add_instruction(f".float {node.value}")
        self.builder.add_instruction(f"l.s {reg}, {label}")
        return ExpressionEval(r_value=reg)

    def visit_char(self, node: ast.CHAR):
        reg = self.module.register_manager.allocate('temp', Char())
        self.builder.add_instruction(f"li {reg}, {ord(node.value)}")
        return ExpressionEval(r_value=reg)

    def visit_identifier(self, node: ast.IDENTIFIER):
        addr = self.variable_addresses[node.name]
        if isinstance(addr.type, Float):
            reg = self.module.register_manager.allocate('float', Float())
        else:
            reg = self.module.register_manager.allocate('temp', addr.type)
        self.builder.load_word(reg, addr)
        addr_reg = self.module.register_manager.allocate('temp', addr.type)
        self.builder.load_address(addr_reg, addr)
        return ExpressionEval(l_value=addr_reg, r_value=reg)

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        with self.eval(node.expression) as eval:
            target_type = self.visit_type(node.cast_type)
            r_value = eval.r_value
            source_type = r_value.type

            if isinstance(target_type, Float) and isinstance(source_type, Int):
                float_reg = self.module.register_manager.allocate('float', Float())
                self.builder.add_instruction(f"mtc1 {r_value}, {float_reg}")
                self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                self.builder.add_instruction(f"mov.s {float_reg}, {float_reg}")
                res = ExpressionEval(r_value=float_reg)
            elif isinstance(target_type, Int) and isinstance(source_type, Float):
                float_reg = self.module.register_manager.allocate('float', Float())
                self.builder.add_instruction(f"mov.s {float_reg}, {r_value}")
                int_reg = self.module.register_manager.allocate('temp', Int())
                self.builder.add_instruction(f"cvt.w.s {float_reg}, {float_reg}")
                self.builder.add_instruction(f"mfc1 {int_reg}, {float_reg}")
                res = ExpressionEval(r_value=int_reg)
            else:
                if isinstance(target_type, Float):
                    result_reg = self.module.register_manager.allocate('float', Float())
                    self.builder.add_instruction(f"mov.s {result_reg}, {r_value}")
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
                dealloc_left = False
                # cast to float if necessary
                if not isinstance(left_type, Float):
                    float_reg = self.module.register_manager.allocate('float', Float())
                    self.builder.add_instruction(f"mtc1 {left}, {float_reg}")
                    self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                    left_float = float_reg
                    dealloc_left = True
                else:
                    left_float = left

                dealloc_right = False
                if not isinstance(right_type, Float):
                    float_reg = self.module.register_manager.allocate('float', Float())
                    self.builder.add_instruction(f"mtc1 {right}, {float_reg}")
                    self.builder.add_instruction(f"cvt.s.w {float_reg}, {float_reg}")
                    right_float = float_reg
                    dealloc_right = True
                else:
                    right_float = right

                result_reg = self.module.register_manager.allocate('float', Float())
                if node.operator == ast.BinaryArithmetic.Operator.PLUS:
                    self.builder.add_instruction(f"add.s {result_reg}, {left_float}, {right_float}")
                elif node.operator == ast.BinaryArithmetic.Operator.MINUS:
                    self.builder.add_instruction(f"sub.s {result_reg}, {left_float}, {right_float}")
                elif node.operator == ast.BinaryArithmetic.Operator.MUL:
                    self.builder.add_instruction(f"mul.s {result_reg}, {left_float}, {right_float}")
                elif node.operator == ast.BinaryArithmetic.Operator.DIV:
                    self.builder.add_instruction(f"div.s {result_reg}, {left_float}, {right_float}")

                if dealloc_left:
                    self.module.register_manager.free(left_float)
                if dealloc_right:
                    self.module.register_manager.free(right_float)

                ret = ExpressionEval(r_value=result_reg)
            else:
                # pointer arithmetic
                if isinstance(left_type, Pointer) and isinstance(right_type, Int):
                    # multiply right by the size of the target type
                    self.builder.add_instruction(f"mul {right}, {right}, {left_type.target.width}")
                    result_reg = self.module.register_manager.allocate('temp', left_type)
                else:
                    result_reg = self.module.register_manager.allocate('temp', Int())

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
            result_reg = self.module.register_manager.allocate('temp', Int())

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
            result_reg = self.module.register_manager.allocate('temp', Int())
            left_reg = left.r_value
            right_reg = right.r_value

            # Convert non-zero values to 1 (true) and zero to 0 (false)
            self.builder.add_instruction(
                f"sltu {left_reg}, $zero, {left_reg}")  # if left_reg != 0 -> left_reg = 1 else left_reg = 0
            self.builder.add_instruction(
                f"sltu {right_reg}, $zero, {right_reg}")  # if right_reg != 0 -> right_reg = 1 else right_reg = 0

            if node.operator == ast.BinaryLogicalOperation.Operator.AND:
                self.builder.add_instruction(f"and {result_reg}, {left_reg}, {right_reg}")
            elif node.operator == ast.BinaryLogicalOperation.Operator.OR:
                self.builder.add_instruction(f"or {result_reg}, {left_reg}, {right_reg}")

        return ExpressionEval(r_value=result_reg)

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        with self.eval(node.left) as left, self.eval(node.right) as right:

            result_reg = self.module.register_manager.allocate('temp', Int())
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
                if isinstance(value.r_value.type, Float):
                    result_reg = self.module.register_manager.allocate('float', Float())
                    self.builder.add_instruction(f"mov.s {result_reg}, {value.r_value}")
                else:
                    result_reg = self.module.register_manager.allocate('temp', value.r_value.type)
                    self.builder.add_instruction(f"move {result_reg}, {value.r_value}")
                ret = ExpressionEval(r_value=result_reg)
            elif node.operator == ast.UnaryExpression.Operator.NEGATIVE:
                if isinstance(value.r_value.type, Float):
                    result_reg = self.module.register_manager.allocate('float', Float())
                    self.builder.add_instruction(f"neg.s {result_reg}, {value.r_value}")
                else:
                    result_reg = self.module.register_manager.allocate('temp', value.r_value.type)
                    self.builder.add_instruction(f"neg {result_reg}, {value.r_value}")
                ret = ExpressionEval(r_value=result_reg)
            elif node.operator == ast.UnaryExpression.Operator.ONESCOMPLEMENT:
                result_reg = self.module.register_manager.allocate('temp', value.r_value.type)
                self.builder.add_instruction(f"not {result_reg}, {value.r_value}")
                ret = ExpressionEval(r_value=result_reg)
            elif node.operator == ast.UnaryExpression.Operator.LOGICALNEGATION:
                result_reg = self.module.register_manager.allocate('temp', Int())
                self.builder.add_instruction(f"seq {result_reg}, {value.r_value}, $zero")
                ret = ExpressionEval(r_value=result_reg)
            elif node.operator == ast.UnaryExpression.Operator.ADDRESSOF:
                r_reg = self.module.register_manager.allocate('temp', Pointer(value.l_value.type))
                self.builder.load_address(r_reg, value.l_value)
                ret = ExpressionEval(r_value=r_reg)
            elif node.operator == ast.UnaryExpression.Operator.DEREFERENCE:
                r_reg = self.module.register_manager.allocate('temp', value.r_value.type.target)
                self.builder.load_word(r_reg, value.r_value)
                l_reg = self.module.register_manager.allocate('temp', value.r_value.type.target)
                self.builder.add_instruction(f"move {l_reg}, {value.r_value}")
                ret = ExpressionEval(l_value=l_reg, r_value=r_reg)
            elif node.operator == ast.UnaryExpression.Operator.INCREMENT:
                reg = self.module.register_manager.allocate('temp', value.r_value.type)

                if not node.prefix:
                    # we need to return the value before the operation is done
                    self.builder.add_instruction(f"move {reg}, {value.r_value}")

                # pointer arithmetic
                if isinstance(value.r_value.type, Pointer):
                    immediate_value = value.r_value.type.target.width
                else:
                    immediate_value = 1

                self.builder.add_instruction(f"addi {value.r_value}, {value.r_value}, {immediate_value}")

                if node.prefix:
                    # we need the value after the opration is done
                    self.builder.add_instruction(f"move {reg}, {value.r_value}")

                self.builder.store_word(value.r_value, value.l_value)
                ret = ExpressionEval(r_value=reg)

            elif node.operator == ast.UnaryExpression.Operator.DECREMENT:
                reg = self.module.register_manager.allocate('temp', value.r_value.type)

                if not node.prefix:
                    # we need to return the value before the operation is done
                    self.builder.add_instruction(f"move {reg}, {value.r_value}")

                # pointer arithmetic
                if isinstance(value.r_value.type, Pointer):
                    immediate_value = value.r_value.type.target.width
                else:
                    immediate_value = 1

                self.builder.add_instruction(f"addi {value.r_value}, {value.r_value}, -{immediate_value}")

                if node.prefix:
                    # we need the value after the opration is done
                    self.builder.add_instruction(f"move {reg}, {value.r_value}")

                self.builder.store_word(value.r_value, value.l_value)
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
                if isinstance(arg_eval.r_value.type, Float):
                    self.builder.add_instruction(f"mfc1 {arg_reg}, {arg_eval.r_value}")
                elif isinstance(arg_eval.r_value.type, Struct):
                    # move the address of the struct to the argument register
                    self.builder.add_instruction(f"move {arg_reg}, {arg_eval.l_value}")
                else:
                    self.builder.add_instruction(f"move {arg_reg}, {arg_eval.r_value}")

        self.builder.jal(node.name, self.module.register_manager)

        for reg in reversed(arg_regs):
            self.module.register_manager.free(reg)

        return_type = self.functions[node.name].return_type
        if isinstance(return_type, Float):
            result_reg = self.module.register_manager.allocate('float', Float())
            self.builder.add_instruction(f"mov.s {result_reg}, $f0")
        else:
            result_reg = self.module.register_manager.allocate('temp', return_type)
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
        self.builder.load_address(reg, label)
        return ExpressionEval(r_value=reg)

    def visit_printf_call(self, node: ast.PrintFCall):
        # Link the printf block
        label = f"printf_{uuid.uuid4().hex}"

        # Call the printf function to handle data and instruction generation
        args_eval = []
        for arg in node.args:
            if isinstance(arg, ast.ArrayInitializer):
                arg_eval = self.visit_string_literal(arg)
            else:
                arg_eval = self.visit_expression(arg)
            args_eval.append(arg_eval)
        #args_eval = [self.visit_expression(arg) for arg in node.args] # This is a list of registers
        self.module.printf(label, node.format, args_eval)

        # Free the registers
        for reg in reversed(args_eval):
            if reg.l_value:
                self.module.register_manager.free(reg.l_value)
            if reg.r_value:
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

    def get_array_dimensions(self, node: ast.ArrayInitializer):
        if isinstance(node, ast.ArrayInitializer):
            return self.get_array_dimensions(node.elements[0])
        else:
            return 1


    def get_array_element_type(self, node: ast.ArrayInitializer):
        node = node.elements[0]
        if isinstance(node, ast.ArrayInitializer):
            return self.get_array_element_type(node)
        else:
            if isinstance(node, ast.INT):
                return Int()
            elif isinstance(node, ast.FLOAT):
                return Float()
            elif isinstance(node, ast.CHAR):
                return Char()
            else:
                raise NotImplementedError("Only int, float and char are supported for array elements")


    def visit_array_initializer(self, node: ast.ArrayInitializer):
        if node.struct_type:
            return self.visit_struct_initializer(node)
        label = f"array_{uuid.uuid4().hex}"
        array_block = self.module.data_block(label)
        elements = []
        self.array_elements(node.elements, elements)
        self.module.array(array_block, elements)
        # Now you should first store the address of the array in a register
        #array_type = Array(target=self.get_array_element_type(node), length=len(node.elements), dimensions=self.get_array_dimensions(node))
        reg = self.module.register_manager.allocate('temp', Pointer(Any()))
        self.builder.load_address(reg, label)
        return ExpressionEval(r_value=reg)

    def get_array_indices(self, node: ast.ArrayAccess):
        indices = []
        while isinstance(node, ast.ArrayAccess):
            index_eval = self.visit_expression(node.index)
            indices.append(index_eval.r_value)
            if index_eval.l_value:
                self.module.register_manager.free(index_eval.l_value)
            node = node.target
        indices.reverse()
        return indices

    def get_array_dimensions(self, node: ast.ArraySpecifier):
        dimensions = []
        if isinstance(node, ast.ArraySpecifier):
            for size in node.sizes:
                if isinstance(size, ast.INT):
                    dimensions.append(size.value)
                else:
                    raise NotImplementedError("Only int is supported for array sizes")
        return dimensions

    def visit_array_access(self, node: ast.ArrayAccess):
        indices = self.get_array_indices(node)
        array_eval = node.target
        while isinstance(array_eval, ast.ArrayAccess):
            array_eval = array_eval.target


        with self.eval(array_eval) as array_identifier_eval:
            array_type = array_identifier_eval.l_value.type

            temp_array_type = array_type
            while isinstance(temp_array_type, Pointer):
                temp_array_type = temp_array_type.target
            dimensions = self.get_array_dimensions(temp_array_type.dimensions)

            # Calculate the offset for multidimensional arrays
            offset_reg = self.module.register_manager.allocate('temp', Int())
            self.builder.add_instruction(f"li {offset_reg}, 0 # Initialize the offset to 0")
            stride_reg = self.module.register_manager.allocate('temp', Int())
            self.builder.add_instruction(f"li {stride_reg}, {temp_array_type.target.width} # The size of the array element")
            self.builder.add_instruction(f"# Calculating the offset for the array access")
            for index_reg, dim in zip(reversed(indices), reversed(dimensions)):
                temp_reg = self.module.register_manager.allocate('temp', Int())
                # Multiply index by current stride and add to offset
                self.builder.add_instruction(f"mul {temp_reg}, {index_reg}, {stride_reg} # temp = index * stride")
                self.builder.add_instruction(f"add {offset_reg}, {offset_reg}, {temp_reg} # offset += temp")
                # Update stride for the next dimension
                self.builder.add_instruction(f"li {temp_reg}, {dim} # Load dimension size into temp")
                self.builder.add_instruction(f"mul {stride_reg}, {stride_reg}, {temp_reg} # stride *= dimension size")
                self.module.register_manager.free(temp_reg)
                self.module.register_manager.free(index_reg)
            self.module.register_manager.free(stride_reg)

            l_val = self.module.register_manager.allocate('temp', array_type.target)
            self.builder.add_instruction(f"add {l_val}, {array_identifier_eval.r_value}, {offset_reg} # The address of the array word at the index just calculated")
            self.module.register_manager.free(offset_reg)
            r_val = self.module.register_manager.allocate('temp', array_type.target)
            self.builder.load_word(r_val, l_val)

        return ExpressionEval(l_value=l_val, r_value=r_val)


    def visit_struct_definition(self, node: ast.StructDefinition):
        new_type = Struct(name=node.name, fields=[])
        self.structs[node.name] = new_type
        new_type.fields = [(member.name, self.visit_type(member.type)) for member in node.members]
        new_type.set_width()

    def visit_struct_initializer(self, node: ast.ArrayInitializer):
        raise NotImplementedError("Struct initializer not implemented")

    def visit_struct_access(self, node: ast.StructAccess):
        with self.eval(node.target) as target_eval:
            struct_type = target_eval.l_value.type
            if not isinstance(struct_type, Struct):
                raise TypeError(f"Cannot access member of non-struct type {struct_type}")

            offset = struct_type.get_member_offset(node.member_name)

            member_type = struct_type.get_member_type(node.member_name)
            lval = self.module.register_manager.allocate('temp', member_type)
            self.builder.add_instruction(f"addi {lval}, {target_eval.l_value}, {offset}")
            rval = self.module.register_manager.allocate('temp', member_type)
            self.builder.load_word(rval, lval)
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
        if node.expression is None:
            self.builder.ret()
        else:
            with self.eval(node.expression) as result_eval:
                self.builder.ret(result_eval.r_value)

    def visit_forward_declaration(self, node: ast.ForwardDeclaration):
        # create an empty block for the function if it does not exist yet
        if node.name not in self.functions:
            self.functions[node.name] = self.module.function(node.name, self.visit_type(node.return_type))

    def visit_comment_statement(self, node: ast.CommentStatement):
        if self.builder is None or (isinstance(self.builder, Function) and self.builder.current_block is None):
            return
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
            elif node.type == ast.BaseType.void:
                mips_type = Void()
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
