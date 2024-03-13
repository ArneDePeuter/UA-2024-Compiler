# Compiler

## Overview

This document provides comprehensive instructions for using our custom compiler, designed to support various optimizations and target code generations for enhanced flexibility during development.

## Setup

### Prerequisites

- Java Runtime Environment (JRE) to run the ANTLR tool.
- Python 3 for running the compiler.

### Recompiling ANTLR Classes

To ensure that the ANTLR classes are up to date, recompile them with the following command:

```bash
java -jar ../../antlr-4.13.1-complete.jar -Dlanguage=Python3 MyGrammar.g4 -visitor
```

This step is crucial for reflecting any changes made to the grammar files.

## Compilation Options

The compiler supports multiple command-line arguments to customize its behavior based on your needs:

- `--input <file>`: (Required) Specifies the input file to compile.
- `--render_ast`: If set, renders the Abstract Syntax Tree (AST) of the input file.
- `--render_symb`: If set, renders the symbol table of the input file.
- `--target_llvm`: If set, generates LLVM code for the input file.
- `--target_mips`: If set, generates MIPS code for the input file.
- `--constant_folding`: If set, performs constant folding on the AST to optimize the code by evaluating constant expressions at compile time.

## Usage Examples

### Compiling a File

To compile an input file with the basic setup:

```bash
python -m src.main --input your_input_file.c
```

Replace `your_input_file.c` with the path to your actual input file.

### Applying Optimizations and Rendering

To compile a file, render its AST and symbol table, and apply constant folding optimization:

```bash
python -m src.main --input your_input_file.c --render_ast --render_symb --constant_folding
```

For further assistance or to report issues, please refer to our project's issue tracker or contact support.
