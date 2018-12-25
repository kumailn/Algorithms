from _DATATYPES import TreeNode
#Question: Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
#Solution: Traverse reverse in order, keep count of sums and adjust each node as needed
#Difficulty: Easy
#Note: Due to Python scoping restrictions, var s needs to be in a class to be accessed by a recusive function

class Solution(object):
    sumCount = 0
    def convertBST(self, root):
        #Recursive helper to traverse reverse in order
        def reverseInOrder(r):
            #Go to right-most element
            if r.right: reverseInOrder(r.right)   
            #Set its value to be the current sum, and update current sum to be its (old) value
            r.val, self.sumCount = r.val + self.sumCount, self.sumCount + r.val
            #Go to left node if exists
            if r.left: reverseInOrder(r.left)
        #Run recursive helper
        reverseInOrder(root)
        #Return root because alorithm is in-place
        return root
    
def main():
    t = TreeNode(5)
    t.left = TreeNode(2)
    t.right = TreeNode(13)
    x = Solution()
    print(t.printInOrder(t))
main()
