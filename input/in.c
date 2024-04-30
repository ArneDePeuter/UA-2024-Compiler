 struct ListNode {
     int value;
     struct ListNode* next_ptr;
 };

 int main() {
    struct ListNode node1 = {1, 0};
    struct ListNode node2 = {3, &node1};

    printf("%d", node1.value);
    (*node2.next_ptr).value = 3;
    printf("%d", node1.value);
 }