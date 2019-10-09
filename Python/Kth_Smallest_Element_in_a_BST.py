
# Question: Given the root node of a tree, find the nth smallest element in the tree
# Solution: Traverse in order iteratively and keep track of the nth smallest element 
# Difficulty: Easy


def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        val = None
        
        # Iterative in order travesal, keep track of K
        while (stack or root) and k != 0:
            while root:
                stack += [root]
                root = root.left

            # Every time we pop something from the stack we know that it's ordered
            # so subtract 1 from k and set out value to be that nodes value
            root = stack.pop()
            k -= 1
            val = root.val

            # Shift node to its right child normally 
            root = root.right
            
        return val