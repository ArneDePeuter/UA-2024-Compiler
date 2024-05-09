from dataclasses import dataclass
from typing import Optional

from .ast import AST
from .type import Type

# forward declaration
class Expression:
    pass


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
class ForwardDeclaration(Statement):
    return_type: Type
    name: str
    parameters: list[Type]


@dataclass
class FunctionParameter(AST):
    name: str
    type: Type


@dataclass
class FunctionDeclaration(Statement):
    return_type: Type
    name: str
    body: Body
    parameters: list[FunctionParameter]


@dataclass
class VariableDeclarationQualifier(Statement):
    identifier: str
    array_specifier: Optional[Expression] = None
    initializer: Optional[Expression] = None

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

    def __post_init__(self):
        for stmt in self.body.statements:
            if isinstance(stmt, BreakStatement):
                stmt.if_statement = self
            elif isinstance(stmt, ContinueStatement):
                stmt.if_statement = self


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


@dataclass
class ReturnStatement(Statement):
    function: FunctionDeclaration
    expression: Optional[Expression] = None


@dataclass
class StructMember(Statement):
    name: str
    type: Type


@dataclass
class StructDefinition(Statement):
    name: str
    members: list[StructMember]

    def __eq__(self, other):
        if isinstance(other, StructDefinition):
            return self.name == other.name
        return False
