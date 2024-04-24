enum Days {
    FRIDAY,
    SATURDAY
};

int main() {
    // Use the enum to set a variable
    int i = 1;
    enum Days today = FRIDAY;
    enum Days tomorrow = today + 1;
}
