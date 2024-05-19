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
            repr_str += "\n\n.text\n"
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

    def printf(self, label: str, format_string: str, args: list):
        """
        Generates the MIPS assembly code for the printf function
        :param label: The label of the function
        :param format_string: The format string for the printf call
        :param args: The list of arguments to be printed
        :return:
        """
        printf_block = self.function(label)
        # Split the format string into part %\w using re.
        # Then when the part starts with % meaning it is a format specifier, for an argument. We should make a printf_text_block for printing the argument
        # When the part doesn't stat with % meaning it is a strign we should make a printf text block for printing the strin
        parts = re.split(r'(%[dxfsc%])', format_string.strip("\""))
        while parts.count("") > 0:
            parts.remove("")
        arg_index = 0
        for part in parts:
            if part.startswith('%'):
                # Print the arg
                if isinstance(args[arg_index], ast.INT):
                    # Check if the argument is hex
                    if part.count('x') > 0:
                        hex_str = format(args[arg_index], 'x')
                        for char in hex_str:
                            printf_block.add_instruction(f"li $a0, '{char}'")
                            printf_block.add_instruction("li $v0, 11")
                            printf_block.add_instruction("syscall")
                    else:
                        printf_block.add_instruction(f"li $a0, {args[arg_index]}")
                        printf_block.add_instruction("li $v0, 1")
                        printf_block.add_instruction("syscall")
                elif isinstance(args[arg_index], ast.FLOAT):
                    float_str = f"{args[arg_index]:.6f}"
                    for char in float_str:
                        printf_block.add_instruction(f"li $a0, '{char}'")
                        printf_block.add_instruction("li $v0, 11")
                        printf_block.add_instruction("syscall")
                elif isinstance(args[arg_index], ast.CHAR):
                    printf_block.add_instruction(f"li $a0, \'{args[arg_index]}\'")
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

    def scanf(self, label: str, format_string: str, args: list):
        """
        Generates the MIPS assembly code for the scanf function
        :param label: The label of the function
        :param format_string: The format string for the scanf call
        :param args: The list of arguments to be read
        :return:
        """
        scanf_block = self.function(label)
        parts = re.split(r'(%[dxfsc])', format_string.strip("\""))
        while parts.count("") > 0:
            parts.remove("")

        arg_index = 0
        for part in parts:
            # Print the arg
            if isinstance(args[arg_index], ast.INT):
                # Check if the argument is hex
                if part.count('x') > 0:
                    # Read integer in hex format
                    scanf_block.add_instruction("li $v0, 5")
                    scanf_block.add_instruction("syscall")
                    scanf_block.add_instruction(f"sw $v0, {args[arg_index]}($gp)")
                else:
                    # Read integer in decimal format
                    scanf_block.add_instruction("li $v0, 5")
                    scanf_block.add_instruction("syscall")
                    scanf_block.add_instruction(f"sw $v0, {args[arg_index].address}($gp)")
            elif isinstance(args[arg_index], ast.FLOAT):
                # Read float
                scanf_block.add_instruction("li $v0, 6")
                scanf_block.add_instruction("syscall")
                scanf_block.add_instruction(f"swc1 $f0, {args[arg_index].address}($gp)")
            elif isinstance(args[arg_index], ast.CHAR):
                # Read character
                scanf_block.add_instruction("li $v0, 12")
                scanf_block.add_instruction("syscall")
                scanf_block.add_instruction(f"sb $v0, {args[arg_index].address}($gp)")
            elif isinstance(args[arg_index], ast.ArrayInitializer):
                # Read string
                scanf_block.add_instruction(f"la $a0, {args[arg_index].address}($gp)")
                scanf_block.add_instruction("li $v0, 8")
                scanf_block.add_instruction("syscall")
            arg_index += 1

