import os

from compiler.frontend import tree_from_file, tree_to_ast
from compiler.frontend.symbol_table.symbol_table_visitor import SymbolTableVisitor, SymbolTable
from compiler.core.errors.semantic_error import SemanticError
from compiler.core.errors.compiler_syntaxerror import CompilerSyntaxError
import pytest

error_dict = {
    "proj2_man_semanticErr_constAssignment.c": SemanticError("Cannot assign to a const variable.", 4, 0),
    "proj2_man_semanticErr_constPointerRessignment.c": SemanticError("Cannot assign to a const variable.", 7, 0),
    "proj2_man_semanticErr_incompatibleTypes1.c": SemanticError("Type mismatch in assignment: int** and int*.", 9, 0),
    "proj2_man_semanticErr_incompatibleTypes2.c": SemanticError("Incompatible types for variable 'x_ptr': int** and int*.", 6, 0),
    "proj2_man_semanticErr_incompatibleTypes3.c": SemanticError("Incompatible types for variable 'y': float and int*.", 5, 0),
    "proj2_man_semanticErr_incompatibleTypes4.c": SemanticError("Type mismatch in binary operation: float* and int*.", 7, 18),
    "proj2_man_semanticErr_incompatibleTypes5.c": SemanticError("Cannot dereference a non pointer type: int.", 9, 4),
    "proj2_man_semanticErr_redeclaration.c": SemanticError("Variable 'x' is already declared.", 5, 0),
    "proj2_man_semanticErr_redefinition.c": SemanticError("Variable 'f' is already defined.", 4, 0),
    "proj2_man_semanticErr_rvalueAssignment1.c": SemanticError("Cannot assign to an expression.", 4, 0),
    "proj2_man_semanticErr_rvalueAssignment2.c": SemanticError("Cannot assign to an expression.", 4, 0),
    "proj2_man_semanticErr_undeclaredVariable1.c": SemanticError("Undefined identifier 'x'.", 6, 16),
    "proj2_man_semanticErr_undeclaredVariable2.c": SemanticError("Undefined identifier 'x'.", 3, 0),
    "proj2_man_semanticErr_undeclaredVariable3.c": SemanticError("Undefined identifier 'z'.", 2, 12),
    "proj3_man_semanticErr_typedef.c": CompilerSyntaxError("mismatched input 'int' expecting ID", 4, 14),
    "proj4_man_semanticErr_switch_var_decl.c": SemanticError("Undefined identifier 'b'.", 8, 4),
    "proj_5_no_main.c": SemanticError("main function is undefined", 0, 0),
    "proj_5_faulty_main.c": SemanticError("Return type of main is invalid", 1, 0),
    "proj_5_invalid_return.c": SemanticError("Type mismatch in return statement: int* and int.", 4, 4),
    "proj_5_double_declare.c": SemanticError("Function 'fib' is already defined.", 7, 0),
    "proj_5_forward_declare.c": None,
    "proj_5_return_outside_function.c": SemanticError("Return statement outside of function", 3, 0),
    "proj_5_define_void.c": SemanticError("Cannot declare a variable of type void.", 2, 4),
    "proj_5_define_void_ptr.c": None,
    "proj_5_assign_void_ptr.c": SemanticError("Type mismatch in assignment: void* and int.", 3, 4),
    "proj_5_void_func_addition.c": SemanticError("Cannot perform arithmetic operations on void type.", 5, 12),
    "proj_5_variable_call.c": SemanticError("'a' called but it is not a function", 5, 11),
    "proj_5_nested_function_declaration.c": SemanticError("Function definition is not allowed here", 4, 4),
    "proj6_man_semanticError_arrayTypeChecking.c": SemanticError("Array 'a' must be initialized with elements of type int.", 2, 4),
    "proj6_man_semanticError_array-length.c": SemanticError("Array 'a' must be initialized with [2] elements.", 2, 4),
    "proj6_man_semanticError_array-length-multi.c": SemanticError("Array initializer elements must all be of the same length.", 2, 18),
}


@pytest.mark.parametrize("input_file", os.listdir("./tests/semantic_errors/files"))
def test_semantic_err(input_file) -> None:
    expected = error_dict.get(input_file)

    try:
        tree, input_stream = tree_from_file(f"./files/{input_file}")
        ast = tree_to_ast(tree, input_stream)

        symbol_table_visitor = SymbolTableVisitor(symbol_table=SymbolTable())
        symbol_table_visitor.visit_program(ast)
    except Exception as e:
        print(e)
        assert str(expected) == str(e)
    else:
        assert expected is None