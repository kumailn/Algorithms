class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeList(a, b):
    if (not a or b and a.val > b.val): a, b = b, a
    if a: a.next = mergeList(a.next, b)
    return a

a = ListNode(7)
a.next = ListNode(32)
a.next.next = ListNode(2)

b = ListNode(5)
b.next = ListNode(0)
b.next.next = ListNode(43)

def printLinkedList(ll):
    l = []
    while(ll):
        l += [(ll.val)]
        ll = ll.next
    print(l)
    
printLinkedList(mergeList(a, b))