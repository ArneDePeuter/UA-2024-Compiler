from dataclasses import dataclass

from .statement import Statement


@dataclass
class Program(Statement):
    statements: list[Statement]

