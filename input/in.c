

struct A {
    int a;
    char b;
};

int main() {
    struct A a = {1, 'c'};
    struct A* a_ptr = &a;
    int a_a = (*(a_ptr+1)).a;
    
    return 0;
}