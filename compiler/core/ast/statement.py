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
    left: Expression
    right: Expression


@dataclass
class CommentStatement(Statement):
    content: str


@dataclass
class WhileStatement(Statement):
    expression: Expression
    to_execute: Statement

    def __post_init__(self):
        if not isinstance(self.to_execute, Body):
            stmts = [self.to_execute]
        else:
            stmts = self.to_execute.statements
        for stmt in stmts:
            if isinstance(stmt, BreakStatement):
                stmt.while_statement = self
            elif isinstance(stmt, ContinueStatement):
                stmt.while_statement = self


@dataclass
class BreakStatement(Statement):
    while_statement: Optional[WhileStatement] = None


@dataclass
class ContinueStatement(Statement):
    while_statement: Optional[WhileStatement] = None
