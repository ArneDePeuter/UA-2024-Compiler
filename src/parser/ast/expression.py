from .statement import Statement
from enum import Enum


class Expression(Statement):
    pass


class INT(Expression):
    def __init__(self, value: int) -> None:
        self.value = value


class BinaryOperation(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right


class BinaryArithmetic(BinaryOperation):
    class Operator(Enum):
        PLUS = "+"
        MINUS = "-"
        MUL = "*"
        DIV = "/"
        MOD = "%"

    def __init__(self, left: Expression, right: Expression, operator: Operator) -> None:
        super().__init__(left, right)
        self.operator = operator


class BinaryBitwiseArithmetic(BinaryOperation):
    class Operator(Enum):
        AND = "&"
        OR = "|"
        XOR = "^"

    def __init__(self, left: Expression, right: Expression, operator: Operator) -> None:
        super().__init__(left, right)
        self.operator = operator


class BinaryLogicalOperation(BinaryOperation):
    class Operator(Enum):
        AND = "&&"
        OR = "||"

    def __init__(self, left: Expression, right: Expression, operator: Operator) -> None:
        super().__init__(left, right)
        self.operator = operator


class ComparisonOperation(BinaryOperation):
    class Operator(Enum):
        GT = ">"
        LT = "<"
        GTE = ">="
        LTE = "<="
        EQ = "=="
        NEQ = "!="

    def __init__(self, left: Expression, right: Expression, operator: Operator) -> None:
        super().__init__(left, right)
        self.operator = operator


class UnaryExpression(Expression):
    class Operator(Enum):
        POSITIVE = "+"
        NEGATIVE = "-"
        ONESCOMPLEMENT = "~"
        LOGICALNEGATION = "!"

    def __init__(self, value: Expression, operator: Operator) -> None:
        self.value = value
        self.operator = operator

class BitwiseExpression(BinaryOperation):
    class Operator(Enum):
        BITAND = "&"
        BITOR = "|"
        BITXOR = "^"
        BITNOT = "~"

    def __init__(self, left, op, right):
        self.left = left  # The left operand
        self.op = op      # The operator ('&', '|', '^')
        self.right = right  # The right operand

class ShiftExpression(Expression):
    class Operator(Enum):
        LEFT = "<<"
        RIGHT = ">>"

    def __init__(self, value: Expression, operator: Operator, shamt: int) -> None:
        self.value = value
        self.operator = operator
        self.shamt = shamt