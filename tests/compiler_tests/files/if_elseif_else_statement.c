#include <stdio.h>

int main() {
    int marks = 85;

    if (marks > 90) {
        printf("%d", 10);
    } else if ("%s", marks > 80) {
        printf("%d", 8);
    } else if ("%s", marks > 70) {
        printf("%d", 7);
    } else if (marks > 60) {
        printf("%d", 6);
    } else {
        printf("%d", 0);
    }
}
