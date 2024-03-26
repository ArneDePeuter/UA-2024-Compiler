from compiler.core import ast
from compiler.middleend import ConstantFoldingVisitor


def test_bitwise_and():
    my_ast = ast.BinaryBitwiseArithmetic(
        left=ast.INT(10),
        operator=ast.BinaryBitwiseArithmetic.Operator.AND,
        right=ast.INT(3)
    )

    result = ConstantFoldingVisitor().visit_binary_bitwise_arithmetic(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 2


def test_bitwise_or():
    my_ast = ast.BinaryBitwiseArithmetic(
        left=ast.INT(10),
        operator=ast.BinaryBitwiseArithmetic.Operator.OR,
        right=ast.INT(3)
    )

    result = ConstantFoldingVisitor().visit_binary_bitwise_arithmetic(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 11


def test_bitwise_xor():
    my_ast = ast.BinaryBitwiseArithmetic(
        left=ast.INT(10),
        operator=ast.BinaryBitwiseArithmetic.Operator.XOR,
        right=ast.INT(3)
    )

    result = ConstantFoldingVisitor().visit_binary_bitwise_arithmetic(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 9


def test_invalid_bitwise():
    my_ast = ast.BinaryBitwiseArithmetic(
        left=ast.FLOAT(10),
        operator=ast.BinaryBitwiseArithmetic.Operator.XOR,
        right=ast.INT(3)
    )

    result = ConstantFoldingVisitor().visit_binary_bitwise_arithmetic(my_ast)

    assert result is my_ast

