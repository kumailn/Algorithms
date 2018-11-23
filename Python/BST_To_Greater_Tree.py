from _DATATYPES import TreeNode
#Question: Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
#Solution: Traverse reverse in order, keep count of sums and adjust each node as needed
#Difficulty: Easy
#Note: Due to Python scoping restrictions, var s needs to be in a class to be accessed by a recusive function

class Solution(object):
    s = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        def revS(r):
            if r.right: revS(r.right)   
            r.val, self.s = r.val + self.s, self.s + r.val
            if r.left: revS(r.left)
        revS(root)
        return root
    
def main():
    t = TreeNode(5)
    t.left = TreeNode(2)
    t.right = TreeNode(13)
    x = Solution()
    print(t.printInOrder(t))
main()
