from antlr4.error.ErrorListener import ErrorListener
import antlr4

from src.antlr_files.MyGrammarLexer import MyGrammarLexer
from src.antlr_files.MyGrammarParser import MyGrammarParser


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))


def tree_from_file(filename: str):
    with open(filename, 'r') as file:
        input_stream = antlr4.InputStream(file.read())

    lexer = MyGrammarLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MyErrorListener())
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = MyGrammarParser(token_stream)

    return parser.program()
