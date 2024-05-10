#include <stdio.h>

int globalVar = 10; // Global variable

int add(int a, int b) {
    int sum = a + b; // Local variable in add function
    {
        int scopeVar = 20; // Block scope variable inside add function
    }
    int localVar = 30; // Local variable in add function
    return sum;
}

int main() {
    int scope1Var = 30; // Local variable in main
    {
        int scope2Var = 40; // Block scope variable inside if statement
    }
    int localVar = 50; // Local variable in main
    return 0;
}