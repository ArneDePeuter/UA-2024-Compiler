#include <stdio.h>

// Define the inner struct
struct Inner {
    int value;
};

struct Outer {
    struct Inner *inner_ptr;
};

void modifyInner(struct Outer *outer) {
    if (outer != 0) {
        if (outer->inner_ptr != 0) {
            outer->inner_ptr->value = 42;
        }
    }
}

int main() {
    struct Inner inner = {10};
    struct Outer outer = {&inner};


    printf("%d", outer.inner_ptr->value);
    modifyInner(&outer);
    printf("%d", outer.inner_ptr->value);

    return 0;
}
