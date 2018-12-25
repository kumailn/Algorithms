#Question: Given a trees root, and a number, determine if any path in that tree sums to the given number
#Solution: 

def hasPathSum(root, sum):
        #Keep track of all the sums
        sums = []
        #Define a helper that takes into account the sum of the current path
        def helper(root, pathSum, sums):
            #If our node is null return nothing
            if not root: return
            #If the node is a leaf child, we have reached a sum path, append the current sum to the sums list
            if not root.left and not root.right: sums.append(pathSum + root.val)
            #If the left or right children exist, then recursively go into them and update the current paths sum with their values
            if root.left: helper(root.left, pathSum + root.val, sums)
            if root.right: helper(root.right, pathSum + root.val, sums)
        #Run the helper function on th given root with the given sum
        helper(root, 0, sums)
        #Return true if the given sum exists in our sums list, else return false
        return sum in sums
    