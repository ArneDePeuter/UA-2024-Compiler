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

struct A generateA() {
    struct A a;
    a.num = 10;
    a.character = 'a';
    a.b.num = 1;
    return a;
}

int main() {
    struct A a1;
    a1.num = 10;
    a1.character = 'a';
    a1.b.num = 1;

    printA(a1);
    a1.num = 20;
    printA(a1);

    printA(generateA());

    return 0;
}