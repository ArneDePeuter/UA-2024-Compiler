from .block import Block
from .allocator import Allocator


class Function(Block):
    def __init__(self, label: str, parent: "Block" = None):
        super().__init__(label, Allocator(), parent)

    def __repr__(self):
        # add global main
        total = "\n"
        if self.label == "main":
            total += ".globl main\n"
        total += f"{self.label}:\n"

        # add stack frame enter
        total_stack_size = self.allocator.allocation_ptr + 16
        frame_enter = [
            f"addiu   $sp, $sp, -{total_stack_size}",
            f"sw      $ra, {total_stack_size-4}($sp)",
            f"sw      $fp, {total_stack_size-8}($sp)",
            f"move    $fp, $sp"
        ]
        frame_enter.extend(self.instructions)
        self.lines = frame_enter

        # add stack frame exit
        frame_exit = [
            f"move    $sp, $fp",
            f"lw      $fp, {total_stack_size-8}($sp)",
            f"lw      $ra, {total_stack_size-4}($sp)",
            f"addiu   $sp, $sp, {total_stack_size}",
            f"jr      $ra",
            f"nop"
        ]
        # add exit syscall
        if self.label == "main":
            frame_exit.extend([
                "# Exit syscall",
                f"li      $v0, 10",
                f"syscall"
            ])
        self.lines.extend(frame_exit)

        total += "\t" + "\n\t".join(self.lines)

        for child in self.children:
            total += f"\n{child}"
        return total
