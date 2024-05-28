#include <stdio.h>

int main() {
    int x = 10;
    int y = 20;

    int *ptr; // Pointer definition
    ptr = &x; // Pointer assignment

    printf("Value pointed to by ptr: %d\n", *ptr);

    ptr = &y; // Reassigning pointer to a different variable
    printf("Value pointed to by ptr after reassignment: %d\n", *ptr);

    return 0;
}
