from compiler.frontend import tree_from_str, tree_to_ast
from compiler.core import ast

def test_if1() -> None:
    input = """
        int main() {
            if (1) {
                int a = 5;
            }
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    assert len(constructed_ast.statements) == 1
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)
    if_statement = main_func.body.statements[0]
    assert isinstance(if_statement, ast.IfStatement)
    assert if_statement.condition.value == 1
    assert len(if_statement.body.statements) == 1
    declaration = if_statement.body.statements[0]
    assert isinstance(declaration, ast.VariableDeclaration)


def test_if_with_else() -> None:
    input = """
        int main() {
            if (0) {
                int b = 10;
            } else {
                int c = 20;
            }
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    assert len(constructed_ast.statements) == 1
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)
    assert len(main_func.body.statements) == 1

    if_statement = main_func.body.statements[0]
    assert isinstance(if_statement, ast.IfStatement)
    assert if_statement.condition.value == 0
    assert len(if_statement.body.statements) == 1
    assert isinstance(if_statement.body.statements[0], ast.VariableDeclaration)
    assert if_statement.body.statements[0].qualifiers[0].identifier == 'b'

    assert isinstance(if_statement.else_statement, ast.ElseStatement)
    assert len(if_statement.else_statement.body.statements) == 1
    assert isinstance(if_statement.else_statement.body.statements[0], ast.VariableDeclaration)
    assert if_statement.else_statement.body.statements[0].qualifiers[0].identifier == 'c'


def test_if_with_else_if() -> None:
    input = """
        int main() {
            if (0) {
                int d = 30;
            } else if (1) {
                int e = 40;
            } else {
                int f = 50;
            }
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    main_func = constructed_ast.statements[0]
    if_statement = main_func.body.statements[0]
    assert isinstance(if_statement, ast.IfStatement)
    assert if_statement.condition.value == 0
    assert len(if_statement.else_statement.body.statements) == 1

    assert isinstance(if_statement.else_statement, ast.IfStatement)
    else_if_statement = if_statement.else_statement
    assert else_if_statement.condition.value == 1
    assert len(else_if_statement.body.statements) == 1
    assert else_if_statement.body.statements[0].qualifiers[0].identifier == 'e'

    assert isinstance(else_if_statement.else_statement, ast.ElseStatement)
    assert else_if_statement.else_statement.body.statements[0].qualifiers[0].identifier == 'f'
