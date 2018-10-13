def LinkedListIntersection(headA, headB):
        #Save heads of a and b
        a, b = headA, headB
        #As long as both aren't equal (they'll be equal if the have an intersection
        # of if they both reach the end of the linked list)
        while a != b:
            #Swap the values if they've become null, else move onto next value
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a