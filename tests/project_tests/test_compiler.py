import pytest
import os
import subprocess
from compiler.__main__ import compile_file


def run_my_compiler(input_file, include_paths):
    compile_file(input_file, no_optimise=True, target_llvm=".", include_paths=include_paths)
    ll_file = input_file[:-1] + "ll"
    ll_file = ll_file.replace("./files", ".")
    my_output = run_lli(ll_file)
    os.remove(ll_file)
    return my_output


def run_lli(file: str):
    command = ["lli", file]
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


@pytest.mark.parametrize("input_file", os.listdir("./tests/project_tests/files"))
def test_compiler(input_file):
    include_paths = ["./includes"]  # Add the include paths here
    relative = os.path.join("./files", input_file)

    my_output = run_my_compiler(relative, include_paths)
    clang_output = run_clang(relative, include_paths)

    assert my_output == clang_output