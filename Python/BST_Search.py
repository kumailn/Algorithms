def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root and val != root.val:
            root = root.left if val < root.val else root.right
        return root