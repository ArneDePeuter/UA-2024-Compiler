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
        self.visit(node)
        return str(self.module)

    def visit_program(self, node: ast.Program):
        for statement in node.statements:
            self.visit(statement)

    def visit_function_declaration(self, node: ast.FunctionDeclaration):
        # Get the function return type
        return_type = self._get_llvm_type(node.return_type)

        # Create the function type
        func_type = ir.FunctionType(return_type, [])

        # Create the function
        func = ir.Function(self.module, func_type, name=node.name)

        # Create a new basic block for the function body
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        # Visit the function body
        self.visit(node.body)

        # Add a default return statement if not present
        if not block.is_terminated:
            if return_type == ir.VoidType():
                self.builder.ret_void()
            else:
                default_value = ir.Constant(return_type, None)
                self.builder.ret(default_value)

        # Reset the builder
        self.builder = None

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        self.builder.comment(f"C Syntax: {node.c_syntax}")
        for qualifier in node.qualifiers:
            var_name = qualifier.identifier
            var_type = self._get_llvm_type(node.var_type)

            # Check if the variable is a pointer type
            if node.var_type.address_qualifiers:
                # Create a pointer type based on the number of address qualifiers
                for _ in range(len(node.var_type.address_qualifiers)):
                    var_type = ir.PointerType(var_type)

            var_addr = self.builder.alloca(var_type, name=var_name)
            self.variables[var_name] = var_addr

            if qualifier.initializer is not None:
                init_value = self.visit(qualifier.initializer)

                # Cast the initializer value to the variable type if necessary
                if init_value.type != var_type:
                    if isinstance(var_type, ir.PointerType) and isinstance(init_value.type, ir.PointerType):
                        init_value = self.builder.bitcast(init_value, var_type)
                    elif isinstance(var_type, ir.IntType) and isinstance(init_value.type, ir.DoubleType):
                        init_value = self.builder.fptosi(init_value, var_type)
                    elif isinstance(var_type, ir.DoubleType) and isinstance(init_value.type, ir.IntType):
                        init_value = self.builder.sitofp(init_value, var_type)
                    else:
                        raise TypeError(
                            f"Cannot cast initializer value of type {init_value.type} to variable type {var_type}")
                self.builder.store(init_value, var_addr)

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        self.builder.comment(node.c_syntax)

        # Visit the right expression to get the value to be assigned
        value = self.visit(node.right)

        # Visit the left expression to get the assignment target
        target = self.visit(node.left)

        # Get the target type
        target_type = target.type

        # Check if the target is a pointer type
        if isinstance(target_type, ir.PointerType):
            # If the target is a pointer, we need to store the value directly
            # Cast the value to the target's pointee type if necessary
            pointee_type = target_type.pointee
            if value.type != pointee_type:
                value = self._cast_value(value, pointee_type)
            self.builder.store(value, target)
        else:
            # If the target is not a pointer, we need to allocate memory for it
            # and store the value in the allocated memory
            alloca = self.builder.alloca(target_type)
            # Cast the value to the target type if necessary
            if value.type != target_type:
                value = self._cast_value(value, target_type)
            self.builder.store(value, alloca)

            # Update the variables dictionary only if the left side is an identifier
            if isinstance(node.left, ast.IDENTIFIER):
                self.variables[node.left.name] = alloca

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        left = self.visit(node.left)
        right = self.visit(node.right)

        # Perform type conversion if necessary
        if isinstance(left.type, ir.IntType) and isinstance(right.type, ir.DoubleType):
            left = self.builder.sitofp(left, right.type)
        elif isinstance(left.type, ir.DoubleType) and isinstance(right.type, ir.IntType):
            right = self.builder.sitofp(right, left.type)

        if node.operator == ast.BinaryArithmetic.Operator.PLUS:
            if isinstance(left.type, ir.IntType):
                return self.builder.add(left, right)
            else:
                return self.builder.fadd(left, right)
        elif node.operator == ast.BinaryArithmetic.Operator.MINUS:
            if isinstance(left.type, ir.IntType):
                return self.builder.sub(left, right)
            else:
                return self.builder.fsub(left, right)
        elif node.operator == ast.BinaryArithmetic.Operator.MUL:
            if isinstance(left.type, ir.IntType):
                return self.builder.mul(left, right)
            else:
                return self.builder.fmul(left, right)
        elif node.operator == ast.BinaryArithmetic.Operator.DIV:
            if isinstance(left.type, ir.IntType):
                return self.builder.sdiv(left, right)
            else:
                return self.builder.fdiv(left, right)
        elif node.operator == ast.BinaryArithmetic.Operator.MOD:
            if isinstance(left.type, ir.IntType):
                return self.builder.srem(left, right)
            else:
                return self.builder.frem(left, right)

    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self._handle_binary_bitwise_arithmetic(node.operator, left, right)

    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self._handle_binary_logical_operation(node.operator, left, right)

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self._handle_comparison_operation(node.operator, left, right)

    def visit_binary_operation(self, node: ast.BinaryOperation):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node, ast.BinaryArithmetic):
            return self._handle_binary_arithmetic(node.operator, left, right)
        elif isinstance(node, ast.BinaryBitwiseArithmetic):
            return self._handle_binary_bitwise_arithmetic(node.operator, left, right)
        elif isinstance(node, ast.BinaryLogicalOperation):
            return self._handle_binary_logical_operation(node.operator, left, right)
        elif isinstance(node, ast.ComparisonOperation):
            return self._handle_comparison_operation(node.operator, left, right)
        else:
            raise NotImplementedError(f"Unsupported binary operation: {type(node)}")

    def _handle_binary_arithmetic(self, operator, left, right):
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
        if operator == ast.BinaryBitwiseArithmetic.Operator.AND:
            return self.builder.and_(left, right)
        elif operator == ast.BinaryBitwiseArithmetic.Operator.OR:
            return self.builder.or_(left, right)
        elif operator == ast.BinaryBitwiseArithmetic.Operator.XOR:
            return self.builder.xor(left, right)
        else:
            raise NotImplementedError(f"Unsupported bitwise arithmetic operator: {operator}")

    def _handle_binary_logical_operation(self, operator, left, right):
        if operator == ast.BinaryLogicalOperation.Operator.AND:
            return self.builder.and_(left, right)
        elif operator == ast.BinaryLogicalOperation.Operator.OR:
            return self.builder.or_(left, right)
        else:
            raise NotImplementedError(f"Unsupported logical operator: {operator}")

    def _handle_comparison_operation(self, operator, left, right):
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
        else:
            raise NotImplementedError(f"Unsupported comparison operator: {operator}")

    def visit_unary_expression(self, node: ast.UnaryExpression):
        operand = self.visit(node.value)
        if node.operator == ast.UnaryExpression.Operator.POSITIVE:
            return operand
        elif node.operator == ast.UnaryExpression.Operator.NEGATIVE:
            return self.builder.neg(operand)
        elif node.operator == ast.UnaryExpression.Operator.LOGICALNEGATION:
            return self.builder.not_(operand)
        elif node.operator == ast.UnaryExpression.Operator.ADDRESSOF:
            if isinstance(operand, ir.AllocaInstr):
                return operand
            elif isinstance(operand, ir.Argument):
                return self.builder.alloca(operand.type, name=operand.name)
            elif isinstance(operand, ir.LoadInstr):
                return operand.operands[0]  # Return the pointer being loaded
            else:
                raise NotImplementedError(f"Unsupported operand type for address-of operator: {type(operand)}")
        elif node.operator == ast.UnaryExpression.Operator.DEREFERENCE:
            if isinstance(operand.type, ir.PointerType):
                return self.builder.load(operand)
            else:
                raise NotImplementedError(f"Unsupported operand type for dereference operator: {type(operand)}")
        else:
            raise NotImplementedError(f"Unsupported unary operator: {node.operator}")

    def visit_int(self, node: ast.INT):
        return ir.Constant(ir.IntType(32), node.value)

    def visit_float(self, node: ast.FLOAT):
        return ir.Constant(ir.DoubleType(), node.value)

    def visit_char(self, node: ast.CHAR):
        return ir.Constant(ir.IntType(8), ord(node.value))

    def visit_identifier(self, node: ast.IDENTIFIER):
        var_addr = self.variables[node.name]
        return self.builder.load(var_addr)

    def visit_printf_call(self, node: ast.PrintFCall):
        self.builder.comment(node.c_syntax)
        # Get the format string based on the replacer
        format_string = {
            ast.PrintFCall.Replacer.d: "%d\n",
            ast.PrintFCall.Replacer.c: "%c\n",
            ast.PrintFCall.Replacer.f: "%f\n",
            ast.PrintFCall.Replacer.s: "%s\n",
            ast.PrintFCall.Replacer.x: "%x\n",
        }[node.replacer]

        # Create a global string constant for the format string
        format_string_constant = ir.GlobalVariable(
            self.module, ir.ArrayType(ir.IntType(8), len(format_string)),
            name=f"printf_format_{node.line}_{node.position}"
        )
        format_string_constant.global_constant = True
        format_string_constant.initializer = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(format_string)),
            bytearray(format_string.encode('utf-8'))
        )

        # Generate the IR for the expression to be printed
        value = self.visit(node.expression)

        # Declare the printf function
        printf_type = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
        printf_func = ir.Function(self.module, printf_type, name="printf")

        # Call the printf function with the format string and the value
        self.builder.call(printf_func, [format_string_constant.bitcast(ir.PointerType(ir.IntType(8))), value])

    def visit_comment_statement(self, node: ast.CommentStatement):
        for line in node.content.split("\n"):
            self.builder.comment(line)

    def _get_llvm_type(self, node_type: ast.Type):
        if node_type.base_type == ast.BaseType.int:
            return ir.IntType(32)
        elif node_type.base_type == ast.BaseType.float:
            return ir.DoubleType()
        elif node_type.base_type == ast.BaseType.char:
            return ir.IntType(8)
        else:
            raise NotImplementedError(f"Type {node_type.base_type} not supported")

    def visit_body(self, node: ast.Body):
        for statement in node.statements:
            self.visit(statement)

    def visit_expression_statement(self, node: ast.ExpressionStatement):
        self.visit(node.expression)

    def visit_shift_expression(self, node: ast.ShiftExpression):
        value = self.visit(node.value)
        amount = self.visit(node.amount)
        if node.operator == ast.ShiftExpression.Operator.LEFT:
            return self.builder.shl(value, amount)
        elif node.operator == ast.ShiftExpression.Operator.RIGHT:
            return self.builder.ashr(value, amount)
        else:
            raise NotImplementedError(f"Unsupported shift operator: {node.operator}")

    def visit_type(self, node: ast.Type):
        # No need to generate LLVM IR for type nodes
        pass

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        value = self.visit(node.expression)
        target_type = self._get_llvm_type(node.cast_type)
        return self._cast_value(value, target_type)

    def _cast_value(self, value, target_type):
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
            return value  # No casting needed for double to double

        raise NotImplementedError(f"Casting from {value_type} to {target_type} is not implemented")

    def _cast_to_common_type(self, left, right):
        if isinstance(left.type, ir.IntType) and isinstance(right.type, ir.DoubleType):
            return self.builder.sitofp(left, right.type)
        elif isinstance(left.type, ir.DoubleType) and isinstance(right.type, ir.IntType):
            return self.builder.sitofp(right, left.type)
        else:
            return left

    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        # No need to generate LLVM IR for variable declaration qualifiers
        pass