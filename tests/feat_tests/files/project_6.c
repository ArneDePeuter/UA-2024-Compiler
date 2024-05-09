#include <stdio.h>

/*
 Arrays: simple one dimensional arrays
 Arrays: multi-dimensional arrays.
 Arrays: assignment of complete arrays or array rows in case of multi-dimensional arrays.
 Arrays: array initialisation: int arr[3] = {1,2,3}.
 Arrays: Operations on array elements.
 Strings encoded as zero-terminated char-arrays. String literals. Passing strings around as char*. Support for IO: printf and scanf that support char* strings.
 The header stdio.h is treated as a special instruction that makes printf and scanf available. Including the actual stdio.h header is not necessary.
*/

int main() {
    // Arrays: simple one dimensional arrays
    // Array initialisation
    int arr[3] = {10, 20, 30};

    // Arrays: Operations on array elements. simple one dimensional arrays
    printf("%d\n", arr[0]);
    printf("%d\n", arr[1]);
    printf("%d\n", arr[2]);

    // Arrays: multi-dimensional arrays.
    int arr2[2][3] = {{1, 2, 3}, {4, 5, 6}};
    // Assigning complete arrays
    arr2[0] = arr;

    // Looping over multi-dimensional arrays
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d\n", arr2[i][j]);
        }
    }

    // Using pointer arithmetic on arrays for looping
    int *p = arr;
    for (int i = 0; i < 3; i++) {
        printf("%d\n", *(p + i));
    }

    // Strings encoded as zero-terminated char-arrays. String literals. Passing strings around as char*. Support for IO: printf and scanf that support char* strings.
    char *str = "Hello, World!";
    printf("%s\n", str);
    char str[20] = "Hello, World!";
    printf("%s\n", str);

    // Scanf and printf all formatters
    char str[20];
    scanf("%s", str);
    printf("%s\n", str);
    int x;
    scanf("%d", &x);
    printf("%d\n", x);
    float f;
    scanf("%f", &f);
    printf("%f\n", f);
    char c;
    scanf("%c", &c);
    printf("%c\n", c);

    return 0;
}