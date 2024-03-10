from abc import ABC
from dataclasses import dataclass
from typing import Optional as Optional
from ..symbol_table.symboltable import SymbolTable


@dataclass
class AST(ABC):
    #symbol_table: Optional[SymbolTable] = None
    pass