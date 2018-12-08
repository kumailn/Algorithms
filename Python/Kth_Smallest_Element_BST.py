class Solution(object):
    a = 0; result = None
    def kthSmallest(self, root, k):
        self.a = k
        def rec(r):
            if r.left: rec(r.left)
            self.a -= 1
            if not self.a: self.result = r.val; return
            if r.right: rec(r.right)
        rec(root)
        return self.result
        
            
        