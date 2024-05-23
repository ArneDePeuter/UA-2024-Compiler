#include <stdio.h>

int main() {
    int a = 0;
    if (a == 0) {
        printf("a is 0\n");
        if (1) {
            printf("yes\n");
        } else {
            printf("no\n");
        }
    }
    printf("hello");
    return 0;
}