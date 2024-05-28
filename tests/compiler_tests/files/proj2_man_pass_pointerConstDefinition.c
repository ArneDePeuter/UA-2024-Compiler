#include <stdio.h>

int main() {
    const int x = 98362;            // Initialize constant int x
    const int* x_ptr = &x;          // Pointer to constant int x
    const int** p = &x_ptr;         // Pointer to pointer to constant int x
    const int* z = &x;              // Another pointer to constant int x

    const float a = 856.25668;      // Initialize constant float a
    const float* a_ptr = &a;        // Pointer to constant float a

    // Print the values and addresses
    printf("Value of x: %d\n", x);
    printf("Address of x: %p\n", (void*)&x);
    printf("Value pointed to by x_ptr: %d\n", *x_ptr);
    printf("Address stored in x_ptr: %p\n", (void*)x_ptr);
    printf("Value pointed to by p (which is x_ptr): %p\n", (void*)*p);
    printf("Value pointed to by z: %d\n", *z);

    printf("Value of a: %f\n", a);
    printf("Address of a: %p\n", (void*)&a);
    printf("Value pointed to by a_ptr: %f\n", *a_ptr);
    printf("Address stored in a_ptr: %p\n", (void*)a_ptr);

    return 0;
}
