from dataclasses import dataclass
from .statement import Statement

@dataclass
class MainFunction(Statement):
    return_type: str
    name: str
    parameters: list
    body: Statement