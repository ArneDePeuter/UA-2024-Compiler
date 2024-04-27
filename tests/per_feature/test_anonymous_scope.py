import pytest

from compiler.frontend.symbol_table.symbol_table_visitor import SymbolTableVisitor
from compiler.frontend import tree_from_str, tree_to_ast
from compiler.core.errors.compiler_syntaxerror import CompilerSyntaxError


def test_semantic_1():
    input = """
        int main() {
            int b = 3;
            {
                int a = 5;
                b = 5;
            }
            int a = 3;
        }
    """
    tree, input_stream = tree_from_str(input)
    ast, tree_visitor = tree_to_ast(tree, input_stream)
    symbol_table = SymbolTableVisitor(tree_visitor=tree_visitor)
    symbol_table.visit_program(ast)


def test_syntax_1():
    input = """
        int main() {
            {
                int a = 5;
            }
            int a = 3;
        }
    """
    tree_from_str(input)


def test_syntax_2():
    input = """
        int main() {
            {
                int a = 5;
            int a = 3;
        }
    """

    with pytest.raises(CompilerSyntaxError):
        tree_from_str(input)