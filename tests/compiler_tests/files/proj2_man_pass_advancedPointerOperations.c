#include <stdio.h>

int main() {
    int x = 4;
    int y = 5;

    int* ptr = &x;
    ptr++;
    ptr--;

    int is_x = (ptr == &x);
    int is_y = (ptr == &y);
    is_y = (&x != ptr);

    // Output results to understand the behavior
    printf("ptr points to x: %d\n", is_x);
    printf("ptr points to y: %d\n", is_y);

    float* ptr2 = 0;

    // Output results of pointer comparisons
    printf("ptr2 >= ptr: %d\n", ptr2 >= (float*)ptr); // Need to cast ptr to float*
    printf("ptr2 <= ptr: %d\n", ptr2 <= (float*)ptr); // Need to cast ptr to float*
    printf("ptr > &x: %d\n", ptr > &x);
    printf("ptr < 32: %d\n", ptr < (int*)32); // Need to cast 32 to int* for comparison

    int num_skip_elements = 4;

    // Perform pointer arithmetic
    ptr = ptr + 4 * num_skip_elements;

    // Output the final pointer value
    printf("ptr after skipping elements: %p\n", (void*)ptr);

    return 0;
}
