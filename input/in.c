struct B {
    int num;
};

struct A {
    int num;
    char character;
    struct B b;
};

void printA(struct A a) {
//    printf("%d", a.numarray[0]);
//    printf("%d", a.numarray[1]);
//    printf("%d", a.numarray[2]);
    printf("%d", a.num);
    printf("%c", a.character);
    printf("%d", a.b.num);
}

int main() {
    struct A a1 = {10, 'a', {1}};

    printA((struct A){10,  'a', {1}});

    printA(a1);
    a1.num = 20;
    printA(a1);

    return 0;
}