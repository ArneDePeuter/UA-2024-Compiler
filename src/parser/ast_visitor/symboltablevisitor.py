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
        self.current_scope = SymbolTable(scope_name="global", scope_level=0)

    def enter_scope(self, scope_name):
        self.current_scope = self.current_scope.enter_new_scope(scope_name)

    def exit_scope(self):
        if self.current_scope.parent is not None:
            self.current_scope = self.current_scope.parent

    def visit_program(self, program: Program) -> Any:
        for statement in program.statements:
            self.visit(statement)

    def visit_main_function(self, main_function: MainFunction) -> Any:
        self.enter_scope("main_function") # Main Function scope
        # Visit children nodes
        for statement in main_function.body.statements:
            self.visit(statement)
        self.exit_scope()

    def visit_compound_statement(self, compound_statement: CompoundStatement) -> Any:
        self.enter_scope("compound") # Compound statements (e.g., blocks) introduce a new scope
        # Visit children nodes
        for statement in compound_statement.statements:
            self.visit(statement)
        self.exit_scope() # Exit the scope

    def visit_declaration(self, declaration: Declaration) -> Any:
        for variable in declaration.variables:
            self.visit(variable)

    def visit_type(self, type_node: Type) -> Any:
        pass
    def visit_variable(self, variable: Variable) -> Any:
        if self.current_scope.lookup(variable.identifier, current_scope_only=True):
            raise Exception(f"Redeclaration of variable: {variable.identifier}")

        else:
            symbol = Symbol(name=variable.identifier, type=variable.type, scope_level=self.current_scope.scope_level)
            self.current_scope.insert(variable.identifier, symbol)

    def visit_cast_expression(self, cast_expression: CastExpression) -> Any:
        self.visit(cast_expression.expr)

    def visit_binary_arithmetic(self, expr: EXPR.BinaryArithmetic) -> Any:
        self.visit(expr.left)
        self.visit(expr.right)

    def visit_binary_bitwise_arithmetic(self, expr: EXPR.BinaryBitwiseArithmetic) -> Any:
        self.visit(expr.left)
        self.visit(expr.right)

    def visit_binary_logical_operation(self, expr: EXPR.BinaryLogicalOperation) -> Any:
        self.visit(expr.left)
        self.visit(expr.right)

    def visit_comparison_operation(self, expr: EXPR.ComparisonOperation) -> Any:
        self.visit(expr.left)
        self.visit(expr.right)

    def visit_unary_expression(self, expr: EXPR.UnaryExpression) -> Any:
        self.visit(expr.expr)

    def visit_shift_expression(self, expr: EXPR.ShiftExpression) -> Any:
        self.visit(expr.left)
        self.visit(expr.right)

    def visit_int(self, expr: EXPR.INT) -> Any:
        pass


