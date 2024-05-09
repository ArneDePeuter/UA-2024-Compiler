#include <stdio.h> // #include.

#define FOO 5 // #define.

/*
 Function scopes.
 Local and global variables.
 Functions: definitions; declarations; calling, recursive calls; parameters (const, float, int, pointers); returns; void functions;
 Pre-processor: #define. Parameters do not need to be supported.
 Pre-processor: #include.
*/

// global variable
int global = 5;

int add(int a, int b) {
    return a + b;
}

int sub(int a, int b) {
    return a - b;
}

int mul(int a, int b) {
    return a * b;
}

int div(int a, int b) {
    return a / b;
}

int mod(int a, int b) {
    return a % b;
}

// forward declaration of fib
int fib(int n);

int main() {
    // use of define
    int x = FOO;
    // use of global variable
    int y = global;
    int z = add(x, y);
    printf("%d\n", z);
    z = sub(x, y);
    printf("%d\n", z);
    z = mul(x, y);
    printf("%d\n", z);
    z = div(x, y);
    printf("%d\n", z);
    z = mod(x, y);
    printf("%d\n", z);
    z = fib(5);
    printf("%d\n", z);
    return 0;
}

// recursive fib function
int fib(int n) {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}