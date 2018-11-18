from _DATATYPES import TreeNode
#Question: Given a Binary Search Tree, swap all mirrored nodes
#Solution: Recursively swap all pairs of mirroring nodes
#Difficulty: Easy

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    #If root is null return null
    if not root: return None
    #Let the left and right children be recursive calls to right and left children respectively
    root.right, root.left = invertTree(root.left), invertTree(root.right)
    #return current root
    return root

def main():
    a = TreeNode(4)
    a.left = TreeNode(3)
    a.right = TreeNode(5)
    print(invertTree(TreeNode(None)))
    print(invertTree(a).right)
main()