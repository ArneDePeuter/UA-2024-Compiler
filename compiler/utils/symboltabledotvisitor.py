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
        dot_output = self.traverse_scope(symbol_table)
        self.total = dot_output

    def traverse_scope(self, scope, parent_id=None):
        # Ensuring unique node IDs
        self.node_counter += 1
        node_id = f"node{self.node_counter}"

        # Scope nodes have a different style
        scope_style = 'style=filled, fillcolor=lightblue'
        node_label = f"Scope Level {scope.level}"
        output = f'  {node_id} [label="{node_label}", {scope_style}];\n'

        if parent_id:
            # Draw an edge from the parent scope to this scope
            output += f"  {parent_id} -> {node_id};\n"

        for symbol in scope.symbols.values():
            # Symbol nodes are plain text
            symbol_node_id = f"{node_id}_{symbol.name}"
            output += f'  {node_id} -> {symbol_node_id} [color=black];\n'
            output += f'  {symbol_node_id} [label="{symbol.type} {symbol.name}", shape=box, style=filled, fillcolor=white];\n'

        for child in scope.children.values():
            output += self.traverse_scope(child, node_id)
        return output
