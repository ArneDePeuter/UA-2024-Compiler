#include <stdio.h>
#include "mul.c"

// #include "boogiewoogie.h
/*
#include dookie_pointer.h
*/

#define bool int
#define true 1
#define false 0

//#define true false
/*
#define false true
*/

/** My program */
int main() {
    bool val = false;
    bool some_value = true;
    bool another_value = some_value && val;
    int x = 1;

    while (x < 10) {
        int result = mul(x, 2);

        if (x > 5) {
            result = mul(result, x);
        }

        printf("%d", result); // show the result

        x = x + 1;
    }

    return 0;
}
