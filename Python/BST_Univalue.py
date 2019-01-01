    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        def univalue(root, val):
            if not root: return True
            if root.val != val: return False
            return univalue(root.left, val) and univalue(root.right, val)
        return univalue(root, root.val)