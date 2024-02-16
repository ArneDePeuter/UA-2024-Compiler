import antlr4
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from CustomAstVisitor import CustomAstVisitor  # This will be your custom visitor for AST construction

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
    input_string = "5*(3/10 + 9/10);"  
    input_stream = antlr4.InputStream(input_string)
    
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
