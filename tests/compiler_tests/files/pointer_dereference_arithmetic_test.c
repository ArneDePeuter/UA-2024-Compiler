#include <stdio.h>

int main() {
    char c = 1; // Starting with a numeric value rather than a character for arithmetic purposes
    char *p = &c;
    *p = *p + 5; // Increment the value by 5
    printf("%d", *p);
}
