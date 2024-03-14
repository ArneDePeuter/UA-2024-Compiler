from src.frontend.parser.tree_creation import tree_from_file
from src.antlr_files.project_1.MyGrammarParser import MyGrammarParser
from src.frontend.antlr_files.project_1.MyGrammarLexer import MyGrammarLexer


def test_intliteralbeginwithzero():
    try:
        tree = tree_from_file(
            filename="./files/proj1_man_syntaxErr_intLiteralBeginWithZero.c",
            lexer_class=MyGrammarLexer,
            parser_class=MyGrammarParser
        )
    except Exception as e:
        pass
    else:
        assert False


def test_operators():
    try:
        tree = tree_from_file(
            filename="./files/proj1_man_syntaxErr_operators.c",
            lexer_class=MyGrammarLexer,
            parser_class=MyGrammarParser
        )
    except Exception as e:
        pass
    else:
        assert False
