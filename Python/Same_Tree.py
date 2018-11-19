from _DATATYPES import TreeNode
#Question: Given two trees, check if they are the exact same
#Solution: Traverse both trees recursively 
#Difficulty: Easy 

def isSameTree(p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #If both p and q are non null, their values should be the same, and so should their left and right children
        if p and q: return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right) 
        #Otherwise return p == q (True only if both p and q have become null)
        return p == q