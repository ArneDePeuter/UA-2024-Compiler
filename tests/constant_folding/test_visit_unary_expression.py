from compiler.middleend import ConstantFoldingVisitor
from compiler.core import ast


def test_unary_positive():
    my_ast = ast.UnaryExpression(
        value=ast.INT(5),
        operator=ast.UnaryExpression.Operator.POSITIVE
    )

    result = ConstantFoldingVisitor().visit_unary_expression(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 5


def test_unary_negative():
    my_ast = ast.UnaryExpression(
        value=ast.FLOAT(3.5),
        operator=ast.UnaryExpression.Operator.NEGATIVE
    )

    result = ConstantFoldingVisitor().visit_unary_expression(my_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == -3.5


def test_unary_onescomplement():
    my_ast = ast.UnaryExpression(
        value=ast.INT(10),
        operator=ast.UnaryExpression.Operator.ONESCOMPLEMENT
    )

    result = ConstantFoldingVisitor().visit_unary_expression(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == -11


def test_unary_logicalnegation():
    my_ast = ast.UnaryExpression(
        value=ast.INT(0),
        operator=ast.UnaryExpression.Operator.LOGICALNEGATION
    )

    result = ConstantFoldingVisitor().visit_unary_expression(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 1

