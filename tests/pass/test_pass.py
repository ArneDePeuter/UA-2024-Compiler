import os
import pytest

from compiler.frontend import tree_from_file, tree_to_ast
from compiler.frontend.symbol_table.symbol_table_visitor import SymbolTableVisitor, SymbolTable
from compiler.middleend import optimise_ast
from compiler.backend.llvm_target.llvm_ir_generator import LLVMIRGenerator


@pytest.mark.parametrize("input_file", os.listdir("./tests/pass/files"))
def test_pass(input_file) -> None:
    tree, input_stream = tree_from_file(f"./files/{input_file}")
    ast = tree_to_ast(tree, input_stream)

    ast = optimise_ast(ast)

    symbol_table_visitor = SymbolTableVisitor(symbol_table=SymbolTable())
    symbol_table_visitor.visit(ast)

    llvm_ir_generator = LLVMIRGenerator()
    llvm_ir = llvm_ir_generator.generate_llvm_ir(ast)
