import os
import pytest
from compiler.frontend import tree_from_file, tree_to_ast
from compiler.middleend import optimise_ast
from compiler.backend.llvm_target.llvm_ir_generator import LLVMIRGenerator

TEST_FILES_DIR = "files"
OUTPUT_DIR = "output"

def test_pass_llvm():
    # Check if output directory exists, if not create it
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Counter for passed and failed tests
    passed = 0
    failed = 0

    # Iterate over each .c file in the test files directory that contains "man_pass" in the filename
    for file in os.listdir(TEST_FILES_DIR):
        if "man_pass" in file and file.endswith(".c"):
            file_path = os.path.join(TEST_FILES_DIR, file)
            filename, _ = os.path.splitext(file)

            try:
                # Frontend: Construct CST and AST
                tree, input_stream = tree_from_file(filename=file_path)
                ast = tree_to_ast(tree, input_stream)

                # Middle End: Optimize AST
                # ast = optimise_ast(ast)

                # Backend: Generate LLVM IR
                llvm_ir_generator = LLVMIRGenerator()
                llvm_ir = llvm_ir_generator.generate_llvm_ir(ast)

                # Write LLVM IR to a file
                output_file = f"{OUTPUT_DIR}/{filename}.ll"
                with open(output_file, "w") as file:
                    file.write(llvm_ir)

                print(f"Test case {filename} passed.")
                passed += 1
            except Exception as e:
                output_file = os.path.join(OUTPUT_DIR, f"{filename}_compile_output.txt")
                with open(output_file, "w") as f:
                    f.write(str(e))
                print(f"Test case {filename} failed. Check {output_file} for details.")
                failed += 1

    # Summary
    print(f"Total passed: {passed}")
    print(f"Total failed: {failed}")

    # Assert that there are no failed tests
    assert failed == 0, f"{failed} test(s) failed"