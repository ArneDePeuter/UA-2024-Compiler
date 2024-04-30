

struct B {
    int num1;
};

struct A {
    int num1[3];
    char num2;
    struct B b;
    struct A* parent;
};

void printA(struct A a) {
    printf("%d", a.num1);
    printf("%d", a.num2);
    printf("%d", a.b.num1);
}

int main() {
    struct A a1 = {{1, 2, 3}, 'a', {1}, 0};
    struct A* a_ptr = &a1;

    (*a_ptr).num1;

    printA((struct A){{1, 2, 3}, 'a', {1}, &a1});

    return 0;
}