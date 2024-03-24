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

    def __add__(self, other):
        return INT(self.value + other.value)

    def __sub__(self, other):
        return INT(self.value - other.value)

    def __mul__(self, other):
        return INT(self.value * other.value)

    def __truediv__(self, other):
        return INT(self.value // other.value)

    def __mod__(self, other):
        return INT(self.value % other.value)


@dataclass
class FLOAT(Expression):
    value: float

    def __add__(self, other):
        return FLOAT(
            value=self.value + other.value,
            line=self.line,
            position=self.position
        )

    def __sub__(self, other):
        return FLOAT(
            value=self.value - other.value,
            line=self.line,
            position=self.position
        )

    def __mul__(self, other):
        return FLOAT(
            value=self.value * other.value,
            line=self.line,
            position=self.position
        )

    def __truediv__(self, other):
        return FLOAT(
            value=self.value / other.value,
            line=self.line,
            position=self.position
        )

    def __mod__(self, other):
        return FLOAT(
            value=self.value % other.value,
            line=self.line,
            position=self.position
        )


@dataclass
class CHAR(Expression):
    value: str

    def __add__(self, other):
        return CHAR(
            value=chr(ord(self.value) + ord(other.value)),
            line=self.line,
            position=self.position
        )

    def __sub__(self, other):
        return CHAR(
            value=chr(ord(self.value) - ord(other.value)),
            line=self.line,
            position=self.position
        )

    def __mul__(self, other):
        return CHAR(
            value=chr(ord(self.value) * ord(other.value)),
            line=self.line,
            position=self.position
        )

    def __truediv__(self, other):
        return CHAR(
            value=chr(ord(self.value) // ord(other.value)),
            line=self.line,
            position=self.position
        )

    def __mod__(self, other):
        return CHAR(
            value=chr(ord(self.value) % ord(other.value)),
            line=self.line,
            position=self.position
        )


@dataclass
class IDENTIFIER(Expression):
    name: str


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
        ADDRESSOF = "&"
        DEREFERENCE = "*"
        INCREMENT = "++"
        DECREMENT = "--"

    value: Expression
    operator: Operator
    prefix: bool


@dataclass
class ShiftExpression(Expression):
    class Operator(Enum):
        LEFT = "<<"
        RIGHT = ">>"

    value: Expression
    operator: Operator
    amount: Expression


@dataclass
class PrintFCall(Expression):
    class Replacer(Enum):
        s = "%s"
        d = "%d"
        x = "%x"
        f = "%f"
        c = "%c"

    replacer: Replacer
    expression: Expression
