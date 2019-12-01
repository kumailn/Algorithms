# Question (#1110): Given the root of a binary tree, After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees). 
#                   Return the roots of the trees in the remaining forest.  You may return the result in any order.
# Solution: Recursively traverse through the tree and keep track of parents, after deleting a node, a given node is the head of the forest
#           if it has no parent node.

def delNodes(root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

    # Our recursive helper function
    def delNode(root, parent, to_delete, forest):
        # If we get to a None node, return None
        if not root: return root

        # If the current node is one we want to delete, we need to traverse down it's subtrees
        # and delete other nodes before we delete this one. Once we have finished our recursion,
        # delete the current node by returning None to its parent.
        if root.val in to_delete:
            # Set it's left and right nodes to be recursive calls to our helper, we need to set the parent in our
            # recursive call to None as the current Node will be deleted and will no longer be a parent.
            root.left = delNode(root.left, None, to_delete, forest)
            root.right = delNode(root.right, None, to_delete, forest)
            return None

        # Otherwise, if we don't want to delete this node, recursively call our helper in it's subtrees
        root.left = delNode(root.left, root, to_delete, forest)
        root.right = delNode(root.right, root, to_delete, forest)

        #Finally, if the node we're currently at has no parent, then add it to our forest
        if not parent: forest += [root]
        return root
            
    forest = []
    delNode(root, None, to_delete, forest)
    return forest