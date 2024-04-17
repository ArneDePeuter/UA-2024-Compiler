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

def test_if_else_1() -> None:
    input = """
        int main() {
            if (1) {
                int a = 5;
            } else {
                int b = 6;
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
    else_statement = main_func.body.statements[1]
    assert isinstance(else_statement, ast.ElseStatement)
    assert len(else_statement.body.statements) == 1
    declaration = else_statement.body.statements[0]
    assert isinstance(declaration, ast.VariableDeclaration)

def test_if_nested() -> None:
    input = """
        int main() {
            if (1) {
                if (0) {
                    int a = 10;
                }
            }
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    main_func = constructed_ast.statements[0]
    outer_if_statement = main_func.body.statements[0]
    assert isinstance(outer_if_statement, ast.IfStatement)
    assert outer_if_statement.condition.value == 1

    inner_if_statement = outer_if_statement.body.statements[0]
    assert isinstance(inner_if_statement, ast.IfStatement)
    assert inner_if_statement.condition.value == 0
    assert len(inner_if_statement.body.statements) == 1
    inner_declaration = inner_if_statement.body.statements[0]
    assert isinstance(inner_declaration, ast.VariableDeclaration)
    assert inner_declaration.qualifiers[0].identifier == "a"
    assert inner_declaration.qualifiers[0].initializer.value == 10