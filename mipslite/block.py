from .register_manager import Register
from .type import Float

from typing import Union


class Block:
    def __init__(self, label: str):
        self.label = label
        self.instructions: list[str] = []
        self.cursor = 0

    def __repr__(self):
        return f"{self.label}:\n\t" + "\n\t".join(self.instructions)

    def add_instruction(self, instruction: str) -> None:
        self.instructions.insert(self.cursor, instruction)
        self.cursor += 1

    def position_at_start(self) -> None:
        self.cursor = 0

    def position_at_end(self) -> None:
        self.cursor = len(self.instructions)

    def load_word(self, dest: Register, src: Register) -> None:
        src_fmt = f"({src})" if src.offset is None else src
        if src.type == Float:
            self.add_instruction(f"l.s {dest}, {src_fmt}")
        else:
            self.add_instruction(f"lw {dest}, {src_fmt}")

    def load_address(self, dest: Register, src: Union[Register, str]) -> None:
        src_fmt = f"({src})" if isinstance(src, Register) and src.offset is None else src
        self.add_instruction(f"la {dest}, {src_fmt}")

    def store_word(self, src: Register, dest: Register) -> None:
        dest_fmt = f"({dest})" if dest.offset is None else dest
        if src.type == Float:
            self.add_instruction(f"s.s {src}, {dest_fmt}")
        else:
            self.add_instruction(f"sw {src}, {dest_fmt}")

    def comment(self, comment: str) -> None:
        self.add_instruction(f"# {comment}")

