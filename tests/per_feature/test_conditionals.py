from compiler.frontend import tree_from_str, tree_to_ast
from compiler.core import ast

def test_if1() -> None:
    input = """
        int main() {
            if (1) {
                int a = 5;
            }
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast, _ = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    assert len(constructed_ast.statements) == 1
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)
    if_statement = main_func.body.statements[0]
    assert isinstance(if_statement, ast.IfStatement)
    assert if_statement.condition.value == 1
    assert len(if_statement.body.statements) == 1
    declaration = if_statement.body.statements[0]
    assert isinstance(declaration, ast.VariableDeclaration)


def test_if_with_else() -> None:
    input = """
        int main() {
            if (0) {
                int b = 10;
            } else {
                int c = 20;
            }
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast, _ = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    assert len(constructed_ast.statements) == 1
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)
    assert len(main_func.body.statements) == 1

    if_statement = main_func.body.statements[0]
    assert isinstance(if_statement, ast.IfStatement)
    assert if_statement.condition.value == 0
    assert len(if_statement.body.statements) == 1
    assert isinstance(if_statement.body.statements[0], ast.VariableDeclaration)
    assert if_statement.body.statements[0].qualifiers[0].identifier == 'b'

    assert isinstance(if_statement.else_statement, ast.ElseStatement)
    assert len(if_statement.else_statement.body.statements) == 1
    assert isinstance(if_statement.else_statement.body.statements[0], ast.VariableDeclaration)
    assert if_statement.else_statement.body.statements[0].qualifiers[0].identifier == 'c'


def test_if_with_else_if() -> None:
    input = """
        int main() {
            if (0) {
                int d = 30;
            } else if (1) {
                int e = 40;
            } else {
                int f = 50;
            }
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast, _ = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    main_func = constructed_ast.statements[0]
    if_statement = main_func.body.statements[0]
    assert isinstance(if_statement, ast.IfStatement)
    assert if_statement.condition.value == 0
    assert len(if_statement.else_statement.body.statements) == 1

    assert isinstance(if_statement.else_statement, ast.IfStatement)
    else_if_statement = if_statement.else_statement
    assert else_if_statement.condition.value == 1
    assert len(else_if_statement.body.statements) == 1
    assert else_if_statement.body.statements[0].qualifiers[0].identifier == 'e'

    assert isinstance(else_if_statement.else_statement, ast.ElseStatement)
    assert else_if_statement.else_statement.body.statements[0].qualifiers[0].identifier == 'f'

def test_switch_1():
    input = """
        int main() {
            int x = 3;
            switch (x) {
                case 1:
                    printf("%d", x);
                    break;
                case 2:
                    printf("%d", x);
                    break;
                default:
                    printf("%d", x);
            }
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast, _ = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)
    assert len(main_func.body.statements) == 2
    switch_statement = main_func.body.statements[1]
    assert isinstance(switch_statement, ast.Body)
    case_1 = switch_statement.statements[0]
    assert isinstance(case_1, ast.IfStatement)
    # Condition
    assert case_1.condition.operator == ast.ComparisonOperation.Operator.EQ
    assert case_1.condition.left.name == 'x'
    assert case_1.condition.right.value == 1
    # Body
    assert len(case_1.body.statements) == 1 # Break statement should be gone
    printf_call = case_1.body.statements[0]
    assert isinstance(printf_call, ast.ExpressionStatement)
    assert isinstance(printf_call.expression, ast.PrintFCall)
    # Next case
    case_2 = case_1.else_statement
    assert isinstance(case_2, ast.IfStatement)
    # Condition
    assert case_2.condition.operator == ast.ComparisonOperation.Operator.EQ
    assert case_2.condition.left.name == 'x'
    assert case_2.condition.right.value == 2
    # Body
    assert len(case_2.body.statements) == 1 # Break statement should be gone
    printf_call = case_2.body.statements[0]
    assert isinstance(printf_call, ast.ExpressionStatement)
    assert isinstance(printf_call.expression, ast.PrintFCall)
    # Default case
    default_case = case_2.else_statement
    assert isinstance(default_case, ast.ElseStatement)
    assert len(default_case.body.statements) == 1
    printf_call = default_case.body.statements[0]
    assert isinstance(printf_call, ast.ExpressionStatement)
    assert isinstance(printf_call.expression, ast.PrintFCall)

