#include <stdio.h>

typedef const int ConstInt;

int main() {
    const ConstInt* b = 0;
    printf("%x", b);
}

