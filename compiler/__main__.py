import argparse
import subprocess
from colored import Fore, Back, Style

from compiler.frontend import tree_from_file, tree_to_ast
from compiler.frontend.symbol_table.symbol_table_visitor import SymbolTableVisitor
from compiler.frontend.symbol_table.symboltable import SymbolTable
from compiler.middleend import optimise_ast
from compiler.utils import AstDotVisitor
from compiler.utils.symboltabledotvisitor import SymbolTableDotVisitor
from compiler.backend.llvm_target.llvm_ir_generator import LLVMIRGenerator


def compile_file(input_file: str, render_ast: str = None, render_symb: str = None, no_optimise: bool = False, target_llvm: str = None):
    # frontend
    tree, input_stream = tree_from_file(filename=input_file)
    ast = tree_to_ast(tree, input_stream)

    symbol_table_visitor = SymbolTableVisitor(symbol_table=SymbolTable())
    symbol_table_visitor.visit_program(ast)

    # middle end
    if not no_optimise:
        ast = optimise_ast(ast)

    if target_llvm:
        # Generate LLVM IR
        llvm_ir_generator = LLVMIRGenerator()
        llvm_ir = llvm_ir_generator.generate_llvm_ir(ast)

        # Write LLVM IR to a file
        filename = str(input_file).split("/")[-1][:-2]
        output_file = f"{target_llvm}/{filename}.ll"
        with open(output_file, "w") as file:
            file.write(llvm_ir)

    # Perform actions based on the command line arguments
    if render_ast:
        dot_visitor = AstDotVisitor()
        dot_visitor.visit_program(ast)
        folder = render_ast
        filename = str(input_file).split("/")[-1][:-2] + "_AST"
        dot_visitor.output(f"{folder}/{filename}.dot")
        command = f"dot -Tpng -o {folder}/{filename}.png {folder}/{filename}.dot"
        subprocess.run(command, shell=True, check=True)

    if render_symb:
        symbol_table_tree = symbol_table_visitor.symbol_table.global_scope
        dot_visitor = SymbolTableDotVisitor()
        dot_visitor.generate_dot(symbol_table_tree)
        folder = render_symb
        filename = str(input_file).split("/")[-1][:-2] + "_SymbTable.dot"
        dot_visitor.output(f"{folder}/{filename}")
        command = "dot -Tpng -o" + f"{folder}/{filename}" + ".png " + f"{folder}/{filename}"
        subprocess.run(command, shell=True, check=True)


def main():
    parser = argparse.ArgumentParser(description='Compiler options.')
    parser.add_argument('--input', required=True, help='The input file to compile')
    parser.add_argument('--render_ast', help='Render the AST of the input file. Specify output folder.')
    parser.add_argument('--render_symb', help='Render the symbol table of the input file. Specify output folder.')
    parser.add_argument('--no-optimise', action='store_true', help='Dont optimise the ast if this flag is provided.')
    parser.add_argument('--target_llvm', help='LLvm Target. Specify output folder.')

    args = parser.parse_args()
    try:
        compile_file(args.input, args.render_ast, args.render_symb, args.no_optimise, args.target_llvm)
    except Exception as e:
        print(f"{Fore.red}{e}{Style.reset}")

if __name__ == "__main__":
    main()
