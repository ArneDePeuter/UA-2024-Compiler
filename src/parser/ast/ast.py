from abc import ABC
from dataclasses import dataclass
from ..symbol_table.symboltable import SymbolTable


@dataclass
class AST(ABC):
    symbol_table: SymbolTable(parent=None)
