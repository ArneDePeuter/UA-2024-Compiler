from .ast import AST
from .statement import Statement

class Program(AST):
    def __init__(self, statements: list[Statement]) -> None:
        self.statements = statements

