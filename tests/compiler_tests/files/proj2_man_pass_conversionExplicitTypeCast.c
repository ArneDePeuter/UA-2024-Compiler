#include <stdio.h>

int main() {
    int x = 5;
    float f = 33989.586265;

    int z = (int) f;           // Convert float to int, truncating the decimal part
    float z2 = (float) x;      // Convert int to float

    int a = (int) (f + z2 * 2); // Perform arithmetic and convert the result to int

    float f2 = f;               // Copy float value (explicit cast not needed here)
    f2 = (float) (a + z2 / (3 * 65232)); // Perform arithmetic and convert the result to float

    // Print the results to verify the operations
    printf("x: %d\n", x);
    printf("f: %f\n", f);
    printf("z: %d\n", z);
    printf("z2: %f\n", z2);
    printf("a: %d\n", a);
    printf("f2: %f\n", f2);

    return 0;
}
