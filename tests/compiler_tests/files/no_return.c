char char_func(char c) {
}

int int_func(int i) {
}

float float_func(float f) {
}

void void_func() {
}

int* int_ptr_func(int* i) {
}

int main() {
    char_func('a');
    int_func(1);
    float_func(1.0);
    void_func();
    int i = 1;
    int_ptr_func(&i);
    return 0;
}