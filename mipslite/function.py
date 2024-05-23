from contextlib import contextmanager
from uuid import uuid4
from typing import List

from .block import Block
from .allocator import Allocator
from .type import Type


class Function:
    def __init__(self, label: str):
        self.label = label
        self.allocator = Allocator()
        self.blocks: List[Block] = []
        self.current_block = self.create_block(label)

    def __repr__(self):
        if len(self.blocks) == 0:
            return ""

        # add enter and exit stack setup to first and last block
        self.add_function_enter(self.blocks[0])
        self.add_function_exit(self.blocks[-1])

        return "\n".join(map(str, self.blocks))

    @property
    def total_stack_size(self) -> int:
        return self.allocator.allocation_ptr + 16

    def add_function_enter(self, block: Block):
        block.position_at_start()
        block.add_instruction(f"addiu $sp, $sp, -{self.total_stack_size}")
        block.add_instruction(f"sw $ra, {self.total_stack_size - 4}($sp)")
        block.add_instruction(f"sw $fp, {self.total_stack_size - 8}($sp)")
        block.add_instruction(f"move $fp, $sp")

    def add_function_exit(self, block: Block):
        block.position_at_end()
        block.add_instruction("move $sp, $fp")
        block.add_instruction(f"lw $fp, {self.total_stack_size - 8}($sp)")
        block.add_instruction(f"lw $ra, {self.total_stack_size - 4}($sp)")
        block.add_instruction(f"addiu $sp, $sp, {self.total_stack_size}")
        # Main function should not have jr ra but should have exit syscall
        if self.label != "main":
            block.add_instruction("jr $ra")
            block.add_instruction("nop")
        else:
            block.add_instruction("li $v0, 10")
            block.add_instruction("syscall")

    def allocate(self, type_: Type) -> str:
        return self.allocator.allocate(type_)

    def create_block(self, label: str) -> Block:
        block = Block(label)
        self.blocks.append(block)
        return block

    def add_instruction(self, instruction: str) -> None:
        self.current_block.add_instruction(instruction)

    def load(self, dest: str, src: str) -> None:
        self.current_block.add_instruction(f"lw {dest}, {src}")

    def load_double(self, dest: str, src: str) -> None:
        self.current_block.add_instruction(f"l.d {dest}, {src}")

    def store(self, src: str, dest: str) -> None:
        self.current_block.add_instruction(f"sw {src}, {dest}")

    def store_double(self, src: str, dest: str) -> None:
        self.add_instruction(f"s.d {src}, {dest}")

    @contextmanager
    def if_then(self, condition_register: str) -> None:
        # Labels for branches
        true_label = f"if_{uuid4().hex}"
        end_label = f"endif_{uuid4().hex}"

        # Branch if false (if condition_register is zero)
        self.add_instruction(f"beq {condition_register}, $zero, {end_label}")
        self.add_instruction(f"nop")

        # Enter the true block
        true_block = self.create_block(true_label)
        self.current_block = true_block

        yield

        # Jump to end after true block
        self.add_instruction(f"j {end_label}")
        self.add_instruction(f"nop")

        # End block
        end_block = self.create_block(end_label)
        self.current_block = end_block

    @contextmanager
    def if_else(self, condition_register: str):
        # Labels for branches
        true_label = f"if_{uuid4().hex}"
        false_label = f"else_{uuid4().hex}"
        end_label = f"endif_{uuid4().hex}"

        # Branch if false (if condition_register is zero)
        self.add_instruction(f"beq {condition_register}, $zero, {false_label}")
        self.add_instruction("nop")

        # Define context managers for true and false blocks
        @contextmanager
        def true_block():
            self.current_block = self.create_block(true_label)
            yield
            self.add_instruction(f"j {end_label}")
            self.add_instruction("nop")

        @contextmanager
        def false_block():
            self.current_block = self.create_block(false_label)
            yield
            self.add_instruction(f"j {end_label}")
            self.add_instruction("nop")

        try:
            yield true_block(), false_block()
        finally:
            # Create the end block after both true and false blocks are executed
            self.current_block = self.create_block(end_label)