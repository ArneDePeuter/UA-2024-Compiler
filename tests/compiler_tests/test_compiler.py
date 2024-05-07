import pytest
import os
import subprocess
from compiler.__main__ import compile_file


def run_my_compiler(input_file, include_paths):
    compile_file(input_file, no_optimise=True, target_llvm=".", include_paths=include_paths)


def run_lli():
    command = ["lli", "test.ll"]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout


def run_clang(input_file, include_paths):
    output_file = "temp.out"
    command = ["clang", "-o", output_file]
    for path in include_paths:
        command.extend(["-I", path])
    command.append(input_file)
    subprocess.run(command, check=True)
    command = ["./" + output_file]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    os.remove(output_file)
    return result.stdout


@pytest.mark.parametrize("input_file", os.listdir("./tests/compiler_tests/files"))
def test_compiler(input_file):
    input_file = os.path.join("./tests/compiler_tests/files", input_file)
    include_paths = ["./tests/compiler_tests/includes"]  # Add the include paths here
    run_my_compiler(input_file, include_paths)
    my_output = run_lli()
    os.remove("test.ll")
    clang_output = run_clang(input_file, include_paths)
    assert my_output == clang_output