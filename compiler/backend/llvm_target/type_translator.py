from compiler.core import ast
from llvmlite import ir

from .ir_types import IrIntType, IrFloatType, IrCharType


class TypeTranslator:
    @staticmethod
    def translate_ast_type(node: ast.Type) -> ir.Type:
        llvm_base_type = TypeTranslator.translate_ast_base_type(node.base_type)

        if node.address_qualifiers:
            for qualifier in node.address_qualifiers:
                if qualifier == ast.AddressQualifier.pointer:
                    llvm_base_type = ir.PointerType(llvm_base_type)

        return llvm_base_type

    @staticmethod
    def translate_ast_base_type(base_type: ast.BaseType) -> ir.Type:
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
        if target == value.type:
            return value
        elif isinstance(target, ir.IntType) and isinstance(value.type, ir.FloatType):
            return builder.fptosi(value, target)
        elif isinstance(target, ir.FloatType) and isinstance(value.type, ir.IntType):
            return builder.sitofp(value, target)
        elif isinstance(target, ir.IntType) and isinstance(value.type, ir.PointerType):
            return builder.ptrtoint(value, target)
        elif isinstance(target, ir.PointerType) and isinstance(value.type, ir.FloatType):
            return builder.fptosi(value, target)
        elif isinstance(target, ir.ArrayType):
            return TypeTranslator.match_llvm_type(builder, target.element, value)
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