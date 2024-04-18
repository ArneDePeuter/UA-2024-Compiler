#include <stdio.h>

typedef int bool;

int main() {
    bool b = 0;
    b = 1;
    bool* b_ptr = &b;
    *b_ptr = 0;
    printf("%d", b);
}

