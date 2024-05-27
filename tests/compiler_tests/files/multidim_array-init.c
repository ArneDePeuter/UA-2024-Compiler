#include <stdio.h>

int main() {
    char c[2][3] = {{'a', 'b', 'c'}, {'d', 'e', 'f'}};
    printf("%c", c[0][0]);
    printf("%c", c[0][1]);
    printf("%c", c[0][2]);
    printf("%c", c[1][0]);
    printf("%c", c[1][1]);
    printf("%c", c[1][2]);
    return 0;
}