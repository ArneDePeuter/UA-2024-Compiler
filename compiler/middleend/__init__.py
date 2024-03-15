from compiler.core import ast
from .constant_folding_ast_visitor import ConstantFoldingASTVisitor
from .constant_propagation_ast_visitor import ConstantPropagationAstVisitor


def optimise_ast(input: ast.AST) -> ast.AST:
    constant_folding = ConstantFoldingASTVisitor()
    folded_ast = constant_folding.visit_ast(input)
    return folded_ast


def constant_propagate(input: ast.Program) -> ast.AST:
    constant_folding = ConstantPropagationAstVisitor()
    folded_ast = constant_folding.visit_program(input)
    return folded_ast
