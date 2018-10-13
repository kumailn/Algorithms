def isSymmetric(root):
    if not root: return True
    def help(l, r):
        if not l and not r: return True
        if not l or not r or l.val != r.val: return False
        return help(l.left, r.right) and help(l.right, r.left)
    return help(root.left, root.right)
    