from _DATATYPES import TreeNode
#Question: Given the root node of a tree, find the in order successor of that node
#Solution: Find the first node that is not smaller than the given one
#Difficulty: Easy

def inorderSuccessor(root, p):
    if not root: return None
    successor = None
    while root:
        if root.val > p.val: successor, root = root, root.left
        else: root = root.right
    return successor

def main():
    a = TreeNode(6)
    a.left = TreeNode(4)
    a.left.right = TreeNode(5)
    a.left.left = TreeNode(3)

    print(inorderSuccessor(a, TreeNode(4)))

main()