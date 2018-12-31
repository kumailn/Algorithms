def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        def helper(root, currentPath, allPaths):
            if not root.left and not root.right: allPaths.append(currentPath + [root.val])
            if root.left: helper(root.left, currentPath + [root.val], allPaths)
            if root.right: helper(root.right, currentPath + [root.val], allPaths)
            return allPaths
        return sum(map(lambda x: int("".join(list(map(str, x)))), helper(root, [], [])))
        