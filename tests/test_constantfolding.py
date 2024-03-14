from src.frontend.parser.tree_creation import tree_from_str, tree_from_file
from src.antlr_files.project_1.MyGrammarParser import MyGrammarParser
from src.frontend.antlr_files.project_1.MyGrammarLexer import MyGrammarLexer
from src.middleend.optimizervisitor import OptimizerVisitor
from src.frontend.parser.cst_visitor import CSTVisitor

from src.core.ast.program import Program
from src.core.ast import expression as expr


def eval_expr(eq: str) -> expr.INT:
    return expr.INT(int(eval(
        eq
        .replace("/", "//")
        .replace("||", "or")
        .replace("&&", "and")
        .replace("!", "not ")
        .replace("not =", "!=")
        .replace(";", "")
    )))


def test_folding():
    tree = tree_from_file(
        filename="files/proj1_man_pass_constantFolding.c",
        lexer_class=MyGrammarLexer,
        parser_class=MyGrammarParser
    )

    cst_visitor = CSTVisitor()
    ast = cst_visitor.visit(tree)

    optimizer_visitor = OptimizerVisitor()
    ast: Program = optimizer_visitor.visit_ast(ast)

    assert isinstance(ast, Program)

    with open("files/proj1_man_pass_constantFolding.c", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    for i, line in enumerate(lines):
        assert ast.statements[i] == eval_expr(line)


def test_negative_shift():
    tree = tree_from_str(
        data="2048 >> -3;",
        lexer_class=MyGrammarLexer,
        parser_class=MyGrammarParser
    )

    cst_visitor = CSTVisitor()
    ast = cst_visitor.visit(tree)

    optimizer_visitor = OptimizerVisitor()
    ast: Program = optimizer_visitor.visit_ast(ast)

    assert isinstance(ast, Program)

    assert ast.statements[0] == expr.INT(eval("2048 << 3"))
