from compiler.frontend import tree_from_str, tree_to_ast
from compiler.core import ast


def test_1() -> None:
    input = """
        typedef int a;

        int main() {
            a b = 5;
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    assert len(constructed_ast.statements) == 1
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)
    declaration = main_func.body.statements[0]
    assert isinstance(declaration, ast.VariableDeclaration)
    assert declaration.var_type.base_type == ast.BaseType.int


def test_2() -> None:
    input = """
        typedef int c;
        typedef c a;

        int main() {
            a b = 5;
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    assert len(constructed_ast.statements) == 1
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)
    declaration = main_func.body.statements[0]
    assert isinstance(declaration, ast.VariableDeclaration)
    assert declaration.var_type.base_type == ast.BaseType.int