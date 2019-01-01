from _DATATYPES import TreeNode
#Question: Given the root node of a tree, determine if the tree is univalued (ie all nodes have the same value)
#Solution: Use recursion to compare every node in the tree with the value of the root node
#Difficulty: Easy
#Time Complexity: O(n)
#Space Complexity: O(n)

def isUnivalTree(self, root):
    #If out root node is null, return True becuse it is univalue
    if not root: return True
    #Define our recursive helper function
    def univalue(root, val):
        #If the root is null, return true
        if not root: return True
        #If the roots value is not equal to the value that was passed in, return False
        if root.val != val: return False
        #Return a recursive call on the left and right node, this ensures every single node will be visited
        return univalue(root.left, val) and univalue(root.right, val)
    return univalue(root, root.val)