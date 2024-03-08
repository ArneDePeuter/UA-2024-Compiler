from dataclasses import dataclass
from .ast import AST
from .expression import Expression

@dataclass
class Variable(AST):
    identifier: str
    initializer: Expression or None