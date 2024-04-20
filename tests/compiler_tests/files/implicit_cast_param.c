#include <stdio.h>

int add (int a, int b) {
    return a + b;
}

int main () {
    int b = 'c';
    int c = 2;
    int d = add(b, c);
    printf("%d", d);
    return 0;
}

