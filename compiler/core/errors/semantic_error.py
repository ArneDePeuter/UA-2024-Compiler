class SemanticError(Exception):
    def __init__(self, message, line=None, position=None):
        self.message = message
        self.line = line
        self.position = position
        super().__init__(self.message)

    def __str__(self):
        error_message = "[ Error ]"
        if self.line is not None:
            error_message += f" line {self.line}"
        if self.position is not None:
            error_message += f", position {self.position}"
        error_message += f": {self.message}"
        return error_message
