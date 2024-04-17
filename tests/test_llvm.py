import os
import pytest
from compiler.frontend import tree_from_file, tree_to_ast
from compiler.middleend import optimise_ast
from compiler.backend.llvm_target.llvm_ir_generator import LLVMIRGenerator

def test_pass_llvm():
    for file in os.listdir("./files"):
        if "man_pass" in file and file.endswith(".c"):
            print(f"TESTING: {file}")
            file_path = os.path.join("./files", file)
            filename, _ = os.path.splitext(file)

            tree, input_stream = tree_from_file(filename=file_path)
            ast = tree_to_ast(tree, input_stream)

            ast = optimise_ast(ast)

            llvm_ir_generator = LLVMIRGenerator()
            llvm_ir_generator.generate_llvm_ir(ast)

            print(f"PASSED: {file}")
