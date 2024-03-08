class Symbol:
    def __init__(self, name, type=None, scope_level=None, line=None, additional_info=None):
        self.name = name
        self.type = type
        self.scope_level = scope_level
        self.line = line  # Useful for error reporting
        self.additional_info = additional_info  # For any additional symbol-related information

    def __str__(self):
        return f"Symbol(name={self.name}, type={self.type}, scope_level={self.scope_level}, line={self.line}, additional_info={self.additional_info})"

class SymbolTable:
    def __init__(self, parent=None, scope_name=None, scope_level=0):
        self.symbols = {}
        self.parent = parent
        self.scope_name = scope_name  # Name of the scope (useful for debugging)
        self.scope_level = scope_level  # Nested scope level

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
        return SymbolTable(parent=self, scope_name=scope_name, scope_level=self.scope_level + 1)

    def __str__(self):
        return f"SymbolTable(scope_name={self.scope_name}, scope_level={self.scope_level}, symbols={list(self.symbols.keys())})"

""""
Example usage:
    global_table = SymbolTable(scope_name="global")
    function_table = global_table.enter_new_scope("function")
source: https://www.geeksforgeeks.org/symbol-table-compiler/
"""

