from compiler.core import ast
from compiler.frontend import tree_from_str, tree_to_ast
from compiler.middleend import ConstantPropagationVisitor


def test_1():
    test_str = """
    int main() {
        int a = 5;
        int b = a + 3;
    }
    """

    tree, input_stream = tree_from_str(test_str)
    output_ast = tree_to_ast(tree, input_stream)
    result = ConstantPropagationVisitor().visit_statement(output_ast)

    assert isinstance(result, ast.Program)
    assert type(result.statements[0].body.statements[1].qualifiers[0].initializer.left) == ast.INT
    assert result.statements[0].body.statements[1].qualifiers[0].initializer.left.value == 5


def test_2():
    test_str = """
    int main() {
        int a = 5;
        int b = 3;
        int c = a + b;
    }
    """

    tree, input_stream = tree_from_str(test_str)
    output_ast = tree_to_ast(tree, input_stream)
    result = ConstantPropagationVisitor().visit_statement(output_ast)

    assert isinstance(result, ast.Program)
    assert type(result.statements[0].body.statements[2].qualifiers[0].initializer.left) == ast.IDENTIFIER
    assert type(result.statements[0].body.statements[2].qualifiers[0].initializer.right) == ast.INT
    assert result.statements[0].body.statements[2].qualifiers[0].initializer.right.value == 3


def test_3():
    test_str = """
    int main() {
        const int a = 5;
        int b = 3;
        int c = a + b;
    }
    """

    tree, input_stream = tree_from_str(test_str)
    output_ast = tree_to_ast(tree, input_stream)
    result = ConstantPropagationVisitor().visit_statement(output_ast)

    assert isinstance(result, ast.Program)
    assert type(result.statements[0].body.statements[2].qualifiers[0].initializer.left) == ast.INT
    assert result.statements[0].body.statements[2].qualifiers[0].initializer.left.value == 5
    assert type(result.statements[0].body.statements[2].qualifiers[0].initializer.right) == ast.INT
    assert result.statements[0].body.statements[2].qualifiers[0].initializer.right.value == 3