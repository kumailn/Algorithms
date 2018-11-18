#Question: Traverse a tree level by level in a zig zag order
#Solution: Typical Breadth First Search (BFS) but keep track of zigzag
#Difficulty: Medium 

def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        r, q, c = [[]], [root], []
        zig = False
        while q:
            for i in q:
                r[-1] += [i.val]
                if i.left: c += [i.left]
                if i.right: c += [i.right]
            q, c = c, []
            if zig:
                r[-1] = r[-1][::-1]
            zig = not zig
            if q: r += [[]]
        return r