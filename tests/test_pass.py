import os

from compiler.frontend import tree_from_file, tree_to_ast
from compiler.frontend.symbol_table.symbol_table_visitor import SymbolTableVisitor, SymbolTable
from compiler.backend.llvm_target.llvm_ir_generator import LLVMIRGenerator


def test_pass() -> None:
    directory = os.fsencode("./files")
    for file in os.listdir(directory):
        file_str = file.decode("utf-8")
        str_list = file_str.split("_")
        if (str_list[2] != "pass"):
            continue

        filename = os.fsdecode(file)
        print(f"Testing {filename}")

        tree, input_stream = tree_from_file(f"{directory.decode()}/{filename}")
        ast = tree_to_ast(tree, input_stream)

        symbol_table_visitor = SymbolTableVisitor(symbol_table=SymbolTable())
        symbol_table_visitor.visit(ast)

        llvm_ir_generator = LLVMIRGenerator()
        # llvm_ir = llvm_ir_generator.generate_llvm_ir(ast)
