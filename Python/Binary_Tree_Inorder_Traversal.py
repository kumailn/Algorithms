# Question: Given the root node of a tree, traverse it in order and return it as a list
# Solution: Keep track of nodes through a stack and a pointer to the root
# Difficulty: Easy

def inorderTraversal(root: TreeNode) -> List[int]:
        stack = []
        order = []
        
        # As long as we have either something in the stack or a non null node
        while root or stack:
            
            # As long as the roots not null, keep going to the left child
            while root:
                stack += [root]
                root = root.left
            
            # Get the top node in the stack and pop it, this node is in order
            # so append its value to our results
            root = stack.pop()
            order += [root.val]
            
            # Now move the current root to the right 
            root = root.right