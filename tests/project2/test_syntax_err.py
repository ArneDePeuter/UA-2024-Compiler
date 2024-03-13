import os
from src.parser.tree_creation import tree_from_file
from src.antlr_files.project_2.MyGrammarParser import MyGrammarParser
from src.antlr_files.project_2.MyGrammarLexer import MyGrammarLexer


def test_syntax_err() -> None:
    directory = os.fsencode("./files/syntaxerr")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        try:
            tree_from_file(
                filename=f"{directory.decode()}/{filename}",
                lexer_class=MyGrammarLexer,
                parser_class=MyGrammarParser
            )
        except Exception as e:
            ...
        else:
            assert False
