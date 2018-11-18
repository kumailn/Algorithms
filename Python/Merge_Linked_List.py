from _DATATYPES import ListNode
#Question: Given two sorted linked lists, join them
#Solution: Traverse through both lists, swapping values to find smallest, then working backwards
#Difficulty: Easy 

def mergeList(a, b):
    #If the first node is null, or the second node exists and is smaller than the first node, swap the two nodes
    #This ensures that a is always the smallest non null node
    if not a or b and a.val > b.val: a, b = b, a
    #If a is not null, then let its next value be a recursive call to its next value, and b
    if a: a.next = mergeList(a.next, b)
    #Return a's head as we never shifted a in this scope, only in subsequent recursive calls
    return a

def main():
    a = ListNode(4)
    a.next  = ListNode(23)
    a.next.next = ListNode(44)

    b = ListNode(5)
    b.next = ListNode(11)
    b.next.next = ListNode(14)
    mergeList(b, a)
    
    print(a.printList())
main()