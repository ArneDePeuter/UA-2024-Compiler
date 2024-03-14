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


