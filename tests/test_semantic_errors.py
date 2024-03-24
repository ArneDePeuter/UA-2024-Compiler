import os

from compiler.frontend import tree_from_file
from compiler.core.errors.semantic_error import SemanticError

error_dict = {
    "proj2_man_semanticErr_constAssignment.c": SemanticError("Cannot assign to const variable 'x'", 4, 0),
    "proj2_man_semanticErr_constPointerRessignment.c": SemanticError("Cannot assign to const variable 'x_ptr'", 7, 0),
    "proj2_man_semanticErr_incompatibleTypes1.c": SemanticError("Incompatible types for variable 'x_ptr': Type(line=8, position=14, base_type=<BaseType.int: 'int'>, const=False, address_qualifiers={<AddressQualifier.pointer: '*'>}) and Type(line=8, position=0, base_type=<BaseType.int: 'int'>, const=False, address_qualifiers=[<AddressQualifier.pointer: '*'>, <AddressQualifier.pointer: '*'>])", 8, 0),
    "proj2_man_semanticErr_incompatibleTypes2.c": SemanticError("Incompatible types for variable 'x_ptr': Type(line=6, position=14, base_type=<BaseType.int: 'int'>, const=False, address_qualifiers={<AddressQualifier.pointer: '*'>}) and Type(line=6, position=0, base_type=<BaseType.int: 'int'>, const=False, address_qualifiers=[<AddressQualifier.pointer: '*'>, <AddressQualifier.pointer: '*'>])", 6, 0),
    "proj2_man_semanticErr_incompatibleTypes3.c": SemanticError("Incompatible types for variable 'y': Type(line=5, position=10, base_type=<BaseType.int: 'int'>, const=False, address_qualifiers={<AddressQualifier.pointer: '*'>}) and Type(line=5, position=0, base_type=<BaseType.float: 'float'>, const=False, address_qualifiers=[])", 5, 0),
    # TODO: Implement proj2_man_semanticErr_incompatibleTypes4.c
    "proj2_man_semanticErr_incompatibleTypes5.c": SemanticError("Invalid unary operation Operator.DEREFERENCE for type Type(line=3, position=0, base_type=<BaseType.int: 'int'>, const=False, address_qualifiers=[]).", 9, 4),
    "proj2_man_semanticErr_redeclaration.c": SemanticError("Variable 'x' is already declared.", 5, 0),
    "proj2_man_semanticErr_redefinition.c": SemanticError("Variable 'f' is already declared.", 4, 0), # TODO: Trow more specific error message
    # TODO: Implement proj2_man_semanticErr_rvalueAssignment1.c
    # TODO: Implement proj2_man_semanticErr_rvalueAssignment2.c
    "proj2_man_semanticErr_undeclaredVariable1.c": SemanticError("Variable 'some_variable' must have an initializer. Meaning it is undeclared.", 4, 0),
    "proj2_man_semanticErr_undeclaredVariable2.c": SemanticError("Use of undeclared variable 'x'.", 3, 0),
    "proj2_man_semanticErr_undeclaredVariable3.c": SemanticError("Use of undeclared identifier 'z'.", 2, 12)
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