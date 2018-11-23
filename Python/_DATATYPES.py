#This file defines the different types of data structures used

#Definition for a binary tree node.
class TreeNode:
    inOrder = []
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)
    def printInOrder(self, r):
        if r.left: r.printInOrder(r.left)
        self.inOrder += [r.val]
        if r.right: r.printInOrder(r.right)
        return self.inOrder


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val)
    def printList(self):
        r, t = [], self
        while t:
            r += [t.val]
            t = t.next
        return r
