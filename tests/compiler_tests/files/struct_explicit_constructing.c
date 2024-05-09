#include <stdio.h>

struct Point {
    int x;
    int y;
};

void printPoint(const struct Point p) {
    printf("%d", p.x);
    printf("%d", p.y);
}

int main() {
    printPoint((struct Point){1, 2});
}
