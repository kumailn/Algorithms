from _DATATYPES import ListNode
#Question: Given a linked list, reverse it, in place
#Solution: Iterate through, swapping pointers
#Difficulty: Easy

def reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Let previous node be null and current be head
        previous = None
        current = head
        #As long as head isnt null
        while head:
            #Set current to head, head to the next (Important otherwise heads next node will also become previous)
            current, head = head, head.next
            #Let current's next node be previous
            current.next = previous
            #Let previous be current
            previous = current
        return current
