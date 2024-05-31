#include <stdio.h>

int main() {
    printf("%d\n", 1 + 1);
    printf("%d\n", 0 - 6985);
    printf("%d\n", 5 * 63);
    printf("%d\n", 99 / 3622);
    printf("%d\n", 3 > 1);
    printf("%d\n", 3 < 1);
    printf("%d\n", 8897 == 45647897);
    printf("%d\n", +487897);
    printf("%d\n", -5);
    printf("%d\n", 1 && 656);
    printf("%d\n", 989 || 68779);
    printf("%d\n", !65465);
    printf("%d\n", 1 + (3 * 6) / (1 + 3));
    printf("%d\n", 1 + 3 + 5 * (62 / 3));
    printf("%d\n", 5 * +9);
    printf("%d\n", 33 * -5);
    printf("%d\n", ((-6)) * (((5 + 32 / (6532)))));
    printf("%d\n", 1 >= 3);
    printf("%d\n", 695 <= 44878);
    printf("%d\n", 98333 != 6565911);
    printf("%d\n", 55 % 963);
    printf("%d\n", 45 << 4);
    // printf("%d\n", -33 >> -4);
    // Right shifting a negative number by a negative amount is undefined behavior.
    printf("%d\n", 1 & 8784573);
    printf("%d\n", 898 | 98);
    printf("%d\n", !-97435345);
    printf("%d\n", 9787 ^ -9987);

    return 0;
}
