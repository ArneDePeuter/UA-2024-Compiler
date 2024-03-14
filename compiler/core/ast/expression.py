from enum import Enum
from dataclasses import dataclass

from .type import Type
from .ast import AST


@dataclass
class Expression(AST):
    pass


@dataclass
class INT(Expression):
    value: int


@dataclass
class FLOAT(Expression):
    value: float


@dataclass
class CHAR(Expression):
    value: str


@dataclass
class IDENTIFIER(Expression):
    name: str


@dataclass
class DereferenceExpression(Expression):
    expression: Expression


@dataclass
class AddressExpression(Expression):
    expression: Expression


@dataclass
class TypeCastExpression(Expression):
    cast_type: Type
    expression: Expression


@dataclass
class BinaryOperation(Expression):
    left: Expression
    right: Expression


@dataclass
class BinaryArithmetic(BinaryOperation):
    class Operator(Enum):
        PLUS = "+"
        MINUS = "-"
        MUL = "*"
        DIV = "/"
        MOD = "%"

    operator: Operator


@dataclass
class BinaryBitwiseArithmetic(BinaryOperation):
    class Operator(Enum):
        AND = "&"
        OR = "|"
        XOR = "^"

    operator: Operator


@dataclass
class BinaryLogicalOperation(BinaryOperation):
    class Operator(Enum):
        AND = "&&"
        OR = "||"

    operator: Operator


@dataclass
class ComparisonOperation(BinaryOperation):
    class Operator(Enum):
        GT = ">"
        LT = "<"
        GTE = ">="
        LTE = "<="
        EQ = "=="
        NEQ = "!="

    operator: Operator


@dataclass
class UnaryExpression(Expression):
    class Operator(Enum):
        POSITIVE = "+"
        NEGATIVE = "-"
        ONESCOMPLEMENT = "~"
        LOGICALNEGATION = "!"

    value: Expression
    operator: Operator


@dataclass
class ShiftExpression(Expression):
    class Operator(Enum):
        LEFT = "<<"
        RIGHT = ">>"

    value: Expression
    operator: Operator
    amount: Expression
