#include <stdio.h>

struct myStruct {
    int x[3];
};

int main() {
    struct myStruct s;
    s.x[0] = 1;
    s.x[1] = 2;
    s.x[2] = 3;

    printf("%d\n", s.x[0]);
    printf("%d\n", s.x[1]);
    printf("%d\n", s.x[2]);
    s.x[0] = 5;
    s.x[1] = 10;
    s.x[2] = 15;
    printf("%d\n", s.x[0]);
    printf("%d\n", s.x[1]);
    printf("%d\n", s.x[2]);
    return 0;
}
