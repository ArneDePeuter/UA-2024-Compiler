#include <stdio.h>

struct Node {
    int data;
    struct Node *next;
};

int main() {
    struct Node head;
    head.data = 1;

    struct Node node1;
    node1.data = 2;
    head.next = &node1;

    struct Node node2;
    node2.data = 3;
    node1.next = &node2;


    struct Node *current = &head;
    while (current != 0) {
        printf("%d\n", current->data);
        current = current->next;
    }

    return 0;
}
