#include <stdio.h>

// Define a new type name for an existing type using typedef
typedef unsigned long ulong;

int main() {
    ulong largeNumber = 1234567890;
    printf("The value of largeNumber is: %lu\n", largeNumber);
    return 0;
}
