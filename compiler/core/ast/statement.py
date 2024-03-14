from dataclasses import dataclass

from .ast import AST
from .expression import Expression
from .type import Type


@dataclass
class Statement(AST):
    pass


@dataclass
class Program(Statement):
    statements: list[Statement]


@dataclass
class Body(Statement):
    statements: list[Statement]


@dataclass
class FunctionDeclaration(Statement):
    return_type: Type
    name: str
    body: Body


@dataclass
class VariableDeclarationQualifier(Statement):
    identifier: str
    initializer: Expression or None


@dataclass
class VariableDeclaration(Statement):
    var_type: Type
    qualifiers: list[VariableDeclarationQualifier]


@dataclass
class AssignmentStatement(Statement):
    identifier: str
    value: Expression
