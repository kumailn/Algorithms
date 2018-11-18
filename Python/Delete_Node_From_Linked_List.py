from _DATATYPES import ListNode
#Question: Given ta node in a linked list, delete it
#Solution: Copy next value into current node and let next be nexts next
#Difficulty: Easy

def deleteNode(node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next