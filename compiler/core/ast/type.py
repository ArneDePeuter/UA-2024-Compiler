from dataclasses import dataclass
from .ast import AST

@dataclass
class Type(AST):
    base_type: str
    type_qualifier: str or None
    pointer_qualifiers: list[str]