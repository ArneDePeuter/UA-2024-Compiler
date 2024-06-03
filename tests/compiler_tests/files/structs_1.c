#include <stdio.h>

struct B {
    int num;
};

struct A {
    int num;
    char character;
    struct B b;
};

void printA(struct A a) {
    printf("%d", a.num);
    printf("%c", a.character);
    printf("%d", a.b.num);
}

int main() {
    struct A a1;
    a1.num = 10;
    a1.character = 'a';
    a1.b.num = 1;

    printA(a1);
    a1.num = 20;
    printA(a1);

    return 0;
}