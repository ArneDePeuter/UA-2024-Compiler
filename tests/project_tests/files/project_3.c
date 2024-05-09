#include <stdio.h>

/*
 Comments: Store comments in the AST, and add them to LLVM IR and MIPS code at the appropriate line.
 Comments: Add the original C-code as a comment in the LLVM IR and MIPS code.
 Typedefs
 printf
 */

int main() {
    // single line comment
    /*
     multi-line comment
    */
    typedef int myInt;
    myInt x = 5;


    // scoped typedef
    {
        typedef int type;
        type x = 5;
        printf("%d\n", x);
    }
    {
        typedef float type;
        type x = 5;
        printf("%d\n", x);
    }

    // nested typedef
    typedef int type;
    typedef type nestedType;
    nestedType y = 5;

    // typedef with pointer
    typedef int *type;
    type z = &x;

    // typedef with const
    typedef const int type;
    type a = 5;

    printf("Hello, World!\n");
    return 0;
}