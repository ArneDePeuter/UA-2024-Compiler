int main() {
    int x = 4;
    int* ptr = &x;
    float* ptr2 = 0;

    float* ptr3 = ptr2 + ptr;
    ptr3 = ptr - ptr3;

}
