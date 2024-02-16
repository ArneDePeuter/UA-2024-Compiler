class AstNode:
    def print_ast(self, level=0):
        raise NotImplementedError("Subclass must implement abstract method")

class BinaryOpNode(AstNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def print_ast(self, level=0):
        print('  ' * level + f'BinaryOp: {self.op}')
        self.left.print_ast(level + 1)
        self.right.print_ast(level + 1)

class UnaryOpNode(AstNode):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def print_ast(self, level=0):
        print('  ' * level + f'UnaryOp: {self.op}')
        self.operand.print_ast(level + 1)

class NumberNode(AstNode):
    def __init__(self, value):
        self.value = value

    def print_ast(self, level=0):
        print('  ' * level + f'Number: {self.value}')
