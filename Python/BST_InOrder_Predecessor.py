from _DATATYPES import TreeNode
#Question: Given the root node of a tree, find the in order successor of that node
#Solution: Find the first node that is not smaller than the given one
#Difficulty: Easy

def inorderPredecessor(root, p):
    if not root: return None
    predecessor = None
    while root:
        if root.val < p.val: predecessor, root = root, root.right
        else: root = root.left
    return predecessor

def main():
    a = TreeNode(6)
    a.left = TreeNode(4)
    a.left.right = TreeNode(5)
    a.left.left = TreeNode(3)

    print(inorderPredecessor(a, TreeNode(5)))

main()