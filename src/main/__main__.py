import argparse
import os
import subprocess

from src.parser.cst_visitor import CSTVisitor
from src.parser.ast_visitor.dotvisitor import DotVisitor
from src.parser.tree_creation import tree_from_file
from src.antlr_files.project_2.MyGrammarLexer import MyGrammarLexer
from src.antlr_files.project_2.MyGrammarParser import MyGrammarParser
from src.parser.ast_visitor.optimizervisitor import OptimizerVisitor
from src.parser.ast_visitor.symboltablevisitor import SymbolTableVisitor
#from src.parser.ast_visitor.llvmvisitor import LLVMVisitor
#from src.parser.ast_visitor.mipsvisitor import MIPSVisitor


def main():
    parser = argparse.ArgumentParser(description='Compiler options.')
    parser.add_argument('--input', required=True, help='The input file to compile')
    parser.add_argument('--render_ast', action='store_true', help='Render the AST of the input file.')
    parser.add_argument('--render_symb', action='store_true', help='Render the symbol table of the input file.')
    parser.add_argument('--target_llvm', action='store_true', help='Generate LLVM code for the input file.')
    parser.add_argument('--target_mips', action='store_true', help='Generate MIPS code for the input file.')

    args = parser.parse_args()

    tree = tree_from_file(
        filename=args.input,
        lexer_class=MyGrammarLexer,
        parser_class=MyGrammarParser
    )

    cst_visitor = CSTVisitor()
    ast = cst_visitor.visit(tree)

    optimizer_visitor = OptimizerVisitor()
    ast = optimizer_visitor.visit_ast(ast)

    symbol_table_visitor = SymbolTableVisitor()
    symbol_table_visitor.visit_ast(ast)
    symbol_table_tree = symbol_table_visitor.get_symbol_table_tree()

    # Perform actions based on the command line arguments
    if args.render_ast:
        dot_visitor = DotVisitor()
        dot_visitor.visit_ast(ast)
        base_filename = os.path.splitext(os.path.basename(args.input))[0]
        dotfile = "temp/ast_output_"+base_filename
        dot_visitor.output(dotfile + ".dot")

        output_png = dotfile.replace(".dot", ".png")  # Construct the output PNG filename
        command = ["dot", "-Tpng", f"-o{output_png}", dotfile]
        subprocess.run(command, check=True)

    if args.render_symb:
        dot_visitor = DotVisitor()
        dot_visitor.visit_symbol_table(symbol_table_tree)
        base_filename = os.path.splitext(os.path.basename(args.input))[0]
        file_name = "temp/symb_output_"+base_filename
        dot_visitor.output(file_name + ".dot")

        command = "dot -Tpng -o"+file_name+".png "+file_name+".dot"
        subprocess.run(command, shell=True, check=True)

    if args.target_llvm:
        pass
    if args.target_mips:
        pass


if __name__ == "__main__":
    main()