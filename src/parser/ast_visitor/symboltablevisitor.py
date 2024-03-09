from .visitor import Visitor

from ..ast.program import Program
from ..ast import expression as EXPR
from ..ast import ast as AST
from ..ast.main_function import MainFunction
from ..ast.compound_statement import CompoundStatement
from ..ast.expression import CastExpression
from ..ast.type import Type
from ..ast.declaration import Declaration
from ..ast.variable import Variable

from ..symbol_table.symboltable import SymbolTable, Symbol



class SymbolTableVisitor(Visitor):
    def __init__(self):
        super().__init__()
        # Initialize the root symbol table with the global scope
        self.root_symbol_table = SymbolTable(scope_name="global", scope_level=0)
        # The current_scope starts as the root symbol table and will change as we enter/exit scopes
        self.current_scope = self.root_symbol_table

    def enter_scope(self, scope_name, node=None):
        self.current_scope = self.current_scope.enter_new_scope(scope_name)
        if node is not None:
            node.symbol_table = self.current_scope

    def exit_scope(self):
        if self.current_scope.parent is not None:
            self.current_scope = self.current_scope.parent

    def get_symbol_table_tree(self):
        # Return the root symbol table, which represents the complete symbol table tree
        return self.root_symbol_table

    def visit_program(self, program: Program):
        for statement in program.statements:
            self.visit_ast(statement)

    def visit_main_function(self, main_function: MainFunction):
        self.enter_scope("main_function", main_function)  # Pass the node to enter_scope
        for statement in main_function.body.statements:
            self.visit_ast(statement)
        self.exit_scope()

    def visit_compound_statement(self, compound_statement: CompoundStatement):
        self.enter_scope("compound", compound_statement)
        for statement in compound_statement.statements:
            self.visit_ast(statement)
        self.exit_scope()

    def visit_declaration(self, declaration: Declaration):
        for variable in declaration.variables:
            self.visit_ast(variable)

    def visit_type(self, type_node: Type):
        pass
    def visit_variable(self, variable: Variable):
        if self.current_scope.lookup(variable.identifier, current_scope_only=True):
            raise Exception(f"Redeclaration of variable: {variable.identifier}")

        else:
            symbol = Symbol(name=variable.identifier, type=variable.initializer, scope_level=self.current_scope.scope_level)
            self.current_scope.insert(variable.identifier, symbol)

    def visit_cast_expression(self, cast_expression: CastExpression):
        self.visit(cast_expression.expr)

    def visit_binary_arithmetic(self, expr: EXPR.BinaryArithmetic):
        self.visit_ast(expr.left)
        self.visit_ast(expr.right)

    def visit_binary_bitwise_arithmetic(self, expr: EXPR.BinaryBitwiseArithmetic):
        self.visit_ast(expr.left)
        self.visit_ast(expr.right)

    def visit_binary_logical_operation(self, expr: EXPR.BinaryLogicalOperation):
        self.visit_ast(expr.left)
        self.visit_ast(expr.right)

    def visit_comparison_operation(self, expr: EXPR.ComparisonOperation):
        self.visit_ast(expr.left)
        self.visit_ast(expr.right)

    def visit_unary_expression(self, expr: EXPR.UnaryExpression):
        pass
    def visit_shift_expression(self, expr: EXPR.ShiftExpression):
        self.visit_ast(expr.value)
        self.visit_ast(expr.amount)

    def visit_int(self, expr: EXPR.INT):
        pass

    def visit_float(self, expr: EXPR.FLOAT):
        pass

    def visit_char(self, expr: EXPR.CHAR):
        pass

    def visit_variable_reference(self, expr: EXPR.VariableReference):
        # Look up the variable in the current scope's symbol table to ensure it is declared
        symbol = self.current_scope.lookup(expr.identifier)
        if symbol is None:
            raise Exception(f"Undeclared variable '{expr.identifier}' referenced.")
        return symbol  # Return the symbol found for further use or validation if needed

    def visit_assignment(self, expr: EXPR.Assignment):
        # Validate the left-hand side of the assignment to ensure it's a valid variable
        lhs_symbol = self.visit_ast(expr.left)
        # Validate the right-hand side of the assignment
        rhs_value = self.visit_ast(expr.right)

        # Here you would include logic to ensure the assignment is semantically valid
        # For example, check that the rhs value is compatible with the type of lhs_symbol
        if lhs_symbol is not None and rhs_value is not None:
            if lhs_symbol.type != rhs_value.type:
                raise Exception(f"Type mismatch in assignment to '{lhs_symbol.name}'.")

