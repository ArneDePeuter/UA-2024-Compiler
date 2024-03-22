import os

from compiler.frontend import tree_from_file
from compiler.core.errors.semantic_error import SemanticError

error_dict = {
    "proj2_man_semanticErr_constAssignment.c": SemanticError("Cannot assign to const variable 'x'", 4, 0),
    # "proj2_man_semanticErr_constPointerRessignment.c": SemanticError()
}


def test_semantic_err() -> None:
    directory = os.fsencode("./files/semantic_err")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        try:
            tree_from_file(f"{directory.decode()}/{filename}")
        except Exception as e:
            error_dict[filename] = str(e)
        else:
            print(f"{filename} passed")
            assert False