# Question: Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.
# Solution: Do a reverse in order traversal and keep track of the sum

def bstToGst(self, root: TreeNode) -> TreeNode:
    x = 0
    
    def revInOrder(root):
        nonlocal x
        if not root: return 
        
        revInOrder(root.right)
        root.val += x 
        x = root.val
        revInOrder(root.left)
    
    revInOrder(root)
    return root