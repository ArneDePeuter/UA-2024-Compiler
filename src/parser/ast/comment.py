from dataclasses import dataclass
from .statement import Statement

@dataclass
class Comment(Statement):
    content: str