int main() {
    int b = 1;
    int* a[2] = {&b, &b};

    char f[2][1] = {{'a'}, {'b'}};
    char* c[2] = {&f[0][0], &f[1][0]};
}