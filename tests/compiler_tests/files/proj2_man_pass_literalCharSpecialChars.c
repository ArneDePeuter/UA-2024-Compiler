#include <stdio.h>

int main() {
    char nl = '\n';            // Initialize char nl with newline character
    char tab = '\t';           // Initialize char tab with tab character
    char character_null = '\0'; // Initialize char character_null with null character

    // Print statements demonstrating the special characters
    printf("This is a newline character:%c", nl);
    printf("This is a tab character:%cafter tab\n", tab);
    printf("This string ends with a null character here%cafter null\n", character_null);
    printf("ASCII value of newline: %d\n", nl);
    printf("ASCII value of tab: %d\n", tab);
    printf("ASCII value of null character: %d\n", character_null);

    return 0;
}
