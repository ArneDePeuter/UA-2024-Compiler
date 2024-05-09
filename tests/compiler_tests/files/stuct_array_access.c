#include <stdio.h>

struct Test {
    int array[5];
};

int main() {
    struct Test test = {{10, 20, 30, 40, '2'}};

    for (int i = 0; i < 5; i++ ) {
        printf("%d", test.array[i]);
    }
}