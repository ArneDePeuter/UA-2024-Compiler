import antlr4
from src.antlr_files.GrammarLexer import GrammarLexer
from src.antlr_files.GrammarParser import GrammarParser
from src.parser.CustomAstVisitor import CustomAstVisitor  # This will be your custom visitor for AST construction
import argparse

def print_ast(node, level=0):
    if node is None:
        return
    # Indent to show tree structure
    indent = ' ' * (level * 2)
    print(f"{indent}{type(node).__name__}: {node}")
    # If the node has children or attributes that are AST nodes, print them as well
    if hasattr(node, 'left'):
        print_ast(node.left, level + 1)
    if hasattr(node, 'right'):
        print_ast(node.right, level + 1)
    if hasattr(node, 'operand'):  # For unary operations
        print_ast(node.operand, level + 1)

def main():
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

    lexer = GrammarLexer(input_stream)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = GrammarParser(token_stream)
    
    tree = parser.expression()  # Adjust if different
    
    visitor = CustomAstVisitor()
    ast = visitor.visit(tree)
    
    if ast:
        print("AST generated:")
        print_ast(ast)
    else:
        print("No AST generated.")

if __name__ == "__main__":
    main()
