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
    // continue
    for (int l = 0; l < 5; l++) {
        if (l == 3) {
            continue;
        }
        printf("%d\n", l);
    }

    return 0;
}