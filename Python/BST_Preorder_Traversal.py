def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        def preorder(root, order):
            if root: order.append(root.val)
            if root.left: preorder(root.left, order)
            if root.right: preorder(root.right, order)
            return order
        return preorder(root, [])
            