from .block import Block
from .function import Function

class Module:
    def __init__(self):
        self.blocks: list[Block] = []

    def __repr__(self):
        return "\n".join(map(str, self.blocks))

    def function(self, label: str) -> Function:
        func = Function(label)
        self.blocks.append(func)
        return func
