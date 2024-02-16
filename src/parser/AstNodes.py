from abc import abstractmethod, ABC
from enum import Enum


class AST(ABC):
    @abstractmethod
    def visit(self, visitor):
        raise NotImplementedError

    @abstractmethod
    def to_dot(self) -> str:
        raise NotImplementedError


class Expression(AST, ABC):
    pass


class BinaryOp(Enum):
    plus = "+"
    minus = "-"
    div = "/"
    mul = "*"


class BinaryOperation(Expression):
    def __init__(self, left: Expression, op: BinaryOp, right: Expression) -> None:
        self.left = left
        self.op = op
        self.right = right

    @abstractmethod
    def visit(self, visitor):
        raise NotImplementedError

    @abstractmethod
    def to_dot(self) -> str:
        raise NotImplementedError

