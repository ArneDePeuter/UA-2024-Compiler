 #include <stdio.h>

 struct ListNode {
     int value;
     struct ListNode* next_ptr;
 };

 int main() {
    struct ListNode node1;
    node1.value = 2;
    node1.next_ptr = 0;
    struct ListNode node2;
    node2.value = 3;
    node2.next_ptr = 0;

    printf("%d", node1.value);
    node2.next_ptr->value = 8;
    printf("%d", node1.value);
 }