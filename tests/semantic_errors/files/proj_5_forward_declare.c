int fib(int);

int main() {
    printf("%d", fib(2));
    return 0;
}

int fib(int a) {
    if (a == 0) {
        return 0;
    } else if (a == 1) {
        return 1;
    } else {
        return fib(a - 1) + fib(a - 2);
    }
}