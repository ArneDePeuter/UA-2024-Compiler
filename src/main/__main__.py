import antlr4
from src.antlr_files.GrammarLexer import GrammarLexer
from src.antlr_files.GrammarParser import GrammarParser
import argparse


def parse_input(input_stream: antlr4.InputStream) -> None:
    # Create a stream from the input
    lexer = GrammarLexer(input_stream)  # Make sure this matches the generated Lexer name
    stream = antlr4.CommonTokenStream(lexer)
    parser = GrammarParser(stream)  # Make sure this matches the generated Parser name

    # Parse the input and get the parse tree
    tree = parser.expression()  # This now correctly refers to the 'expression' rule

    # Print the tree (or process it further if you have a visitor)
    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--input', dest="filename", help='the input file to compile')
    parser.add_argument('--render_ast', dest="render_ast", help='the input file to compile')
    parser.add_argument('--render_symb', dest="render_symb", help='the input file to compile')
    parser.add_argument('--target_llvm', dest="target_llvm", help='the input file to compile')
    parser.add_argument('--target_mips', dest="target_mips", help='the input file to compile')

    args = parser.parse_args()
    if not args.filename:
        raise RuntimeError("You didn't specify a file to compile")

    with open(args.filename, 'r') as file:
        input_stream = antlr4.InputStream(file.read())

    parse_input(input_stream)
