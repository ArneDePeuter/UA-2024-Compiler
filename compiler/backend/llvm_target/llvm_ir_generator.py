import copy

from llvmlite import ir
from compiler.core.ast_visitor import AstVisitor
from compiler.core import ast
from dataclasses import dataclass
from typing import Optional

from .type_translator import TypeTranslator
from .ir_types import IrIntType, IrFloatType, IrCharType


@dataclass
class ExpressionEval:
    l_value: Optional[ir.AllocaInstr] = None
    r_value: Optional[ir.Constant] = None


class LLVMIRGenerator(AstVisitor):
    def __init__(self):
        self.module = ir.Module()
        self.builder = None
        self.var_addresses: dict[str, ir.AllocaInstr] = {}
        self.while_fd = {}
        self.functions = {}

        printf_type = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
        self.printf_func = ir.Function(self.module, printf_type, name="printf")

        super().__init__()

    def generate_llvm_ir(self, node):
        self.visit(node)
        result = str(self.module)
        lines = result.split("\n")
        lines.remove(lines[1])
        lines.remove(lines[1])
        return "\n".join(lines)

    def visit_expression(self, node: ast.Expression):
        if node.c_syntax and self.builder:
            comment = node.c_syntax.split("\n")
            self.builder.comment(f"C Syntax: {comment[0]}")
        return super().visit_expression(node)

    def visit_statement(self, node: ast.Statement):
        if self.builder is None and (isinstance(node, ast.FunctionDeclaration) or isinstance(node, ast.Program) or isinstance(node, ast.ForwardDeclaration)):
            super().visit_statement(node)
            return

        if self.builder is None and isinstance(node, ast.CommentStatement):
            return

        if self.builder.block is not None and self.builder.block.is_terminated:
            return

        if node.c_syntax:
            comment = node.c_syntax.split("\n")
            try:
                self.builder.comment(f"C Syntax: {'-'.join(comment)}")
            except:
                pass
        super().visit_statement(node)

    def visit_type(self, node: ast.Type) -> ir.types.Type:
        return TypeTranslator.translate_ast_type(node)

    def visit_int(self, node: ast.INT) -> ExpressionEval:
        return ExpressionEval(
            r_value=ir.Constant(IrIntType, node.value)
        )

    def visit_float(self, node: ast.FLOAT) -> ExpressionEval:
        return ExpressionEval(
            r_value=ir.Constant(IrFloatType, node.value)
        )

    def visit_char(self, node: ast.CHAR) -> ExpressionEval:
        return ExpressionEval(
            r_value=ir.Constant(IrCharType, ord(node.value))
        )

    def visit_identifier(self, node: ast.IDENTIFIER) -> ExpressionEval:
        return ExpressionEval(
            l_value=self.var_addresses[node.name],
            r_value=self.builder.load(self.var_addresses[node.name])
        )

    def visit_type_cast_expression(self, node: ast.TypeCastExpression) -> ExpressionEval:
        expr_eval: ExpressionEval = self.visit_expression(node.expression)

        if not expr_eval.r_value:
            raise NotImplementedError("Cannot type cast, r_value is None")

        value = expr_eval.r_value
        target_type = self.visit_type(node.cast_type)
        return ExpressionEval(r_value=TypeTranslator.match_llvm_type(self.builder, target_type, value))

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic) -> ExpressionEval:
        left: ExpressionEval = self.visit_expression(node.left)
        right: ExpressionEval = self.visit_expression(node.right)

        left_value = left.r_value
        right_value = right.r_value

        if not left_value or not right_value:
            raise NotImplementedError("Cannot perform binary arithmetic operation, r_value is None")

        if node.operator == ast.BinaryArithmetic.Operator.PLUS:
            if isinstance(left_value.type, ir.PointerType):
                element_size = left_value.type.pointee.width
                right_value = TypeTranslator.match_llvm_type(self.builder, IrIntType, right_value)
                offset = self.builder.mul(right_value, ir.Constant(IrIntType, element_size))
                result = self.builder.gep(left_value, [offset])
            else:
                left_value, right_value = TypeTranslator.cast_to_common_type(self.builder, left_value, right_value)
                if isinstance(left_value.type, ir.FloatType):
                    result = self.builder.fadd(left_value, right_value)
                else:
                    result = self.builder.add(left_value, right_value)
        elif node.operator == ast.BinaryArithmetic.Operator.MINUS:
            if isinstance(left_value.type, ir.PointerType):
                element_size = left_value.type.pointee.width
                right_value = TypeTranslator.match_llvm_type(self.builder, IrIntType, right_value)
                offset = self.builder.mul(right_value, ir.Constant(IrIntType, element_size))
                result = self.builder.gep(left_value, [self.builder.neg(offset)])
            else:
                left_value, right_value = TypeTranslator.cast_to_common_type(self.builder, left_value, right_value)
                if isinstance(left_value.type, ir.FloatType):
                    result = self.builder.fsub(left_value, right_value)
                else:
                    result = self.builder.sub(left_value, right_value)
        else:
            left_value, right_value = TypeTranslator.cast_to_common_type(self.builder, left_value, right_value)
            if node.operator == ast.BinaryArithmetic.Operator.MUL:
                if isinstance(left_value.type, ir.FloatType):
                    result = self.builder.fmul(left_value, right_value)
                else:
                    result = self.builder.mul(left_value, right_value)
            elif node.operator == ast.BinaryArithmetic.Operator.DIV:
                if isinstance(left_value.type, ir.FloatType):
                    result = self.builder.fdiv(left_value, right_value)
                else:
                    result = self.builder.sdiv(left_value, right_value)
            elif node.operator == ast.BinaryArithmetic.Operator.MOD:
                if isinstance(left_value.type, ir.FloatType):
                    result = self.builder.frem(left_value, right_value)
                else:
                    result = self.builder.srem(left_value, right_value)
            else:
                raise NotImplementedError(f"Binary arithmetic operator {node.operator} is not supported")

        return ExpressionEval(r_value=result)

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic) -> ExpressionEval:
        left: ExpressionEval = self.visit_expression(node.left)
        right: ExpressionEval = self.visit_expression(node.right)

        left_value = left.r_value
        right_value = right.r_value

        if not left_value or not right_value:
            raise NotImplementedError("Cannot perform binary bitwise operation, r_value is None")

        if node.operator == ast.BinaryBitwiseArithmetic.Operator.AND:
            result = self.builder.and_(left_value, right_value)
        elif node.operator == ast.BinaryBitwiseArithmetic.Operator.OR:
            result = self.builder.or_(left_value, right_value)
        elif node.operator == ast.BinaryBitwiseArithmetic.Operator.XOR:
            result = self.builder.xor(left_value, right_value)
        else:
            raise NotImplementedError(f"Binary bitwise arithmetic operator {node.operator} is not supported")

        return ExpressionEval(r_value=result)

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation) -> ExpressionEval:
        left: ExpressionEval = self.visit_expression(node.left)
        right: ExpressionEval = self.visit_expression(node.right)

        left_value = left.r_value
        right_value = right.r_value

        if not left_value or not right_value:
            raise NotImplementedError("Cannot perform binary logical operation, r_value is None")

        if node.operator == ast.BinaryLogicalOperation.Operator.AND:
            result = self.builder.and_(left_value, right_value)
        elif node.operator == ast.BinaryLogicalOperation.Operator.OR:
            result = self.builder.or_(left_value, right_value)
        else:
            raise NotImplementedError(f"Binary logical operator {node.operator} is not supported")

        return ExpressionEval(r_value=result)

    def visit_comparison_operation(self, node: ast.ComparisonOperation) -> ExpressionEval:
        left: ExpressionEval = self.visit_expression(node.left)
        right: ExpressionEval = self.visit_expression(node.right)

        left_value = left.r_value
        right_value = right.r_value

        if not left_value or not right_value:
            raise NotImplementedError("Cannot perform comparison operation, r_value is None")
        if isinstance(left_value.type, ir.PointerType):
            left_value = self.builder.ptrtoint(left_value, IrIntType)
        if isinstance(right_value.type, ir.PointerType):
            right_value = self.builder.ptrtoint(right_value, IrIntType)
        left_value, right_value = TypeTranslator.cast_to_common_type(self.builder, left_value, right_value)
        if isinstance(left_value.type, ir.FloatType):
            result = self.builder.fcmp_ordered(node.operator.value, left_value, right_value)
        else:
            result = self.builder.icmp_signed(node.operator.value, left_value, right_value)
        return ExpressionEval(r_value=result)

    def visit_unary_expression(self, node: ast.UnaryExpression) -> ExpressionEval:
        value: ExpressionEval = self.visit_expression(node.value)

        if not value.r_value:
            raise NotImplementedError("Cannot perform unary operation, r_value is None")

        if node.operator == ast.UnaryExpression.Operator.POSITIVE:
            result = value.r_value
        elif node.operator == ast.UnaryExpression.Operator.NEGATIVE:
            result = self.builder.neg(value.r_value)
        elif node.operator == ast.UnaryExpression.Operator.ONESCOMPLEMENT:
            result = self.builder.not_(value.r_value)
        elif node.operator == ast.UnaryExpression.Operator.LOGICALNEGATION:
            result = self.builder.icmp_signed("==", value.r_value, ir.Constant(value.r_value.type, 0))
        elif node.operator == ast.UnaryExpression.Operator.DEREFERENCE:
            return ExpressionEval(r_value=self.builder.load(value.r_value), l_value=value.r_value)
        elif value.l_value:
            if node.operator == ast.UnaryExpression.Operator.ADDRESSOF:
                result = value.l_value
            elif node.operator == ast.UnaryExpression.Operator.INCREMENT:
                if isinstance(value.r_value.type, ir.PointerType):
                    element_size = value.r_value.type.pointee.width
                    offset = self.builder.mul(ir.Constant(IrIntType, 1), ir.Constant(IrIntType, element_size))
                    result = self.builder.gep(value.r_value, [offset])
                else:
                    left_value, right_value = TypeTranslator.cast_to_common_type(self.builder, value.r_value, ir.Constant(value.r_value.type, 1))
                    if isinstance(value.r_value.type, ir.FloatType):
                        result = self.builder.fadd(left_value, right_value)
                    else:
                        result = self.builder.add(left_value, right_value)

                self.builder.store(result, value.l_value)

                if node.prefix:
                    result = result
                else:
                    result = value.r_value

            elif node.operator == ast.UnaryExpression.Operator.DECREMENT:
                if isinstance(value.r_value.type, ir.PointerType):
                    element_size = value.r_value.type.pointee.width
                    offset = self.builder.mul(ir.Constant(IrIntType, 1), ir.Constant(IrIntType, element_size))
                    result = self.builder.gep(value.r_value, [self.builder.neg(offset)])
                else:
                    left_value, right_value = TypeTranslator.cast_to_common_type(self.builder, value.r_value, ir.Constant(value.r_value.type, 1))
                    if isinstance(value.r_value.type, ir.FloatType):
                        result = self.builder.fsub(left_value, right_value)
                    else:
                        result = self.builder.sub(left_value, right_value)

                self.builder.store(result, value.l_value)

                if node.prefix:
                    result = result
                else:
                    result = value.r_value
        else:
            raise NotImplementedError(f"Unary operator {node.operator} is not supported")

        return ExpressionEval(r_value=result)

    def visit_shift_expression(self, node: ast.ShiftExpression) -> ExpressionEval:
        expression_eval_value: ExpressionEval = self.visit_expression(node.value)
        expression_eval_amount: ExpressionEval = self.visit_expression(node.amount)

        value = expression_eval_value.r_value
        amount = expression_eval_amount.r_value

        if not value or not amount:
            raise NotImplementedError("Cannot perform shift expression, r_value is None")

        if node.operator == ast.ShiftExpression.Operator.LEFT:
            result = self.builder.shl(value, amount)
        elif node.operator == ast.ShiftExpression.Operator.RIGHT:
            result = self.builder.lshr(value, amount)
        else:
            raise NotImplementedError(f"Shift operator {node.operator} is not supported")

        return ExpressionEval(r_value=result)

    def visit_program(self, node: ast.Program) -> None:
        for statement in node.statements:
            if isinstance(statement, ast.VariableDeclaration):
                self.visit_variable_declaration_global(statement)
                continue
            self.visit_statement(statement)

    def visit_body(self, node: ast.Body) -> None:
        for statement in node.statements:
            self.visit_statement(statement)

    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier) -> ir.Constant:
        ...

    def visit_variable_declaration(self, node: ast.VariableDeclaration) -> None:
        decl_type = self.visit_type(node.var_type)
        for qualifier in node.qualifiers:
            alloc = self.builder.alloca(decl_type, name=qualifier.identifier) # Create an allocation for the variable
            self.var_addresses[qualifier.identifier] = alloc
            # Handle default initialization
            if qualifier.initializer is None:
                default = ir.Constant(decl_type, None)
                self.builder.store(default, alloc)
                continue

            # Evaluate the expression for initializer
            expr_eval: ExpressionEval = self.visit_expression(qualifier.initializer)
            if not expr_eval.r_value:
                raise NotImplementedError("Cannot assign value to variable, r_value is None")

            # Store the value to the allocated variable
            if isinstance(decl_type, ir.PointerType) and not isinstance(expr_eval.r_value.type, ir.PointerType):
                null_ptr = ir.Constant(decl_type, None)
                self.builder.store(null_ptr, alloc)
            else:
                value = TypeTranslator.match_llvm_type(self.builder, decl_type, expr_eval.r_value)
                self.builder.store(value, alloc)

    def visit_assignment_statement(self, node: ast.AssignmentStatement) -> None:
        left_eval = self.visit_expression(node.left)
        right_eval = self.visit_expression(node.right)
        if not left_eval.l_value:
            raise NotImplementedError("Cannot assign value to variable, l_value is None")
        if not right_eval.r_value:
            raise NotImplementedError("Cannot assign value to variable, r_value is None")
        left_type = left_eval.l_value.type.pointee
        if isinstance(left_type, ir.PointerType) and not isinstance(right_eval.r_value.type, ir.PointerType):
            null_ptr = ir.Constant(left_type, None)
            self.builder.store(null_ptr, left_eval.l_value)
            return
        value = TypeTranslator.match_llvm_type(self.builder, left_type, right_eval.r_value)
        self.builder.store(value, left_eval.l_value)

    def visit_expression_statement(self, node: ast.ExpressionStatement) -> None:
        self.visit_expression(node.expression)

    def visit_comment_statement(self, node: ast.CommentStatement) -> None:
        for line in node.content.split("\n"):
            self.builder.comment(line)

    def visit_while_statement(self, node: ast.WhileStatement):
        w_condition_block = self.builder.append_basic_block("w_condition")
        w_body_block = self.builder.append_basic_block("w_body")
        w_after_block = self.builder.append_basic_block("w_after")

        # Store the blocks for break and continue
        self.while_fd[(node.line, node.position)] = (w_condition_block, w_after_block)

        self.builder.branch(w_condition_block)

        # Condition block
        self.builder.position_at_start(w_condition_block)
        cond_head = self.to_bool_expr(node.expression)
        self.builder.cbranch(cond_head, w_body_block, w_after_block)

        # Body block
        self.builder.position_at_start(w_body_block)
        self.visit_statement(node.to_execute)
        if not w_body_block.is_terminated:
            self.builder.branch(w_condition_block)

        # After block
        self.builder.position_at_start(w_after_block)

    def to_bool_expr(self, node: ast.Expression):
        ir_node_eval: ExpressionEval = self.visit_expression(node)

        ir_node = ir_node_eval.r_value
        if not ir_node:
            raise NotImplementedError("Cannot convert to bool, r_value is None")

        if isinstance(ir_node, ir.CompareInstr):
            return ir_node
        ir_node: ir.Constant
        if isinstance(ir_node.type, ir.IntType):
            return self.builder.icmp_signed("!=", ir_node, ir.Constant(ir.IntType(32), 0))
        elif isinstance(ir_node.type, ir.DoubleType):
            return self.builder.fcmp_ordered("!=", ir_node, ir.Constant(ir.DoubleType(), 0.0))
        elif isinstance(ir_node.type, ir.PointerType):
            return self.builder.icmp_unsigned("!=", ir_node, ir.Constant(ir.PointerType(ir.IntType(8)), 0))
        else:
            raise NotImplementedError(f"Conversion to bool for {node} is not implemented")

    def visit_break_statement(self, node: ast.BreakStatement):
        _, w_after_block = self.while_fd[(node.while_statement.line, node.while_statement.position)]
        self.builder.branch(w_after_block)

    def visit_continue_statement(self, node: ast.ContinueStatement):
        w_condition_block, _ = self.while_fd[(node.while_statement.line, node.while_statement.position)]
        self.builder.branch(w_condition_block)

    def visit_if_statement(self, node: ast.IfStatement):
        conditional = self.to_bool_expr(node.condition)
        if node.else_statement:
            with self.builder.if_else(conditional) as (then, otherwise):
                with then:
                    self.visit_body(node.body)
                with otherwise:
                    self.visit_else_statement(node.else_statement)
        else:
            with self.builder.if_then(conditional):
                self.visit_body(node.body)

    def visit_else_statement(self, node: ast.ElseStatement):
        self.visit_statement(node.body)

    def visit_printf_call(self, node: ast.PrintFCall) -> None:
        format_string = node.replacer.value

        # Create the format string constant
        format_string_constant = ir.Constant(ir.ArrayType(ir.IntType(8), len(format_string) + 1),
                                             bytearray(format_string.encode('utf-8') + b'\00'))

        # Create the format string global variable
        format_string_global = ir.GlobalVariable(
            self.module, format_string_constant.type, name=f"printf_format_{node.line}_{node.position}"
        )
        format_string_global.linkage = "internal"
        format_string_global.global_constant = True
        format_string_global.initializer = format_string_constant

        expression_value = self.visit_expression(node.expression).r_value
        if isinstance(expression_value.type, ir.FloatType):
            expression_value = self.builder.fpext(expression_value, ir.DoubleType())

        self.builder.call(self.printf_func, [
            format_string_global.bitcast(ir.PointerType(ir.IntType(8))),
            expression_value
        ])

    def visit_function_declaration(self, node: ast.FunctionDeclaration) -> None:
        func = self.functions.get(node.name) # Check if the function is already declared
        return_type = self.visit_type(node.return_type)
        if not func:
            args = [self.visit_type(param.type) for param in node.parameters]
            func_type = ir.FunctionType(return_type, args)
            func = ir.Function(self.module, func_type, name=node.name)
            self.functions[node.name] = func

        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        for param, arg in zip(node.parameters, func.args):
            # Allocate memory for the argument
            alloc = self.builder.alloca(arg.type, name=param.name)
            # Store the argument in the allocated memory
            self.builder.store(arg, alloc)
            # Store the pointer to the allocated memory in the dictionary
            self.var_addresses[param.name] = alloc

        self.visit_body(node.body)

        if not self.builder.block.is_terminated:
            if isinstance(return_type, ir.VoidType):
                self.builder.ret_void()
            else:
                default_value = ir.Constant(return_type, None)
                self.builder.ret(default_value)

        self.builder = None

    def visit_forward_declaration(self, node: ast.ForwardDeclaration):
        if self.functions.get(node.name):
            return
        return_type = self.visit_type(node.return_type)
        args = [self.visit_type(param) for param in node.parameters]
        func_type = ir.FunctionType(return_type, args)
        func = ir.Function(self.module, func_type, name=node.name)
        self.functions[node.name] = func

    def visit_return_statement(self, node: ast.ReturnStatement):
        if node.expression is not None:
            expr_eval = self.visit_expression(node.expression)
            if not expr_eval.r_value:
                raise NotImplementedError("Cannot return value, r_value is None")
            self.builder.ret(expr_eval.r_value)
        else:
            self.builder.ret_void()

    def visit_function_call(self, node: ast.FunctionCall):
        func = self.functions.get(node.name)
        if not func:
            raise NotImplementedError(f"Function {node.name} not found")

        args = [self.visit_expression(arg).r_value for arg in node.arguments]
        return ExpressionEval(r_value=self.builder.call(func, args))

    def visit_variable_declaration_global(self, node: ast.VariableDeclaration):
        decl_type = self.visit_type(node.var_type)
        for qualifier in node.qualifiers:
            ir_global = ir.GlobalVariable(self.module, decl_type, name=qualifier.identifier)
            self.var_addresses[qualifier.identifier] = ir_global
            if qualifier.initializer is None:
                continue
            expr_eval: ExpressionEval = self.visit_expression(qualifier.initializer)
            if not expr_eval.r_value:
                raise NotImplementedError("Cannot assign value to variable, r_value is None")
            if isinstance(decl_type, ir.PointerType) and not isinstance(expr_eval.r_value.type, ir.PointerType):
                null_ptr = ir.Constant(decl_type, None)
                ir_global.initializer = null_ptr
                continue
            value = TypeTranslator.match_llvm_type(self.builder, decl_type, expr_eval.r_value)
            ir_global.initializer = value
