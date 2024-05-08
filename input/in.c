#include <stdio.h>

struct Inner {
    int value;
};

struct Outer {
    struct Inner* inner_ptr;
};

void modifyInner(struct Outer* outer) {
    if (outer != 0) {
        if (outer->inner_ptr != 0) {
            outer->inner_ptr->value = 42;
            return;
        }
    }
    printf("%d", 0);
}

int main() {
    struct Inner inner = {10};
    struct Outer outer = {&inner};
    struct Outer *outer_ptr = 0;
    modifyInner(outer_ptr);
    return 0;
}
