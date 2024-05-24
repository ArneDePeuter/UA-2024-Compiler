from typing import Optional


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

    def load(self, dest: str, src: str) -> None:
        self.add_instruction(f"lw {dest}, {src}")

    def load_float(self, dest: str, src: str) -> None:
        self.add_instruction(f"l.s {dest}, {src}")

    def store(self, src: str, dest: str) -> None:
        self.add_instruction(f"sw {src}, {dest}")

    def store_float(self, src: str, dest: str) -> None:
        self.add_instruction(f"s.s {src}, {dest}")
