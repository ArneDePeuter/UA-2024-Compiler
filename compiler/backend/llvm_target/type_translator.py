from compiler.core import ast
from llvmlite import ir

from .ir_types import IrIntType, IrFloatType, IrCharType, IrArrayType


class TypeTranslator:
    @staticmethod
    def translate_ast_type(node: ast.Type) -> ir.Type:
        llvm_base_type = TypeTranslator.translate_ast_base_type(node.type)

        if node.address_qualifiers:
            for qualifier in node.address_qualifiers:
                if qualifier == ast.AddressQualifier.pointer:
                    llvm_base_type = ir.PointerType(llvm_base_type)

        return llvm_base_type

    @staticmethod
    def get_array_size(array_type: ast.ArrayType) -> int:
        size = 1
        for array_size in array_type.array_sizes.sizes:
            size *= array_size.value
        return size

    @staticmethod
    def translate_ast_base_type(base_type: ast.BaseType) -> ir.Type:
        if isinstance(base_type, ast.ArrayType):
            element_type = None
            for size in reversed(base_type.array_sizes.sizes):
                if element_type is None:
                    element_type = ir.ArrayType(TypeTranslator.translate_ast_base_type(base_type.element_type.type), size.value)
                else:
                    element_type = ir.ArrayType(element_type, size.value)
            return element_type

        llvm_type = {
            ast.BaseType.int: IrIntType,
            ast.BaseType.float: IrFloatType,
            ast.BaseType.char: IrCharType,
            ast.BaseType.void: ir.VoidType(),
        }.get(base_type, None)

        if llvm_type is None:
            raise NotImplementedError(f"Translation of base type {base_type} not implemented.")

        return llvm_type

    @staticmethod
    def match_llvm_type(builder: ir.IRBuilder, target: ir.Type, value: ir.Constant) -> ir.Constant:
        # TODO: Once a array is partially initialized, it should be filled with zeros
        #if isinstance(value.type, ir.ArrayType):
        #    if value.type.count < target.count:
        #        num_it = target.count - value.type.count
        #        for _ in range(num_it):
        #            builder.insert_value(value, ir.Constant(IrIntType, 0), value.type.count)
        if target == value.type:
            return value
        elif isinstance(target, ir.PointerType) and not isinstance(value, ir.PointerType):
            return ir.Constant(target, None)
        elif isinstance(target, ir.IntType) and isinstance(value.type, ir.FloatType):
            return builder.fptosi(value, target)
        elif isinstance(target, ir.FloatType) and isinstance(value.type, ir.IntType):
            return builder.sitofp(value, target)
        elif isinstance(target, ir.IntType) and isinstance(value.type, ir.PointerType):
            return builder.ptrtoint(value, target)
        elif isinstance(target, ir.PointerType) and isinstance(value.type, ir.FloatType):
            return builder.fptosi(value, target)
        elif isinstance(target, ir.ArrayType):
            return TypeTranslator.match_llvm_type(builder, target.elements, value)
        elif isinstance(target, ir.ArrayType) and isinstance(value.type, ir.ArrayType) and target.element == value.type.element:
            # Handle partial array initialization
            if value.type.count < target.count:
                # Fill remaining elements with zeros if partially initialized
                extended_value = [value.getelement(i) for i in range(value.type.count)]
                extended_value += [ir.Constant(value.type.element, 0) for _ in range(target.count - value.type.count)]
                return ir.Constant(target, extended_value)
            return value
        elif target.width > value.type.width:
            return builder.zext(value, target)
        elif target.width < value.type.width:
            return builder.trunc(value, target)
        else:
            raise NotImplementedError(f"Type cast from {value} to {target} is not supported")

    @staticmethod
    def cast_to_common_type(builder: ir.IRBuilder, left: ir.Constant, right: ir.Constant) -> tuple[ir.Constant, ir.Constant]:
        if left.type == right.type:
            return left, right
        if isinstance(left.type, ir.IntType) and isinstance(right.type, ir.FloatType):
            return builder.sitofp(left, right.type), right
        elif isinstance(left.type, ir.FloatType) and isinstance(right.type, ir.IntType):
            return left, builder.sitofp(right, left.type)
        elif isinstance(left.type, ir.IntType) and isinstance(right.type, ir.IntType):
            if left.type.width > right.type.width:
                return left, builder.zext(right, left.type)
            else:
                return builder.zext(left, right.type), right

    @staticmethod
    def get_type_size(target: ir.Type) -> int:
        if isinstance(target, ir.IntType):
            return target.width // 8
        elif isinstance(target, ir.FloatType):
            return 4
        elif isinstance(target, ir.PointerType):
            return 8
        elif isinstance(target, ir.ArrayType):
            return TypeTranslator.get_type_size(target.element) * target.count
        else:
            raise NotImplementedError(f"Size of type {target} not implemented.")