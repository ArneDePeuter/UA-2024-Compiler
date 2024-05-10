#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5};
    int *ptr = numbers;  // Pointer to the first element
    printf("First element: %d\n", ptr[0]);
    printf("Third element: %d\n", ptr[2]);
    return 0;
}
