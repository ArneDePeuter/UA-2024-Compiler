#include <stdio.h>

int main() {
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

    return 0;
}