#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main() {
    struct Point p;
    p.x = 1;
    p.y = 2;
    int total = p.x + p.y;
    printf("%d", total);
}
