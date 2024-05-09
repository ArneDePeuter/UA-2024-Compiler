#include <stdio.h>

int main() {
    char* str_arr[3] = {"Hello", "World", "!"};
    for (int i = 0; i < 3; i++) {
        printf("%s ", str_arr[i]);
    }

    str_arr[0] = "Goodbye";
    for (int i = 0; i < 3; i++) {
        printf("%s ", str_arr[i]);
    }

    return 0;
}
