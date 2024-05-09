from compiler.frontend import tree_from_str, tree_to_ast
from compiler.core import ast


def test_array_1():
    input = """
    int main() {
        int a[5];
        a[0] = 1;
        a[1] = 2;
        a[2] = 3;
        a[3] = 4;
        a[4] = 5;
        return 0;
    }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast = tree_to_ast(tree, input_stream)

    # Assert that the AST is correctly recognized as a Program with one function
    assert isinstance(constructed_ast, ast.Program)
    assert len(constructed_ast.statements) == 1

    # Check that the first statement is a function declaration
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)

    # Verify the array declaration
    array_decl = main_func.body.statements[0]
    assert isinstance(array_decl, ast.VariableDeclaration)
    assert array_decl.c_syntax == "int a[5];"
    assert array_decl.qualifiers[0].identifier == "a"
    assert isinstance(array_decl.var_type.type, ast.ArrayType)
    assert array_decl.var_type.type.array_sizes.sizes[0].value == 5
    assert array_decl.var_type.type.element_type.type == ast.BaseType.int

    # Verify assignments to the array elements
    for i in range(5):
        array_access = main_func.body.statements[i + 1]
        assert isinstance(array_access, ast.AssignmentStatement)
        assert array_access.c_syntax == f"a[{i}] = {i + 1};"
        assert isinstance(array_access.left, ast.ArrayAccess)
        assert array_access.left.target.name == "a"
        assert array_access.left.index.value == i
        assert array_access.right.value == i + 1


def test_array_2():
    input = """
    int main() {
        int a[5] = {1, 2, 3, 4, 5};
        return 0;
    }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    assert len(constructed_ast.statements) == 1
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)
    array_decl = main_func.body.statements[0]
    assert isinstance(array_decl, ast.VariableDeclaration)
    assert array_decl.c_syntax == "int a[5] = {1, 2, 3, 4, 5};"
    assert array_decl.qualifiers[0].identifier == "a"
    array_specifier = array_decl.var_type.type.array_sizes
    assert isinstance(array_specifier, ast.ArraySpecifier)
    assert array_specifier.sizes[0].value == 5
    assert array_decl.qualifiers[0].initializer is not None
    array_initializer = array_decl.qualifiers[0].initializer
    assert isinstance(array_initializer, ast.ArrayInitializer)
    assert len(array_initializer.elements) == 5
    assert array_initializer.elements[0].value == 1
    assert array_initializer.elements[1].value == 2
    assert array_initializer.elements[2].value == 3
    assert array_initializer.elements[3].value == 4
    assert array_initializer.elements[4].value == 5
    assert array_decl.var_type.type.element_type.type == ast.BaseType.int

def test_uninitialized_array():
    input = """
    int main() {
        int b[10];
        return 0;
    }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    main_func = constructed_ast.statements[0]
    array_decl = main_func.body.statements[0]
    assert isinstance(array_decl, ast.VariableDeclaration)
    assert array_decl.c_syntax == "int b[10];"
    assert array_decl.qualifiers[0].identifier == "b"
    array_specifier = array_decl.var_type.type.array_sizes
    assert array_specifier.sizes[0].value == 10
    assert array_decl.qualifiers[0].initializer is None

def test_dynamic_sized_array():
    input = """
    int main() {
        int size = 10;
        int d[size];
        return 0;
    }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    main_func = constructed_ast.statements[0]
    size_decl = main_func.body.statements[0]
    assert isinstance(size_decl, ast.VariableDeclaration)
    assert size_decl.qualifiers[0].identifier == "size"
    array_decl = main_func.body.statements[1]
    assert isinstance(array_decl, ast.VariableDeclaration)
    assert array_decl.qualifiers[0].identifier == "d"
    array_size = array_decl.var_type.type.array_sizes
    assert isinstance(array_size, ast.ArraySpecifier)
    assert array_size.sizes[0].name == "size"

def test_multidimensional_array_access():
    input = """
    int main() {
        int f[10][10];
        for (int i = 0; i < 10; ++i) {
            for (int j = 0; j < 10; ++j) {
                f[i][j] = i + j;
            }
        }
        return 0;
    }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    main_func = constructed_ast.statements[0]
    assert len(main_func.body.statements) == 3
    array_decl = main_func.body.statements[0]
    assert isinstance(array_decl, ast.VariableDeclaration)
    assert array_decl.var_type.type.element_type.type == ast.BaseType.int
    array_specifier = array_decl.var_type.type.array_sizes
    assert len(array_specifier.sizes) == 2
    for s in array_specifier.sizes:
        assert s.value == 10
    for_loop_i = main_func.body.statements[1]
    assert isinstance(for_loop_i, ast.Body)
    while_stmt_i = for_loop_i.statements[1]
    assert isinstance(while_stmt_i, ast.WhileStatement)
    assert isinstance(while_stmt_i.to_execute, ast.Body)
    for_loop_j = while_stmt_i.to_execute.statements[0].statements[1]
    assert isinstance(for_loop_j, ast.WhileStatement)
    array_assignment = for_loop_j.to_execute.statements[0]
    assert isinstance(array_assignment, ast.AssignmentStatement)
    assert array_assignment.c_syntax == "f[i][j] = i + j;"
    assert array_assignment.left.array_name == "f"
    for s in array_assignment.left.index.sizes:
        assert s.name == "i" or "j"
    assert array_assignment.right.left.name == "i"
    assert array_assignment.right.right.name == "j"



