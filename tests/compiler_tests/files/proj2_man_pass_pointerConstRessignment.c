#include <stdio.h>

void changeValue(const int *ptr) {
    // This function will attempt to change the value of the constant pointer
    // const int* ptr means the value pointed to by ptr is constant and cannot be modified.
    // *ptr = 20; // This line would cause a compile error
}

int main() {
    const int x = 10;
    int y = 20;

    // const int* ptr means ptr is a pointer to a constant int
    const int *ptr = &x;

    printf("Before changing value: %d\n", *ptr);

    changeValue(ptr);

    printf("After attempting to change value: %d\n", *ptr);

    return 0;
}
