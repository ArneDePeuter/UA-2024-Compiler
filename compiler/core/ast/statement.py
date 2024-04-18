from dataclasses import dataclass
from typing import Optional

from .ast import AST
from .expression import Expression, INT, CHAR, FLOAT
from .type import Type, AddressQualifier, BaseType


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

    def set_default_initializer(self, type: Type):
        if len(type.address_qualifiers) > 0:
            self.initializer = INT(value=0)
        elif type.base_type == BaseType.int:
            self.initializer = INT(value=0)
        elif type.base_type == BaseType.float:
            self.initializer = FLOAT(value=0.0)
        elif type.base_type == BaseType.char:
            self.initializer = CHAR(value='')


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
