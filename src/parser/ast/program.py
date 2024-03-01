from dataclasses import dataclass

from .ast import AST
from .statement import Statement


@dataclass
class Program(AST):
    statements: list[Statement]
