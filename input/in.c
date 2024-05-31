#include <stdio.h>

int main() {
    int arr[3] = {1, 2, 3};
    printf("%d\n", arr[0]);
    printf("%d\n", arr[1]);
    printf("%d\n", arr[2]);
    arr[0] = 4;
    arr[1] = 5;
    arr[2] = 6;
    printf("%d\n", arr[0]);
    printf("%d\n", arr[1]);
    printf("%d\n", arr[2]);

    return 0;
}
