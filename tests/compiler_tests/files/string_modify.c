#include <stdio.h>

int main() {
    char str[] = "Hello, World!"; // Mutable array
    printf("%s", str);
    str[0] = 'S'; // Modify the string through the array
    printf("%s", str); // Prints "Sello, World!"
    return 0;
}