#include <stdio.h>

void modifyValue(int *ptr) {
    *ptr = 20;
}

int main() {
    int x = 10;
    const int *const_ptr = &x;

    // Cast away const-ness using a temporary pointer
    int *temp_ptr = (int *)const_ptr;
    modifyValue(temp_ptr);

    printf("Value of x after modification: %d\n", x);

    return 0;
}
