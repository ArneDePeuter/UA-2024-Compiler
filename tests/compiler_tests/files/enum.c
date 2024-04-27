#include <stdio.h>

enum Days {
    MONDAY,
    TUESDAY
};

int main() {
    // Use the enum to set a variable
    enum Days today = MONDAY;
    enum Days tomorrow = today + 1;
    float td = today;
    float tm = tomorrow;
    printf("%f", td);
    printf("%c", '\n');
    printf("%f", tm);
    return 0;
}
