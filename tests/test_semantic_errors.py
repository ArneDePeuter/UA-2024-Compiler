import os

from compiler.frontend import tree_from_file, tree_to_ast
from compiler.frontend.symbol_table.symbol_table_visitor import SymbolTableVisitor, SymbolTable
from compiler.core.errors.semantic_error import SemanticError

error_dict = {
    "proj2_man_semanticErr_constAssignment.c": None,
    "proj2_man_semanticErr_constPointerRessignment.c": None,
    "proj2_man_semanticErr_incompatibleTypes1.c": SemanticError("Type mismatch in assignment: int** and int*.", 9, 0),
    "proj2_man_semanticErr_incompatibleTypes2.c": SemanticError("Incompatible types for variable 'x_ptr': int** and int*.", 6, 0),
    "proj2_man_semanticErr_incompatibleTypes3.c": SemanticError("Incompatible types for variable 'y': float and int*.", 5, 0),
    "proj2_man_semanticErr_incompatibleTypes4.c": SemanticError("Type mismatch in binary operation: float* and int*.", 7, 18),
    "proj2_man_semanticErr_incompatibleTypes5.c": SemanticError("Type mismatch in assignment: int* and int.", 9, 0),
    "proj2_man_semanticErr_redeclaration.c": SemanticError("Variable 'x' is already declared.", 5, 0),
    "proj2_man_semanticErr_redefinition.c": SemanticError("Variable 'f' is already declared.", 4, 0), # TODO: We might find a way to split redefinition and redeclaration inside variable_declaration
    # TODO: Implement proj2_man_semanticErr_rvalueAssignment1.c
    "proj2_man_semanticErr_rvalueAssignment1.c": None,
    # TODO: Implement proj2_man_semanticErr_rvalueAssignment2.c
    "proj2_man_semanticErr_rvalueAssignment2.c": None,
    "proj2_man_semanticErr_undeclaredVariable1.c": SemanticError("Undefined identifier 'x'.", 6, 16),
    "proj2_man_semanticErr_undeclaredVariable2.c": SemanticError("Undefined identifier 'x'.", 3, 0),
    "proj2_man_semanticErr_undeclaredVariable3.c": SemanticError("Undefined identifier 'z'.", 2, 12)
}


def test_semantic_err() -> None:
    directory = os.fsencode("./files/semantic_err")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(f"Testing {filename}")

        if error_dict[filename] is None:
            print(f"{filename} to be implemented")
        else:
            try:
                tree = tree_from_file(f"{directory.decode()}/{filename}")
                ast = tree_to_ast(tree)

                symbol_table_visitor = SymbolTableVisitor(symbol_table=SymbolTable())
                symbol_table_visitor.visit(ast)
            except Exception as e:
                error_dict[filename] = str(e)
                print(f"{filename} failed")
                assert True
            else:
                print(f"{filename} passed")
                assert False