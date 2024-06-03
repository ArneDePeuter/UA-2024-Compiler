#include <stdio.h>

int main() {
    int f[10][10];
    f[0][0] = 1;
    printf("%d\n", f[0][0]);
    printf("%d\n", f[0][1]);
    printf("%d\n", f[3+3][5+3]);
    return 0;
}