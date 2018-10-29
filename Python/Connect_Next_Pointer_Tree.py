#Question: 
def connect(self, root):
        if not root: return None
        q, c, head = [root], [], root
        while q:
            for i, v in enumerate(q):
                v.next = q[i + 1] if i + 1 < len(q) else None
                if v.left: c += [v.left]
                if v.right: c += [v.right]
            q, c = c, []
            print([v.val for v in q])
            
            