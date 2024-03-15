from compiler.core.ast_visitor import AstVisitor
from compiler.core.errors.semantic_error import SemanticError
from compiler.core import ast
from symboltable import SymbolTable, Symbol
class SymbolTableVisitor(AstVisitor):
    def __init__(self, symbol_table):
        # super().__init__()  # Aanroep constructor van ASTVisitor indien nodig
        self.symbol_table = symbol_table

    def visit_type(self, node: ast.Type):
        # Implementatie afhankelijk van wat je wilt controleren/uitvoeren voor type nodes

    def visit_int(self, node: ast.INT):
        # Mogelijk wil je hier niets specifieks doen, tenzij je checks hebt voor INT waarden

    def visit_float(self, node: ast.FLOAT):
        # Idem als bij INT, afhankelijk van je specifieke vereisten

    def visit_char(self, node: ast.CHAR):
        # Idem, specifieke acties voor CHAR types indien nodig

    def visit_identifier(self, node: ast.IDENTIFIER):
        # Dit is belangrijk voor het controleren van de declaratie van identifiers
        if self.symbol_table.lookup(node.name) is None:
            raise SemanticError(f"Use of undeclared identifier '{node.name}'.", node.line, node.position)

    def visit_type_cast_expression(self, node: ast.TypeCastExpression):
        # Controleer of het type waarnaar wordt gecast geldig is
        # en of de expressie compatibel is met het cast type.
        # Dit vereist gedetailleerde typevergelijking en mogelijk informatie over impliciete/expliciete conversies.
        self.visit(node.expression)  # Bezoek de expressie die gecast wordt
        # Voeg hier logica toe voor het controleren van de typecast

    def visit_binary_arithmetic(self, node: ast.BinaryArithmetic):
        # Bezoek eerst de linker- en rechterzijde van de operatie
        self.visit(node.left)
        self.visit(node.right)
        # Voer hier type checks uit om te zorgen dat de operatie geldig is voor de gegeven typen


    def visit_binary_bitwise_arithmetic(self, node: ast.BinaryBitwiseArithmetic):
        # Bitwise operaties vereisen meestal integer uitdrukkingen; controleer dit
        self.visit(node.left)
        self.visit(node.right)
        # Voeg logica toe voor het controleren van de geldigheid van de bitwise operatie
    def visit_binary_logical_operation(self, node: ast.BinaryLogicalOperation):
        # Logische operaties vereisen meestal boolean uitdrukkingen; controleer dit
        self.visit(node.left)
        self.visit(node.right)
        # Voeg logica toe voor het controleren van de geldigheid van de logische operatie

    def visit_comparison_operation(self, node: ast.ComparisonOperation):
        # Vergelijkingsoperaties controleren; zorg ervoor dat de typen compatibel zijn
        self.visit(node.left)
        self.visit(node.right)
        # Voeg checks toe om te verzekeren dat de typen vergeleken kunnen worden

    def visit_unary_expression(self, node: ast.UnaryExpression):
        # Bezoek de unaire expressie; controleer op geldigheid afhankelijk van het type operatie
        self.visit(node.expression)
        # Voeg specifieke logica toe voor het type unaire operatie, bijv. negatie, bitwise not, etc.

    def visit_shift_expression(self, node: ast.ShiftExpression):
        # Shift operaties controleren; zorg ervoor dat de typen compatibel zijn
        self.visit(node.left)
        self.visit(node.right)
        # Voeg checks toe om te verzekeren dat de typen vergelijkt kunnen worden

    def visit_program(self, node: ast.Program):
        # Controleer de declaraties in de program
        for declaration in node.declarations:
            self.visit(declaration)

    def visit_body(self, node: ast.Body):
        # Controleer de statements in de body
        for statement in node.statements:
            self.visit(statement)

    def visit_function_declaration(self, node: ast.FunctionDeclaration):
        # Controleer de declaraties in de functie
        for declaration in node.declarations:
            self.visit(declaration)

    def visit_variable_declaration_qualifier(self, node: ast.VariableDeclarationQualifier):
        # Controleer de declaraties in de variabele declaratie
        for declaration in node.declarations:
            self.visit(declaration)

    def visit_variable_declaration(self, node: ast.VariableDeclaration):
        # Voorbeeld voor het behandelen van variabele declaraties
        if self.symbol_table.lookup(node.name, current_scope_only=True):
            raise SemanticError(f"Variable '{node.name}' is already declared.", node.line, node.position)
        self.symbol_table.define_symbol(Symbol(node.name, node.type, scope_level=self.symbol_table.current_scope_level))

    def visit_assignment_statement(self, node: ast.AssignmentStatement):
        # Controleren of de variabele bestaat voordat deze wordt toegewezen
        symbol = self.symbol_table.lookup(node.variable_name)
        if symbol is None:
            raise SemanticError(f"Use of undeclared variable '{node.variable_name}'.", node.line, node.position)
        # Voeg hier extra logica toe voor type checks of andere regels