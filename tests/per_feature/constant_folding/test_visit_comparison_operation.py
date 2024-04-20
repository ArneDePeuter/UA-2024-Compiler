from compiler.core import ast
from compiler.middleend import ConstantFoldingVisitor


def test_comparison_gt():
    my_ast = ast.ComparisonOperation(
        left=ast.INT(5),
        operator=ast.ComparisonOperation.Operator.GT,
        right=ast.FLOAT(3.5)
    )

    result = ConstantFoldingVisitor().visit_comparison_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 1


def test_comparison_lt():
    my_ast = ast.ComparisonOperation(
        left=ast.CHAR('a'),
        operator=ast.ComparisonOperation.Operator.LT,
        right=ast.INT(97)
    )

    result = ConstantFoldingVisitor().visit_comparison_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 0


def test_comparison_lt_2():
    my_ast = ast.ComparisonOperation(
        left=ast.CHAR('a'),
        operator=ast.ComparisonOperation.Operator.LT,
        right=ast.INT(98)
    )

    result = ConstantFoldingVisitor().visit_comparison_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 1


def test_comparison_gte():
    my_ast = ast.ComparisonOperation(
        left=ast.INT(10),
        operator=ast.ComparisonOperation.Operator.GTE,
        right=ast.CHAR('A')
    )

    result = ConstantFoldingVisitor().visit_comparison_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 0


def test_comparison_lte():
    my_ast = ast.ComparisonOperation(
        left=ast.FLOAT(3.5),
        operator=ast.ComparisonOperation.Operator.LTE,
        right=ast.INT(4)
    )

    result = ConstantFoldingVisitor().visit_comparison_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 1


def test_comparison_eq():
    my_ast = ast.ComparisonOperation(
        left=ast.INT(5),
        operator=ast.ComparisonOperation.Operator.EQ,
        right=ast.FLOAT(5.0)
    )

    result = ConstantFoldingVisitor().visit_comparison_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 1


def test_comparison_neq():
    my_ast = ast.ComparisonOperation(
        left=ast.INT(10),
        operator=ast.ComparisonOperation.Operator.NEQ,
        right=ast.CHAR('b')
    )

    result = ConstantFoldingVisitor().visit_comparison_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 1
