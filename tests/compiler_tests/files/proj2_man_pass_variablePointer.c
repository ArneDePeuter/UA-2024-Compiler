#include <stdio.h>

int main() {
    int x = 10;
    int *ptr = &x; // Pointer to int

    printf("Value of x: %d\n", x);
    printf("Value pointed to by ptr: %d\n", *ptr);

    *ptr = 20; // Changing the value of x through the pointer

    printf("New value of x: %d\n", x);
    printf("New value pointed to by ptr: %d\n", *ptr);

    return 0;
}
