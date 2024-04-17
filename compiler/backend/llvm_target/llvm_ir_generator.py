from llvmlite import ir
from compiler.core.ast_visitor import AstVisitor
from compiler.core import ast


class LLVMIRGenerator(AstVisitor):
    def __init__(self):
        super().__init__()
        self.module = ir.Module()
        self.builder = None
        self.variables = {}

    def generate_llvm_ir(self, node):
        """Generate LLVM IR code for the given AST node."""
        self.visit(node)
        return str(self.module)

    def visit_program(self, program_node: ast.Program):
        """Visit a program node and generate LLVM IR code for its statements."""
        for statement in program_node.statements:
            self.visit(statement)

    def visit_function_declaration(self, func_node: ast.FunctionDeclaration):
        """Visit a function declaration node and generate LLVM IR code for the function."""
        return_type = self._get_llvm_type(func_node.return_type)
        func_type = ir.FunctionType(return_type, [])
        func = ir.Function(self.module, func_type, name=func_node.name)

        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        self.visit(func_node.body)

        if not block.is_terminated:
            if return_type == ir.VoidType():
                self.builder.ret_void()
            else:
                default_value = ir.Constant(return_type, None)
                self.builder.ret(default_value)

        self.builder = None

    def visit_variable_declaration(self, var_node: ast.VariableDeclaration):
        """Visit a variable declaration node and generate LLVM IR code for variable allocation and initialization."""
        self.builder.comment(var_node.c_syntax)
        for qualifier in var_node.qualifiers:
            var_name = qualifier.identifier
            var_type = self._get_llvm_type(var_node.var_type)

            if var_node.var_type.address_qualifiers:
                for _ in range(len(var_node.var_type.address_qualifiers)):
                    var_type = ir.PointerType(var_type)

            var_addr = self.builder.alloca(var_type, name=var_name)
            self.variables[var_name] = var_addr

            if qualifier.initializer is not None:
                init_value = self.visit(qualifier.initializer)
                casted_init_value = self._cast_value(init_value, var_type)
                self.builder.store(casted_init_value, var_addr)

    def visit_assignment_statement(self, assign_node: ast.AssignmentStatement):
        """Visit an assignment statement node and generate LLVM IR code for the assignment."""
        target = self.visit(assign_node.left)
        value = self.visit(assign_node.right)

        target_type = target.type

        if isinstance(target_type, ir.PointerType):
            casted_value = self._cast_value(value, target_type.pointee)
            self.builder.store(casted_value, target)
        else:
            alloca = self.builder.alloca(target_type)
            casted_value = self._implicit_cast(value, target_type)
            self.builder.store(casted_value, alloca)

            if isinstance(assign_node.left, ast.IDENTIFIER):
                self.variables[assign_node.left.name] = alloca

    def visit_binary_arithmetic(self, binary_node: ast.BinaryArithmetic):
        """Visit a binary arithmetic node and generate LLVM IR code for the arithmetic operation."""
        left = self.visit(binary_node.left)
        right = self.visit(binary_node.right)

        if isinstance(left.type, ir.PointerType) and isinstance(right.type, ir.IntType):
            return self._handle_pointer_arithmetic(left, right, binary_node.operator)
        elif isinstance(left.type, ir.IntType) and isinstance(right.type, ir.PointerType):
            return self._handle_pointer_arithmetic(right, left, binary_node.operator)
        else:
            return self._handle_binary_arithmetic(binary_node.operator, left, right)

    def visit_binary_bitwise_arithmetic(self, binary_node: ast.BinaryBitwiseArithmetic):
        """Visit a binary bitwise arithmetic node and generate LLVM IR code for the bitwise operation."""
        left = self.visit(binary_node.left)
        right = self.visit(binary_node.right)
        return self._handle_binary_bitwise_arithmetic(binary_node.operator, left, right)

    def visit_binary_logical_operation(self, binary_node: ast.BinaryLogicalOperation):
        """Visit a binary logical operation node and generate LLVM IR code for the logical operation."""
        left = self.visit(binary_node.left)
        right = self.visit(binary_node.right)
        return self._handle_binary_logical_operation(binary_node.operator, left, right)

    def visit_comparison_operation(self, comparison_node: ast.ComparisonOperation):
        """Visit a comparison operation node and generate LLVM IR code for the comparison."""
        left = self.visit(comparison_node.left)
        right = self.visit(comparison_node.right)

        if isinstance(left.type, ir.PointerType) and isinstance(right.type, ir.IntType):
            right = self.builder.zext(right, ir.IntType(64))
            left = self.builder.ptrtoint(left, ir.IntType(64))
            return self.builder.icmp_unsigned(comparison_node.operator.value, left, right)
        elif isinstance(left.type, ir.IntType) and isinstance(right.type, ir.PointerType):
            left = self.builder.zext(left, ir.IntType(64))
            right = self.builder.ptrtoint(right, ir.IntType(64))
            return self.builder.icmp_unsigned(comparison_node.operator.value, left, right)
        else:
            return self._handle_comparison_operation(comparison_node.operator, left, right)

    def visit_unary_expression(self, unary_node: ast.UnaryExpression):
        """Visit a unary expression node and generate LLVM IR code for the unary operation."""
        operand = self.visit(unary_node.value)

        if unary_node.operator == ast.UnaryExpression.Operator.INCREMENT:
            return self._handle_increment(operand, unary_node.prefix)
        elif unary_node.operator == ast.UnaryExpression.Operator.DECREMENT:
            return self._handle_decrement(operand, unary_node.prefix)
        elif unary_node.operator == ast.UnaryExpression.Operator.POSITIVE:
            return operand
        elif unary_node.operator == ast.UnaryExpression.Operator.NEGATIVE:
            return self.builder.neg(operand)
        elif unary_node.operator == ast.UnaryExpression.Operator.LOGICALNEGATION:
            return self.builder.not_(operand)
        elif unary_node.operator == ast.UnaryExpression.Operator.ADDRESSOF:
            return self._handle_address_of(operand)
        elif unary_node.operator == ast.UnaryExpression.Operator.DEREFERENCE:
            return self._handle_dereference(operand)

    def visit_int(self, int_node: ast.INT):
        """Visit an integer node and generate LLVM IR code for the constant integer."""
        return ir.Constant(ir.IntType(32), int_node.value)

    def visit_float(self, float_node: ast.FLOAT):
        """Visit a float node and generate LLVM IR code for the constant float."""
        return ir.Constant(ir.DoubleType(), float_node.value)

    def visit_char(self, char_node: ast.CHAR):
        """Visit a char node and generate LLVM IR code for the constant character."""
        return ir.Constant(ir.IntType(8), ord(char_node.value))

    def visit_identifier(self, identifier_node: ast.IDENTIFIER):
        """Visit an identifier node and generate LLVM IR code for loading the variable value."""
        var_addr = self.variables[identifier_node.name]
        return self.builder.load(var_addr)

    def visit_printf_call(self, printf_node: ast.PrintFCall):
        """Visit a printf call node and generate LLVM IR code for the printf function call."""
        self.builder.comment(printf_node.c_syntax)
        format_string = self._get_format_string(printf_node.replacer)
        format_string_constant = self._create_global_string_constant(format_string, printf_node)

        value = self.visit(printf_node.expression)

        printf_type = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
        printf_func = ir.Function(self.module, printf_type, name="printf")

        self.builder.call(printf_func, [format_string_constant.bitcast(ir.PointerType(ir.IntType(8))), value])

    def visit_comment_statement(self, comment_node: ast.CommentStatement):
        """Visit a comment statement node and generate LLVM IR code for the comment."""
        for line in comment_node.content.split("\n"):
            self.builder.comment(line)

    def visit_body(self, body_node: ast.Body):
        """Visit a body node and generate LLVM IR code for its statements."""
        for statement in body_node.statements:
            self.visit(statement)

    def visit_expression_statement(self, expr_node: ast.ExpressionStatement):
        """Visit an expression statement node and generate LLVM IR code for the expression."""
        c_syntax_cleaned = expr_node.c_syntax.replace('\n', '\\n')
        self.builder.comment(f"C Syntax: {c_syntax_cleaned}")
        self.visit(expr_node.expression)

    def visit_shift_expression(self, shift_node: ast.ShiftExpression):
        """Visit a shift expression node and generate LLVM IR code for the shift operation."""
        value = self.visit(shift_node.value)
        amount = self.visit(shift_node.amount)

        if shift_node.operator == ast.ShiftExpression.Operator.LEFT:
            return self.builder.shl(value, amount)
        elif shift_node.operator == ast.ShiftExpression.Operator.RIGHT:
            return self.builder.ashr(value, amount)

    def visit_type(self, type_node: ast.Type):
        """Visit a type node. No LLVM IR code is generated for type nodes."""
        pass

    def visit_type_cast_expression(self, cast_node: ast.TypeCastExpression):
        """Visit a type cast expression node and generate LLVM IR code for the type cast."""
        value = self.visit(cast_node.expression)
        target_type = self._get_llvm_type(cast_node.cast_type)
        return self._cast_value(value, target_type)

    def visit_variable_declaration_qualifier(self, qualifier_node: ast.VariableDeclarationQualifier):
        """Visit a variable declaration qualifier node. No LLVM IR code is generated for variable declaration qualifiers."""
        pass

    def _get_llvm_type(self, node_type: ast.Type):
        """Get the corresponding LLVM IR type for a given AST type."""
        if node_type.base_type == ast.BaseType.int:
            return ir.IntType(32)
        elif node_type.base_type == ast.BaseType.float:
            return ir.DoubleType()
        elif node_type.base_type == ast.BaseType.char:
            return ir.IntType(8)
        else:
            raise NotImplementedError(f"Type {node_type.base_type} not supported")

    def _cast_value(self, value, target_type):
        """Cast a value to the target type."""
        value_type = value.type

        if value_type == target_type:
            return value

        if isinstance(value_type, ir.IntType) and isinstance(target_type, ir.IntType):
            if value_type.width < target_type.width:
                return self.builder.sext(value, target_type)
            elif value_type.width > target_type.width:
                return self.builder.trunc(value, target_type)
        elif isinstance(value_type, ir.IntType) and isinstance(target_type, ir.DoubleType):
            return self.builder.sitofp(value, target_type)
        elif isinstance(value_type, ir.DoubleType) and isinstance(target_type, ir.IntType):
            return self.builder.fptosi(value, target_type)
        elif isinstance(value_type, ir.DoubleType) and isinstance(target_type, ir.DoubleType):
            return value
        elif isinstance(value_type, ir.PointerType) and isinstance(target_type, ir.IntType):
            return self.builder.ptrtoint(value, target_type)

        raise NotImplementedError(f"Casting from {value_type} to {target_type} is not implemented")

    def _implicit_cast(self, value, target_type):
        """Perform implicit casting of a value to the target type."""
        value_type = value.type

        if value_type == target_type:
            return value

        if isinstance(value_type, ir.IntType) and isinstance(target_type, ir.IntType):
            if value_type.width < target_type.width:
                return self.builder.sext(value, target_type)
            elif value_type.width > target_type.width:
                return self.builder.trunc(value, target_type)
        elif isinstance(value_type, ir.IntType) and isinstance(target_type, ir.DoubleType):
            return self.builder.sitofp(value, target_type)
        elif isinstance(value_type, ir.DoubleType) and isinstance(target_type, ir.IntType):
            return self.builder.fptosi(value, target_type)
        elif isinstance(value_type, ir.DoubleType) and isinstance(target_type, ir.DoubleType):
            return value
        elif isinstance(value_type, ir.PointerType) and isinstance(target_type, ir.IntType):
            return self.builder.ptrtoint(value, target_type)
        elif isinstance(value_type, ir.IntType) and isinstance(target_type, ir.PointerType):
            return self.builder.inttoptr(value, target_type)
        elif isinstance(value_type, ir.PointerType) and isinstance(target_type, ir.PointerType):
            pointee_value = self.builder.load(value)
            casted_pointee = self._implicit_cast(pointee_value, target_type.pointee)
            casted_pointer = self.builder.alloca(target_type.pointee)
            self.builder.store(casted_pointee, casted_pointer)
            return casted_pointer

        raise NotImplementedError(f"Implicit casting from {value_type} to {target_type} is not implemented")

    def _handle_pointer_arithmetic(self, pointer, integer, operator):
        """Handle pointer arithmetic operations."""
        element_type = pointer.type.pointee
        element_size = self._size_of(element_type)
        scaled_offset = self.builder.mul(integer, ir.Constant(integer.type, element_size))

        if operator == ast.BinaryArithmetic.Operator.PLUS:
            return self.builder.gep(pointer, [scaled_offset])
        elif operator == ast.BinaryArithmetic.Operator.MINUS:
            return self.builder.gep(pointer, [self.builder.neg(scaled_offset)])

    def _handle_binary_arithmetic(self, operator, left, right):
        """Handle binary arithmetic operations."""
        if isinstance(left.type, ir.IntType) and isinstance(right.type, ir.IntType):
            if operator == ast.BinaryArithmetic.Operator.PLUS:
                return self.builder.add(left, right)
            elif operator == ast.BinaryArithmetic.Operator.MINUS:
                return self.builder.sub(left, right)
            elif operator == ast.BinaryArithmetic.Operator.MUL:
                return self.builder.mul(left, right)
            elif operator == ast.BinaryArithmetic.Operator.DIV:
                return self.builder.sdiv(left, right)
            elif operator == ast.BinaryArithmetic.Operator.MOD:
                return self.builder.srem(left, right)
        elif isinstance(left.type, ir.DoubleType) and isinstance(right.type, ir.DoubleType):
            if operator == ast.BinaryArithmetic.Operator.PLUS:
                return self.builder.fadd(left, right)
            elif operator == ast.BinaryArithmetic.Operator.MINUS:
                return self.builder.fsub(left, right)
            elif operator == ast.BinaryArithmetic.Operator.MUL:
                return self.builder.fmul(left, right)
            elif operator == ast.BinaryArithmetic.Operator.DIV:
                return self.builder.fdiv(left, right)
            elif operator == ast.BinaryArithmetic.Operator.MOD:
                return self.builder.frem(left, right)
        else:
            left = self._cast_to_common_type(left, right)
            right = self._cast_to_common_type(right, left)
            return self._handle_binary_arithmetic(operator, left, right)

    def _handle_binary_bitwise_arithmetic(self, operator, left, right):
        """Handle binary bitwise arithmetic operations."""
        if operator == ast.BinaryBitwiseArithmetic.Operator.AND:
            return self.builder.and_(left, right)
        elif operator == ast.BinaryBitwiseArithmetic.Operator.OR:
            return self.builder.or_(left, right)
        elif operator == ast.BinaryBitwiseArithmetic.Operator.XOR:
            return self.builder.xor(left, right)

    def _handle_binary_logical_operation(self, operator, left, right):
        """Handle binary logical operations."""
        if operator == ast.BinaryLogicalOperation.Operator.AND:
            return self.builder.and_(left, right)
        elif operator == ast.BinaryLogicalOperation.Operator.OR:
            return self.builder.or_(left, right)

    def _handle_comparison_operation(self, operator, left, right):
        """Handle comparison operations."""
        if isinstance(left.type, ir.PointerType) and isinstance(right.type, ir.PointerType):
            left = self.builder.ptrtoint(left, ir.IntType(64))
            right = self.builder.ptrtoint(right, ir.IntType(64))
            return self.builder.icmp_unsigned(operator.value, left, right)
        else:
            if operator == ast.ComparisonOperation.Operator.EQ:
                return self.builder.icmp_signed('==', left, right)
            elif operator == ast.ComparisonOperation.Operator.NEQ:
                return self.builder.icmp_signed('!=', left, right)
            elif operator == ast.ComparisonOperation.Operator.LT:
                return self.builder.icmp_signed('<', left, right)
            elif operator == ast.ComparisonOperation.Operator.LTE:
                return self.builder.icmp_signed('<=', left, right)
            elif operator == ast.ComparisonOperation.Operator.GT:
                return self.builder.icmp_signed('>', left, right)
            elif operator == ast.ComparisonOperation.Operator.GTE:
                return self.builder.icmp_signed('>=', left, right)

    def _handle_increment(self, operand, prefix):
        """Handle increment operations."""
        if isinstance(operand.type, ir.PointerType):
            incremented_value = self.builder.gep(operand, [ir.Constant(ir.IntType(32), 1)])
            self.builder.store(incremented_value, operand)
            return incremented_value if prefix else operand
        else:
            incremented_value = self.builder.add(operand, ir.Constant(operand.type, 1))
            self.builder.store(incremented_value, self.variables[operand.name])
            return incremented_value if prefix else operand

    def _handle_decrement(self, operand, prefix):
        """Handle decrement operations."""
        if isinstance(operand.type, ir.PointerType):
            decremented_value = self.builder.gep(operand, [ir.Constant(ir.IntType(32), -1)])
            self.builder.store(decremented_value, operand)
            return decremented_value if prefix else operand
        else:
            decremented_value = self.builder.sub(operand, ir.Constant(operand.type, 1))
            self.builder.store(decremented_value, self.variables[operand.name])
            return decremented_value if prefix else operand

    def _handle_address_of(self, operand):
        """Handle address-of operations."""
        if isinstance(operand, ir.AllocaInstr):
            return operand
        elif isinstance(operand, ir.Argument):
            return self.builder.alloca(operand.type, name=operand.name)
        elif isinstance(operand, ir.LoadInstr):
            return operand.operands[0]
        else:
            raise NotImplementedError(f"Unsupported operand type for address-of operator: {type(operand)}")

    def _handle_dereference(self, operand):
        """Handle dereference operations."""
        if isinstance(operand.type, ir.PointerType):
            return self.builder.load(operand)
        else:
            raise NotImplementedError(f"Unsupported operand type for dereference operator: {type(operand)}")

    def _get_format_string(self, replacer):
        """Get the format string based on the replacer."""
        format_string = {
            ast.PrintFCall.Replacer.d: "%d\n",
            ast.PrintFCall.Replacer.c: "%c\n",
            ast.PrintFCall.Replacer.f: "%f\n",
            ast.PrintFCall.Replacer.s: "%s\n",
            ast.PrintFCall.Replacer.x: "%x\n",
        }[replacer]
        return format_string

    def _create_global_string_constant(self, format_string, printf_node):
        """Create a global string constant for the format string."""
        format_string_constant = ir.GlobalVariable(
            self.module, ir.ArrayType(ir.IntType(8), len(format_string)),
            name=f"printf_format_{printf_node.line}_{printf_node.position}"
        )
        format_string_constant.global_constant = True
        format_string_constant.initializer = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(format_string)),
            bytearray(format_string.encode('utf-8'))
        )
        return format_string_constant

    def _size_of(self, ty):
        """Calculate the size of a type in bytes."""
        if isinstance(ty, ir.IntType):
            return ty.width // 8
        elif isinstance(ty, ir.DoubleType):
            return 8
        elif isinstance(ty, ir.PointerType):
            return 8
        else:
            raise NotImplementedError(f"Size calculation for type {ty} is not implemented")

    def _cast_to_common_type(self, left, right):
        """Cast operands to a common type."""
        if isinstance(left.type, ir.IntType) and isinstance(right.type, ir.DoubleType):
            return self.builder.sitofp(left, right.type)
        elif isinstance(left.type, ir.DoubleType) and isinstance(right.type, ir.IntType):
            return self.builder.sitofp(right, left.type)
        else:
            return left

    def visit_if_statement(self, if_node: ast.IfStatement):
        """Visit an if statement node and generate LLVM IR code for the if statement."""
        condition_value = self.visit(if_node.condition)

        #with self.builder.if_else(condition_value) as (then, otherwise):
        #    with then:
        #        self.visit(if_node.body)
        #    with otherwise:
        #        self.visit(if_node.else_statement) # Currently this doesn't have an else body


    def visit_else_statement(self, else_node: ast.ElseStatement):
        """Visit an else statement node. No LLVM IR code is generated for else statements."""
        pass

