#include <stdio.h>

void modifyValue(int *ptr) {
    *ptr = 20;
}

int main() {
    int x = 10;
    const int *const_ptr = &x;

    // Cast away const-ness
    modifyValue((int *)const_ptr);

    printf("Value of x after modification: %d\n", x);

    return 0;
}
