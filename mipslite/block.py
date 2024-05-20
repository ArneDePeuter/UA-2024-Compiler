from typing import Optional
from .allocator import Allocator


class Block:
    def __init__(self, label: str, allocator: Allocator = None, parent: "Block" = None):
        self.parent = parent
        self.children: list[Block] = []
        self.label = label
        self.instructions: list[str] = []
        self.cursor = 0
        self.allocator = allocator

    def __repr__(self):
        total = f"{self.label}:\n\t" + "\n\t".join(self.instructions)
        for child in self.children:
            total += f"\n{child}"
        return total

    def add_instruction(self, instruction: str) -> None:
        self.instructions.insert(self.cursor, instruction)
        self.cursor += 1

    def position_at_start(self) -> None:
        self.cursor = 0

    def position_at_end(self) -> None:
        self.cursor = len(self.instructions)

    def spawn(self, label: str) -> "Block":
        block = Block(label, self.allocator, self)
        self.children.append(block)
        return block

    def kill(self) -> Optional[None]:
        return self.parent

    def allocate(self, size: int) -> str:
        if self.allocator is None:
            raise ValueError("Cannot allocate in root block")
        return self.allocator.allocate(size)

    def load(self, dest: str, src: str) -> None:
        self.add_instruction(f"lw {dest}, {src}")

    def store(self, src: str, dest: str) -> None:
        self.add_instruction(f"sw {src}, {dest}")

    def store_double(self, src: str, dest: str) -> None:
        self.add_instruction(f"s.d {src}, {dest}")
