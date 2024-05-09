#include <stdio.h>

int main() {
    int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
    printf("%d", a[1][2]);
    a[1][2] = 7;
    printf("%d", a[1][2]);
    return 0;
}