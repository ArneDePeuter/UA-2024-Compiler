int main() {

int x = 54;

int z = -33;

int* p = &z;

p = *x; // error: indirection requires pointer operand ('int' invalid)
}
