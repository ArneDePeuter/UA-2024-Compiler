#include <stdio.h>

int make_ptr_null (int* ptr) {
    *ptr = 0;
    return 0;
}

int main () {
    int a = 1;
    printf("%d", a);
    make_ptr_null(&a);
    printf("%d", a);
    return 0;
}

