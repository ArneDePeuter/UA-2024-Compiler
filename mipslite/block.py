from .register_manager import Register, RegisterManager
from .allocator import Allocator
from .type import Float, Type

from typing import Union, Optional


class Block:
    def __init__(self, label: str, allocator: Optional[Allocator] = None):
        self.label = label
        self.allocator = allocator
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
        src_fmt = None
        if isinstance(src, Register):
            if src.offset is not None:
                src_fmt = f"{src.offset}({src.register})"
            elif src.register.startswith("$"):
                src_fmt = f"({src.register})"
            else:
                src_fmt = src.register
        #src_fmt = f"({src})" if src.offset is None else src
        if isinstance(src.type, Float):
            self.add_instruction(f"l.s {dest}, {src_fmt}")
        else:
            self.add_instruction(f"lw {dest}, {src_fmt}")

    def load_address(self, dest: Register, src: Union[Register, str]) -> None:
        src_fmt = None
        if isinstance(src, Register):
            if src.offset is not None:
                src_fmt = f"{src.offset}({src.register})"
            else:
                if src.register.startswith("$"):
                    src_fmt = f"({src.register})"
                else:
                    src_fmt = src.register
        else:
            src_fmt = src
        #src_fmt = f"({src})" if isinstance(src, Register) and src.offset is None else src
        self.add_instruction(f"la {dest}, {src_fmt}")

    def store_word(self, src: Register, dest: Union[Register, str]) -> None:
        dest_fmt = None
        if isinstance(dest, Register):
            if dest.offset is not None:
                dest_fmt = f"{dest.offset}({dest.register})"
            elif dest.register.startswith("$"):
                dest_fmt = f"({dest.register})"
            else:
                dest_fmt = dest.register
        else:
            dest_fmt = dest
        #dest_fmt = f"({dest})" if isinstance(dest, Register) and dest.offset is None else dest
        if isinstance(src.type, Float):
            self.add_instruction(f"s.s {src}, {dest_fmt}")
        else:
            self.add_instruction(f"sw {src}, {dest_fmt}")

    def comment(self, comment: str) -> None:
        self.add_instruction(f"# {comment}")

    def allocate(self, type_: Type) -> Register:
        return self.allocator.allocate(type_)

    def jal(self, label: str, register_manager: RegisterManager) -> None:
        # save all temp registers on the stack
        fd_dict = {}
        for reg in register_manager.used_registers["temp"]:
            cls = register_manager.used_reg_classes[reg]
            alloc = self.allocator.allocate(cls.type)
            self.add_instruction(f"sw {reg}, {alloc}")
            fd_dict[reg] = alloc
        self.add_instruction(f"jal {label}")
        self.add_instruction("nop")
        # restore all temp registers from the stack
        for reg, alloc in fd_dict.items():
            self.add_instruction(f"lw {reg}, {alloc}")
