import re

from compiler.core import ast

from .block import Block
from .function import Function
from .register_manager import RegisterManager

class Module:
    def __init__(self):
        self.data_blocks: list[Block] = []
        self.text_blocks: list[Block] = []
        self.register_manager = RegisterManager()

    def __repr__(self):
        repr_str = ""
        if self.data_blocks:
            repr_str = ".data\n"
            repr_str += "\n".join(map(str, self.data_blocks))
        if self.text_blocks:
            repr_str += "\n.text\n"
            repr_str += "\n".join(map(str, self.text_blocks))
        return repr_str

    def function(self, label: str) -> Function:
        func = Function(label)
        self.text_blocks.append(func)
        return func

    def data_block(self, label: str,) -> Block:
        block = Block(label)
        self.data_blocks.append(block)
        return block

    def printf(self, format_string: str, args: list):
        """
        Generates the MIPS assembly code for the printf function
        :param format_string: The format string for the printf call
        :param args: The list of arguments to be printed
        :return:
        """
        printf_block = self.function("printf")
        # Split the format string into part %\w using re.
        # Then when the part starts with % meaning it is a format specifier, for an argument. We should make a printf_text_block for printing the argument
        # When the part doesn't stat with % meaning it is a strign we should make a printf text block for printing the strin
        parts = re.split(r'(%[dxfsc%])', format_string.strip("\""))
        if parts.count("") > 0:
            parts.remove("")
        arg_index = 0
        for part in parts:
            if part.startswith('%'):
                # Print the arg
                if isinstance(args[arg_index], ast.INT):
                    printf_block.add_instruction(f"li $a0, {args[arg_index].value}")
                    printf_block.add_instruction("li $v0, 1")
                    printf_block.add_instruction("syscall")
                elif isinstance(args[arg_index], ast.FLOAT):
                    printf_block.add_instruction(f"li $f12, {args[arg_index].value}")
                    printf_block.add_instruction("li $v0, 2")
                    printf_block.add_instruction("syscall")
                elif isinstance(args[arg_index], ast.CHAR):
                    printf_block.add_instruction(f"li $a0, \'{args[arg_index].value}\'")
                    printf_block.add_instruction("li $v0, 11")
                    printf_block.add_instruction("syscall")
                elif isinstance(args[arg_index], ast.ArrayInitializer):
                    str = ""
                    for char in args[arg_index]:
                        str += char.value
                    printf_block.add_instruction(f"li $a0, {str}")
                    printf_block.add_instruction("li $v0, 4")
                    printf_block.add_instruction("syscall")
                arg_index += 1
            else:
                # Print the string
                # Create a new data block for the string
                printf_data_block = self.data_block(f"printf_text_{id(part)}")
                printf_data_block.add_instruction(f".asciiz \"{part}\"")
                printf_block.add_instruction(f"la $a0, {printf_data_block.label}")
                printf_block.add_instruction("li $v0, 4")
                printf_block.add_instruction("syscall")
