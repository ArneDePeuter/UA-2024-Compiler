from enum import Enum
from dataclasses import dataclass
from typing import Tuple, Optional

from .type import Type, StructType
from .ast import AST
from compiler.core.errors.semantic_error import SemanticError


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

    def __bool__(self):
        return bool(self.value > 0)

    def __and__(self, other):
        return INT(self.value & other.value)

    def __or__(self, other):
        return INT(self.value | other.value)

    def __xor__(self, other):
        return INT(self.value ^ other.value)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value < other.value or self.value == other.value

    def __ge__(self, other):
        return self.value > other.value or self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


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

    def __bool__(self):
        return bool(self.value > 0)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value < other.value or self.value == other.value

    def __ge__(self, other):
        return self.value > other.value or self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


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

    def __bool__(self):
        return bool(ord(self.value) > 0)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return ord(self.value) > ord(other.value)

    def __le__(self, other):
        return ord(self.value) < ord(other.value) or self.value == other.value

    def __ge__(self, other):
        return ord(self.value) > ord(other.value) or self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)


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
    prefix: bool = False


@dataclass
class ShiftExpression(Expression):
    class Operator(Enum):
        LEFT = "<<"
        RIGHT = ">>"

    value: Expression
    operator: Operator
    amount: Expression


@dataclass
class FunctionCall(Expression):
    name: str
    arguments: list[Expression]


@dataclass
class PrintFCall(Expression):
    format: str
    args: list[Expression]


@dataclass
class ScanFCall(Expression):
    format: str
    args: list[Expression]


@dataclass
class ArrayInitializer(Expression):
    elements: Tuple[Expression]
    struct_type: Optional[StructType] = None

    def set_struct_type(self, struct_type: StructType):
        if len(self.elements) < len(struct_type.definition.members):
            raise SemanticError(f"Too few elements in struct initializer, default params for struct not implemented.", self.line, self.position)
        self.struct_type = struct_type
        for i, member in enumerate(self.struct_type.definition.members):
            if isinstance(member.type.type, StructType) and len(member.type.address_qualifiers) == 0 and isinstance(self.elements[i], ArrayInitializer):
                self.elements[i].set_struct_type(member.type.type)


@dataclass
class ArrayAccess(Expression):
    target: Expression
    index: Expression


@dataclass
class StructAccess(Expression):
    target: Expression
    member_name: str
