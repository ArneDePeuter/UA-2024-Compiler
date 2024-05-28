#include <stdio.h>

int main() {
    printf("%d\n", 33 + 69789 * (69421 / 51213 + (2231 - 654)));
    printf("%d\n", 654 * (15486 - (15000 + 486)));
    printf("%d\n", 1 && (1 || 0));
    printf("%d\n", 0 && (1 && 1));
    printf("%d\n", 0 || (0 * 3));
    printf("%d\n", 1 && (!(1 + 0)));
    printf("%d\n", 12 + (98721 + 36265 / 456) * (0 + 1687));
    printf("%d\n", 12 + (98721 * 0 + 36265 / 456) * (0));

    printf("%d\n", (12321 > (9656 + 3)));
    printf("%d\n", (125154 < (54 > -65)));

    printf("%d\n", 987842121 >= 212);

    printf("%d\n", -6549 <= (2189 + 63));
    printf("%d\n", 0 >= (-564654));

    printf("%d\n", 540 != 58973);
    printf("%d\n", -5 != -5);

    printf("%d\n", (-5 * 20) != ((-4 * 25)));

    printf("%d\n", 9 % 10);
    printf("%d\n", 19 % 10);
    printf("%d\n", 8971 % 8);

    printf("%d\n", 1024 << 4);
    printf("%d\n", 2048 >> 3);
    printf("%d\n", 2048 >> -3);

    printf("%d\n", 23423 ^ 7345345);
    printf("%d\n", 843 & -86);
    printf("%d\n", 954 | 976);
    printf("%d\n", !9736);

    return 0;
}
