#include <stdio.h>

int main() {
    int a = 0;
    int counter = 0;
    while (counter < 1000000) {
        counter++;
        continue;
        a++;
    }
    printf("%d", (a==0) & (counter==1000000));
}

