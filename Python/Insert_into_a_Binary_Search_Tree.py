def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        original = root
        
        last = None
        while root:
            last = root
            if root.val > val: root = root.left
            else: root = root.right
                
        if last.val > val: last.left = TreeNode(val)
        else: last.right = TreeNode(val)
        
        return original