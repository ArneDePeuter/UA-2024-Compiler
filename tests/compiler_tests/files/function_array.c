#include <stdio.h>

// Function to print an array of integers
void print_array(int arr[5]) {
    for (int i = 0; i < 5; i++) {
        printf("%d", arr[i]);
    }
}

int main() {
    int numbers[5] = {1, 2, 3, 4, 5}; // Example array
    print_array(numbers); // Call the print function
    return 0;
}
