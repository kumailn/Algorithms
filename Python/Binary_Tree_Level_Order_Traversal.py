def levelOrder(self, root):
        if not root: return []
        r, q, c = [[]], [root], []
        while q:
            for i in range(len(q)):
                r[-1] += [q[i].val]
                c = c + [q[i].left] if q[i].left else c
                c = c + [q[i].right] if q[i].right else c
            q, c = c, []
            r = r + [[]] if q else r
        return r
        