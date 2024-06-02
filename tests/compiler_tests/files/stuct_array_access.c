#include <stdio.h>

struct Test {
    int array[5];
};

int main() {
    struct Test test;
    test.array = {1, 2, 3, 4, 5};

    for (int i = 0; i < 5; i++ ) {
        printf("%d", test.array[i]);
    }
}