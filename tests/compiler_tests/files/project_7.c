#include <stdio.h>

/*
 User-defined structs. The structs should support members with primitive fields, arrays, enum types, as well as pointer types. You do not have to support default values for the struct members.
 Optional: Structs that contain other structs as a value.
 Optional: Structs explicit initialization.
*/

// User-defined structs. The structs should support members with primitive fields, arrays, enum types, as well as pointer types. You do not have to support default values for the struct members.
struct myStruct {
    int x;
    int y;
    int z;
};

// Optional: Structs that contain other structs as a value.
struct myStruct2 {
    struct myStruct s;
    int x;
};

// Struct with pointer to itself
struct myStruct3 {
    struct myStruct3 *next;
    int x;
};

// Struct with array
struct myStruct4 {
    int arr[3];
};

// function to print struct
void printStruct(struct myStruct s) {
    printf("%d\n", s.x);
    printf("%d\n", s.y);
    printf("%d\n", s.z);
}

int main() {
    // Structs
    struct myStruct s;
    s.x = 5;
    s.y = 10;
    s.z = 15;
    printf("%d\n", s.x);
    printf("%d\n", s.y);
    printf("%d\n", s.z);

    // Structs that contain other structs as a value.
    struct myStruct2 s2;
    s2.s.x = 5;
    s2.s.y = 10;
    s2.s.z = 15;
    s2.x = 20;
    printf("%d\n", s2.s.x);
    printf("%d\n", s2.s.y);
    printf("%d\n", s2.s.z);
    printf("%d\n", s2.x);

    // Struct with pointer to itself
    struct myStruct3 s3;
    s3.x = 5;
    struct myStruct3 s4;
    s4.x = 10;
    s3.next = &s4;
    printf("%d\n", s3.x);
    printf("%d\n", s3.next->x);

    // Struct with array
    struct myStruct4 s5;
    s5.arr[0] = 5;
    s5.arr[1] = 10;
    s5.arr[2] = 15;
    printf("%d\n", s5.arr[0]);
    printf("%d\n", s5.arr[1]);
    printf("%d\n", s5.arr[2]);

    struct myStruct s6;
    s6.x = 20;
    s6.y = 25;
    s6.z = 30;

    // function to print struct
    printStruct(s6);

    return 0;
}