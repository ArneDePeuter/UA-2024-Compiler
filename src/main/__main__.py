import argparse

from src.parser.cst_visitor import CSTVisitor
from src.parser.ast_visitor.dotvisitor import DotVisitor
from src.parser.tree_creation import tree_from_file
from src.antlr_files.project_2.MyGrammarLexer import MyGrammarLexer
from src.antlr_files.project_2.MyGrammarParser import MyGrammarParser
from src.parser.ast_visitor.optimizervisitor import OptimizerVisitor
from src.parser.ast_visitor.astprintvisitor import ASTPrintVisitor


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--input', dest="filename", help='the input file to compile')
    parser.add_argument('--render_ast', dest="render_ast", help='the input file to compile')
    parser.add_argument('--render_symb', dest="render_symb", help='the input file to compile')
    parser.add_argument('--target_llvm', dest="target_llvm", help='the input file to compile')
    parser.add_argument('--target_mips', dest="target_mips", help='the input file to compile')

    args = parser.parse_args()
    if not args.filename:
        raise RuntimeError("You didn't specify a file to compile")

    tree = tree_from_file(
        filename=args.filename,
        lexer_class=MyGrammarLexer,
        parser_class=MyGrammarParser
    )

    cst_visitor = CSTVisitor()
    ast = cst_visitor.visit(tree)

    optimizer_visitor = OptimizerVisitor()
    ast = optimizer_visitor.visit_ast(ast)

    #ast_print_visitor = ASTPrintVisitor()
    #ast_print_visitor.visit_ast(ast)

    dot_visitor = DotVisitor()
    dot_visitor.visit_ast(ast)
    dotfile = "temp/ast_proj1"
    dot_visitor.output(dotfile+".dot")


if __name__ == "__main__":
    main()
