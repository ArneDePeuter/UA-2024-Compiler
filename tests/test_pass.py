from compiler.frontend import tree_from_file


def test_intliteral():
    tree_from_file("./files/proj1_man_pass_intliteral.c")


def test_operators():
    tree_from_file("./files/proj1_man_pass_operators.c")


def test_whitespace():
    tree_from_file("./files/proj1_man_pass_whitespace.c")
