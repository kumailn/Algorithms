def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        def helper(root, order):
            if root.left: helper(root.left, order)
            if root.right: helper(root.right, order)
            if root: order.append(root.val)
            return order
        return helper(root, [])