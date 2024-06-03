#include <stdio.h>

int main() {
    int num = 255;
    float pi = 3.14159;
    char ch = 'A';
    char* str = "Hello, World!";

    // Print integer in decimal and hexadecimal format
    printf("Decimal: %d\n", num);
    printf("Hexadecimal: %x\n", num);

    // Print floating-point number
    printf("Pi: %f\n", pi);

    // Print character
    printf("Character: %c\n", ch);

    // Print string
    printf("String: %s\n", str);

    // Print percent sign
    printf("Print 100%% complete\n");

    return 0;
}