

class Allocator:
    def __init__(self):
        self.allocation_ptr = 0

    def allocate(self, size: int) -> str:
        start = self.allocation_ptr
        self.allocation_ptr += size
        return f"{start}($fp)"
