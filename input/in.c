struct Leg {
    int healthy;
}

struct Dog {
    int number;
    struct Leg legs[4];
    struct Dog* parent;
}

int main() {
    struct Dog papa = {0, {{0}, {1}, {1}, {1}}, 0};
    struct Dog kid = {0, {{1}, {1}, {1}, {1}}, &papa};
    printf("%d", kid.number);
    return 0;
}

