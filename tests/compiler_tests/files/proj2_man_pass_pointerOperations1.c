#include <stdio.h>

void increment(int *ptr) {
    (*ptr)++; // Increment the value pointed to by ptr
}

int main() {
    int x = 10;

    printf("Before increment: %d\n", x);

    increment(&x);

    printf("After increment: %d\n", x);

    return 0;
}
