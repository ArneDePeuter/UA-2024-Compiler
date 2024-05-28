#include <stdio.h>

int main() {
    int x = 5;
    printf("Initial x: %d\n", x);

    x--; // Post-decrement: x becomes 4
    printf("After x--: %d\n", x);

    int z = x--; // Post-decrement: z is assigned 4, then x becomes 3
    printf("After int z = x--: x = %d, z = %d\n", x, z);

    x = x-- + z--; // Complex expression:
                   // 1. Evaluate x-- (x is 3, then decremented to 2)
                   // 2. Evaluate z-- (z is 4, then decremented to 3)
                   // 3. x is assigned the result of 3 + 4 = 7
    printf("After x = x-- + z--: x = %d, z = %d\n", x, z);

    --x; // Pre-decrement: x becomes 6
    printf("After --x: x = %d\n", x);

    return 0;
}
