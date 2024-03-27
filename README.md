# Compiler

## How to Run the Program

To run the program, execute the following command: `python3 -m compiler`

## Command Line Flags

- `--input`: (**required**) Specifies the input file to compile.
- `--render_ast`: Renders the Abstract Syntax Tree (AST) of the input file.
- `--no-optimise`: If provided, the AST will not be optimized.

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
- [ ] Semantic Errors

### Project 3
- [X] Single line and multi line comments
- [ ] Comments output to LLVM
- [ ] C statement in LLVM output as comment
- [X] Printf
- [X] Typedef
- [ ] LLVM code generation
