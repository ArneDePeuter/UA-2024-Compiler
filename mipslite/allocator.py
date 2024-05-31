from .type import Type
from .register_manager import Register


class Allocator:
    def __init__(self):
        self.allocation_ptr = 0

    def allocate(self, type_: Type) -> Register:
        start = self.allocation_ptr
        self.allocation_ptr += type_.width
        return Register("$fp", start, type_)
