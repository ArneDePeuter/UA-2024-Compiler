int main() {
    int x = 4;
    int* ptr = &x;
    float* ptr2 = 0; // This should be valid using NULL

    // wrong types
    float* ptr3 = ptr2 + ptr; // error: invalid operands to binary expression ('float *' and 'int *')
    ptr3 = ptr - ptr3; // error: 'int *' and 'float *' are not pointers to compatible types

}
