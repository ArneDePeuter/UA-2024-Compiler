import os

from compiler.frontend import tree_from_file


def test_syntax_err() -> None:
    directory = os.fsencode("./files")

    for file in os.listdir(directory):
        file_str = file.decode("utf-8")
        str_list = file_str.split("_")
        if (str_list[2] != "syntaxErr"):
            continue

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
