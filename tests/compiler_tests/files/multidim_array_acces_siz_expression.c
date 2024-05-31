#include <stdio.h>

int main() {
    char c[2][3] = {{'a', 'b', 'c'}, {'d', 'e', 'f'}};
    c[0][0] = 'N';
    c[0][1] = 'i';
    c[0][1+1] = 'c';
    c[1][0] = 'e';
    c[1][1] = 'e';
    c[1][2] = '!';
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%c", c[i][j]);
        }
    }
    return 0;
}