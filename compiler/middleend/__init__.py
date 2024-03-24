from compiler.core import ast
from .constant_folding_visitor import ConstantFoldingVisitor
from .constant_propagation_visitor import ConstantPropagationVisitor


def optimise_ast(input: ast.AST) -> ast.AST:
    constant_folding = ConstantFoldingVisitor()
    folded_ast = constant_folding.visit_ast(input)
    return folded_ast


def constant_propagate(input: ast.Program) -> ast.AST:
    constant_folding = ConstantPropagationVisitor()
    folded_ast = constant_folding.visit_program(input)
    return folded_ast
