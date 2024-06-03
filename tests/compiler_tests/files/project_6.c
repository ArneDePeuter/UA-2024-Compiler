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

void capitalise_char(char *c) {
    *c = *c - 32;
}

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

    // Looping over multi-dimensional arrays
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d\n", arr2[i][j]);
        }
    }

    // Using pointer arithmetic on arrays for looping
    int *p = &arr[0];
    for (int i = 0; i < 3; i++) {
        printf("%d\n", *(p + i));
    }

    // Strings encoded as zero-terminated char-arrays. String literals. Passing strings around as char*. Support for IO: printf and scanf that support char* strings.
    char *str_ptr = "Hello, World!";
    printf("%s\n", str_ptr);
    char str_arr[14] = "Hello, World!";
    printf("%s\n", str_arr);

    // printf with string literals
    printf("%s", "This is a string\n");

    char str[] = "hello"; // Mutable array
    char* hello = str; // Decay array to pointer
    capitalise_string(hello, 5);
    printf("Capitalise: %s\n", hello);

    for (int i = 0; i < 5; i++) {
        printf("%c", capitalise_char(&str[i]));
    }

    return 0;
}