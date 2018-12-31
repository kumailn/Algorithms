class Solution(object):
    lsum = 0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        def helper(root):
            if root.right: helper(root.right)
            if root.left: helper(root.left)
            if root.left and not root.left.left and not root.left.right:
                self.lsum += root.left.val
        helper(root)
        return self.lsum