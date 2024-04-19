# [Compiler](https://petalite-vise-993.notion.site/Compilers-Project-719f132847644adfbb4a0ae85aa41fe5?pvs=74)

## Venv with poetry

- `pip install poetry`
- `poetry install --no-root`
- `poetry shell`

## How to Run the Program
**!You must have poetry env enabled!**
- To run the program, execute the following command: `python3 -m compiler`
- To run all the files in **./input** and output to **./output**: `python3 scripts/create_all_pass.py`

## How to run tests
**!You must have poetry env enabled!**
- Run command `pytest`
- Generate a report of the test coverage `pytest --cov-report html --cov=.`

## Command Line Flags

- `--input`: (**required**) Specifies the input file to compile.
- `--render_ast`: Renders the Abstract Syntax Tree (AST) of the input file. Specify the output folder
- `--render_symb`: Renders the Symbol table of the input file. Specify the output folder
- `--no-optimise`: If provided, the AST will not be optimized.
- `--target_llvm`: Output llvm target to specified output folder.

### Examples:

1. Compiling a file and rendering its AST: `python3 -m compiler --input <input_file> --render_ast <output_file>`
2. Compiling a file without optimizing its AST: `python3 -m compiler --input <input_file> --no-optimise`
3. Compiling a file and not rendering its AST: `python3 -m compiler --input <input_file>`

## Compiler features

### Project 1
- [X] Binary operations +, -, *, and /
- [X] Binary operations >, <, and ==
- [X] Unary operators + and -
- [X] Parenthesis to overwrite the order of operations
- [X] Logical operators &&, ||, and !
- [X] Comparison operators >=, <=, and !=
- [X] Binary operator %
- [X] Shift operators <<, >>
- [X] Bitwise operators &, |, ~, and ^
- [X] Constant folding

### Project 2
- [X] Main function declaration
- [X] const, char, int, float
- [X] Literals
- [X] Variables
- [X] Pointers
- [X] Constants
- [X] Implicit conversions
- [X] Explicit conversions
- [X] Pointer arithmetic
- [X] Increment/Decrement operations
- [X] Constant folding with conversions
- [X] Constant Propagation
- [X] Semantic Errors

### Project 3
- [X] Single line and multi line comments
- [X] Comments output to LLVM
- [X] C statement in LLVM output as comment
- [X] Printf
- [X] Typedef
- [X] LLVM code generation

### Project 4
- [X] Conditional statements: if and else.
- [X] Else if statements.
- [X] Loops: while, for, break, and continue.
- [X] Anonymous scopes
- [X] Switch, case, break, and default.
- [ ] Enumerations.
