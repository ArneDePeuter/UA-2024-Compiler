from compiler.core import ast
from .constant_folding_ast_visitor import ConstantFoldingASTVisitor


def optimise_ast(input: ast.AST) -> ast.AST:
    constant_folding = ConstantFoldingASTVisitor()
    folded_ast = constant_folding.visit_ast(input)
    return folded_ast

