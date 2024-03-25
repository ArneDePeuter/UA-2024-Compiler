import os

from compiler.frontend import tree_from_file


def test_syntax_err() -> None:
    directory = os.fsencode("./files/syntax_err")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(f"Testing {filename}")

        try:
            tree_from_file(f"{directory.decode()}/{filename}")
        except Exception as e:
            print(f"{filename} failed")
            assert True
        else:
            print(f"{filename} passed")
            assert False