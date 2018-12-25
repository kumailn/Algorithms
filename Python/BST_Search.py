#Question: Given a BST and a value to find, find the node with that value
#Solution: Simple BST tree traversal
#Difficulty: Easy

def searchBST(root, val):
        #As long as the current node is not null, and its value is not the value we're looking for
        while root and val != root.val:
            #Move to left child node if the value we're looking for is less than current nodes value, else to right child node
            root = root.left if val < root.val else root.right
        #Return the node we stop at
        return root