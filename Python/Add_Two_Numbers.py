#Question: Given two numbers in the form of linked lists, add them
#Solution: Loop until the first list, second list or a carry exists, add accordingly 
#Difficulty: Easy

def addTwoNumbers(l1, l2):
        #Initialize variable to hold the carryover from an addition
        carry = 0
        #Let origin = n = an empty LinkedList node
        orig = n = ListNode(None)
        #If one of the input nodes is null, return the one that's not
        if not l2 or not l1: return l2 if l2 else l1
        #While one of the nodes is not null or the carry value exists
        while l1 or l2 or carry:
            #Let value of node1 be the value of node1 if node1 is not null, otherwise 0, same for node2
            lv, lv2 = l1.val if l1 else 0, l2.val if l2 else 0
            #Let next node from our temp node be the sum of the values of the nodes and the carry, mod 10, (to find leftmost number)
            n.next = ListNode((lv + lv2 + carry) % 10)
            #Let the carry be the same sum but int divided by 10 (to find number after leftmost)
            carry = (lv + lv2 + carry) // 10
            #If node1 exists move to next, if node2 exists move to next, shift temp to next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            n = n.next
        #Return the origin nodes next node
        return orig.next