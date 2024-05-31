#include <stdio.h>

int main() {
    int i1 = 10, i2= 3;
    float f1 = 10.0, f2 = 3.0;

    printf("Ints");
    printf("%d - ", i1 + i2);
    printf("%d - ", i1 - i2);
    printf("%d - ", i1 * i2);
    printf("%d - ", i1 / i2);
    printf("%d - ", i1 % i2);

    printf("Floats");
    printf("%f - ", f1 + f2);
    printf("%f - ", f1 - f2);
    printf("%f - ", f1 * f2);
    printf("%f - ", f1 / f2);
}