#include <stdio.h>

int main() {
    int a = 0;
    int counter = 0;
    while (counter < 1000000) {
        a++;
        break;
        counter++;
    }
    printf("%d", (a==1) & (counter==0));
}

