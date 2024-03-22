import os

from compiler.frontend import tree_from_file
from compiler.core.errors.semantic_error import SemanticError

error_dict = {
    "proj2_man_semanticErr_constAssignment.c": SemanticError("Cannot assign to const variable 'x'", 4, 0),
    "proj2_man_semanticErr_constPointerRessignment.c": SemanticError("Cannot assign to const variable 'x_ptr'", 7, 0),
    "proj2_man_semanticErr_incompatibleTypes1.c": SemanticError("Incompatible types for variable 'x_ptr': Type(line=8, position=14, base_type=<BaseType.int: 'int'>, const=False, address_qualifiers={<AddressQualifier.pointer: '*'>}) and Type(line=8, position=0, base_type=<BaseType.int: 'int'>, const=False, address_qualifiers=[<AddressQualifier.pointer: '*'>, <AddressQualifier.pointer: '*'>])", 8, 0)
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