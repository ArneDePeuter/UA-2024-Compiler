import argparse
import subprocess
from colored import Fore, Back, Style

from compiler.frontend import tree_from_str, tree_to_ast
from compiler.frontend.symbol_table.symbol_table_visitor import SymbolTableVisitor
from compiler.frontend.symbol_table.symboltable import SymbolTable
from compiler.middleend import optimise_ast
from compiler.utils import AstDotVisitor
from compiler.utils.symboltabledotvisitor import SymbolTableDotVisitor
from compiler.backend.llvm_target.llvm_ir_generator import LLVMIRGenerator
from compiler.backend.mips_target.mips_generator import MIPSGenerator
from compiler.core.errors.semantic_error import SemanticError
from compiler.core.errors.compiler_syntaxerror import CompilerSyntaxError
from compiler.preprocessor.preprocessor import Preprocessor


def compile_file(input_file: str,
                 render_ast: str = None,
                 render_symb: str = None,
                 no_optimise: bool = False,
                 target_llvm: str = None,
                 target_mips: str = None,
                 include_paths=None,):

    # preprocessor
    with open(input_file, 'r', encoding='utf-8') as file:
        input_code = file.read()

    preprocessor = Preprocessor()
    preprocessed_code = preprocessor.preprocess(input_code, include_paths)


    # frontend
    tree, input_stream = tree_from_str(preprocessed_code)
    ast = tree_to_ast(tree, input_stream)

    symbol_table_visitor = SymbolTableVisitor(stdio_included=preprocessor.stdio_included, symbol_table=SymbolTable())
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

    if target_mips:
        # Generate MIPS code
        mips_generator = MIPSGenerator()
        mips_code = mips_generator.generate_mips(ast)

        # Write MIPS code to a file
        filename = str(input_file).split("/")[-1][:-2]
        output_file = f"{target_mips}/{filename}.s"
        with open(output_file, "w", encoding='utf-8') as file:
            file.write(mips_code)

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


def generate_cool_error(e: SemanticError|CompilerSyntaxError, filename: str):
    print(f"{Fore.red}{e}{Style.reset}")
    with open(filename, "r") as file:
        lines = file.readlines()
        if e.line > 0:
            print(f"{Fore.red}{e.line - 1}| {lines[e.line - 2]}{Style.reset}", end="")
        print(f"{Fore.red}{e.line}| {lines[e.line - 1]}{Style.reset}", end="")
        offset = len(str(e.line)) + len("| ")
        print(f"{Fore.red}{'-' * (e.position + offset)}^{Style.reset}")
        if e.line < len(lines):
            print(f"{Fore.red}{e.line + 1}| {lines[e.line]}{Style.reset}")


def main():
    parser = argparse.ArgumentParser(description='Compiler options.')
    parser.add_argument('--input', required=True, help='The input file to compile')
    parser.add_argument('--render_ast', help='Render the AST of the input file. Specify output folder.')
    parser.add_argument('--render_symb', help='Render the symbol table of the input file. Specify output folder.')
    parser.add_argument('--no-optimise', action='store_true', help='Dont optimise the ast if this flag is provided.')
    parser.add_argument('--target_llvm', help='LLvm Target. Specify output folder.')
    parser.add_argument('--target_mips', help='MIPS Target. Specify output folder.')
    parser.add_argument('--throw', action='store_true', help='Raise python exception.')
    parser.add_argument('--include_paths', nargs='*', help='Include paths for the pre-processor')

    args = parser.parse_args()
    try:
        include_paths = args.include_paths or []
        compile_file(args.input, args.render_ast, args.render_symb, args.no_optimise, args.target_llvm, args.target_mips, include_paths)
    except SemanticError as e:
        if args.throw:
            raise e
        generate_cool_error(e, args.input)
    except CompilerSyntaxError as e:
        if args.throw:
            raise e
        generate_cool_error(e, args.input)
    except Exception as e:
        if args.throw:
            raise e
        print(f"{Fore.red}{e}{Style.reset}")


if __name__ == "__main__":
    main()