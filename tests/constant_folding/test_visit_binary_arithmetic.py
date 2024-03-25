import pytest

from compiler.middleend import ConstantFoldingVisitor
from compiler.core import ast


def test_addition_1():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(5),
        operator=ast.BinaryArithmetic.Operator.PLUS,
        right=ast.INT(3)
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == 8


def test_addition_2():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(5.2),
        operator=ast.BinaryArithmetic.Operator.PLUS,
        right=ast.CHAR('a')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == 102.2


def test_addition_3():
    my_ast = ast.BinaryArithmetic(
        left=ast.INT(10),
        operator=ast.BinaryArithmetic.Operator.PLUS,
        right=ast.CHAR('b')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 108


def test_multiplication_1():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(5),
        operator=ast.BinaryArithmetic.Operator.MUL,
        right=ast.INT(3)
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == 15.0


def test_multiplication_2():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(5.2),
        operator=ast.BinaryArithmetic.Operator.MUL,
        right=ast.CHAR('a')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == pytest.approx(504.4, 0.01)


def test_multiplication_3():
    my_ast = ast.BinaryArithmetic(
        left=ast.INT(10),
        operator=ast.BinaryArithmetic.Operator.MUL,
        right=ast.CHAR('b')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 980


def test_modulo_1():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(10.5),
        operator=ast.BinaryArithmetic.Operator.MOD,
        right=ast.INT(3)
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == pytest.approx(1.5, 0.01)


def test_modulo_2():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(15.2),
        operator=ast.BinaryArithmetic.Operator.MOD,
        right=ast.CHAR('a')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == 15.2


def test_modulo_3():
    my_ast = ast.BinaryArithmetic(
        left=ast.INT(33),
        operator=ast.BinaryArithmetic.Operator.MOD,
        right=ast.CHAR(' ')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 1


def test_subtraction_1():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(10.5),
        operator=ast.BinaryArithmetic.Operator.MINUS,
        right=ast.INT(3)
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == 7.5


def test_subtraction_2():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(5.5),
        operator=ast.BinaryArithmetic.Operator.MINUS,
        right=ast.CHAR('2')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == -44.5


def test_subtraction_3():
    my_ast = ast.BinaryArithmetic(
        left=ast.INT(8),
        operator=ast.BinaryArithmetic.Operator.MINUS,
        right=ast.CHAR('2')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == -42


def test_division_1():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(10.0),
        operator=ast.BinaryArithmetic.Operator.DIV,
        right=ast.INT(2)
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == 5.0


def test_division_2():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(8.5),
        operator=ast.BinaryArithmetic.Operator.DIV,
        right=ast.CHAR('2')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.FLOAT)
    assert result.value == 0.17


def test_division_3():
    my_ast = ast.BinaryArithmetic(
        left=ast.INT(510),
        operator=ast.BinaryArithmetic.Operator.DIV,
        right=ast.CHAR('3')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 10
