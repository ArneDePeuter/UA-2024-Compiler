import os

from compiler.frontend import tree_from_file, tree_to_ast
from compiler.core.errors.warning_error import WarningError

warning_dict = {
    "proj2_opt_pass_constPointerToNonConstPointer1.c": WarningError("Initializing Type(line=2, position=15, base_type=<BaseType.char: 'char'>, const=False, address_qualifiers=[]) with Type(line=2, position=0, base_type=<BaseType.char: 'char'>, const=True, address_qualifiers=[]) discard the const qualifier.", 2, 0),
    "proj2_opt_pass_constPointerToNonConstPointer1.c": WarningError("Initializing Type(line=3, position=0, base_type=<BaseType.char: 'char'>, const=True, address_qualifiers=[<AddressQualifier.pointer: '*'>]) with Type(line=4, position=0, base_type=<BaseType.char: 'char'>, const=False, address_qualifiers=[<AddressQualifier.pointer: '*'>]) discard the const qualifier.", 4, 0),
    "proj2_opt_pass_constPointerToNonConstPointer2.c": WarningError("Initializing Type(line=2, position=16, base_type=<BaseType.float: 'float'>, const=False, address_qualifiers=[]) with Type(line=2, position=0, base_type=<BaseType.float: 'float'>, const=True, address_qualifiers=[]) discard the const qualifier.", 2, 0),
    "proj2_opt_pass_constPointerToNonConstPointer2.c": WarningError("Initializing Type(line=3, position=0, base_type=<BaseType.float: 'float'>, const=True, address_qualifiers=[<AddressQualifier.pointer: '*'>]) with Type(line=4, position=0, base_type=<BaseType.float: 'float'>, const=False, address_qualifiers=[<AddressQualifier.pointer: '*'>]) discard the const qualifier", 3, 0)
}

def test_pass() -> None:
    directory = os.fsencode("./files/pass")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(f"Testing {filename}")

        tree = tree_from_file(f"{directory.decode()}/{filename}")
        ast = tree_to_ast(tree)

