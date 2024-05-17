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

    def store(self, dest: str, src: str) -> None:
        self.add_instruction(f"sw {dest}, {src}")

    # Additional MIPS Instructions for LLVM IR commands
    def alloca(self, dest: str, size: int) -> None:
        addr = self.allocate(size)
        self.add_instruction(f"la {dest}, {addr}")

    def and_(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"and {dest}, {src1}, {src2}")

    def bitcast(self, dest: str, src: str) -> None:
        self.add_instruction(f"move {dest}, {src}")

    def call(self, func: str, args: list[str], ret: Optional[str] = None) -> None:
        for i, arg in enumerate(args):
            self.add_instruction(f"move $a{i}, {arg}")
        self.add_instruction(f"jal {func}")
        if ret:
            self.add_instruction(f"move {ret}, $v0")

    def cbranch(self, cond: str, true_label: str, false_label: str) -> None:
        self.add_instruction(f"bne {cond}, $zero, {true_label}")
        self.add_instruction(f"j {false_label}")

    def ret(self, src: Optional[str] = None) -> None:
        if src:
            self.add_instruction(f"move $v0, {src}")
        self.add_instruction(f"jr $ra")
        self.add_instruction("nop")

    def ret_void(self) -> None:
        self.add_instruction(f"jr $ra")
        self.add_instruction("nop")

    def fadd(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"add.s {dest}, {src1}, {src2}")

    def fsub(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"sub.s {dest}, {src1}, {src2}")

    def fmul(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"mul.s {dest}, {src1}, {src2}")

    def fdiv(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"div.s {dest}, {src1}, {src2}")

    def frem(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"rem.s {dest}, {src1}, {src2}")

    def fcmp_ordered(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"c.eq.s {src1}, {src2}")
        self.add_instruction(f"bc1t {dest}")

    def icmp_signed(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"slt {dest}, {src1}, {src2}")

    def icmp_unsigned(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"sltu {dest}, {src1}, {src2}")

    def insert_value(self, agg: str, value: str, index: int) -> None:
        self.add_instruction(f"sw {value}, {index * 4}({agg})")

    def gep(self, dest: str, base: str, offset: str) -> None:
        self.add_instruction(f"addu {dest}, {base}, {offset}")

    def ptrtoint(self, dest: str, src: str) -> None:
        self.add_instruction(f"move {dest}, {src}")

    def lshr(self, dest: str, src: str, shift: int) -> None:
        self.add_instruction(f"srl {dest}, {src}, {shift}")

    def mul(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"mul {dest}, {src1}, {src2}")

    def neg(self, dest: str, src: str) -> None:
        self.add_instruction(f"neg {dest}, {src}")

    def not_(self, dest: str, src: str) -> None:
        self.add_instruction(f"not {dest}, {src}")

    def or_(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"or {dest}, {src1}, {src2}")

    def sdiv(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"div {dest}, {src1}, {src2}")

    def shl(self, dest: str, src: str, shift: int) -> None:
        self.add_instruction(f"sll {dest}, {src}, {shift}")

    def srem(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"rem {dest}, {src1}, {src2}")

    def sub(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"sub {dest}, {src1}, {src2}")

    def xor(self, dest: str, src1: str, src2: str) -> None:
        self.add_instruction(f"xor {dest}, {src1}, {src2}")
