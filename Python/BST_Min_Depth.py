def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        current = []
        mindepth = 0
        if not root: return mindepth
        while queue:
            for i in queue:
                if not i.left and not i.right: return mindepth + 1
                if i.left: current.append(i.left)
                if i.right: current.append(i.right)
            queue = current
            current = []
            mindepth += 1
        return mindepth