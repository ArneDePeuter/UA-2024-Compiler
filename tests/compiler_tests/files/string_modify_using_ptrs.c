#include <stdio.h>

int main() {
    char str[] = "Hello, World!"; // Mutable array
    char *ptr = str; // Decay array to pointer
    printf("%s", ptr);
    ptr[7] = 'P'; // Modify the string through the pointer
    printf("%s", ptr); // Prints "Hello, Porld!"
    return 0;
}