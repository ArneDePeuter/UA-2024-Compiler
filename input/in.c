#include <stdio.h>

int main() {
    char* array_of_strings[3] = {"Hello", "World", "!"};
    for (int i = 0; i < 3; i++) {
        printf("%s ", array_of_strings[i]);
    }
    return 0;
}