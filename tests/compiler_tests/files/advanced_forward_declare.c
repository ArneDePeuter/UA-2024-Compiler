#include <stdio.h>

// Function declaration
void outerFunction();

int main() {
    // Calling the outer function
    outerFunction();

    return 0;
}

// Outer function definition
void outerFunction() {
    // Nested function declaration
    void innerFunction();

    printf("%c",'o');

    // Calling the inner function
    innerFunction();
}

// Inner function definition
void innerFunction() {
    printf("%c",'i');
}
