from contextlib import contextmanager
from uuid import uuid4
from typing import List

from .block import Block
from .allocator import Allocator
from .type import Type, Float
from .register_manager import Register, RegisterManager


class Function:
    def __init__(self, label: str, return_type: Type):
        self.label = label
        self.return_type = return_type
        self.allocator = Allocator()
        self.blocks: List[Block] = []
        self.current_block = self.create_block(label)

    def __repr__(self):
        if len(self.blocks) == 0:
            return ""

        # add enter and exit stack setup to first and last block
        self.add_function_enter(self.blocks[0])
        self.add_function_exit()

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

    def add_function_exit(self):
        block = Block(f"{self.label}_exit", self.allocator)
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
        self.blocks.append(block)

    def allocate(self, type_: Type) -> Register:
        return self.allocator.allocate(type_)

    def create_block(self, label: str) -> Block:
        block = Block(label, self.allocator)
        self.blocks.append(block)
        return block

    def add_instruction(self, instruction: str) -> None:
        self.current_block.add_instruction(instruction)

    def load_word(self, dest: Register, src: Register) -> None:
        self.current_block.load_word(dest, src)

    def load_address(self, src: Register, dest: Register) -> None:
        self.current_block.load_address(src, dest)

    def store_word(self, src: Register, dest: Register) -> None:
        self.current_block.store_word(src, dest)

    def comment(self, comment: str) -> None:
        self.current_block.comment(comment)

    def ret(self, register: Register) -> None:
        self.add_instruction(f"move $v0, {register}")
        self.add_instruction(f"j {self.label}_exit")
        self.add_instruction("nop")

    def jal(self, label: str, register_manager: RegisterManager) -> None:
        self.current_block.jal(label, register_manager)

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

    @contextmanager
    def while_loop(self):
        condition_label = f"while_{uuid4().hex}"
        start_label = f"start_{uuid4().hex}"
        end_label = f"end_{uuid4().hex}"

        @contextmanager
        def condition_block():
            self.add_instruction(f"j {condition_label}")
            self.add_instruction("nop")
            self.current_block = self.create_block(condition_label)
            yield condition_label
            self.add_instruction(f"j {start_label}")
            self.add_instruction("nop")

        @contextmanager
        def start_block(result_register: str):
            self.add_instruction(f"beq {result_register}, $zero, {end_label}")
            self.add_instruction("nop")
            self.current_block = self.create_block(start_label)
            yield start_label
            self.add_instruction(f"j {condition_label}")
            self.add_instruction("nop")

        yield condition_block(), start_block, [condition_label, start_label, end_label]

        self.current_block = self.create_block(end_label)
