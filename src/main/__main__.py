import argparse

from src.parser.visitor.concretevisitor import ConcreteVisitor as CustomASTVisitor
from src.parser.visitor.dotvisitor import DotVisitor
from src.parser.tree_creation import tree_from_file


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

    tree = tree_from_file(filename=args.filename)
    
    visitor = CustomASTVisitor()
    ast = visitor.visit(tree)

    if ast:
        print("AST generated:")
        dot_visitor = DotVisitor()
        dot_visitor.visit_ast(ast)
        dotfile = "temp/ast_proj1"
        dot_visitor.output(dotfile+".dot")
    else:
        print("No AST generated.")


if __name__ == "__main__":
    main()
