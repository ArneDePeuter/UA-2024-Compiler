#include <stdio.h>

int main() {
    char c = 'A';
    char *p = &c;
    (*p)++; // Increment the character 'A' to 'B'
    printf("%c", *p);
}
