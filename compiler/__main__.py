import argparse

from compiler.frontend import tree_from_file, tree_to_ast
from compiler.middleend import optimise_ast
from compiler.utils import ASTDotVisitor


def main():
    parser = argparse.ArgumentParser(description='Compiler options.')
    parser.add_argument('--input', required=True, help='The input file to compile')
    parser.add_argument('--render_ast', help='Render the AST of the input file.')
    parser.add_argument('--no-optimise', action = 'store_true', help='Dont optimise the ast if this flag is provided.')

    args = parser.parse_args()

    # frontend
    tree = tree_from_file(filename=args.input)
    ast = tree_to_ast(tree)

    # middle end
    if not args.no_optimise:
        ast = optimise_ast(ast)

    # Perform actions based on the command line arguments
    if args.render_ast:
        dot_visitor = ASTDotVisitor()
        dot_visitor.visit_ast(ast)
        dot_visitor.output(args.render_ast)


if __name__ == "__main__":
    main()
