from llvmlite import ir
from compiler.core.ast_visitor import AstVisitor
from compiler.core import ast

class LLVMIRGenerator(AstVisitor):
    def __init__(self):
        super().__init__()
        self.module = ir.Module()
        self.builder = None
        self.variables = {}
        self.comment_map = {}

    def generate_llvm_ir(self, node):
        self.visit(node)
        self.append_comments()
        return str(self.module)

    def append_comments(self):
        for line_num, node in self.comment_map.items():
            if isinstance(node, ast.CommentStatement):
                self.module.get_global(line_num).set_metadata('comment', f"{node.content}")
            else:
                self.module.get_global(line_num).set_metadata('node', f"{node}")

    def visit_program(self, node: ast.Program):
        main_func = ir.FunctionType(ir.IntType(32), [])
        func = ir.Function(self.module, main_func, 'main')
        block = func.append_basic_block('entry')
        self.builder = ir.IRBuilder(block)

        for statement in node.statements:
            self.visit(statement)

        self.builder.ret(ir.Constant(ir.IntType(32), 0))

    def visit_function_declaration(self, node: ast.FunctionDeclaration):
        # Skipping function declaration for now
        pass

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        for qualifier in node.qualifiers:
            var_name = qualifier.identifier
            var_type = self._get_llvm_type(node.var_type)
            var_addr = self.builder.alloca(var_type, name=var_name)
            self.variables[var_name] = var_addr

            if qualifier.initializer:
                init_value = self.visit(qualifier.initializer)
                self.builder.store(init_value, var_addr)

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        var_addr = self.variables[node.identifier]
        value = self.visit(node.value)
        value = self._cast_value(value, var_addr.type.pointee)
        self.builder.store(value, var_addr)

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return self._handle_binary_arithmetic(node.operator, left, right)

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
        # Skipping printf call for now
        pass

    def visit_comment_statement(self, node: ast.CommentStatement):
        # Comments are handled separately in the append_comments method
        pass

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

    def visit_expression(self, node: ast.Expression):
        if isinstance(node, ast.BinaryOperation):
            return self.visit_binary_operation(node)
        elif isinstance(node, ast.UnaryExpression):
            return self.visit_unary_expression(node)
        elif isinstance(node, ast.INT):
            return self.visit_int(node)
        elif isinstance(node, ast.FLOAT):
            return self.visit_float(node)
        elif isinstance(node, ast.CHAR):
            return self.visit_char(node)
        elif isinstance(node, ast.IDENTIFIER):
            return self.visit_identifier(node)
        elif isinstance(node, ast.TypeCastExpression):
            return self.visit_type_cast_expression(node)
        elif isinstance(node, ast.Expression):
            return self.visit(node)
        else:
            raise NotImplementedError(f"Unsupported expression type: {type(node)}")

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
        if isinstance(value.type, ir.IntType) and isinstance(target_type, ir.DoubleType):
            return self.builder.sitofp(value, target_type)
        elif isinstance(value.type, ir.DoubleType) and isinstance(target_type, ir.IntType):
            return self.builder.fptosi(value, target_type)
        else:
            return value

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