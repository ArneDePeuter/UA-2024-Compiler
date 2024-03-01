from antlr4.error.ErrorListener import ErrorListener
import antlr4


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))


def tree_from_file(filename: str, lexer_class, parser_class):
    with open(filename, 'r') as file:
        input_stream = antlr4.InputStream(file.read())

    my_listener = MyErrorListener()
    lexer = lexer_class(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(my_listener)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = parser_class(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(my_listener)

    return parser.program()
