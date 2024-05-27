#include <stdio.h>

/*
 Binary operations: +, -, *, and /.
 Binary operations: >, <, and ==.
 Unary operators: + and -.
 Order of operations: Parenthesis to overwrite the order of operations.
 Logical operators &&, ||, and !.
 Comparison operators: >=, <=, and !=.
 Binary operator: %.
 Shift operators: <<, >>.
 Bitwise operators: &, |, ~, and ^.
 Abstract syntax tree and visualisation
 Constant folding: (e.g., a sub-tree of the AST “3+4” gets replaced by a single node “7”)
 */

int main() {
    // Binary operations: +, -, *, / and %.
    printf("%d\n", 5 + 3);
    printf("%d\n", 5 - 3);
    printf("%d\n", 5 * 3);
    printf("%d\n", 5 / 3);
    printf("%d\n", 5 % 3);
    // Binary operations >, <, >=, <=, == and !=.
    printf("%d\n", 5 > 3);
    printf("%d\n", 5 < 3);
    printf("%d\n", 5 >= 3);
    printf("%d\n", 5 <= 3);
    printf("%d\n", 5 <= 5);
    printf("%d\n", 5 >= 5);
    printf("%d\n", 5 == 3);
    printf("%d\n", 5 != 3);
    // Order of operations
    printf("%d\n", 5 + 3 * 2);
    printf("%d\n", (5 + 3) * 2);
    printf("%d\n", 5 + 3 / 2);
    printf("%d\n", (5 + 3) / 2);
    // Logical operations: &&, ||, and !.
    printf("%d\n", 5 > 3 && 5 < 3);
    printf("%d\n", 5 > 3 || 5 < 3);
    printf("%d\n", !(5 > 3));
    // Shift operations: << and >>.
    printf("%d\n", 5 << 1);
    printf("%d\n", 5 >> 1);
    // Bitwise operations: &, |, ^, and ~.
    printf("%d\n", 5 & 3);
    printf("%d\n", 5 | 3);
    printf("%d\n", 5 ^ 3);
    printf("%d\n", ~5);
    return 0;
}
