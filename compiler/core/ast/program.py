from dataclasses import dataclass
from .ast import AST
from .expression import Expression


@dataclass
class Program(AST):
    expressions: list[Expression]
