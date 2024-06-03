#include <stdio.h>

struct Test {
    int array[5];
};

int main() {
    struct Test test;
    test.array[0] = 1;
    test.array[1] = 2;
    test.array[2] = 3;
    test.array[3] = 4;
    test.array[4] = 5;

    for (int i = 0; i < 5; i++ ) {
        printf("%d", test.array[i]);
    }
}