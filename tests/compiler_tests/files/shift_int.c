#include <stdio.h>

int main() {
    int num = 4; // Example number for shifting
    int leftShiftAmount = 1; // Shift left by 1 bit
    int rightShiftAmount = 2; // Shift right by 2 bits

    // Left shift operation
    int leftShifted = num << leftShiftAmount;
    printf("%d", leftShifted);

    // Right shift operation
    int rightShifted = num >> rightShiftAmount;
    printf("%d", rightShifted);

}
