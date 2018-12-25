from _DATATYPES import TreeNode
#Question: Given the root node of a tree, traverse it in order and return it as a list
#Solution: Run a DFS, keep going left if it exists, add node to list, keep going right if it exists
#Difficulty: Easy

#First method, go left and right if children exist
def inOrder(root, order=[]):
    #If the left child of the current node exists, run the function on the left child
    if root.left: inOrder(root.left, order)
    #Add the current node to our list, note this would first happen when we have gone to the leftmost child (ie the smallest)
    order.append(root.val)
    #Run the function on the right child if it exists
    if root.right: inOrder(root.right, order)
    #Return our list
    return order

#Second method, go left and right always, keep a check at the top if root exists
def inOrder2(root, order=[]):
    if not root: return 
    inOrder2(root.left, order)
    order.append(root.val)
    inOrder2(root.right, order)
    return order

def main():
    a = TreeNode(5)
    a.left = TreeNode(3)
    a.left.right = TreeNode(4)
    a.right = TreeNode(7)
    a.right.right = TreeNode(12)

    print(inOrder(a))
    print(inOrder2(a))
main()