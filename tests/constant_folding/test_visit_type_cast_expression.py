from dataclasses import asdict

from compiler.middleend import ConstantFoldingVisitor
from compiler.core import ast


def test_int_conv_1():
    test_ast = ast.TypeCastExpression(
        cast_type=ast.Type(
            base_type=ast.BaseType.int
        ),
        expression=ast.CHAR(value="a")
    )

    folded = ConstantFoldingVisitor().visit_type_cast_expression(test_ast)
    expected = ast.INT(
        value=97
    )

    assert type(folded) == type(expected)
    assert folded.value == expected.value


def test_int_conv_2():
    test_ast = ast.TypeCastExpression(
        cast_type=ast.Type(
            base_type=ast.BaseType.int
        ),
        expression=ast.INT(value=5)
    )

    folded = ConstantFoldingVisitor().visit_type_cast_expression(test_ast)
    expected = ast.INT(
        value=5
    )

    assert type(folded) == type(expected)
    assert folded.value == expected.value


def test_int_conv_3():
    test_ast = ast.TypeCastExpression(
        cast_type=ast.Type(
            base_type=ast.BaseType.int
        ),
        expression=ast.FLOAT(value=5.3)
    )

    folded = ConstantFoldingVisitor().visit_type_cast_expression(test_ast)
    expected = ast.INT(
        value=5
    )

    assert type(folded) == type(expected)
    assert folded.value == expected.value


def test_char_conv_1():
    test_ast = ast.TypeCastExpression(
        cast_type=ast.Type(
            base_type=ast.BaseType.char
        ),
        expression=ast.INT(value=97)
    )

    folded = ConstantFoldingVisitor().visit_type_cast_expression(test_ast)
    expected = ast.CHAR(
        value="a"
    )

    assert type(folded) == type(expected)
    assert folded.value == expected.value


def test_char_conv_2():
    test_ast = ast.TypeCastExpression(
        cast_type=ast.Type(
            base_type=ast.BaseType.char
        ),
        expression=ast.CHAR(value="Z")
    )

    folded = ConstantFoldingVisitor().visit_type_cast_expression(test_ast)
    expected = ast.CHAR(
        value="Z"
    )

    assert type(folded) == type(expected)
    assert folded.value == expected.value


def test_char_conv_3():
    test_ast = ast.TypeCastExpression(
        cast_type=ast.Type(
            base_type=ast.BaseType.char
        ),
        expression=ast.FLOAT(value=97.3)
    )

    folded = ConstantFoldingVisitor().visit_type_cast_expression(test_ast)
    expected = ast.CHAR(
        value='a'
    )

    assert type(folded) == type(expected)
    assert folded.value == expected.value


def test_float_conv_1():
    test_ast = ast.TypeCastExpression(
        cast_type=ast.Type(
            base_type=ast.BaseType.float
        ),
        expression=ast.INT(value=5)
    )

    folded = ConstantFoldingVisitor().visit_type_cast_expression(test_ast)
    expected = ast.FLOAT(
        value=5.0
    )

    assert type(folded) == type(expected)
    assert folded.value == expected.value


def test_float_conv_2():
    test_ast = ast.TypeCastExpression(
        cast_type=ast.Type(
            base_type=ast.BaseType.float
        ),
        expression=ast.CHAR(value="a")
    )

    folded = ConstantFoldingVisitor().visit_type_cast_expression(test_ast)
    expected = ast.FLOAT(
        value=97.0
    )

    assert type(folded) == type(expected)
    assert folded.value == expected.value


def test_float_conv_3():
    test_ast = ast.TypeCastExpression(
        cast_type=ast.Type(
            base_type=ast.BaseType.float
        ),
        expression=ast.FLOAT(value=5.5)
    )

    folded = ConstantFoldingVisitor().visit_type_cast_expression(test_ast)
    expected = ast.FLOAT(
        value=5.5
    )

    assert type(folded) == type(expected)
    assert folded.value == expected.value


def test_no_conv():
    no_conv_asts = [
        ast.IDENTIFIER("a"),
        ast.BinaryArithmetic(
            left=ast.INT(2),
            operator=ast.BinaryArithmetic.Operator.PLUS,
            right=ast.IDENTIFIER("a")
        )
    ]

    for no_conv_ast in no_conv_asts:
        no_conv_ast = ast.TypeCastExpression(
            cast_type=ast.Type(
                base_type=ast.BaseType.float
            ),
            expression=no_conv_ast
        )
        assert asdict(no_conv_ast) == asdict(ConstantFoldingVisitor().visit(no_conv_ast))

