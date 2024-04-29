
#include <stdio.h>

int main() {
    int f[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    printf("%d\n", f[1][1]);  // Print middle element to ensure array initialization
    return 0;
}
