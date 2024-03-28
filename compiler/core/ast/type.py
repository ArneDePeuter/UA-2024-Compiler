from enum import Enum
from typing import Optional
from dataclasses import dataclass

from .ast import AST


class BaseType(Enum):
    int = "int"
    char = "char"
    float = "float"
    bool = "bool"

    def __str__(self):
        return self.value


class AddressQualifier(Enum):
    pointer = "*"

    def __str__(self):
        return self.value


@dataclass
class Type(AST):
    base_type: BaseType
    const: Optional[bool] = False
    address_qualifiers: Optional[list[AddressQualifier]] = None

    def __post_init__(self):
        if self.address_qualifiers is None:
            self.address_qualifiers = []

    def __str__(self):
        return str(self.base_type)+''.join(str(qualifier) for qualifier in self.address_qualifiers)
