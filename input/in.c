int main() {
    int f[10][10];
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < 10; ++j) {
            f[i][j] = i + j;
        }
    }
    return 0;
}