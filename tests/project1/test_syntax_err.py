from src.parser.tree_creation import tree_from_file


def test_intliteralbeginwithzero():
    try:
        tree = tree_from_file("./files/proj1_man_syntaxErr_intLiteralBeginWithZero.c")
    except Exception as e:
        pass
    else:
        assert False


def test_operators():
    try:
        tree = tree_from_file("./files/proj1_man_syntaxErr_operators.c")
    except Exception as e:
        pass
    else:
        assert False
