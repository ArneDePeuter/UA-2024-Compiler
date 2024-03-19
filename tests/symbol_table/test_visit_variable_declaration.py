from compiler.frontend.symbol_table.symbol_table_visitor import SymbolTableVisitor, SemanticError
from compiler.frontend.symbol_table.symboltable import SymbolTable
from compiler.core import ast


def test_1():
    # int a = 5;
    variable_declaration = ast.VariableDeclaration(
        var_type=ast.Type(
            base_type=ast.BaseType.int,
        ),
        qualifiers=[
            ast.VariableDeclarationQualifier(
                identifier="a",
                initializer=ast.INT(value=5)
            )
        ]
    )

    visitor = SymbolTableVisitor()
    visitor.visit_variable_declaration(variable_declaration)
    symbol = visitor.symbol_table.lookup("a")

    assert symbol is not None
    assert symbol.name == "a"
    assert symbol.type == ast.Type(base_type=ast.BaseType.int)
    assert symbol.scope_level == 0


def test_2():
    # const int a = 5;
    variable_declaration = ast.VariableDeclaration(
        var_type=ast.Type(
            base_type=ast.BaseType.int,
            const=True
        ),
        qualifiers=[
            ast.VariableDeclarationQualifier(
                identifier="a",
                initializer=ast.INT(value=5)
            )
        ]
    )

    visitor = SymbolTableVisitor()
    visitor.visit_variable_declaration(variable_declaration)
    symbol = visitor.symbol_table.lookup("a")

    assert symbol is not None
    assert symbol.name == "a"
    assert symbol.type == ast.Type(base_type=ast.BaseType.int, const=True)
    assert symbol.scope_level == 0


def test_symbol_present():
    # const int a = 5;
    variable_declaration = ast.VariableDeclaration(
        var_type=ast.Type(
            base_type=ast.BaseType.int,
            const=True
        ),
        qualifiers=[
            ast.VariableDeclarationQualifier(
                identifier="a",
                initializer=ast.INT(value=5)
            )
        ]
    )

    visitor = SymbolTableVisitor()
    visitor.visit_variable_declaration(variable_declaration)
    try:
        visitor.visit_variable_declaration(variable_declaration)
    except SemanticError:
        ...
    else:
        assert False


