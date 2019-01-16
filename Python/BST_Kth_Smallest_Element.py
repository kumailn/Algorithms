from _DATATYPES import TreeNode

def kthSmallest(root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while stack or root:
            while root: 
                stack += [root]
                root = root.left
            root = stack.pop()
            k -= 1
            if not k: return root.val
            root = root.right

def main():
    a = TreeNode(6)
    a.left = TreeNode(3)
    a.right = TreeNode(11)
    a.left.right = TreeNode(4)
    a.left.right.right = TreeNode(5)

    print(kthSmallest(a, 2))

main()