struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *a = headA;
    struct ListNode *b = headB;

    while (a != b){
        if(!a) a = headB;
        else a = a->next;
        if(!b) b = headA;
        else b = b->next;
    }
    return a;

}