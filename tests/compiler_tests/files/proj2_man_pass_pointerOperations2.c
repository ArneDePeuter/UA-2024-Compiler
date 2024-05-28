#include <stdio.h>

void add(int *a, int *b, int *result) {
    *result = *a + *b;
}

int main() {
    int x = 10;
    int y = 20;
    int result;

    add(&x, &y, &result);

    printf("Result of addition: %d\n", result);

    return 0;
}
