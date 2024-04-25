from enum import Enum
from typing import Optional, List
from dataclasses import dataclass

from .ast import AST


class BaseType(Enum):
    int = "int"
    char = "char"
    float = "float"
    bool = "bool"
    void = "void"

    def __str__(self):
        return self.value


class AddressQualifier(Enum):
    pointer = "*"

    def __str__(self):
        return self.value

@dataclass
class ArraySpecifier(AST):
    sizes: list[int]

@dataclass
class ArrayType(AST):
    element_type: BaseType
    array_sizes: List[ArraySpecifier]


@dataclass
class Type(AST):
    type: BaseType | ArrayType
    const: Optional[bool] = False
    address_qualifiers: Optional[list[AddressQualifier]] = None

    def __post_init__(self):
        if self.address_qualifiers is None:
            self.address_qualifiers = []

    def __str__(self):
        return ("const " if self.const else "")+str(self.type)+''.join(str(qualifier) for qualifier in self.address_qualifiers)

    def __eq__(self, other):
        if isinstance(other, Type):
            return self.type == other.type and self.const == other.const and self.address_qualifiers == other.address_qualifiers
        return False