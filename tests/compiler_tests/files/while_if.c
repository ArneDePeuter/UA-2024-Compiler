#include <stdio.h>

int main() {
    int a = 0;
    int counter = 0;
    int b = 0;
    while (counter < 1000000) {
        if (counter > 100) {
            b++;
        }
        a++;
        counter++;
    }
    printf("%d", a);
    printf("%d", b);
}