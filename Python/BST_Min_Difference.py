from _DATATYPES import TreeNode
#Question: Given a BST, find the minimum difference between any two nodes
#Solution: Traverse in order, keep track of the previous node, and find the difference between current one. The minimun difference must be between two consecutive nodes because we are travelling in order!
#Difficulty: Easy 

class Solution(object):
    #Value of previous node, set to -infinity intitially 
    previousVal = float('-inf') 
    #The minimum difference between the nodes, set to infinity initially
    minDifference = float('inf')
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Define the recursive helper that travels in order
        def rec(r):
            #If left node exists go left
            if r.left: rec(r.left)
            #Set the min difference to be the min of itself or the difference between current and previous nodes
            self.minDifference = min(self.minDifference, (r.val - self.previousVal))
            #Set the previous node to be the current node
            self.previousVal = r.val
            #IF right node exists go right
            if r.right: rec(r.right)
        #Run recursive helper
        rec(root)
        #Return original tree root
        return self.minDifference