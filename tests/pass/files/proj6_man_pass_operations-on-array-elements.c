int main () {
    int a[6] = {100, 50, 20, 10, 5, 1};
    char b[6] = {'A', 'B', 'C', 'D', 'E', 'F'};

    // Performing arithmetic operations on elements of array 'a'
    a[0] -= 50; // Decrease the first element by 50
    a[1] += 30; // Increase the second element by 30
    a[2] *= 2;  // Double the third element
    a[3] /= 2;  // Halve the fourth element
    a[4]++;     // Increment the fifth element
    a[5]--;     // Decrement the sixth element

    // Performing operations on elements of array 'b'
    b[0] = 'Z';  // Change the first character
    b[1] += 1;   // Move the second character to the next in ASCII table
    b[2] -= 1;   // Move the third character to the previous in ASCII table
    b[3] = 'b'[0] - 'a'[0] + b[3];  // Convert to lowercase if possible
    b[4] ^= 32;  // Another method to toggle case if it's letter
}