def test_switch_2():
    input = """
        int main() {
            int x = 3;
            switch (x) {
                case 1:
                    printf("%d", x);
                case 2:
                    printf("%d", x);
                    break;
                default:
                    printf("%d", x);
            }
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast, _ = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)
    assert len(main_func.body.statements) == 2
    switch_statement = main_func.body.statements[1]
    assert isinstance(switch_statement, ast.Body)
    assert len(switch_statement.statements) == 2 # 2 if statements, since the frist case doesn't have a break
    case_1 = switch_statement.statements[0]
    assert isinstance(case_1, ast.IfStatement)
    # Condition
    assert case_1.condition.operator == ast.ComparisonOperation.Operator.EQ
    assert case_1.condition.left.name == 'x'
    assert case_1.condition.right.value == 1
    # Body
    assert len(case_1.body.statements) == 1 # No break statement
    printf_call = case_1.body.statements[0]
    assert isinstance(printf_call, ast.ExpressionStatement)
    assert isinstance(printf_call.expression, ast.PrintFCall)
    assert case_1.else_statement is None # No else statement
    # Next case
    case_2 = switch_statement.statements[1]
    assert isinstance(case_2, ast.IfStatement)
    # Condition
    assert case_2.condition.operator == ast.ComparisonOperation.Operator.EQ
    assert case_2.condition.left.name == 'x'
    assert case_2.condition.right.value == 2
    # Body
    assert len(case_2.body.statements) == 1 # Break statement should be gone
    printf_call = case_2.body.statements[0]
    assert isinstance(printf_call, ast.ExpressionStatement)
    assert isinstance(printf_call.expression, ast.PrintFCall)
    # Default case
    default_case = case_2.else_statement
    assert isinstance(default_case, ast.ElseStatement)
    assert len(default_case.body.statements) == 1
    printf_call = default_case.body.statements[0]
    assert isinstance(printf_call, ast.ExpressionStatement)
    assert isinstance(printf_call.expression, ast.PrintFCall)

def test_switch_3():
    input = """
        int main() {
            int x = 3;
            switch (x) {
                case 1:
                    printf("%d", x);
                    break;
                case 2:
                    printf("%d", x);
                case 3:
                    printf("%d", x);
                    break;
                default:
                    printf("%d", x);
            }
        }
    """

    tree, input_stream = tree_from_str(input)
    constructed_ast, _ = tree_to_ast(tree, input_stream)

    assert isinstance(constructed_ast, ast.Program)
    main_func = constructed_ast.statements[0]
    assert isinstance(main_func, ast.FunctionDeclaration)
    assert len(main_func.body.statements) == 2
    switch_statement = main_func.body.statements[1]
    assert isinstance(switch_statement, ast.Body)
    assert len(switch_statement.statements) == 2 # 2 if statements one for case 1 and 2, and one for case 3 (and default)
    case_1 = switch_statement.statements[0]
    assert isinstance(case_1, ast.IfStatement)
    # Condition
    assert case_1.condition.operator == ast.ComparisonOperation.Operator.EQ
    assert case_1.condition.left.name == 'x'
    assert case_1.condition.right.value == 1
    # Body
    assert len(case_1.body.statements) == 1 # Break statement should be gone
    printf_call = case_1.body.statements[0]
    assert isinstance(printf_call, ast.ExpressionStatement)
    assert isinstance(printf_call.expression, ast.PrintFCall)
    assert case_1.else_statement is not None

    case_2 = case_1.else_statement
    assert isinstance(case_2, ast.IfStatement)
    # Condition
    assert case_2.condition.operator == ast.ComparisonOperation.Operator.EQ
    assert case_2.condition.left.name == 'x'
    assert case_2.condition.right.value == 2
    # Body
    assert len(case_2.body.statements) == 1
    printf_call = case_2.body.statements[0]
    assert isinstance(printf_call, ast.ExpressionStatement)
    assert isinstance(printf_call.expression, ast.PrintFCall)
    assert case_2.else_statement is None # No else statement, since their is no break statement
    # Next case
    case_3 = switch_statement.statements[1]
    assert isinstance(case_3, ast.IfStatement)
    # Condition
    assert case_3.condition.operator == ast.ComparisonOperation.Operator.EQ
    assert case_3.condition.left.name == 'x'
    assert case_3.condition.right.value == 3
    # Body
    assert len(case_3.body.statements) == 1 # Break statement should be gone
    printf_call = case_3.body.statements[0]
    assert isinstance(printf_call, ast.ExpressionStatement)
    assert isinstance(printf_call.expression, ast.PrintFCall)
    # Default case
    default_case = case_3.else_statement
    assert isinstance(default_case, ast.ElseStatement)
    assert len(default_case.body.statements) == 1
    printf_call = default_case.body.statements[0]
    assert isinstance(printf_call, ast.ExpressionStatement)
    assert isinstance(printf_call.expression, ast.PrintFCall)