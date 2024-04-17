from dataclasses import dataclass
from typing import Optional, Union

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
    left: Expression
    right: Expression


@dataclass
class CommentStatement(Statement):
    content: str

@dataclass
class ElseStatement(Statement):
    body: Body

@dataclass
class IfStatement(Statement):
    condition: Expression
    body: Body
    else_statement: ElseStatement or None