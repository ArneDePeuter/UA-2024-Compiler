class SymbolTableDotVisitor():
    def __init__(self):
        self.total = ""
        self.node_counter = 0  # Added to ensure unique node IDs

    def output(self, filename: str):
        with open(filename, "w") as file:
            file.write("digraph SymbolTable {\n")
            file.write(self.total)
            file.write("}\n")

    def generate_dot(self, symbol_table):
        self.traverse_scope(symbol_table)

    def traverse_scope(self, scope):
        current_id = id(scope)

        scope_style = 'style=filled, fillcolor=lightblue'
        node_label = f"Scope Level {scope.level}"

        symbols = ""
        for symbol in scope.symbols.values():
            symbols += f'{symbol.name} : {symbol.type}\n'

        self.total += f'{current_id} [label="{node_label}\n {symbols}"{scope_style}];\n'

        for child in scope.children.values():
            self.total += f'{current_id} -> {id(child)};\n'
            self.traverse_scope(child)
