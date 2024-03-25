import os

from compiler.frontend import tree_from_file, tree_to_ast


def test_pass() -> None:
    directory = os.fsencode("./files/pass")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(f"Testing {filename}")

        tree = tree_from_file(f"{directory.decode()}/{filename}")
        ast = tree_to_ast(tree)

