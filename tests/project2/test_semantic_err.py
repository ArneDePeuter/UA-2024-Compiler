import os
from src.parser.tree_creation import tree_from_file
from src.antlr_files.project_2.MyGrammarParser import MyGrammarParser
from src.antlr_files.project_2.MyGrammarLexer import MyGrammarLexer
from src.parser.ast_visitor.symboltablevisitor import SymbolTableVisitor
from src.parser.cst_visitor import CSTVisitor
from src.parser.ast_visitor.optimizervisitor import OptimizerVisitor


def test_semantic_err() -> None:
    directory = os.fsencode("./files/semanticerr")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        tree = tree_from_file(
            filename=f"{directory.decode()}/{filename}",
            lexer_class=MyGrammarLexer,
            parser_class=MyGrammarParser
        )

        ast = CSTVisitor().visit(tree)
        ast = OptimizerVisitor().visit_ast(ast)

        try:
            symbol_table_visitor = SymbolTableVisitor()
            symbol_table_visitor.visit_ast(ast)
            symbol_table_tree = symbol_table_visitor.get_symbol_table_tree()
        except Exception as e:
            ...
        else:
            assert False
