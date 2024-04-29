#include <stdio.h>

int main() {
    char grade = 'B';
    switch (grade) {
        case 'A':
            //printf("Excellent!\n");
            printf("%c", grade);
            break;
        case 'B':
        case 'C':
            //printf("Well done\n");
            printf("%c", grade);
            break;
        case 'D':
            //printf("You passed\n");
            printf("%c", grade);
            break;
        case 'F':
            //printf("Better try again\n");
            printf("%c", grade);
            break;
        default:
            //printf("Invalid grade\n");
            printf("%c", grade);
    }
    return 0;
}
