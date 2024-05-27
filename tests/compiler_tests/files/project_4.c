#include <stdio.h>

/*
 Conditional statements: if and else must be supported. You can assume that curly braces are required.
 Loops. You have to implement while, for, break, and continue.
 Scopes: anonymous, if-else, for, while.
 Switch statements: switch, break, case.
 Your compiler should support enumerations.
 else if statements.
*/

int main() {
    // Conditional statements: if and else must be supported. You can assume that curly braces are required.
    int x = 5;
    if (x == 5) {
        printf("x is 5\n");
    } else {
        printf("x is not 5\n");
    }

    // Loops. You have to implement while, for, break, and continue.
    // while loop
    int i = 0;
    while (i < 5) {
        printf("%d\n", i);
        i++;
    }

    // for loop
    for (int j = 0; j < 5; j++) {
        printf("%d\n", j);
    }

    // break
    for (int k = 0; k < 5; k++) {
        if (k == 3) {
            break;
        }
        printf("%d\n", k);
    }

    // continue
    for (int l = 0; l < 5; l++) {
        if (l == 3) {
            continue;
        }
        printf("%d\n", l);
    }

    // Scopes: anonymous, if-else, for, while.
    {
        int new_x = 5;
        printf("%d\n", new_x);
    }
    int new_x = 10; // redeclare but not in the same scope

    // switch statements: switch, break, case.
    int switch_x = 5;

    switch (switch_x) {
        case 1:
            printf("switch_x is 1\n");
            break;
        case 2:
            printf("switch_x is 2\n");
            break;
        case 3:
            printf("switch_x is 3\n");
            break;
        default:
            printf("switch_x is not 1, 2, or 3\n");
    }

    // Your compiler should support enumerations.
    enum colors {RED, GREEN, BLUE};
    enum colors my_color = RED;
    switch (my_color) {
        case RED:
            printf("my_color is RED\n");
            break;
        case GREEN:
            printf("my_color is GREEN\n");
            break;
        case BLUE:
            printf("my_color is BLUE\n");
            break;
    }

    // else if statements.
    int else_if_x = 5;
    if (else_if_x == 1) {
        printf("else_if_x is 1\n");
    } else if (else_if_x == 2) {
        printf("else_if_x is 2\n");
    } else if (else_if_x == 3) {
        printf("else_if_x is 3\n");
    } else {
        printf("else_if_x is not 1, 2, or 3\n");
    }

    // Nested if-else
    int nested_x = 5;
    if (nested_x == 5) {
        if (nested_x == 5) {
            printf("nested_x is 5\n");
        } else {
            printf("nested_x is not 5\n");
        }
    } else {
        printf("nested_x is not 5\n");
    }

    return 0;
}