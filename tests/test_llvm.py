import os

from compiler.frontend import tree_from_file, tree_to_ast
from compiler.frontend.symbol_table.symbol_table_visitor import SymbolTableVisitor, SymbolTable
from compiler.backend.llvm_target.llvm_ir_generator import LLVMIRGenerator


def test_pass_llvm() -> None:
    directory = os.fsencode("./files")
    for file in os.listdir(directory):
        file_str = file.decode("utf-8")
        str_list = file_str.split("_")
        if (str_list[2] != "pass"):
            continue

        filename = os.fsdecode(file)
        print(f"LLVM: Testing {filename}")

        tree, input_stream = tree_from_file(f"{directory.decode()}/{filename}")
        ast = tree_to_ast(tree, input_stream)

        symbol_table_visitor = SymbolTableVisitor(symbol_table=SymbolTable())
        symbol_table_visitor.visit(ast)

        try:
            expected_llvm_ir_dir = os.fsencode(f"./llvm_expected")

            with open(f"{expected_llvm_ir_dir.decode()}/{filename[:-2]}.ll", "r") as file:

                llvm_ir_generator = LLVMIRGenerator()
                generated_llvm_ir = llvm_ir_generator.generate_llvm_ir(ast)

                expected_llvm_ir = file.read()
                assert generated_llvm_ir == expected_llvm_ir
        except FileNotFoundError:
            print((f"{filename} yet to be implemented"))
        else:
            print((f"{filename} yet to be implemented"))