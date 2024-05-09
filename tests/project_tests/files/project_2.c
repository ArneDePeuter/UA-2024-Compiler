#include <stdio.h>

/*
 Main function: Add an int main() { ... } function.
 Reserved keywords: const, char, int, and float.
 Literals: float, integer, character (scientific notation not necessary).
 Variable handling: declarations, definitions, assignments, identifiers in expressions.
 Pointers: declaration, definition, operators * (dereference) and & (address).
 Const variables. For pointers, only “pointer to const” needs to be supported. The type is const int*. This means the value pointed to is const. The variable itself can be re-assigned with a different address.
 Implicit conversions. We consider the order float isRicherThan int isRicherThan char. Pay attention to warnings.
 Explicit conversions (i.e., the cast operator). Any conversion done this way should not cause a warning.
 Pointer arithmetic (all of the following need to be implemented):
 Assignment: p = 0,
 Addition and subtraction: p + q, p + 2, q - 5, etc. Take the size of the datatype into account!
 Increment, decrement: p++, q--, etc.
 Comparison: p < end,p >= 0,p == 0,etc.
 Note that this is only relevant for arrays.
 Increment/Decrement Operations: i++, i--. Both suﬀix and prefix variants.
*/

// main function
int main() {
    // Reserved keywords: const, char, int, and float.
    const char c = 'a';
    printf("%c\n", c);
    const int i = 5;
    printf("%d\n", i);
    const float f = 5.0;
    printf("%f\n", f);
    // Literals: float, integer, character (scientific notation not necessary).
    float f1 = 5.0;
    printf("%f\n", f1);
    int i1 = 5;
    printf("%d\n", i1);
    char c1 = 'a';
    printf("%c\n", c1);
    // Variable handling: declarations, definitions, assignments, identifiers in expressions.
    int x = 5;
    printf("%d\n", x);
    int y = x + 3;
    printf("%d\n", y);
    // Pointers: declaration, definition, operators * (dereference) and & (address).
    int *p = &x;
    printf("%d\n", *p);
    int *q = p;
    printf("%d\n", *q);
    // Const variables. For pointers, only “pointer to const” needs to be supported. The type is const int*. This means the value pointed to is const. The variable itself can be re-assigned with a different address.
    const int *cp = &x;
    printf("%d\n", *cp);
    // Implicit conversions. We consider the order float isRicherThan int isRicherThan char. Pay attention to warnings.
    float f2 = 5;
    printf("%f\n", f2);
    int i2 = 5.0;
    printf("%d\n", i2);
    char c2 = 5;
    printf("%c\n", c2);
    // Explicit conversions (i.e., the cast operator). Any conversion done this way should not cause a warning.
    int i3 = (int) 5.0;
    printf("%d\n", i3);
    float f3 = (float) 5;
    printf("%f\n", f3);
    char c3 = (char) 5;
    printf("%c\n", c3);
    // Pointer arithmetic (all of the following need to be implemented):
    // Assignment: p = 0,
    p = 0;
    // Addition and subtraction: p + q, p + 2, q - 5, etc. Take the size of the datatype into account!
    p = p + 1;
    p = p - 1;
    // Increment, decrement: p++, q--, etc.
    p++;
    q--;
    // Comparison: p < end,p >= 0,p == 0,etc.
    if (p < q) {
        printf("p < q\n");
    }
    if (p >= q) {
        printf("p >= q\n");
    }
    if (p == q) {
        printf("p == q\n");
    }
    // Increment/Decrement Operations: i++, i--. Both suﬀix and prefix variants.
    int i4 = 5;
    printf("%d\n", i4++);
    printf("%d\n", i4);
    printf("%d\n", ++i4);
    printf("%d\n", i4);
    printf("%d\n", i4--);
    printf("%d\n", i4);
    printf("%d\n", --i4);
    printf("%d\n", i4);
}