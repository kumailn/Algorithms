from _DATATYPES import ListNode
#Question: Given ta node in a linked list, delete it
#Solution: Copy next value into current node and let next be nexts next
#Difficulty: Easy

def deleteNode(node):
        #Set the current nodes value to the value of the next node
        node.val = node.next.val
        #Set the current nodes next property to the next nodes next, esspentially 'deleting' the original next node
        node.next = node.next.next