#include <stdio.h>

int main() {
    char c[2][3] = {{'a', 'b', 'c'}, {'d', 'e', 'f'}};
    printf("%c", c[0][0]);
    c[0][0] = 'x';
    printf("%c", c[0][0]);
    return 0;
}