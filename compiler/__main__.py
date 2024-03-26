import argparse
import subprocess

from compiler.frontend import tree_from_file, tree_to_ast
from compiler.frontend.symbol_table.symbol_table_visitor import SymbolTableVisitor
from compiler.frontend.symbol_table.symboltable import SymbolTable
from compiler.middleend import optimise_ast
from compiler.utils import AstDotVisitor
from compiler.utils.symboltabledotvisitor import SymbolTableDotVisitor


def main():
    parser = argparse.ArgumentParser(description='Compiler options.')
    parser.add_argument('--input', required=True, help='The input file to compile')
    parser.add_argument('--render_ast', help='Render the AST of the input file. Specify output folder.')
    parser.add_argument('--render_symb', help='Render the symbol table of the input file. Specify output folder.')
    parser.add_argument('--no-optimise', action='store_true', help='Dont optimise the ast if this flag is provided.')

    args = parser.parse_args()

    # frontend
    tree = tree_from_file(filename=args.input)
    ast = tree_to_ast(tree)

    symbol_table_visitor = SymbolTableVisitor(symbol_table=SymbolTable())
    symbol_table_visitor.visit_program(ast)

    # middle end
    if not args.no_optimise:
        ast = optimise_ast(ast)

    # Perform actions based on the command line arguments
    if args.render_ast:
        dot_visitor = AstDotVisitor()
        dot_visitor.visit_program(ast)
        folder = args.render_ast
        filename = str(args.input).split("/")[-1][:-2] + "_AST"
        dot_visitor.output(f"{folder}/{filename}.dot")
        command = f"dot -Tpng -o {folder}/{filename}.png {folder}/{filename}.dot"
        subprocess.run(command, shell=True, check=True)

    if args.render_symb:
        symbol_table_tree = symbol_table_visitor.symbol_table.global_scope
        dot_visitor = SymbolTableDotVisitor()
        dot_visitor.generate_dot(symbol_table_tree)
        folder = args.render_symb
        filename = str(args.input).split("/")[-1][:-2] + "_SymbTable.dot"
        dot_visitor.output(f"{folder}/{filename}")
        command = "dot -Tpng -o" + f"{folder}/{filename}" + ".png " + f"{folder}/{filename}"
        subprocess.run(command, shell=True, check=True)



if __name__ == "__main__":
    main()
