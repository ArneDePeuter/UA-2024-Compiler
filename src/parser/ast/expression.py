from enum import Enum
from dataclasses import dataclass

from .statement import Statement


@dataclass
class Expression(Statement):
    pass


@dataclass
class INT(Expression):
    value: int


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

    left: Expression
    operator: Operator
    right: Expression


@dataclass
class BinaryBitwiseArithmetic(BinaryOperation):
    class Operator(Enum):
        AND = "&"
        OR = "|"
        XOR = "^"

    left: Expression
    operator: Operator
    right: Expression


@dataclass
class BinaryLogicalOperation(BinaryOperation):
    class Operator(Enum):
        AND = "&&"
        OR = "||"

    left: Expression
    operator: Operator
    right: Expression

@dataclass
class ComparisonOperation(BinaryOperation):
    class Operator(Enum):
        GT = ">"
        LT = "<"
        GTE = ">="
        LTE = "<="
        EQ = "=="
        NEQ = "!="

    left: Expression
    operator: Operator
    right: Expression


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
class BitwiseExpression(BinaryOperation):
    class Operator(Enum):
        BITAND = "&"
        BITOR = "|"
        BITXOR = "^"
        BITNOT = "~"

    left: Expression
    operator: Operator
    right: Expression


@dataclass
class ShiftExpression(Expression):
    class Operator(Enum):
        LEFT = "<<"
        RIGHT = ">>"

    value: Expression
    operator: Operator
    amount: Expression
