// Forward declaration of a recursive function
int factorial(int n);

int main() {
    int num = 5;
    int result = factorial(num);
    printf("%d", num);
    return 0;
}

// Recursive function to calculate factorial
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}
