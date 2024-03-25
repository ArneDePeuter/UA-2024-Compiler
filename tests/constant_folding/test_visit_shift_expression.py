from compiler.core import ast
from compiler.middleend import ConstantFoldingVisitor


def test_shift_left_positive():
    my_ast = ast.ShiftExpression(
        value=ast.INT(5),
        operator=ast.ShiftExpression.Operator.LEFT,
        amount=ast.INT(2)
    )

    result = ConstantFoldingVisitor().visit_shift_expression(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 20


def test_shift_left_negative():
    my_ast = ast.ShiftExpression(
        value=ast.INT(5),
        operator=ast.ShiftExpression.Operator.LEFT,
        amount=ast.INT(-1)
    )

    result = ConstantFoldingVisitor().visit_shift_expression(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 2


def test_shift_right_positive():
    my_ast = ast.ShiftExpression(
        value=ast.INT(10),
        operator=ast.ShiftExpression.Operator.RIGHT,
        amount=ast.INT(1)
    )

    result = ConstantFoldingVisitor().visit_shift_expression(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 5


def test_shift_right_negative():
    my_ast = ast.ShiftExpression(
        value=ast.INT(10),
        operator=ast.ShiftExpression.Operator.RIGHT,
        amount=ast.INT(-2)
    )

    result = ConstantFoldingVisitor().visit_shift_expression(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 40
