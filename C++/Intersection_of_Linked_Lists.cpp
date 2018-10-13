class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *a = headA;
        ListNode *b = headB;
        while (a != b){
            if(!a) a = headB;
            else a = a->next;
            if(!b) b = headA;
            else b = b->next;
        }
        return a;
    }
};