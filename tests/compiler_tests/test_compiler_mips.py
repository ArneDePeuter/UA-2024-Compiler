import re

import pytest
import os
import subprocess
from compiler.__main__ import compile_file

def run_my_compiler(input_file, include_paths):
    try:
        compile_file(input_file, no_optimise=True, target_mips=".", include_paths=include_paths)
    except Exception as e:
        return e
    mips_file = input_file[:-1] + "s"  # Assuming the MIPS assembly file extension is .s
    mips_file = mips_file.replace("./files", ".")
    my_output = run_mars(mips_file)
    os.remove(mips_file)
    return my_output

def run_mars(file: str):
    command = ["java", "-jar", "Mars4_5.jar", "nc", "sm", file]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    output_lines = result.stdout.splitlines()
    # Normalize the output format
    normalized_output = []
    for line in output_lines:
        line = line.strip()
        import re
        # Check if the line contains a hexadecimal number prefixed with '0x'
        if re.search(r'0x[0-9a-fA-F]+', line):
            # Find all hexadecimal numbers in the line and convert them
            line = re.sub(r'0x([0-9a-fA-F]+)', lambda x: hex(int(x.group(1), 16))[2:], line)

        # Check if the line contains a floating-point number
        float_match = re.search(r'([+-]?\d*\.\d+([eE][+-]?\d+)?)', line)
        if float_match:
            # Extract the float value and format it to 6 decimal places
            float_value = float(float_match.group(1))
            formatted_float = f"{float_value:.6f}"
            line = line.replace(float_match.group(1), formatted_float)

        normalized_output.append(line)

    # Join lines and strip leading/trailing whitespace
    return "\n".join(normalized_output)

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


def normalize_float_string(float_str):
    """Normalize the floating point string by removing trailing zeroes and optional decimal point."""
    # Use regex to match floats and normalize them
    def normalize(match):
        s = match.group(0)
        return s.rstrip('0').rstrip('.') if '.' in s else s

    # Apply the regex substitution to the whole string
    normalized_str = re.sub(r'\d+\.\d+', normalize, float_str)
    return normalized_str


@pytest.mark.parametrize("input_file", os.listdir("./tests/compiler_tests/files"))
def test_compiler(input_file):
    if re.findall(r"struct_explicit_constructing.c", input_file):
        return
    include_paths = ["./includes"]  # Add the include paths here
    relative = os.path.join("./files", input_file)

    my_output = run_my_compiler(relative, include_paths)
    clang_output = run_clang(relative, include_paths)

    normalized_my_output = normalize_float_string(my_output)
    normalized_clang_output = normalize_float_string(clang_output)

    assert normalized_my_output == normalized_clang_output
