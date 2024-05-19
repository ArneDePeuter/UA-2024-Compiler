from .type import Type


class Allocator:
    def __init__(self):
        self.allocation_ptr = 0

    def allocate(self, type_: Type) -> str:
        start = self.allocation_ptr
        self.allocation_ptr += type_.width
        return f"{start}($fp)"
