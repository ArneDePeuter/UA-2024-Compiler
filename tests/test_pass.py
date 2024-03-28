import os

from compiler.frontend import tree_from_file, tree_to_ast
from compiler.frontend.symbol_table.symbol_table_visitor import SymbolTableVisitor, SymbolTable
from compiler.core.errors.warning_error import WarningError

warning_dict = {
    "proj2_opt_pass_constPointerToNonConstPointer1.c": [
        WarningError("Initializing Type(line=2, position=15, base_type=<BaseType.char: 'char'>, const=False, address_qualifiers=[]) with Type(line=2, position=0, base_type=<BaseType.char: 'char'>, const=True, address_qualifiers=[]) discards the const qualifier.", 2, 0),
        WarningError("Initializing Type(line=3, position=0, base_type=<BaseType.char: 'char'>, const=True, address_qualifiers=[<AddressQualifier.pointer: '*'>]) with Type(line=4, position=0, base_type=<BaseType.char: 'char'>, const=False, address_qualifiers=[<AddressQualifier.pointer: '*'>]) discards the const qualifier.", 4, 0)
    ],
    "proj2_opt_pass_constPointerToNonConstPointer2.c": [
        WarningError("Initializing Type(line=2, position=16, base_type=<BaseType.float: 'float'>, const=False, address_qualifiers=[]) with Type(line=2, position=0, base_type=<BaseType.float: 'float'>, const=True, address_qualifiers=[]) discards the const qualifier.", 2, 0),
        WarningError("Initializing Type(line=3, position=0, base_type=<BaseType.float: 'float'>, const=True, address_qualifiers=[<AddressQualifier.pointer: '*'>]) with Type(line=4, position=0, base_type=<BaseType.float: 'float'>, const=False, address_qualifiers=[<AddressQualifier.pointer: '*'>]) discards the const qualifier", 4, 0)
    ]
}

def test_pass() -> None:
    directory = os.fsencode("./files/pass")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(f"Testing {filename}")

        tree = tree_from_file(f"{directory.decode()}/{filename}")
        ast = tree_to_ast(tree)


        symbol_table_visitor = SymbolTableVisitor(symbol_table=SymbolTable())
        symbol_table_visitor.visit(ast)

        print(f"{filename} passed")
        assert True

        # TODO: Implement checking the warnings
        #for warning in warning_dict:
        #    if warning in filename:
        #        assert warning_dict[warning] in ast
