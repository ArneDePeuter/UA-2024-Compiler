from dataclasses import dataclass
from .statement import Statement

@dataclass
class CompoundStatement(Statement):
    statements: list[Statement]