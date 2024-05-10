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
- Generate a report of the test coverage `pytest --cov-report html --cov=./compiler`

## Command Line Flags

| Flag            | Description                                                                          |
|-----------------|--------------------------------------------------------------------------------------|
| `--input`       | **Required.** Specifies the input file to compile.                                   |
| `--render_ast`  | Renders the Abstract Syntax Tree (AST) of the input file. Specify the output folder. |
| `--render_symb` | Renders the Symbol Table of the input file. Specify the output folder.               |
| `--no-optimise` | Disables AST optimization.                                                           |
| `--target_llvm` | Outputs LLVM target code to the specified folder.                                    |

### Examples:

1. Compiling a file and rendering its AST: `python3 -m compiler --input <input_file> --render_ast <output_file>`
2. Compiling a file without optimizing its AST: `python3 -m compiler --input <input_file> --no-optimise`
3. Compiling a file and not rendering its AST: `python3 -m compiler --input <input_file>`

## Compiler features

### Project 1
- [X] Binary operations: +, -, *, and /.
- [X] Binary operations: >, <, and ==.
- [X] Unary operators: + and -.
- [X] Order of operations: Parenthesis to overwrite the order of operations. Logical operators &&, ||, and !.
- [X] Comparison operators: >=, <=, and !=.
- [X] Binary operator: %.
- [X] Shift operators: <<, >>.
- [X] Bitwise operators: &, |, ~, and ^.
- [X] Abstract syntax tree and visualisation
- [X] Constant folding: (e.g., a sub-tree of the AST “3+4” gets replaced by a single node “7”)

### Project 2
- [X] Main function: Add an `int main() { ... }` function.
- [X] Reserved keywords: const, char, int, and float.
- [X] Literals: float, integer, character (scientific notation not necessary).
- [X] Variable handling: declarations, definitions, assignments, identifiers in expressions.
- [X] Pointers: declaration, definition, operators * (dereference) and & (address).
- [X] Const variables. For pointers, only “pointer to const” needs to be supported. The type is const int*. This means the value pointed to is const. The variable itself can be re-assigned with a different address.
- [X] Implicit conversions. We consider the order float isRicherThan int isRicherThan char. Pay attention to warnings.
- [X] Explicit conversions (i.e., the cast operator). Any conversion done this way should not cause a warning.
- [X] Pointer arithmetic (all of the following need to be implemented):
  * [X] Assignment: p = 0,
  * [X] Addition and subtraction: p + q, p + 2, q - 5, etc. Take the size of the datatype into account!
  * [X] Increment, decrement: p++, q--, etc.
  * [X] Comparison: p < end,p >= 0,p == 0,etc. 
  - Note that this is only relevant for arrays.
- [X] Increment/Decrement Operations: i++, i--. Both suﬀix and prefix variants.
- [X] Constant propagation.
- [X] Syntax errors
- [X] Semantic error: Use of undeclared var
- [X] Semantic error: Redeclaration of an undeclared var
- [X] Semantic error: Operations or assignments of incompatible types
- [X] Semantic error: Assignment to an rvalue
- [X] Semantic error: Assignment to a const variable
- [X] Symbol table and visualisation
- Optional
  - [X] Const casting: make it possible to have a non-const pointer to a const value

### Project 3
- [X] Comments: Store comments in the AST, and add them to LLVM IR and MIPS code at the appropriate line.
- [X] Comments: Add the original C-code as a comment in the LLVM IR and MIPS code.
- [X] Typedefs
- Note: the PDF for assignment 3 mentions a printf function. This is temporary, however, and
should not be present in the final version of the compiler.
- Note: This is graded separately for MIPS and LLVM IR.

### Project 4
- [X] Conditional statements: if and else must be supported. You can assume that curly braces are required.
- [X] Loops. You have to implement while, for, break, and continue.
- [X] Scopes: anonymous, if-else, for, while.
- [X] Switch statements: switch, break, case.
- [X] Your compiler should support enumerations.
- [X] Support scopes in symbol table, semantic analysis, constant propagation
- Optional
  - [X] else if statements.

### Project 5
- [X] Function scopes.
- [X] Local and global variables.
- [X] Functions: definitions; declarations; calling, recursive calls; parameters (const, float, int, pointers); returns; void functions;
- [X] Pre-processor: #define. Parameters do not need to be supported.
- [X] Pre-processor: #include.
- [X] Semantic analysis: Functions and their scopes in the symbol table
- [X] Semantic analysis: Consistency of return type.
- [X] Semantic analysis: Parameter types passed to call should be consistent with the function signature.
- [X] Semantic analysis: Consistency between forward declarations and function definitions. Functions must be declared/defined before calling them. Functions should not be re-defined. 
- [X] Optimisations (1pt): no code after break, continue, or return. (llvm wise)
- Optional
  - [ ] Overloading of functions on the amount and types of the parameters.
  - [ ] Prevent headers from being included twice by implementing include guards.
  - [ ] Semantic analysis: Check for all paths in a function body whether a return statement is present. 
  - [ ] Optimisation: Do not generate code for unused variables
  - [ ] Optimisation: Do not generate code for conditions that are always false.

### Project 6
- [X] Arrays: simple one dimensional arrays
- [X] Arrays: multi-dimensional arrays.
- [X] Arrays: assignment of complete arrays or array rows in case of multi-dimensional arrays. 
- [X] Arrays: array initialisation: int arr[3] = {1,2,3}.
- [X] Arrays: Operations on array elements.
- [X] Strings encoded as zero-terminated char-arrays. String literals. Passing strings around as char*. Support for IO: printf and scanf that support char* strings. 
- [X] The header stdio.h is treated as a special instruction that makes printf and scanf available. Including the actual stdio.h header is not necessary.
- [X] Semantic analysis: Type checking for array types (parameter passing, assignment, indexing). 
- [X] Semantic analysis: Checking the length of array initialisers ({ ... }) during assignment.
- Optional
  - [ ] Dynamic arrays (stored on the heap).

### Project 7
- [X] User-defined structs. The structs should support members with primitive fields, arrays, enum types, as well as pointer types. You do not have to support default values for the struct members. 
- [X] Semantic analysis: Type checking for accessing and assigning struct members.
- [ ] Semantic analysis: Type checking for accessing and assigning union members (if implemented). 
- [ ] Semantic analysis: Type checking for function pointers: assigning function pointers, calling functions, etc. (if implemented)
- Optional
  - [X] Structs that contain other structs as a value.
  - [ ] Dynamic allocation of structs (stored on the heap). 
  - [ ] Unions.
  - [ ] Function pointers. All the checks and errors that apply to ordinary pointers should also be implemented for function pointers.
  - [ ] File reading using fgets. You can implement file pointers (FILE*) together with fopen and fclose, but this is not required. You may also just pass filenames to fgets.
  - [ ] File writing using fputs. You can implement file pointers (FILE*) together with fopen and fclose, but this is not required. You may also just pass filenames to fputs.
    - [ ] Dynamically allocated strings and character buffers. These can work in combination with printf, fgets, fputs, etc.
