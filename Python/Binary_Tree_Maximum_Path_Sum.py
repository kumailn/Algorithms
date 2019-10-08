def maxPathSum(root: TreeNode) -> int:
    maxSum = float('-inf')
    
    def maxChildrenSum(root):
        nonlocal maxSum 
        
        # If we land on a null node we can return 0 safely because
        # we know that it will not contribute to the sum of the root
        if not root: return 0
        
        # Now we need to compute the sums of the left and right children
        # if the sums of either children is less than 0 we know it'll drag down the total
        # sum of our path, so we can just omit that child and take 0 instead of it's sum
        left = max(maxChildrenSum(root.left), 0)
        right = max(maxChildrenSum(root.right), 0)
        
        # If the path we just computed (ie the path with the current node as root) happens to
        # have a bigger sum than the biggest one we've seen, it becomes our new biggest
        maxSum = max(maxSum, left + root.val + right)
        
        # We return the sum of our current node plus the biggest gain on left or the right
        # we don't take both the left and right sums because we are looking for an end to
        # end path and so cannot traverse down both subtrees
        return root.val + max(left, right)
    
    maxChildrenSum(root)
    return maxSum