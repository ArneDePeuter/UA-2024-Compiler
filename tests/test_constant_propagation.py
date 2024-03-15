from compiler.core import ast
from compiler.middleend.constant_propagation_ast_visitor import ConstantPropagationAstVisitor


def test_1():
    test_ast = ast.Body([
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
                const=True
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="a",
                    initializer=ast.INT(5)
                )
            ]
        ),
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="b",
                    initializer=ast.IDENTIFIER("a")
                )
            ]
        )
    ])
    visitor = ConstantPropagationAstVisitor()

    new_ast = visitor.visit_body(test_ast)

    assert new_ast == ast.Body([
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
                const=True
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="a",
                    initializer=ast.INT(5)
                )
            ]
        ),
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="b",
                    initializer=ast.INT(5)
                )
            ]
        )
    ])


def test_2():
    test_ast = ast.Body([
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
                const=True
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="a",
                    initializer=ast.INT(5)
                )
            ]
        ),
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
                const=True
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="b",
                    initializer=ast.IDENTIFIER("a")
                )
            ]
        ),
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="b",
                    initializer=ast.IDENTIFIER("b")
                )
            ]
        )
    ])
    visitor = ConstantPropagationAstVisitor()

    new_ast = visitor.visit_body(test_ast)

    assert new_ast == ast.Body([
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
                const=True
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="a",
                    initializer=ast.INT(5)
                )
            ]
        ),
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
                const=True
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="b",
                    initializer=ast.INT(5)
                )
            ]
        ),
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="b",
                    initializer=ast.INT(5)
                )
            ]
        )
    ])


def test_3():
    test_ast = ast.Body([
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
                const=True
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="a",
                    initializer=ast.INT(5)
                )
            ]
        ),
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
                const=True
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="b",
                    initializer=ast.BinaryArithmetic(
                        left=ast.IDENTIFIER("a"),
                        operator=ast.BinaryArithmetic.Operator.PLUS,
                        right=ast.INT(6)
                    )
                )
            ]
        )
    ])
    visitor = ConstantPropagationAstVisitor()

    new_ast = visitor.visit_body(test_ast)

    assert new_ast == ast.Body([
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
                const=True
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="a",
                    initializer=ast.INT(5)
                )
            ]
        ),
        ast.VariableDeclaration(
            var_type=ast.Type(
                base_type=ast.BaseType.int,
                const=True
            ),
            qualifiers=[
                ast.VariableDeclarationQualifier(
                    identifier="b",
                    initializer=ast.BinaryArithmetic(
                        left=ast.INT(5),
                        operator=ast.BinaryArithmetic.Operator.PLUS,
                        right=ast.INT(6)
                    )
                )
            ]
        )
    ])
