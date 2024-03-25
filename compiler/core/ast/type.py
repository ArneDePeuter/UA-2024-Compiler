from enum import Enum
from typing import Optional
from dataclasses import dataclass

from .ast import AST


class BaseType(Enum):
    int = "int"
    char = "char"
    float = "float"


class AddressQualifier(Enum):
    pointer = "*"


@dataclass
class Type(AST):
    base_type: BaseType
    const: Optional[bool] = False
    address_qualifiers: Optional[list[AddressQualifier]] = None

    def __post_init__(self):
        if self.address_qualifiers is None:
            self.address_qualifiers = []
