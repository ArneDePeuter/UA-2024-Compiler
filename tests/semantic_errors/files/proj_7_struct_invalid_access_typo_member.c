struct Point {
    int x;
    int y;
};

int main() {
    struct Point p;
    p.x = 5;
    p.y = 10;

    p.x = 15;
    p.yy = 20; // Typo here, should be 'y'

    return 0;
}
