#include <stdio.h>

int main() {
    int x = 4;
    int y = 5;

    int* ptr = &x;
    printf("%d", *ptr);
    ptr++;
    ptr--;
    printf("%d", *ptr);
}
