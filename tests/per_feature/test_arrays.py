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

    assert isinstance(constructed_ast, ast.Program)
    assert len(constructed_ast.statements) == 1
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)
    array_decl = main_func.body.statements[0]
    assert isinstance(array_decl, ast.VariableDeclaration)
    assert array_decl.c_syntax == "int a[5];"
    assert array_decl.qualifiers[0].identifier == "a"
    array_specifier = array_decl.qualifiers[0].array_specifier
    assert isinstance(array_specifier, ast.ArraySpecifier)
    assert array_specifier.size.value == 5
    assert array_decl.qualifiers[0].initializer is None
    assert array_decl.var_type.base_type == ast.BaseType.int
    array_access_1 = main_func.body.statements[1]
    assert isinstance(array_access_1, ast.AssignmentStatement)
    assert array_access_1.c_syntax == "a[0] = 1;"
    assert isinstance(array_access_1.left, ast.ArrayAccess)
    assert array_access_1.left.array_name == "a"
    assert array_access_1.left.index.value == 0
    assert array_access_1.right.value == 1
    array_access_2 = main_func.body.statements[2]
    assert isinstance(array_access_2, ast.AssignmentStatement)
    assert array_access_2.c_syntax == "a[1] = 2;"
    assert isinstance(array_access_2.left, ast.ArrayAccess)
    assert array_access_2.left.array_name == "a"
    assert array_access_2.left.index.value == 1
    assert array_access_2.right.value == 2
    array_access_3 = main_func.body.statements[3]
    assert isinstance(array_access_3, ast.AssignmentStatement)
    assert array_access_3.c_syntax == "a[2] = 3;"
    assert isinstance(array_access_3.left, ast.ArrayAccess)
    assert array_access_3.left.array_name == "a"
    assert array_access_3.left.index.value == 2
    assert array_access_3.right.value == 3
    array_access_4 = main_func.body.statements[4]
    assert isinstance(array_access_4, ast.AssignmentStatement)
    assert array_access_4.c_syntax == "a[3] = 4;"
    assert isinstance(array_access_4.left, ast.ArrayAccess)
    assert array_access_4.left.array_name == "a"
    assert array_access_4.left.index.value == 3
    assert array_access_4.right.value == 4
    array_access_5 = main_func.body.statements[5]
    assert isinstance(array_access_5, ast.AssignmentStatement)
    assert array_access_5.c_syntax == "a[4] = 5;"
    assert isinstance(array_access_5.left, ast.ArrayAccess)
    assert array_access_5.left.array_name == "a"
    assert array_access_5.left.index.value == 4
    assert array_access_5.right.value == 5

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
    array_specifier = array_decl.qualifiers[0].array_specifier
    assert isinstance(array_specifier, ast.ArraySpecifier)
    assert array_specifier.size.value == 5
    assert array_decl.qualifiers[0].initializer is not None
    array_initializer = array_decl.qualifiers[0].initializer
    assert isinstance(array_initializer, ast.ArrayInitializer)
    assert len(array_initializer.elements) == 5
    assert array_initializer.elements[0].value == 1
    assert array_initializer.elements[1].value == 2
    assert array_initializer.elements[2].value == 3
    assert array_initializer.elements[3].value == 4
    assert array_initializer.elements[4].value == 5
    assert array_decl.var_type.base_type == ast.BaseType.int

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
    array_specifier = array_decl.qualifiers[0].array_specifier
    assert array_specifier.size.value == 10
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
    array_size = array_decl.qualifiers[0].array_specifier
    assert isinstance(array_size, ast.ArraySpecifier)
    assert array_size.size.name == "size"

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
    assert len(main_func.body.statements) == 1
    for_loop = main_func.body.statements[0]
    assert isinstance(for_loop, ast.ForStatement)
    assert isinstance(for_loop.to_execute, ast.ForStatement)


