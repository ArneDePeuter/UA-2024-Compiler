from enum import Enum
from typing import Optional, List, ForwardRef, Union
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

    def __eq__(self, other):
        if isinstance(other, ArraySpecifier):
            return self.sizes == other.sizes
        return False

    def __str__(self):
        return ''.join(f"[{size.value}]" for size in self.sizes)

    def __gt__(self, other):
        for i in range(len(self.sizes)):
            if self.sizes[i] > other.sizes[i]:
                return True
        return False

@dataclass
class ArrayType(AST):
    element_type: 'Type'
    array_sizes: List[ArraySpecifier]

    def __eq__(self, other):
        if isinstance(other, ArrayType):
            return self.element_type == other.element_type and self.array_sizes == other.array_sizes
        return False

    def __str__(self):
        return f"array of {self.element_type}{self.array_sizes}"

@dataclass
class Type(AST):
    type: Union[BaseType, ArrayType, ForwardRef("StructType")]
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

    def __hash__(self):
        return hash(str(self))

@dataclass
class StructType(AST):
    definition: "StructDefinition"

    def __eq__(self, other):
        if isinstance(other, StructType):
            return self.definition == other.definition
        return False

    def __str__(self):
        return f"struct {self.definition.name}"

from .statement import StructDefinition