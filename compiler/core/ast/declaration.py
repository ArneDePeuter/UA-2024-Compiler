from dataclasses import dataclass
from .statement import Statement
from .type import Type
from .variable import Variable

@dataclass
class Declaration(Statement):
    var_type: Type
    variables: list[Variable]