#Question: Given two numbers in the form of linked lists, add them
def addTwoNumbers(l1, l2):
        carry = 0
        orig = n = ListNode(None)
        if not l2 or not l1: return l2 if l2 else l1
        while l1 or l2 or carry:
            lv, lv2 = l1.val if l1 else 0, l2.val if l2 else 0
            n.next = ListNode((lv + lv2 + carry) % 10)
            carry = (lv + lv2 + carry) // 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            n = n.next
        return orig.next