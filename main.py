import antlr4
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarVisitor import GrammarVisitor  # Replace with your visitor, if you have one

def parse_input(input_stream):
    # Create a stream from the input
    lexer = GrammarLexer(input_stream)  # Make sure this matches the generated Lexer name
    stream = antlr4.CommonTokenStream(lexer)
    parser = GrammarParser(stream)  # Make sure this matches the generated Parser name
    
    # Parse the input and get the parse tree
    tree = parser.expression()  # This now correctly refers to the 'expression' rule

    # Print the tree (or process it further if you have a visitor)
    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    # Read from an input file or use a string
    # For file input, uncomment the following lines:
    # with open('your_input_file.txt', 'r') as file:
    #     input_stream = antlr4.InputStream(file.read())

    # For direct string input, uncomment this line:
    input_stream = antlr4.InputStream("1+1")

    parse_input(input_stream)
