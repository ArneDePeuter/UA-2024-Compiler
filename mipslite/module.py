from .block import Block
from .function import Function
from .register_manager import RegisterManager

class Module:
    def __init__(self):
        self.blocks: list[Block] = []
        self.register_manager = RegisterManager()

    def __repr__(self):
        return "\n".join(map(str, self.blocks))

    def function(self, label: str) -> Function:
        func = Function(label)
        self.blocks.append(func)
        return func
