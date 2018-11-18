from _DATATYPES import TreeNode

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root: return None
    root.right, root.left = invertTree(root.left), invertTree(root.right)
    return root

def main():
    print(invertTree(TreeNode(None)))
main()