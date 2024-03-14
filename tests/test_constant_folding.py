from compiler.core import ast
from compiler.frontend import tree_from_file, tree_from_str, tree_to_ast
from compiler.middleend import optimise_ast


def eval_expr(eq: str) -> ast.INT:
    return ast.INT(int(eval(
        eq
        .replace("/", "//")
        .replace("||", "or")
        .replace("&&", "and")
        .replace("!", "not ")
        .replace("not =", "!=")
        .replace(";", "")
    )))


def test_folding():
    tree = tree_from_file("./files/proj1_man_pass_constantFolding.c")
    created_ast = tree_to_ast(tree)
    optimised_ast = optimise_ast(created_ast)

    assert isinstance(optimised_ast, ast.Program)

    with open("./files/proj1_man_pass_constantFolding.c", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    for i, line in enumerate(lines):
        assert optimised_ast.expressions[i] == eval_expr(line)


def test_negative_shift():
    tree = tree_from_str(data="2048 >> -3;")
    created_ast = tree_to_ast(tree)
    optimised_ast = optimise_ast(created_ast)

    assert isinstance(optimised_ast, ast.Program)
    assert optimised_ast.expressions[0] == ast.INT(eval("2048 << 3"))