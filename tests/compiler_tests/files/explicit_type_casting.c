#include <stdio.h>

int main() {
    // Integer to float
    int i = 10;
    float f = (float)i;
    printf("Integer %d cast to float: %f\n", i, f);

    // Float to integer
    float f2 = 3.14159;
    int i2 = (int)f2;
    printf("Float %f cast to integer: %d\n", f2, i2);

    // Integer to char
    int i3 = 65;
    char c = (char)i3;
    printf("Integer %d cast to char: %c\n", i3, c);

    // Char to integer
    char c2 = 'B';
    int i4 = (int)c2;
    printf("Char %c cast to integer: %d\n", c2, i4);

    return 0;
}
