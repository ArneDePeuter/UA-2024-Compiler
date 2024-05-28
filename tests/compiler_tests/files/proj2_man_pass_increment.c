#include <stdio.h>

int main() {
    int number = -55;
    printf("Initial number: %d\n", number);

    number++; // Post-increment: number becomes -54
    printf("After number++: %d\n", number);

    number = number++; // Post-increment: number is assigned -54, then incremented to -53
    printf("After number = number++: %d\n", number);

    int n = number++; // Post-increment: n is assigned -53, then number is incremented to -52
    printf("After int n = number++: number = %d, n = %d\n", number, n);

    n = n - n++; // Complex expression:
                 // 1. Evaluate n++ (n is -53, then incremented to -52)
                 // 2. Subtract n from the old value of n
                 // 3. n = -53 - (-52) = -1
    printf("After n = n - n++: n = %d\n", n);

    ++n; // Pre-increment: n becomes 0
    printf("After ++n: n = %d\n", n);

    return 0;
}
