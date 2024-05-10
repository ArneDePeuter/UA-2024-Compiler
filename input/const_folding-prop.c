#include <stdio.h>

int main() {
    // More complex constant folding example
    const int a = (2 + 3) * (4 << 1) + 1; // (5 * 8) + 1 = 41 computed at compile time

    // Constant propagation example
    int b = a; // 'b' is initialized with the constant value of 'a'

    // Using the constants
    printf("The value of 'a' after more complex constant folding: %d\n", a);
    printf("The value of 'b' after constant propagation from 'a': %d\n", b);

    // Further complex constant folding
    const int c = (a * 20) / 2;  // Calculation is done at compile time
    printf("The value of 'c' after further complex constant folding: %d\n", c);

    return 0;
}
