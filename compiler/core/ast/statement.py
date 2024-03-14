from dataclasses import dataclass

from .ast import AST
from .expression import Expression
from .type import Type


@dataclass
class Statement(AST):
    pass


class Body(Statement):
    statements: list[Statement]


@dataclass
class FunctionDeclaration(Statement):
    return_type: Type
    name: str
    body: Body


@dataclass
class VariableDeclaration(Statement):
    var_type: Type
    identifier: str
    initializer: Expression or None


@dataclass
class AssignmentStatement(Statement):
    identifier: str
    value: Expression
