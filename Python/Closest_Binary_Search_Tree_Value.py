# Question: Find the closest element to a given target in a tree
# Solution: Conduct a simple BST search but update the closest whenever the absloute difference is smaller
# Difficulty: Easy

def closestValue(root: TreeNode, target: float) -> int:

    # Initialize closest to infinity so its greater than any node
    closest = float('inf')

    while root:

        # Every time we come across a node that has a smaller absloute difference than our
        # target, we update closest with that nodes value
        if abs(closest - target) > abs(root.val - target):
            closest = root.val
        
        # Go to the left child if the current node is greater than the target, otherwise the right child
        root = root.left if root.val > target else root.right

    return closest