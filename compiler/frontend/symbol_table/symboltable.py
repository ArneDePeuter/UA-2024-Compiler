class Symbol:
    def __init__(self, name, type, scope_level=0):
        self.name = name
        self.type = type
        self.scope_level = scope_level

class Scope:
    def __init__(self, level=0, parent=None):
        self.level = level
        self.parent = parent
        self.children = {} # Track children for the visualization (when scope is exited, the scope is gone)
        self.symbols = {}

    def define_symbol(self, symbol):
        self.symbols[symbol.name] = symbol

    def lookup(self, name, current_scope_only=False):
        symbol = self.symbols.get(str(name))

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
        new_scope_level = self.current_scope.level + 1
        new_scope = Scope(level=new_scope_level, parent=self.current_scope)
        self.global_scope.children[new_scope_level] = new_scope
        self.current_scope = new_scope

    def exit_scope(self):
        if self.current_scope.parent is not None:
            self.current_scope = self.current_scope.parent

    def define_symbol(self, symbol):
        return self.current_scope.define_symbol(symbol)

    def lookup(self, name, current_scope_only=False) -> Symbol:
        return self.current_scope.lookup(name, current_scope_only=current_scope_only)
