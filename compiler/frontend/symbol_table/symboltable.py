class Symbol:
    def __init__(self, name, type, is_constant=False, is_pointer=False, scope_level=0):
        self.name = name
        self.type = type
        self.is_constant = is_constant
        self.is_pointer = is_pointer
        self.scope_level = scope_level

class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = {}

    def define_symbol(self, symbol):
        self.symbols[symbol.name] = symbol

    def lookup(self, name, current_scope_only=False):
        symbol = self.symbols.get(name)

        if symbol is not None:
            return symbol
        elif self.parent is not None and not current_scope_only:
            return self.parent.lookup(name)
        else:
            return None

class SymbolTable:
    def __init__(self):
        self.global_scope = Scope(level=0)
        self.current_scope = self.global_scope

    def enter_scope(self):
        self.current_scope = Scope(level=self.current_scope.level + 1, parent=self.current_scope)

    def exit_scope(self):
        self.current_scope = self.current_scope.parent

    def define_symbol(self, symbol):
        return self.current_scope.define_symbol(symbol)

    def lookup(self, name):
        return self.current_scope.lookup(name)