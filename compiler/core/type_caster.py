from typing import Union

from . import ast
from compiler.core.errors.semantic_error import SemanticError


class TypeCaster:
    heirarchy = [ast.CHAR, ast.INT, ast.FLOAT]

    @staticmethod
    def upcast(item: Union[ast.INT, ast.CHAR]) -> Union[ast.FLOAT, ast.INT]:
        if isinstance(item, ast.INT):
            return ast.FLOAT(
                value=float(item.value),
                line=item.line,
                position=item.position
            )
        if isinstance(item, ast.CHAR):
            return ast.INT(
                value=ord(item.value),
                line=item.line,
                position=item.position
            )

    @staticmethod
    def downcast(item: Union[ast.FLOAT, ast.INT]) -> Union[ast.INT, ast.CHAR]:
        if isinstance(item, ast.FLOAT):
            return ast.INT(
                value=int(item.value),
                line=item.line,
                position=item.position
            )
        if isinstance(item, ast.INT):
            return ast.CHAR(
                value=chr(item.value),
                line=item.line,
                position=item.position
            )

    @staticmethod
    def get_heirarchy_of_ast(input: Union[ast.FLOAT, ast.INT, ast.CHAR]) -> int:
        return TypeCaster.heirarchy.index(type(input))

    @staticmethod
    def get_heirarchy_of_base_type(input: ast.BaseType) -> int:
        res = None
        if input == ast.BaseType.int:
            res = ast.INT(value=0)
        elif input == ast.BaseType.float:
            res = ast.FLOAT(value=0)
        elif input == ast.BaseType.char:
            res = ast.CHAR(value="0")
        return TypeCaster.get_heirarchy_of_ast(res)

