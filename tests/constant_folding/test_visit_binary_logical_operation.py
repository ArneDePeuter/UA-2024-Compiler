from compiler.core import ast
from compiler.middleend import ConstantFoldingVisitor


def test_logical_and_1():
    my_ast = ast.BinaryLogicalOperation(
        left=ast.INT(1),
        operator=ast.BinaryLogicalOperation.Operator.AND,
        right=ast.INT(0)
    )

    result = ConstantFoldingVisitor().visit_binary_logical_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 0


def test_logical_and_2():
    my_ast = ast.BinaryLogicalOperation(
        left=ast.INT(1),
        operator=ast.BinaryLogicalOperation.Operator.AND,
        right=ast.INT(1)
    )

    result = ConstantFoldingVisitor().visit_binary_logical_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 1


def test_logical_or_1():
    my_ast = ast.BinaryLogicalOperation(
        left=ast.INT(1),
        operator=ast.BinaryLogicalOperation.Operator.OR,
        right=ast.INT(0)
    )

    result = ConstantFoldingVisitor().visit_binary_logical_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 1


def test_logical_or_2():
    my_ast = ast.BinaryLogicalOperation(
        left=ast.INT(0),
        operator=ast.BinaryLogicalOperation.Operator.OR,
        right=ast.INT(0)
    )

    result = ConstantFoldingVisitor().visit_binary_logical_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 0


def test_logical_and_mixed_types_1():
    my_ast = ast.BinaryLogicalOperation(
        left=ast.INT(0),
        operator=ast.BinaryLogicalOperation.Operator.AND,
        right=ast.FLOAT(0.1)
    )

    result = ConstantFoldingVisitor().visit_binary_logical_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 0


def test_logical_and_mixed_types_2():
    my_ast = ast.BinaryLogicalOperation(
        left=ast.INT(0),
        operator=ast.BinaryLogicalOperation.Operator.AND,
        right=ast.CHAR(' ')
    )

    result = ConstantFoldingVisitor().visit_binary_logical_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 0


def test_logical_or_mixed_types_1():
    my_ast = ast.BinaryLogicalOperation(
        left=ast.INT(1),
        operator=ast.BinaryLogicalOperation.Operator.OR,
        right=ast.FLOAT(0.1)
    )

    result = ConstantFoldingVisitor().visit_binary_logical_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 1


def test_logical_or_mixed_types_2():
    my_ast = ast.BinaryLogicalOperation(
        left=ast.INT(0),
        operator=ast.BinaryLogicalOperation.Operator.OR,
        right=ast.CHAR(' ')
    )

    result = ConstantFoldingVisitor().visit_binary_logical_operation(my_ast)

    assert isinstance(result, ast.INT)
    assert result.value == 1
