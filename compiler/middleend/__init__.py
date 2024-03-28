from compiler.core import ast
from .constant_folding_visitor import ConstantFoldingVisitor
from .constant_propagation_visitor import ConstantPropagationVisitor


def optimise_ast(input: ast.AST) -> ast.AST:
    constant_propagation = ConstantPropagationVisitor()
    folded_ast = constant_propagation.visit(input)
    constant_folding = ConstantFoldingVisitor()
    folded_ast = constant_folding.visit(folded_ast)
    return folded_ast

