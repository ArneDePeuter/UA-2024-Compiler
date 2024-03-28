import ast

from antlr4.error.ErrorListener import ErrorListener
import antlr4

from .antlr_files.GrammarParser import GrammarParser
from .antlr_files.GrammarLexer import GrammarLexer
from .parser.tree_visitor import TreeVisitor
from ..core.errors.compiler_syntaxerror import CompilerSyntaxError


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise CompilerSyntaxError(msg, line, column)


def tree_from_file(filename: str):
    with open(filename, 'r') as file:
        data = file.read()

    return tree_from_str(data)


def tree_from_str(data: str):
    input_stream = antlr4.InputStream(data)
    my_listener = MyErrorListener()
    lexer = GrammarLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(my_listener)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = GrammarParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(my_listener)

    return parser.program(), input_stream


def tree_to_ast(tree, input_stream) -> ast.AST:
    tree_visitor = TreeVisitor(input_stream)
    return tree_visitor.visit(tree)

