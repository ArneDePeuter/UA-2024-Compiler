#include <stdio.h>

int add (int a, int b) {
    return a + b;
}

int main () {
    int b = 'c';
    int c = 2;
    char d = add(b, c);
    printf("%c", d);
    return 0;
}

