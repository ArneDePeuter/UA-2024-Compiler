#include <stdio.h>

int main() {
    int i;
    char c;
    float f;

    // Assign values to variables, since the default init is random using the refence compiler
    i = 5;
    c = 'a';
    f = 5.8;

    printf("%d", i);
    printf("%c", c);
    printf("%f", f);
    return 0;
}