from abc import ABC
from dataclasses import dataclass


@dataclass
class AST(ABC):
    line: int = None
    position: int = None
