from compiler.core import ast
from compiler.middleend import ConstantFoldingVisitor


def test_addition_1():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(5),
        operator=ast.BinaryArithmetic.Operator.PLUS,
        right=ast.INT(3)
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert result == ast.FLOAT(8)


def test_addition_2():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(5.2),
        operator=ast.BinaryArithmetic.Operator.PLUS,
        right=ast.CHAR('a')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert result == ast.FLOAT(102.2)


def test_addition_3():
    my_ast = ast.BinaryArithmetic(
        left=ast.INT(10),
        operator=ast.BinaryArithmetic.Operator.PLUS,
        right=ast.CHAR('b')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert result == ast.INT(108)


def test_addition_4():
    my_ast = ast.BinaryArithmetic(
        left=ast.CHAR('c'),
        operator=ast.BinaryArithmetic.Operator.PLUS,
        right=ast.INT(20)
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert result == ast.INT(119)


def test_addition_5():
    my_ast = ast.BinaryArithmetic(
        left=ast.CHAR('d'),
        operator=ast.BinaryArithmetic.Operator.PLUS,
        right=ast.FLOAT(30.5)
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert result == ast.FLOAT(130.5)


def test_subtraction():
    my_ast = ast.BinaryArithmetic(
        left=ast.INT(10),
        operator=ast.BinaryArithmetic.Operator.MINUS,
        right=ast.FLOAT(5.5)
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert result == ast.FLOAT(4.5)


def test_multiplication():
    my_ast = ast.BinaryArithmetic(
        left=ast.FLOAT(2.5),
        operator=ast.BinaryArithmetic.Operator.MUL,
        right=ast.INT(4)
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert result == ast.FLOAT(10.0)


def test_division():
    my_ast = ast.BinaryArithmetic(
        left=ast.INT(20),
        operator=ast.BinaryArithmetic.Operator.DIV,
        right=ast.CHAR('5')
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert result == ast.INT(0)


def test_modulus():
    my_ast = ast.BinaryArithmetic(
        left=ast.CHAR('a'),
        operator=ast.BinaryArithmetic.Operator.MOD,
        right=ast.INT(3)
    )

    result = ConstantFoldingVisitor().visit_binary_arithmetic(my_ast)

    assert result == ast.INT(1)
