class Symbol:
    def __init__(self, name, type=None, scope_level=None, line=None, additional_info=None):
        self.name = name
        self.type = type
        self.scope_level = scope_level
        self.line = line  # Useful for error reporting
        self.additional_info = additional_info  # For any additional symbol-related information

class SymbolTable:
    def __init__(self, parent=None, scope_name=None, scope_level=0):
        self.symbols = {}
        self.parent = parent
        self.scope_name = scope_name  # Name of the scope (useful for debugging)
        self.scope_level = scope_level
        self.children = []  # Added this line to track child symbol tables

    def insert(self, name, symbol):
        self.symbols[name] = symbol

    def lookup(self, name, current_scope_only=False):
        symbol = self.symbols.get(name)
        if symbol is not None:
            return symbol
        if not current_scope_only and self.parent:
            return self.parent.lookup(name)
        return None

    def enter_new_scope(self, scope_name):
        new_child = SymbolTable(parent=self, scope_name=scope_name, scope_level=self.scope_level + 1)
        self.children.append(new_child)  # Track the new child
        return new_child

""""
source: https://www.geeksforgeeks.org/symbol-table-compiler/
"""

