from _DATATYPES import TreeNode
#Question: Given a Binary Search Tree, determing if it's valid
#Solution: Recursively check all nodes in tree are within their valid ranges
#Difficulty: Easy

def isValidBST(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #If node is null then return True
        if not root: return True
        #Define recursive helper, takes in current node and its valid range
        def helper(r, minVal, maxVal):
            #If node is null return true
            if not r: return True
            #If nodes val is not within given range, return False
            if r.val <= minVal or r.val >= maxVal: return False
            #Call helper on left and right children, for left child let the maxVal be the current nodes value (Max decreases as you go left)
            #For right child let minVal be current nodes val (Min increases as you go right)
            return helper(r.left, minVal, r.val) and helper(r.right, r.val, maxVal)
        #Initially call on root node with a min of -infinity and max of +infinity
        return helper(root, float('-inf'), float('inf'))

