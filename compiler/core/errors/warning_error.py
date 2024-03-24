class WarningError(Warning):
    def __init__(self, message, line=None, position=None):
        self.message = message
        self.line = line
        self.position = position
        super().__init__(self.message)

    def __str__(self):
        return f"[ Warning ] line {self.line}, position {self.position}: {self.message}"