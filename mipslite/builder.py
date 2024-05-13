from .module import Module


class Function:
    def __init__(self, name: str):
        self.name = name
        self.allocation_ptr = 0
        self.lines: list[str] = []

    def __repr__(self):
        total = f"{self.name}:\n"

        # add stack frame enter
        total_stack_size = self.allocation_ptr + 16
        frame_enter = [
            f"addiu   $sp, $sp, -{total_stack_size}",
            f"sw      $ra, {total_stack_size-4}($sp)",
            f"sw      $fp, {total_stack_size-8}($sp)",
            f"move    $fp, $sp"
        ]
        frame_enter.extend(self.lines)
        self.lines = frame_enter

        # add stack frame exit
        frame_exit = [
            f"lw      $2, 4($fp)",
            f"move    $sp, $fp",
            f"lw      $fp, {total_stack_size-8}($sp)",
            f"lw      $ra, {total_stack_size-4}($sp)",
            f"addiu   $sp, $sp, {total_stack_size}",
            f"jr      $ra",
            f"nop"
        ]
        self.lines.extend(frame_exit)

        total += "\t" + "\n\t".join(self.lines)

        return total

    def allocate(self, size: int) -> str:
        start = self.allocation_ptr
        self.allocation_ptr += size
        return f"{start}($fp)"

    def load(self, dest: str, src: str) -> None:
        self.lines.append(f"lw {dest}, {src}")

    def store(self, dest: str, src: str) -> None:
        self.lines.append(f"sw {dest}, {src}")



