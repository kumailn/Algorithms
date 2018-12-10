def hasPathSum(root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        sums = []
        def helper(root, pathSum, sums):
            if not root: return
            if not root.left and not root.right: sums.append(pathSum + root.val)
            if root.left: helper(root.left, pathSum + root.val, sums)
            if root.right: helper(root.right, pathSum + root.val, sums)
        helper(root, 0, sums)
        print(sums)
        return sum in sums
    