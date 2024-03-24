int main() {
const char c = 'a';
const char* chr_ptr = &c;
char* non_const_ptr = chr_ptr; // warning: initializing 'char *' with an expression of type 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
*non_const_ptr = 'c';

}
