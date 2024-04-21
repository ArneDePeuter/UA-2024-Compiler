from compiler.middleend import ConstantFoldingVisitor
from compiler.core import ast


def test_1():
    # 5 * (3.0 + 2)
    test_ast = ast.BinaryArithmetic(
        left=ast.INT(5),
        operator=ast.BinaryArithmetic.Operator.MUL,
        right=ast.BinaryArithmetic(
            left=ast.FLOAT(3.0),
            operator=ast.BinaryArithmetic.Operator.PLUS,
            right=ast.INT(2)
        )
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(test_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == 25
