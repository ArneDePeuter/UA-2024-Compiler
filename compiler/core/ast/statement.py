from dataclasses import dataclass
from typing import Optional

from .ast import AST
from .expression import Expression
from .type import Type, AddressQualifier


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
class ExpressionStatement(Statement):
    expression: Expression


@dataclass
class AssignmentStatement(Statement):
    identifier: str
    value: Expression
    address_qualifiers: Optional[list[AddressQualifier]] = None

    def __post_init__(self):
        if self.address_qualifiers is None:
            self.address_qualifiers = []


@dataclass
class CommentStatement(Statement):
    content: str
