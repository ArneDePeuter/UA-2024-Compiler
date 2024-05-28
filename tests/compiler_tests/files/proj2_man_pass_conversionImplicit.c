#include <stdio.h>

int main() {
    int x = 5;                  // Initialize an integer x with value 5

    float f = x;                // Implicitly convert integer x to float and assign to f

    int z = -32682;             // Initialize an integer z with value -32682

    f = 33.0 * z + x;           // Perform arithmetic: multiply 33.0 (float) with z (int), then add x (int)
                                // The result is assigned to f (float)

    z = f * 0.7;                // Perform arithmetic: multiply f (float) by 0.7 (float)
                                // The result is implicitly converted to int and assigned to z

    int k = 'a' + 'z';          // Sum the ASCII values of characters 'a' and 'z' and assign to k

    // Print the results to verify the operations
    printf("x: %d\n", x);
    printf("f: %f\n", f);
    printf("z: %d\n", z);
    printf("k: %d\n", k);

    return 0;
}
