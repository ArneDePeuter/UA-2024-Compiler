#include <stdio.h>

int main () {
    int a[5];
    // printf("%d", a[0]);// undefined behavior
    a[0] = 1;
    printf("%d", a[0]);
    return 0;
}
