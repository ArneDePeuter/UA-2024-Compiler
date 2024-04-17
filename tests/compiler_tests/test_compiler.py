import pytest
import os
import subprocess
from compiler.__main__ import compile_file


def run_my_compiler(input_file):
    with open(input_file, "r") as file:
        code = file.read()
        with open("test.c", "w") as file:
            code = code.replace("#include <stdio.h>", "")
            file.write(code)
    compile_file("test.c", target_llvm=".")
    os.remove("test.c")


def run_lli():
    command = ["lli", "test.ll"]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout


def run_clang(input_file):
    output_file = "temp.out"
    command = ["clang", "-o", output_file, input_file]
    subprocess.run(command, check=True)
    command = ["./" + output_file]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    os.remove(output_file)
    return result.stdout


@pytest.mark.parametrize("input_file", os.listdir("./tests/compiler_tests/files"))
def test_compiler(input_file):
    input_file = os.path.join("./files", input_file)
    run_my_compiler(input_file)
    my_output = run_lli()
    os.remove("test.ll")
    clang_output = run_clang(input_file)
    assert my_output == clang_output


